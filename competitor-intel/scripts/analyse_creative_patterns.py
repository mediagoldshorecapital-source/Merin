#!/usr/bin/env python3
"""Reproduce every number quoted in static-creative-playbook.md from the CSV.

Usage:
    python analyse_creative_patterns.py ../data/competitor_ads.csv
"""
import argparse
import csv
import datetime as dt
import re
import statistics as st
from collections import Counter, defaultdict

# Copy-layer patterns. These read the ad's text only — they cannot see words
# baked into the image, so image-layer formats are catalogued by eye instead.
PATTERNS = {
    "Mechanism / molecule named": r"\b(NAD\+?|mitochondri|cellular|urolithin|NMN|nicotinamide|resveratrol|creatine|senescen|hallmarks of aging|precursor|collagen|spermidine|fisetin)\b",
    "Clinical proof language": r"\b(clinical(ly)?|stud(y|ies)|peer.reviewed|trial|placebo|randomi[sz]ed|published|proven|third.party)\b",
    "Question hook": r"\?",
    "Offer / price / urgency": r"\b(\d{1,2}%\s*(off|lower)|\$\d+|save|sale|price drop|subscribe (and|&) save|free shipping|limited)\b",
    "Symptom or pain enumeration": r"\b(tired|fatigue|brain fog|foggy|stiff|sluggish|slower|forget|crash|sagging|wrinkl|joint|shed)\w*",
    "Age / decade callout": r"\b(30s|40s|50s|60s|70s|over (40|50|60))\b",
    "Identity / status framing": r"\b(high performers?|executives?|CEOs?|biohackers?|athletes?|top performers?)\b",
    "Authority / doctor": r"\b(doctor|dr\.|M\.?D\.?|physician|formulated by|founder)\b",
    "Social proof / press / rating": r"\b(customers|reviews?|thousands|rated|as seen in|#1|verified buyer)\b",
    "Comparison / category takedown": r"\b(unlike (other|most)|most supplements|other brands|versus|vs\.?)\b",
    "Second person (you / your)": r"\byou(r)?\b",
}


def load(path):
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["running_days"] = float(r["running_days"]) if r["running_days"] else 0.0
        r["active_days"] = int(r["active_days"]) if r["active_days"] else 0
        r["days"] = r["running_days"] or r["active_days"]
        r["page_likes"] = int(r["page_likes"]) if r["page_likes"] else 0
    return rows


def section(title):
    print("\n" + title)
    print("-" * len(title))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    args = ap.parse_args()
    rows = load(args.csv_path)
    statics = [r for r in rows if r["media_type"] == "static"]

    section("DATASET")
    print("unique ads: %d   static: %d   video: %d   advertisers: %d"
          % (len(rows), len(statics), len(rows) - len(statics),
             len({r["advertiser"] for r in rows})))

    section("PER-ADVERTISER MIX AND LONGEVITY")
    print("%-26s %4s %7s %6s %7s %7s %6s %6s" %
          ("ADVERTISER", "ADS", "STATIC", "%STAT", "MED_DAY", "MAX_DAY", ">30d", ">60d"))
    for brand, n in Counter(r["advertiser"] for r in rows).most_common():
        rs = [r for r in rows if r["advertiser"] == brand]
        if len(rs) < 5:
            continue
        s = [r for r in rs if r["media_type"] == "static"]
        d = [r["days"] for r in rs]
        print("%-26s %4d %7d %5.0f%% %7.1f %7.1f %6d %6d"
              % (brand, len(rs), len(s), 100 * len(s) / len(rs), st.median(d), max(d),
                 sum(1 for x in d if x > 30), sum(1 for x in d if x > 60)))

    section("CREATIVE MODULARITY (how much gets reused)")
    print("%-26s %4s %8s %9s %9s %10s" %
          ("ADVERTISER", "ADS", "IMAGES", "COPIES", "ADS/IMAGE", "IMGS/COPY"))
    for brand, n in Counter(r["advertiser"] for r in rows).most_common():
        rs = [r for r in rows if r["advertiser"] == brand]
        if len(rs) < 20:
            continue
        images = {r["creative_image"] for r in rs if r["creative_image"]}
        copies = {r["primary_text"][:200] for r in rs if r["primary_text"]}
        per_copy = defaultdict(set)
        for r in rs:
            if r["primary_text"] and r["creative_image"]:
                per_copy[r["primary_text"][:200]].add(r["creative_image"])
        print("%-26s %4d %8d %9d %9.2f %10.2f"
              % (brand, len(rs), len(images), len(copies),
                 len(rs) / max(len(images), 1),
                 st.mean([len(v) for v in per_copy.values()]) if per_copy else 0))

    section("STATIC COPY PATTERNS (share of %d static ads)" % len(statics))
    for name, pattern in PATTERNS.items():
        hits = sum(1 for r in statics
                   if re.search(pattern, " ".join([r["primary_text"], r["headline"] or "",
                                                   r["description"] or ""]), re.I))
        print("%5.1f%%  %4d  %s" % (100 * hits / len(statics), hits, name))

    section("STATIC COPY SHAPE")
    lengths = [len(r["primary_text"]) for r in statics if r["primary_text"]]
    heads = [len(r["headline"]) for r in statics if r["headline"]]
    print("primary text chars — p25 %d / median %d / p75 %d / max %d"
          % (sorted(lengths)[len(lengths) // 4], st.median(lengths),
             sorted(lengths)[3 * len(lengths) // 4], max(lengths)))
    print("headline chars — median %d / p90 %d"
          % (st.median(heads), sorted(heads)[int(0.9 * len(heads))]))
    print("two or more paragraphs: %.0f%%"
          % (100 * sum(1 for r in statics if "\n" in r["primary_text"]) / len(statics)))

    section("HOW LONG STATICS SURVIVE")
    buckets = Counter()
    for r in statics:
        d = r["days"]
        buckets["0-7d" if d < 7 else "7-30d" if d < 30 else "30-60d" if d < 60
                else "60-100d" if d < 100 else "100d+"] += 1
    for k in ["0-7d", "7-30d", "30-60d", "60-100d", "100d+"]:
        print("%-9s %4d  %5.1f%%" % (k, buckets[k], 100 * buckets[k] / len(statics)))

    section("PROVEN (>=60d) VS FRESH (<14d) STATICS — copy-layer index")
    proven = [r for r in statics if r["days"] >= 60]
    fresh = [r for r in statics if r["days"] < 14]
    print("proven n=%d   fresh n=%d" % (len(proven), len(fresh)))
    for name, pattern in PATTERNS.items():
        def share(group):
            return sum(1 for r in group if re.search(
                pattern, " ".join([r["primary_text"], r["headline"] or ""]), re.I)) / max(len(group), 1)
        a, b = share(proven), share(fresh)
        print("%-32s proven %4.0f%%  fresh %4.0f%%  index %s"
              % (name, 100 * a, 100 * b, ("%.2f" % (a / b)) if b else "n/a"))

    section("LAUNCH CADENCE (new ads first seen, by month)")
    months = Counter()
    for r in rows:
        try:
            months[dt.datetime.strptime(r["started"], "%d %b %Y").strftime("%Y-%m")] += 1
        except (ValueError, TypeError):
            pass
    for k in sorted(months):
        print("%s  %4d  %s" % (k, months[k], "#" * (months[k] // 8)))

    section("CTA MIX")
    for cta, n in Counter(r["cta"] for r in rows).most_common(8):
        print("%5d  %s" % (n, cta))


if __name__ == "__main__":
    main()
