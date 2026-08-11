# 06 — Testing, Media Buying & Measurement

Where creative turns into money. All thresholds below are derived from the live account, not from generic benchmarks.

---

## 1. The reference numbers (from `01-strategy-and-brief.md`)

| | Value |
|---|---|
| Gross margin | 58.4% |
| Gross profit per order | $33.83 |
| **Break-even CPA** | **$33.83** |
| Current blended CPA | $39.68 |
| **Target blended CPA** | **≤ $30.00** |
| Current AOV | $55.78 |
| **Target AOV** | **≥ $62.00** |
| Account outbound CTR | 5.16% |
| Account outbound CPC | $2.35 |
| Account CPM | $121.07 |
| Current daily spend | ~$3,006 |

Recompute gross profit per order monthly from Triple Whale. Every rule below moves with it.

---

## 2. Account structure

Three campaigns. That's all.

```
[TEST]  NMN | Creative Testing | ABO
        └─ Ad set: Broad US, 55–70, All genders
           └─ 6–8 new ads per launch, one per creative
        Budget: $450/day  (15% of total spend)
        Optimisation: Purchase, 7-day click / 1-day view

[SCALE] NMN | Prospecting | CBO or Advantage+
        └─ Winners only, promoted from TEST
        Budget: ~$2,100/day  (70%)
        Optimisation: Purchase

[RETAR] NMN | Retargeting | ABO
        ├─ Ad set: Site visitors 30d + ATC 14d (exclude purchasers 60d)
        └─ Ad set: IG/FB engagers 90d (exclude purchasers 60d)
        Budget: ~$450/day  (15%)
        Formats: 08 Objection Checklist, 12 Bundle Maths, 02 Comment Frame
```

**If your total budget is smaller, keep the ratios:**

| Daily budget | Test | Scale | Retarget | New creatives/week |
|---|---|---|---|---|
| $150 | $50 | $80 | $20 | 4–6 |
| $500 | $100 | $325 | $75 | 8 |
| $1,500 | $250 | $1,025 | $225 | 10–12 |
| **$3,000 (today)** | **$450** | **$2,100** | **$450** | **12–16** |

### Targeting

- **Broad beats interests here.** Age 55–70, US, all genders, no interest stack. Meta's delivery already knows who buys NMN — 110K sessions of pixel data have taught it. Interest targeting narrows the pool and is a contributing cause of the +38% CPM.
- Do **not** exclude men. Robert converts at a 1.81 ROAS — the most efficient segment in the account. Let broad find him.
- Geo: run US-wide, then check the Sunbelt breakdown in reporting. Do not pre-restrict to AZ/FL/TX — you'll strangle delivery and raise CPM further.
- Placements: **Advantage+ placements ON**, but upload the 9:16 asset for Stories/Reels via asset customisation. Never let Meta crop your 4:5 into a story — it will cut your headline in half.

### Scheduling — what actually works in Ads Manager

The data says 11 AM and 7 PM ET, Thursday–Saturday. Here is the honest implementation guidance:

- **Ad scheduling (dayparting) requires a lifetime budget** at the ad set level. On daily budgets you cannot restrict hours.
- **Do not daypart your main scaling campaign.** Restricting hours starves the algorithm, raises CPM and usually costs more than the timing gains.
- **What to do instead:** control the *launch* timing, which is free. Publish new ads Thursday morning so they exit learning by Saturday's peak. Never publish Monday.
- **Where dayparting is worth it:** one dedicated ad set, lifetime budget, running only 2–5 PM ET, carrying nothing but ENG-territory "3 PM crash" creatives. She is living the pain point in real time in that window. Cap it at 10% of budget and judge it on its own CPA.

---

## 3. Testing protocol

### Isolate one variable

Treat each test like a science experiment. Change exactly one thing versus the control:

| Test type | What changes | Everything else |
|---|---|---|
| Headline test | The headline text | Same format, image, colours, offer, primary text |
| Format test | The layout | Same headline, same territory |
| Territory test | The angle | Same format |
| Proof test | Which review is shown | Same Comment Frame template |
| Offer-framing test | "$16.66/bottle" vs "6 bottles $100" vs "Save $80" | Same creative |

**One ad = one variable.** If you change the headline *and* the background, a win teaches you nothing.

### Volume expectation

Roughly **1 in 8 statics becomes a winner.** To hold three winners in rotation you need 12–16 new creatives per week. This is not an aesthetic exercise — it's the mechanism that pulls CPM back down from $121. Test fast, test messy.

### Judging statics

Statics have no hook rate or hold rate. Judge them on **CPA, outbound CTR, and outbound CPC** — in that order.

---

## 4. Kill and scale rules

