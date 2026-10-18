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
- 2026-10-16: the user chose to build Static_V (16)–(20) as extra ads 31E–35E (Halloween copy, paused). Built and verified (hash, title, description, CTA): 31E `120254512566570341` (b026c71d…), 32E `120254512571250341` (2114ec85…), 33E `120254512578850341` (db926c6c…), 34E `120254512584270341` (82c91d8d…), 35E `120254512587930341` (52d507f5…). Create responses show 5/5/5 copy, `audios` random and `audio` OPT_IN. Ad set 87 now has 21 ads; it reaches 29 when the 8 missing videos are uploaded.
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

## Audit notes (2026-10-13, devil's-advocate pass)
- Ad set settings for 85/86/87 match 84 (pixel PURCHASE, 7d click/1d view/1d engaged view, US home/recent/frequently-in, 18–65 Advantage+ audience, Advantage+ placements, relaxed brand safety). 86/87 show `targeting_optimization: expansion_all` without `individual_setting`; delivery should be the same.
- Video cover images are stored at 1080×1920 (the 160px picture URL is fine). Statics are 1254×1254 square, with no 9:16 version.
- Every creative has an Instagram media ID and display link `Primeingredients.com`.
- The connector can't set or read WhatsApp = "Use Facebook Page". It has to be bulk-edited in Ads Manager on every new ad set (86 and 87 still need it).
- Daylight saving: US clocks go back on Sun 2026-11-01 at 2am. Start times from 2026-11-03 onwards use `-05:00`, not `-04:00`.
- Name check (2026-10-13): all 76 ads in 85/86/87 use the file their name says. Videos were matched by length to the upload and, for C and E, to the Drive original. Statics were traced from the ad's image hash to its "<n><L> import" creative and then to the Drive file ID and file name. Notes:
  - The 30 creatives in 85 are named "Support Energy Without More Coffee <date>-<hash>" because the user's Ads Manager bulk edit rebuilt them. Ad names are right; creative names are internal only.
  - Meta's copies of the videos are all titled with the headline. That's automatic.
  - fbcdn.net is blocked by this environment's network policy, so Meta-hosted images can't be downloaded to compare by eye.
  - Typos in source file names carry into ad names: 10D "CoffeeAin_thitting", and E Drive "61yrNMNefferct" and "NADorNMNt".

## Ad set 80 copy rewrite (2026-10-13, from "Prime Ingredients - final2.pdf")
- Ad set `80__Broad_USA_Creative_testing - 14-10-26` (`120254418516530341`, starts 2026-10-14 00:01 ET).
- 25 ads were rebuilt with the same media and new copy, and turned on. The 25 old ads were deleted.
- Each new ad carries all 5 primary texts, 5 headlines and 4 descriptions as text options (asset_feed_spec, DEGREES_OF_FREEDOM). The default is Option 1 (Halloween). Full copy is in `ad-set-80-new-copy.md`.
- Small fixes approved by the user: "Support Healthy Aging at the Cellular Level", "One Capsule. All 12 Aging Pathways", "Free shipping. 30-Day Money-Back Guarantee."
- Kept on every new ad: link /products/nmn, Shop Now, display link, url_tags, Enhance CTA, multi-advertiser ads, Page and IG.
- Not rebuilt: `1. 20260921_HavingtoGrab_V1` (120254437781370341). The real HavingtoGrab video isn't in Ad account media (both "HavingtoGrab" uploads are SideEffects), and the creative from the user's edit is unreadable (PRIVACY_CHECK_FAIL). It still has the old copy, so the user must edit it in Ads Manager.
- Left paused: old `2. SideEffects_V1` (120254418516590341).

## Ad set 81 rebuild (2026-10-15)

