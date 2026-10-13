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
  - URL parameters: `utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&tw_source={{site_source_name}}&tw_adid={{ad.id}}`
  - Enhancements: **Enhance CTA ON** (`degrees_of_freedom_spec.creative_features_spec.enhance_cta = OPT_IN`); other enhancements off
  - WhatsApp phone number: **Use Facebook Page**
  - Multi-advertiser ads: **ON** (`contextual_multi_ads.enroll_status = OPT_IN` in the creative; the tool defaults it to OPT_OUT, so set it explicitly)
  - Also set `url_tags` on the creative to the URL parameters above, so new builds carry them without a manual edit
  - The connector can't read back URL parameters, Enhance CTA or the WhatsApp setting. After a build, the user checks them in Ads Manager, or bulk-edits all ads at once (select all → Edit), which is fast and keeps the media.
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
  - Drive original lengths, used to check each Meta upload (a mismatch means the wrong file): 1C 96.18s, 2C 110.37, 3C 121.09, 4C 59.75, 5C 103.14, 6C 85.64, 7C 65.95, 8C 74.00, 9C 44.00, 10C 67.64, 11C 94.76, 12C 45.00, 13C 52.25, 14C 15.37, 15C 47.37
  - The first "15C Secret" upload (video 28750526634570128, 96.18s) was really EyeSight. Its ad was deleted, and a correct re-upload is needed.
  - Status 2026-10-13: all 30 built and turned off (1C–15C videos, 16C–30C statics), each with bodies, titles and descriptions and each checked against its Drive original. The wrong 15C (EyeSight file, video 28750526634570128) ad was deleted and rebuilt. Template ad paused. Ad set starts 2026-10-24 00:01 ET; ads still need to be turned on.
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

## Verification rule for videos
Before building a video ad, compare the Meta video `length` with the Drive original's duration (read the mp4 `mvhd` box after downloading from `drive.usercontent.google.com/download?id=<ID>&export=download`; large files need the `confirm=t&uuid=` step from the virus-scan page). If they don't match, the upload is mislabeled: don't build the ad.

## Ad set 86 (batch D, 20261002)

- Ad set `86__Broad_USA_Creative_testing – 26-10-26` (`120254445369460341`), created by Claude with 85's settings, start 2026-10-26 00:01 ET, turned off
- Drive folder: `1yonY0pfIc9CW8WorKmkHrNNs-ARw3Jwl` (statics only at first; no videos in Drive)
- 16D–30D statics built 2026-10-13 with url_tags, Enhance CTA OPT_IN, multi-advertiser OPT_IN, bodies, titles and descriptions
- 2D–10D videos built 2026-10-13 (lengths 118.0, 66.4, 92.1, 51.6, 87.5, 37.3, 16.6, 20.7, 32.3s; no Drive originals, so checked only for duplicates).
- 13D Teacher_V1 (video 1113942288040094, 27.9s), 14D CarExplained_V1 (2174336333513565, 34.3s), 15D FlashSale_V1 (1050258754716605, 14.144s, matches Drive original 1mwisqdSy4yYs7tJuZkZ6PjL9fypl3943) built 2026-10-13, off. A second upload named 15D FlashSale (1581338093200609, 230.3s) is the wrong file (it is 1D CaptAmerica); don't use it. 12D MenopauseWomen_V1 (4426904427525066, 37.4s) built 2026-10-13, off.
- Audit 2026-10-13: 28/30 ads checked. Every video ad's creative video length matches its upload (Meta re-hosts the video under a new ID titled with the headline, so compare lengths, not IDs); statics 16D–30D hashes match in order; copy, CTA and link correct on all.
- 1D CaptAmerica_V1 (1731941841224749, 230.272s) and 11D MassiveSale_V1 (2912530785767058, 22.407s) built 2026-10-13, off. Ad set 86 complete: 30/30. The extra '15D FlashSale' upload (1581338093200609, 230.272s) was really CaptAmerica (1D) under the wrong name; not used.

## Ad set 87 (batch E, 20261003)

- Ad set `87__Broad_USA_Creative_testing – 28-10-26` (`120254446150740341`), same settings as 86, start 2026-10-28 00:01 ET, turned off
- Drive folder `161yfT6--WDmTMksKhYC797E34X7QFZmc`: subfolders Images (`1lgT32zvNvSSLRyzNtzf-y8zdo2E7ZZ4A`, 20 statics `20261003-Static_V (1..20).png`) and Videos (`18ez2UMWz5Bm1pxVsZTL8SRBPYIJztCN3`, 9 videos, no number prefix)
- 16E–30E built 2026-10-13 from Static_V (1)–(15), off. Static_V (16)–(20) not used yet (waiting on the user)
- 9E GetThisTonight_V1 (video 4525729444352440, 19.388s, matches Drive 19.389s) built 2026-10-13, off
- Drive video lengths, used to check uploads: 61yrNMNefferct 97.965 · BiggerThanCreatine 118.26 · EndsToday 7.338 · Explainer 115.171 · GetThisTonight 19.389 · HonestReviews 350.041 · Iam40 78.577 · NADorNMNt 101.657 · Tedtalk 189.034

## Standing workflow (from the user, 2026-10-13)
- Videos: the user uploads them to **Media Library → Ad account media** (not the ad edit screen), named `<n><Letter>. <YYYYMMDD>_<Concept>_V<v>.mp4`. Look for them there.
- Statics: in a Google Drive folder link; import via lh3, numbered 16–30 with the batch letter.
- Batch letter per ad set: 85=C, 86=D, 87=E, 88=F, 89=G, and so on (ad set number minus 82 → letter index, A=83).
- New ad set every 2 days at 00:01 ET: 86 = Oct 26, 87 = Oct 28, 88 = Oct 30, …

## Copy-paste templates for the user

Drive folder: `<AdSetNumber>_<Letter>_<YYYYMMDD>` with subfolders `Statics` and `Videos`.

Statics (15): `16<Letter>. <YYYYMMDD>_Static_V (1).png` … `30<Letter>. <YYYYMMDD>_Static_V (15).png`
Videos (15, same names in Drive and Ad account media): `1<Letter>. <YYYYMMDD>_<Concept>_V1.mp4` … `15<Letter>. <YYYYMMDD>_<Concept>_V1.mp4`

Message:
```
New ad set ready
Ad set: <AdSetNumber>
Letter: <Letter>
Creative date: <YYYYMMDD>
Start date: <DD-MM-YY> (or "usual")
Drive link: <paste link>
Videos uploaded to Ad account media: yes / partly (<which ones>)
Text changes: none / <describe>
```
