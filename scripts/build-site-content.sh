#!/usr/bin/env bash
# Rebuilds all website content from papers/latex/*.tex: pandoc, macro map, raw-LaTeX sweep, structure fixer,
# then copies PDFs, covers and HTML into website/. Run from anywhere; re-run after any .tex change.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
SLUGS="financial-power political-power judicial-power ideological-power coercive-power productive-power formalized-state"
S="$ROOT/website/scripts"

mkdir -p docs/papers docs/.build website/public/pdf website/public/images website/content

echo "== 0. prepare tex (tabularx, citations, tikz figures)"
node "$S/prep-tex.mjs" "$ROOT"

echo "== 1. pandoc"
for s in $SLUGS; do
  pandoc "docs/.build/$s.tex" --to html5 --mathjax --toc --toc-depth=3 --number-sections --no-highlight --wrap=none -o "docs/papers/$s.html" 2> >(grep -v Deprecated >&2 || true)
done

echo "== 2. KaTeX macro map"
node "$S/extract-macros.mjs" "$ROOT"

echo "== 3-4. raw-LaTeX sweep, structure, manifest"
node "$S/fix-html.mjs" "$ROOT"

echo "== 5. PDFs and covers"
for s in $SLUGS; do
  if [ -f "papers/pdf/$s.pdf" ]; then src="papers/pdf/$s.pdf"; else src="papers/latex/$s.pdf"; fi
  cp "$src" "website/public/pdf/$s.pdf"
  pdftocairo -jpeg -jpegopt quality=82 -r 110 -f 1 -l 1 -singlefile "$src" "website/public/images/$s"
  pdftocairo -jpeg -jpegopt quality=80 -scale-to-x 640 -scale-to-y -1 -f 1 -l 1 -singlefile "$src" "website/public/images/$s-card"
done
echo "done: $(ls website/content/*.html | wc -l) papers"
