# 01 — Foundations SOP (Phase 0)

**Time required:** 4–8 hours of work, plus up to 48h of waiting on DNS and data backfill.
**Do not launch until every gate in §9 passes.**

Signal quality is not admin work. Blue Sense's mechanism is explicit: your auction value is
`Bid × Estimated Action Rate + Ad Quality`. Estimated Action Rate is Meta's *confidence*
that a user converts. Bad tracking means low confidence means you lose auctions you should
have won and pay higher CPMs for the ones you win. **Poor EMQ is a permanent tax on every
dollar you will ever spend in this account.**

---

## 1. Business Manager & asset hygiene

**Path:** `business.facebook.com` → Business Settings

- [ ] Business Manager exists and is verified (Business Info → Verification). Unverified BMs
      hit lower spend caps and slower reviews.
- [ ] Ad Account created, currency **USD**, timezone **America/New_York** (matches the EST
      reporting used throughout this SOP — a mismatch silently shifts every 7-day window)
- [ ] Facebook Page and Instagram account both connected to the BM (not just to a personal profile)
- [ ] Payment method added **plus a backup card**. A declined card mid-flight pauses delivery
      and resets learning — the single most avoidable disaster in this document
- [ ] People → your account has **Full control** of the ad account, Page, Pixel, and Catalog
- [ ] Two-factor authentication enforced on all admins

> **Timezone warning:** the ad account timezone is set once and **can never be changed**.
> Get it right now.

---

## 2. Domain verification

**Path:** Business Settings → Brand Safety → **Domains**

- [ ] Add your primary domain (the root, e.g. `primeingredients.com` — not `www.`)
- [ ] Verify by **DNS TXT record** (most durable) or meta-tag
- [ ] Wait for the green "Verified" state — can take up to 72h for DNS propagation

**Why it matters:** without domain verification you cannot configure Aggregated Event
Measurement, which means iOS conversion attribution degrades badly for a demographic that
skews heavily toward iPhone and iPad.

---

## 3. Pixel + Conversions API

**Path:** Events Manager → Data Sources → your Pixel

### 3.1 Browser pixel
- [ ] Pixel installed site-wide (Shopify: Settings → Customer events, or the official
      Facebook & Instagram channel app)
- [ ] Standard events firing: `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`
- [ ] `Purchase` passes **value** and **currency**. Verify with the Meta Pixel Helper
      browser extension on a real test order

### 3.2 Conversions API — mandatory, not optional
Browser-only tracking loses a large share of a 48–65 audience on iOS. CAPI recovers it.

Choose one, in order of preference:
1. **Shopify native CAPI** via the Facebook & Instagram sales channel (simplest, ships
   customer data automatically)
2. **Server-side GTM** (most control)
3. **Third-party connector** — Triple Whale / Elevar (best if you're already running a
   third-party tracker; see §6)

- [ ] CAPI live and sending `Purchase`
- [ ] **Deduplication configured** — browser and server events for the same purchase must
      share an `event_id`. Without this, Meta double-counts and your ROAS is fiction.
      Check: Events Manager → your Pixel → the event → "Deduplication" should read
      *"Events are being deduplicated"*

### 3.3 Maximise Event Match Quality
Send every parameter you legally have. Each one you add measurably lifts the score.

| Parameter | Send? | Note |
|-----------|:-----:|------|
| Email (`em`) | ✅ Required | Hashed SHA-256, lowercased, trimmed |
| Phone (`ph`) | ✅ Required | E.164, digits only |
| First / last name (`fn`, `ln`) | ✅ | |
| City / State / Zip (`ct`, `st`, `zp`) | ✅ | Explicitly called out in the source doc |
| Country (`country`) | ✅ | |
| External ID (`external_id`) | ✅ **High impact** | Your customer/session ID — one of the strongest match keys |
| Click ID (`fbc`) | ✅ **High impact** | From the `fbclid` URL param; must be captured and persisted in a cookie |
| Browser ID (`fbp`) | ✅ | The `_fbp` cookie |
| Client IP + User Agent | ✅ | Server events only |

**Gate: EMQ ≥ 7.0 on `Purchase`.** Check at Events Manager → Pixel → Overview → the event →
*Event Match Quality*. Give it 48h of real traffic before reading the score.

