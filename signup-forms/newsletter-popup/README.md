# Newsletter Subscription Popup — Prime Ingredients

An on-brand **email capture popup** for building the newsletter list, designed to be
built **directly in Klaviyo's Sign-Up Forms editor**. It matches the Prime Ingredients
brand kit used in the first newsletter (forest / caramel / sand + Georgia + Helvetica).

> **Important — why this is a build kit, not a file you upload.**
> Klaviyo sign-up forms (popups) are **not creatable through the API or by pasting
> raw HTML**. Every popup is built in Klaviyo's drag-and-drop **Sign-Up Forms** editor.
> This kit gives you (1) a pixel-accurate preview to see and copy the design from, and
> (2) exact editor settings so you can reproduce it in Klaviyo in a few minutes.

## Files
- **`popup-preview.html`** — open in any browser to see the finished design. Includes
  Desktop/Mobile toggles and the Success state (buttons at the bottom are preview-only,
  not part of the Klaviyo form).
- **`custom-css.css`** — finishing-touch CSS to paste into the form's **Styles → Custom CSS**.
- **`README.md`** — this build guide.

---

## The design at a glance
A centered **two-column popup** on a dimmed overlay:

- **Left panel — forest `#2E3D31`:** brand wordmark, the offer (**15% off**), a one-line
  benefit, and a 5-star trust cue. Caramel glow accent.
- **Right panel — ivory `#FBF8F3`:** eyebrow "JOIN THE LIST", serif headline, one line of
  value copy, a single **email field**, a caramel **pill button** ("Claim my 15% off"),
  small consent line, and an understated **"No thanks"** decline link.
- **Success state:** forest checkmark, welcome message, and the discount code (`WELCOME15`).
- On mobile it **stacks** to a single column (offer on top, form below).

### Brand tokens
| Token | Hex | Use |
|---|---|---|
| Forest | `#2E3D31` | Left panel, headings, checkmark |
| Caramel | `#A9805A` | Button, accents, eyebrow |
| Caramel (hover) | `#946E4C` | Button hover |
| Sand | `#EFE9E0` | Page background |
| Ivory | `#FBF8F3` | Form panel background |
| Cream | `#F4EFE6` | Text on forest |
| Gold | `#C9B79C` | Secondary text on forest |
| Body text | `#5B5B52` | Paragraphs |
| Border | `#E4DCCD` | Input border / dividers |

Fonts: **Georgia** (serif) for headlines, **Helvetica/Arial** (sans) for body & button —
identical to `newsletters/first-newsletter-multi-collagen/email.html`.

---

## Step 1 — Create the list to collect subscribers
1. Klaviyo → **Audience → Lists & Segments → Create List / Segment → List**.
2. Name it **`Newsletter Subscribers`**. (Or reuse the existing **Email List** `Uisyj7`
   referenced in the first newsletter — but a dedicated newsletter list keeps reporting clean.)
3. Set **Single or Double opt-in** under the list's settings:
   - **Double opt-in** (recommended for a clean, engaged list + most compliant).
   - Single opt-in if you want the discount to arrive instantly with no confirm click.

## Step 2 — Create the form
1. Klaviyo → **Sign-Up Forms → Create Form → Create from scratch**.
2. Form type: **Popup**. Name it **`Newsletter Popup — Welcome 15%`**.
3. Under **behaviors / list**, point the form's submit action at **`Newsletter Subscribers`**.

## Step 3 — Build the layout (blocks)
Use a **two-column** row (Klaviyo: add a row → set to 2 columns, ~44% / 56% split).

**Left column (forest panel)** — set the *column* background to `#2E3D31`, padding ~44px:
- Text block (eyebrow): `PRIME INGREDIENTS CIRCLE` — Helvetica, 11px, letter-spacing 3px, color `#C9B79C`, uppercase.
- Text block (wordmark): `Prime Ingredients` — Georgia, 20px, letter-spacing 3px, uppercase, color `#F4EFE6`.
- Text block (offer): `15%` — Georgia, ~60px, color `#FFFFFF`; on the next line `off your first order` — Georgia, 26px, color `#F4EFE6`.
- Text block (benefit): `Plus clean, science-backed healthy-aging tips delivered to your inbox.` — 13px, color `#C9B79C`.
- Text block (trust): `★★★★★` in caramel `#A9805A`, then `Loved by our collagen community` — 12px, `#C9B79C`.

