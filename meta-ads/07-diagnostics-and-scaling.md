# 07 — Diagnostics & Scaling

The reference you open when something moved and you need to know *what* moved before you
touch anything.

**The universal first step, always:** confirm you are looking at a **7-day window**. Roughly
half of all "problems" brought to this document dissolve the moment the window is corrected.

---

## 1. Master triage tree

```
                   Something changed. Start here.
                              │
              ┌───────────────┴───────────────┐
              │  Is the window ≥ 7 days?      │
              └───────────────┬───────────────┘
                    NO ───────┴────── YES
                     │                 │
              Fix the window.          │
              Re-read. Usually         │
              the problem is gone.     │
                                       ▼
                        ┌──────────────────────────┐
                        │ Did SITE conversion rate │
                        │ change?                  │
                        └──────────┬───────────────┘
                     YES ──────────┴────────── NO
                      │                         │
              ┌───────▼────────┐                │
              │ NOT AN ADS     │                │
              │ PROBLEM.       │                ▼
              │ → §3           │      ┌──────────────────────┐
              └────────────────┘      │ Did CPM move >30%    │
                                      │ across ALL ad sets?  │
                                      └──────────┬───────────┘
                                    YES ─────────┴────── NO
                                     │                    │
                            ┌────────▼──────┐             │
                            │ EXTERNAL.     │             ▼
                            │ Hold budget.  │  ┌─────────────────────┐
                            │ Change        │  │ Is frequency rising │
                            │ NOTHING. §2   │  │ on specific ads?    │
                            └───────────────┘  └──────────┬──────────┘
                                             YES ─────────┴───── NO
                                              │                   │
                                    ┌─────────▼──────┐   ┌────────▼─────────┐
                                    │ FATIGUE. §5    │   │ Check tracking   │
                                    │ Revival ladder │   │ health first. §4 │
                                    └────────────────┘   │ Then Ring        │
                                                         │ diagnostic. §6   │
                                                         └──────────────────┘
```

---

## 2. External variables — recognise and ignore

External factors move your numbers and are **not** a reason to change your account. Pausing
high-spending ads during an external shift is the most expensive mistake available to you,
because you pay twice: once in lost revenue, once in re-acquiring the learning.

| External factor | Signature | Correct response |
|-----------------|-----------|------------------|
| Q4 / Q5 auction pressure | CPM up 40–150% across all ad sets, CTR flat | Hold budget. Expect a worse CPA and plan cash for it |
| Competitor launches a new offer | CPM up, CTR down, no internal change | Check Meta Ad Library. Consider an offer response — **not** an ad pause |
| Platform-wide outage / reporting lag | Reported conversions collapse, Shopify orders normal | Wait 48h. Reporting backfills |
| Seasonal demand trough | All metrics soft, site CVR soft | Hold. Do not restructure into a trough |
| iOS / privacy release | EMQ drops, attribution gap widens | Re-verify CAPI. Structure is fine |
| Election / major news cycle | CPM spike, engagement down | Temporary. Hold |

> **The written rule:** external factors adjust your *expectations*. They never adjust your
> *structure*.

---

## 3. "Revenue dropped" — the diagnostic that saves the most money

Revenue falling is the most common trigger for panic changes, and it is very often **not
caused by the ads at all.** Diagnose in this exact order.

### Step 1 — Split new vs. returning revenue
In Shopify or Triple Whale, split last week's revenue into **new customers** and **returning
customers**.

| New customer revenue | Returning revenue | Diagnosis | Action |
|---------------------|-------------------|-----------|--------|
| **Flat / up** | **Down** | ✅ **Retention problem. Your ads are fine.** | Go to Step 2. Change nothing in Meta |
| **Down** | Flat | Acquisition problem | Go to Step 3 |
| Down | Down | Site, offer, or external | Go to Step 4 |

> This split is why the source document insists on it. Prime Ingredients sells a 3–6 month
> supply — a reorder cohort landing a few weeks late will crater weekly revenue while
> acquisition is perfectly healthy. Restructuring the ad account in response would be
> actively destructive.

### Step 2 — Retention problem (new-customer acquisition is steady)
**Do not alter working paid campaigns.** Fix it in owned channels:

- [ ] Deploy/repair the **reorder flow targeting Day 75–95 post-purchase** — the window when
      a 3-bottle buyer is finishing her supply
