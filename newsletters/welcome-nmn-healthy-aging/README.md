# Welcome Email — Your Healthy Aging Era (NMN)

Prime Ingredients' welcome / onboarding email for new subscribers, built around the
hero SKU **NMN Ultimate 10-in-1 (1,000mg)**. Uses the **exact design artwork** (hosted
on Klaviyo's CDN) as the visual, with the pieces that must be live layered on top:
Klaviyo tags, a **click-to-copy PRIME10** code, social links, unsubscribe / manage
preferences, and a view-in-browser web page.

## Design artwork
The email renders the finished design as a single hosted image:
`https://d3k81ch9hvuctc.cloudfront.net/company/U8pRQr/images/b924903e-211e-4ad8-9267-4a430ce4988f.png`
(Klaviyo company `U8pRQr`). Tapping the artwork opens the store with PRIME10 applied.

## Files
- `email.html` — Klaviyo email. Design image + a **live** welcome-gift band (PRIME10 +
  "Shop with PRIME10") + a **live** footer (social, unsubscribe, manage preferences,
  address, disclaimer). No JavaScript — email clients strip it.
- `landing.html` — the **web page / view-in-browser** version. Same layout, but the
  PRIME10 code is a real **click-to-copy** button (clipboard + fallback, "Copied!"
  state + toast). Point the email's web-view link here for true copy-on-click.

## The PRIME10 code — how "copy on click" works
Email clients (Gmail, Apple Mail, Outlook) **do not run JavaScript**, so a click can't
copy to the clipboard *inside the email itself*. It's handled two ways:
1. **In the email (`email.html`)** — the code and "Shop with PRIME10" button link to
   `https://tryprimeingredients.com/discount/PRIME10`; Shopify auto-applies the 10% off,
   no manual entry. The code also links to the web view where copy works.
2. **On the web page (`landing.html`)** — clicking `PRIME10` copies it to the clipboard
   (`navigator.clipboard` with an `execCommand` fallback), flips the chip to a green
   "Copied!" state, and fires a toast. Verified with a headless browser.

## Why some elements are "live" over the image
An all-image email can't have a working unsubscribe, a copyable code, or accessible
links — and a live **unsubscribe** is legally required (CAN-SPAM). So the artwork carries
the look, and these sit as real HTML beneath it:
- Personalization-ready footer, `{% unsubscribe %}`, `{% manage_preferences %}`
- `{% web_view %}` (view in browser) at the top
- `{{ organization.name }}` / `{{ organization.full_address }}` (CAN-SPAM address)
- Social links (Instagram, Facebook, email)
- Copyable PRIME10 + apply-discount button

> If your artwork already includes a footer/social/unsubscribe row, crop it off the
> image so it isn't duplicated by the live footer — the live one is the one that must
> function.

## Before sending — checklist
1. **Verify the From address** on a verified sending domain in Klaviyo.
2. **Confirm the artwork URL** renders (it's blocked in the dev sandbox but public on the
   CDN). Add a taller `width`/`height`-free `<img>` if you swap it for a different export.
3. **Confirm the PRIME10 discount exists** in Shopify and `/discount/PRIME10` auto-applies.
4. **Update social handles + company address** (address is placeholder copy).
5. **Send a test** to yourself; check desktop + mobile, then schedule/send.

## Notes
- Palette: purple `#6D4C9F` / plum `#7E64AB`, lavender `#E9DFF4` / `#EFE6F9`, gold `#C6A24E`.
- `landing.html` uses plain `{unsubscribe_url}` / `{manage_preferences_url}` placeholders
  since a hosted page renders outside Klaviyo's tag engine — swap for real links.