Ad set `120254419640220341` ("81__Broad_USA_Creative_testing – 16-10-26", starts Oct 16 00:01 ET). All 26 ads rebuilt to the CLAUDE.md core rules: new headlines, 5 descriptions, 5 PTs (PT1 "up to 75% off"), URL parameters, every creative-setup and Advantage+ option off except Enhance CTA and multi-advertiser ads, and Add music ON for the 11 statics only.

- 11 statics: same image hash as the old ads (checked one by one).
- 15 videos: Meta re-hosted under new video IDs; every length matches the original to the millisecond (LastDay kept its original ID).
- 26 new ads turned on, 26 old ads deleted. The ad set now holds exactly 26 ads.
- On 2026-10-15, 5 videos were still in Meta review: Shoelace, DoubleDiscount, FallEndSale, USGovUsesNMN, PodcastExplainer.
- Still manual: WhatsApp "Use Facebook Page" (bulk-edit in Ads Manager).
- **Correction (2026-10-16):** Add music was NOT actually on for the 11 statics; the user checked in Ads Manager. They were built with `audio` OPT_IN only. A test ad with `asset_feed_spec.audios=[{"type":"random"}]` added is waiting on the user's check (see CLAUDE.md). The 11 statics still need rebuilding once the fix is confirmed.
- **Fixed (2026-10-16):** after the user confirmed the test ad showed Music ON, all 11 statics in ad set 81 were rebuilt with `audio` OPT_IN plus `asset_feed_spec.audios=[{"type":"random"}]`. The old no-music statics were deleted. The ad set holds 26 ads (15 videos + 11 statics). Ad sets 86/87 statics still have no music.

## Ad sets 82–87 rebuild (2026-10-16)

Rebuilt with the Halloween copy (`copy/2026-q4-halloween.json`) via `build_specs.py`: all rules, music on statics. Each new ad uses the same media as the ad it replaced (statics checked by hash, videos by length). Old ads were deleted only after their replacement was verified. **All new ads are PAUSED and wait for the user's check.** Ad set on/off states were not changed.

| Ad set | New (paused) | Old deleted | Kept, still old copy |
|---|---|---|---|
| 82 | 30 | 31 (incl. paused duplicate DontUseNMN) | none |
| 83 | 15 (14 statics + LiveTV) | 15 | 12 videos (source hidden: PRIVACY_CHECK_FAIL) + 4A Bandaid (disapproved), still ACTIVE |
| 84 | 16 statics | 16 | 14 videos (source hidden), still ACTIVE |
| 85 | 30 | 30 | none |
| 86 | 30 | 30 | none |
| 87 | 16 | 16 | none |

- Renames in 82: "SheSaysThat_V1 – Copy" → "SheSaysThat_V1", "091520260928_HollywoodStars_V1" → "20260928_HollywoodStars_V1". In 83: double space removed in "1A. LiveTV".
- The 26 hidden videos in 83/84 need the MP4s uploaded to Ad account media (or a hand edit in Ads Manager) before they can be rebuilt.
- To go live: turn on the new ads (82 starts Oct 18 00:01 ET). Bulk-edit WhatsApp → "Use Facebook Page".
- 2026-10-16: the user asked to delete 4A Bandaid (`120254422868250341`, DISAPPROVED). The connector's delete was refused: "Ad Creative Is Incomplete: The reel you selected for your ad is not available" (code 100 / 2446289). Meta re-checks the hidden video even on delete, so the ad has to be deleted by hand in Ads Manager. The other hidden-video ads in 83/84 will probably hit the same error when their replacements are ready.
- Ad set 87 statics: Drive has 20 statics (all different, by md5). Static_V (16)–(20) were built as 31E–35E on 2026-10-16 (see the ad set 87 section).

## Drive reorganized by ad set (2026-10-18)

The creatives for ad sets 80–87 now live in one folder per Meta ad set, named exactly like the ad set, under **"Meta ad sets 80-87"** (`1GQVRjl0jM-ir7dLiaX1voRH-m8nRSwqA`) inside the shared "2. Video Editor" folder (`1ng4U0MmER_6v1NajZH-oToyrh8C4Lggj`). Each has `Images` and `Videos` subfolders. File names were not changed, so they still match the Meta ad names.

