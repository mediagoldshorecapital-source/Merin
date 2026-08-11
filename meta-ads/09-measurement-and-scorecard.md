# 09 — Measurement & Scorecard: How You Know It Worked

This file turns "the ads feel like they're doing okay" into a number that decides kill, iterate, or scale. **This is the file that makes the whole SOP produce revenue instead of content.**

---

## Part A — The four numbers per creative

Every creative is judged on four metrics, in order. Each one isolates a different failure point, which is what makes this diagnostic rather than just a report.

| # | Metric | How to get it in Ads Manager | What it tells you |
|---|---|---|---|
| 1 | **Hook rate** | `3-second video plays ÷ impressions` | Did the first 3 seconds stop the scroll? |
| 2 | **Hold rate** | `ThruPlays ÷ 3-second video plays` | Did the body keep her? |
| 3 | **Link CTR** | `Outbound clicks ÷ impressions` (use *outbound*, not "all clicks") | Did she want it enough to leave Facebook? |
| 4 | **CPA / ROAS** | `Spend ÷ purchases` and `revenue ÷ spend` | Did it make money? |

**Set up a custom column view** in Ads Manager once, and save it: Ad name · Spend · Impressions · 3-sec plays · ThruPlays · Outbound clicks · Outbound CTR · CPC · Adds to cart · Purchases · CPA · Purchase ROAS · Frequency.

You'll need to build Hook rate and Hold rate as **custom metrics** (Columns → Customise Columns → Create Custom Metric). Do it once; it pays for itself weekly.

---

## Part B — The benchmark table

Thresholds calibrated to this account: $56 AOV, 4.2–4.4% site conversion rate, target CPA ~$30.

| Metric | 🔴 Kill | 🟡 Iterate | 🟢 Scale |
|---|---|---|---|
| **Hook rate** | < 20% | 20–28% | **> 28%** |
| **Hold rate** (ThruPlay ÷ 3s) | < 12% | 12–20% | **> 20%** |
| **Outbound CTR** | < 0.7% | 0.7–1.2% | **> 1.2%** |
| **CPC (outbound)** | > $2.50 | $1.50–2.50 | **< $1.50** |
| **Add-to-cart rate** (ATC ÷ outbound clicks) | < 6% | 6–12% | **> 12%** |
| **CPA** | > $45 | $30–45 | **< $30** |
| **ROAS** | < 1.2 | 1.2–1.8 | **> 1.8** |
| **Frequency** (7d) | > 3.0 → refresh | 2.0–3.0 | < 2.0 |

> **Calibrate these to yourself after 30 days.** Take your account's own median for each metric and set 🟢 at roughly the 75th percentile and 🔴 at the 25th. Industry benchmarks are a starting point; your account's own distribution is the truth.

### Your breakeven, computed properly

```
Contribution margin per order = AOV × (1 − discount rate) − COGS − shipping − payment fees
Breakeven ROAS                = AOV ÷ contribution margin
Target CPA                    = contribution margin × (safety factor, 0.7–0.85)
```

**Worked example** (replace with real numbers):
AOV $56 · effective discount already reflected in AOV · COGS $9 · shipping $6 · fees $2
→ contribution = $56 − $17 = **$39**
→ breakeven ROAS = 56 ÷ 39 = **1.44**
→ target CPA at 0.8 safety = **$31**

**The lever most people miss:** repeat rate went 1.0% → 7.8% between January and May, doubling monthly, with a 90–120 day reorder window. If you have a Day-75 reorder flow live, your **90-day LTV** is materially above first-order AOV, and your allowable CPA rises with it. Compute LTV:CAC quarterly and raise your target CPA deliberately. Without the flow, hold the line at first-order breakeven — don't buy a customer you have no plan to keep.

---

## Part C — The diagnostic ladder

This is the part that makes you fast. Read the four numbers **in order** and stop at the first failure. Everything downstream of a failure is uninterpretable.

```
Hook rate < 20%?
   └─► THE HOOK IS DEAD. Nothing else matters — the body was never seen.
       Fix: new first 3 seconds. Keep the body, swap the hook. Try a
       different archetype entirely (04-hook-library.md). If it's a
       static, the headline or the image is the problem.

Hook rate OK, hold rate < 12%?
   └─► THE BODY LOSES HER. She stopped, then left.
       Fix: get to the mechanism faster; cut the first 3 seconds of the
       body; move a proof element earlier; shorten to 15s.

Hook + hold OK, CTR < 0.7%?
   └─► NO REASON TO ACT. She watched and didn't care enough to tap.
       Fix: the CTA is vague or the offer isn't on screen. State the
       bundle, the per-bottle price, and the guarantee explicitly.
       Add the offer as burned-in text, not just voiceover.

CTR OK, ATC rate < 6%?
   └─► MESSAGE MISMATCH AT THE LANDING PAGE. The ad promised something
       the page doesn't immediately confirm.
       Fix: match the landing page headline to the ad's hook. Send
       bundle-led creatives directly to the bundle selector, not the
       generic PDP.

ATC OK, purchase CPA too high?
   └─► CHECKOUT OR OFFER FRICTION.
       Fix: Apple Pay visible? Shipping cost a surprise? Guarantee
       stated at checkout? Is the pre-selected bundle the one the ad
       advertised?

Everything OK but ROAS low?
   └─► AOV PROBLEM, not a creative problem.
       Fix: push B3G3 harder in the creative. She buys 6 bottles ~40%
       of the time; every point you move that mix is pure margin.
```