Check daily at 10 AM ET. Do not touch ads on Friday–Sunday except to raise budget on a proven winner.

### KILL — turn it off, log why

| Trigger | Threshold |
|---|---|
| No add-to-cart | **$60 spent** (≈2× target CPA), 0 ATC |
| No purchase | **$100 spent**, 0 purchases |
| Weak click-through | Outbound CTR **< 2.5%** after 5,000 impressions |
| Expensive clicks | Outbound CPC **> $3.50** after $50 spend |
| Unprofitable | CPA **> $45** after $150 spend and ≥3 purchases |
| Fatigued | Frequency > 2.5 (7-day) **and** CPA rising 3 days running |

### WATCH — leave running, review in 48h

- CPA between **$34 and $45**
- Outbound CTR 2.5–5.0%
- Spend under $100 with 1–2 purchases (not enough data yet — do not kill early)

### WINNER — promote to [SCALE]

All four must be true:
- CPA **≤ $30**
- Spend **≥ $150**
- Purchases **≥ 3**
- Outbound CTR **≥ 5.0%**

**How to promote:** duplicate the ad into the [SCALE] campaign. Do not move the original — leave it running in [TEST] so the comparison stays clean.

### Scaling ladder

| Step | Action | Wait |
|---|---|---|
| 1 | Promote into [SCALE] at $100/day | 3 days |
| 2 | If CPA holds ≤ $30, raise **+20%** | 3 days |
| 3 | Repeat +20% every 3 days while CPA holds | — |
| 4 | If CPA breaks $34 for 2 consecutive days, roll back to the last working budget | 3 days |
| 5 | If frequency > 2.5 and CPA rising, the creative is fatigued. Build 3 variations of it (headline only) and rotate. | — |

**Never raise a budget more than 20% in a day** — it resets learning and you pay for the re-learn.

### The three things you must not do

1. **Don't kill an ad before $60 spend.** At a $30 CPA, one purchase is normal randomness. Killing at $25 spend is superstition.
2. **Don't judge on ROAS at the ad level.** Use CPA. ROAS at ad level is distorted by which bundle happened to sell.
3. **Don't edit a live winning ad.** Any edit resets social proof (likes/comments accumulated on the ad) and re-enters learning. Duplicate instead.

---

## 5. What to report, weekly

Blended, from Triple Whale, every Monday:

| Metric | Where | Target |
|---|---|---|
| Blended CPA | TW Summary → `shopifyCpa` | ≤ $30 |
| Blended ROAS | TW Summary | ≥ 1.86 |
| AOV | TW Summary | ≥ $62 |
| Net profit | TW Summary | > $0 |
| CPM | Ads Manager | ≤ $95 |
| Outbound CTR | Ads Manager | ≥ 5.0% |
| Cost per ATC | TW `pixelCostPerAtc` | ≤ $24 |
| New creatives launched | Tracker | ≥ 12 |
| Winners found | Tracker | ≥ 1 |

**Also report per territory** — sum spend and purchases across all ads whose name contains `_ENG_`, `_FOG_`, etc. After four weeks you'll know which of the six angles deserves 50% of your creative budget. That insight is worth more than any single winning ad.

---

## 6. The scorecard question

Every Monday, answer these five in writing. Two sentences each is enough.

1. Which **territory** produced the lowest CPA last week?
2. Which **format** produced the lowest CPA?
3. Which **framework** produced the highest outbound CTR?
4. What is the one variable I'm testing this week, and against which control?
5. Did AOV move toward $62? If not, how many Timeline (04) and Bundle Maths (12) creatives are actually live right now?

Question 5 is the one people skip, and it is the one attached to $31,583/month.

---

## 7. Attribution note

Triple Whale is configured to **Triple Attribution, lifetime window**. Meta's in-platform numbers will disagree — Meta reported 1,502 purchases at $60.04 CPA last period while Shopify recorded 2,278 orders at $39.68 blended.

**The rule:**
- **Blended CPA from Triple Whale / Shopify is truth** for "are we making money."
- **In-platform CPA is the comparator** for "which ad beat which ad."

Never mix them in the same sentence. Use in-platform to rank creatives against each other; use blended to decide whether to scale the account at all.

---

## 8. Milestones

| Week | Milestone |
|---|---|
| 1 | 12 creatives live, tracker running, 12 Canva templates built |
| 2 | First winner identified and promoted; 24 creatives tested total |
| 4 | Blended CPA ≤ $34 (break-even), AOV ≥ $58, CPM trending down |
| 8 | Blended CPA ≤ $30, AOV ≥ $62, net profit positive |
| 12 | 3+ evergreen winners in rotation, territory-level answer established, creative volume sustainable at 12–16/week |