- [ ] Check Klaviyo deliverability, especially to **Yahoo/AOL** — Linda's likely providers,
      and the ones with the harshest recent sender requirements
- [ ] Check for a subscription/billing failure spike
- [ ] Verify the reorder cohort size: was the acquisition cohort 90 days ago genuinely
      smaller? Then this drop was *scheduled*, and you saw it coming

### Step 3 — Acquisition problem (new-customer revenue down)
- [ ] Did **new-customer count** fall, or did **AOV** fall? Different problems entirely
- [ ] Is Meta spend flat? A silent delivery drop (billing, rejection, exhausted audience)
- [ ] Is CPM up? → §2, external
- [ ] Is CTR down? → creative fatigue, §5
- [ ] Is the ATC→Purchase rate down? → checkout problem, not an ads problem
- [ ] Are exclusions over-excluding? Check `EXCL_Purchasers_180d` size hasn't ballooned

### Step 4 — Both down
- [ ] Site conversion rate over the last 14 days — any drop points to site/offer/checkout
- [ ] Page speed on **mobile and iPad**
- [ ] Apple Pay / Shop Pay still enabled
- [ ] Any recent theme, app, or price change
- [ ] Stock availability on the B3G3 bundle specifically
- [ ] Review score / social proof changes

---

## 4. Tracking health check

Run whenever numbers look strange, and monthly regardless.

| Check | Where | Healthy | If unhealthy |
|-------|-------|---------|--------------|
| EMQ on Purchase | Events Manager | ≥ 7.0 | Add `external_id`, `fbc`, city/state/zip to CAPI |
| Deduplication | Events Manager → Purchase | "Events are being deduplicated" | Fix `event_id` matching. **You are double-counting revenue** |
| Meta purchases vs. Shopify orders | Both | Within 30% | > 40% gap = signal loss |
| UTMs arriving | GA4 / Triple Whale | All params present | Landing page is stripping the query string |
| CAPI errors | Events Manager → Diagnostics | Zero | Fix immediately |
| Pixel on all key pages | Pixel Helper | Fires everywhere | Reinstall |

> **The double-counting trap.** Broken deduplication is uniquely dangerous because it makes
> the account look *better*, not worse. You scale into a ROAS that doesn't exist and only
> find out at the month-end P&L. Check dedup before you believe a great week.

---

## 5. Fatigue diagnosis and revival

### Is it actually fatigue?

| Frequency | CPM | Spend | Verdict |
|:---:|:---:|:---:|---|
| ↑ | flat | flat | ✅ **Genuine fatigue.** Revival ladder |
| **↓** | flat | **↑** | ✅ **Graduation, not death.** The ad left the warm pool and is prospecting cold. **Do nothing** |
| flat | ↑ | flat | External auction pressure. Do nothing |
| ↑ | ↑ | ↓ | Fatigue + external. Revival ladder, expect slower recovery |
| flat | flat | flat, CPA ↑ | Not the ad. Check site/checkout |

### The revival ladder — in order, never skip

| # | Move | Cost | Why it works |
|---|------|------|--------------|
| 1 | **Hook rotation** — keep the winning body, cut 3 new first-5-seconds | Lowest | The body is proven; only the entry point is exhausted |
| 2 | **Environment re-shoot** — same script, new location/wardrobe/creator | Low | New Entity ID, proven script |
| 3 | **Format translation** — turn the winning VSL script into a long-form static advertorial | Low | Unlocks an entirely different placement/format audience from an asset you already own |
| 4 | **Retire and replace the Ring** from the Concept Matrix | Highest | Only when 1–3 are exhausted |

**Never** fully turn off a fatigued winner before its replacement has proven itself in a
test ad set. You'd absorb the CPA hit twice — once losing the incumbent, once during the
replacement's learning.

---

## 6. Ring-level diagnostic

Which of the five jobs is under-performing? Match the symptom.

| Symptom | Failing Ring | Fix |
|---------|:---:|-----|
| Low impressions, low spend, campaign-wide | None — budget/delivery issue | Check billing, rejections, exclusion size |
| High impressions, hook rate < 25% | **Ring 1–3** (the hellos) | New hooks. §5 move 1 |
| Good hook rate, hold rate < 20% | **Ring 2** (authority) | Script problem mid-video. Delay the product reveal further |
| Good CTR, low landing page views | Not a Ring — page speed | File 09 |
| Good LP views, low ATC | **Ring 4/5 ↔ page mismatch** | Angle-match the page to the ad (file 09) |
| Good ATC, low purchase | Not a Ring — checkout | Apple Pay, shipping cost shock, trust badges |
| Everything fine, CPA high | Warm supply exhausted | Rings 1–3 aren't generating enough new demand. Add a *hello*, not a *close* |
| Statics great, videos "bad" | ✅ Nothing is wrong | Funnel synergy. Do not kill the videos |

