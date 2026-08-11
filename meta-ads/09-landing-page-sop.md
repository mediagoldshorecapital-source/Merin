# 09 — Landing Page SOP

The most common cause of "the ads don't work" is that the ads worked and the page didn't
finish the job.

**The core rule:** if the ad hooked her on brain fog, the page must open on brain fog. Send
her to a generic homepage and you break the argument mid-sentence — she has to re-orient,
and a 62-year-old on an iPad does not re-orient. She leaves.

---

## 1. The page map

| Ring | CTA | Destination | Why |
|:---:|-----|-------------|-----|
| **1** `3PMCRASH` | Learn More | `/pages/energy-advertorial` | Cold. Needs the argument finished before a price |
| **2** `BRAINFOG` | Learn More | `/pages/clarity-advertorial` | Cold. Rational buyer, wants mechanism |
| **3** social proof | Learn More | `/pages/energy-advertorial` | Cold. Proof-led, lands on the primary story |
| **4** direct offer | Shop Now | `/products/nmn-complex?variant=b3g3` | Warm. She's decided. Get out of the way |
| **5** objection | Shop Now | `/products/nmn-complex?variant=b3g3` | Warm |

**Minimum viable build: two advertorials + one bundle-preselected product page.** Do not
launch with fewer.

---

## 2. Advertorial anatomy (Rings 1–3)

"Ugly" outperforms "designed" here, consistently. The page should look like an article
someone wrote, not a brand asset someone commissioned.

```
┌──────────────────────────────────────────┐
│  [NO TOP NAVIGATION]                     │ ← removing the nav is worth
│  small logo only, no menu, no cart icon  │   several points of CVR
├──────────────────────────────────────────┤
│  HEADLINE — echoes the ad hook verbatim  │
│  Subhead — the reframe                   │
├──────────────────────────────────────────┤
│  Author byline + date (real person)      │
├──────────────────────────────────────────┤
│  Story: her problem, in her language      │
│  ~200 words. No product yet.              │
├──────────────────────────────────────────┤
│  The mechanism: NAD+ decline. Simple      │
│  diagram. Still no product.               │
├──────────────────────────────────────────┤
│  The solution category: what NMN is       │
├──────────────────────────────────────────┤
│  ▶ FIRST CTA — soft                       │ ← ~50% scroll depth
├──────────────────────────────────────────┤
│  Why most NMN fails: dose, purity,        │
│  testing → why this one is different      │
├──────────────────────────────────────────┤
│  Testimonials — MATCHING THIS PAGE'S      │ ← a fatigue page shows
│  PAIN POINT ONLY                          │   fatigue reviews. Non-negotiable
├──────────────────────────────────────────┤
│  Offer block: Buy 3 Get 3 Free, all six   │
│  bottles shown, guarantee, lab badge      │
├──────────────────────────────────────────┤
│  ▶ MAIN CTA — large, high contrast        │
├──────────────────────────────────────────┤
│  FAQ / objection handling                 │
├──────────────────────────────────────────┤
│  ▶ FINAL CTA                              │
├──────────────────────────────────────────┤
│  Footer: contact, returns, disclaimers    │ ← keep these. Older buyers
└──────────────────────────────────────────┘   check them before buying
```

### Headline matching — the single highest-leverage element

| Ad hook | Page headline |
|---------|---------------|
| "It's three o'clock and I'm already done for the day." | **"How Women Over 50 Are Beating The 3 PM Crash By Restoring Their Cellular Energy"** |
| "I stood in my kitchen and couldn't remember why I'd walked in." | **"The 1000mg Daily Habit That Clears Menopause Brain Fog"** |
| "I'd been burned by supplements before. Three times." | **"Why Most NMN Supplements Do Nothing — And How To Read The Label"** |

The page headline should feel like the *next sentence* of the ad, not a new conversation.

---

## 3. Non-negotiable page rules

