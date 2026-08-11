# 08 — Launch & Testing SOP: Exactly What to Click

---

## Part A — The account structure

Modern Meta delivery works best **consolidated**. Fragmenting into many small ad sets starves each one of data and prevents the algorithm from finding your buyer. Three campaigns is enough to run a $50K/month account.

```
CAMPAIGN 1 — PROSPECTING (CBO)                        ← 70–80% of budget
  Objective: Sales · Conversion event: Purchase
  Budget: Campaign-level (Advantage Campaign Budget), daily
  ├─ Ad Set: BROAD-FEMALE      US · Women 48–68 · Advantage+ audience OFF
  ├─ Ad Set: BROAD-MALE        US · Men 58–72   (Robert · ROAS 1.81)
  └─ Ad Set: TESTING           US · Women 48–68 · new creatives only
                               minimum spend limit = 1× AOV/day

CAMPAIGN 2 — RETARGETING (ABO)                        ← 15–20% of budget
  ├─ Ad Set: WARM-30D    site visitors 30d + IG/FB engagers 30d, minus purchasers 180d
  └─ Ad Set: ATC-14D     add-to-cart / initiate-checkout 14d, minus purchasers 180d

CAMPAIGN 3 — ADVANTAGE+ SHOPPING (ASC)                ← optional, 10–20%
  Single campaign, your proven winners only
  Existing-customer budget cap: 10–15%
```

### Exclusions (set once, everywhere)

- **Purchasers, last 180 days** — excluded from all prospecting. Her reorder window is 90–120 days; you don't want to pay to reach someone who already has six bottles in the cupboard. Handle reorders with email/SMS (cheaper) and a *separate* Day-75 retargeting ad set (see `10-iteration-and-scaling.md`).
- No interest stacking in prospecting. **The creative is the targeting** (Law 1). Interest targeting in 2026 mostly just makes the auction more expensive.

### Placements

Start with **Advantage+ Placements ON.** Facebook and Instagram already drive 94% of orders and the system will find that on its own. Exclude Audience Network only if you see it eating budget with no purchases after 14 days of data.

Upload **9:16 for Reels/Stories and 4:5 for Feed** as separate placement assets in the same ad — don't let Meta auto-crop.

---

## Part B — Naming (do this or you cannot measure)

**Campaign:** `PROSPECTING_CBO_2608`
**Ad set:** `BROAD-FEMALE_48-68_US` · `TESTING_48-68_US` · `BROAD-MALE_58-72_US`
**Ad:** the full creative name from `03-creative-matrix.md` —
`2608_ToF_LIN_3PMCRASH_UGC_H02_9x16_v1`

Use **UTM parameters** on every ad so Shopify and Triple Whale can see it:

```
utm_source=facebook
utm_medium=paid
utm_campaign={{campaign.name}}
utm_content={{ad.name}}
utm_term={{adset.name}}
```

Meta's dynamic parameters fill these automatically. Set them once in the ad-level URL parameters field and every ad inherits the pattern.

---

## Part C — The testing protocol

### The two rules that matter most

> **Rule 1 — Forced daily spend.** Every new creative ad set gets a **minimum spend limit equal to 1× AOV (~$55–60/day).** Without this, Meta will quietly spend $4 on your new creative, decide it doesn't like it, and you'll have learned nothing while thinking you ran a test.
>
> **Rule 2 — Seven full days.** Do not judge, pause, or "optimise" before day 7. At $56 AOV and a ~$30 target CPA, you need roughly 15–20 purchases for a read you can trust. That takes a week.

**Cost of a clean test:** ~$55/day × 7 days = **~$385 per creative.**
**Budget planning:** testing 4 new creatives per month = ~$1,540/month in test budget. Add that to your plan before you start, not after.

### How to launch a batch

