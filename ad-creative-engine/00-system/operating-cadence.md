# The Weekly Operating Cadence

The engine runs on a five-day loop. The point of fixing the days is that research never
gets skipped when a launch is on fire — it has its own slot, before the slot where
decisions get made.

---

## Monday — READ (½ day)

**Input:** last week's ad account data + the running learning log.

1. Pull creative-level metrics for every ad live ≥ 4 days. Fill `04-testing/weekly-scorecard.md`.
2. Classify each ad against the decision gates in `04-testing/testing-framework.md`:
   **Scale / Iterate / Re-hook / Kill.**
3. Diagnose *where* each loser broke, not just that it lost:
   - Low hook rate → the first 3 seconds failed. The body may be fine. **Re-hook, don't kill.**
   - Good hook rate, cliff before 25% → the bridge broke its promise.
   - Good hold, low CTR → the offer/CTA is weak or the ad never earned the ask.
   - Good CTR, bad CPA → wrong audience or the landing page is off-message.
4. Write one line per ad into the **learning log** at the bottom of the scorecard. One line.
   Not a paragraph. Format: `<what we believed> → <what happened> → <what we now believe>`.

**Output:** the winners list and the re-hook list that feed Tuesday.

---

## Tuesday — RESEARCH & DECIDE (full day)

### Morning: refill the libraries
- **Reviews** — read the last 50 product reviews. Pull verbatim phrases into
  `02-libraries/angle-map.md` under *Voice of Customer*. Use `05-prompts/02-mine-voc-reviews.md`.
- **Comments** — read the comment section of your own top 3 ads and your competitors' top 3.
  Comments are the cheapest angle source that exists: every repeated objection is an ad,
  every repeated question is a hook, every unprompted benefit mention is an angle.
- **Support / DMs** — anything that came in twice is a pattern.
- **Swipe** — add any new competitor ad to `01-swipe/competitor-ad-index.md`; run the
  full Phase 1–6 protocol on the two most interesting. Use `05-prompts/01-deconstruct-competitor-ad.md`.

### Afternoon: build the slate
- Run `python3 tools/combo_planner.py` for a proposed 11-brief slate.
- Override it with judgement. The planner does not know that you just found a new angle
  in the reviews; you do.
- For every brief, write the **hypothesis** before the brief (see testing framework).
  If you cannot state what you'd learn from it, it does not go on the slate.

**Output:** 11 named, hypothesised concepts.

---

## Wednesday — BRIEF (full day)

For each of the 11: `python3 tools/new_brief.py --format Fxx --hook Hxx --angle Axx --icp <name>`,
then write it. Target: **45 minutes per brief.** They are not screenplays.

Every brief must clear the gate in `03-templates/creative-brief.md`:
- The first 3 seconds are written word-for-word, with the visual and the on-screen text.
- The hook makes a **specific, falsifiable, or forbidden** claim — not a general one.
- The ad handles at least two objections from the ICP stack.
- Every claim has a substantiation note per `02-libraries/proof-and-claims.md`.

---

## Thursday — HAND OFF & PRODUCE

- Briefs to creators / editors with reference links to the swipe ad they're modelled on.
  **Always send the reference.** A brief without a reference video gets misinterpreted.
- Cast to the ICP, not to who is available. A 32-year-old cannot deliver a Linda ad.
- Batch-shoot: one creator, one session, **the same body with 4–6 different hooks**.
  This is where the iteration budget comes from and it costs almost nothing extra.

---

## Friday — SHIP & LOG

- Upload with the naming convention from `00-system/naming-and-tracking.md`. Non-negotiable —
  an unparseable name is a data point you will never recover.
- One ad = one variable changed versus its parent, or you cannot attribute the result.
- Log launch date, hypothesis, parent creative, and the changed variable in the scorecard.

---

## Monthly (first Monday)

- **Format audit** — which of the 10 formats has produced a winner in 90 days? Retire dead ones; promote a wild that worked into the standing library.
- **Hook archetype audit** — same question, on hooks. Rank archetypes by median hook rate.
- **Swipe refresh** — pull 10 new competitor ads from Meta Ad Library (`ads_library_search`) filtered to ads running 30+ days; longevity is a fast-rotating category and a 4-month-old swipe file is a liability.
- **Angle exhaustion check** — an angle that has run 12+ creatives with declining hook rate is fatigued. Rest it for 8 weeks; it comes back.
