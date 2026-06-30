# Welcome Newsletter — NMN (New Customer Spotlight)

A warm, premium **welcome email** for new Prime Ingredients subscribers, built around the
flagship SKU, **NMN (β-Nicotinamide Mononucleotide), 1,000 mg · Ultimate 10-in-1**. The layout
recreates the supplied NMN promo graphic — violet product label, three benefit callouts, warm
backdrop — rebuilt as a compliant, email-client-safe HTML newsletter with a "glad you're here"
welcome vibe.

## Files
- `email.html` — responsive, self-contained HTML email source (mirror this into the Klaviyo template).

## Look & feel
- **Palette:** brand violet `#6D388B` / deep violet `#4A2660`, warm cream + sand canvas
  (`#FFFDFA`, `#F2E6D4`, `#E9DDCE`), gold accent `#C99A3F`, ink `#33203F`. Warm-toned throughout
  to match the "welcome / new customer" brief.
- **Fonts (premium):** `Playfair Display` (elegant serif) for headlines + `Montserrat` for body,
  loaded as progressive enhancement. Email clients that block web fonts fall back cleanly to
  `Georgia` (serif) and `Helvetica/Arial` (sans) — both already premium-feeling.
- **Structure:** trust bar → wordmark → welcome hero → NMN product spotlight (CSS-rendered label
  + 3 benefit pills) → "Why 50+ make it a habit" checklist → "The science, simply" card →
  3-step how-to → 30-day guarantee → social proof → final CTA → footer. One product, one PDP,
  every CTA → `tryprimeingredients.com/products/nmn`.

## Adjustments made from the base graphic (brand & compliance)
The supplied image was adapted to Prime Ingredients' brand rules (see `references/brand.md` in the
Klaviyo newsletter skill):
- **Removed "BUY 1, GET 1 FREE."** The list is auto-subscribed and the brand has a hard
  **no-discounts / no-offers** rule. The **30-day money-back guarantee** is the trust lever instead.
- **Softened the claims.** "Ultimate anti-aging supplement," "promotes longevity," and
  "rejuvenation in a bottle" were reframed as compliant **structure/function** language
  ("supports healthy aging," "supports healthy NAD+ levels," "NMN is the precursor your cells use
  to make more NAD+"). The three callouts became "Supports healthy aging," "Cellular &
  mitochondrial support," and "Immune health & recovery support."
- **No invented stats.** The science card explains NAD+ decline qualitatively — no percentages or
  clinical numbers.
- **Footer** = "you subscribed at…" line + unsubscribe only. No postal address, no FDA disclaimer,
  no legal-entity name (per brand rule).

## Suggested subject + preheader (brand name kept out of the subject)
- **Subject:** `Welcome — your healthiest years start here`
- **Preheader:** `So glad you're here. Meet the molecule behind healthy aging.`

## Before sending — checklist
1. **Verify the From address** in Klaviyo — pull the verified `default_sender_email` live
   (`get_account_details`); do not hardcode. `from_label` / footer show **Prime Ingredients** only.
2. **Drop in the real hosted assets.** The header/footer wordmark and the product label are rendered
   in HTML/CSS so the file has **no external image dependencies** (nothing to break). For the final
   send, swap in the **real hosted logo image** and a **hosted NMN bottle photo** (Klaviyo
   `upload_image_from_url`) — the brand prefers the real logo over a text wordmark.
3. **Swap the testimonials.** Carol M. / Dianne R. quotes are illustrative placeholders — replace
   with real verified reviews before sending.
4. **Send a test** to yourself; check desktop + mobile (Gmail, Apple Mail, Outlook), then
   schedule for the **12:00 PM America/New_York** anchor slot.
