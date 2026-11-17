# The Glass Box — a curriculum in logical thinking

This repository holds **The Glass Box**, a curriculum in logical thinking: four school bands, two university courses, an adult course, an overview, and the design archive behind them. Each document is a Markdown source and a PDF built from it.

The argument of the set is one sentence: **the concepts of logical thinking do not change as students get older; their resolution changes.** Grice's Cooperative Principle and the maxims are used both as the editorial standard for the documents and as taught content, from four classroom rules in grades 1–3 to the audit of a machine answer in adult life.

## The documents

| PDF | Source | Pages | Reader |
|---|---|---|---|
| `00_Overview_and_Map.pdf` | `00_Overview_and_Map.md` | 27 | Everyone: which document to open, and why |
| `G1-3_Foundations.pdf` | `G1-3_Foundations.md` | 24 | Teachers of grades 1–3 |
| `G4-6_Rules_and_Search.pdf` | `G4-6_Rules_and_Search.md` | 27 | Teachers of grades 4–6 |
| `G7-9_Critique.pdf` | `G7-9_Critique.md` | 27 | Teachers of grades 7–9 |
| `G10-12_Judgement.pdf` | `G10-12_Judgement.md` | 26 | Teachers of grades 10–12 |
| `T4_CS_Logical_Thinking_and_Logic_Programming.pdf` | matching `.md` | 89 | Computer-science lecturers |
| `T4_GEN_Logic_Evidence_and_Machines.pdf` | matching `.md` | 75 | Lecturers in other disciplines |
| `Adult_PostCollege.pdf` | `Adult_PostCollege.md` | 30 | Trainers, managers, facilitators |
| `Curriculum_Plan_Logic_Programming.pdf` | `Curriculum_Plan_Logic_Programming.md` | 73 | The design archive: stages, gates, pilot plan, figures |

The eight teaching documents are standalone: each contains its year map, unit cards, scripted lessons, assessment, common errors, out-of-bounds list and references. The archive is not required for teaching.

Two supporting sources are kept as Markdown because the documents cite them:

- `An Introduction to Logical Thinking (v2 university).md` — the university sketch, units U0–U9 and capstones C1–C3.
- `Concept_Sequence_Logic_Critical_Thinking.md` — the concept ladder of stages and gates.

## Quick start

Ubuntu, Debian or WSL2:

```bash
git clone https://github.com/jacintodavila/curricula.git
cd curricula
./setup.sh
./build/build_all.sh
```

`setup.sh` installs TeX Live, the two fonts, Python and the PDF tools. `build_all.sh` rebuilds the eight teaching volumes, updates the page counts in every document, and prints the final counts. It takes a few minutes.

To rebuild the archive as well:

```bash
./build/build.sh Curriculum_Plan_Logic_Programming.md
```

Check the result:

```bash
./build/check.sh
```

The PDFs are already committed, so you can read them on GitHub without building anything. Building is for editing.

---

## 1. Install the toolchain

### What the build needs

| Component | Why | Tested with |
|---|---|---|
| LuaLaTeX (TeX Live) | converts the generated `.tex` to PDF | TeX Live 2025, LuaHBTeX 1.22 |
| Python 3 | runs `build/md2tex.py` and the sync scripts | Python 3.14 (3.8+ should work) |
| Lato | body and heading font | `fonts-lato` 2.015 |
| DejaVu Sans Mono | code and inline code font | DejaVu 2.37 |
| `pdfinfo`, `pdftotext` | page counts and the check script | poppler 26.01 |
| Inkscape | optional: regenerates the archive's figures | 1.4 |

The Python scripts use only the standard library. There is no virtual environment, no `pip install`, and no Node toolchain.

### Ubuntu, Debian and WSL2

Run the installer:

```bash
./setup.sh
```

Or install the packages by hand:

```bash
sudo apt-get update
sudo apt-get install -y \
  texlive-luatex texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended fonts-lato fonts-dejavu-core fontconfig \
  poppler-utils python3
```

