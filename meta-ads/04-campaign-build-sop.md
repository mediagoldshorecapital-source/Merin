# 04 — Campaign Build SOP

Click-by-click. Do not improvise. Where a toggle isn't mentioned, leave it at its default.

**Before you start:** file 01 gates all green, file 02 worksheet complete, ≥ 9 approved
assets uploaded to your Media Library.

Meta renames UI controls between releases. Where a label may have shifted, the *function*
is described so you can find its current equivalent.

---

## Step 1 — Create the campaign

`Ads Manager → Campaigns → + Create`

| Field | Setting |
|-------|---------|
| Buying type | Auction |
| Objective | **Sales** |
| Campaign name | `PI \| CORE \| CBO \| Sales` |
| Special Ad Categories | **None** — supplements are not a special category. ⚠️ Ticking one here strips your age and location targeting |
| Campaign details | Manual sales campaign (not Advantage+ Shopping) |
| A/B test | **Off** |
| **Advantage campaign budget** | **ON** ← this is CBO. Non-negotiable |
| Campaign budget | **Daily budget**, set per your tier (file 00 §3.2) |
| Campaign bid strategy | **Highest volume** (no cost cap at launch) |

> **Why "Highest volume" and not "Cost per result goal":** a cost cap on a fresh campaign
> suppresses delivery and prevents the model from finding your buyer. Add a cost cap only
> at T3+, and only when CPA has been stable for a month.

> **Why manual, not Advantage+ Shopping:** Advantage+ Shopping (ASC) is a legitimate
> alternative structure, but it removes the ad-set-level control and forced spending limits
> that this entire system depends on. Run this structure first. Revisit ASC at T4 as a
> parallel campaign, never as a replacement.

---

## Step 2 — Ad Set 1: CONTROL

`New Ad Set → name it: CONTROL`

### Conversion
| Field | Setting |
|-------|---------|
| Conversion location | **Website** |
| Performance goal | **Maximise number of conversions** |
| Pixel | Your Prime Ingredients pixel |
| Conversion event | **Purchase** |
| Cost per result goal | *(leave blank)* |

### Budget & schedule
| Field | Setting |
|-------|---------|
| Ad set spending limits | **None on CONTROL.** Let Meta allocate freely |
| Schedule | Start date = your launch date. **No end date** |
| Ad scheduling | Not available (daily budget). See file 00, Conflict D |

### Audience
| Field | Setting |
|-------|---------|
| Location | **United States** — *People living in this location* (not "recently in") |
| Age | **48–65** |
| Gender | **Women** |
| Detailed targeting | **EMPTY.** Add nothing |
| Advantage+ audience | **ON** (treats your inputs as a suggestion and expands) |
| **Exclude** | `EXCL_Purchasers_180d` **and** `EXCL_Purchasers_180d_CRM` |
| Languages | English (All) |

> **The empty detailed-targeting box will feel wrong.** It is correct. Andromeda does not
> use your interest labels; adding them shrinks the auction pool you can win from and gives
> the retrieval layer less room to find Linda. The creative is the targeting.

### Placements
| Field | Setting |
|-------|---------|
| Placements | **Advantage+ placements (all)** |
| Manual exclusions | **None** |
| Brand safety | Standard inventory filter |

> Do not exclude Audience Network or Reels "to protect quality". Rings 4–5 statics find warm
> users across placement types you would never pick manually — that's precisely the funnel
> synergy this structure is built on.

### Optimization
| Field | Setting |
|-------|---------|
| Attribution setting | **7-day click, 1-day view** |
| Advantage+ creative enhancements | **OFF** at ad level (see Step 5) |

---

## Step 3 — Ad Set 2: TEST-A

Duplicate CONTROL (`⋯ → Duplicate`), then change exactly two things:

1. **Name** → `TESTA_{ANGLE}_{FORMAT}` — e.g. `TESTA_3PMCRASH_UGC`
2. **Ad set spending limits** → **Daily minimum = `$58`** (1× AOV)

Everything else stays byte-identical to CONTROL. **Targeting must not differ.** These are
concept containers, not audience tests.

> **Where to find the spending limit:** Ad set level → Budget & schedule → *Ad set spending
> limits* → *Daily minimum*. This control only appears when the campaign has Advantage
> campaign budget ON. If you can't see it, CBO isn't enabled.

### What the forced minimum actually does
Without it, CBO looks at a brand-new ad set with zero conversion history, judges it unlikely
to convert, and gives it $4/day. It never gets enough data to prove itself, so it never
gets budget — a self-fulfilling failure. The minimum breaks that loop by *compelling* Meta
to buy enough data to form a real opinion.

**This is the single most important mechanical setting in the account.**

---

## Step 4 — Ad Set 3: TEST-B

Duplicate TEST-A. Change the name to `TESTB_{ANGLE}_{FORMAT}`. Keep the `$58` minimum.

> **Tier 1 accounts ($100–174/day): skip this step.** Two forced minimums of $58 = $116/day,
> which leaves CONTROL starved. Run CONTROL + TEST-A only until you are above $175/day.

**Budget sanity check before you continue:**

```
Campaign daily budget            $______
− TEST-A forced minimum          $   58
− TEST-B forced minimum          $   58
= Available to CONTROL           $______   ← must be ≥ $58, ideally ≥ $100
```

