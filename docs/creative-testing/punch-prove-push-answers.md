# Punch → Prove → Push: Answers, Benchmarks & Open Questions

**Source of truth:** *The Creative Testing Playbook* (Epic Ads Lab) — "For Scaling Meta Ads from $250/day to $2,500/day".

**Not consulted:** the Notion page *Ads Creator Labs* (`3b6a46f065b5802da691db644b058c72`). It is blocked by the network egress proxy in this environment and no Notion connector is authorised on the account. Anything marked **[GAP]** below may already be answered there.

Throughout: **[PLAYBOOK]** = stated verbatim/near-verbatim in the doc. **[INFERRED]** = a reasonable read of the doc's logic, not written in it. **[GAP]** = not in the doc at all — take it to Skool.

---

## 0. Corrections to the stated understanding (read this first)

The three-stage summary in the question is directionally right but three details are wrong against the playbook:

| Stated understanding | What the playbook actually says |
|---|---|
| Punch = $100/day, **1 ad set containing ~25 creatives** | **[PLAYBOOK]** Punch = CBO, Sales objective, **$150–200/day total**, **1 ad per ad set**, broad 18–65+, no interests, automatic placements. So ~25 creatives = ~25 ad sets, one ad each. The whole point of CBO here is that Meta "votes with budget" *between ad sets* — that vote cannot happen if all 25 ads sit in one ad set. |
| Prove = one dedicated 'Prove' ad set | **[PLAYBOOK]** Prove is a **separate campaign** (Manual CBO), running the 3–5 surviving creatives across **2–3 audience types max** — Broad, Engaged Shoppers, Brand-interest stack, Lookalike stack (50% viewers / 180d site visitors / engagers). It is a creative × audience grid, not a single ad set. |
| Prove uses a min spend limit of 25% of daily budget / $25/day | **[PLAYBOOK]** confirms the *mechanism* — "Use ABO to ensure equal spend for testing audiences **or force minimal spend**" — but gives **no percentage or dollar figure**. The 25% / $25 number is not from the doc. **[GAP]** |

Also worth knowing before using the doc as an SOP — it contradicts itself in a few places:

- Creative volume: body says **"Upload 25+ unique creative assets"**; the Punch checklist and the At-a-Glance summary both say **"10–20 assets."**
- Hands-off window: body says **"Let campaigns run for 5–7 days"** and "do not edit during first 5–7 days"; the Punch checklist says **"No interference for 72 hours minimum."**
- Prove has two sections both numbered "3", and says "Campaign Type: Manual CBO" then immediately "Use ABO to ensure equal spend."

Where they conflict, the body text (25+ creatives, 5–7 days) is the more detailed and more recent-looking instruction. Confirm in Skool.

---

## Question Set 1 — Structure & cadence

### 1.1 Batch cadence & account structure — new campaign per batch, or persistent campaign?

**[PLAYBOOK]** The cadence is explicit: *"Run the Punch–Prove–Push cycle every 7 days"*, and the Push checklist sets *"Remix cadence set weekly (Monday = audit + launch)"* and *"New Punch round in motion to replenish pipeline."* So a 3–5 day batch is **faster than the playbook's own cycle** — the doc is built around a 7-day heartbeat.

**[INFERRED]** The playbook never states "new campaign vs. persistent campaign" directly, but its naming convention answers it by implication. The campaign format is `[Objective]_[Test/Scale]_[Theme/Offer/Month]` with examples like `CBO_Test_PainRelief_May24`. That is a **theme + month** key, not a batch key — meaning one testing campaign is expected to span many batches within a theme/month.

Recommended structure:

- **One persistent Punch campaign per theme/offer, rotated monthly.** Rotate ad sets inside it; do not spin up a campaign per batch.
- Roll to a fresh campaign only when (a) the month/theme in the name changes, (b) the offer materially changes, or (c) the campaign has accumulated so many paused ad sets that the view is unreadable.
- **Why:** each new campaign resets campaign-level conversion history and re-enters learning; a campaign-per-batch at 3–5 day intervals means you'd be permanently in learning and never accumulate the signal density the doc says Meta needs (*"The more volume, diversity, and signal you feed it — the faster it learns"*).

