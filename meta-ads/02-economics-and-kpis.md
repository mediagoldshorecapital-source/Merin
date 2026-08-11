# 02 — Economics & KPIs

This is where "measurable results" actually comes from. Every start, stop, and scale
decision in this account cites a number from this file. If you cannot cite one, you are not
allowed to touch the account.

---

## 1. The unit economics worksheet

Fill this in with **real trailing-30-day numbers** before launch. Re-run monthly.

| # | Input | Where to get it | Working value | **Your value** |
|---|-------|-----------------|---------------|----------------|
| A | Blended AOV | Shopify Analytics → Average order value, last 30d | `$58.00` | `$______` |
| B | COGS per order | Product cost × units in the average order | `$8.70` | `$______` |
| C | Shipping + fulfilment per order | 3PL/Shopify shipping cost ÷ orders | `$2.90` | `$______` |
| D | Payment processing | ≈ 2.9% of AOV + $0.30 | `$1.98` | `$______` |
| E | Returns / refund allowance | Refund $ ÷ gross revenue | `$1.16` (2%) | `$______` |
| F | **Contribution per order** | `A − B − C − D − E` | **`$43.26`** | `$______` |
| G | **Gross margin %** | `F ÷ A` | **`74.6%`** | `______%` |
| H | Repeat rate @ 120 days | Shopify / Klaviyo cohort | `35%` | `______%` |
| I | 2nd-order contribution | `F × H` | `$15.14` | `$______` |
| J | **120-day contribution (LTV proxy)** | `F + I` | **`$58.40`** | `$______` |

> The "working value" column is an **illustrative example** built on the source document's
> $58 AOV floor and typical supplement cost structure. It is not your P&L. Replace it.
> Every number downstream moves when you do.

---

## 2. The seven numbers

Derived from the worksheet. Write these on a sticky note.

| Number | Formula | Working value | **Yours** |
|--------|---------|---------------|-----------|
| 1. **Blended AOV** | worksheet A | `$58` | `$____` |
| 2. **Break-even CPA** | worksheet F | `$43.26` | `$____` |
| 3. **Break-even ROAS** | `1 ÷ G` | `1.34x` | `____x` |
| 4. **Target CPA** | see §3 | `$25` | `$____` |
| 5. **Target ROAS** | `A ÷ Target CPA` | `2.32x` | `____x` |
| 6. **Forced min spend / test ad set** | `1 × AOV` | `$58/day` | `$____/day` |
| 7. **Learning-phase floor** | `50 × Target CPA ÷ 7` | `$179/day` | `$____/day` |

Plus one production number:

| 8. **Creative quota** | `monthly spend ÷ $1,000` | at $9k/mo → **9 new ads/mo** | `____/mo` |

---

## 3. Setting Target CPA

The source document gives a target CPA of **$22–$28 per bundle**. Sanity-check it against
your own contribution rather than adopting it blindly.

```
Break-even CPA          $43.26   ← above this you lose money on the first order
LTV break-even CPA      $58.40   ← above this you lose money even counting reorders
Target CPA              $25.00   ← 58% of break-even. Leaves 31% of revenue as profit
```

**How to choose:**

| If your goal is… | Set Target CPA at | Rationale |
|------------------|-------------------|-----------|
| Maximum profit per order | 50–55% of break-even CPA | Slow growth, high margin |
| **Balanced growth (default)** | **55–65% of break-even CPA** | The $25 figure sits here |
| Aggressive share capture | 75–90% of break-even CPA | Only if repeat rate (H) is proven ≥ 35% and cash flow supports it |
| Land-grab / LTV bet | up to LTV break-even | Only with owner sign-off and a funded runway |

At `$43.26` break-even, the balanced band is **$23.79–$28.12** — which independently
confirms the document's $22–28. Good. Use **$25**.

**Set two thresholds, not one:**

| Threshold | Value | Meaning |
|-----------|-------|---------|
| **Target CPA** | `$25` | The number that must be beaten to earn a budget increase |
| **Tolerance CPA** | `$31` (Target × 1.25) | The number above which a *proven* asset becomes a kill candidate |

The gap between them is deliberate. Without it, ordinary week-to-week variance will make
you pause winners.

---

## 4. KPI dictionary — what you look at, and what you ignore

### Tier 1 — Decision KPIs (these drive actions)

