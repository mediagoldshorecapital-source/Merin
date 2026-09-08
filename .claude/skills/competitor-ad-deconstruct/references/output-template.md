# Output template — follow this structure exactly

One ad = one `# Video N — <Creator or Source>` block. Batches stack these in one
document, matching how COMPETITOR_ADS_1 is organized.

Headings must contain the literal words "Phase 1" … "Phase 6" — `verify_report.py`
keys off them to know which text is verbatim evidence and which is Prime copy
subject to the compliance gate. Beat lines must keep the
`**Name (0:00–0:07):** "words"` shape for the same reason.

The examples below are generic placeholders showing *shape*. Never carry example
wording into a real report.

---

# Video N — [Creator / Brand / File name]

**Source file:** `competitor_ad_03.mp4` · **Duration:** 1:11
**Transcription:** faster-whisper large-v3 · 4 segments flagged for review
**Visuals:** 28 frames reviewed *(or: "Visuals not analyzed — audio-only source")*

## Phase 1: Verbal Architecture & Funnel Classification

**Funnel Stage:** [TOFU / MOFU / BOFU — one clause on why]
**Audience Awareness Level:** [Unaware / Problem-Aware / Solution-Aware /
Product-Aware / Most-Aware — one clause on the evidence in the script]

### Timestamped Transcript

Verbatim from `transcript.txt`. Beat windows come from real segment times, not
the canonical numbers below — those are typical, not mandatory. If the ad has no
distinct climax, merge beats and say so; do not pad to fill five slots.

**Hook (0:00–0:07):** "[exact words]"
**Setup / Bridge (0:07–0:26):** "[exact words]"
**Body / Mechanism (0:26–0:41):** "[exact words]"
**Climax / Stack (0:41–0:57):** "[exact words]"
**Close / CTA (0:57–1:11):** "[exact words]"

Uncertainty markers, used inline exactly as `flags.md` directs:
`[unclear: "quercetin" ~0:38]` · `[inaudible 0:44–0:46]` · `[no speech 0:52–0:58]`

### Visual & On-Screen Text Observations
Only what is visible in extracted frames. Format: `0:03 — [what is on screen]`.
Omit this subsection entirely for audio-only sources.

## Phase 2: Macro Formula & Narrative Extraction

**Chain:** [Beat 1 Archetype] → [Beat 2] → [Beat 3] → [Beat 4] → [Beat 5]

Example shape: `Authority Curiosity Hook → Root Cause Reveal → Mechanism Bridge →
Multi-Action Stack → Value De-anchoring & Direct CTA`

**Strategic Breakdown:** 1–2 sentences on why this order converts — what each beat
removes as an objection, and what the viewer must believe before the CTA lands.

## Phase 3: The Customer Psychologist Audit

Column 1 is evidence and must be verbatim (`…` truncation is fine). Columns 2–4
are your analysis. 5–7 rows covering the beats that carry the persuasive load.

| Spoken Audio Line | Psychological Trigger / Bias Activated | Target Customer Internal Dialogue (Raw, 1st Person) | Conversion Viability Verdict |
|---|---|---|---|
| "[verbatim fragment]" | [named bias — see analysis-guide.md] | "[unfiltered inner monologue, contractions, doubts, real objects in their life]" | [High / Very High / Moderate]. [one-sentence diagnostic] |

The internal dialogue is the column that earns the document. Write what the
viewer actually thinks — including their skepticism — not marketing-flavored
paraphrase of the claim.

## Phase 4: Prime Ingredients Adaptation (Production Script)

Preserve the competitor's beat count, timing, cadence and sentence rhythm; write
the words in Prime's own voice. Matching their structure is the strategy;
matching their sentences is copying, and the verifier flags lines that drift into
it. Swap every claim for a structure/function equivalent (`references/compliance.md`).

| Time / Beat | Audio / Spoken Line | Visual Directives & On-Screen Text (OST) |
|---|---|---|
| 0:00–0:07 (Hook) | [adapted line, same rhythm and length as source] | [shot type, talent action, b-roll] **OST:** [card text] |
| 0:07–0:26 (Setup / Bridge) | … | … |
| 0:26–0:41 (Mechanism) | … | … |
| 0:41–0:57 (Product Stack) | … | … |
| 0:57–End (Offer & CTA) | … | … |

**Beats cut for compliance:** [beat + the claim that could not be made compliantly,
or "none"]. Cutting a beat and saying so is correct; inventing a substitute claim
to fill the slot is not.

## Phase 5: Modular Variable-Tagged Skeleton

```
[HOOK: Symptom/Curiosity] → [BRIDGE: Biological Bottleneck] →
[MECHANISM: Pathway/Precursor] → [PRODUCT STACK: Dose/Active Ingredients] →
[OFFER & CTA: Bundle Tier/Price Anchor]
```

Then the fill-in-the-blank script with tokens in place:

> "[HOOK: symptom + timestamp]. [BRIDGE: what is actually depleted].
> [MECHANISM: how the pathway works]. [PRODUCT STACK: dose + actives].
> [OFFER: bundle tier + per-bottle price]. [CTA: action]."

**Swap guide:** which blocks change per audience (hook and offer usually), which
stay fixed (mechanism and dose), and what a valid substitution looks like for each.

## Phase 6: Alternative Hook Variations

Three hooks, 0:00–0:03, roughly 10–18 words each — short enough to actually land
before the scroll.

**Variation 1 — Symptom Timestamp / Root Cause:** "[hook]"
*Visual:* [direction] · **OST:** [card]

**Variation 2 — Category Contrast / Dose Wedge:** "[hook]"
*Visual:* [direction] · **OST:** [card]

**Variation 3 — Status / Insider Curiosity:** "[hook]"
*Visual:* [direction] · **OST:** [card]

---

**Verification:** `verify_report.py` — [N] quoted fragments matched, [N] warnings.
