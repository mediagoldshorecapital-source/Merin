# Send settings — NMN Welcome email

Fill these into Klaviyo when building the campaign/flow email.

## Subject line + preview text (mobile-optimized)
Keep the subject under ~40 characters so it doesn't truncate on phones, and always
set the preview text separately (don't leave it blank, or clients pull the image alt).

**Recommended:**
- **Subject:** `So glad you're here 💜`
- **Preview text:** `Meet NMN — cellular energy in one capsule, risk-free for 30 days.`

Mirrors the hero headline (consistency lifts opens), stays welcoming, and the
preview does the product + risk-reversal selling.

### Alternatives
| Angle | Subject | Preview text |
|---|---|---|
| Warm welcome | `Welcome to the family 💜` | `You're in — here's where it begins.` |
| Short/mobile | `You're in 💜` | `Meet NMN: cellular energy in a single capsule.` |
| Product hook | `NMN: energy in a single capsule` | `NAD+ powers nearly every cell — here's the clean daily source.` |
| Risk-reversal | `Your risk-free welcome to NMN` | `Try it 30 days, backed by our money-back guarantee.` |

Tip: emoji (💜 fits the purple brand) can lift opens with some audiences and hurt with
others — A/B test the subject with and without it.

## From name / from email
- Suggested **From name:** Prime Ingredients
- **From email / reply-to:** your verified Klaviyo sending address.

## Links (already in the HTML)
- Whole image + Shop NMN button → https://tryprimeingredients.com/products/nmn
- Footer: tryprimeingredients.com, Visit our store → https://tryprimeingredients.com
- Unsubscribe → Klaviyo `{% unsubscribe %}`

## Pre-send checklist
- [ ] Paste `email.html` into Klaviyo's HTML/code editor (not drag-and-drop).
- [ ] Set subject + preview text above.
- [ ] Send a test; check mobile (iOS Mail + Gmail app): image fills screen, no
      horizontal scroll, tap opens the NMN product page.
- [ ] Confirm the org name/address + unsubscribe render correctly.
- [ ] Pick the audience (list/segment) and send time.
