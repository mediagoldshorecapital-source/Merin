# 04 — The Design System

Specs a beginner can follow literally. Tuned for one thing: **a 62-year-old woman reading a phone at arm's length, in Arizona daylight.**

---

## 1. Canvas sizes

| Ratio | Pixels | Placements | Priority |
|---|---|---|---|
| **4:5** | **1080 × 1350** | Facebook Feed, Instagram Feed | **Build first — always** |
| **9:16** | **1080 × 1920** | Stories, Reels | Build second — always |
| 1:1 | 1080 × 1080 | Fallback, some Feed placements | Optional |

**Never build 16:9 or 1.91:1.** Desktop converts at 1.86% for this brand. We do not serve it deliberately and we do not design for it.

Export: **PNG** for text-heavy designs (crisper type), **JPG at 90%** for photo-heavy ones. Keep under 8 MB. Colour profile sRGB.

### Safe zones

**4:5 Feed:** keep critical text out of the **bottom 180px** — the profile name, CTA button and "See more" render near there on some surfaces.

**9:16 Stories/Reels:**
```
┌──────────────────┐
│  250px  DEAD     │  ← profile icon, "Sponsored"
├──────────────────┤
│                  │
│   1330px SAFE    │  ← everything important lives here
│                  │
├──────────────────┤
│  340px  DEAD     │  ← CTA sticker, "Learn more" swipe
└──────────────────┘
```

### Text density

Meta no longer hard-rejects for the old 20% text rule, but text-saturated images still get throttled reach and higher CPMs. **Keep text under ~30% of the pixel area.** The Breakup Letter and iMessage formats are deliberate exceptions — they earn it with dwell time, and they should be monitored for CPM specifically.

---

## 2. Type scale (on a 1080-wide canvas)

**Everything scales from canvas width. On 1080px:**

| Role | Size | Weight | Notes |
|---|---|---|---|
| Hero number (Format 11) | 300–400px | Black / 900 | |
| Primary headline | **100–130px** | Bold / 800 | Line height 1.05–1.15 |
| Secondary headline | 72–90px | Bold | |
| Sub-head / benefit line | 52–64px | Semibold | |
| **Body text — absolute minimum 36px** | 40–52px | Regular / Medium | Line height 1.4–1.5 |
| Review quote | 44–56px | Medium, italic optional | |
| Trust bar / review count | 32–38px | Semibold | |
| Legal / disclaimer | **28px minimum** | Regular | Never smaller. Ever. |

**Why so big:** at 1080px wide displayed on a ~390pt-wide iPhone, a 36px asset pixel renders around 13pt. That is already at the low end of comfortable for presbyopic eyes. Anything under 36px is decoration, not communication.

### Font rules

- **Use:** Inter, Poppins, Montserrat, Archivo, Source Sans, Figtree (sans) · Lora, Playfair Display, Source Serif (serif, for the Breakup Letter only)
- **Never use:** thin or light weights at any size; condensed faces; script fonts for body copy; all-caps for anything longer than three words.
- Maximum **two** font families per ad. Two weights of one family is usually better.
- Left-align body copy. Centred text is harder to track for aging eyes — reserve centring for one- and two-line headlines.
- Line length: 20–34 characters per line for headlines. Break lines manually where the meaning breaks, not where the box runs out.

---

## 3. Colour

### The rule

**Pull the primary from the NMN Complex label.** `[CONFIRM]` the label hex codes and fill this table in — familiarity between ad and bottle is a trust mechanic for a woman who has been scammed before.

| Slot | Hex | Use |
|---|---|---|
| Brand primary | `[CONFIRM]` | Backgrounds, dark bands |
| Brand light tint | `[CONFIRM]` | Grid quadrants, timeline band 1 |
| Brand mid tint | `[CONFIRM]` | Timeline band 2 |
| Accent / CTA | `[CONFIRM]` | Prices, ticks, the payoff word |
| Cream | `#F6F1E7` | Breakup letter, checklist panels |
| Near-black | `#141414` | Body text on light |
| Off-white | `#FAFAFA` | Body text on dark |
| Gold (stars) | `#F5A623` | Star ratings only |
| Muted grey | `#8A8A8E` | Struck-through anchor prices, "them" column |

Until the label hexes are confirmed, these work for a longevity/wellness product aimed at this demographic and are safe defaults:

| Slot | Hex | Why |
|---|---|---|
| Deep green | `#14532D` | Reads as natural/clinical, high contrast with white |
| Mid green | `#2F7A4F` | |
| Light sage | `#DDEBE0` | |
| Warm amber accent | `#E08A2B` | Warm, energetic, high contrast on green, and it is not a "medical blue" |
| Warm cream | `#F6F1E7` | Softer than white for long reads |

### Contrast — non-negotiable

