#!/usr/bin/env python3
"""Build ONE downloadable Word file + PDF for a whole folder of ads.

The team uploads these to Drive, so this is the standard last step of every
folder run. Each video starts on a new page with its cover frame, then the full
report. Duplicates get a one-line pointer page. Every report is re-verified
while building, and its verifier result is stamped into the Transcription line;
a report that fails stops the build.

Layout expected:
    <workdir>/NN/report.md      one per video (NN = 01, 02, ...)
    <workdir>/NN/cover.jpg      first frame (from extract_frames.py)
    <workdir>/NN/transcript.json
    (NN may be a symlink into a shared library when one ad appears in several
    folders; its "# Video XX —" heading is renumbered per folder.)

Usage:
    python3 build_folder_report.py <workdir> --title "Competitor Ads — 15 Oct" \
        --subtitle "October - Winners / 15 Oct / Videos · 44 files" \
        --front front.md --duplicates 24=12 33=27 35=15 --out ~/out/Competitor_Ads_15_Oct

<front.md> is the overview: how to use the document, the offer, the index
table and the cross-video patterns. Writes <out>.docx and <out>.pdf.
Needs pandoc; the PDF needs LibreOffice (soffice). Without soffice you get
the .docx only.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.join(HERE, "verify_report.py")
PAGE_BREAK = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'
PANDOC_FMT = "markdown+raw_attribute-tex_math_dollars-tex_math_single_backslash-subscript-superscript"


def verify(report, transcript):
    """Return the number of quotes traced, or None if the report has no transcript."""
    if not os.path.exists(transcript):
        return None
    r = subprocess.run([sys.executable, "-I", VERIFY, report, "--transcript", transcript],
                       capture_output=True, text=True)
    m = re.search(r"PASSED\S* — (\d+) quoted", r.stdout)
    if not m:
        sys.exit(f"Verifier failed for {report} — fix it before building:\n{r.stdout[-1500:]}")
    return int(m.group(1))


def section(n, d, cover_height, label=None):
    report = os.path.join(d, "report.md")
    t = open(report).read()
    # A report can be shared by several folders: number it for this one.
    t = re.sub(r"(?m)^# Video(?: [0-9X]+)? —", f"# Video {n} —", t, count=1)
    if label:
        t = re.sub(r"(?m)^(# Video .*)$", lambda m: m.group(1) + f"\n\n**Drive subfolder:** {label}", t, count=1)
    tj = os.path.join(d, "transcript.json")
    k = verify(report, tj)
    if k is not None and "**Verifier:**" not in t:
        t = re.sub(r"(\*\*Transcription:\*\*[^\n]*)",
                   lambda m: m.group(1).rstrip() + f" · **Verifier:** passed, {k}/{k} quotes traced to the audio",
                   t, count=1)
    cover = os.path.abspath(os.path.join(d, "cover.jpg"))
    t = re.sub(r"!\[([^\]]*)\]\((?:[^)]*/)?cover\.jpg\)",
               lambda m: f"![{m.group(1)}]({cover}){{height={cover_height}in}}", t)
    return t


def main():
    p = argparse.ArgumentParser()
    p.add_argument("workdir")
    p.add_argument("--title", required=True)
    p.add_argument("--subtitle", default="")
    p.add_argument("--front", help="overview markdown placed before the videos")
    p.add_argument("--duplicates", nargs="*", default=[], help="pairs like 24=12 (copy=original)")
    p.add_argument("--out", required=True, help="output path without extension")
    p.add_argument("--cover-height", type=float, default=3.6)
    p.add_argument("--labels", help="TSV of NN<TAB>Drive subfolder, shown under each heading")
    a = p.parse_args()

    if not shutil.which("pandoc"):
        sys.exit("pandoc is not installed; fall back to build_docx.py per report.")
    dups = dict(x.split("=") for x in a.duplicates)
    labels = dict(l.rstrip("\n").split("\t", 1) for l in open(a.labels)) if a.labels else {}
    nums = sorted({n for n in os.listdir(a.workdir) if re.fullmatch(r"\d+", n)} | set(dups), key=int)

    body, heads = [], []
    for n in nums:
        body.append(PAGE_BREAK)
        if n in dups:
            o = dups[n]
            first = re.sub(r"^Video(?: [0-9X]+)? —", f"Video {o} —",
                           open(os.path.join(a.workdir, o, "report.md")).readline().lstrip("# ").strip())
            h = f"Video {n} — duplicate of Video {o}"
            body.append(f"# {h}\n\nThis file is a byte-for-byte copy of Video {o} (same checksum). "
                        f"The full teardown is under **{first}**.\n")
        else:
            d = os.path.join(a.workdir, n)
            if not os.path.exists(os.path.join(d, "report.md")):
                sys.exit(f"Missing {d}/report.md")
            t = section(n, d, a.cover_height, labels.get(n))
            h = re.search(r"(?m)^# (.+)$", t).group(1)
            body.append(t)
        heads.append(h)

    md = [f'---\ntitle: "{a.title}"\nsubtitle: "{a.subtitle}"\n---\n',
          "## Contents\n\n" + "\n".join(f"- {h}" for h in heads) + "\n"]
    if a.front:
        md.append(open(a.front).read())
    md += body
    text = "\n".join(md)
    # Every bold-labelled line (beats, metadata, variations) as its own paragraph.
    text = re.sub(r"(?m)(?<=\S)\n(?=\*\*[A-Z0-9])", "\n\n", text)
    text = re.sub(r"(?m)(?<=\S)\n(?=\*Visual:\*)", "\n\n", text)

    out = os.path.abspath(a.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    src = out + ".md"
    open(src, "w").write(text)
    subprocess.run(["pandoc", src, "-f", PANDOC_FMT, "-o", out + ".docx"], check=True)
    style_docx(out + ".docx")
    print(f"Word: {out}.docx")

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if soffice:
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir",
                        os.path.dirname(out), out + ".docx"], check=True, capture_output=True)
        print(f"PDF:  {out}.pdf")
    else:
        print("LibreOffice not found — PDF skipped (Word → File → Save As PDF works too).")


def style_docx(path):
    """Grey table borders, shaded header row, 9 pt table text, Calibri body, 0.8 in margins."""
    from docx import Document
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt

    d = Document(path)
    for t in d.tables:
        borders = OxmlElement("w:tblBorders")
        for e in ("top", "left", "bottom", "right", "insideH", "insideV"):
            x = OxmlElement(f"w:{e}")
            x.set(qn("w:val"), "single"); x.set(qn("w:sz"), "4"); x.set(qn("w:color"), "BFBFBF")
            borders.append(x)
        t._tbl.tblPr.append(borders)
        for c in t.rows[0].cells:
            sh = OxmlElement("w:shd")
            sh.set(qn("w:val"), "clear"); sh.set(qn("w:fill"), "EDEDED")
            c._tc.get_or_add_tcPr().append(sh)
        for row in t.rows:
            for c in row.cells:
                for para in c.paragraphs:
                    for r in para.runs:
                        r.font.size = Pt(9)
    normal = d.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    for s in d.sections:
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Inches(0.8)
    d.save(path)


if __name__ == "__main__":
    main()
