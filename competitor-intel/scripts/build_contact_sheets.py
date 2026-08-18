#!/usr/bin/env python3
"""Lay competitor statics out as labelled contact sheets so they can be reviewed
visually (four creatives per sheet, sorted longest-running first).

Longest-running is the closest free proxy we have for "this ad works": nobody
keeps paying to serve a static for 100+ days that isn't returning.

Usage:
    python build_contact_sheets.py ads.json media_dir out_dir [--per-brand 12]
"""
import argparse
import json
import os

from PIL import Image, ImageDraw, ImageFont

CELL, PAD, LABEL_H = 760, 8, 26


def days(ad):
    return ad.get("running_days") or ad.get("active_days") or 0


def pick(ads, media_dir, per_brand):
    chosen, by_brand = [], {}
    for ad in ads:
        by_brand.setdefault(ad["advertiser"], []).append(ad)
    for brand, brand_ads in by_brand.items():
        statics = [a for a in brand_ads
                   if a["media_type"] == "static" and a.get("creative_image")
                   and os.path.exists(os.path.join(media_dir, a["creative_image"]))]
        statics.sort(key=days, reverse=True)
        seen = set()
        for ad in statics:
            if ad["creative_image"] in seen:
                continue          # the same creative is re-used across many ad IDs
            seen.add(ad["creative_image"])
            chosen.append(ad)
            if len(seen) >= per_brand:
                break
    return chosen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ads_json")
    ap.add_argument("media_dir")
    ap.add_argument("out_dir")
    ap.add_argument("--per-brand", type=int, default=12)
    args = ap.parse_args()

    ads = pick(json.load(open(args.ads_json)), args.media_dir, args.per_brand)
    os.makedirs(args.out_dir, exist_ok=True)
    font = ImageFont.load_default(size=20)

    for i in range(0, len(ads), 4):
        sheet = Image.new("RGB", (CELL * 2 + PAD * 3, (CELL + LABEL_H) * 2 + PAD * 3), (245, 245, 245))
        draw = ImageDraw.Draw(sheet)
        for j, ad in enumerate(ads[i:i + 4]):
            img = Image.open(os.path.join(args.media_dir, ad["creative_image"])).convert("RGB")
            img.thumbnail((CELL, CELL), Image.LANCZOS)
            x = PAD + (j % 2) * (CELL + PAD)
            y = PAD + (j // 2) * (CELL + LABEL_H + PAD)
            draw.text((x, y + 4), "#%d %s | %dd" % (i + j + 1, ad["advertiser"], days(ad)),
                      fill=(0, 0, 0), font=font)
            sheet.paste(img, (x + (CELL - img.width) // 2, y + LABEL_H))
        sheet.save(os.path.join(args.out_dir, "sheet%02d.png" % (i // 4 + 1)))
    print("%d creatives -> %d sheets in %s" % (len(ads), (len(ads) + 3) // 4, args.out_dir))


if __name__ == "__main__":
    main()
