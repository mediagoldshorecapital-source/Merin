# Prime Ingredients — Ad Creative Engine

A repeatable system for deciding **what ads to make, why, and in what order** — then
turning that decision into a brief and a shootable script, every week, without
starting from a blank page.

Built from a teardown of **31 competitor ads** in the NMN / NAD+ / longevity category
(Micro Ingredients, Cata-Kor, Clean Nutra, ACROM, Volera, NMN.Supps, Micronutrients,
and creator accounts). The teardown lives in `01-swipe/`. Everything else in this repo
is the machine that turns that teardown into new creative.

---

## The one-paragraph version

Winning ads in this category are not original. They are **14 hook archetypes** bolted
onto **10 ad formats**, carrying **16 angles**, aimed at **2 ICPs** at **4 awareness
levels**. That is a finite combination space. The engine's job is to (1) keep the
libraries stocked from real research, (2) pick the highest-expected-value combinations
each week, (3) express them as briefs a creator can shoot without asking questions, and
(4) read the results so next week's picks are better than this week's.

---

## Map of the repo

| Path | What it is | When you touch it |
|---|---|---|
| `00-system/operating-cadence.md` | The weekly rhythm — Mon research → Fri ship | Every week |
| `00-system/icp-profiles.md` | Linda & Robert, awareness ladder, objection stack | When research changes them |
| `00-system/naming-and-tracking.md` | Creative naming convention + the tracking schema | Every brief |
| `01-swipe/competitor-ad-index.md` | All 31 ads: format, stage, awareness, hook, formula | Weekly, when adding new swipe |
| `01-swipe/deconstruction-protocol.md` | The Phase 1–6 protocol, written as a procedure | Every new competitor ad |
| `02-libraries/hook-bank.md` | 14 hook archetypes + templates + 70 written hooks | Every brief |
| `02-libraries/format-cards.md` | 10 proven ad formats with beat-by-beat structure | Every brief |
| `02-libraries/angle-map.md` | 16 angles × ICP × awareness → what to make and why | Weekly slate planning |
| `02-libraries/proof-and-claims.md` | Claim guardrails, substantiation, banned phrasings | Every script, before it ships |
| `03-templates/creative-brief.md` | The brief. One page. Non-negotiable 3-second mandate | Every brief |
| `03-templates/script-template.md` | Modular script with `[VARIABLE]` tagging | Every brief |
| `04-testing/testing-framework.md` | Hypothesis format, decision rules, kill/scale gates | Weekly readout |
| `04-testing/weekly-scorecard.md` | The readout table + learning log | Every Monday |
| `05-prompts/` | 5 reusable LLM prompts that run the pipeline | Continuously |
| `06-briefs/` | Where produced briefs live, numbered | Every brief |
| `tools/new_brief.py` | Scaffolds a numbered brief + script from templates | Every brief |
| `tools/combo_planner.py` | Proposes next week's slate from the libraries + winners | Every Tuesday |
| `06-briefs/B-0001_…` | **Worked example** — a fully filled brief and script | Read once, then copy the standard |

---

## The loop (what "owning the engine end to end" means)

```
  RESEARCH            DECIDE              BRIEF               SHIP              READ
 ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
 │ Reviews  │      │ Angle    │      │ Format   │      │ Creator  │      │ Hook rate│
 │ Comments │─────▶│  map     │─────▶│  card    │─────▶│  / edit  │─────▶│ Hold     │
 │ Support  │      │ + hook   │      │ + hook   │      │          │      │ CTR/CPA  │
 │ Swipe    │      │ + ICP    │      │ + script │      │          │      │          │
 └──────────┘      └──────────┘      └──────────┘      └──────────┘      └────┬─────┘
       ▲                                                                       │
       └───────────────────── learning log updates libraries ──────────────────┘
```

Nothing enters the brief stage that did not come out of the angle map, and nothing
enters the angle map that did not come out of research or the swipe file. That
constraint is the whole point — it is what makes the output defensible in a meeting
("why this ad?") instead of a matter of taste.

---

## Weekly output target

| Slate item | Count | Source |
|---|---|---|
| **Iterations** on a proven winner (new hook, same body) | 6 | `04-testing/weekly-scorecard.md` winners |
| **Adjacents** (proven format × new angle, or new ICP) | 3 | `02-libraries/angle-map.md` |
| **Wilds** (untested format or angle) | 2 | `01-swipe/` newest teardowns |
| **Total briefs / week** | **11** | |

60 / 25 / 15 split. The wilds are the R&D budget — they are how the winner column gets
refilled three months from now. Cut them and the engine slowly dies.

---

## Start here

1. Read `00-system/icp-profiles.md` — everything downstream is aimed at Linda or Robert.
2. Read `02-libraries/format-cards.md` — the ten shapes an ad can take.
3. Run `python3 tools/combo_planner.py --winners <your current winners>` to see a proposed slate.
4. Run `python3 tools/new_brief.py --list`, then
   `python3 tools/new_brief.py -f F01 -a A13 -k H05 -i linda -w problem -b Wild`
   to scaffold a brief into `06-briefs/`.
5. Fill the brief, hand to the creator, log it in the scorecard.
