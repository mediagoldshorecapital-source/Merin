# Prime Ingredients — Meta Ads Operating System

A complete, click-by-click Standard Operating Procedure for building, running, and scaling
the Prime Ingredients NMN Complex Meta ads account — written so someone who has **never
opened Ads Manager** can operate it at the level of a senior media buyer, and so every
decision made in the account is **traceable to a number**.

Source material: `Meta_ads_structure_plan.pdf` — a synthesis of four 2026 frameworks
(Ole Strand, Blue Sense Digital, Alex Becker, Professor Charley T) plus the Prime
Ingredients Deep Customer Intelligence brief ("Linda" persona).

---

## Read these in order

| # | File | What it gives you | Read when |
|---|------|-------------------|-----------|
| 00 | [`00-doctrine.md`](00-doctrine.md) | The reconciled strategy. Where the four experts disagree and which one we follow, with reasoning. **The "why" behind every rule.** | Once, before anything |
| 01 | [`01-foundations-sop.md`](01-foundations-sop.md) | Phase 0 plumbing: Business Manager, Pixel + CAPI, Event Match Quality, domain verification, exclusion audiences, naming, UTMs | Week 0 |
| 02 | [`02-economics-and-kpis.md`](02-economics-and-kpis.md) | Unit-economics worksheet, every KPI defined, the exact numeric thresholds that trigger every action | Week 0, then re-run monthly |
| 03 | [`03-creative-system-sop.md`](03-creative-system-sop.md) | Olympic Rings, the Concept Matrix, Entity-ID diversification, the 3:2:2 Flexible Ad | Week 0–1 |
| 04 | [`04-campaign-build-sop.md`](04-campaign-build-sop.md) | The actual build. Every click, every field, every toggle | Week 1 |
| 05 | [`05-launch-sop.md`](05-launch-sop.md) | Launch-day checklist, forced spend limits, the 72-hour freeze | Launch day |
| 06 | [`06-operating-rhythm-sop.md`](06-operating-rhythm-sop.md) | Daily 10-minute check, the Monday Review, the monthly reset | Every day / week / month |
| 07 | [`07-diagnostics-and-scaling.md`](07-diagnostics-and-scaling.md) | Decision trees. "Revenue dropped — what do I do?" answered without guessing | Whenever something moves |
| 08 | [`08-creative-briefs.md`](08-creative-briefs.md) | Ready-to-shoot scripts and static briefs for all 5 Rings × 4 Angles | Every creative cycle |
| 09 | [`09-landing-page-sop.md`](09-landing-page-sop.md) | Angle-matched advertorial pages, the rules that make them convert | Week 1–2 |

Copy-paste templates live in [`templates/`](templates/).

---

## The system in one picture

```
                        ONE CBO CAMPAIGN  ("Andromeda 1")
                        PI | CORE | CBO | Sales
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
   ┌────▼─────┐               ┌─────▼────┐               ┌──────▼───┐
   │ CONTROL  │               │  TEST-A  │               │  TEST-B  │
   │          │               │          │               │          │
   │ Proven   │               │ One      │               │ One      │
   │ winners  │               │ 3:2:2    │               │ 3:2:2    │
   │ Rings1-5 │               │ Flex Ad  │               │ Flex Ad  │
   │          │               │          │               │          │
   │ no min   │               │ MIN $58  │               │ MIN $58  │
   │ limit    │               │ /day     │               │ /day     │
   └──────────┘               └──────────┘               └──────────┘
   Meta decides                Forced learning budget so a new concept
   the split                   cannot be starved before it has data

   Targeting (identical on all three): US · Women 48–65 · broad ·
   Advantage+ audience ON · EXCLUDE 180-day purchasers
```

Everything else in this repo is the discipline that keeps that picture true.

---

## Non-negotiable rules (the 10 that matter most)

1. **Never judge on fewer than 7 days.** 24–48h data is noise. Weekday swings are larger than most creative differences.
2. **Never pause your highest-spending ad during a dip.** Meta routes budget to the asset with the most scale potential. Killing it destroys the campaign's learning.
3. **Diagnose external vs. internal before reacting.** Q4 CPM spikes and competitor offers are not creative failures.
4. **Every new concept gets a forced minimum daily spend of 1× AOV for 7 days.** No exceptions, no early mercy kills.
5. **Never mix angles inside one ad set.** One concept = one ad set. Mixed angles confuse vector retrieval.
6. **Every new creative must change Angle + Persona + Format simultaneously** or Meta's GEM model assigns it the same Entity ID and serves it to the same exhausted pool.
7. **Never judge a top-of-funnel video by its own ROAS.** Statics look better because they're served to warm users the videos created. Judge at ad-set level, not ad level.
8. **Budget changes ≤ 20% at a time**, and only on Mondays after the Review.
9. **If an ad set is hitting KPI, do not add ads to it.** Launch a new ad set instead.
10. **One new ad produced per $1,000 of monthly spend.** Creative supply is the real budget ceiling.

