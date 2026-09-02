#!/usr/bin/env python3
"""Propose a weekly creative slate from the engine libraries.

Applies the 60/25/15 portfolio split from 04-testing/testing-framework.md:
  - Iterations : new hooks on creatives you name as current winners
  - Adjacents  : PROVEN angles that are under-produced, on their best-fit formats
  - Wilds      : UNTESTED angles, which is where next quarter's winners come from

The planner is a starting point, not an oracle. It cannot know what you found in
this week's reviews. Override it.

Usage:
  python3 tools/combo_planner.py
  python3 tools/combo_planner.py --winners PI_LIN_PA_F04_A01_H05_9x16_v1,PI_ROB_SA_F06_A02_H06_9x16_v2
  python3 tools/combo_planner.py --size 11 --seed 3 --markdown
"""
from __future__ import annotations

import argparse
import math
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine_lib as E  # noqa: E402

# The five hook transforms from 02-libraries/hook-bank.md
TRANSFORMS = [
    ("person swap", "2nd person -> 1st person -> 3rd person observation"),
    ("specificity crank", "replace the vague noun with a number, a time, a place"),
    ("negation flip", "deny the false cause before asserting the real one"),
    ("stakes escalation", "state what the symptom costs, not what it is"),
    ("format transposition", "same claim delivered through a different archetype"),
]


def parse_pairings(raw: str) -> list[tuple[str, str]]:
    """'F02/H06, F06/H10' -> [('F02','H06'), ('F06','H10')]"""
    return re.findall(r"(F\d\d)\s*/\s*(H\d\d)", raw or "")


def icp_of(angle) -> str:
    """Pick the angle's primary ICP. '(primary)' wins; otherwise first mentioned."""
    raw = (angle.meta.get("icp") or "").lower()
    for name in ("linda", "robert"):
        if f"{name} (primary)" in raw:
            return name
    positions = {n: raw.find(n) for n in ("linda", "robert") if n in raw}
    return min(positions, key=positions.get) if positions else "linda"


def awareness_of(angle) -> str:
    """Lowest (coldest) awareness level the angle is written for."""
    raw = (angle.meta.get("awareness") or "").lower()
    for key in ("unaware", "problem", "solution", "product"):
        if key in raw:
            return key
    return "problem"


def plan(size: int, winners: list[str], seed: int) -> list[dict]:
    rng = random.Random(seed)
    angles = E.angles()
    formats = E.formats()
    hooks = E.hooks()

    n_iter = math.ceil(size * 0.60)
    n_adj = math.ceil(size * 0.25)
    n_wild = max(size - n_iter - n_adj, 0)

    slate: list[dict] = []

    # --- Iterations -------------------------------------------------------
    if winners:
        for i in range(n_iter):
            parent = winners[i % len(winners)]
            transform, how = TRANSFORMS[i % len(TRANSFORMS)]
            step = i // len(winners) + 1
            slate.append(
                {
                    "bucket": "Iteration",
                    "name": bump_version(parent, step),
                    "parent": parent,
                    "changed": "hook_line",
                    "note": f"{transform}: {how}",
                    "hypothesis": (
                        f"A {transform} on the winning hook lifts hook rate "
                        f"without touching the body that is already converting."
                    ),
                }
            )
    else:
        slate.append(
            {
                "bucket": "Iteration",
                "name": "(name your current winners with --winners)",
                "parent": "",
                "changed": "",
                "note": (
                    f"{n_iter} iteration slots reserved. Fill from this week's "
                    "SCALE/ITERATE verdicts in the scorecard."
                ),
                "hypothesis": "",
            }
        )

    # --- Adjacents: PROVEN angles on their best-fit format/hook -----------
    # Skip anything whose combination is already live as a named winner.
    live = {re.sub(r"_v\d+$", "", w) for w in winners}
    proven = [a for a in angles.values() if a.meta.get("status") == "PROVEN"]
    rng.shuffle(proven)
    picked = 0
    for angle in proven:
        if picked >= n_adj:
            break
        pairs = parse_pairings(angle.meta.get("pairings", ""))
        fmt_id, hook_id = pairs[0] if pairs else ("F01", "H05")
        icp = icp_of(angle)
        name = creative_name(icp, awareness_of(angle), fmt_id, angle.id, hook_id)
        if re.sub(r"_v\d+$", "", name) in live:
            continue  # already running; iterate on it instead of re-briefing it
        picked += 1
        slate.append(
            {
                "bucket": "Adjacent",
                "name": name,
                "parent": "",
                "changed": "angle",
                "note": (
                    f"{formats.get(fmt_id, fmt_id)} x {angle.name} "
                    f"x {hooks.get(hook_id, hook_id)}"
                ),
                "hypothesis": (
                    f"{angle.meta.get('claim', angle.name)} "
                    f"Defeats: {angle.meta.get('defeats', '')}"
                ),
            }
        )

    # --- Wilds: UNTESTED angles ------------------------------------------
    untested = [a for a in angles.values() if a.meta.get("status") == "UNTESTED"]
    rng.shuffle(untested)
    for angle in untested[:n_wild]:
        pairs = parse_pairings(angle.meta.get("pairings", ""))
        fmt_id, hook_id = pairs[0] if pairs else ("F01", "H05")
        icp = icp_of(angle)
        slate.append(
            {
                "bucket": "Wild",
                "name": creative_name(icp, awareness_of(angle), fmt_id, angle.id, hook_id),
                "parent": "",
                "changed": "angle+format",
                "note": (
                    f"UNTESTED angle. {formats.get(fmt_id, fmt_id)} "
                    f"x {hooks.get(hook_id, hook_id)}"
                ),
                "hypothesis": (
                    f"{angle.meta.get('claim', angle.name)} "
                    f"Expected to lose; run it to find out if the argument lands at all."
                ),
            }
        )
    return slate