| # | Rule | Why |
|---|------|-----|
| 1 | **Remove top navigation** | Every menu item is an exit. On advertorials this is worth several points of CVR |
| 2 | **Testimonials must match the page's pain point** | A brain-fog page showing joint-pain reviews tells her this isn't for her |
| 3 | **Preselect the Buy 3 Get 3 Free variant** | Never make her configure. Default to the bundle |
| 4 | **Show all six bottles physically** | Quantity sells; percentages don't |
| 5 | **Apple Pay / Shop Pay above the fold at checkout** | She's on an iPad and will not type a card number |
| 6 | **Minimum 18px body type, 1.6 line height** | Eyesight is a real constraint, not a metaphor |
| 7 | **Load < 3s on 4G, tested on a real iPad** | Tablet converts at 5.11% — the highest device. Protect it |
| 8 | **Trust marks near the CTA** | Lab certificate, money-back guarantee, made-in, real contact details |
| 9 | **Guarantee stated in plain language** | "Send it back within 30 days, we refund you." Not legalese |
| 10 | **UTM parameters preserved through redirects** | The #1 silent attribution killer. Test it |
| 11 | **No countdown timers or fake scarcity** | Her core objection is being deceived. A fake timer confirms it |
| 12 | **Shipping cost shown before checkout** | Late shipping reveals are the top ATC→Purchase leak |

---

## 4. The iPad test (do this on an actual iPad)

Tablet is your highest-converting device. Test on the device, not on a resized browser.

- [ ] Page loads in < 3s on cellular
- [ ] Headline fully visible without scrolling, portrait **and** landscape
- [ ] Body text readable at arm's length
- [ ] CTA buttons ≥ 44×44pt tap target
- [ ] No horizontal scroll
- [ ] Video (if any) autoplays muted with captions
- [ ] Apple Pay appears at checkout
- [ ] Form fields don't trigger awkward zoom
- [ ] Sticky CTA doesn't cover content

---

## 5. Instrumentation

Every page needs measurement or you cannot diagnose file 07 §6.

- [ ] `ViewContent` fires on load
- [ ] `AddToCart` fires on add
- [ ] `InitiateCheckout` fires at checkout
- [ ] Scroll-depth tracking at 25 / 50 / 75 / 100%
- [ ] CTA click tracking, per CTA position
- [ ] UTMs captured into the order record (so Shopify can attribute back to the ad)
- [ ] Heatmap tool (Clarity/Hotjar) live for the first month

**Read weekly:**

| Metric | Target | If below |
|--------|--------|----------|
| LP view rate (LP views ÷ clicks) | ≥ 85% | Page speed, or a broken redirect |
| Scroll to 50% | ≥ 45% | Headline/opening doesn't match the ad |
| CTA click rate | ≥ 12% | Offer block is buried or unconvincing |
| ATC rate | ≥ 6% | Price shock, or trust gap |
| ATC → Purchase | ≥ 35% | Checkout friction, shipping cost reveal |

---

## 6. Testing pages (without breaking the ads)

Only ever test **one page element per 14-day cycle**, and never during a creative test —
otherwise you cannot attribute the result to either.

**Priority order (highest impact first):**
1. Headline — must it match the ad hook more literally?
2. Offer presentation — bundle framing, how the six bottles are shown
3. Testimonial selection — matched to the pain point?
4. CTA placement and wording
5. Page length
6. Everything else

Route the test at the **ad destination URL** level rather than with a client-side split
tester — client-side testers add load time on exactly the device you can least afford to
slow down.

---

## 7. Build checklist

- [ ] Two advertorials live (energy, clarity), matched to Rings 1–3
- [ ] Product page with the B3G3 variant preselected, for Rings 4–5
- [ ] Nav removed on advertorials
- [ ] Testimonials segmented by pain point
- [ ] All 12 non-negotiable rules verified
- [ ] iPad test passed
- [ ] Instrumentation verified with a real test journey
- [ ] UTMs survive end-to-end into the Shopify order
- [ ] Apple Pay / Shop Pay enabled
- [ ] Legal: supplement disclaimer, "individual results vary", FDA statement, returns policy
- [ ] Prices match the ad creative **exactly**

---

**Back to:** [`README.md`](README.md) · **Templates:** [`templates/`](templates/)
