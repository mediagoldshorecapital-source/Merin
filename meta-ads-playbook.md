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
  - Headline: `Support Energy Without More Coffee`
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
