# Measurement & Iteration

How a beginner turns "the ad didn't work" into a specific, cheap, correct next action.

---

# 1. The metrics that matter

Most people look at ROAS and stop. ROAS tells you *whether* something is broken. These four
tell you *what* is broken — which is the only thing you can act on.

| Metric | Formula | What it diagnoses |
|---|---|---|
| **Hook rate** | 3-second video plays ÷ impressions | The first 3 seconds |
| **Hold rate** | ThruPlays ÷ 3-second video plays | The body (3s → 15s) |
| **Outbound CTR** | Outbound clicks ÷ impressions | Whether the ad gave a reason to act |
| **Outbound CPC** | Spend ÷ outbound clicks | Efficiency of attention → traffic |
| **LPV rate** | Landing page views ÷ outbound clicks | Page load / link health |
| **Site CVR** | Purchases ÷ landing page views | Ad-to-page message match |
| **CPA** | Spend ÷ purchases | The outcome |
| **ROAS** | Revenue ÷ spend | The outcome |

**Set up a custom column preset in Ads Manager with exactly these, in this order.** Then
every diagnosis is a left-to-right read: find the first column that's bad, and that's your
problem. Everything to the right of the first failure is downstream noise.

---

# 2. Your targets

## Derived from your own data *(not benchmarks — these are arithmetic)*

```
Net AOV                        $56.50
Meta site CVR                  4.38%
Revenue per session            $2.47
────────────────────────────────────
Break-even CPC                 $2.47
Max CPC @ 2.0× ROAS            $1.24    ← the fastest kill signal you have
Target CPA @ 2.0× ROAS         $28.25
Target CPA @ 1.81× (Robert)    $31.22
Kill threshold (3× CPA)        $85 spent with 0 purchases
```

## Category benchmarks *(directional — Meta, US, 50+ audience, supplement)*

| Metric | Kill | Acceptable | Strong |
|---|---|---|---|
| Hook rate | <20% | 25–30% | >35% |
| Hold rate | <10% | 15–20% | >25% |
| Outbound CTR | <0.8% | 1.0–1.4% | >1.6% |
| Outbound CPC | >$1.60 | $1.00–1.24 | <$0.90 |
| LPV rate | <70% | 80–90% | >90% |
| Site CVR | <3% | 4.0–4.5% | >5% |

**Label which is which when you report.** The first block is arithmetic from your account and
is not negotiable. The second block is directional and should be replaced with your own
trailing-90-day medians as soon as you have 30+ ads tagged with the naming convention.

**Your 4.38% site CVR is genuinely strong** for a $56 AOV supplement. That means when an ad
underperforms, the problem is almost always **upstream of the page**. Fix the ad, not the site.

---

# 3. The diagnostic decision tree

**Run this on every ad that misses target. It takes 30 seconds and it is the most valuable
thing in this repo.**

```
CPA above target?
│
├─ HOOK RATE < 20%?
│     → The first 3 seconds failed. Nothing downstream matters.
│     → FIX: shoot 3 new hooks against the same body. Ship as v1.1.
│     → COST: near zero if you kept the raw footage.
│
├─ Hook OK, HOLD RATE < 10%?
│     → You stopped the scroll and then lost her at 3–15s.
│     → CAUSE: slow second beat, no turn, the hook wrote a cheque the body didn't cash.
│     → FIX: re-edit 3–15s only. Cut 2 seconds. Move the turn earlier. Ship as v1.2.
│
├─ Hook + hold OK, OUTBOUND CTR < 0.8%?
│     → She watched and didn't act. You entertained her.
│     → CAUSE: no clear offer, weak CTA, or the ad never said what to do.
│     → FIX: new last 8 seconds + new primary text. Ship as v1.3.
│
├─ CTR OK, LPV RATE < 70%?
│     → Technical. Slow page, broken link, wrong destination.
│     → FIX: check the URL and page speed. Not a creative problem.
│
├─ LPV OK, SITE CVR < 3%?
│     → Message mismatch. The ad promised something the page doesn't deliver.
│     → FIX: match the page to the ad — headline, image, and offer.
│       An ad about the 3pm crash should not land on a generic product page.
│     → This is the most-missed diagnosis by beginners.
│
└─ Everything OK, CPA still high?
      → Check frequency. >2.5 in the same audience = fatigue, retire it.
      → Check audience overlap between ad sets.
      → If all clean: the offer isn't competitive enough for that audience. Strategy problem,
        not creative problem.
```

## Reading it in practice

| Hook | Hold | CTR | Verdict | Action |
|---|---|---|---|---|
| 18% | 22% | 1.4% | Great ad nobody sees | New hooks. **This is the most recoverable ad in the account.** |
| 42% | 8% | 0.5% | Clickbait | Hook overpromised. Rewrite the body to earn the hook. |
| 38% | 24% | 1.8% + bad CPA | Ad is fine | Page, offer, or frequency. Don't touch the creative. |
| 15% | 6% | 0.3% | Dead | Kill. Don't iterate. The concept is wrong, not the execution. |

**The row-1 case is where the money is.** A 22% hold rate with an 18% hook rate means you
have a genuinely persuasive ad that almost nobody is watching. Three new hooks against
existing footage is a few hundred dollars and often doubles the ad's output. Beginners kill
these ads. Don't.