---

## 30-day rollout

| Days | Milestone | Gate to pass before moving on |
|------|-----------|-------------------------------|
| 1–3 | Foundations (file 01) | EMQ ≥ 7.0 on Purchase, domain verified, 180-day exclusion audience live |
| 3–5 | Economics locked (file 02) | Real 30-day AOV + gross margin written into the worksheet; target CPA agreed |
| 4–10 | Creative production (files 03, 08) | 5 Rings shot/designed; ≥ 9 assets ready; 2 landing pages live |
| 10 | **Launch** (files 04, 05) | Launch checklist 100% ticked; launched Thu–Sat, never Monday |
| 11–13 | 72-hour freeze | Zero edits. Only check: is delivery active, is spend pacing, is the pixel firing |
| 14–17 | First read | 7-day window complete. Record baselines. Still no structural changes |
| 18 | First Monday Review (file 06) | Question 1 answered with a number, not a feeling |
| 18–30 | First test cycle | One weak Ring identified, one replacement 3:2:2 built into TEST-A |

**Do not skip the 72-hour freeze.** More beginner accounts are killed in the first three
days than in the following three months.

---

## What "measurable" means here

Every action in this SOP is triggered by a threshold, and every threshold is derived from
your unit economics in file 02 — not from a benchmark blog post. When you finish the
worksheet you will have exactly seven numbers pinned above your desk:

```
Blended AOV            $______      → sets forced ad-set minimum daily spend (1× AOV)
Gross margin %         ______%      → sets break-even ROAS  (1 ÷ GM)
Break-even CPA         $______      → the number above which you are losing money
Target CPA             $______      → the number that triggers scale/kill decisions
Target ROAS            ______x      → AOV ÷ Target CPA
Learning-phase floor   $______/day  → 50 purchases/wk × target CPA ÷ 7
Creative quota         ______/mo    → monthly spend ÷ $1,000
```

Nothing in this account gets turned on, turned off, or scaled without one of those seven
numbers being cited out loud.

---

## Glossary (read once, then refer back)

| Term | What it actually means |
|------|------------------------|
| **CBO / Advantage campaign budget** | You set one budget at the campaign level and Meta divides it between ad sets. The opposite is ABO, where you set a budget per ad set. |
| **Ad set spending limit** | A minimum and/or maximum daily spend you can force onto an individual ad set *inside* a CBO campaign. This is the mechanism that makes forced-learning budgets possible. |
| **Learning phase** | The period where Meta's model is still unstable for an ad set. It ends after roughly **50 optimization events (purchases) in 7 days**. Under that, the ad set shows "Learning limited". |
| **Andromeda** | Meta's 2026 retrieval layer. It scans your creative and matches it to clusters of users in a high-dimensional vector space during a ~200ms retrieval phase. It does not use your interest labels. |
| **GEM / Entity ID** | Meta's multimodal classifier. Visually or textually similar ads get grouped under one Entity ID and treated as duplicates — served to the same narrow pool instead of unlocking new reach. |
| **EMQ (Event Match Quality)** | A 0–10 score in Events Manager for how well your server events match to real Meta users. Higher EMQ → better attribution → higher Estimated Action Rate → lower effective CPM. |
| **CAPI (Conversions API)** | Server-side event sending. Survives iOS tracking prevention and ad blockers, which browser-pixel events do not. |
| **Estimated Action Rate** | Meta's prediction that *this* user takes *your* action. Auction value = Bid × Estimated Action Rate + Ad Quality. |
| **Flexible Ad** | An ad format where you upload multiple creatives, primary texts, and headlines in a single ad, and Meta assembles combinations. Our standard is 3 creatives : 2 texts : 2 headlines. |
| **Ring** | One of five ads with a distinct job (3 cold "hellos", 2 warm "closes"). From Charley T's Olympic Rings. |
| **Concept** | Persona + Angle + Offer. The unit Andromeda actually targets on. |
| **Doom Cycle** | Launching too many new ads at once. Meta tests them on your best bottom-of-funnel audience, which makes your profitable ads look like they're failing, which makes you kill them. |
| **iROAS** | Incremental ROAS — measured at ad-set/account level, not ad level. Ad-level ROAS is corrupted by last-click attribution. |

---

*Maintained on branch `claude/meta-ads-structure-sop-bpbtxk`.*