**Practical shape at your cadence:** hold **~20–25 active ad sets max** in the Punch campaign at any time. Each Monday: pause the previous batch's failures, launch the new batch into the same campaign. This keeps a rolling window of roughly 1.5–2 batches live.

⚠️ **Budget warning.** At $150–200/day across 25 ad sets in CBO, average spend is $6–8/ad set — but CBO does not spread evenly, so realistically only ~5–8 ad sets get meaningful spend and the rest get near-zero. That is *by design* (the playbook explicitly says *"watch spend allocation"* and *"Meta votes with budget"*), but it means at $100/day you are under-funding the test. **$150–200/day is the floor for a 25-creative Punch round**, not $100.

### 1.2 Pruning non-performers

**[PLAYBOOK]** There is an explicit kill rule, but it lives in the **Prove** chapter under "2. Pause the Losers." Pause anything with:

- **No spend** (Meta declined to fund it — that *is* the verdict)
- **CTR (All) < 0.75%**
- **No conversions AND no engagement**

Rationale given: *"Keep your testing campaigns clean to keep data sharp."* The Prove chapter also lists *"Using too many ad sets → spreads spend too thin"* as a top mistake.

**Best practice for your rolling batch launches:**

1. **Prune on the same clock as you launch.** The audit and the launch are one Monday action, in this order: (a) evaluate the batch that has now run 5–7 days, (b) promote 3–5 candidates to Prove, (c) pause the rest against the three criteria above, (d) launch the new batch into the now-clean campaign. Do not launch a new batch on top of an un-pruned one — you'll be splitting a fixed CBO budget across two batches' worth of ad sets.
2. **Pause, never delete.** The playbook's Push chapter depends on reusing the **original Post ID** of a winner to keep social proof. Deleting an ad set destroys that. Pausing preserves the post and its engagement.
3. **Prune the ad set, not just the ad** — since Punch is 1 ad per ad set, they're the same decision, and leaving empty/paused ad sets active in a CBO still lets Meta consider them for spend.
4. **[INFERRED]** Retire the *campaign* only on the monthly/theme rotation, not per batch.

**[GAP]** The playbook gives no rule for shutting down an older **testing campaign** as a whole, and no maximum number of active ad sets. Those numbers above are inference.

### 1.3 Evaluation window & lifecycle

**[PLAYBOOK]** — the windows are stated:

| Stage | Window | Rule |
|---|---|---|
| Punch | **5–7 days** untouched (checklist says 72h minimum) | *"Do not kill ads unless CPA is outrageously high. Avoid making edits that restart the learning phase."* |
| Prove | **3–5 days** uninterrupted | *"Don't optimize early. Don't edit the campaign."* Do not optimise before **day 3**. |
| Push | Ongoing, judged on **3-day, 7-day and 14-day ROAS windows** | Managed by fatigue signals, not a fixed lifespan. |

So the full pipeline from launch to a scaling decision is roughly **8–12 days**, and an ad in Push has no fixed expiry — it runs until a fatigue signal fires:

**[PLAYBOOK] Rotation / fatigue triggers:**

| Signal | Action |
|---|---|
| Frequency > 2.2 | Launch remix. Pause original. |
| CTR drops > 25% | Refresh hook or angle. |
| Comments drop / turn negative | Rotate creator, format. |
| CPA starts to climb | Split test variants. Pull new from Prove. |

### Strong hook/hold but no conversions after 1–2 weeks — kill, tweak, or fund?

**Tweak. Specifically: keep the hook, rebuild the middle and the close.** Here's the playbook logic that gets you there:

