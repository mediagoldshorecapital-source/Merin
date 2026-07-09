# Welcome Email — Your Healthy Aging Era (NMN)

Prime Ingredients' welcome / onboarding email for new subscribers, built around the
hero SKU **NMN Ultimate 10-in-1 (1,000mg)**. Same purple "Healthy Aging Era" design as
the mockup, now production-ready with Klaviyo tags, social links, unsubscribe / manage
preferences, a view-in-browser web page, and a **click-to-copy PRIME10** code.

## Files
- `email.html` — responsive HTML email source (Klaviyo template). Table-based, inline
  styles, no JavaScript (email clients strip it). The PRIME10 block links to the
  Shopify auto-apply URL so the code is applied on click.
- `landing.html` — the **web page / view-in-browser** version. Same design, but the
  PRIME10 code is a real **click-to-copy** button (writes to clipboard, shows a
  "Copied!" confirmation + toast). Host this and point the email's web-view / code link
  at it if you want true copy-on-click.

## The PRIME10 code — how "copy on click" works
Email clients (Gmail, Apple Mail, Outlook) **do not run JavaScript**, so clipboard copy
cannot happen inside the email itself. It's delivered two ways:
1. **In the email (`email.html`)** — the code and the "Shop with PRIME10" button link to
   `https://tryprimeingredients.com/discount/PRIME10`. Shopify auto-applies the discount
   and drops the shopper into the store with 10% off already active — no manual entry.
2. **On the web page (`landing.html`)** — clicking the `PRIME10` chip copies the code to
   the clipboard (`navigator.clipboard` with an `execCommand` fallback), flips the chip
   to a green "Copied!" state, and fires a toast. Verified with a headless browser.

## Klaviyo features included (in `email.html`)
- **Personalization:** `{{ first_name|default:'there' }}` in the welcome line.
- **View in browser:** `{% web_view 'View this email in your browser' %}` at the top.
- **Unsubscribe:** `{% unsubscribe 'Unsubscribe' %}` in the footer (required).
- **Manage preferences:** `{% manage_preferences 'Manage preferences' %}`.
- **Company address (CAN-SPAM):** `{{ organization.name }}` / `{{ organization.full_address }}`.
- **Preheader / preview text** hidden at the top of the body.

> Note: `landing.html` uses plain `{unsubscribe_url}` / `{manage_preferences_url}`
> placeholders since a hosted web page renders outside Klaviyo's tag engine — swap for
> real links (or your ESP's tags) when you host it.

## Social media
Footer icons link to Instagram, Facebook, and email. Update the handles/URLs:
- Instagram: `https://www.instagram.com/tryprimeingredients`
- Facebook: `https://www.facebook.com/tryprimeingredients`
- Email: `hello@tryprimeingredients.com`

## Before sending — checklist
1. **Verify the From address** on a verified sending domain in Klaviyo.
2. **Drop in the Canva hero image.** Both files have a `[ NMN … hero image ]` placeholder
   where the woman + NMN bottle lifestyle image goes (keep width 600).
3. **Confirm the PRIME10 discount exists** in Shopify and that
   `/discount/PRIME10` resolves and auto-applies.
4. **Update social handles + company address** (address is placeholder copy).
5. **Send a test** to yourself; check desktop + mobile, then schedule/send.

## Notes / approach
- Palette: purple `#6D4C9F` / plum `#7E64AB`, lavender `#EDE4F5` / `#F3ECFA`, gold accent
  `#C6A24E`, ink `#4A3F5C`. Serif = Georgia, sans = Helvetica/Arial.
- Feature/step icons are Unicode + CSS shapes (no image dependencies), matching the
  existing newsletter's approach. Swap for the Canva line icons if you prefer exact parity.
- Product claims (β-NMN, 10-in-1, NAD+ precursor, cGMP, non-GMO/vegan) mirror the mockup —
  verify against the live product page before sending.
