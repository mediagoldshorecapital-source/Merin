# Naming Convention & Tracking Schema

If the name doesn't parse, the learning doesn't happen. This is the highest
effort-to-value ratio rule in the whole engine.

---

## Creative name

```
PI_<ICP>_<AWARE>_<FORMAT>_<ANGLE>_<HOOK>_<RATIO>_v<N>
```

| Token | Values | Example |
|---|---|---|
| `PI` | Brand — Prime Ingredients | `PI` |
| `<ICP>` | `LIN` (Linda) · `ROB` (Robert) | `LIN` |
| `<AWARE>` | `UN` · `PA` · `SA` · `PDA` | `PA` |
| `<FORMAT>` | `F01`–`F10` from `format-cards.md` | `F04` |
| `<ANGLE>` | `A01`–`A16` from `angle-map.md` | `A03` |
| `<HOOK>` | `H01`–`H14` from `hook-bank.md` | `H05` |
| `<RATIO>` | `9x16` · `1x1` · `4x5` | `9x16` |
| `v<N>` | Version. Bump only when **one** variable changes | `v3` |

**Example:** `PI_LIN_PA_F04_A03_H05_9x16_v2`

Reads as: Prime Ingredients, Linda, Problem-Aware, Peer Testimonial Montage,
Underdosing angle, Symptom Qualification hook, vertical, second version.

### The one-variable rule
A `v` bump changes exactly one token or one element (hook line, OST, thumbnail frame,
CTA). Change two and the result is uninterpretable. If you want to change the format
*and* the angle, that is a new v1, not a v-bump — and it belongs in the "wild" bucket.

---

## Tracking schema

One row per creative, appended forever. Keep it in the scorecard file, or mirror it to a
sheet — the columns are what matter.

| Column | Type | Notes |
|---|---|---|
| `creative_name` | string | The convention above |
| `launch_date` | date | |
| `brief_id` | string | e.g. `B-0042`, links to `06-briefs/` |
| `parent_creative` | string | Blank if v1. This is what makes iteration traceable |
| `changed_variable` | string | `hook_line`, `ost`, `format`, `cta`, `creator`, `first_frame` |
| `hypothesis` | string | One sentence, written *before* launch |
| `icp` / `awareness` / `format` / `angle` / `hook` | enum | Parsed from name, kept explicit for pivoting |
| `spend` | currency | |
| `impressions` | int | |
| `hook_rate` | % | 3-sec views ÷ impressions |
| `hold_25` / `hold_50` / `hold_75` | % | Retention curve — where it breaks |
| `ctr_outbound` | % | |
| `cpc` / `cpa` / `roas` | numeric | |
| `verdict` | enum | `SCALE` · `ITERATE` · `RE-HOOK` · `KILL` |
| `learning` | string | One line. Belief → result → new belief |

---

## Asset file naming (so the edit bay stays sane)

```
/raw/<creator>_<shootdate>/           # everything from the shoot
/hooks/<HOOKID>_<creator>_<take>.mp4  # isolated hook takes, reusable across bodies
/bodies/<FORMATID>_<ANGLEID>_<creator>.mp4
/exports/<full creative name>.mp4
```

Keeping **hooks as separate files** is what makes the 60% iteration budget nearly free:
a new ad is often a 4-second file swapped onto an existing body.