---

# 4. The iteration ladder

When a concept wins, **do not go looking for a new idea.** Strip-mine the winner. A single
winning concept should produce **8–15 assets**.

| Step | Iteration | Cost | Typical lift |
|---|---|---|---|
| 1 | **3 new hooks**, same body | ~$0 (existing footage) | Highest ROI move available |
| 2 | **3 new creators**, same script | 1 booking cycle | Unlocks new delivery pockets |
| 3 | **Length cuts** — 15s / 30s / 45s | Editing only | Different placements reward different lengths |
| 4 | **Format port** — video argument → static + carousel | Half a day | Cheap incremental reach |
| 5 | **Awareness port** — same angle, moved up/down the ladder | New script | Opens a new audience |
| 6 | **Persona port** — same angle rewritten for Robert or Dana | New script + creator | Opens a new demographic |

**Worked example — if C04 ("Is Prime Ingredients a scam?") wins:**

```
C04_v1     original                                    ← winner
C04_v1.1   hook: "Somebody commented that we're a scam" (#33)
C04_v1.2   hook: "I'm going to try to talk you out of this" (#35)
C04_v1.3   hook: "The real scam isn't us" (#36)
C04_v2     same argument, founder on camera instead of creator
C04_v2-15s 15s cut: comment → COA → guarantee
C04_S      static: "Is this a scam?" + COA excerpt + guarantee
C04_R      Robert port: male creator, lab numbers, no emotional register
C04_D      Dana port: faster pace, "I don't have time to be scammed twice"
```

That's **9 assets from one win** — roughly one production cycle's worth of output, at a
fraction of the cost and a far higher hit rate than nine cold concepts.

---

# 5. The weekly scorecard

Same day every week. **Thursday works best for you** — it's your launch day and your
second-highest volume day, so you decide and ship in the same session.

| Min | Step | Output |
|---|---|---|
| 0–10 | Pull ad-level report. Update `templates/weekly-scorecard.md`. | Table |
| 10–25 | Run the decision tree on every ad missing target. Assign a fix code. | v1.1/v1.2/v1.3 list |
| 25–35 | **Kill:** anything at $85 spent with 0 purchases. | Paused |
| 35–45 | **Scale:** +20–30% on anything under $28 CPA for 3 straight days. | Budget changes |
| 45–55 | **Iterate:** brief 3 iterations of the week's best concept. | 3 briefs |
| 55–60 | **Mine:** read this week's ad comments, log 5 new quotes in the VoC Bank. | 5 quotes |

That last ten minutes is the compounding step. Your ad comments are a free, continuously
refreshing source of the exact objections your *current, colder* audience holds. Most teams
never read them.

---

# 6. The monthly review

**Four pivot tables. These four decide next month's eight concepts.**

1. **Spend, CPA, ROAS by PILLAR** → which claim territory to go deeper on
2. **…by AWARENESS LEVEL** → whether the funnel is still top-heavy or has drifted back to offers
3. **…by FORMAT** → where production hours should go
4. **…by CREATOR** → who to rebook, who to retire

All four are one filter away if you followed the naming convention in `04` § 3. None of them
are answerable if you didn't.

Then:
- **Re-run Gap Analysis** (`01` Phase 1.3). Gaps reopen as you scale — an audience you fully
  served last month can be under-served this month at 1.5× the budget.
- **Refresh the Objection Ledger.** Colder audiences hold different objections.
- **Retire** everything above 2.5 frequency in the same audience.
- **Recalculate the offer math.** If AOV or site CVR moved, your target CPA moved with it, and
  every kill threshold in this document changes.

---

# 7. Reporting: what to show, monthly

Keep it to one page. Five things:

1. **Spend, revenue, blended ROAS, MER** vs. last month
2. **New winners found** (count) and **hit rate** (winners ÷ concepts tested) — the health of
   the pipeline, and the leading indicator for next quarter
3. **Awareness distribution of spend** — proof the funnel isn't collapsing back to offer ads
4. **Persona distribution of spend and ROAS** — specifically: is Robert's share rising toward
   his efficiency?
5. **One diagnosis and one decision** — what you learned, and what changes because of it

**Do not report on impressions, reach, CPM, engagement, or video views.** None of them are
decisions.

---

# 8. The four failure modes, and how you'll know

| Failure mode | Symptom | Fix |
|---|---|---|
| **No pipeline** | Same 4 ads carrying 70%+ of spend for 6+ weeks; "creative fatigue" | Testing budget is too low. Get to 20%+ and 8 concepts/month. |
| **Volume without strategy** | 20 new ads/month, hit rate under 1-in-12 | You're skipping Phase 1. Every ad should fill a named grid cell. |
| **Winner abandonment** | Winners found and never iterated | Run the iteration ladder. 8–15 assets per win, not 1. |
| **Funnel collapse** | ROAS looks great, revenue is flat or declining | You've drifted back to harvesting existing demand. Check the awareness distribution — Unaware + Problem-aware should be ~45% of spend. |

The fourth one is the dangerous one, because the dashboard looks *better* while the business
gets *smaller*. Offer ads to a warm audience will always show a good ROAS. They just run out
of people.
