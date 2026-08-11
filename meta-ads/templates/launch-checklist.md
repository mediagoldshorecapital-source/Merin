# Launch Checklist

Print this. Do not publish until every box is ticked.

Launch date: ____________ (must be **Thu / Fri / Sat**)  ·  Owner: ____________

---

## A · Foundations (file 01)

- [ ] Ad account timezone = **America/New_York** *(permanent — verify before anything else)*
- [ ] Business Manager verified
- [ ] Page + Instagram connected to the BM
- [ ] Payment method **+ backup card** on file
- [ ] Domain verified (green in Business Settings → Domains)
- [ ] Pixel firing: `ViewContent` `AddToCart` `InitiateCheckout` `Purchase`
- [ ] `Purchase` passes real **value** and **currency**
- [ ] CAPI live
- [ ] **Deduplication confirmed** — "Events are being deduplicated"
- [ ] **EMQ ≥ 7.0 on Purchase** → actual: `______`
- [ ] AEM configured, `Purchase` = priority 1
- [ ] `EXCL_Purchasers_180d` built, size > 0 → `__________`
- [ ] `EXCL_Purchasers_180d_CRM` uploaded
- [ ] `Purchase_HighAOV_Bundle` custom conversion live
- [ ] UTM block tested end-to-end into Shopify

## B · Economics (file 02)

- [ ] Worksheet completed with **real** 30-day numbers
- [ ] Blended AOV `$______`
- [ ] Break-even CPA `$______`
- [ ] **Target CPA** `$______`  ·  Tolerance CPA `$______`
- [ ] Forced minimum spend (1× AOV) `$______/day`
- [ ] Learning-phase floor `$______/day`
- [ ] Creative quota `______ ads/mo`
- [ ] Tier selected: ☐ T1 ☐ T2 ☐ T3 ☐ T4  ·  Daily budget `$______`

## C · Creative (files 03, 08)

- [ ] All 5 Rings have an approved asset
- [ ] TEST-A 3:2:2 pack complete (3 creatives same media type, 2 texts, 2 headlines)
- [ ] TEST-B 3:2:2 pack complete *(T2+ only)*
- [ ] Every asset passes the Entity-ID checklist against every other
- [ ] 3-second muted test passed across all live assets
- [ ] **Compliance sign-off recorded** — reviewer ____________ date ______
- [ ] All `[bracketed placeholders]` replaced with substantiated claims
- [ ] Subtitles burned in, ≥ 40px
- [ ] All assets reviewed on a real **iPad**
- [ ] 3 alternate hook cuts banked per video

## D · Landing pages (file 09)

- [ ] Energy advertorial live
- [ ] Clarity advertorial live
- [ ] Product page with **B3G3 variant preselected**
- [ ] Top navigation removed on advertorials
- [ ] Testimonials matched to each page's pain point
- [ ] Apple Pay / Shop Pay enabled
- [ ] Loads < 3s on a real iPad over cellular
- [ ] UTMs survive into the Shopify order record
- [ ] Prices match the ad creative **exactly**
- [ ] Legal disclaimers present

## E · Campaign build (file 04)

**Campaign**
- [ ] Name `PI | CORE | CBO | Sales`
- [ ] Objective **Sales**
- [ ] Special Ad Categories = **None**
- [ ] **Advantage campaign budget ON**
- [ ] **Daily** budget `$______`
- [ ] Bid strategy **Highest volume** (no cost cap)

**Each ad set — verify all three individually**

| Check | CONTROL | TEST-A | TEST-B |
|-------|:---:|:---:|:---:|
| Conversion event = **Purchase** | ☐ | ☐ | ☐ |
| US · Women · 48–65 | ☐ | ☐ | ☐ |
| Detailed targeting **empty** | ☐ | ☐ | ☐ |
| Advantage+ audience ON | ☐ | ☐ | ☐ |
| **Both 180d exclusions applied** | ☐ | ☐ | ☐ |
| Advantage+ placements, no exclusions | ☐ | ☐ | ☐ |
| Attribution 7-day click / 1-day view | ☐ | ☐ | ☐ |
| Spending limit | **none** ☐ | **min $58** ☐ | **min $58** ☐ |

**Budget math**
```
Campaign daily budget      $ ______
− TEST-A minimum           $ ______
− TEST-B minimum           $ ______
= CONTROL remainder        $ ______   ← must be ≥ $58
```

**Each ad**
- [ ] Named per convention
- [ ] Correct Page + IG identity
- [ ] UTM parameters applied
- [ ] Destination correct: R1–3 → advertorial, R4–5 → bundle page
- [ ] CTA correct: R1–3 Learn More, R4–5 Shop Now
- [ ] **Advantage+ creative enhancements OFF**
- [ ] TEST ad sets contain **exactly one** Flexible Ad each

## F · Operations

- [ ] Stock confirmed for 30 days at forecast volume
- [ ] Tracker sheet created (`tracker-spec.md`)
- [ ] Calendar: **launch + 4** = first read (observation only)
- [ ] Calendar: **launch + 11** = first Monday Review
- [ ] **Freeze declared in writing** to everyone with account access
- [ ] Decision-rights table (file 00 §6) filled in and shared

---

## G · Publish

- [ ] Published before **10 AM ET**, on a **Thu / Fri / Sat**
- [ ] All 3 ad sets **Active** within 24h
- [ ] Impressions serving on all 3 within 2h
- [ ] Live click test → journey to checkout (no purchase) → `ViewContent`, `AddToCart`,
      `InitiateCheckout` confirmed in Test Events with UTMs intact
- [ ] Launch row written into the tracker

---

## 🔒 The 72-hour freeze starts now

**Permitted:** delivery check, spend pacing check, pixel health check.
**Forbidden:** budget changes, pausing, adding creative, editing copy or targeting.

> Emergency stop conditions only: pixel/CAPI down · stockout · compliance issue ·
> runaway spend from a misconfiguration. **"CPA looks bad" is not one of them.**

Signed: ____________  Date: ____________
