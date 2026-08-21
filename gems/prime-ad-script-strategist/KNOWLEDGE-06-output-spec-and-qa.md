# KNOWLEDGE 06 · Output Specification & QA Gate

This file defines **exactly** what a finished script looks like. Deviating from it is a defect, not a style choice.

---

## 1 · The asset ID convention

Adopt this everywhere. Prime currently has `- Video - Ad -2`, `- Video - Ad - 2` and `Video - Ad - 2` as **three
separate rows in reporting**, which is how learning becomes noise.

```
[Product]_[ICP]_[Awareness]_[Pillar]_[ConceptSlug]_[Format]_[Variant]
```

- **Product** — `NMN` · `ASTA`
- **ICP** — `Linda` · `Clarity` · `Margaret` · `Robert` · `All`
- **Awareness** — `UA` · `PA` · `SolA` · `PdA` · `MA`
- **Pillar** — `P1`–`P6`
- **ConceptSlug** — CamelCase, no spaces: `NotAllNMN`, `BecomingMyFather`, `SleepDoesntFixIt`
- **Format** — `UGC` · `FounderVO` · `Teardown` · `Whiteboard` · `SplitScreen` · `Static` · `Bumper`
- **Variant** — `v1`, `h1`–`h5` for hook swaps, `L30` for the 30s cut

Example: `NMN_Linda_SolA_P3_NotAllNMN_Teardown_v1`

---

## 2 · The required output blocks, in order

### Block 1 · Header

```
### SCRIPT 1 · [Concept name in plain English]
`[Asset ID]`
Framework: [# and name] · Pillar: [P#] · ICP: [name] · Awareness: [rung] · Format: [format]
Runtime: [m:ss] · Aspect: 9:16 master (crop 4:5, 1:1) · Target CPA: $[x] · Platform: [TikTok / Reels / Shorts]
```

If you made assumptions to fill any slot, add **one line**: `Assumed: [x], [y]. Say the word and I'll re-cut.`

### Block 2 · Direction note

Two or three sentences. Casting age and gender, register, location, lighting, music. **Be specific and
unglamorous.** Name the thing the director would otherwise get wrong.

> *Male 60–72, non-actor, someone who has done physical work. Register is refusal, not repair — flat,
> unsentimental, slightly reluctant. Garage and truck bed, overcast, available light, no music. One take per
> line; the first is always better on this register. If the take sounds moved, it is wrong.*

### Block 3 · Five hook variants

Numbered 1–5. For each: the **spoken line**, the **OST**, and one line on **who it disqualifies**. All five must
be cuttable onto the identical body (that is iteration rung 1).

```
**HOOK 1** — VO: *"..."*  ·  OST: `...`
   Disqualifies: [who scrolls past, and why that's the point]
```

### Block 4 · The script table — **the core deliverable**

Four columns, always these four, always in this order:

| BEAT / TIME | VO (SPOKEN) | OST (ON-SCREEN TEXT) | B-ROLL / VISUAL DIRECTION |
|---|---|---|---|

Rules:
- **Timestamps are real, cumulative and contiguous.** `0:00–0:03`, `0:03–0:08`, `0:08–0:14`… They must sum to the stated runtime.
- **The framework beat name goes in the BEAT column** beside the timestamp, so the editor can see the architecture.
- **VO is written as spoken** — contractions, fragments, the way she'd say it in a kitchen. Italics.
- **OST is written in the case it appears on screen**, usually caps. `OST: none.` is a valid and often correct entry — let a line land clean.
- **B-roll names the shot, the framing and the hold.** Never "show product." Write: *"macro insert, thumb turning the bottle to the lot number, rack focus onto the printed digits, hold two seconds."*
- **Inline flags live in the row they affect**: `⚠ SUBSTANTIATION: …` · `🔒 GATE: …` · `[VERIFY: …]`

### Block 5 · End card

Bottle, price ladder (per-bottle or per-day — **never a percentage**), single CTA, FDA footer. No countdown, no
starburst.

```
OST: 6 BOTTLES · 180 DAYS · 55¢ A DAY
     ONE-TIME PURCHASE AVAILABLE. NO SUBSCRIPTION REQUIRED.
Compliance footer: These statements have not been evaluated by the Food and Drug Administration.
This product is not intended to diagnose, treat, cure or prevent any disease.
```

### Block 6 · Compliance ledger

Every claim in the script, one row each.

| Line | Claim flag | Obligation |
|---|---|---|
| *"Supports cellular energy"* | ✅ Claimable | — |
| *"My skin looks better"* | ⚠ Testimonial only | Needs verified Prime customer + material-connection disclosure |
| *"60 capsules in the bottle"* | 🔒 Blocked | **G4** — open six bottles and count them |

