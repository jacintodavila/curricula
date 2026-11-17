#!/usr/bin/env python3
"""Rewrite the document-set block in every volume from the built PDFs.

The page counts are read from the PDFs in the project root. Run this after
building, then rebuild the volumes whose block changed.
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOCS = [
    ("00_Overview_and_Map.pdf",
     "The Glass Box: overview and map",
     "The entry point: the Gricean standard, the four bands, the constant, the dial and the assessment spine."),
    ("G1-3_Foundations.pdf",
     "Foundations: grades 1–3",
     "Naming, fact and guess, the question and the first rule. Eighteen unit cards and a scripted lesson."),
    ("G4-6_Rules_and_Search.pdf",
     "Rules and Search: grades 4–6",
     "Rules, needed and enough, search, recursion, sources and the closed world. Eighteen unit cards and two scripted lessons."),
    ("G7-9_Critique.pdf",
     "Critique: grades 7–9",
     "Standard form, counterexample, implicature, fallacies as questions and the first Prolog program. Eighteen unit cards."),
    ("G10-12_Judgement.pdf",
     "Judgement: grades 10–12",
     "Validity, models, Prolog II, uncertainty, the AI audit and the limit-of-the-model defence. Eighteen unit cards."),
    ("T4_CS_Logical_Thinking_and_Logic_Programming.pdf",
     "Logical Thinking and Logic Programming for Computer Science",
     "The fourteen-week computer-science course: two strands, labs, project brief, rubrics and examination."),
    ("T4_GEN_Logic_Evidence_and_Machines.pdf",
     "Logic, Evidence and Machines",
     "The fourteen-week general course: evidence, argument and machines, with workshops and a capstone."),
    ("Adult_PostCollege.pdf",
     "Judgement at Work",
     "Ten sessions of ninety minutes, with thirty-minute cores, for workplaces and community groups."),
]

SOURCES = [
    "00_Overview_and_Map.md",
    "G1-3_Foundations.md",
    "G4-6_Rules_and_Search.md",
    "G7-9_Critique.md",
    "G10-12_Judgement.md",
    "T4_CS_Logical_Thinking_and_Logic_Programming.md",
    "T4_GEN_Logic_Evidence_and_Machines.md",
    "Adult_PostCollege.md",
    "Curriculum_Plan_Logic_Programming.md",
]


def page_count(pdf):
    path = os.path.join(ROOT, pdf)
    if not os.path.exists(path):
        return "not built"
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return f"{m.group(1)} pages" if m else "unknown"


def block():
    lines = []
    for pdf, title, desc in DOCS:
        lines.append(f"- `{pdf}` — *{title}.* {desc} {page_count(pdf)}.")
    return "\n".join(lines)


def main():
    text = block()
    changed = []
    for src in SOURCES:
        path = os.path.join(ROOT, src)
        s = open(path, encoding="utf8").read()
        new, n = re.subn(
            r"<!-- docset:start -->.*?<!-- docset:end -->",
            "<!-- docset:start -->\n" + text + "\n<!-- docset:end -->",
            s,
            flags=re.S,
        )
        if n == 0:
            print(f"no docset markers in {src}", file=sys.stderr)
            continue
        if new != s:
            open(path, "w", encoding="utf8").write(new)
            changed.append(src)
    print("updated:", ", ".join(changed) if changed else "nothing")


if __name__ == "__main__":
    main()
