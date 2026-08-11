# 06 — Operating Rhythm SOP

Three loops, three different jobs. Do not do a weekly job on a daily loop — that is how
accounts get over-managed to death.

```
DAILY    (10 min)   Is anything broken?              → technical only, never performance
WEEKLY   (45 min)   What does the data say to do?    → the only day you may change things
MONTHLY  (90 min)   Are the numbers still true?      → economics, creative pipeline, tiers
```

---

## 1. The Daily Check — 10 minutes, technical only

**When:** every morning, before 11 AM ET.
**Purpose:** catch breakage. Nothing else.

- [ ] All three ad sets **Active** — nothing paused, rejected, or in review
- [ ] Yesterday's spend within ±20% of the daily budget *(a big shortfall = a delivery
      problem, not a performance problem)*
- [ ] Payment method valid, no billing warnings
- [ ] Events Manager: purchases flowing, no CAPI errors
- [ ] Shopify: yesterday's orders roughly match Meta's reported purchases (±30% is normal
      attribution drift; a sudden divergence is a tracking break)
- [ ] Stock level ≥ 14 days of forecast demand
- [ ] No new ad rejections

**Anything red → fix the technical issue. Anything green → close the tab.**

> ### The daily rule
> **You may not look at CPA during the Daily Check.** Not "just a glance". Daily CPA is the
> most misleading number in the account, and looking at it is how you talk yourself into an
> unscheduled change. Ads Manager's default view will show it to you anyway — this is a
> discipline problem, not a UI problem.

---

## 2. The Monday Review — 45 minutes, the only decision point

**When:** every Monday morning. **Window:** last 7 days, Monday–Sunday.
Template: [`templates/weekly-review.md`](templates/weekly-review.md)

Work the questions strictly in order. Most weeks you stop at Question 1.

---

### Question 1 — *Can I spend more money and stay profitable right now?*

Look at: 7-day account **Cost per Purchase** vs. **Target CPA** ($25), and 7-day **Blended
MER** vs. target (2.3x).

| Answer | Action |
|--------|--------|
| **YES** — CPA ≤ Target and cash flow allows | **Increase the CBO campaign budget by 10%.** Then: **do not launch new ads. Do not touch anything else. Close Ads Manager.** The review is over |
| **YES, and it's been 3 straight weeks** | Increase by 20%. Consider moving up a tier (file 00 §3.2). Still change nothing else |
| **NO** | Go to Question 2 |

> **This is the highest-value paragraph in the SOP.** The instinct, when things are working,
> is to improve them. Resist it. A campaign performing at target is a campaign whose model
> has converged — every edit you make costs you some of that convergence. The correct
> response to success is *more budget and nothing else.*

---

### Question 2 — *Is this internal or external?*

Before you touch creative, establish what actually moved.

| Check | External indicator | Internal indicator |
|-------|-------------------|--------------------|
| CPM week-over-week | ↑ >30% across **all** ad sets → external | Up on one ad set only → internal |
| Frequency | Flat → external | Rising → fatigue (internal) |
| Calendar | Q4/Q5, holiday, major sale events → external | Nothing notable → internal |
| Competitors | New offers in Meta Ad Library → external | — |
| CTR | Flat while CPM rose → external | Falling → creative (internal) |
| Site conversion rate | Flat → it's an ads-side issue | Fell → **not an ads problem at all** |

**If external:** record it in the tracker and **change nothing.** Hold budget. Do not cut.
Cutting budget during a CPM spike hands share to competitors and resets your learning right
when re-acquiring it is most expensive.

**If site conversion rate fell:** stop. This is not a Meta problem. Go to file 07 §3.

**If internal:** go to Question 3.

---

### Question 3 — *Which Ring is failing?*

Open CONTROL. Sort ads by **Amount Spent**, descending.

Find the ad consuming the most spend while delivering the worst result **relative to its
Ring's own success metric** — remembering:

- **Rings 1–3** (cold) are judged on Amount Spent, hook rate, hold rate. **Not on ROAS.**
- **Rings 4–5** (warm) are judged on Cost per Purchase against the $25 target.

| Finding | Action |
|---------|--------|
| Ring 4 or 5: high spend, high clicks, CPA > $31 for 2 weeks | This Ring is the failure point. → Question 4 |
| Ring 1, 2 or 3: low ad-level ROAS but high spend | ✅ **Not a failure.** This is funnel synergy. Leave it |
| Ring 1, 2 or 3: hook rate < 25% **and** near-zero spend | Weak hello. → Question 4 |
| A Ring is missing entirely (no live asset) | That's the gap. → Question 4 |
| Nothing clearly failing, CPA just soft | Hold. Do nothing. Re-review next Monday |

---

### Question 4 — *Build the replacement*

**You do not tear down the account. You build one better asset for one failing Ring.**

1. Identify the failing Ring and its Angle
2. Pick the replacement cell from the Concept Matrix (file 03 §3)
3. Build **one 3:2:2 Flexible Ad** designed to beat that specific Ring
4. Load it into an **empty test slot** (TEST-A or TEST-B)
5. Set the `$58` daily minimum
6. Launch **Thursday–Saturday**
7. **Leave the incumbent running in CONTROL.** Do not pre-emptively pause it

