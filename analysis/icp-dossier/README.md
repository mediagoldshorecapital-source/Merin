# Four-ICP Dossier + Voice-of-Customer Quote Bank

Four buyer profiles across all 12 parts, plus **73 verbatim customer quotes**
tagged on emotion, job-to-be-done, objection-or-benefit and trigger moment.

- Working file: `icp-quote-bank.xlsx` — 5 sheets, filterable on every tag
- Report: `report.html` (standalone)
- Published: https://claude.ai/code/artifact/a6a76289-ba87-4186-b1d6-bf2b79985f0e

## The thing that came out of building it

You asked for a bank of the customer's own words so copy becomes transcription
rather than invention. The ICP research contains **zero verbatim quotes** — every
line in it is the researcher's inference. So I went looking for real language:

| Source | Rows |
| --- | ---: |
| `reviews_table` (Okendo/Yotpo) | **0** — never connected |
| `post_purchase_survey_table` | **0** — not running |
| `social_media_brand_mentions_table` | **0** — not configured |
| **`social_media_comments_table`** | **468** — the one live source |

Every quote here is from that corpus, unedited, traceable to a comment ID.

**And what they say is mostly not about aging.** The seven loudest themes are
operational. Three are severe:

1. **"Took my payment and never got my product."** Buyers describe non-delivery,
   automated replies, and are **organising to report the page to Meta, TikTok and
   Instagram.** For a business taking 100% of paid traffic from Meta, that is an
   existential risk, not a support ticket.
2. **"You show MicroIngredients bottle in your ad, but sell a different brand."**
   ~22 comments — the largest single theme. People zoom in on the footage, note
   the "M" on the cap, link the competitor's site, and conclude knock-off.
3. **"I would've purchased"** — at least 8 people say plainly they wanted to buy
   and didn't, because they couldn't find a one-time option. This corroborates
   the warehouse: 97% of orders carry the subscription flag while Subscribe & Save
   SKUs have sold 9 units total.

Also: a **capsule-count gap** (buyers expect 120, receive 30), **spokesperson
backlash** (the target demographic is hostile to the Kardashian association), and
**unanswered medical eligibility questions** from people ready to buy.

These are customer allegations, publicly made. They need verifying — but they're
already visible to every prospect who scrolls the comments.

## The four ICPs

Split by motivation, since the research only names two personas. Every claim is
marked **[M]** measured · **[R]** research · **[I]** inferred · **[—]** unavailable.

| ICP | Size | Evidence | Key numbers |
| --- | --- | --- | --- |
| **Linda — Energy** | ~55–60% [I] | Strong | AOV $60.37 · LTV $71.11 · repeat 13.5% |
| **Linda — Clarity** | Unsized | **Weakest — [R] only** | Not separable in the warehouse |
| **Margaret — Mirror** | 323 customers [M] | **Strongest** | LTV **$98.44** · repeat **26.9%** · 4.70 units |
| **Robert — Male** | 765 customers [M] | Good on spend | AOV **$66.48** · LTV **$82.55** |

**Margaret is the headline.** ASTA buyers have **38% higher LTV** and **twice the
repeat rate** of NMN-only buyers — and almost no marketing is aimed at them.
Moving 10% of the 6,491 NMN-only customers into the ASTA attach adds roughly $27
LTV each, with no new traffic.

**Robert measures out too:** +10% AOV, +16% LTV vs female buyers, on a
conservative name match (so 765 is a floor). Still zero creative written to him.

**Linda–Clarity is the weak one** and is labelled as such throughout — ManyChat
tags aren't in the warehouse, so it can't be sized, costed or tied to revenue.
It's a creative hypothesis, not a measured segment.

## The quote bank

73 rows. Columns: quote · emotion · JTBD · objection/benefit · what it objects to ·
trigger · ICP · copy-ready · flag count · the six quality flags · date ·
comment_id · source.

**The corpus is 84% fear and anger:**

| Emotion | Quotes | |
| --- | ---: | --- |
| Anger | 35 | Well covered |
| Fear | 26 | Well covered |
| Relief | 6 | Thin |
| Grief | 4 | Thin |
| Pride | 2 | Thin |
| **Hope** | **0** | **No data** |
| **Shame** | **0** | **No data** |

Those cells ship **empty, not invented**. Your customers are currently generating
objection language rather than aspiration language — because the loudest
experiences they're having are operational.

**15 quotes are copy-ready** (3+ of your six quality flags).

## Harvest plan — closing the gap

Ranked by quotes per hour. **The quickest win: your landing page cites 5,128
reviews and the warehouse holds none of them**, because the review platform was
never connected. That's thousands of sentences of exactly the hope/relief/pride
language this bank lacks, already written, one integration away.

Then: post-purchase survey (one question — "what made you finally order?" — which
harvests trigger moments), Klaviyo reply inbox, ManyChat DM transcripts, support
tickets.

## Caveats

Commenters are not necessarily verified purchasers. Robert is name-inferred, so
765 is a floor. His 1.81 ROAS is from the research and is not verifiable in the
warehouse — confirm in Ads Manager before moving budget. Section 01 findings are
customer allegations requiring independent verification.

## Regenerating

`icp_data.py` is the single source; `build_xlsx.py` and `build_html.py` generate
both outputs. Edit the data, re-run both, so they can't drift apart.
