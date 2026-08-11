# 05 — Production Workflow

How 12–16 finished statics get made every week by one person who is not a designer.

---

## The weekly rhythm

| Day | Block | Who | Output |
|---|---|---|---|
| **Monday** | Read the numbers. Kill losers, note winners. Mine 10 new reviews + comments. | Buyer | Kill list + winner list + fresh customer language |
| **Tuesday** | Ideation. Pick 12 concepts against the territory quota. Fill 12 briefs. | Buyer + copy | 12 one-line briefs |
| **Wednesday** | Build day 1 — six creatives (4:5 + 9:16 each). | Designer | 12 files |
| **Thursday AM** | Build day 2 — six creatives. QA all 12. | Designer | 12 files, QA'd |
| **Thursday PM** | **Launch.** Upload, name, publish. | Buyer | Live ads |
| **Friday** | Watch. No changes. | Buyer | — |
| **Sat–Sun** | Peak days. Scale winners only, no new launches. | Buyer | — |

**Never launch a new ad set on Monday** — 22% fewer orders than Saturday. Thursday launches get Friday to learn and hit Saturday's peak at full delivery.

---

## The concept brief (fill one per creative, 60 seconds each)

```
CREATIVE BRIEF #___
Territory:        ENG / FOG / GRD / TRU / VAL / TIM
Framework:        (from 02-copy-bank.md, e.g. "F4 — It's not X, it's Y")
Format:           (from 03-creative-formats.md, e.g. "01 Headliner")
Funnel stage:     Cold / Warm / Hot
Exact headline:   "________________________________"
Primary text:     PT-__
Insecurity served: #__  (from the ten in 01-strategy-and-brief.md)
Variable being tested (vs which control): ______________
Filename:         ______________
```

If you can't name the variable being tested, you're not testing — you're just spending.

---

## File naming — mandatory

```
NMN_[TERR]_[FRAMEWORK]_[FORMAT]_[RATIO]_v[NN]

NMN_ENG_F04-ItsNotX_01-Headliner_4x5_v01
NMN_VAL_F03-Timeline_04-Timeline_9x16_v02
NMN_TRU_F05-Testimonial_02-CommentFrame_4x5_v03
```

Iterations that change one variable increment the version: `v01` → `v02`. A genuinely new concept gets a new framework/format code, not a version bump. This is what makes the tracker readable six weeks from now, and it's what lets you answer "which angle actually works?" instead of "which ad worked?"

In Ads Manager the **ad name must exactly match the filename.** No exceptions — this is the join key between your tracker and your reporting.

---

## Tools

| Job | Tool | Note |
|---|---|---|
| Layout & assembly | **Canva** (or Figma) | Canva is the right call for a beginner. Build each format once as a Brand Template, then it's a text swap. |
| Templates | **Creative OS** | Opens directly into Canva/Figma. Fastest path from zero to professional-looking. |
| Background removal | Canva BG Remover | Built in |
| Backgrounds & scenes | Midjourney / Nano Banana / Firefly | Prompts below |
| Copy variations | Claude or ChatGPT + your Brain Trust project | Setup below |
| Review mining | Shopify / Judge.me export → Claude | Prompt below |

### Build each format ONCE

The single biggest speed unlock: build all 12 formats as **Canva Brand Templates** in week one. After that, producing a creative is: duplicate template → swap headline → swap review → export. Twelve creatives becomes a two-hour job, not a two-day job.

---

## The "Brain Trust" — your AI ideation assistant

Create a Claude Project (or ChatGPT Project) called **"Prime Ingredients — NMN Creative"** and upload:

1. `NMN_Deep_Customer_Intelligence.pdf`
2. This entire `meta-ads/` folder
3. A CSV export of all 5,128 customer reviews
4. Your last 90 days of ad-level performance export from Ads Manager
5. Screenshots of your top-10 Facebook ad comment threads
6. The product page copy `[CONFIRM — grab it from the live site]`

Then it can write in her language instead of in marketing language. Refresh the reviews export monthly.

### Prompt — weekly concept generation

