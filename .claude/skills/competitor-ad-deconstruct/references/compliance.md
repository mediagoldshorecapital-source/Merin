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
- **Serving:** 2 vegetarian capsules daily · 30 capsules per bottle · 15-day supply per bottle
- **10 actives:** NMN + TMG, CoQ10, Trans-Resveratrol, Glutathione, Astaxanthin,
  Quercetin, Grape Seed Extract, Fat-Soluble Vitamin C, Apigenin
- **Trust signals:** cGMP-certified facility · Made in the USA · Third-Party Lab
  Tested (Batch COA) · Non-GMO · Vegan · Filler-Free
- **Guarantee:** 30-day money-back guarantee

## Approved pricing (no other numbers)

| Bundle | Price | Per bottle | Supply | Shipping |
|---|---|---|---|---|
| 2-Pack (Buy 1 Get 1) | $39.97 | $19.99 | 30 days | — |
| 4-Pack (Buy 2 Get 2) | $79.97 | $19.99 | 60 days | Free |
| 6-Pack (Buy 3 Get 3) | $99.98 | $16.66 | 90 days | Free |

Value anchor: **~$1.11/day** against $100–$200/month boutique longevity stacks.
Note the supply math: a bottle is 15 days, so bundle-level supply claims must
match the table above — this is the arithmetic most likely to go wrong in a fast
adaptation.

## When a beat won't survive the gate

Cut it and record it under "Beats cut for compliance" in Phase 4. The temptation
is to keep the beat and soften the claim until it technically passes, which
usually produces a vague line that converts badly and still reads as a disease
claim. A cut beat with a note is honest and fixable; a laundered claim is neither.
