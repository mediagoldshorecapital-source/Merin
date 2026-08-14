# Master Synthesis Prompt — Prime Ingredients NMN

**What this is.** A paste-ready prompt for Claude that takes all fourteen research artefacts you
have built — ten documents and four tagged quote banks — and turns them into one document: the
**Creative Intelligence Master**. That document is the input to every ad you make for the next 90
days.

**Why it is not just "summarise these."** Your sources contradict each other on four load-bearing
points, and one of those contradictions will systematically promote your losing ads if it goes
unresolved. The prompt's real job is to arbitrate, not to compile. See `02-SOURCE-INDEX.md` for the
precedence rule and the four conflicts — read that first; the prompt below assumes it.

---

## How to use it

1. Start a **new** Claude conversation. Opus, extended thinking on.
2. **Attach all fourteen sources.** The four `.xlsx` banks attach as files; the ten documents can
   be attached or pasted.
3. Paste `02-SOURCE-INDEX.md` first, as its own message. It is the ruleset.
4. Then paste everything between `PROMPT STARTS` and `PROMPT ENDS` below, with the `<<< >>>` slots
   filled.
5. Any slot you have no data for: write `NO DATA`. Never delete a slot, never invent a value.
6. Expect a long output. If it stops, reply `continue from section N` — never `regenerate`, or the
   evidence tagging drifts.

---

## Your inventory

**~551 tagged quotes across four banks.** Every one is verbatim, tagged on the same four axes, and
scored against the same six specificity markers. This is an unusually good position to be writing
from — the constraint is no longer language, it is arbitration.

| Bank | Rows | Corpus | Key columns |
|------|------|--------|-------------|
| `icpquotebank.xlsx` → *Quote bank* | 83 | **Your own Meta ad comments**, Feb–Aug 2026 | Quote · Emotion · JTBD · Objection/Benefit · Trigger · ICP · Copy-ready · Flags · 6 markers · Date · **comment_id** · Source |
| `primecustomerlanguagebank.xlsx` → *Quote Bank* | 169 | Reddit (r/Biohackers, r/NMN, r/longevity…) | ID · Quote · Speaker · Source · Emotion · JTBD · Type · Objection/Benefit · Trigger · Segment · **Claim risk** · Creative use · 6 markers · Score/6 · Creative-ready |
| `voiceofcustomerbank.xlsx` → *Quote Bank* | 189 | **Competitor** reviews, 8 brands, 2021–2026 | ID · Words · Brand/SKU · Source · **Provenance** · Emotion · JTBD · Objection/Benefit · Trigger · 6 markers · Marker score · **Verdict (USE/CONTEXT)** · Angle |
| `nmnquotebankyoutube.xlsx` → *Quote Bank* | 110 | YouTube comments | ID · Quote · Words · Emotion · JTBD · Type · Objection/benefit · Trigger · Criteria met · Score · **Segment** · Use it for |

Also inside those workbooks: `icpquotebank` carries the **ICP dossier**, **Findings** (the seven
operational findings, three critical) and the **Harvest plan**; `voiceofcustomerbank` carries
**Rollups**; `primecustomerlanguagebank` carries a **Tag Index** and **Tag Counts**;
`nmnquotebankyoutube` carries **Below bar** (rejected quotes, kept deliberately) and **Method**.

**The one rule about the banks:** only `icpquotebank` contains *your* customers. The other three are
category and competitor language. Mine all four for phrasing; attribute nothing from the other three
as your own social proof.

---

## What it will hand you back

| # | Section | What it is |
|---|---------|-----------|
| 0 | Operational Gate | The P0 blockers no creative can fix, and what they block |
| 1 | Evidence Ledger & Conflict Resolution | Every source, its authority, and the four conflicts settled |
| 2 | Objection Ledger | Every objection ranked by frequency × revenue damage, with its counter |
| 3 | Unified Quote Bank | ~551 quotes deduped, clustered by emotion, copy-ready flagged |
| 4 | Persona Set | Four ICPs confirmed / revised / retired against measured data |
| 5 | Awareness Ladder | Five levels × persona, written as arguments |
| 6 | Content Pillars | Durable claim territories, each with ≥4 angles |
| 7 | Gap Scorecard | Persona / awareness / diversity gaps, ranked P0–P2 |
| 8 | Concept Grid | 24–40 named concepts, each with a Concept ID and evidence tier |
| 9 | Hook Bank | 15 hooks per P0 concept, in the winning architecture |
| 10 | Scripts | Full timecoded shooting scripts for the P0 concepts |
| 11 | Claims & Compliance | Every claim triaged, plus the stated risk position |
| 12 | Offer Math | Recalculated from real numbers, against a 1.70 breakeven |
| 13 | 90-Day Plan | Budget, naming, test design, launch calendar |
| 14 | Measurement | Conversions-per-click framework and the corrected decision tree |
| 15 | Open Questions | What the data cannot answer, and the exact check that would |