- **[PLAYBOOK]** Punch measures *"engagement potential, not profitability"* — a high Hook Rate and Hold Rate mean the ad passed Punch. What it has failed is **Prove**, whose explicit test is CPA stability. So the creative is a **validated attention asset with a broken conversion mechanism**.
- **[PLAYBOOK]** The playbook's own remedy set is the **5 variant types**, and two of them target exactly this failure:
  - **CTA Variation** — *"Change offer close — urgency, social proof, incentive."* If people watch and don't buy, the close is the suspect.
  - **Format Shift** — *"Turn winning video into a meme, static, or carousel."*
  - **Shortened Cut** — compress to 15–25s; strong hold on a long ad often means engagement without intent.
  - (Hook Swap and Creator Swap are the *wrong* fixes here — the hook is already working.)
- **[PLAYBOOK]** *"Don't kill based on ROAS in this phase"* applies to Punch only. Once it's in Prove, CPA is the judge and it has failed.

**So the decision rule:**

- Kill the **specific execution** — stop funding that exact cut. It has had 1–2 weeks; it isn't going to convert with more spend.
- Keep the **hook/angle**, which is proven data. Feed it back into Punch as 2–3 new executions with a changed close, changed length, and changed format.
- **Do not** give it more spend hoping conversions catch up. The playbook's entire premise is that Punch findings are *"candidates for validation"* and *"Don't chase one cheap purchase. Look at the full picture"* — the inverse applies too: don't chase one strong hook rate.

**[GAP]** The playbook gives **no spend ceiling** for this decision (see Q3.1). "1–2 weeks with no conversions" is your framing; the doc never sets a maximum spend before a kill.

---

## Question Set 2 — Account consolidation for Q4

### Diagnosis against the playbook

Your account breaks four rules the playbook states explicitly:

| Your setup | Playbook rule broken |
|---|---|
| Testing: 56 ad sets, 226 ads, **3 creatives per ad set** | **[PLAYBOOK]** Punch = *"1 ad per ad set."* With 3 ads per ad set, Meta picks a winner *inside* the ad set and starves the other two — you get one usable read per ad set, not three. You are paying for 226 ads and learning from ~56. |
| 100+ ad sets across two campaigns | **[PLAYBOOK]** *"Using too many ad sets → spreads spend too thin"* is listed as the #1 mistake in Prove. |
| Scaling: **56 ad sets, 1 ad each** | **[PLAYBOOK]** Push = *"Ad Set(s): **1**. Ads: your **2–3** best-performing creatives."* You have 56× the structural surface the doc calls for. |
| Testing $350/day > Scaling $120–200/day | **[INFERRED]** The doc has Punch at **$150–200/day** and Push starting at **2–3× Prove spend**. Testing is meant to be the smaller line item. Yours is inverted — you are paying to discover winners you then refuse to fund. |

The audience fragmentation you're describing is the mechanical consequence: 56 broad-ish ad sets in one CBO all bid into the same auction pool, so you are outbidding yourself, inflating your own CPMs, and none of them ever clears the ~50 conversions/week that stabilises a Meta ad set.

### 2.1 Testing pipeline — how to test without bloating

**Target state — one Punch campaign, hard-capped:**

- **Campaign:** 1 × CBO, Sales objective, named `CBO_Test_[Theme]_[Month]`
- **Budget:** $150–200/day **[PLAYBOOK]** (down from $350 — the freed $150–200 goes to scaling)
- **Structure:** **1 ad per ad set**, broad 18–65+, no interests, automatic placements **[PLAYBOOK]**
- **Cap:** **~20–25 active ad sets** at any time **[INFERRED]** — enforced by the Monday prune, not by willpower
- **Rhythm:** Monday = audit + prune + launch **[PLAYBOOK]**
- **Hands off 5–7 days** after each launch **[PLAYBOOK]**

**On the "winner mix" ad set inside the testing campaign — remove it.** This is the single highest-leverage fix in your testing campaign:

> In a CBO, budget flows to whatever is performing. A proven historical winner will *always* out-perform a cold, unproven test creative on day 1. So your winner-mix ad set is systematically absorbing the budget that was supposed to be discovering your next winner. You are paying testing rates for scaling delivery, and simultaneously starving the tests.

