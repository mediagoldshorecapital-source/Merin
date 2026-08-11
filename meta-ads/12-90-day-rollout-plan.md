# 12 — The 90-Day Rollout Plan

A week-by-week plan from a standing start to an account that is scaling on evidence. Assumes one person working roughly 15 hours/week, plus production days.

**Budget assumption:** ~$150–200/day in month 1, rising to $400–600/day by month 3 *if and only if* the numbers earn it.

---

## Phase 0 — Week 0: Foundations (before you spend a dollar)

**Nothing launches this week. This week prevents three months of wasted spend.**

| Task | Detail | Owner |
|---|---|---|
| Read the SOP | Files 01, 02, 03, 11 at minimum | You |
| Verify the tracking stack | Pixel firing, **Conversions API live**, Purchase event with value + currency, domain verified, AEM priority set | You / dev |
| Verify the claim set | Every row in the README's "facts to verify" table. **Especially the B3G3 price** — the source docs conflict ($58 vs. ~$100–106) | You |
| Build the substantiation folder | One source per claim, per `11-compliance-guardrails.md` | You |
| Confirm brand assets | Colours, fonts, logo, badge files, COA PDF, press screenshots | You |
| Set the account structure | 3 campaigns, exclusions, naming convention, UTMs | You |
| Set up measurement | Custom columns + custom metrics for hook rate and hold rate; open `templates/creative-tracker.csv` | You |
| Compute your true economics | COGS, shipping, fees → contribution margin → breakeven ROAS → target CPA | You |

**Gate:** do not proceed until the Pixel and CAPI are verified and the B3G3 price is confirmed. Running ads with broken tracking or a wrong price is worse than not running ads.

---

## Month 1 — Learn

### Week 1 — Research + first production

```
MON   Full Phase 1 research sprint (4 hrs). Target: 100 verbatim quotes.
      Build the Voice of Customer sheet.
TUE   Pick 6 concepts: C01, C02, C07, C10, C13, C19.
      (5 for Linda, 1 for Robert. 3 ToF, 2 MoF, 1 BoF.)
      Write scripts using 05-script-library.md.
      Run every one through the compliance pre-flight.
WED   Cast: 1 female creator 58–65, 1 male creator 62–70.
      Book the shoot. Send briefs (templates/creator-brief.md).
THU   Build the 8 statics (06-static-ads-sop.md). One afternoon, 16 assets.
FRI   Set up the campaign structure. Nothing live yet.
```

### Week 2 — Film + launch

```
MON   Research (2 hrs). Finalise shot lists.
TUE   FILM. One creator day, full batching structure (07-production-sop.md).
      Target: 10 hooks, 3 bodies, 3 CTAs, full B-roll block.
WED   Edit. Target 8 finished video assets in 9:16 + 4:5.
      QA gate on every one.
THU   ★ LAUNCH. 6 creatives into TESTING at $60/day min spend.
      Broad prospecting live with the 4 strongest statics.
FRI-SUN   Do not touch anything. Read comments daily; reply to objections.
```

### Week 3 — First read

```
MON   First weekly review. Most creatives will only have 4 days of data —
      look at hook rate and CTR only. Do not kill anything yet.
      Research sprint.
TUE   Write 4 new concepts based on which HOOK ARCHETYPES are leading.
WED   Film day 2 (or edit remaining assets from week 2's batch).
THU   ★ Launch 4 new creatives. Leave week 2's cohort running.
FRI-SUN   Hands off.
```

### Week 4 — First real decisions

```
MON   ★ First full 7-day scorecard on the week-2 cohort.
      Apply the diagnostic ladder. Kill 🔴, plan variants for 🟡,
      begin multiplying 🟢.
      Update the creative learning ledger.
TUE   Build 3 hook variants of the best performer. Build the Robert port.
WED   Produce.
THU   ★ Launch variants + 2 new concepts.
```

**Month 1 targets**
- 10–12 creatives tested at full depth
- 2–3 hitting 🟢 (a ~20–25% win rate is healthy — do not expect more)
- Blended MER ≥ 1.5
- The learning ledger has 12 rows and a first real insight about what wins

---

## Month 2 — Scale what works

### Week 5
- Move month-1 winners into BROAD prospecting. Raise budget 20–30%.
- **Build the Robert ad set properly.** ROAS 1.81, currently under-spent — this is the cheapest available win in the account.
- Launch the retargeting campaign (WARM-30D + ATC-14D).
- **Build the Day-75 reorder flow in Klaviyo.** This changes your allowable CPA and it isn't creative work.