def creative_name(icp: str, awareness: str, fmt: str, angle: str, hook: str) -> str:
    return (
        f"PI_{E.ICPS[icp][0]}_{E.AWARENESS[awareness]}_{fmt}_{angle}_{hook}_9x16_v1"
    )


def bump_version(name: str, step: int = 1) -> str:
    m = re.search(r"_v(\d+)$", name)
    if m:
        return re.sub(r"_v\d+$", f"_v{int(m.group(1)) + step}", name)
    return f"{name}_v{step + 1}"


def render(slate: list[dict], markdown: bool) -> str:
    if markdown:
        lines = [
            "| # | Bucket | Creative name | Parent | Changed | Hypothesis |",
            "|---|---|---|---|---|---|",
        ]
        for i, row in enumerate(slate, 1):
            lines.append(
                f"| {i} | {row['bucket']} | `{row['name']}` | {row['parent'] or '—'} "
                f"| {row['changed'] or '—'} | {row['hypothesis'] or row['note']} |"
            )
        return "\n".join(lines)

    out = []
    bucket = None
    for i, row in enumerate(slate, 1):
        if row["bucket"] != bucket:
            bucket = row["bucket"]
            out.append(f"\n{bucket.upper()}\n" + "-" * len(bucket))
        out.append(f"{i:2d}. {row['name']}")
        if row["parent"]:
            out.append(f"    parent: {row['parent']}  (changed: {row['changed']})")
        out.append(f"    {row['note']}")
        if row["hypothesis"]:
            out.append(f"    hypothesis: {row['hypothesis']}")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--size", type=int, default=11, help="briefs on the slate")
    ap.add_argument(
        "--winners",
        default="",
        help="comma-separated creative names with a SCALE/ITERATE verdict",
    )
    ap.add_argument("--seed", type=int, default=0, help="vary to reshuffle proposals")
    ap.add_argument("--markdown", action="store_true", help="scorecard-ready table")
    args = ap.parse_args()

    winners = [w.strip() for w in args.winners.split(",") if w.strip()]
    slate = plan(args.size, winners, args.seed)
    print(render(slate, args.markdown))
    if not args.markdown:
        print(
            "\nNext: scaffold each with tools/new_brief.py, then write the "
            "hypothesis before the brief."
        )


if __name__ == "__main__":
    main()