| EMQ | Verdict |
|-----|---------|
| 8.0–10 | Excellent. Nothing to do |
| 7.0–7.9 | Acceptable. Launch |
| 5.0–6.9 | **Fix before launching.** You're missing `external_id` or `fbc` |
| < 5.0 | Broken. CAPI is likely not sending customer parameters at all |

---

## 4. Aggregated Event Measurement

**Path:** Events Manager → Data Sources → Pixel → Settings → **Aggregated Event Measurement**
→ Configure Web Events

Rank your 8 events by business priority. Priority 1 is what iOS users get attributed to.

```
1. Purchase                ← must be #1
2. InitiateCheckout
3. AddToCart
4. ViewContent
5. Lead                    (if you run a quiz/email capture)
6. Search
7. AddPaymentInfo
8. PageView
```

- [ ] `Purchase` is priority 1
- [ ] Value optimization enabled on `Purchase` if you plan to use value-based bidding later

> Reordering these puts the pixel into a **72-hour cooldown** during which delivery can be
> disrupted. Set it now, before launch, and don't touch it again.

---

## 5. Audiences to build before launch

**Path:** Ads Manager → Audiences → Create Audience → Custom Audience

Build these in this order. The exclusion is the only mandatory one at launch; the rest feed
diagnostics and later phases.

| # | Audience | Source | Definition | Used for |
|---|----------|--------|------------|----------|
| 1 | `EXCL_Purchasers_180d` | Website + Customer list | Purchase, last 180 days | **Mandatory exclusion on all 3 ad sets** |
| 2 | `EXCL_Purchasers_180d_CRM` | Customer list upload | All customers who bought in 180d, from Shopify/Klaviyo | Layered with #1 — catches untracked purchases |
| 3 | `SEED_HighAOV_Buyers` | Customer list | Customers who bought the B3G3 bundle, last 365d | Value signal (§6), and Robert/T3 expansion |
| 4 | `ENG_VideoViewers_75_30d` | Video | Watched ≥75% of any video, 30 days | Diagnostics only — tells you whether Rings 1–3 are producing warm supply |
| 5 | `ENG_AllEngagers_90d` | FB Page + IG account | 90 days | Diagnostics; T4 retargeting |

- [ ] #1 and #2 built and **combined into one exclusion set** on every ad set
- [ ] #3 uploaded with as many match parameters as possible (email, phone, name, city, state,
      zip) — this list's match rate directly determines how well Meta can find more Lindas

> **The 180-day exclusion is worth real money here.** Linda buys a 3–6 month supply. Without
> the exclusion, Meta will happily spend acquisition budget re-selling to a woman who has
> four unopened bottles in her cupboard, and it will look profitable in the reporting while
> your genuine new-customer rate quietly collapses.

---

## 6. Feed value back to Meta (Becker's "secret sauce")

This is the highest-leverage item in this file and the one most accounts skip.

**The problem:** Linda clicks on her phone, researches on her iPad, and buys on desktop a
week later. Meta's native attribution loses that journey and therefore optimizes toward
whoever clicks cheapest — not whoever buys the $99.98 bundle.

**The fix, in three layers:**

### Layer 1 — Accurate purchase value (do this at launch)
- [ ] `Purchase` events carry the **real order value**, not a flat number
- [ ] Currency set explicitly to USD
- [ ] Refunds/cancellations are **not** sent as purchases

### Layer 2 — High-value custom conversion (do this at launch)
- [ ] Events Manager → Custom Conversions → Create
- [ ] Name: `Purchase_HighAOV_Bundle`
- [ ] Rule: `Purchase` where `value >= 90` (the B3G3 tier)
- [ ] **Do not optimize for this yet** — you will not have 50/week. It exists so you can
      *report* on high-value acquisition rate from day one, and so it has history when you
      do switch

### Layer 3 — Third-party tracker + offline conversions (T2 and above)
- [ ] Install Triple Whale (already connected to this workspace), Hyros, or Northbeam
- [ ] Enable its Meta CAPI integration so post-click, cross-device, and delayed purchases
      flow back to the pixel
- [ ] Configure it to pass the **customer LTV / predicted-value** signal where supported

