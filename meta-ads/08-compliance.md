# 08 — Compliance Guardrails

Read before publishing anything. A rejected ad costs a day. A restricted ad account costs the business — and this account currently runs 94% of its revenue through Meta, so there is no fallback channel if it goes down.

**This is practical risk guidance from an advertising-operations perspective, not legal advice.** Supplement claims and FTC endorsement rules are areas where a qualified regulatory or advertising attorney should sign off on your claim set once, after which this document becomes your day-to-day checklist.

---

## 1. The four things that will actually get you in trouble

### 1.1 Fabricated reviews and testimonials

The source material describes a **"Fake Comment" ad** — a comment-styled frame with a review inside it. The *format* is fine and it works. **Writing a review that no customer wrote is not.**

The FTC's rule on consumer reviews and testimonials (16 CFR Part 465, in force since October 2024) makes fake and misrepresented consumer reviews explicitly unlawful and carries civil penalties per violation. Meta's policies prohibit it independently.

**Our rule:**
- Every quoted review is **verbatim** from a real customer.
- Attributed with first name + last initial (+ city if you have it).
- No invented like counts, comment counts, or engagement numbers.
- No stock photo standing in as the reviewer's face — use an initial circle.
- Trimming for length is fine; mark it with an ellipsis. Changing words is not.

This costs you nothing — you have 5,128 real reviews, which is more than enough raw material.

### 1.2 Meta's personal attributes policy

Meta prohibits ad copy that asserts or implies knowledge of a person's personal attributes — including **health and medical conditions**. Second-person copy about how the reader feels is the classic trigger.

| ⚠️ Risky (implies you know her condition) | ✅ Compliant rewrite |
|---|---|
| "Feeling more tired as you age?" | "Most women over 60 blame it on age. It's usually cellular energy." |
| "Your brain fog isn't normal" | "Brain fog after 60 is common. It isn't inevitable." |
| "Struggling with post-menopause fatigue?" | "Post-menopause fatigue is one of the most common reasons women try NMN." |
| "You can't keep up with your grandkids anymore" | "Keeping up with the grandkids is the #1 reason our customers say they started." |
| "Your doctor said it's normal" | "'It's normal' and 'there's nothing you can do' are two different sentences." |

**The mechanical fix:** move from *"you have X"* to *"people who have X"* or *"our customers say."* Third person, category-level, or customer-attributed. You keep the emotional hit and lose the policy exposure.

Note that the brand's existing hook — *"Feeling more tired as you age? It's not just aging"* — sits right on this line and is on the product page. It is being tolerated today. Test the third-person variant alongside it: if it performs comparably, you have removed a standing risk for free, and you'll want that variant already proven if the original ever starts getting rejected at scale.

### 1.3 Disease claims

A dietary supplement may make **structure/function** claims. It may not claim to diagnose, treat, cure, mitigate or prevent a disease. Crossing that line reclassifies the product as an unapproved drug.

| ❌ Never write | ✅ Instead |
|---|---|
| Prevents dementia / Alzheimer's | Supports mental clarity and focus |
| Treats menopause symptoms | Supports energy through the changes after 50 |
| Reverses aging | Supports healthy aging |
| Cures chronic fatigue | Supports cellular energy production |
| Replaces your medication | (never reference medication at all) |
| Clinically proven to… | (only if you hold the study **on this product**, and can produce it) |

**Also banned in our copy:** naming any disease at all — dementia, Alzheimer's, diabetes, chronic fatigue syndrome, osteoporosis. Even in a "not a treatment for" construction. Don't put the word in the ad.

**Structure/function disclaimer:** where required, carry the FDA disclaimer on the landing page — *"These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease."* Keep it at 28px minimum if it appears in a creative.

### 1.4 Substantiation — you must be able to produce the document

Every factual claim in an ad needs a file behind it, before the ad runs.

