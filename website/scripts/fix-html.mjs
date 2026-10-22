// Steps 3 and 4: raw-LaTeX sweep and structure fixer for the pandoc HTML.
// Reads docs/papers/<slug>.html, writes website/content/<slug>.html and website/papers.json.
// Usage: node fix-html.mjs <repoRoot>
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { SERIES, SLUGS } from './series.mjs';

const require = createRequire(import.meta.url);
const cheerio = require('cheerio');

const root = path.resolve(process.argv[2] || '.');
const outDir = path.join(root, 'website', 'content');
fs.mkdirSync(outDir, { recursive: true });

const THM = ['theorem', 'proposition', 'lemma', 'corollary', 'definition', 'assumption', 'remark', 'example'];
const cap = (s) => s[0].toUpperCase() + s.slice(1);
const PLURAL = { Corollary: 'Corollaries' };
const plural = (t) => PLURAL[t] || t + 's';
const stats = {};
const bump = (slug, k, n = 1) => {
  stats[slug] ||= {};
  stats[slug][k] = (stats[slug][k] || 0) + n;
};
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const docs = {};
const index = {}; // slug -> { id -> {type,num} }

function load(slug) {
  const html = fs.readFileSync(path.join(root, 'docs', 'papers', `${slug}.html`), 'utf8');
  return cheerio.load(html, null, false);
}

// Pass 1: numbering in LaTeX style (theorem counter shared and reset per section).
for (const slug of SLUGS) {
  const $ = load(slug);
  docs[slug] = $;
  const idx = (index[slug] = {});
  let sec = 0;
  let c = 0;
  let eq = 0;
  let tab = 0;
  let fig = 0;
  $('h1, h2, h3, div, table, figure, span.math.display').each((_, el) => {
    const $e = $(el);
    const tag = el.tagName;
    if (tag === 'h1' || tag === 'h2' || tag === 'h3') {
      const num = $e.attr('data-number');
      if (tag === 'h1') { sec = parseInt(num, 10); c = 0; }
      if ($e.attr('id') && num) idx[$e.attr('id')] = { type: 'Section', num };
    } else if (tag === 'div') {
      const cls = THM.find((t) => $e.hasClass(t));
      if (cls) {
        c++;
        const num = `${sec}.${c}`;
        $e.attr('data-num', num);
        $e.attr('data-type', cap(cls));
        if ($e.attr('id')) idx[$e.attr('id')] = { type: cap(cls), num };
      }
    } else if (tag === 'table') {
      tab++;
      $e.attr('data-num', String(tab));
      if ($e.attr('id')) idx[$e.attr('id')] = { type: 'Table', num: String(tab) };
    } else if (tag === 'figure') {
      fig++;
      $e.attr('data-num', String(fig));
      if ($e.attr('id')) idx[$e.attr('id')] = { type: 'Figure', num: String(fig) };
    } else if (tag === 'span') {
      const t = $e.text();
      if (/\\begin\{equation\}/.test(t)) {
        eq++;
        $e.attr('data-num', String(eq));
        const m = t.match(/\\label\{([^}]+)\}/);
        if (m) idx[m[1]] = { type: 'Equation', num: String(eq) };
      }
    }
  });
}

const slugOfRoman = Object.fromEntries(SERIES.map((s) => [s.roman, s.slug]));

function walkText($, scope, fn, skip) {
  const visit = (node) => {
    if (node.type === 'text') { fn(node); return; }
    if (node.type !== 'tag' && node.type !== 'root') return;
    if (node.type === 'tag' && skip(node)) return;
    for (const ch of [...(node.children || [])]) visit(ch);
  };
  scope.each((_, n) => visit(n));
}

