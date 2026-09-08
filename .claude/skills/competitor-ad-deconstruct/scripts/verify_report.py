#!/usr/bin/env python3
"""
Prove the deconstruction report is grounded in the actual recording.

Checks, in order of severity:

  FAIL  every quote in Phase 1 (beat transcript) and Phase 3 (audit table,
        column 1) appears verbatim in the ASR output
  FAIL  beat timestamps are ordered, non-inverted, and inside the real duration
  FAIL  Prime-facing copy (Phases 4-6) contains no drug/disease claim, banned
        trope, profanity, or competitor brand name
  WARN  dollar figures and mg doses match the approved spec sheet
  WARN  adapted lines have not simply copied the competitor's wording

A quote that fails the first check is the failure mode this whole skill exists to
prevent: a sentence nobody actually said, presented as evidence.

Usage:
  python3 verify_report.py report.md --transcript workdir/transcript.json
"""
import argparse, difflib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_RULES = os.path.join(HERE, "..", "references", "compliance_rules.json")

RESET, RED, YEL, GRN, BOLD = "\033[0m", "\033[31m", "\033[33m", "\033[32m", "\033[1m"

# Uncertainty markers the writer is told to insert; they are annotations about
# the recording, not words from it, so they are stripped before matching.
MARKER_RE = re.compile(
    r"\[(?:inaudible|no speech|unclear|unintelligible|crosstalk|music|sic)[^\]]*\]",
    re.I)

def norm(t):
    t = (t or "").lower()
    t = t.replace("’", "'").replace("‘", "'")
    t = t.replace("“", '"').replace("”", '"')
    t = t.replace("–", "-").replace("—", "-").replace("…", "...")
    t = MARKER_RE.sub(" ", t)
    t = re.sub(r"[^a-z0-9'\s]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()

def toks(t):
    return norm(t).split()

def sec(mmss):
    parts = [int(x) for x in mmss.split(":")]
    if len(parts) == 3: return parts[0]*3600 + parts[1]*60 + parts[2]
    return parts[0]*60 + parts[1]

# ---------- report parsing ----------

TIME = r"(\d{1,2}:\d{2}(?::\d{2})?)"
BEAT_RE = re.compile(
    r"^\s*[-*]?\s*\*{0,2}([A-Za-z][A-Za-z /&'\-]*?)\*{0,2}\s*\(" + TIME +
    r"\s*[–\-—]\s*(?:" + TIME + r"|end|End|END)\)\s*\*{0,2}\s*:?\s*\*{0,2}\s*(.*)$")

def split_sections(md):
    """Map 'phase 1' -> text.

    Subheadings inside a phase (e.g. '### Timestamped Transcript') belong to that
    phase, so only a phase heading or a new top-level '# Video N' heading starts a
    new section. Getting this wrong silently empties Phase 1 and makes the whole
    verification vacuous, which is worse than a loud parse error.
    """
    secs, cur, buf = {}, "_preamble", []

    def flush(nxt):
        nonlocal buf, cur
        secs[cur] = secs.get(cur, "") + "\n" + "\n".join(buf)
        cur, buf = nxt, []

    for line in md.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level, title = len(m.group(1)), m.group(2).lower()
            pm = re.search(r"phase\s*([1-9])", title)
            if pm:
                flush(f"phase {pm.group(1)}")
            elif level == 1:
                flush(title[:60])
            else:
                buf.append(line)   # subsection of the current phase
        else:
            buf.append(line)
    flush(None)
    return secs

def quotes_in(text):
    """Pull quoted strings; fall back to the raw line for unquoted beats."""
    out = []
    for q in re.findall(r'"([^"]{4,})"|“([^”]{4,})”', text):
        out.append(q[0] or q[1])
    return out

def parse_beats(text):
    beats = []
    for line in text.splitlines():
        m = BEAT_RE.match(line.strip())
        if not m:
            continue
        name, t0, t1, rest = m.group(1).strip(), m.group(2), m.group(3), m.group(4)
        qs = quotes_in(rest) or ([rest.strip()] if len(rest.strip()) > 8 else [])
        beats.append({"name": name, "start": t0, "end": t1, "quotes": qs, "raw": line})
    return beats

def table_rows(text):
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if not (s.startswith("|") and s.count("|") >= 3): continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c): continue
        if cells and re.search(r"spoken audio line|time\s*/\s*beat|audio\s*/\s*spoken",
                               cells[0], re.I): continue
        rows.append(cells)
    return rows