Close with the asset-level verdict: `✅ CLEAR TO SHOOT` · `🔒 WRITE NOW, DO NOT UPLOAD — blocked on G#` ·
`⚠ NEEDS SIGN-OFF — [what and by whom]`.

### Block 7 · Why this should win

Three bullets, maximum. What it disqualifies · which proof tier it lands on · which measured pattern it inherits.

### Block 8 · Iteration ladder

How this one script becomes 8–15 assets. Name the five hook swaps (already written in Block 3), the length ladder
cuts, and the specific proof objects for rung 3.

---

## 3 · Worked example — the gold standard

Copy this structure exactly.

---

### SCRIPT 1 · Not All NMN Is Created Equal
`NMN_Linda_SolA_P3_NotAllNMN_Teardown_v1`
Framework: **14 · Solution-Aware "Alternative Disqualification"** · Pillar: **P3 Trust & Purity** ·
ICP: **Linda–Energy (Robert secondary)** · Awareness: **Solution-Aware** · Format: **Teardown + founder VO**
Runtime: **0:45** · Aspect: 9:16 master (crop 4:5, 1:1) · Target CPA: **$27** · Platform: Reels / TikTok / Shorts

> **Assumed:** NMN flagship, Solution-Aware rung, Linda primary. Framework 14 chosen because beats ①–③ are the
> category-quality contrast — 3 of 12 all-time winners and the best CPM in the account ($57.47 vs $98.37) — and it
> has **never been run on NMN, which is 93.5% of revenue.**

**Direction note.** Female 58–66 or the founder, seated, plain room, available light, no music. Register is flat
and faintly irritated — she is telling you a fact she has stopped questioning, not selling you anything. Two
bottles and a printed COA on the table in front of her from frame one; she does not pick anything up until 0:22.
Shoot on a phone. Visible clutter is a feature.

**FIVE HOOK VARIANTS** *(all cuttable onto the identical body — this is iteration rung 1)*

**HOOK 1** — VO: *"Not all NMN is created equal."* · OST: `NOT ALL NMN IS CREATED EQUAL.`
  Disqualifies: anyone who doesn't already believe supplements vary in quality. They opt out at line one, and you stop paying for their click.

**HOOK 2** — VO: *"Most of what's sold as NMN was never tested by anyone but the seller."* · OST: `NEVER TESTED BY ANYONE BUT THE SELLER.`
  Disqualifies: the price-only shopper. Signals this is a spec conversation before she's committed a second.

**HOOK 3** — VO: *"So I read the panel before I read the ad."* · OST: `none.`
  Disqualifies: everyone who has never read a supplement panel. Robert's opener — the silence is the qualification.

**HOOK 4** — VO: *"Two panels. One number. Let's read them."* · OST: `TWO PANELS. ONE NUMBER.`
  Disqualifies: the casual scroller. Promises work, not a promise.

**HOOK 5** — VO: *"I counted them. All sixty. Because somebody said I shouldn't have to."* · OST: `I COUNTED THEM.`
  🔒 **GATE G4** — do not shoot until the capsule count in ads, on the PDP and in the box is one number.

**THE SCRIPT**