- Headline and body text: **≥ 4.5:1** against its background. Aim for **7:1**.
- Never place text directly on a busy photo. Use a solid band, a 60%+ scrim, or a blur.
- **Avoid blue-on-black and blue/green pairings for text.** The aging lens yellows, which compresses blue discrimination specifically. A 62-year-old sees your navy-on-charcoal as mud.
- Never grey text on a coloured background. Never `#999` on `#FFF`.
- Check every design in greyscale before shipping (Canva: duplicate → apply Greyscale filter). If the headline disappears, the contrast was carried by hue alone and it will fail for some viewers.

### Colour psychology for this buyer

Bold, saturated block colour is what stops the scroll. Warm tones (amber, terracotta, warm green) outperform cool clinical blues for this demographic — blue reads as pharmaceutical, and pharmaceutical reads as "the thing my doctor already told me is normal."

---

## 4. Imagery

### The people rule

**Every human in a Prime Ingredients ad is 55–70 years old.** Not 45 with grey hair. Not a stock "active senior" in a white gym top. A real-looking woman who could be at the Scottsdale farmer's market on a Saturday morning.

Checklist for any hand, face, or body shot:
- [ ] Visible age markers — softer skin, some age spots, natural lines
- [ ] Short natural nails, or a modest manicure. Not gel extensions.
- [ ] Jewellery that reads 60s: a worn wedding band, a simple gold chain
- [ ] Clothing: linen, cotton, muted solids. Not athleisure branding.
- [ ] Hair: natural grey/silver/soft blonde, styled but not salon-fresh
- [ ] Setting: patio, garden, kitchen with warm morning light, walking path, pool deck

### The place rule

**Sunbelt.** Phoenix, Tucson, Scottsdale, Las Vegas, Houston, San Antonio, Miami, San Diego. Palms, desert plants, terracotta, bougainvillea, wide skies, strong warm sun. Never snow, never a Manhattan apartment, never a grey European street.

### Product photography

- Background always removed for composites (Canva BG Remover).
- Bottle occupies **28–38%** of canvas height. Bigger looks like a catalogue; smaller looks like an afterthought.
- Add a grounded shadow. A floating bottle with no shadow is the #1 tell of an amateur composite.
- Label must be legible at full size. If the label text is mush, the ad reads as counterfeit — fatal for insecurity #6.
- For Format 12, six bottles in a row, slight overlap, consistent lighting direction.

---

## 5. Layout

**The thirds rule for statics:**
```
Top third      → the hook (headline or trust bar)
Middle third   → the proof (product, review, comparison, timeline)
Bottom third   → the offer (bundle + guarantee + stars)
```

- Margins: **60px minimum** on all sides. 80–100px looks more premium.
- Alignment: everything snaps to a common left edge or a common centre. Mixed alignment is what makes homemade ads look homemade.
- Whitespace is not wasted space. The single most common beginner error is filling every pixel.
- Maximum **five** distinct elements on a canvas. Count them: headline, product, trust bar, offer bar, one supporting graphic. That's five. Stop.

---

## 6. The 26-point pre-flight QA

Run this on every file before it enters the ad account. Print it.

**Readability**
1. [ ] Headline legible when the file is shrunk to 15% on screen
2. [ ] No text smaller than 36px (28px for legal)
3. [ ] Text contrast ≥ 4.5:1
4. [ ] Passes the greyscale test
5. [ ] No thin or condensed fonts
6. [ ] Maximum two font families

**Format**
7. [ ] Exactly 1080×1350, or 1080×1920
8. [ ] Nothing critical in the story safe zones (top 250px / bottom 340px)
9. [ ] Nothing critical in the bottom 180px of a 4:5
10. [ ] Text covers under ~30% of the area
11. [ ] Exported PNG or JPG-90, sRGB, under 8 MB
12. [ ] A 9:16 version exists

**Content**
13. [ ] One idea only
14. [ ] Social proof present (review count, stars, press, or a real quote)
15. [ ] Offer present and stated as `Buy 3 Get 3 Free · $16.66/bottle`
16. [ ] Guarantee mentioned
17. [ ] No discount code anywhere
18. [ ] Any person shown reads as 55–70
19. [ ] Setting reads Sunbelt/warm
20. [ ] Brand colour matches the label

**Craft**
21. [ ] Product background cleanly removed, no halo
22. [ ] Bottle has a grounded shadow
23. [ ] Label legible
24. [ ] Everything aligned to a shared edge
25. [ ] No spelling errors (read it backwards, word by word)

**Compliance**
26. [ ] Cleared against `08-compliance.md` — no disease claim, no implied personal attribute, no fabricated review, no unsupported statistic

**One ad fails QA = fix it. Three ads in a batch fail the same point = fix the template.**
