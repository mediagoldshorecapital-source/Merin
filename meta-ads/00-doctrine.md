# 00 — Doctrine: the reconciled strategy

Read this once, fully, before touching Ads Manager. Everything else in this SOP is a
mechanical consequence of what's decided here.

---

## 1. What the four sources actually agree on

Strip the branding off the four frameworks and they converge on the same five claims.
These are the load-bearing beliefs of the whole system.

| # | Claim | Ole Strand | Blue Sense | Alex Becker | Charley T |
|---|-------|:---:|:---:|:---:|:---:|
| 1 | **Creative is the targeting.** Interests and lookalikes are dead; Andromeda reads the asset and finds the audience. | ● | ●●● | ●● | ●● |
| 2 | **Consolidate data.** Fragmented structures starve the model of conversion density. | ●●● | ●●● | ○ | ●●● |
| 3 | **Diversity of concept, not volume of ads.** Near-duplicate assets collapse into one Entity ID and buy the same people twice. | ● | ●●● | ●● | ●●● |
| 4 | **Patience is a structural requirement, not a personality trait.** Short windows and reactive pausing are the primary destroyer of accounts. | ●●● | ● | ○ | ●●● |
| 5 | **Signal quality and unit economics beat tactics.** Better EMQ and better margin win auctions that better creative cannot. | ○ | ●●● | ●● | ○ |

**Our doctrine, in one sentence:** run *one consolidated CBO campaign* fed by a *small
number of maximally-distinct creative concepts*, protect every new concept with a *forced
learning budget*, and make every start/stop/scale decision on a *7-day window against a
threshold derived from unit economics*.

---

## 2. Where they contradict each other — and what we do

This is the section that saves the account. Following the PDF literally produces a broken
build, because three of its recommendations are mutually exclusive.

### Conflict A — Campaign count

- **Becker:** build 3 separate campaigns, one per buyer profile ("systems"), each a
  self-contained 5–8 ad funnel.
- **Ole Strand, Charley T, Blue Sense:** one campaign. Splitting campaigns silos
  conversion data and starves the model.

**Ruling: one campaign.** Blue Sense's mechanism explanation wins on evidence — the
learning phase threshold (~50 purchases per ad set per 7 days) is enforced *per ad set*,
so every split you make multiplies the conversion volume you need to escape learning.
Three campaigns at $100/day each is three permanently learning-limited campaigns. One
campaign at $300/day is one campaign that can actually exit learning.

**But Becker isn't wrong about the idea** — he's wrong about the level. His "system per
buyer profile" is preserved as **one concept-siloed ad set per angle**, inside the single
CBO. Same segregation of messaging, none of the data fragmentation.

> **Becker's genuinely durable contributions — kept in full:** angle-matched landing pages
> (file 09) and feeding high-AOV purchase data back to Meta (file 01, §6). Those two are
> the parts of his framework nobody else covers, and they are worth more than his campaign
> architecture.

### Conflict B — How many ads

- **Charley T:** exactly 5 ads. Testing volume creates the Doom Cycle.
- **Synthesis section (p.16–18):** minimum 3 ads per concept ad set, produce 1 new ad per
  $1,000 monthly spend.

**Ruling: both, at different levels.** These are describing different things and the PDF
never says so.

- **5 Rings = 5 *jobs*.** A permanent, fixed set of roles the funnel must fill. This
  number never changes.
- **Creative quota = *assets per job*.** How many candidate executions you produce to fill
  those five roles, refreshed continuously.

So at $9,000/month you produce 9 new ads — but they are not 9 new *ads in the account*.
They are 9 new candidates competing to become the next Ring 1, Ring 4, etc. Only winners
graduate into CONTROL. The live ad count stays disciplined; the production pipeline stays
full. **Volume in the pipeline, restraint in the account.**

### Conflict C — The offer price

The document states the Buy 3 Get 3 Free bundle as **~$58** (Ole, p.2–3), **$99.98**
(Becker, p.8, p.10), and **"Save 75%"** (Charley T, p.14). It also gives an AOV *range* of
$58–$106 and a single-bottle price of both $29.98 and $30.

**Ruling: these are different things being conflated.** Almost certainly:
- $99.98 = the *list price* of the B3G3 bundle
- $58–$106 = the *measured blended AOV range* across all carts
- ~$58 = the *floor* of that range

**Working assumption for this SOP: blended AOV = $58.** We use the floor deliberately —
every threshold derived from AOV (forced spend limits, CPA ceilings, break-even) should be
conservative, so that being wrong makes you *more* profitable, not less.

> ⚠️ **Before launch, replace this assumption with your real number.** Pull trailing-30-day
> blended AOV from Shopify or Triple Whale and write it into `02-economics-and-kpis.md`.
> If your true AOV is $85, you are leaving scale on the table by budgeting for $58.

### Conflict D — Dayparting (the one nobody flagged)

