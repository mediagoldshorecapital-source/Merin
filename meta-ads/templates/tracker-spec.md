# Tracker Spec

One spreadsheet, five tabs. Build it before launch. This is where "measurable results"
actually lives — Ads Manager alone cannot see blended performance, and blended is what pays
the bills.

---

## Tab 1 — `Weekly Scorecard`

One row per week. **The single most important tab.**

| Col | Header | Source | Formula / note |
|-----|--------|--------|----------------|
| A | Week Start (Mon) | manual | |
| B | Ad Spend | Ads Manager | |
| C | Total Revenue | Shopify | |
| D | **Blended MER** | calc | `=C/B` — target ≥ 2.3 |
| E | Orders | Shopify | |
| F | New Customers | Shopify / Triple Whale | |
| G | **New Customer %** | calc | `=F/E` — target ≥ 70% |
| H | **Blended CAC** | calc | `=B/F` — target ≤ $25 |
| I | AOV | calc | `=C/E` |
| J | High-AOV Orders | `Purchase_HighAOV_Bundle` | |
| K | High-AOV % | calc | `=J/E` — target ≥ 40% |
| L | Meta Purchases | Ads Manager | |
| M | Meta CPA | calc | `=B/L` — target ≤ $25 |
| N | Meta ROAS | Ads Manager | |
| O | **Attribution Gap** | calc | `=N-D` — **track the trend, not the value** |
| P | CPM | Ads Manager | |
| Q | CTR (link) | Ads Manager | |
| R | Frequency | Ads Manager | |
| S | Site CVR | Shopify | |
| T | Q1 Answer | manual | YES / NO |
| U | Change Made | manual | **exactly one per week** |
| V | Reason (cite a number) | manual | |
| W | External Factors | manual | Q4, competitor, outage… |

**Conditional formatting:**
- D < 2.0 → red · D ≥ 2.3 → green
- G < 60% → red *(exclusions may be failing)*
- M > Tolerance CPA → amber · M > 1.5× Target → red
- O growing 3 weeks running → amber *(signal degrading — go check EMQ and dedup)*

> **Column O is the early-warning system.** A widening gap between Meta-reported ROAS and
> real blended MER means your pixel is losing signal. It shows up here weeks before it shows
> up in CPA, and it is the difference between fixing tracking and rebuilding an account.

---

## Tab 2 — `Ring Performance`

One row per Ring per week. Drives Question 3 of the Monday Review.

| Col | Header | Note |
|-----|--------|------|
| A | Week | |
| B | Ring | R1–R5 |
| C | Ad Name | |
| D | Angle | |
| E | Format | |
| F | Spend | **primary metric for R1–R3** |
| G | Spend % of CONTROL | `=F/SUM(CONTROL spend)` |
| H | Impressions | |
| I | Purchases | |
| J | CPA | **primary metric for R4–R5** |
| K | Frequency | |
| L | CTR (link) | |
| M | Hook Rate | `3s plays / impressions` — target ≥ 25% |
| N | Hold Rate | `ThruPlays / 3s plays` — target ≥ 20% |
| O | Days Live | |
| P | Status | active / fatiguing / kill-candidate / graduated |

**Reminder row to keep visible at the top of the tab:**
> R1–R3 are judged on **Spend + Hook/Hold rate**, NEVER on ROAS.
> R4–R5 are judged on **CPA**.

---

## Tab 3 — `Test Log`

One row per test ad set cycle. This is your institutional memory — the thing that stops you
re-testing a losing idea in six months.

| Col | Header |
|-----|--------|
| A | Test ID (`T001`, `T002`…) |
| B | Launch Date |
| C | Slot (TEST-A / TEST-B) |
| D | Ring targeted |
| E | Angle |
| F | Format |
| G | Hypothesis — *"we believe X will beat Y because Z"* |
| H | Which live asset it aims to beat |
| I | Forced min spend |
| J | Day 7 Spend |
| K | Day 7 Purchases |
| L | Day 7 CPA |
| M | Pulled spend from incumbent? Y/N |
| N | Decision: graduate / extend / pause |
| O | **What we learned** |

---

## Tab 4 — `Creative Pipeline`

| Col | Header |
|-----|--------|
| A | Asset Name |
| B | Ring |
| C | Angle |
| D | Format |
| E | Status — briefed / shooting / editing / compliance / ready / live / retired |
| F | Creator |
| G | Brief Date |
| H | Due Date |
| I | Compliance approved (Y/N + reviewer) |
| J | Entity-ID check passed (Y/N) |
| K | Launched Date |
| L | Retired Date |

**Header formula:** `Monthly quota = monthly spend / 1000`. Track produced vs. quota each
month — **falling behind quota is your real growth constraint, not budget.**

---

## Tab 5 — `Economics`

One row per month. Re-run on the first Monday.

| Col | Header |
|-----|--------|
| A | Month |
| B | Blended AOV |
| C | COGS/order |
| D | Shipping/order |
| E | Processing/order |
| F | Refund allowance/order |
| G | Contribution/order `=B-C-D-E-F` |
| H | Gross Margin % `=G/B` |
| I | Break-even CPA `=G` |
| J | Break-even ROAS `=1/H` |
| K | **Target CPA** |
| L | **Tolerance CPA** `=K*1.25` |
| M | **Forced min spend** `=B` |
| N | **Learning floor** `=50*K/7` |
| O | Repeat rate @120d |
| P | 120-day contribution `=G*(1+O)` |
| Q | Creative quota `=monthly spend/1000` |

**When B (AOV) moves > 10%, update the forced minimum spend on every test ad set.**

---

## Build notes

- Google Sheets or Excel. Do not over-engineer it — a tracker nobody fills in is worth zero
- Pull Ads Manager numbers with the saved **"PI Weekly Review"** column set (file 02 §7)
- Set the Ads Manager date preset to **Last 7 days, Monday–Sunday** so every week is
  comparable
- Filling this in is part of the Monday Review, not a separate task
- Keep 12 months of history. Tab 3 in particular compounds in value — most "new ideas" in
  month 9 are ideas you already tested in month 2