| Ad set | Folder ID | Old Drive folder | Files |
|---|---|---|---|
| 80 | `1gDk9BUoMPnKVrDF7jdU9FPVJBToMTAkz` | 43. Winning Creatives | 26 |
| 81 | `1fCI7BUr-aQjaTTcpac8WWxP3qUvzeI8F` | 46. Winning ads V13 | 26 |
| 82 | `1Wbs43fJPGF_dXDpheGkcYSnkQ86Xus-L` | 49. Winning Ads V15 | 30 |
| 83 | `1E7-qhbRxBMjqw-QCC3glGBqTCAy07kKa` | 50. Winning Ads V16 | 28 |
| 84 | `1Jy5kWckRseRJVSoMzhpxoWr59sfb1jA6` | 51. Winning Ads V17 | 30 |
| 85 | `1ryd56kAlCNqQgk-ICtwH7JAV49tLJCPS` | 52. Winning Ads V18 | 30 |
| 86 | `13417Oa-byfCyBDlSkM310Asd82Nep0CZ` | 53. Winning Ads V19 | 30 |
| 87 | `1te8joZYAjDqfEEHMrOzwwBi1g3nzCvHv` | 54. Winning ads V20 | 29 (incl. the 8 videos not built yet) |

- 226 files were moved. 3 videos in ad set 80 (BestDuo, Buy1Get1Free, UniverseSign) are owned by su8910bag@gmail.com and couldn't be moved, so copies were put in the ad set 80 folder; the originals are still in folder 43.
- Left behind on purpose (no ad uses them): `20260929_Static_V (3).png` and `20260929_ListenToThis_V1.mp4` in folder 50.
- The old folders 46, 49, 51, 52, 53 and 54 are now empty. The Drive folder IDs logged earlier for batches C, D and E (52, 53, 54) point to those empty folders; use the ad set folders above instead.
- Verified by listing every new folder: 229/229 files in the right place, nothing missing or extra.

## Active ads reference folder (2026-10-18)

**"Active Meta ads – reference (Oct 18)"** (`1IOukstX6jX4oLzRAjpqdWbuPcs9BHJIl`) in "2. Video Editor" holds the Drive file of every ad that was ACTIVE on 2026-10-18 and has a same-name file in Drive, one subfolder per ad set (named exactly like the ad set) with Images/Videos inside. Ad sets 80–87 are not repeated here; they live in "Meta ad sets 80-87".

- 21 ad sets (56, 57, 59–64, 67, 68–79), 302 active ads, 301 files (two ads in 67 share one file). Verified by listing: 301/301 in the right folder.
- 176 files were moved. 125 could not be moved (owned by editor accounts such as maxi10105c@gmail.com), so a same-name copy was put in the ad set folder and the original stayed put: all files for ad sets 56, 57, 59, 60, 61, 62, 63.
- Choices: ad set 62 "LastDayofCrazyPriceDrop" and "ReverseAging" exist in several folders; the `.Corrected Creatives` versions were used. In folder 45, names that differ only by one vs two spaces were matched exactly to the ad name.
- Not in Drive at all (210 active ads): ad sets 66 and part of 67 (AI statics with descriptive names), 55–58 generic names, a few older ones. 173 are images (downloadable from Meta), 15 videos (no download link from Meta), 22 other formats.
- Gallery page for the 173 image ads (2026-10-18): https://claude.ai/artifact/9DCjbJiNjvi7uGjeAGVgdT (private). Images downloaded from Meta (`image_url` on each creative; 170 distinct images, 3 shared by more than one ad), grouped by ad set, each with headline, primary text, ad ID and an Ads Manager link. The 15 video and 22 other-format ads are listed at the bottom with Ads Manager links. Meta returns no `download_hd_url` for those videos.
