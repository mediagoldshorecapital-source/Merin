#!/usr/bin/env python3
"""Turn a Meta Ad Library scraper export (.docx) into a structured ad dataset.

The export pastes one block per ad, in this shape:

    Library ID: <id>
    Started running on <DD Mon YYYY>Platforms
    Running<N> days
    Open Ad[Open All Ads]Download Images/Videos
    [page avatar image]
    <Page name>
    Sponsored
    <primary text, one or more paragraphs>
    [creative image]           <- or "0:00 / 0:45" when the ad is a video
    <DISPLAY.DOMAIN>
    <headline>
    [<description>]
    Active <N> days
    CTA: <CTA_ENUM>
    <link>
    Page like: <N>

Usage:
    python parse_ad_library_export.py export.docx out.csv [--media-dir DIR]

--media-dir also unpacks every embedded creative as a JPG so the images can be
reviewed as contact sheets (see build_contact_sheets.py).
"""
import argparse
import csv
import html
import json
import os
import re
import zipfile

KNOWN_ADVERTISERS = [
    "Timeline Longevity", "Renue By Science", "Omre", "NOVOS", "Elysium Health",
    "Tru Niagen", "Wonderfeel", "ProHealth Longevity", "Double Wood Supplements",
    "Medvi",
]


def docx_to_lines(path, media_dir=None):
    """Flatten document.xml into text lines with [[IMG file.jpg]] markers."""
    with zipfile.ZipFile(path) as z:
        document = z.read("word/document.xml").decode("utf-8")
        rels = dict(re.findall(
            r'Id="(rId\d+)"[^>]*Target="([^"]+)"',
            z.read("word/_rels/document.xml.rels").decode("utf-8"),
        ))
        if media_dir:
            os.makedirs(media_dir, exist_ok=True)
            for name in z.namelist():
                if name.startswith("word/media/"):
                    with open(os.path.join(media_dir, os.path.basename(name)), "wb") as f:
                        f.write(z.read(name))

    lines = []
    for para in re.findall(r"<w:p[ >].*?</w:p>", document, re.S):
        for rid in re.findall(r'r:embed="(rId\d+)"', para):
            lines.append("[[IMG %s]]" % os.path.basename(rels.get(rid, "?")))
        text = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", para, re.S))
        text = html.unescape(text).replace("\u200b", "").strip()
        if text:
            lines.append(text)
    return lines


def normalise_advertiser(name):
    """Collapse 'Brand with Creator' partnership labels onto the brand."""
    if not name:
        return "UNATTRIBUTED"
    name = name.strip()
    if name == "Timeline Nutrition":
        return "Timeline Longevity"
    pair = re.match(r"^(.*) with (.*)$", name)
    if pair:
        for known in KNOWN_ADVERTISERS:
            if known in (pair.group(1), pair.group(2)):
                return known
    return name


def parse(lines):
    starts = [i for i, l in enumerate(lines) if l.startswith("Library ID:")]
    records, seen = [], set()

    for n, start in enumerate(starts):
        end = starts[n + 1] - 1 if n + 1 < len(starts) else len(lines)
        block = [l for l in lines[start:end] if l]
        blob = "\n".join(block)

        library_id = block[0].split(":", 1)[1].strip()
        if library_id in seen:      # scraper exports repeat whole brand sections
            continue
        seen.add(library_id)

        rec = {"library_id": library_id}
        for key, pattern, cast in [
            ("started", r"Started running on ([0-9]{1,2} \w+ \d{4})", str),
            ("running_days", r"Running([\d.]+) days", float),
            ("active_days", r"Active (\d+) days?", int),
            ("cta", r"CTA: (\w+)", str),
            ("page_likes", r"Page like: (\d+)", int),
        ]:
            match = re.search(pattern, blob)
            rec[key] = cast(match.group(1)) if match else None

        rec["multi_version"] = "This ad has multiple versions" in blob
        # A duration read-out ("0:00 / 0:45") sits where a static's image would be.
        rec["media_type"] = "video" if re.search(r"\d:\d\d ?/ ?\d+:\d\d", blob) else "static"

        header = next((i for i, l in enumerate(block) if l.startswith("Open Ad")), None)
        advertiser = body_start = None
        if header is not None:
            i = header + 1
            while i < len(block) and block[i].startswith("[[IMG"):
                i += 1
            if i < len(block):
                advertiser = block[i]
                for j in range(i, min(i + 5, len(block))):
                    if block[j] == "Sponsored":
                        body_start = j + 1

        rec["advertiser_raw"] = advertiser
        rec["advertiser"] = normalise_advertiser(advertiser)

        images = re.findall(r"\[\[IMG (\S+)\]\]", blob)
        rec["creative_image"] = images[1] if len(images) > 1 else None

        def is_creative_marker(line):
            return line.startswith("[[IMG") or re.match(r"^\d:\d\d ?/", line)

        body, tail, past_creative = [], [], False
        for line in block[body_start or 0:]:
            if past_creative:
                tail.append(line)
            elif is_creative_marker(line):
                past_creative = True
            elif body_start is not None:
                body.append(line)
        rec["primary_text"] = "\n".join(body)

        link_unit = []
        for line in tail:
            if re.match(r"^Active \d+ days?$", line) or line.startswith("CTA:"):
                break
            link_unit.append(line)
        rec["display_domain"] = link_unit[0] if link_unit else None
        rec["headline"] = link_unit[1] if len(link_unit) > 1 else None
        rec["description"] = "\n".join(link_unit[2:]) if len(link_unit) > 2 else None

        records.append(rec)
    return records


COLUMNS = ["library_id", "advertiser", "advertiser_raw", "started", "running_days",
           "active_days", "media_type", "cta", "display_domain", "headline",
           "description", "primary_text", "page_likes", "multi_version", "creative_image"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("out_csv")
    ap.add_argument("--media-dir", help="also extract creative images here")
    ap.add_argument("--json", help="also write the records as JSON")
    args = ap.parse_args()

    records = parse(docx_to_lines(args.docx, args.media_dir))
    with open(args.out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=1)
    print("%d unique ads -> %s" % (len(records), args.out_csv))


if __name__ == "__main__":
    main()
