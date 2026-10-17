#!/usr/bin/env python3
"""Render a Prime-branded layout mockup of a static ad and a side-by-side comparison.

Reads the Phase 4 table of a static report (Headline, Subhead, Offer badge, Proof
strip, CTA button), lays it out in the Prime brand system (deep purple / lavender /
ivory, gold accents, two-tone headline, rounded purple CTA) at the competitor ad's
aspect ratio, with the real Prime bottle cut-out, and writes:

    <workdir>/prime_mockup.jpg   the Prime version on its own
    <workdir>/compare.jpg        competitor (left) next to the Prime mockup (right)

It is a layout and copy guide for the designer — not final art.

Usage:
    python3 render_mockup.py <workdir> --bottle prime_bottle.png
"""
import argparse
import os
import re
import textwrap

from PIL import Image, ImageDraw, ImageFilter, ImageFont

PURPLE = (88, 44, 131)
DEEP = (62, 27, 98)
LAV = (233, 225, 242)
IVORY = (251, 248, 242)
GOLD = (191, 160, 92)
CHAR = (40, 36, 44)
GREY = (120, 114, 126)
F = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
SERIF = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"


def font(weight, size):
    try:
        return ImageFont.truetype(F.format(weight), size)
    except OSError:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)


def phase4_copy(md):
    sec = re.split(r"(?m)^## Phase 4.*$", md)
    if len(sec) < 2:
        return {}
    body = re.split(r"(?m)^## Phase 5", sec[1])[0]
    rows = {}
    for line in body.splitlines():
        s = line.strip()
        if not s.startswith("|") or s.count("|") < 3:
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if re.fullmatch(r":?-{2,}:?", cells[0]) or cells[0].lower() == "element":
            continue
        rows[cells[0].lower()] = re.sub(r'^[“"]|[”"]$', "", cells[1].strip()).strip()
    return rows


def pick(rows, *keys):
    for want in keys:
        for k, v in rows.items():
            if want in k and v and v != "—":
                return v
    return ""


def fit(draw, text, weight, width, start, minimum, max_lines):
    size = start
    while size >= minimum:
        f = font(weight, size)
        avg = draw.textlength("abcdefghijklmnopqrstuvwxyz", font=f) / 26
        lines = textwrap.wrap(text, max(6, int(width / avg)))
        if len(lines) <= max_lines and all(draw.textlength(l, font=f) <= width for l in lines):
            return f, lines
        size -= 4
    f = font(weight, minimum)
    avg = draw.textlength("abcdefghijklmnopqrstuvwxyz", font=f) / 26
    return f, textwrap.wrap(text, max(6, int(width / avg)))[:max_lines]