function refHtml(slug, ids, kind) {
  const idx = index[slug];
  const items = ids.map((id) => ({ id, ...(idx[id] || {}) }));
  if (items.some((i) => !i.type)) {
    bump(slug, 'unresolvedRefs', items.filter((i) => !i.type).length);
    items.forEach((i) => { if (!i.type) { i.type = 'Section'; i.num = '?'; } });
  }
  const fmt = (i) => (i.type === 'Equation' ? `(${i.num})` : i.num);
  const link = (i, text) => `<a class="xref" href="#${esc(i.id)}">${esc(text)}</a>`;
  if (kind === 'ref' || kind === 'eqref') {
    return items.map((i) => link(i, fmt(i))).join(', ');
  }
  // cleveref style: group consecutive items of the same type
  const groups = [];
  for (const i of items) {
    const g = groups[groups.length - 1];
    if (g && g.type === i.type) g.items.push(i);
    else groups.push({ type: i.type, items: [i] });
  }
  const parts = groups.map((g) => {
    const name = g.items.length > 1 ? plural(g.type) : g.type;
    const nums = g.items.map((i) => link(i, fmt(i)));
    const list = nums.length === 2 ? `${nums[0]} and ${nums[1]}` : nums.length > 2 ? `${nums.slice(0, -1).join(', ')}, and ${nums.at(-1)}` : nums[0];
    return `${name} ${list}`;
  });
  return parts.length === 2 ? `${parts[0]} and ${parts[1]}` : parts.length > 2 ? `${parts.slice(0, -1).join(', ')}, and ${parts.at(-1)}` : parts[0];
}

const TYPE_RE = '(Theorems?|Propositions?|Lemma|Corollary|Definition|Assumption|Remark|Example|Section|Table|Figure)';