| KPI | Where | Target | Read at |
|-----|-------|--------|---------|
| **Cost per Purchase** | Ads Manager, 7-day window | ≤ $25 | Ad set + account |
| **Amount Spent** | Ads Manager | — (it's a *proxy*, not a goal) | **Ad level — primary ToF signal** |
| **Blended MER** | Total revenue ÷ total ad spend | ≥ 2.3x | Account, weekly |
| **New Customer %** | Shopify / Triple Whale | ≥ 70% | Account, weekly |
| **CAC (blended)** | Total ad spend ÷ new customers | ≤ $25 | Account, weekly |
| **High-AOV rate** | `Purchase_HighAOV_Bundle` ÷ all purchases | ≥ 40% | Account, weekly |

> **Why "Amount Spent" is a Tier 1 KPI and not a vanity metric.** Under CBO, Meta routes
> budget to the creative it believes drives the most incremental value across the whole
> journey — including multi-click lift that ad-level ROAS never sees. A top-of-funnel video
> that quietly absorbs 40% of campaign spend is Meta telling you, in the only language it
> has, that this asset is carrying the account. Believe it.

### Tier 2 — Diagnostic KPIs (these explain, they don't decide)

| KPI | Healthy range | What a bad reading means |
|-----|---------------|--------------------------|
| CPM | $18–$45 (spikes in Q4/Q5) | High → external competition, or narrow effective audience, or low EMQ |
| CTR (all) | ≥ 1.2% | Low → hook problem in the first 3 seconds |
| CTR (link) | ≥ 0.9% | Low → creative interests but doesn't persuade a click |
| Hook rate (3s views ÷ impressions) | ≥ 25% | Low → the opening frame/line is the problem, not the offer |
| Hold rate (ThruPlay ÷ 3s views) | ≥ 20% | Low → script loses her in the middle |
| Outbound CTR ÷ LP view rate | ≥ 85% | Low → landing page is slow, or the click is accidental |
| LP conversion rate | ≥ 2.5% (desktop), ≥ 5% (tablet) | Low → ad-to-page message mismatch (see file 09) |
| ATC → Purchase | ≥ 35% | Low → checkout friction, price shock, or trust gap |
| Frequency (7d) | 1.2–2.5 | > 3.0 with rising CPA → genuine fatigue |
| Learning status | "Active" preferred | "Learning limited" → below the learning floor; see §5 |

### Tier 3 — Metrics you deliberately ignore

| Ignore | Why |
|--------|-----|
| **Ad-level ROAS on videos** | Last-click attribution systematically under-credits demand creation. This is the #1 cause of good accounts being destroyed |
| Any metric on a window < 7 days | Weekday variance exceeds creative variance |
| Reach, impressions, engagement, "quality ranking" | Non-actionable at this structure |
| Day-over-day anything | See above |
| Cost per ATC as a kill trigger | Diagnose with it. Never decide with it |

---

## 5. The learning-phase reality check

Meta's model stabilises an ad set after roughly **50 optimization events in 7 days**.

```
50 purchases/week × $25 target CPA = $1,250/week = $179/day
```

**What this means for you, honestly:**

| Your total daily budget | What actually happens |
|-------------------------|-----------------------|
| < $179/day | **No ad set will ever exit learning.** "Learning limited" is permanent. This is not a bug you can fix with structure — it's arithmetic |
| $179–$400/day | CONTROL can exit learning. Test ad sets at $58/day will not, and that's fine — their job is signal, not efficiency |
| $400+/day | CONTROL comfortably out of learning; test sets approach it |

**If you are under $179/day, do this instead of panicking:**

1. Accept "Learning limited" as the normal state. It is not a reason to restructure.
2. Judge on **7-day cost per purchase** and **spend migration**, not on learning status.
3. Consider optimizing CONTROL for **Add to Cart** temporarily if weekly purchases are
   under ~15 — more events means a stabler model, and you convert back to Purchase once
   volume supports it. This is a real trade-off: ATC optimization buys stability at the
   cost of buyer quality, so treat it as a bridge, not a destination.
4. Do **not** compensate by splitting into more ad sets. That makes it strictly worse.

---

## 6. The threshold table — every automatic decision in the account

This is the operational core of the whole SOP. Print it.

### Ad-level decisions (inside CONTROL)

| Condition (7-day window) | Action |
|--------------------------|--------|
| Spend ≥ 3× Target CPA (`$75`) **and** 0 purchases | **Pause the ad.** It has had a fair hearing |
| CPA ≤ Target (`$25`) | Leave alone. Do not "optimize" it |
| CPA between Target and Tolerance (`$25–$31`) | Leave alone. This is normal variance |
| CPA > Tolerance (`$31`) for **2 consecutive weeks** | Kill candidate → build a replacement for that Ring |
| Highest-spending ad, CPA anywhere ≤ Tolerance | **Do not touch, under any circumstance** |
| Frequency > 3.0 **and** CPA rising 2 weeks running | Fatigue. Rotate a new hook onto the same body (file 07 §5) |
| Video ad with poor ad-level ROAS but high Amount Spent | **Leave it.** This is funnel synergy, not failure |

### Ad-set-level decisions

| Condition | Action |
|-----------|--------|
| New test ad set, < 7 days at forced minimum | **No decision permitted.** Not even a look |
| Test ad set: 7 full days at `$58`/day, CPA ≤ Target | **Graduate.** Move winning creative into CONTROL; free the test slot |
| Test ad set: 7 full days at `$58`/day, CPA `$25–$40` | Extend **one** more 7-day cycle. Decide at day 14 |
| Test ad set: 7 full days at `$58`/day, CPA > `$40` or 0 purchases | **Pause.** Slot freed for the next concept |
| Test ad set naturally pulling spend **above** its minimum | Strong signal — Meta is choosing it. Do not cap it |
| CONTROL spend share falling below 50% | Your tests are winning. Graduate them; refresh CONTROL |

### Campaign-level decisions

| Condition | Action |
|-----------|--------|
| 7-day account CPA ≤ Target **and** cash allows | **+10% budget.** Once. Monday only. Then nothing for 7 days |
| 7-day account CPA ≤ Target for 3 consecutive weeks | +20% budget. Consider moving up a tier |
| 7-day account CPA `$25–$31` | Hold budget. Run the Ring diagnostic |
| 7-day account CPA > `$31` | Hold budget. **Do not cut.** Run diagnostics (file 07) before any change |
| CPM up > 30% w/w across the whole account | External. Check competitors/seasonality. **Change nothing** |
| Revenue down but new-customer count flat | Retention problem, not an ads problem. Route to email/SMS (file 07 §3) |

---

## 7. Reporting: the one view you build in Ads Manager

**Path:** Ads Manager → Columns → Customise Columns → save as **"PI Weekly Review"**

Include, in this order:

```
Ad Set Name · Ad Name · Delivery
Amount Spent
Purchases · Cost per Purchase · Purchase ROAS
Impressions · CPM · Frequency
CTR (link) · CPC (link)
3-Second Video Plays · ThruPlays
Adds to Cart · Cost per Add to Cart
Landing Page Views
Attribution setting: 7-day click, 1-day view
```

**Default breakdown for the Monday Review:** none. Look at flat ad-set-level numbers first.
Only add a breakdown when a diagnostic in file 07 tells you to.

**Date preset:** *Last 7 days*, and set the week to Monday–Sunday so every review compares
like with like.

### Also build: the weekly scorecard

Ads Manager alone will mislead you, because it can't see blended performance. Maintain the
sheet specified in [`templates/tracker-spec.md`](templates/tracker-spec.md) with these columns
per week:

```
Week | Ad Spend | Total Revenue | Blended MER | Orders | New Customers |
New Cust % | Blended CAC | High-AOV % | Meta CPA | Meta ROAS | CPM | Notes
```

The gap between **Meta ROAS** and **Blended MER** is your attribution drift. Track the gap,
not just the numbers — a widening gap means your pixel is losing signal, and it will show
up here weeks before it shows up in CPA.

---

## 8. Forecast — what good looks like at each tier

Illustrative, at $25 CPA and $58 AOV. Use it to set expectations, not promises.

| Tier | Daily | Monthly spend | Orders/mo | Revenue/mo | Contribution/mo | Creative quota |
|------|-------|---------------|-----------|------------|-----------------|----------------|
| T1 | $150 | $4,500 | 180 | $10,440 | $3,287 | 5 ads |
| T2 | $300 | $9,000 | 360 | $20,880 | $6,574 | 9 ads |
| T3 | $750 | $22,500 | 900 | $52,200 | $16,434 | 23 ads |
| T4 | $1,500 | $45,000 | 1,800 | $104,400 | $32,868 | 45 ads |

*Contribution = orders × ($43.26 − $25). Excludes fixed opex and repeat revenue.*

**The honest constraint:** notice that the creative quota is what actually gates the tiers.
Moving from T2 to T3 means going from 9 to 23 new assets per month. **You will hit the
creative production ceiling long before you hit the budget ceiling.** Plan production
capacity now — file 08 exists for exactly this reason.

---

**Next:** [`03-creative-system-sop.md`](03-creative-system-sop.md) — the creative engine that feeds the machine.
