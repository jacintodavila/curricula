#!/usr/bin/env bash
# Report page counts and common build defects for the eight teaching volumes.
#
# Usage:
#   ./build/check.sh
#
# Exits non-zero if a PDF is missing, contains unresolved references, or the
# LaTeX log reports an overfull box. These are the three failures that matter
# in this set; warnings about fonts or minor spacing are not treated as fatal.

set -uo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

docs=(
  00_Overview_and_Map
  G1-3_Foundations
  G4-6_Rules_and_Search
  G7-9_Critique
  G10-12_Judgement
  T4_CS_Logical_Thinking_and_Logic_Programming
  T4_GEN_Logic_Evidence_and_Machines
  Adult_PostCollege
)

printf '%-52s %8s %12s %9s\n' "document" "pages" "unresolved" "overfull"
printf '%-52s %8s %12s %9s\n' "--------" "-----" "----------" "--------"

fail=0
for base in "${docs[@]}"; do
  pdf="$base.pdf"
  if [[ ! -f "$pdf" ]]; then
    printf '%-52s %8s %12s %9s\n' "$base.pdf" "missing" "-" "-"
    fail=1
    continue
  fi

  pages=$(pdfinfo "$pdf" | awk '/^Pages/{print $2}')
  unresolved=$(pdftotext "$pdf" - 2>/dev/null | grep -c '??' || true)

  overfull=0
  if [[ -f "build/$base.log" ]]; then
    overfull=$(grep -c 'Overfull' "build/$base.log" || true)
  fi

  printf '%-52s %8s %12s %9s\n' "$base.pdf" "$pages" "$unresolved" "$overfull"

  if [[ "$unresolved" -ne 0 || "$overfull" -ne 0 ]]; then
    fail=1
  fi
done

echo
python3 - <<'PY'
import re
import sys

sources = [
    "00_Overview_and_Map.md",
    "G1-3_Foundations.md",
    "G4-6_Rules_and_Search.md",
    "G7-9_Critique.md",
    "G10-12_Judgement.md",
    "T4_CS_Logical_Thinking_and_Logic_Programming.md",
    "T4_GEN_Logic_Evidence_and_Machines.md",
    "Adult_PostCollege.md",
]

blocks = {}
for name in sources:
    try:
        text = open(name, encoding="utf8").read()
    except OSError:
        print(f"document-set check: cannot read {name}")
        sys.exit(1)
    match = re.search(r"<!-- docset:start -->(.*?)<!-- docset:end -->", text, re.S)
    blocks[name] = match.group(1).strip() if match else None

if any(block is None for block in blocks.values()):
    print("document-set check: one or more files lack the docset markers")
    sys.exit(1)

first = blocks[sources[0]]
if all(block == first for block in blocks.values()):
    print("document-set check: all eight blocks agree")
else:
    differing = [name for name, block in blocks.items() if block != first]
    print("document-set check: blocks differ in " + ", ".join(differing))
    print("run: python3 build/update_docset.py, then rebuild the volumes it names")
    sys.exit(1)
PY

if [[ $fail -ne 0 ]]; then
  echo
  echo "One or more checks failed. See build/<name>.log for the LaTeX transcript." >&2
fi

exit $fail