### Week 6
- Multiply winner #1 into 12 variants (`10-iteration-and-scaling.md` Part A).
- Implement **post ID consolidation** on all duplicates so social proof accumulates.
- Launch 4 new concepts, weighted toward the winning archetypes.
- Begin daily comment moderation as a fixed habit.

### Week 7
- Test the **long-form VSSL** (Script 11) now that short hooks are proven.
- Test **Advantage+ Shopping** with proven winners only.
- Build the ASTA cross-sell retargeting ad set.
- Launch 4 new concepts.

### Week 8
- Full month-2 scorecard. Recalibrate benchmarks against your own distribution — replace the starting thresholds in `09` with your account's actual 25th/75th percentiles.
- Test **lifetime-budget dayparting** as a parallel ad set if you're now above ~$300/day.
- Test the Perimenopause Professional avatar properly (Scripts 9 + C18).

**Month 2 targets**
- 20+ creatives tested cumulatively
- 4–6 winners live
- Robert ad set profitable
- Reorder flow live
- Blended MER ≥ 1.8
- Spend up 50–100% from month 1

---

## Month 3 — Systematise

### Week 9
- **Street interview day** — batch 8 interviews with women 55–65 in a Sunbelt city. Expensive but the highest-quality ToF format available. One day yields 8 ToF assets.
- Launch 4 new concepts.

### Week 10
- Build the **Arizona-specific creative set.** Tucson AOV $82 vs. Houston $43 — film in Phoenix/Tucson, name the place, cast locally.
- Build the **tablet-first 4:5 set.** Tablet is your highest-converting device at 5.11% and is almost certainly under-served.

### Week 11
- Test the **bundle-upgrade** retargeting set (single/B1G1 buyers → B3G3 via the 55¢/day math). Pure AOV, no new acquisition cost.
- Launch the win-back creative for 120–180 day lapsed purchasers.
- Test the **sleep angle** (205 orders at midnight is a signal she hasn't told you about directly).

### Week 12
- **Quarterly review.** Not a weekly review — a strategic one:
  - Which hook archetypes win? Which angles? Which avatars? Which formats?
  - Rewrite the creative mix for Q2 based on 30+ ledger rows.
  - Compute true 90-day LTV:CAC now that the reorder cohort has matured. **Raise your target CPA if the LTV supports it.**
  - Refresh every claim: review count, press, COA batch.
  - Audit the top 10 fatiguing creatives and plan their replacements.

**Month 3 targets**
- 30+ creatives tested cumulatively
- 6–10 winners in rotation with variants
- Blended MER ≥ 2.0
- Repeat rate above 10% and climbing
- Spend at 2–3× month 1
- A creative learning ledger that tells you what to make next without guessing

---

## The permanent cadence (from week 13 onward)

```
MON    Research 2 hrs · weekly scorecard 1 hr · decisions
TUE    Concepts + scripts (4 new/week)
WED    Produce (film every other week; edit and build statics on the alternate)
THU    ★ QA + LAUNCH
FRI    Comment moderation only
SAT    Hands off — highest order day
SUN    Hands off
```

**Fixed ratios, permanently:**
- Testing budget: **15–25%** of total spend
- New concepts: **8–12/month**
- Creative mix: **~5 ToF / 4 MoF / 3 BoF** per batch
- Avatar mix: **60% Linda / 25% Professional / 15% Robert**

---

## What "great results" looks like at 90 days

| Metric | Day 0 | Day 90 target |
|---|---|---|
| Creatives tested at depth | 0 | 30+ |
| Winners in rotation | 0 | 6–10 |
| Blended MER | baseline | ≥ 2.0 |
| New-customer CPA | baseline | < $31 |
| AOV | $56 | $60+ (via B3G3 mix) |
| B3G3 share of orders | ~40% | 45%+ |
| Repeat rate | 7.8% | 12–15% |
| Robert share of spend | minimal | 15% at ≥1.8 ROAS |
| Learning ledger rows | 0 | 30+ |

The last row is the one that compounds. Winning ads fatigue in six weeks. Knowing *why* they won doesn't.

---

## The five failure modes to watch for in yourself

1. **Judging too early.** Killing a creative on day 3 because Friday's ROAS looked bad. This is the most common and most expensive error in the file.
2. **Making variations and calling them tests.** Ten ads that are all the same idea in different fonts teach you nothing.
3. **Neglecting the top of funnel** because BoF statics are easy to make and look good on a ROAS report. The account stops scaling within 60 days.
4. **Skipping the research sprint** and writing from imagination. Every hook you invent is a guess; every hook you harvest is evidence.
5. **Scaling before the reorder flow exists.** You're buying customers at first-order breakeven and then letting them forget you. The intelligence report says it plainly: *"If you don't, she'll forget and buy from someone else."*