On releases that split the DejaVu families, also install `fonts-dejavu-mono`. If `fonts-dejavu-core` does not provide the monospaced face, install `fonts-dejavu`.

Ubuntu 22.04 and 24.04, Debian 12 and 13, and WSL2 Ubuntu are the tested routes.

### Fedora

```bash
sudo dnf install -y \
  texlive-collection-latex texlive-collection-latexrecommended \
  texlive-collection-latexextra texlive-collection-fontsrecommended \
  texlive-collection-luatex poppler-utils python3 fontconfig \
  lato-fonts dejavu-fonts
```

### macOS

```bash
brew install --cask mactex-no-gui
brew install poppler python
brew install --cask font-lato font-dejavu
```

`mactex-no-gui` is large (several GB). `basictex` also works if you add the missing packages with `tlmgr`, but the full MacTeX is the least fragile route. If Homebrew's font casks change name, install Lato and DejaVu Sans Mono from their upstream sources instead:

- Lato: <https://fonts.google.com/specimen/Lato>
- DejaVu: <https://dejavu-fonts.github.io/>

### Windows

The supported route is **WSL2 with Ubuntu**. Install WSL, open an Ubuntu shell, clone the repository inside the Linux filesystem, and run `./setup.sh` as above.

Native Windows is possible with TeX Live or MiKTeX, Python and poppler, but the shell scripts assume a POSIX environment (`bash`, `cp`, `dirname`). If you must build natively, run the commands inside Git Bash and install the Lato and DejaVu Sans Mono fonts for all users.

### Verify the installation

```bash
lualatex --version
python3 --version
pdfinfo -v
fc-match Lato
fc-match "DejaVu Sans Mono"
```

On macOS, `fc-match` may not exist. Check the fonts in Font Book instead. `lualatex` must be the LuaHBTeX engine; plain `pdflatex` will not work, because the house style uses `fontspec`.

### Version notes

The documents were built with TeX Live 2025. TeX Live 2023 and later should work; the packages used are stable. Different font versions can shift pagination by a page. That is not a defect: `build_all.sh` rewrites the page counts from the PDFs it has just built, so the document-set blocks stay correct.

---

## 2. Build

### One document

```bash
./build/build.sh G4-6_Rules_and_Search.md
```

The script writes `build/G4-6_Rules_and_Search.tex`, runs `lualatex` twice, copies the PDF to the project root, and prints the page count.

### The teaching set

```bash
./build/build_all.sh
```

This builds the eight teaching volumes, runs `build/update_docset.py` to rewrite the page counts in every document-set block, rebuilds so the counts match the PDFs that contain them, and reports the final counts.

It does **not** build the design archive, because the archive is not part of the teaching set. Build it separately when you edit it:

```bash
./build/build.sh Curriculum_Plan_Logic_Programming.md
python3 build/update_docset.py
./build/build.sh Curriculum_Plan_Logic_Programming.md
```

### What happens under the hood

```
your.md  →  build/md2tex.py  →  build/your.tex  →  lualatex (×2)  →  build/your.pdf  →  ./your.pdf
```

1. `md2tex.py` converts the Markdown dialect to LaTeX and applies the house style: title page, colours, fonts, boxes, tables, running headers.
2. `lualatex` runs twice so the table of contents and page references resolve.
3. The PDF is copied to the project root.

If conversion fails, `build.sh` prints the first LaTeX errors and exits. The full transcript is `build/<name>.log`, and `build/<name>.tex` is exactly what LaTeX saw. That `.tex` file is where to look when a table or a symbol misbehaves.

### Check the build

```bash
./build/check.sh
```

It prints, for each teaching volume, the page count, the number of unresolved references (`??`) and the number of overfull boxes in the log. It also verifies that all eight document-set blocks agree. It exits non-zero if any of those checks fail.

A healthy set looks like this:

