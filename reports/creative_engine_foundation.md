# Creative Engine Foundation: NMN Complex (Meta account 2009539369903270)

Data: Meta Ads, 16 Apr – 16 Oct 2026, this account only. The numbers behind every claim are in `meta_winning_creatives_2026-04-16_to_2026-10-16.xlsx` (same folder).

---

## 1. What can be pulled from Meta, and what can't

| Item | Status | Notes |
|---|---|---|
| Ad names, campaign / ad set names, IDs | ✅ Yes | Older winners have generic names ("- Video - Ad - 1"), so the name alone says nothing about the creative. |
| Video **file names** | ✅ For newer uploads | e.g. `14B. 20260930_TapTheCart_V1.mp4`. Older winning videos only carry the headline as their title ("SPRING SALE! 75% OFF TODAY ONLY!"). |
| Primary text, headline, description, CTA, video length | ✅ Yes | In the Winners tab. |
| Ad previews (watchable in browser) | ✅ Yes | Ads Manager / preview links per ad. |
| Downloading the actual video/image files | ❌ Not from here | Meta returned no download link for these videos, and this cloud session's network blocks `facebook.com` / `fbcdn.net`. |
| Watching the videos frame by frame | ⚠️ If you upload them | Upload the MP4s and I can extract frames (ffmpeg is installed), read on-screen text, map hook → problem → mechanism → offer, and time each beat. A transcript or caption file also helps (no speech-to-text here). |
| Who bought (age, placement) | ✅ Age; placement partial | Gender came back incomplete. |

**So:** the "why" below is built from performance data, copy, video length, audience and dates. The visual and spoken half of the "why" (hook shot, speaker, pacing) still needs the video files.

---

## 2. Winner DNA: what the proven ads share

Evidence comes from the 22 tier A/B ads ($121k spend; the two tier C ads add $86k). See the Winners, Creative Concepts and Winners by Age tabs.

1. **One product, one problem:** NMN Complex for *tiredness that comes with age*. Every top winner uses the same core message:
   > "Feeling more tired as you age? It's not 'just aging.' Your NAD+ levels naturally drop — the molecule your cells need for clean, steady energy…"
   
   That is **problem-aware education + a simple mechanism (NAD+ drops) + a product as the fix**. It is not curiosity bait and not shock.
2. **A hard, time-boxed offer:** "75% OFF TODAY ONLY", re-skinned as New Year / Flash / Spring / Summer sale. The offer stays the same and only the season label rotates.
3. **The buyer is 55+:** 76% of winner spend went to ages 55+. **65+ has the best ROAS (1.30×)**, then 55–64 (1.23×), 45–54 (1.21×), 35–44 (1.12×). Under 35 barely buys.
4. **Video, served on Facebook rather than Instagram:** in the placement rows returned, Facebook Reels and Feed carry ~94% of the spend. Instagram rows were missing from that response, so this one needs re-checking.
5. **A handful of master visuals do the work:** the visual with ID 634374960 alone carries $109k at 1.20×. Five visuals account for most winning spend. Winners are **re-uploads of the same proven asset** into new ad sets, not new ideas.
6. **Length is not the lever:** winners range from 7s to 133s. The longest (133s "New Year Flash Sale", ad 120242308889180341) held 40% to ThruPlay and made 1.39×.

### What is *not* working (Sept–Oct angle tests)
In September and October, $53k went to 124 named angles (Angle Tests tab):

| Angle style | Examples | Result |
|---|---|---|
| Authority / conspiracy / shock | MilitaryTakesWhat ($13.7k, 0.53×), USGovUsesNMN (0.62×), KattExposedHollywood (0.60×), DoctorExplainsTMG (0.61×) | **High CTR (4–7%) and strong hold, but they lose money.** They attract clicks, not buyers. |
| "Is it a scam?" / myth-busting | IsNADAScam (0.98×, 1 ad disapproved), MostFakedNMN (0.83×) | Breakeven at best, and they carry policy risk. |
| Urgency + offer | **Only4hrsLeft (2.01×, $34 CPA)** | The only clear winner signal in the batch. |

The September strategy moved **away** from the winning DNA (plain problem → mechanism → offer) towards curiosity hooks. At the same time, the proven video kept scaling and wore out (the $66k ad went from 1.29× in Jul to 0.86× in Sep to 0.62× in Oct). That combination largely explains the recent drop.

Testing was also spread too thin: ~124 angles at ~$430 average spend is about 7 purchases each at a $60 cost per purchase. That's too few to tell a winner from noise.

---

## 3. Hypotheses to test (why the winners won)

| # | Hypothesis | How to test it |
|---|---|---|
| H1 | A 55+ viewer buys when they **recognise their own symptom** (afternoon crash, fog), not when they're intrigued. | Same video, swap the first 3s: symptom hook vs. curiosity hook. |
| H2 | The **"75% off today only"** deadline does most of the converting. | Same video, test the offer frame: 75% off today / Buy 3 get 3 / no discount + guarantee. |
| H3 | **Re-skinning** a proven body with a new hook and season beats a brand-new concept. | Make 5 new hooks on the body of the visual with ID 634374960. |
| H4 | A **peer testimonial** (a 58–70-year-old speaking) beats doctor or authority voices for this audience. | The story-style copy ("By 58, my mornings started fine…") is already in the account. Turn it into a UGC video. |
| H5 | Facebook Reels and Feed outperform Instagram because of where 55+ people spend time. | Check the placement breakdown before cutting Instagram. |