**How you'll know it won:** the new test ad set pulls spend *away* from the incumbent inside
CONTROL. That's Meta voting with your budget. Once it does, graduate the winning creative
into CONTROL and retire the loser.

**If both test slots are full:** you don't launch. Wait for a slot to complete its 7-day
cycle. Cramming a third test in is the first step of the Doom Cycle.

---

### Question 5 — *Housekeeping* (5 minutes)

- [ ] Any test ad set that has completed **7 full days at its minimum** → apply the
      graduate / extend / pause rule from file 02 §6
- [ ] Any ad with **≥ $75 spend and 0 purchases** → pause
- [ ] Any ad set showing frequency > 3.0 with a rising CPA → flag for creative rotation
- [ ] Update the tracker: all scorecard columns for the completed week
- [ ] Confirm next Thursday's launch slot has assets in production
- [ ] Log this week's decision and its stated reason in the tracker

---

### The Monday rule

> **All changes happen on Monday.** Not Tuesday because you thought of something. Not Friday
> because it looked bad. One change window per week means every week's data is a clean read
> of exactly one decision.
>
> **The single exception:** launching a new test ad set, which happens Thursday–Saturday and
> was *decided* on Monday.

---

## 3. The Monthly Reset — 90 minutes, first Monday of the month

Runs *in addition to* that day's Monday Review.

### 3.1 Re-run the economics (30 min)
- [ ] Pull trailing-30-day AOV, COGS, shipping, processing, refund rate from Shopify
- [ ] Recalculate the worksheet in file 02 §1
- [ ] Update the seven numbers. **If AOV moved > 10%, update the forced minimum spend
      ($1× AOV) on every test ad set**
- [ ] Recalculate Target CPA and Tolerance CPA
- [ ] Recalculate the learning-phase floor — it moves with Target CPA

### 3.2 Reconcile attribution (15 min)
- [ ] Meta-reported purchases vs. Shopify orders vs. Triple Whale
- [ ] Record the **gap** between Meta ROAS and Blended MER
- [ ] Gap widening month over month → your signal is degrading. Re-check EMQ, CAPI dedup,
      and whether the landing page is still preserving UTMs

### 3.3 Creative pipeline audit (20 min)
- [ ] Did you hit the quota (spend ÷ $1,000)? If not, that's your growth constraint, not
      the budget
- [ ] Which Rings have had no new candidate in 60+ days?
- [ ] Which Angles from the Concept Matrix are still unexplored?
- [ ] Book next month's creator days **now**

### 3.4 Account health (15 min)
- [ ] EMQ still ≥ 7.0 on Purchase
- [ ] Exclusion audiences still populating and still attached to all ad sets
- [ ] Any accumulated ad rejections or policy warnings
- [ ] Frequency trend across the month
- [ ] New-customer % ≥ 70%

### 3.5 Tier review (10 min)
- [ ] Are you above the learning-phase floor?
- [ ] Should you move up a tier? (file 00 §3.2)
- [ ] If moving to T3: add a third test slot, raise minimums to 1.5× AOV
- [ ] If moving to T4: split into Core CBO + Testing CBO at 15–20% of total

---

## 4. Quarterly — the Harvest Protocol

Once a quarter, look for organic breakouts inside your Flexible Ads.

If one specific combination has gone unusually viral — heavy comments, shares, saves:

1. Find that specific **Post ID** (Ads Manager → the ad → *View post*, or Page → Ad Posts)
2. Create a **new standalone ad in CONTROL** using **Use Existing Post** and that Post ID
3. **Do not turn off the original 3:2:2.** Both run

You've just promoted a proven performer into your core team while keeping its social proof
— all the accumulated likes, comments, and shares travel with the Post ID and compound.

---

## 5. The anti-pattern list

Every one of these has killed a working account.

| ❌ Don't | ✅ Instead |
|---------|-----------|
| Check CPA daily | Check delivery daily, CPA weekly |
| Pause a high-spending ad in a dip | Diagnose external vs. internal first |
| Launch 10 new ads at once | Two test slots, one 3:2:2 each |
| Cut budget when CPA rises | Hold. Diagnose. Cutting compounds the problem |
| Add ads to an ad set that's hitting KPI | Launch a new ad set |
| Duplicate a winning ad set to "scale" | Raise the campaign budget 10% |
| Judge a ToF video on its own ROAS | Judge Amount Spent + ad-set-level iROAS |
| Change budget and creative in the same week | One variable per week |
| Add interest targeting when performance dips | Never. Andromeda ignores it |
| Turn off a fatigued winner before its replacement is proven | Run both until the new one pulls spend |
| Make a change on a Wednesday | Wait for Monday |
| "Just refresh" copy on a live winner | Any edit risks resetting learning |

---

**Next:** [`07-diagnostics-and-scaling.md`](07-diagnostics-and-scaling.md) — when something moves, this tells you what it was.
