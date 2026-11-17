#!/usr/bin/env bash
# Build every volume, then synchronise the page counts in the document-set blocks.
# Usage: ./build/build_all.sh
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

docs=(
  00_Overview_and_Map.md
  G1-3_Foundations.md
  G4-6_Rules_and_Search.md
  G7-9_Critique.md
  G10-12_Judgement.md
  T4_CS_Logical_Thinking_and_Logic_Programming.md
  T4_GEN_Logic_Evidence_and_Machines.md
  Adult_PostCollege.md
)

build() {
  ./build/build.sh "$1" >/dev/null
  echo "built $1"
}

for d in "${docs[@]}"; do build "$d"; done
python3 build/update_docset.py

# Rebuild so the page counts written into each volume are the counts of the
# PDF that contains them. Repeat once if the block itself changed pagination.
for d in "${docs[@]}"; do build "$d"; done
out="$(python3 build/update_docset.py)"
if [[ "$out" != "updated: nothing" ]]; then
  for d in "${docs[@]}"; do build "$d"; done
  python3 build/update_docset.py
fi

echo
echo "Final page counts:"
for d in "${docs[@]}"; do
  base="${d%.md}"
  pages=$(pdfinfo "$base.pdf" | awk '/^Pages/{print $2}')
  printf '  %-52s %s pages\n' "$base.pdf" "$pages"
done
