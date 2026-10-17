#!/usr/bin/env python3
"""Machine-read the text on a static ad (one image or a carousel).

The static-ad equivalent of transcribe.py: what the OCR reads is the evidence
that quoted on-image copy is checked against (verify_report.py --static).

Usage:
    python3 ocr_image.py slide1.jpg [slide2.jpg ...] --outdir <workdir>

Writes <workdir>/ocr.json (segments with slide number, text, confidence, box)
and <workdir>/ocr.txt (one line per text block, grouped by slide). Needs
rapidocr_onnxruntime (pip install rapidocr_onnxruntime).
"""
import argparse
import json
import os


def main():
    p = argparse.ArgumentParser()
    p.add_argument("images", nargs="+")
    p.add_argument("--outdir", required=True)
    a = p.parse_args()

    from rapidocr_onnxruntime import RapidOCR
    engine = RapidOCR()
    segs, lines = [], []
    for n, img in enumerate(a.images, 1):
        result, _ = engine(img)
        # Reading order: top-to-bottom, then left-to-right within a row.
        blocks = sorted(result or [], key=lambda r: (round(min(pt[1] for pt in r[0]) / 20), min(pt[0] for pt in r[0])))
        lines.append(f"## Slide {n} — {os.path.basename(img)}")
        if not blocks:
            lines.append("[no text found]")
        for box, text, score in blocks:
            score = float(score)
            segs.append({"slide": n, "text": text, "score": round(float(score), 3),
                         "box": [[round(float(x)), round(float(y))] for x, y in box]})
            lines.append(f"{text}" + ("" if score >= 0.8 else f"   <<low confidence {score:.2f}>>"))
        lines.append("")
    os.makedirs(a.outdir, exist_ok=True)
    meta = {"source": [os.path.basename(i) for i in a.images], "backend": "rapidocr", "slides": len(a.images)}
    json.dump({"meta": meta, "segments": segs}, open(os.path.join(a.outdir, "ocr.json"), "w"), indent=1)
    open(os.path.join(a.outdir, "ocr.txt"), "w").write(
        "# OCR of on-image text — machine-read; stylised type can be misread.\n"
        "# Quote on-image copy from the IMAGE, using this as the cross-check.\n\n" + "\n".join(lines))
    print(f"{len(segs)} text blocks across {len(a.images)} slide(s)")


if __name__ == "__main__":
    main()