**When to switch bidding to value:** once the account produces ≥ 50 purchases per week
*and* your high-AOV rate is stable for 4 weeks, change the CONTROL ad set's optimization to
**Value** instead of Conversions. Not before — value optimization on thin data is worse than
volume optimization.

---

## 7. Naming convention (copy-paste)

Consistency here is what makes reporting possible. See [`templates/naming-convention.md`](templates/naming-convention.md).

```
CAMPAIGN   PI | CORE | CBO | Sales
ADSET      CONTROL
           TESTA_3PMCRASH_UGC
           TESTB_BRAINFOG_VSL
AD         R1_3PMCRASH_UGC_LINDA62_KITCHEN_v1
           R4_SKEPTIC_STATIC_BUNDLE_LABCERT_v2
```

Ad name grammar: `R{ring}_{ANGLE}_{FORMAT}_{PERSONA}_{VISUALSCENE}_v{n}`

| Slot | Allowed values |
|------|----------------|
| `{ring}` | `1` `2` `3` `4` `5` |
| `{ANGLE}` | `3PMCRASH` `BRAINFOG` `GRANDKIDS` `SKEPTIC` |
| `{FORMAT}` | `UGC` `VSL` `FOUNDER` `TESTIMONIAL` `STATIC` `ADVERTORIAL` |
| `{PERSONA}` | `LINDA62` `LINDA55` `ROBERT65` `FOUNDER` |
| `{VISUALSCENE}` | free text, no spaces — `KITCHEN` `CARPARK` `COUCH` `PARKWALK` |
| `v{n}` | iteration number |

**Never rename a live ad.** It breaks your historical reporting joins and your UTMs.

---

## 8. UTM tracking

Set once at the ad level, using Meta's dynamic parameters so it self-populates.

**Path:** Ad level → Tracking → URL parameters

```
utm_source=facebook
&utm_medium=paid
&utm_campaign={{campaign.name}}
&utm_content={{ad.name}}
&utm_term={{adset.name}}
&utm_id={{campaign.id}}
&utm_source_platform=meta
&placement={{placement}}
&site_source={{site_source_name}}
```

- [ ] Applied to every ad
- [ ] Verified in GA4 / Triple Whale — click one live ad and confirm the parameters land
- [ ] Landing page does **not** strip query parameters on redirect (a very common Shopify
      page-builder bug that silently destroys all attribution)

---

## 9. Launch gates — all must be green

| # | Gate | How to verify | ✅ |
|---|------|---------------|---|
| 1 | Ad account timezone = America/New_York | Ad account settings | ☐ |
| 2 | Backup payment method on file | Billing | ☐ |
| 3 | Domain verified | Business Settings → Domains shows green | ☐ |
| 4 | Pixel firing all 4 standard events | Pixel Helper on a real session | ☐ |
| 5 | CAPI live and **deduplicated** | Events Manager shows "Events are being deduplicated" | ☐ |
| 6 | **EMQ ≥ 7.0 on Purchase** | Events Manager → Purchase → Event Match Quality | ☐ |
| 7 | AEM configured, Purchase = priority 1 | Aggregated Event Measurement | ☐ |
| 8 | `EXCL_Purchasers_180d` built and populated | Audiences (size > 0) | ☐ |
| 9 | `Purchase_HighAOV_Bundle` custom conversion live | Custom Conversions | ☐ |
| 10 | UTMs verified end-to-end | Click a live ad, check GA4/TW | ☐ |
| 11 | Landing pages load < 3s on iPad | PageSpeed Insights + a real iPad | ☐ |
| 12 | Apple Pay / Shop Pay enabled at checkout | Test checkout | ☐ |
| 13 | Economics worksheet completed with **real** numbers | `02-economics-and-kpis.md` | ☐ |
| 14 | ≥ 9 creative assets approved and uploaded | `03` + `08` | ☐ |

> **Gate 6 is the one people skip.** An account launched at EMQ 4 will underperform an
> identical account at EMQ 8 by a margin that no amount of creative work recovers. Fix it
> first.

---

**Next:** [`02-economics-and-kpis.md`](02-economics-and-kpis.md) — turn your P&L into the thresholds that run the account.
