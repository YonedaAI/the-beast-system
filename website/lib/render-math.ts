// Build-time math: replaces LaTeX delimiters in an HTML string with KaTeX markup.
import katex from 'katex';
import extracted from './macros.json';

// Macros extracted from the \newcommand / \DeclareMathOperator lines of all seven preambles
// (scripts/extract-macros.mjs), plus a few notation helpers.
export const MACROS: Record<string, string> = {
  '\\slashed': '\\not{#1}',
  '\\bra': '\\langle #1|',
  '\\ket': '|#1\\rangle',
  '\\braket': '\\langle #1\\rangle',
  '\\Hom': '\\operatorname{Hom}',
  '\\Tr': '\\operatorname{Tr}',
  '\\Lan': '\\operatorname{Lan}',
  '\\Ran': '\\operatorname{Ran}',
  ...(extracted as Record<string, string>),
};

function unescapeHtml(s: string) {
  return s
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&amp;/g, '&');
}

function render(tex: string, displayMode: boolean) {
  return katex.renderToString(tex, {
    displayMode,
    throwOnError: false,
    trust: true,
    strict: 'ignore',
    macros: { ...MACROS },
  });
}

export function renderMath(html: string): string {
  // pandoc output: <span class="math inline">\( ... \)</span>
  let out = html.replace(
    /<span class="math (inline|display)"([^>]*)>\\[(\[]([\s\S]*?)\\[)\]]<\/span>/g,
    (_, kind: string, attrs: string, tex: string) => {
      const display = kind === 'display';
      const rendered = render(unescapeHtml(tex), display);
      return display ? `<div class="math-display"${attrs}>${rendered}</div>` : rendered;
    },
  );
  // any remaining bare delimiters
  out = out.replace(/\$\$([\s\S]+?)\$\$/g, (_, t: string) => render(unescapeHtml(t), true));
  out = out.replace(/\\\[([\s\S]+?)\\\]/g, (_, t: string) => render(unescapeHtml(t), true));
  out = out.replace(/\\\(([\s\S]+?)\\\)/g, (_, t: string) => render(unescapeHtml(t), false));
  return out;
}
