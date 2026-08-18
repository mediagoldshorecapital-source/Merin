#!/usr/bin/env python3
"""
Deduplicate Facebook Ad Library CSV exports and report copy-structure stats.

Usage:  python3 extract.py <dir-of-csv-exports>

Ad Library exports overlap heavily (the same ad appears in multiple pulls) and a single
copy block is usually run across many creative variants. We dedupe on "Ad ID", then group
by (brand, copy) so each distinct piece of copy is counted once, annotated with how many
creatives ran it and the longest "Time Running" observed -- our proxy for a winner.
"""
import csv, glob, sys, re, collections, statistics

def load(directory):
    seen, rows = set(), []
    for path in sorted(glob.glob(f"{directory}/*.csv")):
        # exports carry a UTF-8 BOM on the header row
        with open(path, newline="", encoding="utf-8-sig") as fh:
            for row in csv.DictReader(fh):
                if row["Ad ID"] in seen:
                    continue
                seen.add(row["Ad ID"])
                rows.append(row)
    return rows

def days(row):
    m = re.match(r"(\d+)", row.get("Time Running") or "")
    return int(m.group(1)) if m else 0

def dump_copy(rows, out):
    agg = collections.defaultdict(lambda: {
        "n": 0, "days": 0,
        "cta": collections.Counter(), "fmt": collections.Counter(),
        "lp": collections.Counter(), "status": collections.Counter(),
    })
    for r in rows:
        copy = r["Ad Copy"].strip()
        if not copy:
            continue
        a = agg[(r["Brand Name"], copy)]
        a["n"] += 1
        a["days"] = max(a["days"], days(r))
        a["cta"][r["CTA Text"]] += 1
        a["fmt"][r["Type"]] += 1
        a["lp"][(r["Landing Page"] or "")[:60]] += 1
        a["status"][r["Activity Status"]] += 1
    for (brand, copy), a in sorted(agg.items(), key=lambda kv: (kv[0][0], -kv[1]["n"])):
        print("=" * 100, file=out)
        print(f"BRAND: {brand} | variants:{a['n']} | maxdays:{a['days']} | "
              f"CTA:{dict(a['cta'])} | fmt:{dict(a['fmt'])} | status:{dict(a['status'])}", file=out)
        print(f"LP: {a['lp'].most_common(1)[0][0]}", file=out)
        print("-" * 100, file=out)
        print(copy, file=out)
    return agg

# Structural features measured in section 2 of the teardown.
# Structural features measured in section 2 of the teardown.
# Third element is the regex flag set: authority names (TIME, Vogue, MD) must be matched
# case-sensitively, or "TIME" swallows every ordinary use of the word "time".
FEATURES = [
    ("second person 'you/your'",        r"\byou\b|\byour\b", re.I),
    ("question in the hook line",       r"\A[^\n]*\?|\?\s*\Z", re.I),
    ("mentions NAD+",                   r"\bNAD\+?\b", re.I),
    ("contains a % number",             r"\b\d+\s?%", re.I),
    ("emoji checkmark stack",           r"[\u2705\u2713\u2714\ufe0f\u26a1\U0001f3c6\u274c\u23f3\U0001f9e0\U0001f4aa\U0001f48a\U0001f501\u2728]", re.I),
    ("proof/science credential",        r"third-party|clinically|peer-review|stud(y|ies)|certificate of analysis|COA|NSF|placebo", re.I),
    ("'declines with age' mechanism",   r"declin|drops?|depletes?|as you age|with age", re.I),
    ("offer / promo code",              r"\b(code|save|% off|OFF|discount|free shipping|limited time|flash sale)\b", re.I),
    ("explicit CTA in body",            r"\U0001f449|click the link|tap below|link in (our |my )?bio|shop now|see if you qualify|take the (quick )?quiz", re.I),
    ("first-person testimonial voice",  r"\bI\b|\bmy\b|\bme\b", 0),
    ("authority borrow",                r"TIME|Vogue|WSJ|New York Post|Entrepreneur|mindbodygreen|Huberman|Harvard|Nobel|Dr\.|M\.D|MD\b|Ph\.D", 0),
    ("hashtags",                        r"#\w+", re.I),
    ("competitor takedown",             r"not all|most .*(don't|dont|fail)|unlike|others|competitor|isn't new|fake|cheap filler", re.I),
]

def stats(rows):
    weight, longest = collections.Counter(), collections.defaultdict(int)
    for r in rows:
        copy = r["Ad Copy"].strip()
        if not copy:
            continue
        weight[copy] += 1
        longest[copy] = max(longest[copy], days(r))
    copies, total = list(weight), sum(weight.values())
    print(f"unique ads: {len(rows)} | unique copies: {len(copies)} | ads with copy: {total}\n")
    print("STRUCTURAL FEATURES")
    for label, pattern, flags in FEATURES:
        hits = [c for c in copies if re.search(pattern, c, flags)]
        w = sum(weight[c] for c in hits)
        print(f"  {label:34s} copies {len(hits):3d} ({100*len(hits)/len(copies):4.1f}%)"
              f"   ads {w:3d} ({100*w/total:4.1f}%)")
    lengths = [len(c) for c in copies]
    print(f"\nlength: median {statistics.median(lengths):.0f} chars, "
          f"mean {statistics.mean(lengths):.0f}, min {min(lengths)}, max {max(lengths)}")
    print("\nLONGEST-RUNNING COPY (days live is our proxy for a winner)")
    for c in sorted(copies, key=lambda c: -longest[c])[:15]:
        print(f"  {longest[c]:4d}d  x{weight[c]:2d} ads | {c.splitlines()[0][:95]}")

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    data = load(directory)
    with open("ad_copy_deduplicated.txt", "w", encoding="utf-8") as fh:
        dump_copy(data, fh)
    stats(data)
