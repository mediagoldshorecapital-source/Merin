# NMN Welcome Newsletter — Clickable Hero Image

A single, full-length hero image ("So glad you're here") turned into a clickable
email via an HTML image map. **The image is used exactly as provided and is not
altered, sliced, or regenerated.**

## Files
- `email.html` — email-safe HTML: one `<img>` plus a `<map>` with clickable hotspots.

## Image
- Source (hosted, used as-is): `https://d3k81ch9hvuctc.cloudfront.net/company/XTxzmw/images/2355ef42-ae0c-46f3-a2f4-055652f11596.png`
- Intrinsic size: **1360 × 5948 px**. Displayed at **600px** wide on desktop.

## Mobile / responsive
Fluid-hybrid layout: fixed **600px** on desktop and Outlook, but the image, button,
and footer scale to **100% of the screen width** on phones (no horizontal scroll or
pinch-to-zoom). This is done with `width:100%;max-width:600px;height:auto` on the
image + containers, plus a `@media (max-width:600px)` block that also bumps the
footer text to 13px for readability. Requires the `<meta name="viewport">` tag
(included).

## Link behavior
The **entire image** is wrapped in a single link to **https://tryprimeingredients.com**,
so a click anywhere on it opens the website. A single wrapping link is reliable in
every email client (Apple Mail, Gmail, Outlook, mobile) — unlike HTML image maps,
which Outlook desktop and much of Gmail strip.

The reinforcing **"Shop NMN" button** below the image points to the NMN product page
(`/products/nmn`).

### Why not exclude the header/footer inside the image?
The newsletter is one flat image. Carving out clickable sub-regions requires an HTML
image map (unreliable — stripped by Outlook/Gmail) or slicing the image (declined).
The functional footer (store link, unsubscribe, address) is therefore rendered as
**live text below the image** and is NOT part of the image link, so an unsubscribe
click is never redirected to the site.

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

## History
Earlier versions used an HTML image map to make individual on-image buttons
clickable. Those proved unreliable (Outlook/Gmail strip image maps), so the design
was switched to a single wrapping link over the whole image, which works everywhere.

## Klaviyo
Nothing has been pushed to Klaviyo. Ask before importing/sending.
