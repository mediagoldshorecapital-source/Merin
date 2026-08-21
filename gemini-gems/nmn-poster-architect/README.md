# Prime NMN Poster Architect

A Gemini Gem that turns Prime Ingredients NMN ad copy into paste-ready **Nano Banana** static
poster prompts — brand-locked to the purple label, cast 58–68, and pre-cleared against the brand
bible's compliance gate.

## Files

| File | What it is |
|---|---|
| `GEM.md` | The paste-in file. Name, description and the full instruction block |
| `KNOWLEDGE.md` | Upload to the Gem's Knowledge section — ICP cards, pain map, copy banks, claim ladder, setting library |
| `EXAMPLE.md` | Optional second knowledge upload — one worked input and its expected output |

## Setup

1. Go to **gemini.google.com → Gems → New Gem**.
2. Copy the **Name** block from `GEM.md` into the name field.
3. Copy the **Description** block into the description field.
4. Copy the whole **Instructions** block into the instructions field.
5. Under **Knowledge**, upload `KNOWLEDGE.md` — and `EXAMPLE.md` too, if you want the output
   shape anchored to a worked case.
6. Save.

## Using it

**Attach the product bottle photograph at the start of every conversation.** It is what locks the
label and the palette, and it is the cheapest defence against showing the wrong bottle — a live
legal exposure for this brand with roughly 22 public customer complaints behind it.

Then paste ad copy. Headline, callouts, body, CTA — whatever you have. The Gem returns three
poster concepts, each with a layout spec and one paste-ready Nano Banana prompt.

```
Headline: Done With the 3 PM Crash
Callouts: Steadier Daily Energy / Less Afternoon Slump /
          Support for Cellular Energy / More Energy for Your Day
Body: Clean cellular support made for your daily routine.
CTA: Shop Cellular Energy
```

It also takes direction: *"give me Robert instead"*, *"all three on T6"*, *"9:16 only"*,
*"twelve concepts"*.

## What the Gem enforces on its own

- Prime bottle only — white body, purple label, "Prime Ingredients" at the top. Never blue, never
  an "M" cap.
- Talent 58–68, with an exact age stated in every prompt.
- No disease name in any voice. Name the moment, never the diagnosis.
- The verb ladder — `supports` and `helps maintain` are claimable; `boosts`, `restores` and
  `reverses` are not.
- No number it cannot cite: no review count, no star badge, no capsule count, no per-day maths,
  no lab-failure statistic.
- No percentage discount in a headline. The anchor is $29.98 → $16.66, structural.
- No third-party-testing, GMP or COA badge until the certificate is verified.
- FDA disclaimer on every poster at 28 px minimum.
- An ⒝ variant whenever the headline asserts something about the viewer's physiology.
- No rendered lab certificates, seals, press logos or invented review cards — an image model will
  fabricate one on request, and a fake COA is a legal problem, not a compliance one.

## Two things worth confirming

1. **Capsule count.** The product photograph reads "30 vegetarian capsules". The brand bible logs
   this as unresolved — the offer ladder implies 60, customers report 30, some ads apparently say
   120. At two capsules a day, 30 is fifteen days per bottle. Until it is settled the Gem prints no
   capsule count and no per-day cost.
2. **Label hex values.** Read off the supplied photograph, not a label file. The Gem treats an
   attached photo as authoritative, so this does not block anything — but replace the tokens in
   `GEM.md` once the real values are to hand.

## Sources

Prime Ingredients Complete Brand Bible (17 Aug 2026, supersedes all prior documents) · 83 pages of
prior NMN poster prompt work · the NMN Static Ads Playbook · Prime Ingredients product photography.

Nothing here is legal, regulatory or medical advice. The compliance gate is creative triage, not
clearance.
