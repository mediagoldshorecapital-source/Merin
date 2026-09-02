# Testing Framework

The engine's job isn't to make good ads. It's to make the *next* batch better than the
last one. That only happens if every ad was a question with an answer.

---

## 1. Every creative is a hypothesis

No hypothesis, no brief. Written **before** launch, in the brief, in this form:

> **We believe** [ICP] at [awareness] will respond to [angle] delivered as [format]
> **because** [the belief or objection it addresses].
> **We'll know we're right if** [metric] beats [control] by [margin] within [timeframe].

If you can't fill it in, you don't have a test — you have a guess with a budget.

---

## 2. The one-variable rule

An iteration changes **one** element against its parent:

`hook_line` · `first_frame` · `ost` · `creator` · `cta` · `runtime` · `music` · `angle` · `format`

Change two and the result is uninterpretable. If two things must change, it's a new v1
and it goes in the Adjacent or Wild bucket, where you're not claiming attribution.

---

## 3. The diagnostic funnel — read *where* it broke, not *whether* it won

This is the most valuable habit in the whole system. A "losing" ad usually contains a
winning component.

```
Impressions
   │  ── hook rate (3-sec views ÷ impressions) ──▶  weak? THE FIRST 3 SECONDS FAILED
   ▼                                                Body may be fine. RE-HOOK, don't kill.
3-sec views
   │  ── hold to 25% ──▶ cliff here? THE BRIDGE BROKE THE HOOK'S PROMISE
   ▼                     Hook wrote a cheque the setup didn't cash.
25% viewers
   │  ── hold to 50–75% ──▶ decay here? MECHANISM IS BORING OR TOO LONG
   ▼                        Cut 20% of the biology.
Completions
   │  ── outbound CTR ──▶ low? THE AD NEVER EARNED THE ASK
   ▼                      Objections unhandled, or CTA is limp.
Clicks
   │  ── CPA / ROAS ──▶ bad? AUDIENCE OR LANDING PAGE MISMATCH
   ▼                    Not a creative problem. Stop rewriting the ad.
Purchases
```

**Rule:** never kill an ad with a strong hook rate. Strip the hook into `/hooks/` and
put it on a body that converts. Hooks and bodies are separate assets and should be
managed as separate assets.

---

## 4. Decision gates

Set the actual thresholds from **your own account's trailing 90-day medians** — the
numbers below are starting positions to calibrate against, not benchmarks to trust
blind. What matters is that a gate exists and is applied consistently.

| Gate | Condition | Action |
|---|---|---|
| **SCALE** | CPA ≤ target **and** spend ≥ 3× target CPA **and** ≥ 4 days live | Raise budget ≤ 30%/day. Brief 3 iterations against it immediately |
| **ITERATE** | CPA within ~20% of target, healthy hold curve | New hooks on the same body. This is the 60% bucket |
| **RE-HOOK** | Hook rate below account median, but hold-past-25% at/above median | Body works, open doesn't. Swap the first 4 seconds only |
| **RE-BODY** | Hook rate strong, cliff before 25% | Keep the hook file. Rebuild the bridge and mechanism |
| **KILL** | Spend ≥ 3× target CPA, no purchases, hook rate below median | Kill. Log the learning. Do not resurrect without a changed variable |
| **HOLD** | Spend < 1.5× target CPA | Too early. Do not touch it. Most creative gets killed before it has said anything |

**Minimum read:** 3× target CPA in spend *or* 4 days live, whichever is later. Judging a
creative at 20% of a target CPA is reading noise and calling it a decision.

---

## 5. What "statistically meaningful" means here

You will almost never have a clean significance test at creative level, and pretending
otherwise wastes weeks. Practical standard:

- **Directional** (< 1× target CPA in spend): note it, act on nothing.
- **Actionable** (1–3× target CPA): act on *hook rate and hold*, which stabilise fast because they're measured on impressions. Do not act on CPA yet.
- **Conclusive** (≥ 3× target CPA, ≥ 4 days, ≥ ~30 conversions for CPA calls): act on CPA/ROAS.

Upper-funnel metrics (hook rate, hold) are trustworthy at low spend. Lower-funnel
metrics are not. Structure your decisions accordingly — that's what the gate table above
is doing.

---

## 6. Testing ladder — test in this order

Cheapest and highest-variance first:

1. **Hook line** — same body, 4–6 opens. Highest leverage, near-zero cost.
2. **First frame / thumbnail** — same ad, different opening frame.
3. **OST wording** — the muted viewer's whole experience.
4. **Angle** — same format and ICP, different argument.
5. **Format** — same angle, different shape.
6. **Creator / casting** — expensive, slow, and often the real answer for Linda.
7. **Offer / CTA mechanic** — bundle vs. single, discount vs. supply framing.

Most teams start at 5 and 6 because they're the visible ones. Steps 1–3 produce more
wins per dollar than 4–7 combined.

---

## 7. Slate composition

| Bucket | Share | Rule |
|---|---|---|
| **Iteration** | 60% | Only against creatives that hit SCALE or ITERATE |
| **Adjacent** | 25% | Proven format × new angle, or proven angle × new ICP. One step from known |
| **Wild** | 15% | Untested format or `UNTESTED` angle. Expected to lose most weeks |

The wilds feel like waste right up until the month the winners fatigue. Then they're the
only thing standing between you and a rebuild from zero. Protect the 15%.

---

## 8. Creative fatigue

Watch **frequency** and **hook rate on the same creative over time**, not CPA — CPA
degrades last and by then you've lost a week.

| Signal | Read | Action |
|---|---|---|
| Hook rate down > 20% from its own week-1 baseline | Audience has seen it | Re-hook, same body |
| Frequency > 2.5 with flat CPA | Nearing saturation | Queue iterations now |
| CPA up > 25% over 7 days at flat spend | Fatigued | Rotate out; keep the body for a later re-hook |
| An angle's median hook rate declining across 12+ creatives | **Angle** fatigue, not creative fatigue | Rest the angle 8 weeks. Mark `FATIGUED` in the angle map |

Angle fatigue is the one people miss. They keep making new ads for an argument the
market has already heard, and read the losses as a creative-quality problem.

---

## 9. The learning log

Bottom of `weekly-scorecard.md`. One line per resolved creative:

```
2026-09-12 | PI_LIN_PA_F04_A03_H05_9x16_v2
believed: peer testimonials would beat talking-head for Linda at problem-aware
result:   hook rate +34% vs control, CTR flat, CPA -12%
learned:  casting drives the hook, not the line. Recast three existing losers before rewriting them.
```

Read the whole log every month. Patterns show up across ten entries that are invisible
in any one of them — and the log is the only asset here that appreciates.
