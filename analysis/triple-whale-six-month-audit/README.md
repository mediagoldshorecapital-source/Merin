# Triple Whale — Six-Month Data Audit (Jan–Aug 2026)

A full read of the Triple Whale warehouse for **Prime Ingredients**
(`w1rbg9-wu.myshopify.com`), covering **1 January – 7 August 2026**. Written to
answer: what are the patterns, blind spots, errors, and places for improvement
before any further action is taken.

- Report: `report.html` (standalone, no external assets)
- Published version: https://claude.ai/code/artifact/7de229c1-7803-4366-9625-e69047c9f610

## Headline

| Metric | Value |
| --- | --- |
| Revenue (Jan 1 – Aug 7) | $493,300 |
| Meta ad spend | $381,106 |
| Orders | 8,074 |
| Blended ROAS | 1.29 |
| **Breakeven ROAS** | **~1.70** |
| Contribution profit (May – Aug 7) | **−$45,317** |

After COGS, payment fees, shipping and refunds, ~59¢ of every revenue dollar is
left to pay for advertising. That sets breakeven blended ROAS at ~1.70. Actual
has been 1.22–1.43 since May. August (1.77) is the first month above the line,
and only because spend was cut roughly in half.

## Data integrity — three findings that invalidate parts of the warehouse

1. **27-day order gap, Apr 6 – May 2.** Only 11 orders recorded in the window,
   while Meta kept spending ~$2,100/day and reported 25–67 conversions/day.
   Meta's April totals: 1,383 conversions worth $88,269 vs 264 recorded orders.
   This is a Shopify → Triple Whale sync failure, not a business collapse.
   ~$90–100K of revenue is missing. **April's 0.28 ROAS is fiction.**
2. **No COGS before May.** 0% coverage Jan–Apr, then 94–97%. Applying July's
   actual 30.8% ratio, February's reported `+$21,293` net profit was really
   ~`+$5,800`; March's `+$35,637` was really ~`+$4,500`.
3. **No attribution before June.** Pixel produced zero sessions until May and
   only became meaningful in June. **$230,883 of Jan–May spend flew blind.**

Also open: shipping cost is defaulted to equal shipping revenue (Jan–May),
handling fees are $0 in every month, the checkout event fires on ~63% of
purchases (July: 1,491 checkouts vs 2,364 orders), Klaviyo sends no engagement
data at all, inventory is corrupt (1.3B items / $88.2B value), three of four
products have null COGS, and ad naming is inconsistent enough to fragment
creative reporting.

## Unit economics

The whole business reduces to one ratio.

| Order type (July) | Orders | AOV | Contribution | Acq. cost | Net |
| --- | ---: | ---: | ---: | ---: | ---: |
| New subscription | 1,646 | $57.92 | $36.37 | $58.32 | **−$21.95** |
| Recurring charge | 495 | $60.78 | $37.34 | $0.00 | **+$37.34** |
| One-time | 75 | $43.44 | $34.70 | $58.32 | −$23.62 |

You lose $21.95 acquiring a subscriber and make $37.34 on each re-bill, so
breakeven is **0.59 recurring charges per new subscriber**. June's 460 new subs
produced 495 recurring charges in July (108%); July's 1,646 are tracking to
~1,067 in August (65%). Both clear the bar, narrowly, on two months of history.

## The subscription pivot (the one thing working)

Subscription share of orders: **0% in May → 58.7% June → 96.6% July → 98.5%
August.** Recurring charges: 36 → 495 → 249 (in 7 days).

Two notes:
- **Recurring charges are discounted 37.9%** (up from 5.1% in June). Recurring
  revenue needs no acquisition incentive. Cutting to 20% is worth ~$6,700/month
  at July volume and scales with the base.
- The odd June cohort (55.5% repeat vs 5–16% elsewhere) is the subscription
  launch re-billing, not a behaviour change. True organic repeat is 4.8–6.1%.

## The ROAS trap in media

Highest ROAS ≠ best campaign here.

| Campaign (Jun 8 – Aug 7) | Spend | ROAS | % new | New-cust. CAC |
| --- | ---: | ---: | ---: | ---: |
| 9. NMN Scale (CBO) Jun 27 | $75,443 | 1.20 | 85% | **$57.68** |
| 4. N2 Testing (CBO) Jan 27 | $33,501 | 1.75 | 51% | $67.95 |
| 8. NMN Testing (CBO) Jun 21 | $13,616 | 0.98 | 71% | $83.54 |
| 7. N2 Testing (CBO) May 28 | $11,410 | 1.78 | 57% | $68.73 |
| 11. Astaxanthin Scale (CBO) Jun 27 | $7,111 | 0.73 | 74% | $92.35 |

Campaign 4's ROAS advantage comes substantially from harvesting existing
buyers — shifting budget there will not produce proportional new customers.
The real waste is **campaigns 8 and 11**: $20,727 at 0.98 and 0.73 ROAS.

Same trap at creative level: the 3.4×–6.1× ROAS ads are 74–92% *returning*
customers at $64–146 per new customer. Genuine performers are Video Ad 1 Copy 2
($51.12) and Video Ad 3 ($53.32).

## Concentration risk

- **Product** — 93.5% of gross from one SKU ($412,817 of $441,279)
- **Channel** — 100% of paid spend on Meta, all eight months
- **Country** — 99.96% US (5,031 of 5,033 orders)
- **Discounting** — ~35% of gross, every month, on 95% of orders, and it is
  *not* code-driven (4,775 orders show "no discount" yet carry a 34.6%
  markdown). `gross_product_sales` is therefore a list price nobody pays.

Healthy: refund rate 2.85%, AOV stable at $55–62, conversion rate climbing
(3.85% → 5.13% → 7.34%).

## Recommended order of action

1. Stop discounting recurring charges (≈ +$6,700/month, no traffic change)
2. Kill campaigns 8 and 11; move budget to campaign 9, **not** campaign 4
3. Open a Triple Whale ticket for the Apr 6 – May 2 backfill
4. Fix cost settings (product COGS, real shipping rates, handling fees) and
   backfill to January
5. Repair the checkout event and the Klaviyo data feed
6. Instrument subscription churn weekly before scaling spend again
7. Begin reducing single-channel / single-product exposure

## Method & caveats

Figures read directly from the warehouse via the Triple Whale MCP tools on
10 August 2026, in the shop's timezone (America/New_York) and currency (USD).
Sources: `orders_table`, `ads_table`, `blended_stats_tvf`, `pixel_joined_tvf`,
and the configured Summary KPIs.

Contribution profit = revenue − COGS − ad spend − payment gateway costs −
shipping costs − refunds. It **excludes overheads, salaries and software**, so
it is an upper bound on true profit. Because shipping cost and handling fees are
under-recorded (see finding 4 in the report), the real picture is somewhat worse
than shown. April figures appear as recorded and are known to be incomplete.
