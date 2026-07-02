# Fourth of July Newsletter — NMN

A compact, mobile-first Fourth-of-July newsletter (v2, reworked to the brand
kit in the uploaded zip): real Prime Ingredients logo, GIF as the hero on a
navy band, three quick benefit checks, the artwork mid-email on warm cream,
one review + 30-day guarantee block, final CTA, short footer. Palette is
"heritage Americana" — deep navy, flag red, warm cream/parchment, antique
gold, with thin red/gold flag-ribbon stripes as accents. No postal address in
the footer and benefit-style CTA labels, per the brand rules in the zip.

**Nothing has been sent or pushed to Klaviyo.** Paste it yourself when ready.

## Files
- `email.html` — the complete email. Paste into Klaviyo's **HTML/code editor**
  (not drag-and-drop).
- `make-gif.sh` — ffmpeg script that converts the provided video into an
  email-friendly GIF (`july4.gif`).

## Links (already wired in)
- **The entire featured image** is wrapped in a single link →
  `https://tryprimeingredients.com/products/nmn` (a tap anywhere opens the NMN
  page; single wrapping links work in every client, unlike image maps).
- The **GIF** is wrapped in the same link.
- **Shop NMN** buttons (hero + final CTA) → `/products/nmn`.
- Footer: store links, Klaviyo `{% unsubscribe %}`, and
  `{{ organization.name }}` / `{{ organization.full_address }}` (auto-filled by
  Klaviyo — needed for CAN-SPAM).

## The image
The featured artwork is referenced directly from its Klaviyo CDN URL
(`.../5e3bff10-7322-41f8-a800-d95e2d2e5c01.jpeg`), used as-is at 600px wide,
scaling to 100% on phones.

## The GIF ✅
The video was converted to a GIF and uploaded to Klaviyo; the email now
references its hosted URL
(`.../610bbaef-832b-4a25-a5ae-41766dbf13f2.gif`) in the "See it in motion"
section, wrapped in the same NMN product link as the artwork. Note: Outlook
desktop shows only the GIF's first frame, which is normal and acceptable.
`make-gif.sh` is kept in case the GIF ever needs re-encoding (e.g. smaller size).

## Send settings (when you give the signal)
- **Subject:** `Happy 4th — light up your summer 🎆`
- **Preview text:** `Independence from slowing down — cellular energy for the long weekend.`

| Angle | Subject | Preview text |
|---|---|---|
| Short/mobile | `Happy Fourth 🇺🇸` | `Freedom feels like energy. Meet NMN.` |
| Product hook | `Sparks outside. Energy inside.` | `NMN — 1,000 mg of cellular support per serving.` |
| Risk-reversal | `A risk-free Fourth of July` | `Try NMN for 30 days, backed by our guarantee.` |

## Pre-send checklist
- [ ] Paste `email.html` into Klaviyo's HTML/code editor.
- [ ] Set subject + preview text.
- [ ] Send a test; check mobile: image fills the width, tap anywhere on the
      artwork/GIF opens the NMN page, GIF animates (Gmail/Apple Mail).
- [ ] Confirm unsubscribe + organization address render.
- [ ] Wait for the go signal, then pick audience and send time.

## Note on offers
No discount or promo code was added, since none was specified. If the artwork
itself announces an offer (e.g. a July 4th sale), say the word and the copy/CTAs
can be updated to match it.
