# NMN Welcome — "So glad you're here" (violet)

Hyperlinked, email-safe HTML reproduction of the violet NMN welcome design
(the attached mockup). Visual layout/copy match the image; the only work added
here is **working hyperlinks** + a Klaviyo-ready, deliverability-safe build.

## Klaviyo
- Template (`TBHuLK`): **NMN Welcome — So Glad You're Here (violet, 2026-06-30)**
  - Edit/preview: https://www.klaviyo.com/email-editor/TBHuLK/edit
- Editor type: `CODE` (hand-written, table-based, 600px, inline styles, Outlook-safe).
- Not attached to a campaign — this is the newsletter template only.

## Links wired (every clickable element)
| Element | Destination |
| --- | --- |
| Header logo | `https://tryprimeingredients.com` |
| Hero image | `https://tryprimeingredients.com/products/nmn` |
| **DISCOVER NMN →** button | `https://tryprimeingredients.com/products/nmn` |
| **START YOUR ROUTINE** button | `https://tryprimeingredients.com/products/nmn` |
| Footer logo | `https://tryprimeingredients.com` |
| `tryprimeingredients.com` (footer text) | `https://tryprimeingredients.com` |
| **Visit our store** | `https://tryprimeingredients.com` |
| **Unsubscribe** | `{% unsubscribe 'Unsubscribe' %}` (Klaviyo live unsubscribe — verified it renders to a real `<a href>`) |

## Hero image — action needed
The lifestyle hero (woman holding the NMN bottle + the 3 feature pills) wasn't
in the Klaviyo asset library, so the `<img>` currently points at a temporary
on-brand stand-in (`98a8252b…png`). To match the mockup exactly:
1. Upload your hero photo in Klaviyo (or send a public URL).
2. Replace the `src` on the `<!-- HERO IMAGE -->` `<img>` (keep its `href` to the PDP).

The 3 feature pills + intro sit as live HTML directly beneath the hero, so they
stay editable and don't need to be baked into the photo.

## Notes
- Palette: violet `#6D388B`, deep plum `#4A2463`, lavender tint `#F5F1F8/#F1EAF7`,
  ink `#2A2A33`, gold stars `#C99A3F` — per `references/brand.md`.
- Display headings use Georgia (serif) to match the mockup; eyebrows/body/buttons
  use the Montserrat→Helvetica→Arial stack.
- Footer carries no postal address and no FDA disclaimer (per brand rule).
