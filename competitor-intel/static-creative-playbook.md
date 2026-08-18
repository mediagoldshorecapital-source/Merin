# Competitor Static Creative Teardown & Replication Playbook

**Source:** `Competitor_meta_ads_library.docx` — a Meta Ad Library export covering
**736 unique live ads** from **9 core longevity/healthy-aging brands** (plus 8 affiliate and
partner pages), captured 18 Aug 2026.
**Scope of this document:** what their static creatives have in common, the frameworks
underneath them, and a concrete system for building our own batch that out-converts them
without copying them.

---

## 0. Method, and two things worth knowing up front

**How the dataset was built.** The export was parsed into one row per ad
(`data/competitor_ads.csv`, 736 rows × 15 fields: advertiser, first-seen date, days running,
static vs video, full primary text, headline, description, CTA, destination domain, page
likes, creative image). Every creative image was extracted (363 unique images), and the
**84 longest-running statics across all 9 brands plus a 12-creative random control sample
were reviewed by eye**, four to a contact sheet. Every number below is reproducible —
`scripts/analyse_creative_patterns.py` regenerates it from the CSV.

**Two caveats that shape how to read this.**

1. **"Days running" is our only performance signal.** The Ad Library publishes no spend,
   impressions or ROAS. But longevity is a strong free proxy: nobody pays to serve a static
   for 100+ days that isn't returning. Treat *long-running = proven winner* and
   *just-launched = untested bet*. Where I compare "proven vs fresh" ads, the sample is
   brand-confounded (Timeline alone supplies most of the 60-day-plus statics), so read those
   as directional, not causal.
2. **The copy-pattern statistics read the ad's text only — they cannot see words baked into
   the image.** That is why "social proof" scores 0% among proven ads even though
   Wonderfeel's 117-day winners *are* testimonial creatives: the testimonial lives in the
   picture, not the caption. Copy-layer numbers come from the parser; image-layer patterns
   (Part 2) come from visual review.

**A note on fit.** The competitor set in this export is the longevity / NAD+ / cellular-aging
category (Timeline, Renue By Science, Omre, NOVOS, Elysium, Tru Niagen, Wonderfeel,
ProHealth, Double Wood). The frameworks in Part 3 apply to any ingredient-led supplement
brand, but the specific angle recommendations in Part 6 assume we are selling into the
healthy-aging space. If our positioning differs, the angles change; the system does not.

---

## 1. The field at a glance

| Advertiser | Live ads | Statics | % static | Median days live | Longest live | 60d+ ads |
|---|---:|---:|---:|---:|---:|---:|
| Timeline (Mitopure) | 196 | 107 | 55% | 26.5 | 116 | 44 |
| Renue By Science | 175 | 21 | 12% | 15.4 | 70 | 30 |
| Omre | 79 | 43 | 54% | 5.3 | 6 | 0 |
| NOVOS | 61 | 59 | 97% | 1.4 | 95 | 6 |
| Elysium Health | 51 | 47 | 92% | 8.5 | 33 | 0 |
| Wonderfeel | 34 | 19 | 56% | 14.4 | 117 | 8 |
| Tru Niagen | 34 | 20 | 59% | 6.8 | 25 | 0 |
| ProHealth Longevity | 23 | 15 | 65% | 127.3 | 165 | 15 |
| Double Wood | 21 | 20 | 95% | 50.3 | 133 | 10 |