# ---------- checks ----------

def check_verbatim(quote, hay_norm, hay_raw):
    """Each ellipsis-separated fragment must be a contiguous run of real words."""
    frags = [f for f in re.split(r"\.{3}|…", quote) if norm(f)]
    results = []
    for f in frags:
        n = norm(f)
        w = n.split()
        if len(w) < 3:
            results.append(("skip", f, "fragment under 3 words — not checkable")); continue
        if n in hay_norm:
            results.append(("ok", f, "")); continue
        # find the nearest real passage so the writer can fix it fast
        hw = hay_norm.split()
        best, bs = "", 0.0
        for i in range(0, max(1, len(hw) - len(w) + 1)):
            cand = " ".join(hw[i:i + len(w)])
            r = difflib.SequenceMatcher(None, n, cand).ratio()
            if r > bs: bs, best = r, cand
        results.append(("fail", f, f"closest actual audio ({bs:.0%}): \"{best}\""))
    return results

def word_hits(text, terms):
    low = norm(text)
    hits = []
    for t in terms:
        tn = norm(t)
        if not tn: continue
        if re.search(r"(?<!\w)" + re.escape(tn) + r"(?!\w)", low):
            hits.append(t)
    return hits

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--transcript", required=True, help="transcript.json or .txt")
    ap.add_argument("--rules", default=DEFAULT_RULES)
    ap.add_argument("--strict-similarity", action="store_true",
                    help="treat copied competitor wording as a hard failure")
    a = ap.parse_args()

    md = open(a.report, encoding="utf-8").read()
    rules = json.load(open(a.rules, encoding="utf-8"))

    duration, tmeta = None, {}
    if a.transcript.endswith(".json"):
        d = json.load(open(a.transcript, encoding="utf-8"))
        tmeta = d.get("meta", {})
        duration = tmeta.get("duration")
        hay_raw = " ".join(s.get("text", "") for s in d.get("segments", []))
    else:
        hay_raw = open(a.transcript, encoding="utf-8").read()
        hay_raw = "\n".join(l for l in hay_raw.splitlines() if not l.startswith("#"))
    hay_norm = norm(hay_raw)
    if not hay_norm:
        print(f"{RED}FAIL: transcript is empty — there is nothing to verify against.{RESET}")
        sys.exit(1)

    secs = split_sections(md)
    fails, warns, checked = [], [], 0

    print(f"{BOLD}=== Verifying {os.path.basename(a.report)} ==={RESET}")
    if tmeta:
        print(f"Source: {os.path.basename(tmeta.get('source',''))} | "
              f"{tmeta.get('backend')}/{tmeta.get('model')} | "
              f"{tmeta.get('word_count','?')} words\n")

    # --- 1. Phase 1 beat quotes -------------------------------------------
    beats = parse_beats(secs.get("phase 1", ""))
    if not beats:
        fails.append("Phase 1 has no parseable beat lines. Expected: "
                     '**Hook (0:00–0:07):** "verbatim words"')
    for b in beats:
        if not b["quotes"]:
            warns.append(f'Phase 1 beat "{b["name"]}" carries no quoted line.')
        for q in b["quotes"]:
            for status, frag, note in check_verbatim(q, hay_norm, hay_raw):
                checked += 1
                if status == "fail":
                    fails.append(f'Phase 1 [{b["name"]} {b["start"]}] not in audio: '
                                 f'"{frag.strip()[:90]}"\n      {note}')
                elif status == "skip":
                    checked -= 1

    # --- 2. timestamps ------------------------------------------------------
    prev_end = -1.0
    for b in beats:
        s0 = sec(b["start"])
        s1 = sec(b["end"]) if b["end"] else None
        if s1 is not None and s1 <= s0:
            fails.append(f'Phase 1 beat "{b["name"]}" ends before it starts '
                         f'({b["start"]}–{b["end"]}).')
        if s0 + 0.01 < prev_end - 1.0:
            fails.append(f'Phase 1 beat "{b["name"]}" starts at {b["start"]}, '
                         f'before the previous beat ended — beats must run forward.')
        if duration and s1 and s1 > duration + 2:
            fails.append(f'Phase 1 beat "{b["name"]}" ends at {b["end"]} but the clip '
                         f'is only {int(duration//60)}:{int(duration%60):02d} long.')
        prev_end = s1 if s1 is not None else s0
    if beats and duration and sec(beats[0]["start"]) > 3:
        warns.append(f'First beat starts at {beats[0]["start"]} — is the opening '
                     f'of the ad missing from the breakdown?')

    # --- 3. Phase 3 audit quotes -------------------------------------------
    p3 = table_rows(secs.get("phase 3", ""))
    if not p3:
        warns.append("Phase 3 audit table has no data rows.")
    for r in p3:
        for q in (quotes_in(r[0]) or [r[0]]):
            for status, frag, note in check_verbatim(q, hay_norm, hay_raw):
                checked += 1
                if status == "fail":
                    fails.append(f'Phase 3 column 1 not in audio: "{frag.strip()[:90]}"'
                                 f'\n      {note}')
                elif status == "skip":
                    checked -= 1

    # --- 4. compliance on Prime-facing copy --------------------------------
    prime_text_parts, p4_lines = [], []
    for key in ("phase 4", "phase 5", "phase 6"):
        body = secs.get(key, "")
        if not body: continue
        if key == "phase 4":
            for r in table_rows(body):
                if len(r) >= 2:
                    p4_lines.append(r[1]); prime_text_parts.append(r[1])
        else:
            prime_text_parts.append(body)
    prime_text = "\n".join(prime_text_parts)

    if not prime_text.strip():
        warns.append("No Prime-facing copy found in Phases 4-6 — nothing to "
                     "compliance-check.")

    for label, terms, kind in (
        ("drug/disease claim", rules["drug_disease_claims"], "fail"),
        ("banned trope", rules["banned_tropes"], "fail"),
        ("profanity", rules["profanity"], "fail"),
        ("competitor brand", rules["competitor_brands"], "fail"),
    ):
        for h in word_hits(prime_text, terms):
            msg = (f'Compliance — {label} "{h}" appears in Prime copy (Phases 4-6). '
                   f'Rewrite as a structure/function statement or cut the beat.')
            (fails if kind == "fail" else warns).append(msg)

    # --- 5. spec grounding (warnings: judgment calls) -----------------------
    approved = set(rules["approved_prices"])
    for amt in re.findall(r"\$\s?(\d{1,4}(?:\.\d{2})?)", prime_text):
        if amt.rstrip("0").rstrip(".") not in {p.rstrip("0").rstrip(".") for p in approved}:
            warns.append(f'Price ${amt} is not on the approved sheet '
                         f'({", ".join("$"+p for p in rules["approved_prices"])}). '
                         f'Competitor/category anchors are fine — confirm this is one.')
    for mg in re.findall(r"(\d[\d,]*)\s*mg", prime_text, re.I):
        if mg.replace(",", "") != str(rules["product_facts"]["dose_mg"]):
            warns.append(f'Dose "{mg}mg" appears in Prime copy; the product is '
                         f'{rules["product_facts"]["dose_text"]}. Fine as a contrast '
                         f'with underdosed competitors — confirm that is the intent.')

    # --- 6. adapted-expression distance ------------------------------------
    thresh = float(rules.get("expression_similarity_threshold", 0.8))
    src_quotes = [q for b in beats for q in b["quotes"]]
    for line in p4_lines:
        ln = norm(line)
        if len(ln.split()) < 6: continue
        for sq in src_quotes:
            r = difflib.SequenceMatcher(None, ln, norm(sq)).ratio()
            if r >= thresh:
                m = (f'Phase 4 line is {r:.0%} identical to the competitor\'s own '
                     f'wording: "{line.strip()[:80]}..." — keep their beat structure '
                     f'and cadence, but say it in Prime\'s words.')
                (fails if a.strict_similarity else warns).append(m)
                break

    # --- report -------------------------------------------------------------
    print(f"Verbatim fragments checked : {checked}")
    print(f"Beats parsed               : {len(beats)}")
    print(f"Audit rows parsed          : {len(p3)}")
    print(f"Prime copy lines           : {len(p4_lines)}\n")

    for w in warns:
        print(f"{YEL}WARN{RESET} {w}")
    for f in fails:
        print(f"{RED}FAIL{RESET} {f}")

    if fails:
        print(f"\n{RED}{BOLD}{len(fails)} failure(s).{RESET} Fix by requoting from "
              f"transcript.txt — never by adjusting the check. A quote that is not "
              f"in the audio is not a quote.")
        sys.exit(1)
    print(f"\n{GRN}{BOLD}PASSED{RESET} — {checked} quoted fragments all trace to the "
          f"recording; {len(warns)} warning(s) for review.")
    sys.exit(0)

if __name__ == "__main__":
    main()
