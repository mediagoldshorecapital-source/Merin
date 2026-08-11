# VoC Bank — Mining Sheet Spec

The single most valuable asset the creative team owns. Build it once, add to it weekly,
**never delete from it.**

---

## Build it as a spreadsheet with these columns

| Column | Values | Why |
|---|---|---|
| `id` | auto | For citing in briefs |
| `quote` | verbatim, unedited | **Never clean up the grammar.** The awkwardness is the credibility. |
| `source` | site review / ad comment / support ticket / Reddit / Amazon / YouTube / DM / survey / email reply | Weight site reviews and ad comments highest |
| `source_detail` | URL, ticket #, ad name | So you can verify before it airs |
| `date` | | Objections drift as you scale to colder audiences |
| `persona` | LindaB / Dana / Robert / Returner / unknown | |
| `emotion` | fear / shame / hope / relief / pride / anger / grief | **The sort column that finds pillars** |
| `type` | objection / benefit / trigger-moment / comparison / mechanism-question | |
| `jtbd` | what were they trying to accomplish | |
| `trigger_scene` | the specific moment described | Hooks live here |
| `nugget` | Y / N | Meets the golden-nugget bar below |
| `used_in` | Concept IDs | Prevents reusing the same quote in six ads |

---

## The golden-nugget bar

A quote qualifies if it has **≥3** of:

- [ ] A **specific time, place, or scene** — "at 3pm", "in front of my daughter"
- [ ] A **physical sensation**, not an abstraction — "legs like sandbags", not "low energy"
- [ ] A **comparison to a former self** — "I used to…"
- [ ] An **admission** of something slightly embarrassing
- [ ] **Plain, unbranded** language — zero marketing words
- [ ] **Quotable in under 12 words**

**Benchmark from your own data:**
> *"I used to do everything. Now I sit while others do."*
> 10 words · former self · admission · zero marketing language. That's a hook, unedited.

---

## Where to pull from, in priority order

| Priority | Source | How |
|---|---|---|
| 1 | **Your site reviews** | Export CSV from your review app |
| 2 | **Ad comments on top-spending ads** | Ads Manager → top 10 by spend → Preview → View on Facebook → read every comment |
| 3 | **Post-purchase survey** | Ask: *"What almost stopped you from buying?"* — best question in DTC |
| 4 | **Support tickets, pre-purchase** | Filter your helpdesk to pre-purchase enquiries |
| 5 | **ManyChat DM transcripts** | Self-identified goals, in her words |
| 6 | **Reddit** | `site:reddit.com NMN worth it` / `NAD+ supplement waste of money` |
| 7 | **Amazon 1–3★** on category competitors | Plus **Ask Amazon AI**: *"What do reviewers complain about most?"* |
| 8 | **YouTube review comments** | More useful than the videos |
| 9 | **Email replies** to Klaviyo broadcasts | Long-form and emotional |

---

## How to work it

1. **Dump first, judge later.** One quote per row, no editing, no filtering.
2. **Tag in a second pass.** Never tag while collecting — you'll narrow your intake.
3. **Sort by `emotion` and read each cluster together.** A cluster of 15 quotes about the same
   fear is not one ad — it's a **content pillar** that will support six.
4. **Sort by `trigger_scene`.** Repeated scenes across different customers are your strongest
   hooks, because they're the moments the whole segment shares.
5. **Cite the row id in every brief.** If a hook has no id, it was invented — and invented
   hooks lose to transcribed ones.

---

## Maintenance

- **Weekly, 10 minutes:** log 5 new quotes from this week's ad comments *(the last step of the
  weekly scorecard ritual)*
- **Monthly:** re-sort by emotion, check whether a new cluster has formed — new clusters are
  new pillars
- **Quarterly:** re-run the full mine. Objections evolve as you scale into colder audiences.

## Target volume

| Stage | Rows |
|---|---|
| Before writing any copy | **100+** |
| Healthy at month 3 | 250+ |
| Golden nuggets (`nugget = Y`) | ≥20% of rows |