**Read:** 51% of all live ads in the category are static. Statics are not the junior format
here — they are half the category's spend surface, and they hold the longest run times
(ProHealth's median static has been live **127 days**).

Three distinct operating models are visible in one table:

- **Volume-and-velocity (Omre, NOVOS, Elysium):** dozens of ads, median life under 10 days.
  They are running a fast test loop and killing losers weekly.
- **Concentrated winners (ProHealth, Double Wood, Wonderfeel):** few ads, extreme run times.
  They found something and are milking it.
- **Industrialised (Timeline):** 196 ads, 70 unique images, 54 unique copies, and 44 ads past
  60 days. They run a testing machine *and* a stable of proven evergreens simultaneously.

---

## 2. What the numbers say

### 2.1 Statics survive — and most of them don't

| Days live | Share of statics |
|---|---:|
| 0–7 days | 37.6% |
| 7–30 days | 29.6% |
| 30–60 days | 16.8% |
| 60–100 days | 8.5% |
| 100 days+ | 7.5% |

**Two-thirds of static creatives die inside a month; 16% become evergreen.** That is the
category's real hit rate, and it should set our expectations: to hold five evergreen statics,
plan to launch roughly thirty.

### 2.2 They are not making 200 ads — they are making 20 and recombining them

| Advertiser | Ads | Unique images | Unique copies | Ads per image | Images per copy |
|---|---:|---:|---:|---:|---:|
| Timeline | 196 | 70 | 54 | 2.80 | 2.43 |
| Renue By Science | 175 | 22 | 119 | **7.95** | 1.77 |
| Omre | 79 | 43 | 11 | 1.84 | **6.00** |
| ProHealth | 23 | 10 | 6 | 2.30 | **7.50** |
| Elysium | 51 | 34 | 14 | 1.50 | 3.31 |
| NOVOS | 61 | 56 | 34 | 1.09 | 1.75 |

This is the single most useful commercial finding in the dataset. **The category treats
image and copy as independently swappable variables.** Renue runs one image against eight
different captions; Omre and ProHealth run one caption against six or seven different images.
Nobody is briefing 196 bespoke ads. They are briefing a *grid*: a small set of layout
templates, a small set of message angles, and a combinatorial engine on top.

### 2.3 Launch cadence is relentless and accelerating

| Month first seen | New ads |
|---|---:|
| 2026-03 | 4 |
| 2026-04 | 41 |
| 2026-05 | 14 |
| 2026-06 | 109 |
| 2026-07 | 188 |
| 2026-08 (18 days) | 378 |

Roughly **21 new ads per day** across nine brands in August. (Partly a snapshot artifact —
dead ads from older months are missing — but the trend inside the live set is real.) Per
brand, that is a **weekly** creative drop, not a quarterly campaign.

### 2.4 What the copy actually does — 375 statics

| Pattern present | Share |
|---|---:|
| Mechanism / molecule named (NAD+, Urolithin A, NMN, creatine…) | **66.1%** |
| Second person ("you / your") | 61.3% |
| Clinical proof language (study, clinically, placebo, peer-reviewed) | **49.1%** |
| Offer / price / urgency | 28.0% |
| Question hook | 25.3% |
| Authority / doctor | 13.3% |
| Social proof / press / rating *(in caption only)* | 13.1% |
| Symptom or pain enumeration | 7.7% |
| Age or decade callout | 6.9% |
| Comparison / category takedown | 6.1% |
| Identity / status framing | 5.6% |

**Copy shape:** median primary text **284 characters** (p25 205, p75 353) — about
three lines before the "See more" fold. Median headline **31 characters**. 49% use two or
more paragraphs; almost none end in an explicit "shop now" sentence — the CTA button carries
it. **SHOP_NOW is 77% of all CTAs**; Omre and Tru Niagen are the exceptions, favouring
LEARN_MORE / SEE_DETAILS because they send to articles and quizzes rather than product pages.

### 2.5 Proven vs fresh (directional)

Comparing statics live 60+ days against those live under 14 days, on the copy layer only:

| Pattern | Proven | Fresh | Index |
|---|---:|---:|---:|
| Clinical proof language | 62% | 34% | **1.84** |
| Mechanism / molecule named | 55% | 63% | 0.87 |
| Offer / price / urgency | 22% | 29% | 0.74 |
| Question hook | 10% | 29% | **0.35** |

The one signal that survives the brand confound: **claims that carry an explicit evidence
citation outlive claims that don't.** Question hooks and discount hooks churn — they are what
brands *test*; proof is what they *keep*.

---

## 3. The static creative formats — the image layer

Eleven layouts account for essentially every static in the review set. For each: who runs it,
what it is, and why it earns its run time.

### F1 — The Study Card
*Timeline, NOVOS, Tru Niagen.* An editorial "science page": a small `NEW STUDY` / `LONGEVITY`
pill badge, an oversized serif or grotesk headline ("Breakthrough Study: Urolithin A & Immune
Health"), a clean scientific image (a split cell render, a mitochondria micrograph), a short
explanatory paragraph, a molecule diagram in the corner. Product is small or absent.
**Why it works:** it doesn't look like an ad, so it gets read instead of scrolled. It sells
the *category* before the product, which is how a new ingredient becomes a purchase.
**Evidence:** Timeline's Study Cards are the 112–116-day evergreens — the longest-running
creatives of any brand in the set.

### F2 — The Clinical Chart Card
*Timeline.* A literal bar chart in the top two-thirds — `+12% MUSCLE STRENGTH` in red against
`−9.8%` placebo in grey — with a plain-language line underneath ("Subscribe to preserve muscle
strength as you age") and an offer bar at the foot. Full study footnote in 8pt.
**Why it works:** it is the highest-status proof format available. A chart implies a trial,
a comparison and a specific number in one glance, and it is nearly impossible for a
me-too competitor to fake. 115–116 days live.

### F3 — The Annotated Product Diagram
*Tru Niagen, ProHealth, Wonderfeel, NOVOS.* Hero product centred, thin leader lines radiating
to 4–6 short labels: "150% NAD+ boost", "40+ human clinical studies", "Triple Lab Tested",
"100-Day Risk-Free Guarantee", "450 mg NMN". **Why it works:** it converts a bottle into a
spec sheet, answers every objection in one impression, and — critically — reads as *technical*
rather than promotional. This is the highest-leverage format for a brand with a genuinely
better formula.

### F4 — The Benefit-Bubble Render
*Timeline, NOVOS, Omre.* Product or pill rendered on flat brand colour with rounded callout
bubbles floating around it ("Increased cellular energy", "Healthy aging support", "Increased
muscle strength*"), plus an endorsement line ("Try the #1 Doctor-Recommended Urolithin A
Supplement"). **Why it works:** three benefits in one frame with no reading effort. Cheap to
produce, easy to re-skin per angle — Timeline runs the same layout with four different
headlines.

### F5 — The Comparison Table
*Tru Niagen, Renue By Science.* Two columns, ours vs theirs, blue ✓ against black ✗ down four
rows ("45+ published peer-reviewed clinical studies", "~161% NAD+ increase", "Most efficient
NAD+ precursor"). Renue's variant is a split-screen: grey "20 different pills / mystery blends
/ feeling worse" against a lit product with "One easy scoop a day / Simple, proven by science /
Results you can feel, guaranteed". **Why it works:** it does the shopper's comparison research
for them inside the feed and frames the category on our terms. Note the risk: it names a rival
ingredient class, which invites a rebuttal ad.

### F6 — The Testimonial Speech-Bubble
*Wonderfeel (their entire evergreen set), ProHealth.* A branded speech bubble with a real
review, key phrase highlighted in yellow, first name + five stars, laid over product
photography. Same layout, swapped quotes, swapped background colours.
**Why it works:** it is a template, not a design — one layout produced Wonderfeel's four
117-day winners. Highlighting the one phrase that carries the benefit ("brain fog has
improved") is what makes it scannable at thumb speed.

### F7 — The Native / UGC Static
*Timeline, Omre, Renue.* A deliberately imperfect iPhone photo — product on a kitchen counter,
a hand holding a pouch — overlaid with an Instagram-story-style text box in the platform's own
UI ("POV: your muscle strength increased by 12%…", "At 43, I'm paying attention to what happens
behind the scenes"). Advanced variants fake a comment reply ("You're shredded! What are you
doing?") or handwrite the claim on a forearm.
**Why it works:** it borrows the visual grammar of organic content, so it clears the
"this is an ad" filter before the message is judged. Cheapest format to produce; highest
volume potential.

### F8 — The Statement Card
*Omre, Renue, Elysium.* No product. Flat colour or dark ground, one big serif line:
*"Some things decline with age. Your standards don't have to."* / *"The slips are small. You
notice every one."* / *"NOT 18 AGAIN. just more like yourself."* Logo, and "Tap here to find
out more."
**Why it works:** pure emotional resonance, zero product friction, ideal for cold prospecting
into an advertorial. It also builds brand distinctiveness faster than any product shot.

### F9 — The Offer / Price-Drop Card
*ProHealth, Timeline, Ancient-style promo.* "Up to 25% LESS — NEW everyday pricing, starting
now", "NOW 25% LOWER PRICING" chips clipped onto the product, "20% OFF EVERY ORDER" bars.
**Why it works:** it converts warm audiences and reactivates lapsed buyers. ProHealth built a
130–165-day evergreen out of a *price event* — because they framed a permanent price cut as
news, not as a sale.

### F10 — The Problem/Solution Split
*ProHealth, Renue.* Left half: a photo of the symptom (a man pinching his brow, "Tired of
Fatigue, Brain Fog, Slower Recovery?"). Right half: cream background, calm product, "The
longevity protocol serious biohackers rely on. Just got a lot more accessible."
**Why it works:** it stages the before/after that supplements can't legally photograph.
130 days live.

### F11 — The Clean Packshot
*Double Wood, Renue.* Product on pure white, label legible, nothing else.
**Why it works:** for a known-ingredient purchase ("magnesium taurate", "bee pollen") the
shopper is already searching — the job is recognition and price, not persuasion. Double Wood
holds 133-day run times on literal catalogue photography. **This only works for commodity
ingredients where we compete on trust and price**, and it is the one format we should
deliberately *not* build our brand on.

**Bonus pattern — the authority borrow.** NOVOS runs a card citing the American Heart
Association's PREVENT tool ("now starts estimating cardiovascular risk at age 30. That should
tell you something."). Wonderfeel runs "Rated #1 by New York Post". Elysium runs "As seen in
TIME". Borrowed institutional credibility is the cheapest proof asset in the category.

**Format specs observed:** 39% of statics are 9:16, 31% are 4:5, 28% are 1:1. Nobody ships
1.91:1. Text is set large enough to read at ~120px wide. FDA disclaimer language appears in
9% of statics — always as small print inside the image, never in the caption.

---

## 4. The frameworks underneath — reverse engineered

The formats are the surface. These seven frameworks are what actually generate them.

### FW1 — The Molecule Ladder
Every leading brand climbs the same four rungs, in order:

> **Molecule** ("Urolithin A", "Niagen® NR", "NMN + Resveratrol")
> → **Mechanism** ("mitochondrial renewal", "NAD+ is the molecule your cells use to make energy")
> → **Decline** ("it starts declining in your 30s — up to 50% by midlife")
> → **Restoration + proof** ("+12% muscle strength vs placebo, 8-week randomised trial")

66% of statics name a molecule; 49% attach study language. **The product is never the hero —
the molecule is.** This is deliberate: you cannot own "a supplement", but you can own an
ingredient story, and once the consumer believes the molecule matters, the brand with the best
proof asset wins the click. Timeline owns Urolithin A. Tru Niagen owns NR. Elysium is
mid-land-grab on "creatine for longevity".

### FW2 — The Proof Stack
Proof is used in a strict hierarchy, and the higher tiers get the longer run times:

| Tier | Asset | Who |
|---|---|---|
| 1 | Own clinical trial with a number and a placebo arm | Timeline (+12%), NOVOS (placebo-controlled), Tru Niagen (~161%) |
| 2 | Published literature count | "45+ published, peer-reviewed clinical studies" |
| 3 | Institutional / press borrow | TIME, New York Post, American Heart Association |
| 4 | Doctor / founder authority | "#1 Doctor-Recommended", "Formulated by a Doctor Who Also Runs a Company" |
| 5 | Third-party testing & certifications | NSF Certified Sport, "Triple Lab Tested", "third-party tested" |
| 6 | Customer reviews & ratings | Wonderfeel's speech bubbles, "1,000+ reviews / 7 million doses sold" |
| 7 | Guarantee / risk reversal | "100-Day Risk-Free", "More Energy or Money Back" |

**The rule they all follow: never make a claim without immediately attaching the highest tier
of proof you own.** Tier 6–7 assets are available to us on day one. Tiers 3–5 are buyable
within a quarter. Tier 1–2 is the moat, and it is why Timeline can run one chart for four
months.

### FW3 — The Modular Grid (the production framework)
The reason nine brands can ship ~21 ads a day is that no ad is designed from scratch. The
underlying object is:

> **Layout template (F1–F11) × Message angle × Awareness level × Offer state × Format ratio**

Change one variable, ship a new ad. Timeline's 70 images across 54 copies at 2.4 images per
copy is exactly this grid running. **Copying their pictures is worthless; copying this grid is
the whole prize.** Part 6 turns it into our build sheet.

### FW4 — Hook-to-Destination Matching
The destination is chosen to match how cold the hook is, and the CTA follows:

- **Cold, emotional hook (F8 statement card)** → advertorial or listicle on a subdomain
  (`ceo.omre.co`, "The 7 reasons you start losing your edge in your 50s", "Built with
  Heyflow" quiz) → CTA `LEARN_MORE` / `SEE_DETAILS`.
- **Warm, proof-led hook (F1–F3)** → main site collection or PDP → CTA `SHOP_NOW`.
- **Hot, offer-led hook (F9)** → PDP with the discount pre-applied → `SHOP_NOW`.

Omre runs the purest version: 43 statics, 11 captions, six images per caption, all pointing at
one long-form article funnel, with the ad's job being *the click into the story*, not the sale.
Only 55 of 736 ads (7.5%) go to a dedicated advertorial subdomain — **this is the least
crowded, highest-leverage funnel in the category.**

### FW5 — Category Reframe
The best-performing headlines don't argue that the product is better; they redefine what
category the product is in.

- "Creatine for **longevity**, strength, and cognition" — Elysium moves creatine out of the gym.
- "**Muscle is a longevity strategy**" — reframes exercise nutrition as anti-aging.
- "**Drink your skincare**" / "The future of skin support is **inside-out**" — NOVOS and Renue
  move a supplement into the skincare budget, where the willingness to pay is far higher.
- "Why target 1 when you can hit all 12?" — NOVOS reframes single-ingredient rivals as
  *incomplete* rather than *worse*.
- "Your Shelf Is Full. Your Skin Is Confused." — Renue reframes the competitor set as clutter.

A reframe is defensible in a way a claim isn't: rivals can copy your number, but copying your
frame promotes you.

### FW6 — Design as Proof
Look at Timeline, NOVOS and Elysium next to Double Wood. The premium brands use restrained
palettes, generous white space, editorial serif/grotesk pairings, scientific imagery and
consistent brand furniture — because **in a category selling credibility, the art direction is
part of the claim.** Cluttered, high-contrast, arrow-and-starburst design (the affiliate pages
in the set: "LAST CHANCE", "70% OFF", cartoon mascots) signals a different, cheaper promise
and attracts a worse customer. Our design system is a proof asset; treat it as one.

### FW7 — Offer Architecture
Three layers, used consistently:

1. **Standing offer:** subscription discount, always on, baked into creative as a chip or
   footer bar ("20% OFF when you subscribe", "Subscribe & save 35%", "$79/month"). Present in
   28% of statics — it is a permanent design element, not a campaign.
2. **Event offer:** a *reason* for a price change, framed as news ("Up to 25% LESS — NEW
   everyday pricing, effective immediately", "NMN Price Cut. Effective Immediately"). This is
   what makes ProHealth's discount creative run 130+ days instead of two weeks.
3. **Risk reversal:** guarantee as its own creative ("More Energy or Money Back", "100-Day
   Risk-Free"), used to close the objection the proof couldn't.

### FW8 — Awareness Laddering
Mapped onto Schwartz's five awareness levels, the category's hooks sort cleanly — and reveal
where the gaps are:

| Awareness | Their hook | Format | Coverage |
|---|---|---|---|
| Unaware | "Some things decline with age. Your standards don't have to." | F8 | thin — mostly Omre |
| Problem-aware | "Tired of fatigue, brain fog, slower recovery?" | F10, F7 | **7.7% only — the biggest gap** |
| Solution-aware | "NAD+ declines up to 50% by midlife. Here's the science." | F1, F2 | crowded |
| Product-aware | "Niagen NR vs NMN" comparison table | F5, F3 | crowded |
| Most-aware | "25% lower pricing", "Subscribe & save" | F9 | crowded |

**Under 8% of statics open on a felt symptom.** The category is talking about molecules to an
audience that experiences *tiredness*. That asymmetry is our opening.

---

## 5. The hook library

Extracted from the winners, with the variable slots exposed. These are structures, not lines
to copy — fill them with our own proof and voice.

**Mechanism-reveal**
- "[SYMPTOM] isn't [OBVIOUS CAUSE]. It's [MECHANISM] at work."
- "[MOLECULE] is the molecule your cells use to [FUNCTION]. It starts declining in your [DECADE] — up to [N]% by midlife."
- "A [TOPICAL/SURFACE] product works on the leaves. This works on the soil."

**Proof-led**
- "[BENEFIT] with proof: [N]% vs placebo in a [DURATION] randomised trial."
- "[N]+ published, peer-reviewed studies. [RIVAL INGREDIENT]: none."
- "New study: [MOLECULE] & [BODY SYSTEM] — a breakthrough discovery."
- "The #1 [PROFESSIONAL]-recommended [INGREDIENT] supplement."

**Problem-aware (our gap — over-index here)**
- "The name that takes longer to come back. Reading the same paragraph twice."
- "Stop calling [NORMALISED SYMPTOM] normal."
- "Can you tell the difference between running at 100% and running at 80%?"
- "It's not [WILLPOWER/AGE]. It's [MECHANISM]."

**Reframe**
- "[COMMODITY PRODUCT], finally built for [HIGHER-ORDER GOAL]."
- "Why target 1 when you can hit all [N]?"
- "The future of [CATEGORY] is inside-out."
- "[X] is a longevity strategy."

**Identity**
- "For [IDENTITY] who care about [VALUE] past [AGE]."
- "Not 18 again. Just more like yourself."
- "Some things decline with age. Your standards don't have to."

**Objection / risk reversal**
- "[BENEFIT] or your money back. [No questions asked]."
- "Try [PRODUCT] tonight. Pay nothing if it doesn't work."
- "No proprietary blends. Full dose transparency."

**Offer-as-news**
- "[PRODUCT] price cut. Effective immediately."
- "Up to [N]% less — new everyday pricing, starting now."

---

## 6. Our build: from teardown to a converting batch

### 6.1 The differentiation doctrine
Copying their creative loses on arrival: their ads are optimised for *their* proof assets, and
a lookalike with weaker proof reads as the cheap version. The rule is **same framework,
different substance**:

| Steal (the framework) | Never copy (the substance) | Our substitution |
|---|---|---|
| The Study Card layout | Their study, their molecule | Our own trial, our sourcing story, or a published-literature synthesis we commission |
| The Proof Stack hierarchy | Their tier-1 assets | Start at tiers 5–7 (third-party testing, reviews, guarantee) and buy up the ladder |
| The Comparison Table | Their "NR vs NMN" fight | Compare on an axis we win: dose transparency, cost per clinical dose, form factor, adherence |
| The Modular Grid | Their layouts pixel-for-pixel | Our own template kit in our brand system |
| The advertorial funnel | Their article | Our own long-form piece with a named expert |
| Category Reframe | Their frame | An **unclaimed** frame — see 6.2 |

### 6.2 Three positioning wedges the data leaves open

1. **The problem-aware wedge.** Under 8% of category statics open on a felt symptom, and none
   of the proven ones do. A full creative line built on lived symptoms — the 3pm crash, the
   name that won't come back, stiff mornings, needing two coffees — has almost no competition
   at the top of funnel and feeds directly into the advertorial funnel (FW4) that only 7.5% of
   the category uses.
2. **The adherence wedge.** Every brand sells *what's in the bottle*; nobody sells *whether you
   actually take it*. "No missed days" appears once, in a Timeline headline, and is never
   built out. Format, taste, ritual and a 90-day consistency story are wide open — and they're
   the honest driver of results, which makes the claim both differentiated and defensible.
3. **The cost-per-clinical-dose wedge.** The category advertises discounts but never unit
   economics. A transparent "what a clinically-studied dose actually costs you per day" card —
   the F5 comparison table run on price-per-dose rather than ingredient — is a proof asset we
   can build this month with no lab required.

Pick **one** as the brand frame; the other two become creative angles.

### 6.3 The creative matrix — a 60-ad first batch

Build the grid, not the ads. Five variables:

- **Layout templates (6):** Study Card (F1) · Annotated Product Diagram (F3) · Testimonial
  Bubble (F6) · Native/UGC (F7) · Statement Card (F8) · Comparison Table (F5)
- **Angles (5):** symptom/problem-aware · mechanism · proof/clinical · reframe · risk-reversal
- **Awareness (3):** cold (statement + native) · warm (study + diagram) · hot (comparison + offer)
- **Offer state (2):** standing subscription offer on/off
- **Ratio (2):** 4:5 and 9:16 (drop 1:1 unless placements demand it)

**Wave 1 (weeks 1–2): 6 templates × 5 angles = 30 concepts**, each exported 4:5 and 9:16 = 60
assets. Over-weight the problem-aware angle: 12 of the 30 concepts, since that's our wedge.
**Wave 2 (weeks 3–4):** kill everything under the category's 7-day survival bar, then produce
6 variations of each survivor — new headline, new background, new proof chip — using the
image-per-copy trick (FW3). **Wave 3 (weeks 5–8):** promote anything past 21 days into an
evergreen set and rebuild the batch around what won.

Naming convention so the data is analysable later — this is what makes measurement possible:

```
MERIN_<template>_<angle>_<awareness>_<offer>_<ratio>_v<n>
e.g. MERIN_F1study_mechanism_warm_sub20_4x5_v2
```

### 6.4 Production standards (from what the winners do)
- One idea per creative. If the headline needs a second sentence to land, it's an advertorial, not an ad.
- Headline ≤ 8 words, set to be legible at 120px wide. Caption ≤ 280 characters before the fold.
- Every claim carries its proof in the same frame (chip, footnote, badge, or chart).
- Structure-function claims only, with the FDA disclaimer as small print *in the image* — the
  category standard. No disease claims, no before/after body photography, no implied medical outcomes.
- Brand furniture in a fixed position (logo, offer bar) so the system reads as one family.
- Every static gets a matching 9:16 crop with the text inside the safe zone.

### 6.5 Testing protocol
- Hold the audience constant; broad targeting, creative as the only variable.
- Minimum 3–5 days and ~50 link clicks per creative before judging; kill on CTR + cost per
  add-to-cart, not on impressions.
- Test **one variable at a time** within a template family (headline, then image, then offer).
- Promote to evergreen at 21 days; refresh the top performer's *frame* before it fatigues
  rather than replacing the winner outright.
- Ship a new batch every week. The category's median brand launches one; matching that cadence
  is table stakes.

---

## 7. Turning their data into our statistics

The pipeline in `scripts/` is repeatable. Run it monthly against a fresh export and we get a
competitive intelligence loop, not a one-off report:

```bash
# 1. parse a new Ad Library export into structured rows + extract every creative
python scripts/parse_ad_library_export.py export.docx data/competitor_ads.csv \
       --media-dir data/creatives --json data/competitor_ads.json

# 2. regenerate every statistic in this document
python scripts/analyse_creative_patterns.py data/competitor_ads.csv > data/summary_stats.txt

# 3. build contact sheets of each brand's longest-running statics for visual review
python scripts/build_contact_sheets.py data/competitor_ads.json data/creatives sheets/
```

**The five metrics to track month over month:**

1. **Evergreen count per competitor** (ads past 60 days) — who found something that works.
2. **New-ad velocity** (launches per week) — who is scaling and who is coasting.
3. **Format mix drift** (static vs video, and which of F1–F11 is gaining) — where the category
   is moving before it arrives.
4. **Angle share** (the copy-pattern table) — which claims are getting crowded, so we can
   vacate them.
5. **New evergreens** — any creative that crosses 30 days is a signal worth reverse-engineering
   the week it happens.

**Join it to our own numbers.** The competitor set gives us the outside view; our Meta ad
account and Triple Whale give us the inside view. The same tagging taxonomy (6.3) applied to
our creatives lets us answer the only question that matters: *which template × angle
combination produces our lowest CAC*, and then push spend there while the category is still
arguing about molecules.

**What this dataset does not contain** — worth closing before the next round: no spend or
impression data (buy a Foreplay/AdSpyder tier if we want it), no landing pages behind the
ads (worth manually capturing the top 10 funnels, especially Omre's advertorial), a snapshot
skewed to August (dead ads from earlier months are invisible), and no read on video, which is
half the category's volume and where Renue By Science puts 88% of its ads.

---

## Files

| File | What it is |
|---|---|
| `data/competitor_ads.csv` | 736 unique ads × 15 fields — the whole dataset |
| `data/summary_stats.txt` | Every statistic in this report, machine-generated |
| `scripts/parse_ad_library_export.py` | Ad Library `.docx` → structured CSV/JSON + creative images |
| `scripts/analyse_creative_patterns.py` | The statistics engine |
| `scripts/build_contact_sheets.py` | Labelled contact sheets for visual review |
