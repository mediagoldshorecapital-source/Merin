#!/usr/bin/env python3
"""Scaffold a numbered creative brief + script from the engine templates.

Usage:
  python3 tools/new_brief.py --format F04 --hook H05 --angle A03 --icp linda \
      --awareness problem --bucket iteration --parent PI_LIN_PA_F04_A03_H05_9x16_v1

  python3 tools/new_brief.py --list        # show the libraries and exit
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine_lib as E  # noqa: E402


def show_libraries() -> None:
    for title, table in (
        ("FORMATS", E.formats()),
        ("HOOKS", E.hooks()),
        ("ANGLES", E.angles()),
    ):
        print(f"\n{title}")
        print("-" * len(title))
        for entry in table.values():
            status = entry.meta.get("status", "")
            tag = f"  [{status}]" if status else ""
            print(f"  {entry}{tag}")
    print("\nICPs: " + ", ".join(E.ICPS))
    print("AWARENESS: " + ", ".join(E.AWARENESS))


def build(args: argparse.Namespace) -> tuple[Path, Path]:
    fmts, hks, angs = E.formats(), E.hooks(), E.angles()
    for key, table, label in (
        (args.format, fmts, "format"),
        (args.hook, hks, "hook"),
        (args.angle, angs, "angle"),
    ):
        if key not in table:
            raise SystemExit(
                f"unknown {label} '{key}'. Run with --list to see valid ids."
            )
    if args.icp not in E.ICPS:
        raise SystemExit(f"unknown icp '{args.icp}' (linda|robert)")
    if args.awareness not in E.AWARENESS:
        raise SystemExit(f"unknown awareness '{args.awareness}'")

    fmt, hook, angle = fmts[args.format], hks[args.hook], angs[args.angle]
    icp_code, icp_desc = E.ICPS[args.icp]
    aware_code = E.AWARENESS[args.awareness]

    brief_id = E.next_brief_id()
    name = (
        f"PI_{icp_code}_{aware_code}_{fmt.id}_{angle.id}_{hook.id}"
        f"_{args.ratio}_v{args.version}"
    )
    slug = f"{brief_id}_{fmt.id}-{angle.id}-{hook.id}-{icp_code}"
    outdir = E.BRIEFS / slug
    outdir.mkdir(parents=True, exist_ok=True)

    header = "\n".join(
        [
            f"<!-- generated {dt.date.today().isoformat()} by tools/new_brief.py -->",
            "",
            f"**Brief ID:** {brief_id}",
            f"**Creative name:** `{name}`",
            f"**Slate bucket:** {args.bucket}",
            f"**Parent creative:** {args.parent or '—'}",
            f"**ICP:** {icp_desc}",
            f"**Awareness:** {args.awareness.title()}-Aware",
            f"**Format:** {fmt}  ({fmt.meta.get('length', '')}, "
            f"pairs with {fmt.meta.get('pairs', '')})",
            f"**Angle:** {angle}  [{angle.meta.get('status', 'UNTESTED')}]",
            f"  - claim: {angle.meta.get('claim', '')}",
            f"  - defeats: {angle.meta.get('defeats', '')}",
            f"**Hook archetype:** {hook}",
            "",
            "> Open the matching cards before writing:",
            f"> `02-libraries/format-cards.md#{fmt.id.lower()}` · "
            f"`02-libraries/hook-bank.md#{hook.id.lower()}` · "
            f"`02-libraries/angle-map.md#{angle.id.lower()}`",
            "",
            "---",
            "",
        ]
    )

    brief_path = outdir / "brief.md"
    script_path = outdir / "script.md"
    brief_body = (E.TPL / "creative-brief.md").read_text(encoding="utf-8")
    script_body = (E.TPL / "script-template.md").read_text(encoding="utf-8")
    brief_path.write_text(
        header + brief_body.replace("B-XXXX", brief_id), encoding="utf-8"
    )
    script_path.write_text(
        header + script_body.replace("B-XXXX", brief_id).replace(
            "`<creative name>`", f"`{name}`"
        ),
        encoding="utf-8",
    )
    return brief_path, script_path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list", action="store_true", help="print libraries and exit")
    ap.add_argument("--format", "-f", help="format id, e.g. F04")
    ap.add_argument("--hook", "-k", help="hook archetype id, e.g. H05")
    ap.add_argument("--angle", "-a", help="angle id, e.g. A03")
    ap.add_argument("--icp", "-i", default="linda", help="linda|robert")
    ap.add_argument(
        "--awareness", "-w", default="problem", help="unaware|problem|solution|product"
    )
    ap.add_argument(
        "--bucket", "-b", default="Adjacent", help="Iteration|Adjacent|Wild"
    )
    ap.add_argument("--parent", "-p", default="", help="parent creative name")
    ap.add_argument("--ratio", default="9x16")
    ap.add_argument("--version", "-v", default="1")
    args = ap.parse_args()

    if args.list:
        show_libraries()
        return
    if not (args.format and args.hook and args.angle):
        ap.error("--format, --hook and --angle are required (or use --list)")

    brief, script = build(args)
    print(f"created {brief.relative_to(E.ROOT.parent)}")
    print(f"created {script.relative_to(E.ROOT.parent)}")


if __name__ == "__main__":
    main()