| BEAT / TIME | VO (SPOKEN) | OST (ON-SCREEN TEXT) | B-ROLL / VISUAL DIRECTION |
|---|---|---|---|
| **① Pattern Interrupt**<br>`0:00–0:04` | *"Not all NMN is created equal."* | `NOT ALL NMN IS CREATED EQUAL.` | Hard cut in. Mid-shot, seated, plain room, no logo, no lower third. Two bottles and a printed sheet on the table, already in frame. She does not touch them. |
| **② Twist the Knife**<br>`0:04–0:11` | *"Most of it is two-fifty a capsule. Which means four of theirs to get what's in two of these. And at that point you're paying for the capsule, not the ingredient."* | `250mg × 4 = 1000mg`<br>`YOU'RE PAYING FOR THE CAPSULE.` | Insert: four generic capsules laid out on white next to two Prime capsules. Overhead, flat light, hold three seconds. **Generic bottle label obscured — G2 is check zero.** |
| **③ Alternative Disqualification**<br>`0:11–0:22` | *"No lot number on the bottle. A manufacture date printed where an expiry date should be. A proprietary blend so you can't see what's actually in it. And a certificate that isn't tied to your batch — which makes it a brochure."* | `NO LOT NUMBER`<br>`MFG DATE ≠ EXPIRY`<br>`PROPRIETARY BLEND`<br>`A COA THAT ISN'T YOUR BATCH` | Four fast inserts, one per line, each held ~2.5s: a bare bottle base with no printing · a thumb over a manufacture date · a panel where "proprietary blend" is the only line · a generic certificate sheet with no lot field. **Unbranded throughout.** |
| **④ Direct Solution Pivot**<br>`0:22–0:26` | *"This one has all four."* | `none.` | She picks up the Prime bottle for the first time. Holds it steady to lens, label fully legible, **no cutaway, four full seconds.** |
| **⑤ Mechanism & Benefit Stacking**<br>`0:26–0:34` | *"A thousand milligrams a serving, two capsules. Lot number printed on the bottle. Expiry date printed on the bottle. And the certificate of analysis for that exact lot, with the assay result on it. No proprietary blend — what's on the panel is the whole formula."* | `1000mg · 2 CAPS`<br>`LOT # ON BOTTLE · EXP ON BOTTLE`<br>`COA FOR THIS LOT · NO PROPRIETARY BLEND` | Macro: thumb turns the bottle to the lot number, **rack focus onto the printed digits, hold two seconds.** Cut to the printed COA sheet placed on the table, **lot number circled in pen, on camera.** Then the supplement facts panel, full frame, held still, finger tracing each figure as it is spoken.<br>⚠ **SUBSTANTIATION:** the COA shown must be **genuine and matchable to the lot on the bottle in frame.** A fabricated COA is a legal problem, not a compliance one. |
| **⑥ Emotional Agitation → True Desire**<br>`0:34–0:40` | *"I've been burned before. I don't want to find out in six months that what I've been taking never contained what the label said."* | `none.` **Let this land clean.** | Back to her, slightly closer. She sets the bottle down. Hands flat on the table. Static frame. **She does not smile here.**<br>*(Note: written as a disclosure she makes about herself — Law 4. Never "you don't want to find out…")* |
| **⑦ Reassurance Close & Offer**<br>`0:40–0:45` | *"Send it to any lab you like. If the assay doesn't match the certificate, we refund the order and pay for the test."* | `SEND IT TO ANY LAB.`<br>`IF IT DOESN'T MATCH, WE PAY.` | End card. Purple bottle on the table — not a studio surface. Price ladder. Single CTA. **No countdown, no starburst.**<br>⚠ **LEGAL:** the challenge guarantee needs **written terms live on site** before this line ships. Cap, window and process defined. |

**END CARD**

```
OST: 1 BOTTLE $29.98  ·  6 BOTTLES $99.98 = $16.66 EACH
     ONE-TIME PURCHASE AVAILABLE. NO SUBSCRIPTION REQUIRED.   🔒 G3
Compliance footer: These statements have not been evaluated by the Food and Drug Administration.
This product is not intended to diagnose, treat, cure or prevent any disease.
```

**COMPLIANCE LEDGER**

| Line | Flag | Obligation |
|---|---|---|
| *"Not all NMN is created equal"* | ✅ Claimable | Comparative on **specification**, not efficacy. Holds |
| *"250mg × 4 = 1000mg"* | ✅ Claimable | Arithmetic, on screen, verifiable |
| *"No lot number / mfg date / proprietary blend"* | ✅ Claimable | Category-general, unbranded. **No competitor bottle in frame — G2** |
| *"1000mg per serving, 2 capsules"* | ✅ Claimable | Corroborated on the panel shown |
| *"COA for that exact lot"* | ⚠ Substantiate | **Genuine, matchable COA in hand before the shoot** |
| Capsule count / 55¢-a-day | 🔒 Blocked | **G4** — deliberately omitted from this cut. Do not add it back until the count is one number |
| *"One-time purchase available"* | 🔒 Blocked | **G3** — needs a visible one-time option and a self-serve cancel link, genuinely live |
| Lab challenge guarantee | ⚠ Legal | Written terms live on site first |
| Second-person physiology assertion | ✅ None present | Beat ⑥ written as self-disclosure |

**VERDICT: 🔒 WRITE NOW, DO NOT UPLOAD.** Unblocks the day a genuine batch COA is in hand (⑤) and the one-time
option is live (end card). Hook 5 additionally blocked on G4. Beats ①–④ and ⑥ are clear as written.

**WHY THIS SHOULD WIN**
- **It disqualifies at line one.** A reader who doesn't already believe supplements vary in quality is gone before second four — which is the entire $31.90-vs-$58.09 mechanism.
- **It lands on the trust-signal table's top row:** a lot-specific public COA turns a claim into a receipt tied to the exact bottle in her hand. Wide open in this category.
- **It inherits the account's best measured structure.** Template 2 is 3 of 12 all-time winners and posts $57.47 CPM against $98.37 for the volume workhorse — **71% more impressions for the same money** — and has never been run on the 93.5% SKU.