```
document                                                pages   unresolved  overfull
--------                                                -----   ----------  --------
00_Overview_and_Map.pdf                                    27            0         0
G1-3_Foundations.pdf                                       24            0         0
...
document-set check: all eight blocks agree
```

`build/*.tex`, `build/*.log`, `build/*.aux` and `build/*.pdf` are generated and ignored by git. The PDFs in the project root are committed.

A rebuild rewrites the committed PDFs. Their content and page counts stay the same, but the bytes differ because each PDF records its creation date. That is expected. Commit the rebuilt PDFs alongside the source change; do not treat the binary diff as a content change.

---

## 3. Editing rules

- **One source of truth.** Edit the `.md`, never the generated `.tex` or the PDF.
- **Each volume is standalone.** A teacher should not need another file to teach from it.
- **Keep the document-set block current.** `build_all.sh` does it. If you rebuild one volume by hand and its pagination changes, run `python3 build/update_docset.py` and rebuild the volumes it names.
- **Numbering is automatic.** Do not type chapter numbers into the heading text. `# 12. Title` uses `12` only to order the source; the renderer strips it and numbers the chapter itself.
- **Unnumbered material** — preface, front matter, references, appendices — starts with `# ^ `. Its sections use `## ^ `.
- **British spelling and international punctuation** are used throughout. Keep them.
- **No new figures in the teaching volumes.** The band documents and the T4 volumes are text-only by design. The archive holds the figures.
- **The Gricean test.** Before adding a section, ask whether it changes a decision the reader will make. If not, cut it. Define terms at first use. One idea per paragraph.

### The Markdown dialect

Ordinary Markdown works. A few conventions carry the layout.

| In the `.md` | Result |
|---|---|
| `# 12. Title` | numbered chapter |
| `# ^ Preface` | unnumbered chapter, still listed in contents |
| `## Section` | numbered section |
| `## ^ Section` | unnumbered section |
| `<!-- part: Part II — The weeks -->` | part divider page; a leading `Part II — ` is stripped to avoid duplication |
| `<!-- pagebreak -->` | forced page break |
| `![Caption](figures/fig_x.png){width=0.95}` | figure with caption (width is a fraction of the text block) |
| `::: box Title` … `:::` | cream box; also `warning` and `lesson` |
| fenced code block with `prolog` | monospaced code panel |
| `\| a \| b \|` table | dark header, zebra rows, automatic column widths |
| `"quoted"` | typographic double quotes, paired in order of appearance |

### Front matter

Title, subtitle, version, date and the running header come from the YAML block at the top of each source:

```yaml
---
title: Foundations
subtitle: Logical thinking for grades 1–3, ages 6–9
version: Version 2.0
date: November 2026
doccode: CURR-G1-3-001
audience: Teachers of grades 1–3 · ages 6–9
running: FOUNDATIONS · GRADES 1–3
prepared: Prepared by the curriculum drafting group.
---
```

- `running` is the left-hand text in the page header; keep it short.
- `prepared` is the line at the foot of the title page.
- `doccode` appears top-right on the title page.

### Two things that break tables

1. **A pipe `|` inside a cell** splits the column. Write `given` instead of `p(A|B)`, or keep the notation out of tables.
2. **Long unbreakable filenames** in narrow cells overflow the column. Put filenames in bullet lists, one per line.

Tables are set flush in the text flow, so they never float away from the section that introduces them. A table wider than six columns is shrunk automatically; beyond that, split it.

### The document-set block

Each volume ends with a list of the eight teaching documents between two markers:

```
<!-- docset:start -->
...
<!-- docset:end -->
```

`build/update_docset.py` reads the page counts from the PDFs and rewrites the block in every source. Do not edit the block by hand.

---

## 4. Figures (design archive only)

Only `Curriculum_Plan_Logic_Programming` uses figures. The archive embeds the **PNG** files; the **SVG** files are the sources and are generated by a script.

```bash
python3 build/make_figures.py

cd figures
for f in *.svg; do
  inkscape "$f" --export-type=png --export-filename="${f%.svg}.png"
done
cd ..

./build/build.sh Curriculum_Plan_Logic_Programming.md
```

