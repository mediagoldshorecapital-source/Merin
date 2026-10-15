# Compliance gate & product grounding

Machine-readable version: `compliance_rules.json` (that file is what
`verify_report.py` enforces — edit it, not this prose, when rules change).

## Why this is strict

Prime sells a dietary supplement. Supplement marketing may describe support of
normal body structure and function; it may not claim to diagnose, treat, cure or
prevent disease. A single "reverses" or "treats" in a shipped script is a
regulatory and platform problem — Meta rejects on it, and the exposure lands on
the brand, not on the creative. So the rule is not stylistic caution, and
"the competitor said it" is never a reason Prime can.

## Say this, not that

| Competitor says | Prime says |
|---|---|
| reverses aging | supports healthy aging |
| treats fatigue | supports daily energy and cellular stamina |
| prevents cellular damage | provides antioxidant support |
| cures brain fog | supports focus and daily drive |
| repairs your DNA | supports the body's natural cellular maintenance |
| doctor-recommended, FDA approved | third-party lab tested, cGMP-certified facility |
| replaces NAD+ IV therapy | an at-home daily NAD+ support routine |

Approved phrasing bank is in `compliance_rules.json → approved_claim_language`.

## Hard stops in Prime copy (Phases 4–6)

- **Drug/disease vocabulary** — cure, treat, prevent, heal, reverse aging, or any
  named condition (Alzheimer's, diabetes, osteoporosis, cancer…). Naming a disease
  at all implies the product acts on it.
- **Banned tropes** — government/military secrets, "big pharma doesn't want you to
  know", miracle cures, conspiratorial framing. These tank trust and get accounts
  restricted.
- **Profanity.**
- **Competitor brand names and unlicensed personalities.** Quoting a spoken brand
  name inside Phases 1–3 is reporting what the ad said, which is fine. Putting it
  in Prime's mouth in Phase 4+ — including "better than [brand]" or an implied
  celebrity endorsement — is not.
- **Unverifiable specifics** — invented study counts, percentages, clinical results,
  or review numbers. If Prime hasn't got the substantiation on file, it doesn't
  go in the script.

## Product facts (do not restate from memory — copy from here)

- **Product:** Prime Ingredients NMN Ultimate 10-in-1
- **Dose:** 1,000 mg active NMN complex per serving
- **Serving:** 1–2 vegetarian capsules daily · 30 capsules per bottle. All supply
  claims assume **2 capsules/day**, so one bottle = 15 days.
- **10 actives:** NMN + TMG, CoQ10, Trans-Resveratrol, Glutathione, Astaxanthin,
  Quercetin, Grape Seed Extract, Fat-Soluble Vitamin C, Apigenin
- **Trust signals:** cGMP-certified facility · Made in the USA · Third-Party Lab
  Tested (Batch COA) · Non-GMO · Vegan · Filler-Free
- **Guarantee:** 30-day money-back guarantee
- **Substantiated proof points (confirmed 2026-10-15, on the live page):**
  60,000+ five-star reviews · 300+ clinical studies · "clinical". Use the exact
  numbers; never round them up.

## Current offer — Halloween Sale (Oct 16 – Oct 31, 2026)

- **Headline offer: "Up to 75% off".** Always "Up to" — a flat "75% off" is
  wrong and the verifier fails it.
- **Gift:** FREE $250 Amazon gift card.
- **Bundles:** Buy 1 Get 1 · Buy 2 Get 2 · Buy 3 Get 3.
- **Cart rewards:** free shipping over $50 · free Astaxanthin ($30 value) over
  $110 · free Magnesium ($80 value) over $150.

## Bundle pricing

| Bundle | Bottles / capsules | Price | Per bottle | Supply at 2/day | Shipping |
|---|---|---|---|---|---|
| Buy 1 Get 1 | 2 / 60 | $39.97 | $19.99 | 1 month | — |
| Buy 2 Get 2 | 4 / 120 | $79.97 | $19.99 | 2 months | Free |
| Buy 3 Get 3 | 6 / 180 | $99.98 | $16.66 | 3 months | Free |

Per-day anchors: **~$1.33/day** (B1G1) · **~$1.11/day** (B3G3), against
$100–$200/month boutique longevity stacks.

The bundle *structure* was reconfirmed on 2026-10-15; the dollar amounts were last
confirmed in September. Prefer "Up to 75% off" + bundle name + gift in scripts,
and confirm dollar figures with the user before a script goes to production.
The supply math (bottle = 15 days, B1G1 = 1 month) is the arithmetic most likely
to go wrong in a fast adaptation — check it.

## Campaign calendar (Q4 2026 — pick the offer by the ad's run date)

| Campaign | Dates |
|---|---|
| Halloween / Fall Reset | Oct 16 – Oct 31 |
| Veterans Day | Oct 27 – Nov 11 |
| Thanksgiving / BFCM Warm-up | Nov 11 – Nov 26 |
| Black Friday & Cyber Monday | Nov 12 – Nov 30 |
| Winter Solstice & Holiday Gifting | Dec 05 – Dec 25 |
| New Year's Eve / Fresh Start | Dec 16 – Jan 01 |

Windows are 10–15 day early activations and overlap. Only the Halloween offer is
confirmed; for any later campaign, ask the user for the offer before writing
offer copy, and write the CTA beat with an `[OFFER]` token until then.

## When a beat won't survive the gate

Cut it and record it under "Beats cut for compliance" in Phase 4. The temptation
is to keep the beat and soften the claim until it technically passes, which
usually produces a vague line that converts badly and still reads as a disease
claim. A cut beat with a note is honest and fixable; a laundered claim is neither.
