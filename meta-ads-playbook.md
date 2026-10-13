# Prime Ingredients: Meta Ads testing playbook

Learned from the live account on 2026-10-12 (ad account `2009539369903270`). Use this when building new creative-testing ad sets.

## Campaign structure

| Campaign | ID | Objective | Budget (CBO) | Bid strategy |
|---|---|---|---|---|
| 8. NMN Testing Campaign (CBO) June 21 2026 | `120251599164970341` | Sales | $1,500/day | Highest volume |
| 9. NMN Scale Campaign (CBO) June 27 2026 | `120251581940690341` | Sales | $2,000/day | Highest volume |

New test ad sets go into the **Testing** campaign. The budget sits at the campaign level (CBO), so ad sets have no budget of their own.

## Ad set rules (identical across ad sets 73–84)

- **Name:** `<N>__Broad_USA_Creative_testing – <DD-MM-YY>`, where N is the next number in sequence and the date is the start date
- **Cadence:** one new ad set every **2 days**, starting at **00:01 America/New_York**
- **Optimization:** Conversions → Website **Purchase**, pixel `25563599826640611`
- **Billing:** impressions
- **Attribution:** 7-day click, 1-day view, 1-day engaged-view
- **Location:** United States (home, recent and frequently-in)
- **Age:** 18–65+, all genders, **Advantage+ audience ON**, no interests or custom audiences (broad)
- **Placements:** Advantage+ (all platforms: Facebook, Instagram, Audience Network, WhatsApp, Threads)
- **Brand safety:** relaxed

## Ads inside each ad set

- About **30 ads per ad set**: roughly 15 video concepts plus roughly 15 statics
- **Ad name:** `<n>[A|B]. <YYYYMMDD>_<ConceptName>_V<version>` for videos and `<n>. <YYYYMMDD>_Static_V (<k>)` for statics. The YYYYMMDD part is the creative **batch date**, not the launch date. A batch suffix letter (A, B) shows up on newer batches.
- Each ad set uses **one creative batch**:
  - 79 → 20260926
  - 80 → 20260921
  - 81 → 20260924
  - 82 → 20260928
  - 83 → 20260929 (A)
  - 84 → 20260930 (B)
- **Copy is the same on every ad:**
  - Primary text: `Feeling more tired as you age? It's not "just aging." Your NAD+ levels naturally drop — the molecule your cells need for clean, steady energy. Our NMN Complex helps support those levels so you can feel energized, focused, and clear again.`
  - Headlines (5 options, set in Ads Manager as extra text options):
    1. `Support Energy Without More Coffee`
    2. `Beat the 3 PM Energy Slump`
    3. `How to Support Daily Energy`
    4. `Support Cellular Energy Daily`
    5. `SUMMER SALE! 75% OFF TODAY ONLY!` (check this one is still accurate before reusing it)
  - Optimise text per person: Disabled
  - Description: `Say goodbye to tiredness! NAD+ levels drop with age, but our NMN Complex helps boost them for clean energy & focus`
  - Display link: `Primeingredients.com`
  - CTA: **Shop Now**
  - Website link: `https://tryprimeingredients.com/products/nmn`
- **Identity:** Facebook Page "Prime Ingredients" (`1012373248616002`), Instagram @daily_prime_ingredients (`17841480103037701`). Pass the Instagram ID when creating a creative; the connector's Instagram account list comes back empty, but the ID works.
- **Swapping media:** an existing ad's creative can't be edited. Create a new creative and a new ad with the same name in the same ad set, pause the wrong ad, then activate the new one.
- Creative names are auto-generated as `<headline> <date>-<hash>`.

## Video concept themes seen

- Myth-busting or "scam" hooks: NMNScam, MostFakedNMN, DontBuyNMN, SupplementScam, Exposed
- Authority: DocAdvice, FDA, USGovUsesNMN, BryanJohnson, Podcast, AthletesUse
- Transformation: BeforeAfter, GrandmaLooks20, YoungGrandma, ILost45, HowIChanged
- Education: NMNvsNAD, AstaxanthinVsNMN, SignsOfLowNAD, Shoelace/Car explainers
- Offers and urgency: Only4hrsLeft, FlashSale, Buy1Get1Free, 2For2, DoubleDiscount, PriceDrops, Bundle

## Media library naming

- Videos are uploaded as `<n>. <YYYYMMDD>_<Concept>_V<v>.mp4`
- Statics are uploaded as `<n>. <YYYYMMDD>_Static_V (<k>).png`
- Many images are named `untitled`, probably auto-generated crops or thumbnails