**Right column (form panel)** — column background `#FBF8F3`, padding ~46px:
- Text (eyebrow): `JOIN THE LIST` — 11px, letter-spacing 3px, uppercase, caramel `#A9805A`.
- Text (headline): `Unlock 15% off & healthy-aging tips` — Georgia, 30px, color `#2E3D31`.
- Text (value): `Be first to hear about new products, subscriber-only offers, and clean-living guides — and get 15% off to start.` — 14.5px, color `#5B5B52`.
- **Email input block**: placeholder `Enter your email address`; required.
- **Submit button**: label `CLAIM MY 15% OFF` — background `#A9805A`, text `#FFFFFF`,
  radius 30px (pill), uppercase, bold, letter-spacing 1.5px.
- Text (consent): `By subscribing you agree to receive marketing emails from Prime Ingredients. Unsubscribe anytime.` — 11.5px, color `#8B887E`. Link "Privacy Policy".
- (Optional) **Close / "No thanks" link** styled small and muted.

## Step 4 — Success step
Add/edit the form's **success step**:
- Heading: `You're in! Welcome to the Circle.` (Georgia, 28px, `#2E3D31`)
- Body: `Check your inbox to confirm and grab your discount. Use this code at checkout:`
- Discount code block: `WELCOME15` (dashed caramel border, cream background) — see preview.
> Create the coupon first in **Shopify → Discounts** (or Klaviyo coupons) as `WELCOME15`,
> then also deliver it in the welcome email (Step 7). Don't promise a code that doesn't exist.

## Step 5 — Styles & Custom CSS
1. In the form's **Styles** tab set the global corner radius, and the **overlay** to a dark
   scrim (`rgba(20,26,21,0.55)`).
2. Scroll to **Custom CSS** and paste the contents of **`custom-css.css`** for the pill
   button, focus ring, and input polish. Save.

## Step 6 — Targeting & behavior
- **Devices:** show on **Desktop and Mobile** (the design stacks cleanly).
- **Trigger:** *Show after 5 seconds* **or** *on 30% scroll* (whichever fires first is fine).
  Exit-intent is a good desktop alternative if you prefer to delay the interruption.
- **Do not show again** to someone who already submitted: enable **"Only show to people who
  are not already in the list"** and set **cookie / snooze** so dismissers aren't nagged
  (e.g. don't reshow for 14–30 days).
- **Frequency:** limit to one page-load session; respect the dismissal cookie.
- Leave the form **in Draft** while you test, then set **Live**.

## Step 7 — Connect the welcome email (so the discount actually sends)
1. Klaviyo → **Flows → Create Flow → From a template → "Welcome series" / "Sign-up"**.
2. Trigger: **When someone joins `Newsletter Subscribers`**.
3. Email 1 = welcome + the `WELCOME15` code. You can reuse the header/footer styling from
   `newsletters/first-newsletter-multi-collagen/email.html` for brand consistency.
4. Verify the **From address** is on a verified sending domain (the first newsletter still
   uses the placeholder `media.goldshorecapital@gmail.com` — fix before going live).

## Step 8 — Test, then publish
- Preview on desktop + mobile in Klaviyo.
- Submit a test email → confirm it lands in `Newsletter Subscribers` and the welcome flow fires.
- Set the form **Live**.

---

## Copy variants (swap without changing the layout)

**A) Newsletter value only — no discount** (protects margin)
- Left offer: replace `15% / off your first order` with `THE CIRCLE / for healthy-aging insiders`.
- Eyebrow: `JOIN THE CIRCLE`
- Headline: `Clean, essential solutions for healthy aging — delivered.`
- Value: `Science-backed tips, first looks at new products, and subscriber-only offers.`
- Button: `JOIN THE LIST`
- Success: `You're in! Welcome to the Circle.` (drop the code block)

**B) Free lead magnet**
- Left offer: `FREE / The Collagen Guide`
- Headline: `Get the free Collagen Guide`
- Value: `Collagen types, dosing, and what actually drives results — straight to your inbox.`
- Button: `SEND ME THE GUIDE`
- Success links to the PDF (host it and paste the link in the success step / welcome email).

**C) A/B test idea:** run **A (discount)** vs **B (value only)** as two variations in
Klaviyo's built-in form A/B test and keep the higher submit rate.

---

## Notes
- The `WELCOME15` code and "Loved by our collagen community" line are **placeholders** —
  set a real coupon and swap in a real review/rating before going live.
- Preview page has **zero external dependencies** (no web fonts, no CDN) so it renders
  anywhere and is safe to open offline.