---

## 4. Variation matrix

Keep the **core** fixed: NMN Complex, the NAD+-drops-with-age explanation, ages 55+, a sale offer. Change **one variable per test**:

| Variable | Variations |
|---|---|
| Hook (first 3s) | Symptom ("3pm and you're already done?"), Age-callout ("If you're over 55, watch this"), Comparison ("Coffee isn't the fix after 50"), Before/after day, Pattern-interrupt product shot |
| Speaker / persona | Woman 60s, Man 60s, Couple, Faceless text-on-screen, Founder |
| Mechanism depth | 1 line (NAD+ drops) vs. 20s explainer vs. animated cell graphic |
| Proof | Reviews montage, "90 days" journal, Bottle-in-routine |
| Offer frame | 75% off today only, Only X hours left, Bundle (3 bottles), Guarantee-led |
| Format / length | 9:16 Reel 15–30s, 45–75s story, 2-min long-form, Static image |

### First 12 briefs (from proven bodies)

| # | Base asset | Change | Hook (on screen + voice) |
|---|---|---|---|
| 1 | Visual 634374960 | Hook only | "Feeling wiped out by 3pm? After 55 it's not just you." |
| 2 | Visual 634374960 | Hook only | "If you're over 55, your cells are running low on one thing." |
| 3 | Visual 634374960 | Hook only | "Another coffee won't fix this after 50." |
| 4 | Visual 634374960 | Offer: Only 4 hrs left | Same body, end card "75% off ends tonight" |
| 5 | Video 728562103409957 (133s) | Cut to 45s | Keep the first 10s, mechanism, offer |
| 6 | Video 728562103409957 | Season re-skin | "FALL SALE! 75% OFF TODAY ONLY!" |
| 7 | Story copy (ad cr 1. 3 Bottle Offer) | Turn into UGC video | Woman ~60: "By 58, my afternoons were gone…" |
| 8 | Story copy | Man ~62 version | "I thought slowing down was just getting older." |
| 9 | Only4hrsLeft | Scale + 2 hooks | Symptom hook + countdown |
| 10 | Static "19" (1.63×) | 3 headline variants | Symptom / Age-callout / Offer-first |
| 11 | Visual 627853673 (1.44× across ads) | Hook only | "Still tired after a full night's sleep?" |
| 12 | Astaxanthin visual 668732739 (1.47×) | Same treatment for product #2 | "Over 50 and your skin changed overnight?" |

**Compliance:** keep claims to energy, focus and supporting NAD+ levels. Avoid disease, menopause, insulin, eyesight and "reverse aging" claims. Several September file names (TFixInsulineProlem, MenopauseWomen, EyeSight, ReverseGrey) are review and policy risks, and one "scam" ad was already disapproved.

---

## 5. Testing protocol

- **Budget per variation:** at least $600, which is about 10 purchases at the $60 account average. Below $300, don't judge an ad (the Angle Tests sheet flags these).
- **Decision rules:** these use the default thresholds and can be edited in the workbook.
  - Kill: $300 spent with ROAS < 0.8×.
  - Keep: $600 spent with ROAS ≥ 1.10×.
  - Winner: $1,000 spent, 20+ purchases and ROAS ≥ 1.30×. Then duplicate it into scale.
- **Volume:** 6–10 variations a week, spread across ~3 concepts, instead of 100+ one-offs.
- **Refresh trigger:** if a scaled ad's 7-day ROAS drops 25% below its 30-day ROAS, or its frequency passes 2.5, ship its next hook variation.

### Naming convention
Name every file and ad like this:

`YYYYMMDD_Product_Angle_Hook_Persona_Offer_Len_V#`, e.g. `20261020_NMN_NADdecline_Symptom3pm_Woman60_75Today_30s_V1`

With this naming, the Angle Tests analysis runs automatically by hook, persona and offer. Today only the angle can be read from file names.

---

## 6. What I need from you to finish the "why"

1. **Upload the MP4s** of the 6 assets that drive the winners, plus Only4hrsLeft:
   - Ad 120243669805030341 (visual 634374960, $36k, 1.49×)
   - Ad 120242308889180341 (video 728562103409957, "New Year Flash Sale", 133s)
   - Ad 120243160670300341 (visual 626804201)
   - Ad 120243675534840341 (visual 627853673)
   - Ad 120243701969760341 (visual 626417952)
   - Ad 120243619709580341 (visual 632447272, 2.07×)
   - Only4hrsLeft (ad 120254362729110341)

   Each is in Ads Manager: `https://www.facebook.com/adsmanager/manage/ads/edit?act=2009539369903270&selected_ad_ids=<AD ID>`
2. **Scripts or captions** for those videos, if you have them.
3. **Break-even ROAS** (including subscription and repeat purchases), so the winner line isn't guessed.
4. Optionally, allow `facebook.com` and `fbcdn.net` in this environment's network settings so thumbnails can be pulled directly.