---

<!-- ------------------------------------------------------------------ -->
<!--  ---8<---  PROMPT STARTS — copy from here  ---8<---                 -->
<!-- ------------------------------------------------------------------ -->

# ROLE

You are a senior direct-response creative strategist who has bought Meta media for supplement brands
in restricted health categories for a decade. You are unusually good at one specific thing:
**reading what the account actually measured and refusing to prefer the theory over it.**

You are not a copywriter being asked to be creative. You are an analyst being asked to be accurate,
then a strategist being asked to be decisive. Where the data is thin you say so in the document
rather than writing around it.

# THE BRAND

Prime Ingredients / Prime Elements, St. Petersburg FL. Flagship: **NMN Complex 1000mg**, $29.98
anchor, morning oral dose. ~100% of paid traffic from Meta. Sold predominantly in multi-bottle
bundles to US buyers, roughly 55–70. Also in range: Astaxanthin, Multi Collagen Peptides, Calcium
Wrinkle Balm. Brand pillars: targeted formulations, simple daily rituals without complex stacks,
straightforward honest messaging.

**Revenue mix:** NMN 94% ($292,955 Jun–7 Aug) · ASTA 4% · the other two negligible and
margin-unknown.

# YOUR TASK

Synthesise every attached source into **one complete document**: the Creative Intelligence Master.
It must be complete enough that someone who has never seen the research can produce a month of ad
creative from it without asking a single question.

Follow the sixteen-section structure in `OUTPUT SPECIFICATION` exactly, in order, with those exact
headings.

# THE ECONOMICS EVERYTHING SITS INSIDE

State these at the top and let them constrain every recommendation.

- Blended ROAS **1.29** against breakeven **~1.70**. You lose money on first order and recover it on
  re-bills.
- Acquisition **−$21.95** per subscriber. Re-bill **+$37.34**. Breakeven **0.59 re-bills per
  subscriber**. That number is what the entire retention system exists to protect.
- Winners: CPA **$31.90**. Losers: CPA **$58.09**. That spread is the prize.
- Run rate ~**$118K/month**. Refund rate **2.85%**.
- Robert at **1.81 ROAS** is per the research the only segment above breakeven on first order —
  **unverified in the warehouse**, confirm in Ads Manager before moving budget against it.

# THE PRECEDENCE RULE

Your sources disagree. When they do, this order decides:

1. **Meta Creative Teardown + The Linda System** — your own ads, 1,220 of them, $381K, 8 Feb–7 Aug
   2026. Nothing outranks these on "will this work here."
2. **Four-ICP Dossier + warehouse + your own ad-comment corpus** — who buys, what they pay, what
   they are saying in public now.
3. **Category corpora** (Reddit 161K words, competitor reviews 8 brands, YouTube) — authoritative
   for *language, objections and mental models*. Not evidence about your account's performance.
4. **The May 20 ICP report**, where 1–3 have not already corrected it.
5. **The Creative Strategy Operating Manual's numeric benchmarks** — generic category defaults,
   superseded by 1–2 wherever they conflict. Its *process* (phases, Concept IDs, gap analysis,
   iteration ladder, rituals) stands.

# THE FOUR CONFLICTS — RESOLVE THESE EXPLICITLY IN SECTION 1

Do not smooth these over. Name each, state which side wins, show the numbers.

**C1 — How to judge an ad.** The Operating Manual says judge on hook rate, hold rate, CTR. The
account measured hook rate correlating **negatively** with ROAS in **all seven months**, never once
positive. Winners: CTR 5.29%, conv/click 4.26%, CPA $31.90. Losers: CTR 7.18%, conv/click 2.61%,
CPA $58.09 — 36% more clicks, converted 39% worse.
→ **The account data wins outright.** Judging on engagement here systematically promotes losers,
because losers are exactly what looks best on engagement. Keep the Manual's diagnostic *logic*,
rebuild the columns around **conversions per click**. Read from **Meta** — the Triple Whale checkout
event fires on only ~63% of purchases.

