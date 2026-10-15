# Analysis guide — classification and vocabulary

Read before writing Phases 1–3. The point of a shared vocabulary is that the
swipe file stays comparable across dozens of ads: if one entry says
"Solution-Aware" and another says "kind of warm traffic", the file stops being
sortable and stops being useful.

## Funnel stage

| Stage | What the script does | Tells in the copy |
|---|---|---|
| **TOFU** | Creates the problem or the curiosity from scratch | Opens on a symptom, a myth, or a "here's why X happens"; product appears late or barely |
| **MOFU** | Differentiates within a category the viewer already knows | Compares mechanisms, ingredients, doses; "what makes X actually work" |
| **BOFU** | Closes someone already shopping | Opens on offer, price, guarantee, urgency, reviews; product in the first three seconds |

Many UGC ads straddle two. Say so (e.g. "MOFU leaning TOFU") and name the beat
where it shifts — that boundary is usually where the ad's retention curve breaks.

## Awareness level (Schwartz)

- **Unaware** — doesn't know they have the problem. Script must name the symptom first.
- **Problem-Aware** — feels the symptom, doesn't know the cause. Script sells the diagnosis.
- **Solution-Aware** — knows the category (NAD+, NMN), not which product. Script sells the mechanism differentiator.
- **Product-Aware** — knows the brands. Script sells proof, dose, purity, price.
- **Most-Aware** — ready to buy. Script sells the offer and the deadline.

Justify the call with a specific line from the transcript. "Solution-Aware
because the hook assumes the viewer already recognizes NMN without defining it"
is a real classification; a bare label is not.

## Bias and trigger vocabulary (Phase 3, column 2)

Use these names where they fit, and coin a clear one where they don't.

**Attention/entry:** Curiosity Gap · Pattern Interrupt · Symptom Timestamping
(naming a specific hour/moment) · Negative Qualification ("if you're not X, skip this")

**Belief formation:** Epiphany Bridge · Root Cause Framing · Mechanism Credibility ·
Biological Inevitability (aging as unavoidable, so the fix is maintenance not
vanity) · Specificity Bias (odd numbers read as measured, round ones as marketed)

**Social:** In-Group Mimicry · Authority Transfer · Insider/Status Curiosity ·
Consensus Proof · Parasocial Trust (creator speaks as a friend, not a seller)

**Category positioning:** Dose Wedge (their 250mg vs a full serving) ·
Category Disqualification (rules out competitor SKUs by mechanism) ·
Cofactor Gap (the missing ingredient that makes the main one work)

**Conversion pressure:** Price De-anchoring (compare against a far more expensive
alternative before naming yours) · Cost-Per-Day Reframe · Risk Reversal ·
Scarcity/Stock Urgency · Sunk Attention ("you've watched this far")

**Payoff translation:** Vanity ROI (translates invisible cellular benefit into a
visible outcome) · Identity Payoff (who they get to be) · Relief Framing

## Writing the internal dialogue (column 3)

This column is where the document earns its keep, and it is the easiest one to
ruin by writing marketing copy in first person. Rules of thumb:

- Use the objects in their actual life: the 2:30 slump, the school run, the photo
  they didn't like, the shelf of half-finished bottles.
- Let them be skeptical. "Another supplement ad" and "I've heard this before" are
  the honest reactions to most hooks, and a hook that survives them is genuinely strong.
- Contractions, fragments, one swear-free grumble. If it reads like a testimonial,
  rewrite it.
- Ground it in the quoted line next to it — this is inference from evidence, not
  free association.

## Verdict column (column 4)

`Very High` — disqualifies competitors or reframes price; the line does structural
work no other line can do.
`High` — reliably moves belief but is replaceable.
`Moderate` — works for a narrow segment, or leans on a claim Prime can't make.

Always add the one-sentence diagnostic. The verdict without the reason is
unusable when someone rebuilds the ad three months later.

## Adapting for Prime (Phase 4)

What you are transferring is the *skeleton*: how many beats, how long each runs,
where the tension peaks, what objection each beat kills, the rhythm of short line
into long line. What you are not transferring is their sentences.

Practical test before you write each line: could you describe this beat's job in
one sentence without quoting them? Write from that description, then check the
length and stress pattern matches the original slot so the edit still cuts to the
same timing. `verify_report.py` warns when a line ends up too close to the source.

Read `compliance.md` before writing a single claim.