| Claim | Document you must hold |
|---|---|
| **"64% of NMN products fail lab tests"** | The study or testing report, with a citable source. `[CONFIRM]` — this is the highest-value and highest-risk stat in the whole plan. Do not run it until the source is in a folder. |
| "5,128 reviews" | Live review platform count. Never round up. Update the asset when it drifts. |
| "As seen in Forbes / ELLE" | The actual articles, live URLs, and confirmation you have rights to use the marks |
| "Third-party lab tested" | Current COA for the batches you're shipping |
| "500K+ customers" | Order/customer count from Shopify |
| "NAD+ drops ~50% between 40 and 60" | The published research you're citing |
| "[XX]-day money-back guarantee" | Your published policy, matching exactly what the ad says |

---

## 2. Format-specific risks

| Format | Risk | Mitigation |
|---|---|---|
| **02 Comment Frame** | Fabricated review; implying it's a real Facebook comment thread | Real reviews only; style it as a brand-designed card, not a pixel-perfect Facebook screenshot |
| **05 IG-Organic** | Deceptive-format concerns if it impersonates organic content too closely | It runs with Meta's own "Sponsored" label attached; don't fabricate native UI implying engagement that didn't happen |
| **07 iMessage** | Implying a genuine captured conversation between real people | Include a brand lockup; style as an illustration, not a forged screenshot |
| **10 Pain Split** | Reads as a clinical before/after | No dates, no "results in X days" framing, no medical imagery. It's an illustration of a feeling. |
| **09 Us vs Them** | Disparagement of a named competitor | Never name a brand. Compare against the category or against doing nothing. |
| **11 Big Stat** | Unsubstantiated statistic | Every number needs its file (§1.4) |
| **12 Bundle Maths** | Misleading pricing | The struck-through $29.98 must be a genuine regular price the product actually sells at |

---

## 3. NMN's regulatory status — know this before you scale

FDA has taken the position that NMN is **excluded from the dietary supplement definition** because it was authorised for investigation as a new drug — a position it stated in 2022 and which led to major marketplaces (notably Amazon) delisting NMN products. The industry has contested it and the position has moved around.

**What this means practically:**
- The category sits under more scrutiny than a typical supplement. Conservative claims are not just safer, they're strategically correct.
- Aggressive longevity/anti-aging language raises your profile in exactly the wrong way.
- **Verify the current status with a regulatory advisor before scaling spend materially.** My knowledge has a cutoff and this specific area has been in motion.

This is not a reason to stop advertising. It is a reason to keep every claim boringly defensible and to have the substantiation folder built before the spend goes up — because the time to have your documents in order is before anyone asks.

---

## 4. Pre-publish compliance check

Run on every creative. It's point 26 of the QA list in `04-design-system.md`.

- [ ] No disease named, anywhere, in any construction
- [ ] No cure / treat / prevent / reverse language
- [ ] No second-person assertion about her health ("your brain fog", "you're tired") — third person or customer-attributed instead
- [ ] Every review verbatim, real, and attributed
- [ ] No fabricated engagement counts or invented reviewers
- [ ] Every statistic has a document in the substantiation folder
- [ ] No competitor named
- [ ] Strikethrough price is a genuine regular price
- [ ] Guarantee length in the ad matches the published policy exactly
- [ ] Any person shown reads as 55–70 and isn't presented as a customer unless they are one
- [ ] Landing page carries the FDA structure/function disclaimer
- [ ] Any on-image legal text ≥ 28px

---

## 5. If an ad gets rejected

1. **Don't immediately resubmit the same file.** Repeated rejections compound into account-level flags.
2. Read the stated policy. Map it to §1.2 (personal attributes) or §1.3 (health claims) — those two cover the large majority of rejections in this category.
3. Fix the copy using the rewrite tables above, save as a **new** version (`v02`), and publish as a new ad.
4. Appeal only when you're confident the rejection was wrong, and appeal once.
5. Log every rejection in the tracker with the policy cited. After a month you'll see a pattern, and the pattern is usually a single phrase you can permanently retire from the copy bank.
