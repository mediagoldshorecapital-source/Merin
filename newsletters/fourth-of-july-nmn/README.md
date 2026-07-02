# Fourth of July Newsletter — NMN

A full, designed newsletter (same structure as the welcome NMN email: trust bar,
wordmark, hero, benefits, science card, animated section, how-to, guarantee,
reviews, final CTA, footer) in a Fourth-of-July palette — deep navy, flag red,
cream, and the brand's gold. The featured artwork and the GIF sit edge-to-edge
on navy bands so they blend into the design instead of floating like attachments.

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

## The GIF — one step left ⚠️
The video (`.../01KWHNTPHZANKJTDAXM70HXWR7.mp4`) could not be downloaded from
inside this coding session: the session's network policy blocks
`d3k81ch9hvuctc.cloudfront.net` (Klaviyo's CDN). Two ways to finish:

1. **Let the session do it** — in the Claude Code environment settings, set the
   network policy to allow that domain (or "all"), then say "convert the gif".
   ffmpeg is already installed and `make-gif.sh` is ready.
2. **Do it locally** — run `./make-gif.sh` on any machine with ffmpeg
   (or use ezgif.com: ~12 fps, 552px wide, loop forever).

Then upload `july4.gif` to Klaviyo (**Content → Images**), copy the hosted URL,
and in `email.html` replace the placeholder `REPLACE-WITH-KLAVIYO-GIF-URL/july4.gif`
(it's clearly marked with a `GIF SLOT` comment). Keep the GIF under ~3 MB;
Outlook desktop shows only its first frame, which is normal and acceptable.

## Send settings (when you give the signal)
- **Subject:** `Happy 4th — light up your summer 🎆`
- **Preview text:** `Independence from slowing down — cellular energy for the long weekend.`

| Angle | Subject | Preview text |
|---|---|---|
| Short/mobile | `Happy Fourth 🇺🇸` | `Freedom feels like energy. Meet NMN.` |
| Product hook | `Sparks outside. Energy inside.` | `NMN — 1,000 mg of cellular support per serving.` |
| Risk-reversal | `A risk-free Fourth of July` | `Try NMN for 30 days, backed by our guarantee.` |

## Pre-send checklist
- [ ] Convert the video → `july4.gif`, upload to Klaviyo, replace the GIF slot URL.
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