If CONTROL's remainder is under $58, you have too many test slots open for your budget.
Close one.

---

## Step 5 — Build the ads

### 5a. CONTROL ads — Rings 1–5, as five separate standard ads

CONTROL holds your proven winners as **individual ads**, not as a Flexible Ad. You want
clean per-Ring attribution here so the Monday Review can identify which Ring is failing.

For each of the five launch assets (starred cells in file 03 §3):

| Field | Setting |
|-------|---------|
| Ad name | Per convention: `R1_3PMCRASH_UGC_LINDA62_KITCHEN_v1` |
| Identity | Prime Ingredients FB Page + IG account |
| Ad setup | **Manual upload** (single creative) |
| Format | Single image or video |
| Media | The asset. Upload a **4:5** master and let Meta auto-crop for 9:16 placements |
| Primary text | One only |
| Headline | One only |
| Description | Optional |
| Destination | **Website** → the angle-matched landing page (file 09) |
| Call to action | **Shop Now** (Rings 4–5) / **Learn More** (Rings 1–3) |
| URL parameters | The UTM block from file 01 §8 |
| Advantage+ creative enhancements | **OFF** — text/music/crop enhancements alter your asset and muddy the Entity-ID diversification you engineered |

> **Rings 1–3 → "Learn More" → advertorial page. Rings 4–5 → "Shop Now" → product page.**
> A cold viewer sent straight to a checkout page converts at a fraction of the rate of one
> sent to a page that finishes the argument the ad started.

### 5b. TEST-A ad — one 3:2:2 Flexible Ad

| Field | Setting |
|-------|---------|
| Ad name | `R{n}_{ANGLE}_{FORMAT}_FLEX322_v1` |
| Ad setup | **Flexible ad** |
| Media | **3 creatives, same media type**, same Ring, same Angle, 3 environments |
| Primary text | **2 options** — one rational, one emotional |
| Headline | **2 options** — one benefit, one authority |
| Destination | Angle-matched landing page |
| CTA | Matches the Ring |
| URL parameters | Same UTM block |
| Advantage+ creative enhancements | **OFF** |

### 5c. TEST-B ad
Same pattern, testing a **different variable** — a different Ring, or the same Ring in a
completely different format. Not a near-copy of TEST-A.

---

## Step 6 — Pre-publish verification

Do not click Publish until every line is ticked.

**Campaign**
- [ ] Advantage campaign budget ON
- [ ] Daily budget correct for tier
- [ ] Objective = Sales, bid strategy = Highest volume
- [ ] Special Ad Category = None

**Every ad set**
- [ ] Conversion event = **Purchase** (not ViewContent, not ATC)
- [ ] US · Women · 48–65
- [ ] Detailed targeting **empty**
- [ ] Advantage+ audience ON
- [ ] **Both 180-day purchaser exclusions applied** ← check all three ad sets individually
- [ ] Advantage+ placements ON, no manual exclusions
- [ ] Attribution = 7-day click / 1-day view
- [ ] TEST-A / TEST-B have a **$58 daily minimum**; CONTROL has none

**Every ad**
- [ ] Named per convention
- [ ] Correct Page + IG identity
- [ ] UTM parameters present
- [ ] Destination URL loads, is angle-matched, and **keeps its query string**
- [ ] Advantage+ creative enhancements OFF
- [ ] Passed the creative QA list (file 03 §10)

**Cross-checks**
- [ ] No two live assets would fail the 3-second test against each other
- [ ] The 5 Rings are all filled in CONTROL
- [ ] Budget math from Step 4 leaves CONTROL ≥ $58

---

## Step 7 — Publish

- Publish **Thursday, Friday, or Saturday**. Never Monday — it's Linda's lowest converting
  day, and a Monday launch spends its first 24 hours learning from her worst behaviour.
- Publish in the **morning ET** so the first full day has complete delivery hours.
- Expect review to take 15 minutes to 24 hours. Supplements get extra scrutiny.
- If an ad is rejected: **request review once**, and simultaneously prepare a softer-claim
  variant. Do not repeatedly resubmit the same asset — repeated rejections are an account-
  level risk signal.

---

## Step 8 — Immediately after publishing

- [ ] Confirm all three ad sets show **Active** (not "In review", not "Learning limited"
      yet — that appears later and is expected)
- [ ] Within 2 hours: confirm impressions are being served on each ad set
- [ ] Within 4 hours: click one live ad yourself, complete the journey to checkout **without
      purchasing**, then confirm `ViewContent`, `AddToCart`, and `InitiateCheckout` fire in
      Events Manager Test Events with your UTMs intact
- [ ] Record launch date, budget, and the five live Ring assets in the tracker
- [ ] Set a calendar block for **launch + 4 days** = first read. Nothing before then

### 🔒 The 72-hour freeze

For the next three days you may look. You may not touch.

**Permitted:** checking delivery is active, checking spend is pacing, checking the pixel fires.

**Forbidden:** budget changes, pausing anything, adding creative, editing copy, editing
targeting, "just one small tweak".

Any significant edit resets the learning phase and throws away the data you just paid for.
The account's performance on day 2 tells you nothing about the account's performance.

---

**Next:** [`05-launch-sop.md`](05-launch-sop.md) — the printable launch-day checklist and the first 14 days.
