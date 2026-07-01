# NMN Welcome Newsletter — Clickable Hero Image

A single, full-length hero image ("So glad you're here") turned into a clickable
email via an HTML image map. **The image is used exactly as provided and is not
altered, sliced, or regenerated.**

## Files
- `email.html` — email-safe HTML: one `<img>` plus a `<map>` with clickable hotspots.

## Image
- Source (hosted, used as-is): `https://d3k81ch9hvuctc.cloudfront.net/company/XTxzmw/images/2355ef42-ae0c-46f3-a2f4-055652f11596.png`
- Intrinsic size: **1360 × 5948 px**. Displayed at **600px** wide (scales to ~2624px tall).
- Image-map hotspot coordinates are calibrated to the **intrinsic 1360 × 5948** space.

## Hotspots (confirmed)
| Region in image | Destination |
|---|---|
| "DISCOVER NMN →" button | https://tryprimeingredients.com/products/nmn |
| "START YOUR ROUTINE" button | https://tryprimeingredients.com/products/nmn |

Both CTA buttons link to the same NMN product page.

## Bulletproof CTA button (below the image)
A live-text **"Shop NMN"** button → https://tryprimeingredients.com/products/nmn
is rendered below the image. It uses VML for Outlook desktop, so the call-to-action
is clickable in **every** client even though Outlook ignores the on-image hotspots.

## Footer (live text, below the image)
A small live-text footer is rendered **below** the image so these work in every
client (including Outlook, which ignores image maps):
- **tryprimeingredients.com** → https://tryprimeingredients.com
- **Visit our store** → https://tryprimeingredients.com
- **Unsubscribe** → Klaviyo `{% unsubscribe %}` tag (required for compliance)
- Physical address → Klaviyo `{{ organization.name }}` / `{{ organization.full_address }}`
  (auto-filled from your Klaviyo account settings — needed for CAN-SPAM)

The footer links were deliberately **not** placed as in-image hotspots: the
footer is a single line of three small links, so image-map coordinates there
would be imprecise and could mis-route an unsubscribe click to the store. The
live-text footer is the reliable, compliant approach.

## Known limitations of image maps in email
- Coordinates are **fixed pixels**, calibrated to the 600px width. They are not
  responsive — if a client rescales the image (common on mobile), hotspots can
  drift.
- **Outlook desktop** ignores image maps entirely (the image shows but isn't
  clickable).
- Hotspot vertical positions were estimated because the source host is blocked
  in this environment (couldn't auto-measure the file). If a button click misses,
  the `coords` in `email.html` may need a small nudge.

## Klaviyo
Nothing has been pushed to Klaviyo. Ask before importing/sending.