**[PLAYBOOK]** Historical winners belong in **Push**, reused via their **original Post ID** so they retain accumulated likes/comments/shares. There is no "winner mix in the testing campaign" concept anywhere in the doc.

**How to rotate winners vs. fresh tests instead:**
- Fresh tests → Punch campaign, cold, 1 per ad set, they sink or swim on their own signal.
- Historical winners → live in the Push campaign permanently, on their post IDs.
- A retired winner you want to revive → don't re-run the old file. **[PLAYBOOK]** Run it through the 5 variant types (Hook Swap / Shortened Cut / Format Shift / Creator Swap / CTA Variation) and launch the *variant* into Punch as a normal test.

**[GAP]** The playbook has no concept of a benchmark/control ad inside the testing campaign. If the winner-mix ad set exists to give you a performance baseline, ask Skool how to get that baseline without letting the control eat the budget.

### 2.2 Scaling structure & Flexible Ads

**[PLAYBOOK]** Push is **three campaigns**, not 56 ad sets:

**A. Manual scaling CBO**
- Audience: Broad, 18–65+, no targeting
- **Ad sets: 1**
- **Ads: your 2–3 best performers** (on original Post IDs)
- Budget: **2–3× what those creatives spent during Prove** (doc's example: £100 → £250/day)
- Naming: `PUSH_BROAD_CBO_June_CreativeA+CreativeB`

**B. Advantage+ Shopping (ASC)**
- Ads: **2–4 remixed variants** of the winner(s)
- Exclusions: **purchasers 30d**, **ATC/IC/VC 14d**
- Budget: match or slightly exceed the CBO

**C. Retargeting CBO**
- Audience: 7d VC, IC, ATC
- Creative: static testimonials, offer reminders, problem/solution reframes — *"High-CTR statics or memes work well here"*
- Budget: **10–15% of total account spend**

**Plus, on all Push campaigns [PLAYBOOK]:** exclude 180-day purchasers (pixel), CRM uploads (Klaviyo / Shopify CSV / Shopify Audiences), and optionally 180-day site visitors.

**On stacking 20+ assets into one Flexible Ad:** **[GAP]** — the playbook does not mention Flexible Ads at all. But two of its explicit rules argue against 20+ assets in one:

1. **[PLAYBOOK]** *"Share of spend per creative — don't let one ad take 90% if others convert too."* You cannot enforce or even easily read that inside a Flexible Ad, where asset-level delivery is opaque.
2. **[PLAYBOOK]** The Post ID doctrine — *"Keeps all social proof attached to the ad… Reduces CPMs and boosts CTR"* — is hard to preserve when assets are bundled into a flexible unit rather than run as the original post.

**Recommendation:** consolidate into **standard CBO ad sets with 2–3 creatives each**, as the doc prescribes. Use Flexible Ads at most as a *fourth* test line, never as the primary scaling vehicle — and confirm this one in Skool, since it is genuinely outside the document.

### 2.3 Q4 consolidation directive for your media buyer

Copy-paste-able. Everything marked **[PLAYBOOK]** is doc-sourced; the budget split is inferred.

> **Q4 Account Consolidation — Directive**
>
> **Step 1 — Audit (before touching anything).** Pull last 90 days at ad level, sorted by spend. Build the all-time winner list: creatives with **CPA within ±10–15% of target**, **CTR (Link) > 1.5%**, **Hook Rate > 30%**, **Hold Rate > 20%**, and **consistent conversions across 2+ audiences**. **[PLAYBOOK]** Expect **5–10 assets** to qualify, not 20+. Record the **Post ID** for every one of them before you touch the account.
>
> **Step 2 — Collapse scaling to one campaign.** Build `PUSH_BROAD_CBO_[Month]`: **1 ad set**, broad 18–65+, **2–3 top creatives**, each loaded via **"Use Existing Post" + original Post ID** — confirm the likes/comments carry over before publishing. **[PLAYBOOK]** Retire the 56-ad-set scaling campaign and the 20-asset flexible ad set. Do not migrate the also-rans.
>
> **Step 3 — Add ASC alongside it.** `ASC_Scale_[Offer]_[Month]` with **2–4 remixed variants** of the same winners. Exclusions: **purchasers 30d, ATC/IC/VC 14d**. Budget matching or slightly above the CBO. **[PLAYBOOK]**
>
> **Step 4 — Rebuild testing lean.** Cut the testing CBO from **$350 → $150–200/day**. Enforce **1 ad per ad set**. **Delete the winner-mix ad set** — historical winners live in Push only. Cap active ad sets at **~25**. **[PLAYBOOK]**
>
> **Step 5 — Reallocate the freed budget.** Move the ~$150–200/day out of testing into Push. Target split: **~60–65% Push (CBO + ASC), ~20–25% Punch/Prove, ~10–15% retargeting.** The 10–15% retargeting figure is **[PLAYBOOK]**; the rest is **[INFERRED]** — sanity-check it in Skool.
>
> **Step 6 — Set exclusions everywhere.** 180-day purchasers, CRM uploads (Klaviyo/Shopify), optionally 180-day site visitors, on every Push campaign. **[PLAYBOOK]**
>
> **Step 7 — Install the weekly rhythm.** Monday = audit + prune + launch. Track frequency and CTR daily. Fire the rotation rules: **frequency > 2.2 → launch remix, pause original; CTR drops > 25% → refresh hook.** Keep a Punch round always in motion to replenish the pipeline. **[PLAYBOOK]**
>
> **Q4 caveat:** the playbook contains **no Q4/BFCM-specific guidance** — nothing on CPM inflation, budget ramp schedules, or promo-period frequency tolerance. Do not assume the standard benchmarks hold through peak.

---

## Question Set 3 — SOP benchmarks

### 3.1 Kill benchmarks

| Criterion | Answer | Source |
|---|---|---|
| **Spend threshold** | **Not specified.** The playbook has *no* spend-multiple or dollar kill trigger anywhere. It kills on **time + signal**, never on spend. | **[GAP]** — see Open Questions |
| **Time window** | **Punch: 5–7 days untouched** (checklist says 72h minimum — the doc contradicts itself). **Prove: 3–5 days, no optimisation before day 3.** | **[PLAYBOOK]** |
| **Conversion volume** | **Not specified.** The doc says *"consistent conversions"* and *"performance held across 2+ audiences"* — it never gives a purchase count. | **[GAP]** |
| **Secondary metrics** | Full table below. | **[PLAYBOOK]** |

**Kill floor (Prove chapter, "Pause the Losers") [PLAYBOOK]:** no spend, **CTR (All) < 0.75%**, or no conversions + no engagement.

**Pass benchmarks:**

| Metric | Punch benchmark | Prove/Push benchmark |
|---|---|---|
| **CTR (All)** | **> 1.5%** | — |
| **CTR (Link)** | — | **> 1.5%** |
| **3s Plays** | **> 70% of impressions** | — |
| **Hook Rate** | **> 30%** | **> 30%** |
| **Hold Rate** | **> 20%** | **> 20%** |
| **Comments** | **> 3 per ad** | tracked for sentiment |
| **CPA** | *ignored* | **±15% variance** (Prove) / within **10–15% of target** (Push) |
| **ROAS** | *ignored* | Prove: optional, **1.5+ if tracked**, *"only for mature accounts / high data volume"*. Push: **at or above breakeven** |
| **Frequency** | — | Remix trigger at **> 2.2** (campaign-level, not per-ad) |

⚠️ **Two metric-definition corrections:**

1. **Hold Rate.** The playbook defines it as **average watch time ÷ video length** — *not* ThruPlays ÷ impressions. Those produce very different numbers, and a >20% bar calibrated to one is meaningless against the other. Use the playbook's definition or the benchmark doesn't apply.
2. **CTR.** The playbook deliberately uses **CTR (All) in Punch** and **CTR (Link) in Prove/Push** — it explicitly notes *"different to CTR (all)"*. Punch measures whether the creative earns *any* interaction; Prove measures whether it drives traffic. Both bars happen to be 1.5%, which makes Prove's the meaningfully harder one. Don't collapse them into one column.

**Where the playbook stands on your "no conversions yet" scenario [PLAYBOOK]:** in Punch, secondary metrics are the *only* judge — *"Don't kill based on ROAS in this phase"*, *"What to ignore: ROAS, Purchases, CPA."* An ad clearing CTR/Hook/Hold with zero purchases at day 5 is a **Prove candidate**, not a loser. Once it's in Prove and still isn't converting, CPA is the judge and it fails.

### 3.2 Transfer rules

**Punch → Prove [PLAYBOOK].** After 5–7 days, select **3–5 creatives** that had:
- CTR (All) > 1.5%
- Hook Rate > 30%
- Hold Rate > 20%
- **Consistent spend allocation from Meta** (the CBO kept funding it — this is arguably the strongest single signal)
- Positive comment sentiment

> *"These ads aren't winners yet. They're candidates for validation."*

**Prove → Push [PLAYBOOK].** Move **only 2–3 creatives at a time** when **all** of:
- CPA is stable (fluctuates within **10–15%**)
- They receive the **majority of spend**
- **Consistent conversions**
- **CTR (Link) > 1.5%**
- **Hook Rate > 30%**
- **Hold Rate > 20%**
- **ROAS trending at or above breakeven**
- **Performance held across 2+ audiences**

**On your proposed "ROAS > 2.5× over 7 days, 5–10 purchases":** neither figure is in the playbook, and the ROAS bar is materially stricter than what the doc asks for.
- The playbook's graduation bar is **breakeven ROAS**, not 2.5×. Its logic is that Prove tests *stability and repeatability*, and Push is where efficiency is built (via post-ID social proof, exclusions, and remixes). Holding creatives at 2.5× in Prove will starve your Push pipeline.
- Prove's optional ROAS line is **1.5+**, and even that is caveated *"only for mature accounts / high data volume."*
- **The 5–10 purchase minimum is [GAP]** — the doc never quantifies it.
- Note the **evaluation window is 3–5 days in Prove**, not 7.

**Post ID vs. duplicate — unambiguous [PLAYBOOK]: always use the original Post ID.**

> *"Instead of creating a 'new ad,' always use the original Post ID of your best-performing ad creative."*

Because it: keeps all social proof attached, prevents Meta from restarting performance data from scratch, reduces CPMs, boosts CTR, and strengthens buyer confidence mid-scroll.

**Method [PLAYBOOK]:** Testing campaign → **Preview → Share → Facebook Post with Comments** → click the timestamp under the brand name → copy the number from the URL (that's the Post ID) → in the scaling campaign, **Create ad → "Use Existing Post" → paste the Post ID → confirm the same likes/comments appear before launching.**
*Fallback:* if the preview flow fails, go to **Page Posts** in Meta's ad tools, search by the first line of copy, identify the right post by its likes/comments, and copy the ID there.

### 3.3 Budget & scaling rules

**Vertical scaling.** **[GAP]** — the playbook has **no incremental budget rule.** There is no "+20% every 48 hours," no percentage, no cadence. What it does give:

- **[PLAYBOOK]** The *initial* Push budget is **2–3× the creative's Prove spend** (example: £100 → £250/day). That is a one-time step-up at graduation, not an ongoing ramp.
- **[PLAYBOOK]** The health gate that would govern any increase: **CPA within 10–15% of target**, monitored across **3-day, 7-day and 14-day ROAS windows**, at **campaign level, not ad level** — *"Track campaign-level stats, not ad-level micromanagement."*
- **[PLAYBOOK]** ASC budget should **match or slightly exceed** the manual CBO.

**Horizontal scaling.** The playbook doesn't frame it as "duplicate vs. raise budget," but it does prescribe the horizontal moves themselves **[PLAYBOOK]**:

| Move | When |
|---|---|
| **Open an ASC campaign** with 2–4 remixed variants of the winner | Once the manual CBO is stable — *"Wider distribution with Meta automation."* |
| **Launch a remix, pause the original** | **Frequency > 2.2** |
| **Refresh hook or angle** | **CTR drops > 25%** |
| **Rotate creator/format** | Comments drop or turn negative |
| **Split test variants; pull fresh winners from Prove** | **CPA starts to climb** |
| **Add retargeting CBO** (7d VC/IC/ATC, statics/testimonials) | Standing allocation at **10–15% of total account spend** |

**[INFERRED] The synthesis:** the playbook's model is that you scale **horizontally by default and vertically only within a healthy campaign.** It never asks you to build fresh cold audiences to scale — Push is broad + ASC, with audience segmentation reserved for *Prove* (validation) and *retargeting* (bottom of funnel). Horizontal expansion in this system means **more creative variants and more campaign types (CBO → ASC → retargeting)**, not more audiences. If CPA holds and frequency is under 2.2, raise the existing budget; if frequency is climbing or CTR is decaying, the answer is new creative, not a duplicate ad set.

---

## Skool posts — the questions the Playbook doesn't answer

Five ready-to-post questions, ordered by how much each one blocks the SOP. **Post them one at a time, a few days apart** — dumping all of these into a single thread reliably gets zero useful replies. Post 1 is the one that actually unblocks the SOP; if you only post one, post that.

---

### Post 1 — Kill thresholds: what's the actual spend and conversion floor?

> **Title:** What spend / conversion floor do you use before killing a test ad?
>
> Working through the Creative Testing Playbook and building it into a written SOP for my media buyer. The framework itself is clear, but the kill rules are all time-and-signal based — 5–7 days in Punch, pause anything under 0.75% CTR — and I can't find a **spend** threshold or a **conversion count** anywhere in it.
>
> That's fine for the obvious losers, but it leaves the messy middle undefined. Concretely:
>
> 1. **What's the max spend a single test ad should reach before you make the kill/keep call?** 1× target CPA? 1.5×? 2×? A flat dollar number? Right now my buyer has no ceiling, so borderline ads just keep drinking budget until someone notices.
> 2. **What's your minimum purchase count** before you'll call something a genuine winner or a genuine loser? The playbook says "consistent conversions" but never puts a number on it. Is 3 enough? 5? 10?
> 3. **How do you handle the ad that clears every front-end metric but never converts?** Hook rate 35%+, hold rate above 20%, CTR fine — and after 1–2 weeks, zero purchases. My read of the playbook is that the hook is validated and the close is broken, so you keep the angle and rebuild the middle/CTA rather than killing it outright. Is that how you'd play it, or is that just me being sentimental about a creative that isn't working? And how many rebuild attempts before you drop the angle entirely?
>
> Real numbers from your own account would help more than theory here.

---


### Post 2 — Testing cadence & structure

> **Should I make a new testing campaign every time, or keep one and swap the ads?**
>
> We make about 25 new ads every 3–5 days. Before we scale the volume up, I want to get the setup right.
>
> **1. One campaign or many?**
> Every time we have a new batch of 25 ads, should we build a brand new testing campaign? Or keep one testing campaign running permanently and just add new ad sets and switch off the old ones? My worry with building a new campaign every few days is that it's always stuck in learning and never builds up any history.
>
> **2. How many ad sets is too many?**
> We run 1 ad per ad set. So one batch of 25 ads means 25 ad sets straight away. If the previous batch is still running, that's 50. At what number does this stop being a test and just become budget spread too thin?
>
> **3. Our batches overlap.**
> We launch every 3–5 days, but the playbook says leave ads alone for 5–7 days. So batch 2 goes live while batch 1 is still in its don't-touch window, and now the same budget is split across two batches. How do you handle that? Slow down to a strict 7-day cycle? Or give each batch its own campaign?
>
> **4. Quick one.**
> The playbook says "25+ creatives" in one place and "10–20" in another. It also says "leave it 5–7 days" in one place and "72 hours minimum" in another. Which numbers do you actually use?

---

### Post 3 — Consolidating the account

> **My account has over 100 ad sets. How would you clean it up?**
>
> Our budget is spread so thin that nothing gets going. Here's what we have:
>
> **Testing campaign — $350/day**
> 1 campaign, 56 ad sets, 226 ads. 3 ads in each ad set. We add new ad sets as we go. Plus one extra ad set holding 5–10 of our best-ever ads.
>
> **Scaling campaign — $120–200/day**
> 1 campaign, 56 ad sets with 1 ad in each. Plus one flexible ad set with 20+ winning assets.
>
> **The main problem:** we spend more on testing than on scaling. That feels backwards.
>
> Here's what I think we should do. Tell me if I've got it wrong:
>
> **1. Delete the "best-ever ads" ad set out of the testing campaign.**
> My thinking: in a CBO, Meta gives the budget to whatever performs best. A proven winner will always beat a brand new untested ad on day one. So that ad set is eating the money that's meant to be finding our *next* winner. Do you agree? And if you do want a benchmark inside your testing campaign, how do you stop it swallowing the budget?
>
> **2. Should it be 1 ad per ad set instead of 3?**
> With 3 ads in one ad set, Meta picks a favourite and barely spends on the other two. So we're paying for 226 ads but only really learning from about 56. Is that right, or is 2–3 per ad set fine in practice?
>
> **3. Flexible Ads — good or bad for scaling?**
> Is putting 20+ winning assets into one Flexible Ad actually effective? Or should we go back to a few normal ad sets with 2–3 ads each? Two things I can't work out with Flexible Ads: how do you keep the likes and comments from the original post, and how do you see which asset is actually getting the spend?
>
> **4. What budget split should we run?**
> How much should go to testing vs scaling vs retargeting? Ours is clearly upside down and I'd like a number to aim at.

---

### Post 4 — Scaling triggers

> **When do you raise the budget on a winner, and when do you duplicate it instead?**
>
> The playbook tells me how to *start* scaling — launch at 2–3× what the ad spent during testing. But it says nothing about what happens after that. Two things I'm stuck on:
>
> **1. Raising the budget.**
> What's your rule? Something like +20% every 2 days as long as CPA stays good? Or bigger jumps? And what do you check before each increase — CPA, frequency, number of sales?
>
> **2. Duplicating.**
> When do you copy a winner into a new campaign instead of just raising the budget on the one you already have? Is there a spend level where raising the budget stops working?
>
> **3. Does "scaling out" mean new audiences at all?**
> My reading of the playbook is that it doesn't. It means more creative variants and more campaign types — manual CBO, then ASC, then retargeting — while the targeting stays broad the whole way. Is that how you do it, or are you still building new cold audiences to scale?
>
> **4. Advantage+ Audience and Advantage+ Placements.**
> The playbook says "broad, 18–65+, no interests, automatic placements." That was written before Meta turned most of this on by default. Are you still setting anything by hand, or just leaving it on defaults?

---

### Post 5 — Q4

> **Do the normal benchmarks still work during Black Friday?**
>
> We're cleaning up our account before Q4, and I've realised every number I'm working from was written for a normal trading month. For anyone who's traded a few Q4s:
>
> **1. Which numbers change?**
> CPMs go up in Q4. Does the 1.5% CTR target still hold? Do hook rate 30% and hold rate 20% still apply, or do you accept lower?
>
> **2. Frequency.**
> Normally we swap in a fresh version once frequency goes past 2.2. Do you still do that in Q4? My gut says you can let it run higher during a promo because the offer carries it and the window is short — but I don't want to guess with peak budget on the line.
>
> **3. When do you start scaling up?**
> Do you ramp before the peak so campaigns are out of learning by the time CPMs spike? Or hold, then go big on the day?
>
> **4. Do you still test during Q4?**
> Or do you cut testing right back and put everything into proven winners? Ads seem to burn out faster when frequency is high, so I can see it going either way.
>
> Happy to report back with what we find.