**C2 — Second person vs first person.** The Manual says Meta prohibits copy implying knowledge of
the viewer's health, so rewrite to first person. The account measured second-person committed copy
as the **winning** structure (1.41 ROAS, 4 of 12 all-time winners) and first-person story as the
**worst angle in the account** (0.83 ROAS, $69.54 CPA).
→ **Escalate this as a stated risk decision. Do not silently pick a side.** One document describes
rejection *risk*, the other describes *return*; both are true, and the account is currently running
the risky construction and winning. Produce an explicit risk position.
Note the two halves separate cleanly: *"Tired of feeling tired as you age?"* is a second-person
question about a symptom the reader **self-identifies** — low exposure. *"Your NAD+ levels are
plummeting"* is a second-person **assertion about the reader's physiology** — materially higher
exposure. You can keep the winning architecture and move only the assertion into a safer register.
Show both versions of every affected line.

**C3 — Hedged vs committed.** The hedged phrasing of the identical insight (*"naturally drop…
helps support"*) returned **0.92 ROAS across 436 ads with zero winners and nine losers**. The
committed phrasing (*"are plummeting… boost them"*) returned **1.41** across $146K. Same insight,
same mechanism, same audience, **53% apart**. Meanwhile the Reddit corpus says this category has a
hype allergy and that restraint buys credibility.
→ **Both, in different places.** Commit in the ad — hedging is what stops it qualifying. Hedge in
the proof: landing page, PDP, post-purchase. Do not import Reddit's register into the hook.

**C4 — Timing.** The old ranking (Saturday best, never Monday, 11am peak) used raw order counts,
which track the budget schedule rather than her behaviour. Spend-controlled, 1 May–7 Aug: **Friday
best** (1.25 ROAS, $48.47 CPA), **Tuesday worst** (0.99, $61.26), Saturday mid-pack, **Monday fine**
(1.06), Sunday overspent at sixth-best return. Hour curve is flat 8 AM–midnight; only 2–7 AM is
dead.
→ **Measured data wins.** Launch **Wednesday or Thursday** so creative exits learning by Friday.

# NON-NEGOTIABLE RULES

**R1 — Verbatim means verbatim.** Reproduce the customer's own spelling, punctuation, capitalisation
and typos, with source ID and date. Never clean up, never merge two quotes, never write one nobody
said. If you need a point you have no quote for, write the point and mark it `[I]`.

**R2 — Tag every claim.** `[M]` measured (warehouse, ads export, comment corpus) · `[R]` research
(prior reports, may be stale) · `[I]` inferred (hypothesis wearing a fact's clothing) · `[—]` not
available (name the absence).

**R3 — An empty cell stays empty.** The ad-comment corpus returns **zero hope and zero shame** rows.
Those cells read `NO DATA — harvest required`. Do not fill them with something plausible. The value
of this document is that its gaps are visible.

**R4 — Only one bank is your own customers.** `icpquotebank` is Prime Ingredients' Meta ad comments.
Reddit, YouTube and the competitor-review bank are category language — mine them for phrasing, never
attribute them as your social proof, and never publish a competitor's customer as a testimonial.

**R5 — Every concept gets a Concept ID and an evidence tier.**
ID = `C##_Persona_Awareness_Pillar_Angle_Format`. Tier = **Proven** (a winning ad behind it) /
**Adjacent** (variant of a winner) / **Untested** (new). Do not launch twelve untested concepts at
once.

**R6 — Mine before you write.** For every hook, search all four banks first. If a customer already
said it, use it and cite the ID. Mark invented hooks `[I]`.

**R7 — Contradictions get reported, not averaged.** Print both sides, say which you would act on and
why.

**R8 — Rank everything** by expected revenue impact, and state the ordering logic.

# SECTION 0 IS A GATE, NOT AN INTRODUCTION

Before any creative work, open with what no creative can fix. The dossier raises seven findings;
three are critical:

1. **Customers say orders never arrive**, and are publicly organising to report the page to Meta,
   TikTok, Instagram, the BBB and their banks. For a business taking ~100% of paid traffic from
   Meta, a coordinated report campaign is existential.
2. **Ads appear to show a competitor's bottle** (Micro Ingredients) while the shop sells Prime
   Ingredients. ~22 comments, some posting competitor links. Legal exposure as well as trust.
3. **The subscription appears forced at checkout** — 97% of orders carry the subscription flag while
   Subscribe & Save SKUs have sold **nine units total**, meaning enrolment happens at checkout, not
   by product choice. At least eight commenters say plainly they wanted to buy and did not.

Plus: the **capsule-count gap** (120 advertised vs 30 received), the **celebrity association**
repelling the target demographic, **unanswered medical eligibility questions**, and **contradictory
dosing guidance**.

For each: the allegation, the evidence with comment IDs, the verification step, the owner, the
deadline, and **which concepts are blocked until it resolves**. Then state the spend position
plainly. These are customer allegations, not verified facts — say so — but they are being made
publicly under live ads where the next buyer reads them, so they are revenue-affecting either way.

# OUTPUT SPECIFICATION

## 0. Operational Gate
Table: Finding · Severity · Evidence (comment IDs) · Verify how · Owner · Due · Concepts blocked.
Close with the spend recommendation.

## 1. Evidence Ledger & Conflict Resolution
Every source: what it is, date range, volume, what it can support, what it cannot. Then the honest
ranking — which personas and claims are well-evidenced and which are hypotheses. Then **all four
conflicts above, resolved, with the numbers shown**. A persona built mostly of `[I]` is a hypothesis
wearing a name; say which ones are.

## 2. Objection Ledger
Every distinct objection across all sources. Columns: Objection · Verbatim example (ID) · Frequency ·
Where it appears (own comments / Reddit / YouTube / competitor reviews) · Revenue damage `[M/R/I]` ·
Counter-message · Pillar that owns it · Concept that answers it. Ranked by frequency × damage.
Minimum 25 rows. Mark which are **your** customers versus category.

## 3. Unified Quote Bank
Merge all four banks. Dedupe. Normalise the tagging onto the shared axes: **emotion** (fear / shame /
hope / relief / pride / anger / grief), **job-to-be-done**, **objection or benefit**, **trigger
moment**, plus the six markers (specific time or place · physical sensation · comparison to a former
self · embarrassing admission · plain unbranded language · under twelve words). Three or more =
copy-ready.

Sort by emotion and present each cluster together — fifteen quotes about one fear is not one ad, it
is a pillar that will support six. Carry through each bank's own extra columns where they add
signal: **claim risk**, **provenance**, **segment**, **verdict**.

End with the emotion coverage table across the merged bank, split by corpus, and for every emotion
that is empty or thin in **your own** comments, the specific harvest action that fills it.

## 4. Persona Set
Confirm, revise or retire each of the four ICPs — Linda–Energy, Linda–Clarity, Margaret–Mirror,
Robert — against measured data. Per surviving persona: share, AOV, LTV, repeat rate, units/order,
all `[M/R/I]` tagged. Then the twelve parts: who they are · day hour by hour · how they find you and
what they buy · geography · deep insecurities ranked · a day in their life · what they want next ·
repeat behaviour · counterpart · discount and trust mechanics · best-friend card ·
emotion/JTBD/objection/trigger.

Flag explicitly any persona the data **contradicts**, and any the data reveals that the dossier does
not name. Note that Linda–Clarity cannot be sized in the warehouse — it is a creative hypothesis,
and must stay labelled as one.

## 5. Awareness Ladder
Five levels — Unaware, Problem-aware, Solution-aware, Product-aware, Most-aware — written as
**arguments, not headlines**, one column per persona. Then current spend distribution from the ads
export, target distribution, and the delta in dollars per day.

## 6. Content Pillars
A pillar supports 5+ ads for 6+ months. Orthogonal — if two produce the same ad, merge them. Per
pillar: territory · why it exists here · 4–6 angles · supporting quote clusters with IDs · objections
neutralised · personas served · **measured performance if any ad has run in it** · claim risk.

Start from the Manual's six (Energy Reclaim · The Mind · Trust & Purity · The Bundle Math · Identity
& Presence · The Mirror), then revise against the seven measured angles from the teardown. Retire
anything unsupported and say why.

## 7. Gap Scorecard
- **Gap A — Persona.** Creative volume vs ROAS by persona. Flag any persona over 70% of creative,
  any high-ROAS segment under 10% of spend, any segment in orders but absent from the creative log.
- **Gap B — Awareness.** Spend by level vs target.
- **Gap C — Diversity.** Score each persona /5: ≥3 pillars · ≥2 angles per pillar · ≥3 formats ·
  ≥3 creator demographics · ≥3 awareness levels.

Rank P0/P1/P2 by expected incremental revenue. You cannot cannibalise an audience you were never
talking to.

## 8. Concept Grid
24–40 concepts: Concept ID · Persona · Awareness · Pillar · Angle · Format · **Evidence tier** ·
Gap filled · Wave · Source quote ID · Priority. Three monthly waves, Wave 1 pure P0 gap-fill. Mark
the three that survive if capacity is cut to a quarter. Keep the tier mix sane — do not stack a wave
with untested concepts.

## 9. Hook Bank
Fifteen hooks per P0 concept minimum. Two lines that are **never identical** — on-screen text (bold)
and spoken line (italic) — because identical wastes a channel. Cite source quote IDs. Mark invented
hooks `[I]`.

**Write in the architecture that won**, and show it explicitly:

```
[Symptom question, second person]?
"It's not just [the dismissal she's been given]…"
"Your [named mechanism] is [committed verb: plummeting / collapsing]!"
"[Strong verb] it with [product] and get back [b1], [b2] & [b3]."
"[Explicit CTA] →"
```

Rotate four variables — symptom · dismissal · benefit-triad order · CTA verb — to generate testable
variants from one proven skeleton. Also use the second proven template, **category-quality
contrast** (*"Not all X is created equal"*): best CPM in the account at $57.47 vs $98.37, three of
twelve winners, and **never once tested on NMN**, which is 94% of revenue.

**Hooks qualify, they do not attract.** If a line would appeal to someone who has never felt this
pain, rewrite it. That is the whole $31.90-vs-$58.09 difference.

## 10. Scripts
Full shooting scripts for every P0 concept. Timecoded beats (0–3, 3–9, 9–15…), each giving visual,
on-screen text and spoken line. Header: Concept ID · creator brief (age, gender, setting, delivery
register) · length · format · coverage to shoot.

Production constraints, measured: **20 seconds**, hook inside 3, **captions burned in** (she watches
Reels in a recliner with the TV on and the sound off). Talent must read **58–68** — she compares
herself to her peer group and a 45-year-old breaks the mirror. **Plain beats polished** — in this
account the winners look homemade and the losers look like adverts. Never put **"75% OFF"** in a
headline; it lost on conversions-per-click five months out of five. Lead with the per-bottle anchor,
$29.98 → $16.66.

## 11. Claims & Compliance
Triage every ad-facing claim: **Claimable** (structure/function safe) · **Testimonial only**
(attributed customer quote, never brand voice) · **Do not use** (disease or drug claim).

Then the **stated risk position** from C2 — second-person symptom questions versus second-person
physiological assertions — with both versions of every affected line, so the business can choose.

Then the claims already flagged as failing review as written: *"Slows biological cellular aging"*,
*"Enhances cellular insulin sensitivity"*, and the *"NAD+ drops up to 50% by middle age"* stat
(contested in the corpus itself). Soften the first two to "supports"; use the third only with a
citation you can defend.

Then the 60-second pre-shoot check: any disease name → delete · cure/treat/prevent/reverse/clinically
proven/doctor recommended → delete or substantiate · every number real and current · every document
shown on camera genuine (a fabricated COA is a legal problem, not a compliance one) · FDA disclaimer
present.

**The dementia line specifically.** The most loaded finding in the research is *"I'm terrified I'm
losing my mind like my mother did."* It is true, it is powerful, and it must never run — naming a
relative's diagnosis beside a supplement is a disease claim and an implied treatment claim in one
sentence. Use the observable moment: *"The word just wouldn't come. Mid-sentence. In front of my
daughter."* The fear is fully present; nothing actionable was claimed.

## 12. Offer Math
Recalculate against a **1.70 breakeven, not a 2.0× target**. Revenue per session · max CPC · target
CPA · kill threshold. Show the arithmetic. Then the bundle distribution and what it means: if most
orders are multi-bottle, creative selling "try a bottle" sells the wrong thing to the wrong person
and lowers belief as well as AOV.

Flag the still-missing inputs: **COGS is null on Multi Collagen and Calcium Balm**, so their margin
is unknown and neither should be promoted until it is loaded.

## 13. 90-Day Plan
Budget split as percentages so it scales. Naming convention —
`[Product]_[Angle#]_[Format]_[Variant]_[Date]` — and note that ad naming is **currently broken**
(`- Video - Ad -2`, `- Video - Ad - 2` and `Video - Ad - 2` are three separate rows), so angle-level
reporting is impossible until it is fixed. Test design rules. Launch calendar by wave, **Wednesday
or Thursday**. Day weighting: index up Friday, hold Wed/Sat, reduce Sunday, cut Tuesday hardest.
Dayparting: run 8 AM–midnight ET, suppress 2–7 AM, do not over-engineer the rest.

Production capacity required, and what to cut first if capacity is short.

## 14. Measurement
**Conversions per click is the primary metric.** ≥4.0% scale · 3.0–4.0% hold and iterate · <2.8%
kill. Decide after ~40 clicks (≈$60 at a $1.50 CPC). Read from **Meta**, not Triple Whale.

Then the corrected decision tree. Engagement metrics are still **diagnostic** — they tell you which
stage of the ad failed — but they are **not** the promotion criterion, and a high hook rate beside a
low conversion rate is a warning, not a win. Make that inversion explicit, because it is the single
most counter-intuitive thing in the document and the easiest to get wrong.

Then the iteration ladder: a single win should produce 8–15 assets.

## 15. Open Questions
Everything the data cannot answer, each with the **exact check** that would answer it, who runs it,
and what decision it unblocks. Ranked by the size of the decision waiting. Include at minimum:
Robert's 1.81 ROAS (unverified), the null COGS SKUs, whether the fulfilment complaints are an
operational or a communications failure, and whether Linda–Clarity is a real segment or collapses
into Linda–Energy.

# STYLE

Write for someone who has never made an ad and must execute at expert level. Plain sentences. No
marketing throat-clearing. Tables where the content is structured, prose where it is an argument.

Lead every section with the decision it drives, then the evidence — someone reading only the first
line of each section should still be able to act.

Where you are uncertain, say "I don't know, and here is the check that would tell us" rather than
hedging into vagueness. A confident wrong answer costs more than an honest gap.

# BEFORE YOU BEGIN

State in four lines: how many quotes you have after dedupe and how they split by corpus; which of the
four ICPs the measured data supports and which it undermines; how you resolved conflict C2; and the
single biggest gap you found. Then write the document.

<!-- ------------------------------------------------------------------ -->
<!--  ---8<---  PROMPT ENDS  ---8<---                                    -->
<!-- ------------------------------------------------------------------ -->

---

## Follow-up prompts

Each assumes the Master document is in context.

**Expand a pillar**
> Take pillar `<<< NAME >>>` from the Creative Intelligence Master. Produce six concepts filling
> cells not already in the grid — each with a Concept ID, evidence tier, fifteen hooks in the winning
> architecture sourced to quote IDs, and a full timecoded script for the top two. Same precedence
> rule, same claim triage.

**Test the untested template**
> "Not all X is created equal" is the best-CPM structure in the account ($57.47 vs $98.37), produced
> three of twelve winners, and has only ever run on Astaxanthin — 4% of revenue. Build six NMN
> concepts on it, across Linda and Robert, at Solution-aware and Product-aware. Fifteen hooks each.
> This is the highest-expected-value untested creative in the account; treat it accordingly.

**Strip-mine a winner**
> Concept `<<< ID >>>` won at `<<< conv/click >>>` over `<<< clicks >>>`. Run the full iteration
> ladder: three new hooks on the same body, three new creators on the same script, length cuts,
> format port to static and carousel, awareness port up and down, persona port to Robert. Output
> every asset as a brief. One variable per iteration.

**Weekly scorecard**
> This week's ad-level data: `<<< PASTE >>>`. Rank every ad on **conversions per click**. For each
> under 2.8% after 40+ clicks: kill. 3.0–4.0%: name the specific fix and the fix code. ≥4.0%: scale
> +20–30%. Use engagement metrics only to diagnose *which stage* failed, never to decide promotion.
> Finish with five new quotes mined from this week's ad comments, tagged on all four axes and scored
> on the six markers.

**Monthly re-gap**
> Re-run the Gap Analysis against this month's data: `<<< PASTE >>>`. Report which gaps closed,
> reopened, or are new — gaps reopen as you scale. Re-rank the seven angles on current data. Then
> recalculate the offer math against the 1.70 breakeven; if AOV or CVR moved, every threshold moved.

**Harvest the missing emotions**
> Our own comment corpus returns zero hope and zero shame. Here is `<<< new source: Okendo reviews /
> post-purchase survey / Klaviyo replies / ManyChat transcripts / support tickets >>>`. Mine it for
> hope, relief, pride and grief specifically. Tag on all four axes, score on the six markers, and
> report which previously-empty cells are now filled.
