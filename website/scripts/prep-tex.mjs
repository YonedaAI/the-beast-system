// Step 0: prepare each .tex for pandoc.
//  - tabularx -> tabular (pandoc drops tabularx)
//  - natbib citations -> author-year text (links to sibling Parts)
//  - tikz figures -> SVG files in public/figures
// Usage: node prep-tex.mjs <repoRoot>
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { SLUGS } from './series.mjs';

const root = path.resolve(process.argv[2] || '.');
const outDir = path.join(root, 'docs', '.build');
const figDir = path.join(root, 'website', 'public', 'figures');
fs.mkdirSync(outDir, { recursive: true });
fs.rmSync(figDir, { recursive: true, force: true });
fs.mkdirSync(figDir, { recursive: true });

const partKey = Object.fromEntries(SLUGS.map((s) => [s, s]));
const keyToSlug = {
  long2026financial: 'financial-power',
  long2026political: 'political-power',
  long2026judicial: 'judicial-power',
  long2026ideological: 'ideological-power',
  long2026coercive: 'coercive-power',
  long2026productive: 'productive-power',
  long2026formalized: 'formalized-state',
};

function matchBrace(s, i) {
  // s[i] === '{'; return index of the matching '}'
  let d = 0;
  for (let j = i; j < s.length; j++) {
    if (s[j] === '\\') { j++; continue; }
    if (s[j] === '{') d++;
    else if (s[j] === '}') { d--; if (d === 0) return j; }
  }
  throw new Error('unbalanced brace');
}

function countCols(spec) {
  let n = 0;
  for (let i = 0; i < spec.length; i++) {
    const c = spec[i];
    if (c === '@' || c === '>' || c === '<' || c === '!') { i = matchBrace(spec, i + 1); continue; }
    if ('LpmbCPR'.includes(c)) { n++; if (spec[i + 1] === '{') i = matchBrace(spec, i + 1); continue; }
    if ('lcrYX'.includes(c)) n++;
  }
  return n;
}

function fixTabularx(tex) {
  let out = '';
  let i = 0;
  const tag = '\\begin{tabularx}';
  while (true) {
    const k = tex.indexOf(tag, i);
    if (k < 0) { out += tex.slice(i); break; }
    out += tex.slice(i, k);
    let p = k + tag.length;
    const wEnd = matchBrace(tex, p); // width arg
    p = wEnd + 1;
    const sEnd = matchBrace(tex, p);
    const spec = tex.slice(p + 1, sEnd);
    out += `\\begin{tabular}{${'l'.repeat(countCols(spec))}}`;
    i = sEnd + 1;
  }
  return out.replaceAll('\\end{tabularx}', '\\end{tabular}');
}

function parseBib(tex) {
  const map = {};
  const re = /\\bibitem\[([^\]]*)\]\{([^}]+)\}/g;
  let m;
  while ((m = re.exec(tex))) {
    const raw = m[1].replace(/[{}]/g, '');
    const par = raw.lastIndexOf('(');
    map[m[2]] = { author: raw.slice(0, par).trim(), year: raw.slice(par + 1, raw.lastIndexOf(')')).trim() };
  }
  return map;
}

function fixCites(tex, bib, slug) {
  const missing = new Set();
  const entry = (k, mode) => {
    const b = bib[k];
    if (!b) { missing.add(k); return k; }
    let txt = mode === 't' ? `${b.author} (${b.year})` : `${b.author} ${b.year}`;
    if (keyToSlug[k]) txt = `\\href{/papers/${keyToSlug[k]}/}{${txt}}`;
    return txt;
  };
  const re = /\\([Cc]ite(?:t|p|alt|alp|author)?)\*?((?:\[[^\]]*\])*)\{([^}]*)\}/g;
  const out = tex.replace(re, (_, cmd, opts, keys) => {
    const o = [...opts.matchAll(/\[([^\]]*)\]/g)].map((x) => x[1]);
    const pre = o.length === 2 ? o[0] : '';
    const post = o.length === 2 ? o[1] : o[0] || '';
    const ks = keys.split(',').map((s) => s.trim());
    const c = cmd.toLowerCase();
    if (c === 'citet') {
      return ks.map((k) => entry(k, 't')).join(', ') + (post ? ` (${post})` : '');
    }
    const body = ks.map((k) => entry(k, 'p')).join('; ');
    const inner = (pre ? pre + ' ' : '') + body + (post ? ', ' + post : '');
    return c === 'citealt' || c === 'citealp' ? inner : `(${inner})`;
  });
  if (missing.size) console.warn(`[${slug}] unresolved cite keys: ${[...missing].join(', ')}`);
  return out;
}

function tikzToSvg(tex, slug) {
  const preambleEnd = tex.indexOf('\\begin{document}');
  const preamble = tex.slice(0, preambleEnd);
  const keep = preamble
    .split('\n')
    .filter((l) => /^\\(usepackage(\[[^\]]*\])?\{(amsmath,amssymb,amsthm|amsmath|amssymb|tikz|xcolor|lmodern)\}|usetikzlibrary|newcommand|DeclareMathOperator|renewcommand\{\\Pr\})/.test(l))
    .join('\n');
  let n = 0;
  const re = /\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}/g;
  return tex.replace(re, (pic) => {
    n++;
    const name = `${slug}-${n}`;
    const work = path.join(outDir, `fig-${name}`);
    fs.mkdirSync(work, { recursive: true });
    fs.writeFileSync(
      path.join(work, 'fig.tex'),
      `\\documentclass[border=6pt]{standalone}\n\\usepackage[T1]{fontenc}\n${keep}\n\\begin{document}\n${pic}\n\\end{document}\n`,
    );
    execFileSync('pdflatex', ['-interaction=nonstopmode', '-halt-on-error', 'fig.tex'], { cwd: work, stdio: 'pipe' });
    execFileSync('pdftocairo', ['-svg', path.join(work, 'fig.pdf'), path.join(figDir, `${name}.svg`)]);
    fs.rmSync(work, { recursive: true, force: true });
    return `\\includegraphics{/figures/${name}.svg}`;
  });
}

for (const slug of SLUGS) {
  let tex = fs.readFileSync(path.join(root, 'papers', 'latex', `${slug}.tex`), 'utf8');
  const bib = parseBib(tex);
  tex = fixCites(tex, bib, slug);
  tex = fixTabularx(tex);
  tex = tikzToSvg(tex, slug);
  fs.writeFileSync(path.join(outDir, `${slug}.tex`), tex);
  console.log(`prep ${slug}: ${Object.keys(bib).length} bib entries`);
}