> **The most commonly misdiagnosed row is the second-to-last.** When CPA drifts up and
> everything looks individually fine, the instinct is to build a better closing static. It's
> almost always wrong — the closers are starved of warm users because the hellos have run
> out of new people. **Fix the top of the funnel.**

---

## 7. Scaling: the four moves, in order of safety

| # | Move | Risk | When |
|---|------|:---:|------|
| 1 | **Raise the CBO budget 10%** | Lowest | Question 1 = YES. Once per week |
| 2 | **Add a new concept to an empty test slot** | Low | A test slot is free and assets pass Entity-ID QA |
| 3 | **Raise forced minimums to 1.5–2× AOV** | Medium | T3+, when tests are proving out reliably |
| 4 | **Split into Core CBO + Testing CBO** | Highest | T4 only ($1,500+/day) |

### What NOT to do to scale

| ❌ | Why it fails |
|----|--------------|
| Duplicate the winning ad set | Both copies now compete against each other in the same auction, and you've halved each one's conversion density |
| Double the budget overnight | Budget changes > 20% re-enter learning. You bought instability |
| Add lookalike audiences | Andromeda ignores the label. You've narrowed the pool for nothing |
| Broaden the age range to 25–65 | Dilutes the vector signal your creative was built to summon |
| Launch a second identical campaign | Splits conversion density; both learn slower |
| Add more ads to a winning ad set | Disrupts a converged model. **Launch a new ad set instead** |

### The 20% rule
Budget changes above ~20% can push an ad set back into learning. **Step in 10% increments,
once a week.** Three consecutive good weeks earns a single 20% step.

Going from $300/day to $600/day correctly:

```
Week 1  $300 → $330    (Q1 = YES)
Week 2  $330 → $363    (Q1 = YES)
Week 3  $363 → $436    (Q1 = YES ×3 → 20% step earned)
Week 4  $436 → $480
Week 5  $480 → $528
Week 6  $528 → $600    ✅ six weeks, learning intact
```

vs. incorrectly: `$300 → $600` overnight → learning reset → 7–14 days of degraded CPA → a
panic cut back to $300 → learning reset **again**. The fast route is slower.

---

## 8. Symptom → cause quick reference

| Symptom | Most likely cause | First check |
|---------|-------------------|-------------|
| CPM suddenly +50% | External auction pressure | Ad Library, calendar, all-ad-sets scope |
| CPM chronically high | Low EMQ, or audience narrowed | Events Manager EMQ; targeting box empty? |
| CTR falling | Creative fatigue | Frequency trend |
| Hook rate < 25% | First 3 seconds | Broad callout in the opener? |
| Lots of clicks, no purchases | Ad↔page mismatch | Does the page headline echo the ad hook? |
| ATC high, purchase low | Checkout friction | Apple Pay, shipping cost reveal, trust badges |
| Test ad set won't spend past its minimum | Meta has judged it weak | Complete the 7 days, then decide |
| One ad eats all the spend | ✅ Working as designed | Do not "rebalance" |
| "Learning limited" permanently | Below the learning floor | File 02 §5 — arithmetic, not a bug |
| Revenue down, orders flat | AOV fell | Bundle stock? Discount code leak? |
| Great ROAS, bad bank balance | Double-counted conversions | **Deduplication check.** §4 |
| Frequency > 3.0 | Fatigue, or exclusions not applied | Verify exclusions on all 3 ad sets |
| New customer % < 60% | Exclusions failing | Audience size, CRM upload freshness |

---

## 9. The escalation rule

If you cannot map what you're seeing to a row in this file:

1. **Change nothing.**
2. Extend the observation window to 14 days.
3. Write the symptom, the numbers, and the date into the tracker.
4. Wait one more Monday Review.

An unexplained anomaly plus a change equals two unknowns and no way to learn from either.
Waiting a week costs a week. Guessing costs a quarter.

---

**Next:** [`08-creative-briefs.md`](08-creative-briefs.md) — the scripts, ready to shoot.