**ITERATION LADDER — 8 to 13 assets from this one script**
- **Rung 1 · Hook swap (5):** the five variants above, cut onto the identical body and end card. Read 3s hold, then conv/click.
- **Rung 2 · Length ladder (4):** 45s master → 30s (drop beat ②) → 15s (beats ①, ⑤, ⑦) → 6s bumper (beat ① + end card).
- **Rung 3 · Proof-object swap (3):** the batch COA → the capsules counted on white 🔒G4 → the price arithmetic on paper 🔒G4 → the shipped bottle still in its box. Read CPA **and comment sentiment** — this rung is where the operational gaps get answered at scale.
- **Rung 5 · Persona re-cast (2):** same script, male 60–72 in a garage. Read CPA by age/gender. This is how you find out whether you built a persona or a mood.

---

## 4 · The QA gate — run before every output

**A · Structural**
- [ ] All eight blocks present, in order
- [ ] Timestamps contiguous and summing to the stated runtime
- [ ] Framework beat names in the BEAT column
- [ ] Hook inside 3 seconds; five hook variants supplied
- [ ] B-roll names shots, not intentions ("macro insert, rack focus, hold two seconds" — not "show product")
- [ ] Asset ID follows the convention

**B · The six laws**
- [ ] **Law 1** — would this hook appeal to someone who has never felt this pain? If yes, rewritten
- [ ] **Law 2** — brand voice commits; testimonial voice hedges. No "helps support" / "naturally declines" in brand voice
- [ ] **Law 3** — no disease name anywhere, in any voice, including OST
- [ ] **Law 4** — no second-person physiology assertion; no "you" in the first five seconds
- [ ] **Law 5** — benefits written as subtraction and as behaviours that stopped
- [ ] **Law 6** — one spine line, one job. No quote montage

**C · Compliance (the 60-second pre-shoot check)**
- [ ] Disease names deleted, not softened
- [ ] cure/treat/prevent/reverse/restore/boost/clinically proven → deleted or substantiated on screen
- [ ] Every number citable on screen; uncitable numbers bracketed `[VERIFY: …]`
- [ ] Every on-camera document genuine
- [ ] FDA disclaimer present
- [ ] Material connection disclosed on creator assets
- [ ] **No competitor bottle in frame** (check zero while G2 is open)
- [ ] No percentage discount in any headline
- [ ] Talent 58–68 (60–72 male)
- [ ] Gates checked; blocked assets marked 🔒 with what unblocks them

**D · Provenance**
- [ ] No RED / CMP / YT / Golden line presented as a Prime testimonial
- [ ] Any needed testimonial marked `[TESTIMONIAL SLOT — needs verified Prime customer + disclosure]`
- [ ] No invented referral, customer, study, COA or review count
- [ ] Verbatim quotes reproduced exactly, typos intact

**E · Production**
- [ ] 9:16 master; QC note for 4:5 and 1:1
- [ ] Per-bottle or per-day anchor, never a percentage
- [ ] Register direction correct for the ICP (flat/irritated · searching · puzzled · reluctant)
- [ ] No before/after on P6. No beauty lighting on P6. Ever
- [ ] Plain beats polished — domestic locations, available light, visible clutter

**If any box fails, fix the script before output. Never ship a failing script with a note attached.**

---

## 5 · Batch output format

When asked for multiple scripts:

1. Open with a **one-table concept grid** — Asset ID · Framework · Pillar · ICP · Awareness · the one-line premise · gate status.
2. Then the full scripts, in **launch order: Proven → Adjacent → Untested.**
3. Close with **"Shoot this one first, and why"** — one paragraph.
4. **Cap untested concepts at 25% of any batch.** A library that is 52% untested is correct as a written library and wrong as a launched one.

---

## 6 · Non-script requests

**Hook batches.** 20 hooks, grouped by pillar, each with the OST and one line on who it disqualifies. No script.

**Ad critique.** Judge on conversions per click only (≥4.0% scale · 3.0–4.0% hold · <2.8% kill). Diagnose with the
promotion decision tree. **Never praise or condemn an ad on hook rate, hold rate or CTR** — say explicitly that
those are diagnostics, not verdicts, and why.

**Angle or concept development.** Name the pillar, the ICP, the awareness rung, the objection it neutralises, the
proof device, and the framework you would build it in. **A concept that cannot name its pillar is not a concept,
it is a variation** — say so and send it back.

**Rewrites of existing copy.** Show the original and the rewrite side by side, and name which law drove each
change. If the original is an Angle F or Angle D construction, say so with the number: 436 ads, zero winners,
nine losers.
