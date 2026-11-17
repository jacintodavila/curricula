#!/usr/bin/env bash
# Rebuild a curriculum PDF from its Markdown source.
# Usage:
#   ./build/build.sh Curriculum_Plan_Logic_Programming.md
#   ./build/build.sh T4_CS_Logical_Thinking_and_Logic_Programming.md
#   ./build/build.sh T4_GEN_Logic_Evidence_and_Machines.md
set -euo pipefail

src="${1:?usage: build.sh <source.md>}"
[[ "$src" == *.md ]] || { echo "source must end in .md"; exit 1; }

root="$(cd "$(dirname "$0")/.." && pwd)"
base="$(basename "$src" .md)"

cd "$root"
python3 build/md2tex.py "$src" "build/$base.tex"

cd build
lualatex -interaction=nonstopmode "$base.tex" > "$base.log" 2>&1 || true
lualatex -interaction=nonstopmode "$base.tex" > "$base.log" 2>&1 || true

if [[ ! -f "$base.pdf" ]]; then
  echo "FAILED: no PDF produced. Last errors:" >&2
  grep -E '^!' "$base.log" | head -10 >&2
  exit 1
fi

cd "$root"
cp "build/$base.pdf" "$base.pdf"
pages=$(pdfinfo "$base.pdf" | awk '/^Pages/{print $2}')
echo "OK: $base.pdf ($pages pages)"