## Guardrails

- Work only in account `2009539369903270` (see CLAUDE.md)
- Show the plan and get the user's OK before publishing anything that will spend money

## Next build: ad set 85 (batch C, 20261001)

- Ad set: `85__Broad_USA_Creative_testing – 24-10-26` (created by the user as a draft; it must be published turned off before the tools can read it)
- Template ad: copy of ad set 84's `2B. 20260930_Static_V (9)` (same copy, link, Page, Instagram)
- 30 ads in total, named after their files without the extension:
  - `1C`–`15C`: videos, `<n>C. 20261001_<Concept>_V<v>`. Order: 1C EyeSight, 2C Rightway, 3C BiggerThanCreatine, 4C Podcast, 5C NADvsNMN, 6C Athletes, 7C 6MonthsJourney, 8C Longevity, 9C HairGoneBack, 10C QuestionToLongevity, 11C ReverseGrey, 12C Over50s, 13C StopTaking, 14C DoubleDiscount, 15C Secret. The user said 6C/14C could go either way, so Athletes/DoubleDiscount was a free choice.
  - Status 2026-10-13: 15C and 16C–30C built and turned off. 1C–14C wait for video uploads. Template ad paused.
  - `16C`–`30C`: statics, `<n>C. 20261001_Static_V (<k>)`, uploaded to Ad account media on 2026-10-13
- Process: inventory the files, then send the build list for approval, build all ads turned off, verify every ad reads back with the right file, and turn ads on only after approval.
- Business media folders and Ads Manager drafts can't be read by the Meta connector. Files must be in **Ad account media**.

## Working method: ad with 5 headlines (tested 2026-10-13 on 15C)

`ads_create_ad` with an inline creative. A full `asset_feed_spec` (images/videos/bodies) is rejected because the ad set isn't Dynamic Creative. What works is a normal `object_story_spec` plus `asset_feed_spec` holding only `titles`, with `optimization_type: DEGREES_OF_FREEDOM`:

```json
{"name":"<ad name>",
 "object_story_spec":{"page_id":"1012373248616002","instagram_user_id":"17841480103037701",
   "video_data":{"video_id":"<id>","image_url":"<video picture url>",
     "message":"<primary text>","title":"Support Energy Without More Coffee",
     "link_description":"<description>",
     "call_to_action":{"type":"SHOP_NOW","value":{"link":"https://tryprimeingredients.com/products/nmn","link_caption":"Primeingredients.com"}}}},
 "asset_feed_spec":{"bodies":[{"text":"<primary text>"}],
   "titles":[{"text":"Support Energy Without More Coffee"},{"text":"Beat the 3 PM Energy Slump"},{"text":"How to Support Daily Energy"},{"text":"Support Cellular Energy Daily"},{"text":"FALL SALE: Save Up to 75% on NMN"}],
   "descriptions":[{"text":"<description>"}],
   "optimization_type":"DEGREES_OF_FREEDOM"}}
```

IMPORTANT: put `bodies` and `descriptions` in `asset_feed_spec` as well as `titles`. If only `titles` is there, Ads Manager shows the primary text and description as empty and the description is dropped. (This happened on the first batch C build, which was rebuilt.)

For statics, use `link_data` (`image_hash`, `link`, `message`, `name`, `description`, `call_to_action`) instead of `video_data`.

Known blockers and fixes:
- Freshly uploaded images can fail with "Image Not Found" in the connector even though they're in Ad account media.
- **Fix for images (works):** import each image from Drive with `ads_create_creative` and `image_url=https://lh3.googleusercontent.com/d/<DRIVE_FILE_ID>=s0`. Meta can fetch that address; plain `drive.google.com` links are blocked by robots.txt. This creates a throwaway "<n>C import" creative and makes the hash usable. A matching hash also proves the Drive file is the same file as the library upload. Then build the ad with that `image_hash`.
- To list a public Drive folder: `curl https://drive.google.com/embeddedfolderview?id=<FOLDER_ID>` (drive.google.com is allowed in this environment's network settings).
- Videos can't be imported by URL yet (the URL upload tool isn't rolled out for this account). Videos must be uploaded to Ad account media by a person.
- Batch C Drive folder: `18fdhHh0IWm-r9hWFwyDitZ9mFkt1iLBS` (subfolders Image / Video).