def render(rows, size, bottle):
    W, H = size
    im = Image.new("RGB", (W, H), IVORY)
    px = im.load()
    for y in range(H):   # lavender -> ivory gradient
        t = y / H
        c = tuple(int(LAV[i] * (1 - t) + IVORY[i] * t) for i in range(3))
        for x in range(W):
            px[x, y] = c
    d = ImageDraw.Draw(im)
    m = int(W * 0.07)
    y = int(H * 0.04)
    r = int(W * 0.012)   # small leaf mark + serif wordmark
    d.ellipse((m, y + r, m + 2 * r, y + 3.2 * r), fill=(110, 140, 90))
    d.text((m + int(W * 0.035), y), "Prime Ingredients", font=ImageFont.truetype(SERIF, int(W * 0.035)), fill=PURPLE)
    y += int(W * 0.08)

    head = pick(rows, "headline", "hook") or "Prime Ingredients NMN"
    fh, lines = fit(d, head.upper(), "ExtraBold", W - 2 * m, int(W * 0.095), int(W * 0.05), 4)
    for i, line in enumerate(lines):   # house signature: two-tone headline
        d.text((m, y), line, font=fh, fill=CHAR if i < (len(lines) + 1) // 2 else PURPLE)
        y += int(fh.size * 1.08)
    sub = pick(rows, "subhead", "sub-head", "body")
    if sub:
        y += int(W * 0.015)
        fs, sl = fit(d, sub, "Medium", W - 2 * m, int(W * 0.042), int(W * 0.03), 3)
        for line in sl:
            d.text((m, y), line, font=fs, fill=CHAR)
            y += int(fs.size * 1.25)

    cta_h = int(W * 0.11)
    cta_y = H - int(H * 0.05) - cta_h
    proof = pick(rows, "proof", "trust", "badges")
    proof_h = int(W * 0.09) if proof else 0
    top, bottom = y + int(W * 0.03), cta_y - proof_h - int(W * 0.03)
    bh = max(int(W * 0.25), bottom - top)
    b = bottle.copy()
    b.thumbnail((int(W * 0.6), bh))
    bx, by = (W - b.width) // 2, top + (bh - b.height) // 2
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))   # soft floor shadow
    ImageDraw.Draw(sh).ellipse((bx - b.width * 0.1, by + b.height * 0.93, bx + b.width * 1.1, by + b.height * 1.05),
                               fill=(60, 30, 90, 90))
    im.paste(sh.filter(ImageFilter.GaussianBlur(W * 0.015)), (0, 0), sh.filter(ImageFilter.GaussianBlur(W * 0.015)))
    im.paste(b, (bx, by), b)

    offer = pick(rows, "offer", "badge", "price")
    if offer:
        r = int(W * 0.15)
        cx, cy = W - m - r + int(W * 0.02), top + r // 2 + int(W * 0.02)
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=PURPLE, outline=GOLD, width=max(3, W // 180))
        fo, ol = fit(d, offer.upper(), "Bold", int(r * 1.55), int(W * 0.036), int(W * 0.02), 6)
        ty = cy - len(ol) * fo.size * 1.1 / 2
        for line in ol:
            d.text((cx - d.textlength(line, font=fo) / 2, ty), line, font=fo, fill=IVORY)
            ty += fo.size * 1.1

    if proof:
        fp, pl = fit(d, proof.replace(" · ", "  ·  "), "SemiBold", W - 2 * m, int(W * 0.03), int(W * 0.022), 2)
        py = cta_y - proof_h + int(W * 0.01)
        for line in pl:
            d.text(((W - d.textlength(line, font=fp)) / 2, py), line, font=fp, fill=DEEP)
            py += int(fp.size * 1.3)

    cta = (pick(rows, "cta", "button") or "Shop NMN").upper().rstrip(" →>") + "  →"
    d.rounded_rectangle((m, cta_y, W - m, cta_y + cta_h), radius=cta_h // 2, fill=PURPLE)
    fc, cl = fit(d, cta, "Bold", W - 2 * m - cta_h, int(W * 0.045), int(W * 0.028), 1)
    d.text(((W - d.textlength(cl[0], font=fc)) / 2, cta_y + (cta_h - fc.size) / 2 - fc.size * 0.1), cl[0], font=fc, fill=IVORY)
    note = "Layout mockup · copy & composition guide, not final art"
    d.text((m, H - int(H * 0.035)), note, font=font("Medium", max(12, int(W * 0.018))), fill=GREY)
    return im


def compare(comp, mock, h=900):
    a = comp.resize((int(comp.width * h / comp.height), h))
    b = mock.resize((int(mock.width * h / mock.height), h))
    pad, top = 30, 70
    out = Image.new("RGB", (a.width + b.width + pad * 3, h + top + pad), "white")
    d = ImageDraw.Draw(out)
    f = font("Bold", 30)
    d.text((pad, 20), "COMPETITOR", font=f, fill=CHAR)
    d.text((pad * 2 + a.width, 20), "PRIME VERSION (layout mockup)", font=f, fill=PURPLE)
    out.paste(a, (pad, top))
    out.paste(b, (pad * 2 + a.width, top))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("workdir")
    p.add_argument("--bottle", required=True)
    a = p.parse_args()
    rows = phase4_copy(open(os.path.join(a.workdir, "report.md")).read())
    if not rows:
        raise SystemExit("No Phase 4 table found.")
    slide = Image.open(os.path.join(a.workdir, "slide_1.jpg")).convert("RGB")
    ratio = min(max(slide.height / slide.width, 1.0), 16 / 9)   # square to 9:16
    W = 1080
    mock = render(rows, (W, int(W * ratio)), Image.open(a.bottle).convert("RGBA"))
    mock.save(os.path.join(a.workdir, "prime_mockup.jpg"), quality=90)
    compare(Image.open(os.path.join(a.workdir, "cover.jpg")).convert("RGB"), mock).save(
        os.path.join(a.workdir, "compare.jpg"), quality=88)
    print("wrote prime_mockup.jpg and compare.jpg")


if __name__ == "__main__":
    main()