for (const slug of SLUGS) {
  const $ = docs[slug];

  // headings: h1 sections become h2 so the page title is the only h1
  for (const [from, to] of [['h3', 'h4'], ['h2', 'h3'], ['h1', 'h2']]) {
    $(from).each((_, el) => { el.tagName = to; });
  }

  // math: normalize equation environments and add tags
  $('span.math').each((_, el) => {
    const $e = $(el);
    let t = $e.text();
    const display = $e.hasClass('display');
    t = t.replace(/^\\[\(\[]\s*/, '').replace(/\s*\\[\)\]]$/, '');
    const lab = t.match(/\\label\{([^}]*)\}/);
    if (lab && display) $e.attr('id', lab[1].trim());
    t = t.replace(/\\label\{[^}]*\}/g, '');
    const num = $e.attr('data-num');
    t = t.replace(/\\begin\{equation\}/, '').replace(/\\end\{equation\}/, '').trim();
    if (num) t += ` \\tag{${num}}`;
    $e.text(display ? `\\[${t}\\]` : `\\(${t}\\)`);
    $e.removeAttr('data-num');
  });
  const lbl = {};
  void lbl;

  // theorem-like blocks
  $('div[data-type]').each((_, el) => {
    const $e = $(el);
    const type = $e.attr('data-type');
    const num = $e.attr('data-num');
    const first = $e.children('p').first();
    let inner = first.html() || '';
    let name = '';
    const m = inner.match(/^<(?:strong|em)>[A-Za-z]+ \d+<\/(?:strong|em)>(?: \(([\s\S]*?)\)\.)?\s*/);
    if (m) { name = m[1] || ''; inner = inner.slice(m[0].length); }
    else bump(slug, 'thmHeadMissing');
    const head = `<p class="thm-head"><span class="thm-label">${type} ${num}</span>${name ? `<span class="thm-name">${name}</span>` : ''}</p>`;
    first.replaceWith(head + (inner.trim() ? `<p>${inner}</p>` : ''));
    $e.addClass('thm').addClass(`thm-${type.toLowerCase()}`);
    if (!$e.attr('id')) $e.attr('id', `${type.toLowerCase()}-${num.replace('.', '-')}`);
    $e.removeAttr('data-type').removeAttr('data-num');
    bump(slug, 'blocks');
  });

  // references
  $('a[data-reference]').each((_, el) => {
    const $e = $(el);
    const ids = $e.attr('data-reference').split(',').map((s) => s.trim());
    const kind = $e.attr('data-reference-type') || 'ref+label';
    $e.replaceWith(refHtml(slug, ids, kind.startsWith('ref+') ? 'cref' : kind));
    bump(slug, 'refs');
  });

  // tables
  $('table').each((_, el) => {
    const $e = $(el);
    const num = $e.attr('data-num');
    $e.removeAttr('data-num');
    const capEl = $e.children('caption');
    if (capEl.length) capEl.prepend(`<span class="cap-label">Table ${num}.</span> `);
    $e.wrap(`<div class="table-scroll" role="region" aria-label="Table ${num}" tabindex="0"></div>`);
    bump(slug, 'tables');
  });

  // figures
  $('figure').each((_, el) => {
    const $e = $(el);
    const num = $e.attr('data-num');
    const capEl = $e.children('figcaption');
    const altEl = capEl.clone();
    altEl.find('span.math').each((_, m) => {
      $(m).replaceWith($(m).text().replace(/^\\[(\[]|\\[)\]]$/g, '').replace(/\\[a-zA-Z]+/g, '').replace(/[{}^_]/g, ''));
    });
    const alt = altEl.text().trim();
    capEl.prepend(`<span class="cap-label">Figure ${num}.</span> `);
    $e.find('img').attr('alt', alt).attr('loading', 'lazy');
    $e.removeAttr('data-latex-placement').removeAttr('data-num');
    bump(slug, 'figures');
  });

  // drop empty anchors (focusable, unnamed)
  $('a').each((_, el) => {
    const $e = $(el);
    if (!$e.text().trim() && !$e.find('img, svg').length) { $e.remove(); bump(slug, 'emptyAnchorsRemoved'); }
  });

  // bibliography
  $('div.thebibliography').each((_, el) => {
    const $e = $(el);
    $e.children('p').first().remove();
    $e.children('p').each((i, p) => {
      const $p = $(p);
      $p.attr('id', `bib-${i + 1}`);
      walkText($, $p, (node) => {
        const t = esc(node.data);
        const out = t.replace(/doi:(10\.[^\s<]+?)(\.?)(?=\s|$)/g, '<a href="https://doi.org/$1">doi:$1</a>$2');
        if (out !== t) $(node).replaceWith(out);
      }, (n) => n.name === 'a');
    });
    $e.attr('class', 'bibliography');
    $e.before('<h2 id="references"><span class="header-section-number"></span>References</h2>');
    bump(slug, 'bibEntries', $e.children('p').length);
  });
  $('div.small').each((_, el) => { $(el).replaceWith($(el).contents()); });

  // raw LaTeX sweep and cross-Part links in text nodes
  const sweepCounts = {};
  const countSweep = (k) => { sweepCounts[k] = (sweepCounts[k] || 0) + 1; };
  const skipSweep = (node) =>
    (node.name === 'span' && /\bmath\b/.test(node.attribs?.class || '')) || node.name === 'code' || node.name === 'pre';
  walkText($, $.root(), (node) => {
    let s = node.data;
    if (!/[\\$]/.test(s)) return;
    const orig = s;
    s = esc(s);
    const math = (tex, disp) => {
      countSweep('math');
      return `<span class="math ${disp ? 'display' : 'inline'}">${disp ? '\\[' : '\\('}${tex}${disp ? '\\]' : '\\)'}</span>`;
    };
    s = s.replace(/\$\$([\s\S]+?)\$\$/g, (_, t) => math(t, true));
    s = s.replace(/\\\[([\s\S]+?)\\\]/g, (_, t) => math(t, true));
    s = s.replace(/\\\(([\s\S]+?)\\\)/g, (_, t) => math(t, false));
    s = s.replace(/\$([^$\n]+?)\$/g, (m, t) => (/[\\^_{}=]/.test(t) ? math(t, false) : m));
    s = s.replace(/\\(?:emph|textit)\{([^{}]*)\}/g, (_, t) => (countSweep('emph'), `<em>${t}</em>`));
    s = s.replace(/\\textbf\{([^{}]*)\}/g, (_, t) => (countSweep('textbf'), `<strong>${t}</strong>`));
    s = s.replace(/\\texttt\{([^{}]*)\}/g, (_, t) => (countSweep('texttt'), `<code>${t}</code>`));
    s = s.replace(/\\(?:[Cc]ref|ref|eqref|label)\{([^{}]*)\}/g, (_, ids) => {
      countSweep('ref');
      return refHtml(slug, ids.split(',').map((x) => x.trim()), 'cref');
    });
    s = s.replace(/\\cite[a-z]*\{[^{}]*\}/gi, () => (countSweep('cite'), ''));
    if (s !== esc(orig)) $(node).replaceWith(s);
  }, skipSweep);
  for (const [k, v] of Object.entries(sweepCounts)) bump(slug, `swept_${k}`, v);

  // cross-Part links
  const partRe = new RegExp(`\\bPart (VII|VI|IV|V|III|II|I)\\b(?:(, | )${TYPE_RE} (\\d+(?:\\.\\d+)*))?`, 'g');
  walkText($, $.root(), (node) => {
    const s = node.data;
    if (!/Part [IVX]/.test(s)) return;
    let changed = false;
    const out = esc(s).replace(partRe, (m, roman, sep, type, num) => {
      const target = slugOfRoman[roman];
      let hash = '';
      if (type) {
        const t = type.replace(/s$/, '').replace('Lemma', 'Lemma');
        const key = Object.entries(index[target]).find(([, v]) => v.type === t && v.num === num);
        if (key) hash = `#${key[0]}`;
        else bump(slug, 'crossPartUnmatched');
      }
      changed = true;
      bump(slug, 'crossPartLinks');
      return `<a class="xpart" href="/papers/${target}/${hash}">${m}</a>`;
    });
    if (changed) $(node).replaceWith(out);
  }, (n) => skipSweep(n) || n.name === 'a' || /^h[1-6]$/.test(n.name) || (n.attribs?.class || '') === 'bibliography');

  // "Definition 2.5 of Long (2026f)" -> link straight to the target block
  const ofRe = new RegExp(`${TYPE_RE} (\\d+(?:\\.\\d+)*) of $`);
  $('a[href^="/papers/"]').each((_, el) => {
    const $e = $(el);
    const href = $e.attr('href');
    if (href.includes('#')) return;
    const prev = el.prev;
    if (!prev || prev.type !== 'text') return;
    const m = prev.data.match(ofRe);
    if (!m) return;
    const target = href.split('/')[2];
    const t = m[1].replace(/s$/, '');
    const hit = Object.entries(index[target] || {}).find(([, v]) => v.type === t && v.num === m[2]);
    if (hit) { $e.attr('href', `${href}#${hit[0]}`); bump(slug, 'ofLinks'); }
  });

  const html = $.html();
  fs.writeFileSync(path.join(outDir, `${slug}.html`), html);
  const left = (html.replace(/<span class="math[^]*?<\/span>/g, '').match(/\\(frac|mathcal|mathsf|textbf|emph|cite\w*|ref|cref|Cref)\b|\$\$/g) || []).length;
  bump(slug, 'rawLeftovers', left);
}

// manifest
function pdfPath(slug) {
  const a = path.join(root, 'papers', 'pdf', `${slug}.pdf`);
  return fs.existsSync(a) ? a : path.join(root, 'papers', 'latex', `${slug}.pdf`);
}
function pages(slug) {
  try {
    const out = execFileSync('pdfinfo', [pdfPath(slug)], { encoding: 'utf8' });
    return parseInt(out.match(/Pages:\s+(\d+)/)[1], 10);
  } catch {
    return 0;
  }
}
const pand = (tex, to) =>
  execFileSync('pandoc', ['-f', 'latex-smart', '-t', to, '--wrap=none'], { input: tex, encoding: 'utf8' }).trim();

const manifest = SERIES.map((s) => {
  const tex = fs.readFileSync(path.join(root, 'papers', 'latex', `${s.slug}.tex`), 'utf8');
  const abs = tex.match(/\\begin\{abstract\}([\s\S]*?)\\end\{abstract\}/)[1].trim();
  const abstract = pand(abs, 'plain').replace(/\s+/g, ' ');
  const refs = (tex.match(/\\bibitem/g) || []).length;
  return {
    slug: s.slug,
    part: s.part,
    pillar: s.pillar,
    color: s.color,
    title: s.title,
    subtitle: s.subtitle,
    question: s.question,
    abstract,
    abstractHtml: pand(abs, 'html5'),
    pages: pages(s.slug),
    references: refs,
    date: 'October 2026',
    pdf: `/pdf/${s.slug}.pdf`,
    cover: `/images/${s.slug}.jpg`,
    coverCard: `/images/${s.slug}-card.jpg`,
    category: 'econ.GN',
    hasCode: true,
  };
});
fs.writeFileSync(path.join(root, 'website', 'papers.json'), JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(path.join(root, 'website', 'content', 'fix-stats.json'), JSON.stringify(stats, null, 2) + '\n');
console.log(JSON.stringify(stats, null, 1));
