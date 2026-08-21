# Prime Script Forge — a Gemini Gem for high-performing ad scripts

Everything needed to stand up a Gemini Gem that writes production-ready 9:16 video ad scripts for
**Prime Ingredients / Prime Elements**, built on the 16 proprietary creative frameworks, the brand bible, and
the ICP language bank.

---

## What's in here

| File | Goes where | Size |
|---|---|---|
| `01-GEM-NAME.md` | Gem **Name** field | — |
| `02-GEM-DESCRIPTION.md` | Gem **Description** field | — |
| `03-GEM-INSTRUCTIONS.md` | Gem **Instructions** field (paste everything below the rule) | ~17 KB |
| `KNOWLEDGE-01-frameworks-16.md` | Gem **Knowledge** upload | ~34 KB |
| `KNOWLEDGE-02-brand-truth-and-compliance.md` | Gem **Knowledge** upload | ~20 KB |
| `KNOWLEDGE-03-icp-personas.md` | Gem **Knowledge** upload | ~17 KB |
| `KNOWLEDGE-04-voc-language-bank.md` | Gem **Knowledge** upload | ~19 KB |
| `KNOWLEDGE-05-winning-patterns.md` | Gem **Knowledge** upload | ~25 KB |
| `KNOWLEDGE-06-output-spec-and-qa.md` | Gem **Knowledge** upload | ~17 KB |

Six knowledge files, well inside Gemini's ten-file limit. Four slots are left deliberately free — see
*Extending it* below.

---

## Setup, in five minutes

1. Go to **gemini.google.com → Gems → New Gem** (or **Gem manager → New**).
2. **Name:** paste `Prime Script Forge` from `01-GEM-NAME.md`.
3. **Description:** paste the primary description from `02-GEM-DESCRIPTION.md`.
4. **Instructions:** open `03-GEM-INSTRUCTIONS.md`, copy **everything below the horizontal rule** (starting at
   `## ROLE`), paste it in.
5. **Knowledge:** upload all six `KNOWLEDGE-*.md` files.
6. **Save**, then run the smoke test below.

> **Tip.** If your Gemini plan renders `.md` uploads oddly, convert each knowledge file to PDF or paste it into a
> Google Doc and attach that instead. The content is what matters; the container is not.

---

## Smoke test — run these three before you trust it

**Test 1 — does it obey Law 1 (qualification)?**
```
Write me a 20-second Reel for NMN aimed at Linda, using PAS.
```
✅ Pass if: hooks are qualifying (they'd make a non-sufferer scroll), no "you" in the first five seconds, the
compliance ledger appears, and it names why it chose those hooks.
❌ Fail if: it writes broad attention-grabbing hooks, or opens with a second-person assertion about her body.

**Test 2 — does it refuse the fabrication?**
```
Use Framework 13 and include the beat where a colleague recommends the product.
```
✅ Pass if: it refuses to invent the referral, explains why (*"Fyi, this user is an affiliate"* earned 31 upvotes
in this corpus), and offers the self-disclosure substitute instead.

**Test 3 — does it push back once, then deliver?**
```
Give me a first-person story ad with 75% OFF in the headline.
```
✅ Pass if: it says in one or two sentences that Angle D is the worst angle in the account (0.83 ROAS) and the
discount headline lost on conv/click in five months of five, offers the higher-performing alternative — **and then
writes what was asked**, with the concern noted in the ledger.
❌ Fail if: it refuses, or if it silently writes something else.

---

## Starter prompts

**Everyday**
- `Three scripts for the 3 PM crash. Different frameworks. Tell me which to shoot first.`
- `Framework 14 on NMN, Solution-Aware, 45 seconds.`
- `20 qualifying hooks for Robert. Pillar 5. No script.`
- `The Margaret involuntary-discovery concept as a TEASE curiosity loop, 30 seconds.`
- `Take this winning script and run iteration rung 1 and 2 on it.` *(paste the script)*

**Diagnostic**
- `Here's an ad: 44% hook rate, 7.2% CTR, 2.4% conv/click, $61 CPA. What do I do?`
  → should identify the classic loser profile and say **rewrite the premise**, not hook-swap.
- `Critique this copy against the E-vs-F teardown.` *(paste the copy)*

**Strategic**
- `Which of the 16 frameworks are we not using, and what would each unlock?`
- `Build the retention/replenishment angle nobody has written. Flag the gate.`
- `Give me a week's shoot plan: 6 scripts, launch order Proven → Adjacent → Untested.`

---

## How the six laws map to the money

The Gem's instructions are built on six laws. Each is a measured finding, not an opinion:

| Law | The number behind it |
|---|---|
| 1 · Hooks qualify, they don't attract | Hook/hold/CTR correlate **negatively** with ROAS in all seven months. Winner CPA $31.90 vs loser $58.09 |
| 2 · Commit in brand voice, hedge in customer voice | Committed beats hedged by **53%** on ROAS — 1.41 vs 0.92, on the same insight |
| 3 · Name the moment, never the diagnosis | Same emotional payload, completely different risk profile |
| 4 · Second-person questions, not assertions | The winning structure carries the exposure. 100% of spend is on one channel |
| 5 · Subtraction, not addition; behaviour, not metric | How the corpus actually describes benefit, in its own words |
| 6 · One line per asset | A montage reads as a category ad and converts like one |

---

## Extending it

Four knowledge slots are free. In priority order:

1. **`KNOWLEDGE-07-own-testimonials.md`** — the single highest-value addition. Connect the review platform
   (the landing page cites 5,128 reviews; the review table returns zero rows) and drop the verified customer
   language in. **Only `OWN-` provenance can run as social proof**, and right now that's 73 rows out of 512.
   This one file would roughly triple the publishable bank.
2. **`KNOWLEDGE-08-gate-status.md`** — a live one-pager of G1–G7 status. Update it as gates close and the Gem
   stops marking assets 🔒 automatically.
3. **`KNOWLEDGE-09-winners-log.md`** — refresh the winner/loser table monthly from the ads export so the Gem's
   "why this should win" reasoning stays current rather than frozen at August 2026.
4. **`KNOWLEDGE-10-pdp-truth.md`** — the live PDP could not be read when the brand bible was built (blocked by a
   network egress proxy). Paste the PDP HTML or a full-page screenshot export here to close the largest
   information gap in the system and unblock G3 and G4 verification.

**Maintenance cadence:** refresh KNOWLEDGE-05 monthly from the warehouse and the ads export. Update KNOWLEDGE-02's
gate table on every gate close. When an `[R]` figure gets measured, promote it to `[M]` and note what changed —
never silently overwrite.

---

## Source documents

| Source | What it contributed |
|---|---|
| `Copy_of_Scripting_Frameworks_2026.docx` | Frameworks 1–12 with worked briefing examples |
| `_Ads_framework_14.pdf` | Frameworks 13–16 (the two $125K/$200K reverse-engineered structures plus the Good/Better/Best and Threat & Relief triads) |
| `primebrandbible.pdf` | Economics, the seven gates, the four ICPs, the claim ladder, the C2 rule, the 1,220-ad teardown, production rules |
| `icplanguagebank.md` | Verbatim VOC, the 15 golden lines, the 24 crafted lines, the proof hierarchy, the 24 creative territories, the six pillars, the landmines |

---

> Nothing in this repository is legal, regulatory or medical advice. The claim-risk flags throughout are
> **creative triage to speed the team up, not legal clearance.** Every claim needs Prime's own regulatory
> reviewer before it ships, and the G6 medical-eligibility questions need a qualified medical reviewer before
> they are answered anywhere — including in a comment box.
