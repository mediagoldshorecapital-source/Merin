# Klaviyo account reference — Prime Ingredients

Snapshot audited **2026-08-28** via the Klaviyo MCP server. Treat as a cache: if a live API
call disagrees, the API wins — update this file in the same commit.

## Account

| Field | Value |
|---|---|
| Account / public API key | `XTxzmw` |
| Organization | Prime Ingredients |
| Website | http://tryprimeingredients.com |
| Default sender name | Prime Ingredients |
| Default sender email | support@tryprimeingredients.com |
| Address | 7901 4th St N, Ste 300, St. Petersburg, FL 33702, US |
| Timezone | America/New_York |
| Currency | USD |
| Locale | en-US |
| Test account | No — this is production |

## Lists

| Name | ID | Opt-in | Notes |
|---|---|---|---|
| Email List | `Uisyj7` | single | Default marketing audience |
| Preview List | `VtRpcX` | single | Klaviyo default preview/test list |
| Text Messaging List | `WbvGaY` | double | SMS |

## Segments

| Name | ID | Active |
|---|---|---|
| New Subscribers | `YrG7Bi` | yes |

Only the Klaviyo default segment exists. No engagement tiers (30/60/90-day engaged),
no purchaser/non-purchaser, no VIP, no sunset segment. Building these is a prerequisite
for sane sending once a domain is verified.

## Flows

| Name | ID | Status | Trigger |
|---|---|---|---|
| Test Welcome Series - Standard | `U85zrU` | **draft** | Added to List |

No live flows. Nothing is automated.

## Campaigns (email) — all Draft, none ever sent

| Name | ID | Created | Audience |
|---|---|---|---|
| Campaign Jul 1, 2026, 12:26 AM | `01KWCY85MAE5X0CY9XHB0Y5GVV` | 2026-06-30 | `RRP87h`, `Vn3CLR`, `XMuyTX` |
| NMN Welcome — Meet NMN (2026-07-01) | `01KW9NJQ64EV43WSPAS03WTYB5` | 2026-06-29 | `Uisyj7` |
| NMN Welcome — Meet NMN — 2026-06-26 | `01KW29ECNW9KHEF3013WFPB7ES` | 2026-06-26 | `YrG7Bi` |
| NMN Welcome Newsletter | `01KW16N2QB452AW0MQS6HW5Z5N` | 2026-06-26 | `Uisyj7` |
| First Newsletter — Multi Collagen Peptides Spotlight | `01KW0499WS6H6R1N4GCQ64B7JV` | 2026-06-25 | `Uisyj7` |

The three NMN Welcome drafts overlap heavily — consolidate to one before building more.
The Jul 1 draft targets three audience IDs that do not appear in the current list or segment
listings; verify or archive it.

Known template: `VKP9Rs` (Multi Collagen spotlight) —
https://www.klaviyo.com/email-editor/VKP9Rs/edit

## Integrations and metrics

Shopify (`0eMvjm`) is connected and emitting ecommerce events.

| Metric | ID | Integration |
|---|---|---|
| Placed Order | `Rq4Abs` | Shopify |
| Ordered Product | `Y3njW9` | Shopify |
| Checkout Started | `TJSfXa` | Shopify |
| Added to Cart | `VgDkwX` | Shopify |
| Viewed Product | `UcCMSZ` | API |
| Viewed Collection | `VBiesJ` | Shopify |
| Submitted Search | `WpnAGH` | Shopify |
| Fulfilled Order | `YzL8dn` | Shopify |
| Fulfilled Partial Order | `UC2Pyn` | Shopify |
| Delivered Shipment | `TL8n9r` | Shopify |
| Marked Out for Delivery | `Sswvv7` | Shopify |
| Cancelled Order | `UYUmcq` | Shopify |
| Refunded Order | `Wajc6g` | Shopify |
| Subscribed to Back in Stock | `XjJ2Y8` | Klaviyo |
| Active on Site | `T3dWZ9` | API |
| Received Email | `TuYuUY` | Klaviyo |
| Opened Email | `RGyBqv` | Klaviyo |
| Clicked Email | `SqcUnw` | Klaviyo |
| Bounced Email | `UCXzGF` | Klaviyo |
| Dropped Email | `Wrptda` | Klaviyo |
| Marked Email as Spam | `SQxGcc` | Klaviyo |
| Skipped Send | `VfYCji` | Klaviyo |
| Subscribed to Email Marketing | `RJP7xW` | Klaviyo |
| Unsubscribed from Email Marketing | `SBQFcd` | Klaviyo |
| Manually Suppressed from Email Marketing | `VVBV8N` | Klaviyo |
| Subscribed to List | `WzGXNa` | Klaviyo |
| Clicked email to unsubscribe | `R47NFH` | Klaviyo |
| Merged Profile | `RXN6Zs` | Klaviyo |

SMS metrics also exist (`XXVzFt` received, `RSZCbZ` opened, `RXCSxp` clicked, `YwjmWG` sent,
`UVtAVJ` subscribed, `T93Hrf` unsubscribed, `VyuDym` failed, `XTijk5` relayed,
`Sw2ENC` / `W6SrPA` automated response).

## Gaps — verified empty

| Check | Result | Consequence |
|---|---|---|
| `get_sending_domains` | **empty** | No authenticated domain. Cannot send safely. Blocker #1. |
| `get_catalog_items` | **empty** | Dynamic product blocks and recommendations will not render. Hardcode product content. |
| `get_coupons` | **empty** | `PRIME10` etc. are Shopify discounts, not Klaviyo coupons. Klaviyo coupon variables will fail. |
| Live flows | **none** | All lifecycle revenue unearned. |
| Sent campaigns | **none** | No performance baseline exists. |

## Klaviyo AI Customer Agent

Not provisioned. `get_customer_agent`, `get_agent_skills`, `get_agent_tools`, and
`list_customer_agent_conversations` all return `Company does not exist` while ordinary
account endpoints succeed — the feature is not enabled for `XTxzmw`.

## Recommended sequence

1. Add and DNS-verify a sending domain (e.g. `send.tryprimeingredients.com`); confirm the
   from-address sits on it.
2. Enable the Shopify catalog sync so product blocks work.
3. Build engagement + purchaser segments.
4. Consolidate the five drafts to one sendable newsletter.
5. Build Welcome, then Abandoned Checkout, then Browse Abandon — draft, then hand off to a
   human to set live.
6. Warm up: start with the most engaged slice, ramp volume over 2–4 weeks.