```
You are my static ad ideation partner for Prime Ingredients NMN Complex.

Read the persona report and the copy bank in the project files.

Generate 12 static ad concepts for next week's batch. Quota:
3× ENG, 2× FOG, 2× GRD, 2× TRU, 2× VAL, 1× TIM.

For each, give me exactly:
- Territory code
- Framework number from 02-copy-bank.md
- Format number from 03-creative-formats.md
- The exact headline, max 9 words
- Which of Linda's 10 insecurities it serves
- Which of these three currently-winning ads it is a variation of, or "net new":
  [paste your current top 3 ad names + CPA]

Rules: use Linda's vocabulary from the reviews, not marketing vocabulary.
No banned words (see the ban list in 02-copy-bank.md).
Every concept must work as an image with under 15 words on it.
Do not repeat a headline already in the copy bank — these must be new.
```

### Prompt — review mining

```
Attached are [N] customer reviews for our NMN supplement.

1. Find the 20 reviews that describe a SPECIFIC MOMENT rather than a
   general feeling (e.g. "got on the floor with my granddaughter"
   beats "more energy").
2. Find the 10 reviews from customers who say they were skeptical or
   had wasted money on supplements before.
3. List the 25 exact phrases customers use most for: the afternoon
   crash, brain fog, and feeling like themselves again. Verbatim only.
4. Flag any review that mentions a disease, a medication, or a doctor's
   diagnosis — I cannot use those in ads.

Output as a table with: quote (verbatim), first name + last initial,
city if present, and which of these territories it fits:
ENG / FOG / GRD / TRU / VAL / TIM.
```

### Prompt — copy variation on a winner

```
This static ad is my current best performer:

Format: [e.g. 01 Headliner]
Headline: "[exact headline]"
CPA: $[X]  |  Outbound CTR: [X]%  |  Spend: $[X]

Write 5 variations that change ONLY the headline. Keep the same
framework, the same territory, and the same emotional promise.
Each variation should test a different hypothesis about WHY it works
— tell me the hypothesis alongside each line.

Constraints: max 9 words, Linda's vocabulary, no banned words,
no disease claims, no implied personal attributes.
```

---

## AI image prompt library

For backgrounds, scenes and hands. **Always** review output against the people rule in `04-design-system.md` — image models systematically render people 15–20 years younger than you ask for, so you will need to push the age language hard and re-roll.

**Hand holding the bottle (Format 05):**
```
first-person POV photograph, the hand of a 65-year-old woman holding a
white supplement bottle, natural aged skin with visible veins and age
spots, short natural nails, thin worn gold wedding band, warm morning
sunlight on a patio in Arizona, shallow depth of field, shot on iPhone,
candid and slightly imperfect framing, no filter --ar 9:16
```

**Lifestyle — the grandkids moment (Format 03, GRD):**
```
a 64-year-old woman with silver hair sitting on the floor of a bright
living room playing with a 3-year-old, warm afternoon light through a
window, linen shirt, genuine laughter, documentary photography, natural
skin texture with visible lines, no makeup retouching, Phoenix home
interior --ar 4:5
```

**Sunbelt walking scene (GRD, ENG):**
```
three women aged 60 to 70 walking briskly on a desert path at golden
hour, Arizona landscape with saguaro cacti, athletic but not fitness-model
bodies, silver and grey hair, laughing mid-conversation, warm backlight,
documentary style, natural skin texture --ar 4:5
```

**Clean product background (Format 01, 12):**
```
solid deep green studio background with soft top-left key light and a
gentle vignette, a small patch of natural grass at the base, minimal,
premium supplement advertising, no product, no text, high resolution
--ar 4:5
```

**Premium plinth composite (Format 01 hero):**
```
minimal studio scene, a stone plinth centred on a warm cream background,
soft directional lighting from the upper left, subtle contact shadow,
premium wellness brand aesthetic, empty plinth, no product, no text
--ar 4:5
```

**Rules for AI imagery:**
- Never AI-generate a face and present it as a real customer.
- Never AI-generate a "before/after."
- Check hands. Six fingers ships more often than you'd think.
- Check the label. If you composite a bottle, use the real product cutout — never let a model draw your label.

---

## Asset library structure

```
/creative-assets
  /product          bottle cutouts, PNG with transparency, all angles
  /six-bottle       the Format 12 lockup, pre-built
  /lifestyle        approved 55-70 photography, tagged by territory
  /hands            POV hand shots for Format 05
  /trust            Forbes/ELLE lockups, star bars, guarantee badges,
                    lab-tested seal, review-count bar at 3 sizes
  /templates        the 12 Canva template links
  /exports
    /2026-08-14     one folder per launch date
```

Build the `/trust` folder once, properly. Every ad needs it, and rebuilding a star bar 40 times is how a week disappears.