The colours and type sizes are defined at the top of `build/make_figures.py`:

```python
INK='#123A5C'; GOLD='#C9A227'; TEAL='#1F5A7A'; CREAM='#F7F4EC'
```

Change them there, not in individual SVGs, so the set stays consistent.

---

## 5. Repository layout

```
.
├── README.md
├── LICENSE                        CC BY 4.0 for the documents
├── LICENSE-CODE                   MIT for the scripts
├── setup.sh                       installs the toolchain (Debian/Ubuntu/WSL2)
├── .gitignore
├── build/
│   ├── build.sh                   rebuild one PDF
│   ├── build_all.sh               rebuild the teaching set and sync page counts
│   ├── check.sh                   page counts, unresolved refs, overfull boxes
│   ├── md2tex.py                  Markdown → LaTeX converter and house style
│   ├── update_docset.py           sync the document-set blocks
│   └── make_figures.py            generates figures/*.svg
├── figures/                       SVG sources and PNG exports (archive only)
├── 00_Overview_and_Map.md/.pdf
├── G1-3_Foundations.md/.pdf
├── G4-6_Rules_and_Search.md/.pdf
├── G7-9_Critique.md/.pdf
├── G10-12_Judgement.md/.pdf
├── T4_CS_Logical_Thinking_and_Logic_Programming.md/.pdf
├── T4_GEN_Logic_Evidence_and_Machines.md/.pdf
├── Adult_PostCollege.md/.pdf
├── Curriculum_Plan_Logic_Programming.md/.pdf   design archive
├── An Introduction to Logical Thinking (v2 university).md
└── Concept_Sequence_Logic_Critical_Thinking.md
```

---

## 6. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `! Missing $ inserted` | an unescaped `_` or `^` outside a code span | put the symbol in backticks, or rephrase |
| `Font "Lato" not found` | Lato is not installed for fontconfig | install `fonts-lato`, or the font files, then rerun `fc-cache -f` |
| `Font "DejaVu Sans Mono" not found` | only the proportional DejaVu is installed | install `fonts-dejavu-mono` or `fonts-dejavu` |
| Table columns shifted | a `|` inside a cell | remove the pipe or move the notation to prose |
| Overfull hbox warning | a long word or filename in a narrow column | shorten it, or move it to a bullet list |
| Contents entry missing | heading used `#^` or `##^` instead of `# ^` | add the space after `#` |
| Figure missing | PNG not exported after editing the SVG | rerun the figure loop in section 4 |
| Build stops with no PDF | LaTeX error | read `build/<name>.log`, first `!` line |
| Page numbers in the document set are stale | a rebuild changed pagination | run `build_all.sh`, or `update_docset.py` and rebuild |
| A part page says “Part II” twice | the marker repeated the prefix | the converter strips `Part II — `; check the marker syntax |
| `./setup.sh: Permission denied` | the script is not executable | `chmod +x setup.sh build/*.sh` |

---

## 7. Contributing

1. Edit the Markdown source.
2. Run `./build/build_all.sh`.
3. Run `./build/check.sh`. All eight volumes should report zero unresolved references and zero overfull boxes, and the document-set blocks should agree.
4. Commit the `.md` and the rebuilt `.pdf` together, so the repository stays readable without a TeX installation.

Please do not commit `build/*.tex`, `build/*.log` or `build/*.pdf`; they are ignored, and they duplicate content.

## Licence

- The **documents** — all `.md` sources and the PDFs built from them — are licensed under the [Creative Commons Attribution 4.0 International Licence](LICENSE). You may share and adapt them, including commercially, with attribution.
- The **scripts** in `build/` and `setup.sh` are licensed under the [MIT Licence](LICENSE-CODE).

If you reuse the curriculum, cite it as:

> *The Glass Box: a curriculum in logical thinking.* Version 2.0, November 2026. <https://github.com/jacintodavila/curricula>
