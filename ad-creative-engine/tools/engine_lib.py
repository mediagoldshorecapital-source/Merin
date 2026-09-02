"""Shared library parsing for the ad creative engine.

Reads the markdown libraries so the tools always reflect what is actually written
in 02-libraries/ rather than a hardcoded copy that drifts out of sync.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "02-libraries"
TPL = ROOT / "03-templates"
BRIEFS = ROOT / "06-briefs"


@dataclass
class Entry:
    id: str
    name: str
    meta: dict = field(default_factory=dict)

    def __str__(self) -> str:
        return f"{self.id} — {self.name}"


def _read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"missing library file: {path}")
    return path.read_text(encoding="utf-8")


def _parse_headings(text: str, prefix: str) -> dict[str, Entry]:
    """Pull '## F01 — Name' / '### A01 — Name' style headings."""
    out: dict[str, Entry] = {}
    pattern = re.compile(rf"^#{{2,4}}\s+({prefix}\d\d)\s+[—-]\s+(.+?)\s*$", re.M)
    for match in pattern.finditer(text):
        out[match.group(1)] = Entry(match.group(1), match.group(2).strip())
    return out


def formats() -> dict[str, Entry]:
    text = _read(LIB / "format-cards.md")
    entries = _parse_headings(text, "F")
    for fid, entry in entries.items():
        block = text.split(f"## {fid} — ", 1)[1][:400]
        for key, pat in (
            ("length", r"\*\*Length:\*\*\s*([^·\n]+)"),
            ("awareness", r"\*\*Awareness:\*\*\s*([^·\n]+)"),
            ("icp", r"\*\*ICP:\*\*\s*([^\n]+)"),
            ("pairs", r"\*\*Pairs with:\*\*\s*([^·\n]+)"),
            ("angles", r"\*\*Angles:\*\*\s*([^\n]+)"),
        ):
            m = re.search(pat, block)
            if m:
                entry.meta[key] = m.group(1).strip()
    return entries


def hooks() -> dict[str, Entry]:
    return _parse_headings(_read(LIB / "hook-bank.md"), "H")


def angles() -> dict[str, Entry]:
    text = _read(LIB / "angle-map.md")
    entries = _parse_headings(text, "A")
    for aid, entry in entries.items():
        block = text.split(f"### {aid} — ", 1)[1][:900]
        for key, pat in (
            ("claim", r"\*\*Claim:\*\*\s*([^\n]+)"),
            ("defeats", r"\*\*Defeats:\*\*\s*([^\n]+)"),
            ("icp", r"\*\*ICP:\*\*\s*([^·\n]+)"),
            ("awareness", r"\*\*Awareness:\*\*\s*([^\n]+)"),
            ("status", r"\*\*Status:\*\*\s*`([A-Z]+)`"),
            ("pairings", r"\*\*Best pairings:\*\*\s*([^\n]+)"),
        ):
            m = re.search(pat, block)
            if m:
                entry.meta[key] = m.group(1).strip()
    return entries


ICPS = {
    "linda": ("LIN", "Linda — woman 52-68, daily fatigue and visible aging"),
    "robert": ("ROB", "Robert — man 48-66, spec-driven, recovery and dose"),
}

AWARENESS = {"unaware": "UN", "problem": "PA", "solution": "SA", "product": "PDA"}


def next_brief_id() -> str:
    BRIEFS.mkdir(exist_ok=True)
    used = []
    for p in BRIEFS.glob("B-*"):
        m = re.match(r"B-(\d+)", p.name)
        if m:
            used.append(int(m.group(1)))
    return f"B-{max(used, default=0) + 1:04d}"
