# Meta Creative Teardown — Winners vs Losers (Feb–Aug 2026)

Six months of Meta creative for **Prime Ingredients** analysed for what separates
winning ads from losing ones: messaging, angles, creative mechanics, and how to
replicate the outliers.

- Report: `report.html` (standalone, no external assets)
- Published version: https://claude.ai/code/artifact/fcd9380a-f5f5-464c-a339-413ebfae6616
- Companion to: `analysis/triple-whale-six-month-audit/`

**Scope:** 8 Feb – 7 Aug 2026 · 1,220 ads · $381K spend · 68 ads over $700 in a
deep-dive set.

## Three constraints on the analysis (read first)

1. **Uses Meta channel-reported conversions, not Triple Whale attribution.** The
   TW pixel produced no data before June 2026, so it cannot span six months.
   Meta-reported ROAS runs below blended store ROAS by a varying factor
   (0.47×–1.00× by month), so these figures are valid for **ranking ads against
   each other** and invalid as an absolute profit bar. "Winner" = top-tier
   relative performance, not "profitable."
2. **The winner list is time-concentrated.** 11 of 12 winners launched Feb–Apr,
   when the whole account performed better. All headline claims are therefore
   tested *within* each month, where account-level decay cancels out.
3. **Ad longevity is an outcome, not a cause.** Winners ran 54 days vs losers 28
   because losers got turned off. Excluded from the diagnostic patterns.

## The core finding

**Engagement is inversely correlated with return.** The tiers are monotonic:

| Tier | Ads | Spend | ROAS | Hook | CTR | Conv/click | CPA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Winners | 12 | $44,112 | 1.98 | 32.1% | 5.29% | **4.26%** | **$31.90** |
| Marginal | 30 | $172,155 | 1.41 | 36.7% | 5.72% | 3.49% | $43.57 |
| Losers | 26 | $61,980 | 1.00 | 44.9% | 7.18% | **2.61%** | **$58.09** |

Losers buy 36% more clicks and convert them 39% worse. **Hook rate correlates
negatively with ROAS in all seven months** — never once positive. The most
predictive creative property is not stopping power, it is *qualification*.

## Angle league table (full population)

| Angle | Ads | Spend | ROAS | CPA |
| --- | ---: | ---: | ---: | ---: |
| A. "Not all Astaxanthin is created equal" — category-quality contrast | 355 | $49,464 | **1.41** | **$40.31** |
| E. "Tired of feeling tired as you age?" — direct symptom question | 146 | $146,474 | **1.41** | $44.36 |
| C. "WARNING…" — pattern interrupt | 77 | $58,501 | 1.31 | $45.92 |
| G. Other / mixed | 86 | $39,982 | 1.31 | $48.82 |
| B. "Unleash your glow" — tan benefit | 71 | $5,337 | 0.98 | $59.96 |
| F. "Feeling more tired as you age?" — soft educational | 436 | $54,582 | **0.92** | **$67.72** |
| D. First-person story | 49 | $7,093 | **0.83** | **$69.54** |

**Angle F is the expensive mistake** — second-most-produced angle, and among
high-spend ads it produced **0 winners and 9 losers**. Its CTR (5.48%) is
nearly identical to the winning angles, which is why it survived.

## Why E wins and F loses (same claim, 53% apart)

Both describe NAD+ decline. The difference is construction:

| Winner (E) | Loser (F) |
| --- | --- |
| Opens on a question, line-broken | Question buried in a paragraph |
| Second person — "your NAD+ levels" | Third person — "the molecule" |
| Committed verbs — *plummeting, boost, regain* | Hedged — *naturally drop, helps support* |
| Benefit triad, scannable | Benefits as prose |
| Explicit CTA | No CTA in visible portion |
| ~220 chars | Runs long, truncates mid-benefit |

Hedging is the copy-level version of the same disease as high-hook creative: it
maximises audience and minimises intent.

## The discount headline loses on click quality 5 months out of 5

`75% OFF TODAY ONLY` vs no headline, month-controlled — conversions per click:
2.50 vs 3.44 (Apr) · 2.62 vs 3.87 (May) · 2.59 vs 3.03 (Jun) · 2.66 vs 3.47
(Jul) · 2.49 vs 2.76 (Aug). ROAS worse in 4 of 5. Compounds with the audit
finding that prices already carry a permanent ~35% non-code discount.

## Replication playbook

1. **Template 1 — direct symptom question** (7 of 12 winners). Rotate symptom,
   dismissive explanation, benefit triad, CTA verb.
2. **Template 2 — category-quality contrast** (3 of 12 winners, best CPM at
   $57.47). Only ever used on Astaxanthin — **never tested on the NMN flagship,
   which is 93.5% of revenue.** Biggest untested opportunity.
3. **Template 3 — warning + named mechanism** (2 of 12). Winners name a specific
   mechanism; generic warnings sit at 1.31.
4. **Kill angles F and D** — $61,675 of combined spend at 0.91 average ROAS.
5. **Drop the discount headline** and re-test the field.
6. **Change the judging metric** — gate on conversions per click, not hook/CTR:
   ≥4.0% scale · 3.0–4.0% hold · <2.8% kill. Test budget ~40 clicks (~$60 at
   $1.50 CPC). Read from Meta, since the TW checkout event only fires on ~63%
   of purchases.
7. **Test the retention angle** — 97% of orders are subscriptions and recurring
   charges are the only profitable order type, yet not one ad in six months
   mentions subscription or replenishment.

## Method

`ads_table` via the Triple Whale MCP tools, read 10 August 2026. Angle
classification is by pattern-match on the opening of each ad's primary text;
"Other" holds ads matching no defined pattern. Correlations are Pearson on
per-ad monthly aggregates for ads with over $250 spend that month.
