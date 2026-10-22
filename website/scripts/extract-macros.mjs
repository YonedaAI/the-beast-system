// Step 2: collect every \newcommand, \renewcommand and \DeclareMathOperator from the paper preambles
// into website/lib/macros.json (KaTeX macro map).
import fs from 'node:fs';
import path from 'node:path';
import { SLUGS } from './series.mjs';

const root = path.resolve(process.argv[2] || '.');
const macros = {};
const seen = {};
const conflicts = [];

function group(s, i) {
  let d = 0;
  for (let j = i; j < s.length; j++) {
    if (s[j] === '\\') { j++; continue; }
    if (s[j] === '{') d++;
    else if (s[j] === '}' && --d === 0) return j;
  }
  throw new Error('unbalanced');
}

for (const slug of SLUGS) {
  const tex = fs.readFileSync(path.join(root, 'papers', 'latex', `${slug}.tex`), 'utf8');
  const pre = tex.slice(0, tex.indexOf('\\begin{document}'));
  const re = /\\(newcommand|renewcommand|providecommand|DeclareMathOperator)(\*?)\s*\{?(\\[A-Za-z]+)\}?(\[\d\])?\s*\{/g;
  let m;
  while ((m = re.exec(pre))) {
    const [, kind, star, name, nargs] = m;
    const start = m.index + m[0].length - 1;
    const end = group(pre, start);
    let body = pre.slice(start + 1, end).trim();
    if (kind === 'DeclareMathOperator') body = `\\operatorname${star}{${body}}`;
    (seen[name] ||= new Set()).add(body);
    if (!(name in macros)) macros[name] = body;
    else if (macros[name] !== body) conflicts.push(`${name} (${slug}): ${body} vs ${macros[name]}`);
  }
}
const out = Object.fromEntries(Object.entries(macros).sort());
fs.writeFileSync(path.join(root, 'website', 'lib', 'macros.json'), JSON.stringify(out, null, 2) + '\n');
console.log(`macros: ${Object.keys(out).length} unique names (${conflicts.length} cross-paper redefinitions)`);
for (const c of conflicts) console.log('  conflict', c);