1. **Thursday morning.** Never Monday (her lowest order day, −22% vs Saturday). Thursday–Saturday are her strongest days, so a new creative gets its best possible first impression.
2. Add 3–5 new ads into the **TESTING** ad set.
3. Set the ad set minimum spend limit to $55–60/day.
4. Turn everything on and **walk away until the following Thursday.**
5. Do not edit an active ad set. Any meaningful edit resets learning and wastes the spend so far.

### What "walk away" means

No budget changes. No pausing the underperformer on day 3. No adding a new ad mid-flight. No turning it off overnight because the ROAS looked bad on Friday morning.

The number one reason beginner accounts fail is **premature intervention.** You are not helping. You are resetting the learning phase and paying for the privilege.

---

## Part D — Dayparting: the honest version

The source documents recommend scheduling delivery for 10:30–11:30 AM and 6:30–8:00 PM EST. The data behind that is solid — 11 AM peaks at 299 orders/hour and 7 PM at 293/hour. **But there's a platform constraint the documents don't mention, and if you don't know it you'll waste a week trying to find a setting that isn't there:**

> **Meta's ad scheduling ("Run ads on a schedule") is only available on ad sets using a lifetime budget.** You cannot daypart a daily-budget CBO campaign. Full stop.

So you have three real options:

| Option | How | When to use |
|---|---|---|
| **1 — Don't daypart (recommended to start)** | Run daily budgets. Let the algorithm find the hours — it already knows they convert, and it will bid into them automatically. | Under ~$300/day spend, or fewer than 50 purchases/week. Restricting hours on small budgets starves the learning phase and usually costs more than it saves. |
| **2 — Lifetime-budget dayparting** | Duplicate your best ad set → switch to lifetime budget → Schedule → set 9 AM–1 PM and 5 PM–10 PM EST. Run it *alongside* the always-on ad set and compare. | Once you're spending $300+/day with stable performance and want to test hour concentration properly. |
| **3 — Message-time matching (do this regardless)** | Don't restrict delivery; instead match the *message* to the moment. Run afternoon-crash creatives heavily so they're in rotation during 2–5 PM, and evening-scroll UGC for the 7 PM session. | Always. It's free and it captures most of the upside. |

**Verify before assuming:** her order times are Eastern. If your ad account timezone isn't EST, every schedule you set will be shifted. Check Ads Manager → Account Settings → time zone before touching a schedule.

**The genuinely free win in this data isn't hourly — it's weekly.** Saturday is her best day (742 orders); Monday her worst (575, −22%). You cannot easily daypart by hour on a daily budget, but you *can* control which day you launch. Launch Thursday. Refresh creatives Thursday. Never launch Monday.

---

## Part E — Budget and scaling rules

### Starting budget

| Account stage | Daily budget | Split |
|---|---|---|
| Cold start (no winners yet) | $150–200 | $60 testing / $90–140 broad prospecting |
| 1–2 proven winners | $300–500 | $60 testing / $180–330 broad / $60–110 retargeting |
| 3+ proven winners | $800–1,500 | $120 testing / rest across broad + ASC + retargeting |

Testing budget should be **15–25% of total spend, permanently.** The day you stop testing is the day the account starts dying, because every creative has a fatigue curve and you need the next winner ready before the current one decays.

### Scaling a winner

**Vertical (increase budget on the existing campaign):**
- Raise campaign budget by **no more than 20–30% every 3 days**.
- Larger jumps re-enter the learning phase and performance drops for 3–5 days.
- If CPA holds after 3 days, raise again. If it degrades more than 20%, step back down to the last stable level and hold for a week.

**Horizontal (add more surface area) — usually the better move:**
- Duplicate the winner into a new ad set with a different avatar (Linda winner → Robert version)
- New ratio (9:16 winner → 4:5 version)
- New hook on the same body (see `10-iteration-and-scaling.md`)
- Add it to an Advantage+ Shopping campaign

Horizontal scaling has a much lower risk of destabilising a working campaign.

### When to stop scaling