Two sources instruct you to concentrate delivery at 11:00 AM and 7:00 PM EST to match
Linda's scrolling windows.

**This is not compatible with the structure we just chose.** Ad scheduling / dayparting in
Meta requires a **lifetime budget at the ad set level**. Our architecture uses a *daily*
budget at the *campaign* level. You cannot have both.

**Ruling: do not daypart the ads.** The dayparting insight is real but belongs in channels
where you control send time:

| Lever | Where the 11 AM / 7 PM EST insight goes |
|-------|------------------------------------------|
| Meta ads delivery | ❌ Not used. Let CBO optimize timing; it already knows when Linda converts. |
| Email / SMS sends | ✅ Schedule Klaviyo sends into those windows |
| Organic / Trial Reels posting | ✅ Post into those windows |
| Budget increases | ✅ Apply Monday-morning increases before 11 AM EST so the day's delivery has headroom |
| Launch timing | ✅ Thursday–Saturday launches, never Monday (Linda's worst converting day) |

Trying to force dayparting into the ads would cost you CBO, ad set spending limits, and
the forced-learning mechanic — the three things holding the whole system up. Not worth it.

---

## 3. The architecture

### 3.1 The one campaign

```
PI | CORE | CBO | Sales
├── CONTROL          — proven winners, Rings 1–5, no spending limit
├── TEST-A           — one 3:2:2 Flexible Ad, min daily spend $58
└── TEST-B           — one 3:2:2 Flexible Ad, min daily spend $58
```

- Objective: **Sales**, optimizing for **Purchase**
- Budget: **campaign-level daily budget** (Advantage campaign budget ON)
- Targeting, identical on all three ad sets: United States · Women · 48–65 · no interest
  layers · Advantage+ audience ON · **exclude 180-day purchasers**
- Placements: **Advantage+ placements** (all). Do not manually restrict — you'd cut off the
  placements where statics find warm users.
- Attribution: 7-day click, 1-day view

**Why the ad sets are identical in targeting:** they are not audience tests. They are
*concept containers*. The audience differentiation happens inside Andromeda, driven by the
creative. This is the single biggest mental shift from pre-2024 media buying, and the one
beginners get wrong most often.

### 3.2 Budget tiers — the structure changes as you scale

The PDF gives one structure. In practice, three ad sets at $58 forced minimum each is
impossible below ~$175/day. Use the tier that matches your actual spend.

| Tier | Daily budget | Ad sets live | Min spend limit per test | What to expect |
|------|-------------|--------------|--------------------------|----------------|
| **T1 — Foundation** | $100–174 | CONTROL + **TEST-A only** | $58 | Permanently learning-limited. This is a *data collection* phase, not a scaling phase. Accept it. |
| **T2 — Healthy floor** | $175–499 | CONTROL + TEST-A + TEST-B | $58 | CONTROL can exit learning. This is where the system starts working as designed. |
| **T3 — Scaling** | $500–1,499 | CONTROL + TEST-A/B/C | $87 (1.5× AOV) | Add a third test slot. Concept-siloed CONTROL split becomes viable. |
| **T4 — Split** | $1,500+ | Core CBO **+** separate Testing CBO at 15–20% of total | $116 (2× AOV) | Only now does a second campaign stop hurting you. Testing spend is large enough to stand alone. |

> **The learning-phase floor is real math, not a vibe.** 50 purchases / 7 days × your
> target CPA ÷ 7 = the daily spend one ad set needs to exit learning. At a $25 target CPA:
> 50 × $25 ÷ 7 = **$179/day**. Below that, "Learning limited" is your permanent state and
> you must judge on cost-per-purchase and spend migration instead of on learning status.

### 3.3 What we deliberately do NOT build

| Not building | Why |
|--------------|-----|
| Separate retargeting campaign | Broad + Advantage+ already reaches warm users, and Rings 4–5 are the closers. A retargeting campaign at this spend level steals conversion density from CORE for no incremental lift. Revisit at T4. |
| Interest / lookalike ad sets | Andromeda ignores your labels. You're paying for a smaller auction pool and getting nothing. |
| ABO testing campaign | Fragments data. The forced spending limit inside CBO gives you ABO's protection without ABO's cost. |
| Separate campaigns per angle | See Conflict A. |
| Manual placement selection | Cuts off the placements where statics convert the demand videos created. |
| Dayparting | See Conflict D. |

---

## 4. The two mental models that prevent 90% of beginner damage

### Model 1 — Funnel Synergy (why static ROAS is a lie)

Static image ads will show you a beautiful ROAS. Top-of-funnel videos will show you an
ugly one. **Both numbers are true and the conclusion you want to draw from them is wrong.**

```
   Video ad (Ring 1)                     Static ad (Ring 4)
   ─────────────────                     ──────────────────
   Serves to cold users                  Serves to users who already
   Creates the demand                    watched the video
   Gets last-click credit                Gets last-click credit
   almost never                          almost always

   Reported ROAS: 1.4x                   Reported ROAS: 4.8x
   Actual contribution: the              Actual contribution: closing
   entire pipeline                       demand it did not create
```

Kill the video because of its ROAS and the static's ROAS collapses within two weeks,
because you just turned off its supply of warm users.

**The rule:** judge Rings 1–3 on **Amount Spent** and ad-set-level incremental ROAS. Judge
Rings 4–5 on cost per purchase. Never compare a video's ad-level ROAS to a static's.

### Model 2 — The Doom Cycle (why volume testing destroys accounts)

```
   You launch 20 new ads
             ↓
   Meta tests them on your warmest, most-likely-to-convert users
   (that's the cheapest place to get a signal)
             ↓
   Those users are no longer available to your proven ads
             ↓
   Your proven ads' ROAS drops
             ↓
   You panic and pause your proven ads
             ↓
   You now have 20 unproven ads and no revenue
             ↓
   You launch 20 more new ads  ─────────────┐
             ↑                              │
             └──────────────────────────────┘
```

The exit is at the top: **launch two concepts at a time, into dedicated ad sets, with
forced minimum budgets, and leave the control alone.**

---

## 5. The Prime Ingredients context this is tuned to

Everything above is generic system design. These are the facts that make it *this* account's
plan.

| Dimension | Fact | Consequence for the build |
|-----------|------|---------------------------|
| Persona | "Linda", F62 (sweet spot 58–68), Sunbelt/retirement corridors: AZ, FL, TX, CA, NV | Age range 48–65 with creative skewed 55–65; creators cast at 55–65, not 35 |
| Secondary persona | "Robert", M60–72, retired professional, recovery/performance | Do **not** add to CORE. Becomes a separate concept ad set at T3+ |
| Platform split | Facebook 60%, Instagram 34% = 94% of revenue | Advantage+ placements is safe; FB Feed will dominate and that's correct |
| Device | Tablet converts at 5.11% — the highest | Landing pages and creative must be checked on iPad, not just phone |
| Buying windows | 11 AM EST and 7 PM EST | Email/SMS + organic scheduling lever, not an ads lever (see Conflict D) |
| Worst day | Monday | Never launch new ad sets Monday. Launch Thu–Sat |
| Offer | Buy 3 Get 3 Free — 3 free bottles reads as a trust signal to a burned buyer | Bundle is the *primary* landing page offer, not single bottles |
| Commitment frame | She sees NMN as a 3–6 month commitment | Lead with multi-month framing; it justifies the bundle without a discount fight |
| Core insecurities | 3 PM crash · brain fog / memory anxiety · energy for grandchildren · supplement skepticism | These are the four Angles. Nothing else gets written |
| Email provider | Legacy (Yahoo/AOL) | Matters for CAPI match quality and Klaviyo deliverability, not for ads targeting |

### The four Angles (fixed — all creative maps to one of these)

| Code | Angle | Emotional job |
|------|-------|---------------|
| `3PMCRASH` | The 3 PM Afternoon Crash | Agitate a fatigue she is feeling *right now*, in real time |
| `BRAINFOG` | Brain Fog / Memory Anxiety | Agitate the fear of cognitive decline and lost independence |
| `GRANDKIDS` | Energy for the Grandchildren | Agitate purpose, and "becoming invisible" |
| `SKEPTIC` | Supplement Skepticism | Neutralise the "I've been burned by fake supplements" objection |

### The hook rule

> **Never open with a broad callout.** "Listen up, women over 50!" is a dead hook — it
> announces an ad. Open on problem agitation, in her words, about a sensation she had this
> week.
>
> ✅ *"It's 3 o'clock and I'm already done for the day."*
> ✅ *"Feeling more tired as you age? It's not just aging."*
> ❌ *"Attention women over 50 — are you tired?"*

---

## 6. Decision rights — who may change what

Ambiguity about who's allowed to touch the account is how accounts die. Fill this in and
enforce it.

| Action | Who | When | Requires |
|--------|-----|------|----------|
| Pause an ad | Media buyer | Any Monday | 7-day data + threshold cited |
| Pause an ad set | Media buyer | Any Monday | Full forced-spend cycle complete (7 days at min) |
| Pause the top-spending ad | **Nobody** | — | Requires written owner sign-off. Default answer is no |
| Budget change | Media buyer | Monday only, ≤ 20% | Question 1 answered YES |
| Launch a new test ad set | Media buyer | Thu–Sat | Slot is empty + 3:2:2 assets pass Entity-ID check |
| Change targeting | Owner | Never, in practice | Written rationale; this resets everything |
| Change the offer | Owner | — | Re-run the economics worksheet first |
| Emergency full pause | Owner | Anytime | Tracking outage, compliance issue, or stockout only |

---

**Next:** [`01-foundations-sop.md`](01-foundations-sop.md) — build the plumbing before you build the campaign.
