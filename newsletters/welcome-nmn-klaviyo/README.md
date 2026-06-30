# Welcome Email — Meet NMN

Prime Ingredients' welcome email for new subscribers, spotlighting the flagship
**NMN (Nicotinamide Mononucleotide) — Ultimate 10-in-1, 1,000 mg**. A warm "so glad
you're here" welcome that introduces the brand, explains NAD+ in plain language, and
points to the NMN product page. Built on-brand in a violet/purple palette.

## Klaviyo (CODE template)
- Template: **NMN Welcome — So Glad You're Here (violet, 2026-06-30)** (`TBHuLK`)
  - Edit: https://www.klaviyo.com/email-editor/TBHuLK/edit
- Subject (suggested): `So glad you're here ✨ Meet NMN`
- Preview text (suggested): `One clean capsule for the energy inside every cell.`
- Account: Prime Ingredients (`XTxzmw`), sender `support@tryprimeingredients.com`

## Files
- `email.html` — responsive HTML email source (mirrors the Klaviyo template).

## Hero image
- Source provided by the brand: `https://kommodo.ai/i/A1Dal7I67rEondFWM6nN`
  (woman holding the NMN bottle — lifestyle photo). This is wired into the hero
  `<img src>` in `email.html`.
- Note: the `kommodo.ai/i/...` link is a share/viewer URL. Klaviyo's image importer
  and Canva both fetched it server-side and could **not** decode it as a raw
  JPEG/PNG/GIF, so it could not be re-hosted on Klaviyo's CDN automatically.
  It does render as an image in a browser/email-client render (see preview).
  **Before sending, do a test send and confirm the hero displays across clients**
  (notably Outlook desktop). If any client shows a broken image, re-host the photo:
  save it as a PNG/JPEG and upload via Klaviyo's image library, then swap the src.
- Previous Klaviyo-hosted hero (working fallback if needed):
  `https://d3k81ch9hvuctc.cloudfront.net/company/XTxzmw/images/98a8252b-1ba7-4f65-834d-bbf097cefd2e.png`

## Before sending — checklist
1. **Push the hero src to the live Klaviyo template.** `email.html` here is the
   source of truth; mirror the hero `<img src>` into template `TBHuLK` in Klaviyo
   (this repo update was made while the Klaviyo connection was down).
2. **Verify the From address / sending domain** is set on a verified domain.
3. **Confirm the NMN PDP URL.** All CTAs point to
   `https://tryprimeingredients.com/products/nmn` — update if the live handle differs.
4. **Swap testimonials for real, verified reviews** (Carol M. / Dianne R. are
   illustrative placeholders).
5. **Send a test**, review desktop + mobile, then add to the welcome flow / schedule.

## Notes / approach
- Palette: deep violet `#4A2463`, primary purple `#6D388B`, lilac wash `#F5F1F8`/`#F1EAF7`,
  page background `#ECE4F1`, gold stars `#C99A3F`.
- Type: Georgia serif headlines + Montserrat/Helvetica body.
- Claims are kept to structure/function language ("supports", "helps maintain") to
  stay compliant; no disease claims.
- Could fit Klaviyo's "Test Welcome Series - Standard" flow (`U85zrU`, Added-to-List
  trigger, currently draft) as the first message.
