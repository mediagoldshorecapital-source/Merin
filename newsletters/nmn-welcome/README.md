# First Newsletter — NMN Welcome ("Meet NMN")

Prime Ingredients' welcome newsletter introducing the flagship product **NMN**
(Nicotinamide Mononucleotide). A warm, premium *designed* email that teaches the
NAD+ → NMN mechanism, leans on the **30-day money-back guarantee** (no discounts),
and sends readers to the NMN product page. Built per the bundled
`klaviyo-newsletter` blueprint and set up as a **draft** campaign in Klaviyo
(nothing is scheduled or sent until a human confirms in the wizard).

Product: https://tryprimeingredients.com/products/nmn

## Klaviyo (sendable draft — DRAFT only, NOT sent)
- Campaign: **NMN Welcome — Meet NMN (2026-07-01)** (`01KW9NJQ64EV43WSPAS03WTYB5`)
  - Review, edit & schedule (1 click): https://www.klaviyo.com/campaign/01KW9NJQ64EV43WSPAS03WTYB5/wizard
- Template (`Sq6nDd`): https://www.klaviyo.com/email-editor/Sq6nDd/edit
  - (Assigning to the campaign cloned it to `R8CxhN` "Clone of Sq6nDd" — the clone is
    what the campaign renders; edit it through the wizard, not the library template.)
- Audience: **Email List** (`Uisyj7`)  ·  Excluded: none
- Subject: `Meet The Molecule Behind Your Energy`
- Preview text: `NAD+ fuels your cells and naturally dips with age — NMN is the precursor that helps.`
- From: `Prime Ingredients <support@tryprimeingredients.com>` (verified account sender)
- Send time (pre-filled, fixed): **Wed Jul 1, 2026, 12:00 PM America/New_York** = `2026-07-01T16:00:00+00:00`

## Design / illustrations
- **Hero** (`assets/hero.png`) and **molecule band** (`assets/molecule-band.png`) are
  hand-authored flat-vector illustrations in the warm Prime Ingredients palette —
  cream `#F4E8DE`, maroon `#8A2A33`, gold `#C99A3F`, charcoal `#2A2A33`. Source SVG +
  re-render script live in `assets/src/` (`render.sh`).
- Hosted copies (used by the Klaviyo template) live on Klaviyo's image CDN:
  - hero: `…/images/a97a9416-118e-496e-ba06-2feb8e432a6c.png`
  - band: `…/images/9bb85d99-7e5c-48ed-bd0c-ef5e718186c6.png`
- Editable **Canva** design (artwork): see "Canva" below.
- Note: Canva's *AI design generation* was unavailable this session (account quota
  reached), so the illustrations were produced as bespoke vector art instead — which
  also keeps tighter control of the "premium, warm, lightly-illustrated" brief.

## Files
- `email.html` — the responsive HTML email (mirrors the Klaviyo template `Sq6nDd`).
- `assets/hero.png`, `assets/molecule-band.png` — final illustrations.
- `assets/src/*.svg.html`, `assets/src/render.sh` — illustration source + renderer.

## Compliance (baked in, per blueprint)
- Structure/function claims only ("supports healthy NAD+ levels", "helps maintain",
  "supports normal metabolism") — no treat/cure/prevent/reverse, no "anti-aging" promise.
- No invented stats/percentages. No discounts or subscription offers (auto-subscribed list).
- Footer = "you subscribed" line + `{% unsubscribe %}` only — no postal address,
  no FDA disclaimer (email, not label).

## Before sending — checklist
1. Open the **wizard link** above; confirm the **audience** (defaulted to the whole
   Email List — switch to an engaged segment, e.g. `Engaged (30 Days)` `W2fbuc`, if you
   prefer to protect deliverability) and the **send time**.
2. Send a **test** to yourself; check desktop + mobile (hero, band, both CTAs, unsubscribe).
3. Click **Schedule** (or Send). The MCP intentionally leaves it one click short.