Stop and hold when any of these appear:
- Frequency in a 7-day window exceeds **~2.5**
- CPA rises **more than 30%** above target for 3 consecutive days
- Hook rate on the top creative drops **25% below its peak** (fatigue — go make new creative)

---

## Part F — Launch-day checklist

Before you press publish:

**Tracking**
- [ ] Meta Pixel firing, verified in Events Manager Test Events
- [ ] **Conversions API live** (server-side). Without it you're losing 20–40% of attributed conversions on iOS — and this buyer is overwhelmingly an iPhone user.
- [ ] Purchase event passing `value` and `currency`
- [ ] Domain verified; Purchase prioritised #1 in Aggregated Event Measurement
- [ ] UTMs on every ad
- [ ] Shopify / Triple Whale connected and reconciling with Meta

**Campaign**
- [ ] Objective = Sales, conversion event = Purchase (never Add to Cart unless you're under 50 purchases/week)
- [ ] 180-day purchaser exclusion applied to all prospecting ad sets
- [ ] Ad set minimum spend limit set on TESTING
- [ ] Advantage+ Placements on
- [ ] Account timezone confirmed

**Creative**
- [ ] Both 9:16 and 4:5 uploaded per ad
- [ ] Primary text, headline, and description written (see below)
- [ ] Destination URL correct, with the right bundle pre-selected if possible
- [ ] Every ad passed the QA gate in `07-production-sop.md`
- [ ] Ad names follow the convention

**Post-launch, within 1 hour**
- [ ] All ads show "Active," not "In Review" or "Rejected"
- [ ] Test-click every ad's link on a phone
- [ ] Landing page loads in under 3 seconds on mobile
- [ ] Apple Pay is visible at checkout

---

## Part G — Ad copy (the text around the creative)

Her behaviour: she taps, reads the landing page for 4 minutes, checks Forbes, reads two reviews, picks B3G3, pays with Apple Pay. The ad copy's job is to **get her to tap and to pre-load the trust**, not to sell the whole thing.

### Primary text template (short — default)

```
Waking up tired after eight hours isn't a sleep problem.

After 50, cellular NAD+ levels drop significantly — which is why more
sleep and more coffee stopped working.

1000mg pure NMN Complex. Third-party lab tested. 5,000+ reviews.
Most people notice a difference around week three.

Buy 3 Get 3 Free — $16.66 a bottle, and 90 days to change your mind.
```

### Primary text template (long — for MoF/BoF, she reads)

```
Three months ago I was planning my whole day around 3 PM.

Nothing after two o'clock. No errands, no phone calls, because by
three I was finished.

I thought that was just what 62 looked like.

Here's what I found out: after 50, your cells lose the ability to
produce energy the way they used to. The molecule that runs that
process — NAD+ — drops off sharply. It isn't your mattress and it
isn't your willpower.

I'd been burned by supplements before, so I checked the certificate
of analysis before I ordered. 1000mg, third-party verified.

Weeks one and two, nothing. Week three, the afternoons came back.

It didn't fix my sleep and it didn't change my weight — I want to be
honest about that.

Buy 3 Get 3 Free works out at $16.66 a bottle, about 55 cents a day,
with a 90-day money-back guarantee.
```

### Headline (max 40 characters)
- `1000mg NMN — $16.66/Bottle`
- `Buy 3 Get 3 Free · 90-Day Guarantee`
- `Third-Party Tested 1000mg NMN`
- `6 Months. Under $100.`

### Description (max 30 characters)
- `Free shipping · 90-day returns`
- `5,000+ verified reviews`

### Copy rules
- **First line must survive truncation.** Facebook cuts at roughly 125 characters on mobile. Your best sentence goes first.
- **No emoji spam.** Reads as scam to a burned 62-year-old buyer. One at most, or none.
- **No ALL CAPS shouting** in body copy.
- **Never write "click here"** — write what happens next: "Tap to see the lab results."
- Always include: bundle name + per-bottle price + guarantee.
