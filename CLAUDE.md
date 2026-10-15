# Prime Ingredients

## Meta Ads account

When the user says "Prime Ingredients" or "Daily Prime Ingredients", use this Meta ad account:

- Ad account name: `Shopify: w1rbg9wu 1767817097 business's ad account`
- Ad account ID: `2009539369903270`
- Owning business: Olia Zakharovas (business ID `3084997128375299`)
- Currency: USD

Don't ask which account to use. Use this one unless the user says otherwise.

## Never touch any other ad account

Prime Ingredients (`2009539369903270`) is the ONLY Meta ad account you may use. Never read from, query, change, create anything in, or run any tool against any other ad account the Meta connector can see. This covers:

- Isha 925 Silver Jewellery (`475547324887973`)
- ishaasilver (`1268009838440094`)
- `1361699501690893`
- Hand of growth (`740061042040715`)
- HOG Ads Acc (`2931123823758160`)
- Metrocode ads (`1013522877268855`)
- Clipston Lifts and Escalators Contracting (`1347305866989905`)
- Thaalio Foods (`862162773497143`)
- Any other account that shows up later

If a request seems to need another account, stop and ask the user. Don't act.

## Ad-building playbook

Before creating Prime Ingredients ads, read `meta-ads-playbook.md` and follow its structure.

## Core rules for every Prime Ingredients ad (from the user, 2026-10-15)

Apply these to every ad you create or rebuild. They override any default.

- **Creative setup: all OFF.** In Ads Manager, "Creative setup" means Site links, Products (catalog), Website summaries and 2 more. Everything has to be off. When these are on they break the funnel and waste money. Never connect a catalog.
- **Advantage+ / creative enhancements: all OFF**, with these exceptions that stay **ON**:
  - Enhance CTA
  - Multi-advertiser ads
  - Add music, on statics only (see below)
- **URL parameters on every ad** (`url_tags`): `utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&tw_source={{site_source_name}}&tw_adid={{ad.id}}`
- **Destination:** `https://tryprimeingredients.com/products/nmn`, Shop Now, display link `Primeingredients.com`.
- **Spec to put on every creative.** Don't include `standard_enhancements`; the API rejects it.
  - `"contextual_multi_ads":{"enroll_status":"OPT_IN"}`
  - `"degrees_of_freedom_spec":{"creative_features_spec":{` with:
    - `"enhance_cta":{"enroll_status":"OPT_IN"}`
    - `OPT_OUT` for each of: `site_extensions`, `product_extensions`, `show_summary`, `local_store_extension`, `profile_card`, `image_touchups`, `text_optimizations`, `image_templates`, `adapt_to_placement`, `inline_comment`, `image_animation`, `add_text_overlay`, `description_automation`, `image_brightness_and_contrast`, `image_uncrop`, `audio`, `video_auto_crop`, `media_type_automation`, `show_destination_blurbs`, `reveal_details_over_time`, `text_translation`
  - Tested and accepted by the API on 2026-10-15.
- **Add music: ON for statics only.** On static image ads, set `"audio":{"enroll_status":"OPT_IN"}` (Meta's "Add music" enhancement). On video ads, keep `audio` as `OPT_OUT`. Accepted by the API on 2026-10-15.
- **Can't be set by the connector:** WhatsApp = "Use Facebook Page". Remind the user to bulk-edit it after every build.