**Why order matters:** a creative with a 12% hook rate and a "terrible" CTR does not have a CTR problem. Its CTR is meaningless — almost nobody saw the ad. Fixing the CTA would be wasted work. Always debug top-down.

---

## Part D — The weekly review (Mondays, 60 minutes)

```
0:00–0:10  Pull last 7 days, ad level, sorted by spend.
           Filter: spend ≥ $150 (below that, ignore — it's noise).

0:10–0:25  Fill in templates/creative-tracker.csv for every ad that
           completed its 7-day window. Four numbers each.

0:25–0:40  Apply the diagnostic ladder to every 🔴 and 🟡.
           Write one sentence per ad: what failed and what you'll change.

0:40–0:50  Decisions:
             🔴 KILL     → pause. Log why in the tracker.
             🟡 ITERATE  → build 2–3 variants fixing the diagnosed layer.
             🟢 SCALE    → move into BROAD ad set; raise budget 20–30%;
                           build 3 hook variants; build the Robert version.

0:50–1:00  Update the running scoreboards:
             · Which hook archetypes win (H1–H10)
             · Which angles win (A1–A12)
             · Which formats win
             · Which avatars win
           Next month's creative mix is weighted toward the winners.
```

---

## Part E — The account-level scorecard

Track weekly in `templates/weekly-report.md`:

| Metric | Target | Why it's on the list |
|---|---|---|
| Blended ROAS (Meta-reported) | > 1.8 | Directional |
| **Blended MER** (total revenue ÷ total ad spend) | > 2.0 | **The number that actually tells you if the business made money.** Meta over-reports; MER can't lie. |
| New-customer CPA | < $31 | The real cost of growth |
| AOV | > $56 and rising | Bundle mix is working |
| B3G3 share of orders | > 40% | Directly moves margin |
| Purchases/week | rising | Volume, not just efficiency |
| Testing spend as % of total | 15–25% | Are you feeding the future? |
| New creatives launched | 8–12/month | Your fatigue insurance |
| Creative win rate | > 20% | Is the research process working? |
| Repeat rate | rising from 7.8% | Where the margin actually is |

### Why MER matters more than ROAS here

Meta's reported ROAS uses its own attribution window (typically 7-day click / 1-day view) and will happily claim credit for purchases it influenced marginally. **MER = total store revenue ÷ total ad spend** is unfakeable. If Meta says 2.4 ROAS and your MER is 1.1, Meta is over-claiming. Your Triple Whale connection reconciles these — use it.

**Set a MER target, not a ROAS target.** Then use ROAS only for *comparing creatives against each other* within the same account, where the attribution bias is constant and therefore cancels out.

---

## Part F — Rules that stop you from fooling yourself

1. **Never judge before day 7 or before ~$350 spend on a creative.** Whichever comes later.
2. **Never judge on a metric with under 15 conversions.** A creative with 3 purchases and a 4.0 ROAS is noise. Rank it by CTR and hook rate until it has volume.
3. **Never compare creatives from different weeks.** Auction conditions change. Compare within a cohort launched together.
4. **Never kill a creative that has a great hook rate and bad CPA without trying a CTA fix first.** You've already paid for the hard part — attention. Trading it away is expensive.
5. **Watch frequency before you blame the creative.** A "declining" ad at frequency 3.2 isn't a bad ad; it's a saturated audience.
6. **Statistical honesty:** at ~$350 spend and ~12 purchases, you can detect large differences, not small ones. A 20% CPA gap between two creatives at that volume is not a real result. Only act on gaps of 40%+ or on the leading indicators (hook rate, CTR), which reach significance far faster because they have thousands of events instead of a dozen.

---

## Part G — The creative learning ledger

The compounding asset. After every review, append one row:

| Date | Creative | Hook archetype | Angle | Avatar | Hook rate | CTR | CPA | Verdict | **What it taught us** |
|---|---|---|---|---|---|---|---|---|---|
| 26-08-14 | 2608_ToF_LIN_3PMCRASH_UGC_H02 | H2 Swap | A2 | A | 31% | 1.4% | $27 | 🟢 Scale | Naming the specific hour ("3 PM") beats generic "afternoon" |
| 26-08-14 | 2608_ToF_LIN_WAKE_VSSL_H19 | H1 Listicle | A1 | A | 22% | 0.9% | $41 | 🟡 Iterate | Listicle opens slower; try dropping the count and leading with truth #1 |

That last column is the entire point. After 90 days you'll have 30+ rows and you will *know* what works for Linda — not believe it, know it. That knowledge is worth more than any individual winning ad, because winning ads fatigue and knowledge doesn't.
