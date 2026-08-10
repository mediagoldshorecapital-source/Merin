# NMN Pain-Point → Creative Brief Matrix

Thirty customer pain points for **NMN Complex**, each mapped to a producible ad
brief. A designer should be able to build the poster, and an editor cut the reel,
from a single row without asking a follow-up question.

- Working file: `nmn-creative-matrix.xlsx` — 3 sheets, filter/sort, tracker columns
- Report: `report.html` (standalone)
- Published: https://claude.ai/code/artifact/e6583e78-1538-4eda-80ad-32f71346b1f6

**Sources.** Pain points from the *NMN Deep Customer Intelligence Report*
(20 May 2026). Copy structures and evidence tiers from the six-month teardown of
1,220 Meta ads / $381K spend in `analysis/meta-creative-teardown/`.

## Coverage

| Cut | Breakdown |
| --- | --- |
| Persona | Linda 25 · Robert 5 |
| Evidence tier | Proven 8 · Adjacent 10 · Untested 12 |
| Category | Psychological/identity 10 · Physiological/symptom 9 · Comparative/trust 5 · Demographic/situational 3 · Behavioural/purchase-friction 3 |
| Funnel | Cold 22 · Warm 4 · Retention 3 · All stages 1 |

**Evidence tier** = how much budget a concept has earned. *Proven* has winning ads
behind it, *adjacent* is a variant of a winner, *untested* is new. Don't launch
twelve untested concepts at once.

## Columns

`# · Persona · Category · Evidence tier · Funnel stage · Pain point ·
Surface pain · Deep pain · Evidence anchor · Format · Angle · Qualifying hook ·
Heading · Subheading · Idea · Creative description (poster) ·
Video description (reel)` — plus `Owner · Status · Asset link` for your team.

## The rule that governs all thirty

In this account, **hook rate, hold rate and CTR all correlate *negatively* with
return**, in all seven months measured. Losing ads buy 36% more clicks and convert
them 39% worse ($58.09 CPA vs $31.90). So every hook here is written to
**disqualify** — to give a non-buyer a reason to scroll past. Several look
narrower and plainer than a normal brief. That is deliberate.

### Non-negotiables

1. Hooks qualify, they don't attract.
2. **Committed verbs only** — *plummeting / collapsing / rebuild*. Never
   *naturally declines / helps support / may assist*. This is the 0.92-vs-1.41
   ROAS difference.
3. **Never "75% OFF" in a headline** — lost on conversions-per-click 5 months out
   of 5. Lead with the per-bottle anchor ($29.98 → $16.66).
4. Talent must read 58–68.
5. Reels: 20s, hook inside 3s, captions burned in.
6. Plain beats polished — the winners look homemade.
7. Judge on **conversions per click**: ≥4.0% scale · 3.0–4.0% hold · <2.8% kill,
   after ~40 clicks (≈$60). Read from Meta, not the pixel (checkout event fires
   on ~63% of purchases).

## Brief these three first

- **#16 — "Not all NMN is created equal"** · *Proven.* Best structure by CPM
  ($57.47 vs $98.37), 3 of 12 all-time winners — and it has **only ever run on
  Astaxanthin (~4% of revenue)**, never on NMN (94%). Highest expected value in
  the set.
- **#9 — "Slept eight hours. Woke up like it was four."** · *Proven.* The most
  self-identifying line in the whole research. Should be your highest-volume
  angle.
- **#26 — "You watched him slow down. You swore you wouldn't."** · *Untested.*
  Robert is reported at 1.81 ROAS, the only segment above the ~1.70 breakeven,
  with zero creative written to him.

## Flags before anything ships

- **#14 (weight)** — must carry no weight-loss claim; needs legal review.
- **#23 (cancellation)** — verify self-serve cancellation is real before claiming
  it, especially as 97% of orders are now subscriptions.
- **#15 (joints)** — blocked until Multi Collagen COGS is populated; margin
  currently unknown.

## Naming convention

```
NMN_[PainPoint#]_[Angle]_[Format]_[Variant]_[YYYYMM]
e.g. NMN_16_QualityContrast_DemoCOA_A_202608
```

Three separate rows currently exist for what looks like one ad
(`- Video - Ad -2`, `- Video - Ad - 2`, `Video - Ad - 2`), which fragments every
angle-level report. Adopt this so new assets are analysable on arrival.

## Caveats

Ad performance behind the tiers is Meta channel-reported — valid for ranking
creative against creative, not as absolute profit measures, since TW pixel
attribution doesn't exist before June 2026. Robert's 1.81 ROAS is carried from the
research and is not independently verifiable in the warehouse. All copy is a
production brief, not legally reviewed final copy.

## Regenerating

Both outputs build from one source, `matrix_data.py`, via `build_xlsx.py` and
`build_html.py` (kept in the session scratchpad). Edit the data, re-run both, so
spreadsheet and report never drift apart.
