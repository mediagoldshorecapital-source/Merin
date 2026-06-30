# NMN Welcome Newsletter — Clickable Hero Image

A single, full-length hero image ("So glad you're here") turned into a clickable
email via an HTML image map. **The image is used exactly as provided and is not
altered, sliced, or regenerated.**

## Files
- `email.html` — email-safe HTML: one `<img>` plus a `<map>` with clickable hotspots.

## Image
- Source (hosted, used as-is): `https://d3k81ch9hvuctc.cloudfront.net/company/XTxzmw/images/2355ef42-ae0c-46f3-a2f4-055652f11596.png`
- Displayed at **600px** wide (standard email content width).

## Hotspots (confirmed)
| Region in image | Destination |
|---|---|
| "DISCOVER NMN →" button | https://tryprimeingredients.com/products/nmn |
| "START YOUR ROUTINE" button | https://tryprimeingredients.com/products/nmn |

Both CTA buttons link to the same NMN product page.

## Not yet linked (pending confirmation)
The footer links shown in the image — `tryprimeingredients.com`, "Visit our
store", and "Unsubscribe" — are **not** linked yet. Say the word and I'll add
them (e.g. site/store → homepage, Unsubscribe → Klaviyo `{% unsubscribe %}` tag).
A linked unsubscribe is typically required for compliance, so confirm how you
want to handle it before sending.

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
