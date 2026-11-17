#!/usr/bin/env bash
# Install the toolchain needed to rebuild the curriculum PDFs.
#
# Supported: Debian, Ubuntu and WSL2 with an Ubuntu distribution.
# For macOS, Fedora and native Windows, follow the instructions in README.md.
#
# Usage:
#   ./setup.sh
#
# The script needs sudo if it is not already running as root.

set -euo pipefail

if ! command -v apt-get >/dev/null 2>&1; then
  cat >&2 <<'EOF'
This installer supports Debian/Ubuntu only.

macOS:   install MacTeX, poppler, Python 3, Lato and DejaVu Sans Mono; see README.md.
Fedora:  install the TeX Live LaTeX collections, poppler-utils, Python 3 and the fonts; see README.md.
Windows: use WSL2 with Ubuntu and run this script inside it; see README.md.
EOF
  exit 1
fi

if [[ ${EUID} -eq 0 ]]; then
  SUDO=""
else
  SUDO="sudo"
fi

echo "Updating package lists..."
${SUDO} apt-get update

echo "Installing TeX Live, fonts and PDF tools..."
${SUDO} apt-get install -y --no-install-recommends \
  texlive-luatex \
  texlive-latex-recommended \
  texlive-latex-extra \
  texlive-fonts-recommended \
  fonts-lato \
  fonts-dejavu-core \
  fontconfig \
  poppler-utils \
  python3

# Newer Debian and Ubuntu releases split the DejaVu families into
# separate packages. Install the monospaced family when it exists.
${SUDO} apt-get install -y --no-install-recommends fonts-dejavu-mono 2>/dev/null || true

echo
echo "Checking the installation..."

status=0
for tool in lualatex python3 pdfinfo; do
  if command -v "$tool" >/dev/null 2>&1; then
    printf '  %-10s %s\n' "$tool" "$(command -v "$tool")"
  else
    printf '  %-10s MISSING\n' "$tool"
    status=1
  fi
done

for font in Lato "DejaVu Sans Mono"; do
  match=$(fc-match -f '%{family}: %{file}' "$font" 2>/dev/null || true)
  printf '  font       %s -> %s\n' "$font" "$match"
done

echo
if [[ $status -eq 0 ]]; then
  echo "Ready. Rebuild the set with:"
  echo "  ./build/build_all.sh"
else
  echo "Some tools are missing. Read the messages above and see README.md." >&2
fi

exit $status
