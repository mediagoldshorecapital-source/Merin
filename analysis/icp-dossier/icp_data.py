# -*- coding: utf-8 -*-
"""Four-ICP dossier + verbatim quote bank. Single source for xlsx + html.

Confidence markers used throughout:
  [M] Measured  - Triple Whale warehouse or the 468-comment corpus
  [R] Research  - NMN Deep Customer Intelligence Report, 20 May 2026
  [I] Inferred  - reasoned from the above, explicitly not observed
"""

# ---------------------------------------------------------------------------
# OPERATIONAL FINDINGS - customers' own words, ahead of the personas
# ---------------------------------------------------------------------------
FINDINGS = [
 dict(sev="critical", title="Customers say orders never arrive — and are organising to report you",
  body="The single largest negative theme in the corpus. Buyers describe paying, receiving no tracking, "
       "getting an automated 'page responded privately' reply, and then escalating to their bank, the BBB "
       "and Meta itself. Several explicitly say they are reporting the page to get it removed from Facebook, "
       "TikTok and Instagram. For a business that takes 100% of its paid traffic from Meta, an organised "
       "report campaign is an existential risk, not a customer-service issue.",
  quotes=["Scam alert! Took my payment and never got my product. I also cannot get communication other then the automated 'page responded privately' comment.",
          "I ordered a product on May 10th and have still not received it, I called Prime Ingredients or what I thought was and it was a completely different website, they said they have been getting calls for about a year. What's up are you legit??",
          "I'll comment SCAM and continue to get this rogue company off Facebook. Just reported and intend to escalate further",
          "Scam. Stay away from this company. Also please report so they can get booted from Facebook, tik tok and instagram. This products is great. Ended up getting mine off Amazon after paying this company and never receiving my order"],
  action="Pull fulfilment SLA and the unshipped-order backlog today. Establish whether this is a real "
         "operational failure or a tracking-communication failure — the fix is completely different, but "
         "the reputational damage is identical either way."),

 dict(sev="critical", title="Your ads appear to show a competitor's product",
  body="Roughly 22 usable comments — the largest single identifiable theme — say the bottle in the video is "
       "Micro Ingredients, while the shop page sells Prime Ingredients. Commenters describe zooming in on "
       "the footage, note the 'M' on the cap, and post links to the competitor's site. Several conclude the "
       "brand is a knock-off. This is a claim being made publicly by customers; treat it as an allegation to "
       "verify, not an established fact — but verify it urgently, because it is doing more damage to trust "
       "than any messaging weakness in the account.",
  quotes=["You show MicroIngredients bottle in your ad, but sell a different brand… fake and buyer beware… buy only on MicroIngredients site.",
          "that video and the product in the video is from Micro Ingredients (do a screen shot and zoom in). Micro ingredients has their own Amazon shop and their own website. This company is trying to use the images of Micro Ingredients",
          "Why is the bottle different from the one the lady on the commercial is holding. Hers has the letter M at the top of the bottle and the one that would be purchased says Prime up top?",
          "The labels you have are BLUE in the video! The ones for sale on the shop now button are PURPLE! That a RED flag for me!"],
  action="Audit every running video against the actual product you ship. Any asset showing another brand's "
         "packaging comes down today. This is legal exposure as well as a trust problem."),

 dict(sev="critical", title="The forced subscription is costing you sales, stated out loud",
  body="At least eight commenters say plainly that they wanted to buy and did not, because they could not find "
       "a one-time purchase option. This corroborates the warehouse: 97% of orders carry the subscription flag "
       "while the Subscribe & Save SKUs have sold nine units in total — meaning enrolment happens at checkout, "
       "not by product choice. Others describe being billed repeatedly and having to change their bank details "
       "to stop it. Each of these comments sits publicly under a live ad, where the next prospect reads it.",
  quotes=["I wanna order but I don't want a subscription and it says you can opt out below but I can't find the opt out selection or I would've purchased",
          "You need to make it available For a single purchase.... The subscription is stopping me .",
          "I bought this one time and they kept sending more every month and kept billing me. I had to change my account to get them to stop",
          "They have hidden an automatic renewal, so if you order make sure to unchecked that box or in 3 months they will take a lot of money out of you account"],
  action="Ship a visible one-time purchase option and a self-serve cancel link this week. Note this also "
         "invalidates the 'cancel any time' creative concept until it is genuinely true."),

 dict(sev="high", title="A capsule-count expectation gap is generating 'half-empty bottle' complaints",
  body="Multiple buyers expected 120 capsules and received 30. The complaint surfaces in two forms — people "
       "who counted, and people who describe bottles as barely covered at the bottom and blame excess "
       "packaging. It also drives the price objection: at 30 capsules and two a day, a bottle is a fortnight, "
       "which makes the per-bottle anchor look dishonest rather than generous.",
  quotes=["It says 120 in the bottle but mine only had 30 in each one, why?",
          "30 capsules per bottle, that's two bottles per month which is $80/mo-- what a rip off",
          "I got 6 bottles, barely enough pills in each bottle to cover the bottom, I literally dumped all six into one & there's still room in the bottle",
          "30 capsules only,...if we take 2/ day,to get 1000 mg. we'll have it just for 15 days!"],
  action="Reconcile the count stated in ads and on the listing against what ships. If the product is 30 "
         "capsules, every 120-capsule reference has to go, and the per-bottle maths in the offer needs rebuilding."),

 dict(sev="high", title="The celebrity association is repelling the exact demographic you sell to",
  body="A large share of the corpus is women in the target age band reacting with hostility to a Kardashian "
       "association in the creative — the objections are about authenticity and cosmetic surgery, and they "
       "read as personally offended rather than indifferent. This audience explicitly compares herself to her "
       "peer group; a spokesperson she experiences as artificial breaks the mirror the research says the "
       "creative depends on.",
  quotes=["Liar,...it's all plastic surgery...please pls don't believe anything this woman says....",
          "I really can't stand the kardashians, and I don't really think anything.What about kim k would say, who cares",
          "Because no one wants to be like the Kardashians. Be a Beth!",
          "Seriously. A woman that had ribs taken out so her waist would shrink. This is your spokesperson"],
  action="Test peer-age, unbranded talent against the celebrity cut. The teardown already shows plain "
         "creative beating polished creative in this account; this is the same finding arriving from the audience."),

 dict(sev="high", title="Unanswered medical questions are unconverted buyers",
  body="A steady stream of specific, sincere eligibility questions goes unanswered in the comments: gastric "
       "bypass, dialysis, rheumatoid arthritis, osteoporosis, neuropathy, blood pressure, GLP-1 use, and an "
       "early-stage-cancer concern raised by one commenter. Each is a person far enough down the funnel to "
       "ask. Silence reads as evasion to an audience already primed to distrust supplements.",
  quotes=["Can I take this of o have gastric by pass 8 years ago",
          "Can you take this if you are a dialysis patient ?",
          "Is NMNs good for women who have osteoporosis?????",
          "Does this help with neuropathy? I'm seeing mixed reports."],
  action="Publish a plain eligibility and interactions FAQ, and answer these in-thread. Have the copy "
         "medically reviewed — do not improvise answers to the cancer question in a comment box."),

 dict(sev="medium", title="Dosing guidance is contradictory, and customers are correcting each other",
  body="Buyers are teaching each other how to take the product because you have not. The empty-stomach "
       "question recurs repeatedly, with people citing an outside scientist rather than your own materials. "
       "This is a cheap content gap with a direct retention consequence: someone who takes it wrong, sleeps "
       "badly and quits at week two never reaches the re-bill your economics depend on.",
  quotes=["Some say take on an empty stomach, some say take with food? Which is it? I was taking with food and heard another doctor say take on an empty stomach! Geesh..",
          "Better absorption on empty. Give it 30-60 minutes then eat something.",
          "I've been taking it on an empty stomach for about 4 months now. It really keeps me energized throughout my day. I forgot to take it in the morning a few times, so I took it in the evening. I wouldn't recommend that, it led to a few sleepless nights.",
          "You have to take three capsules at once.  Why"],
  action="Ship a one-page 'how to take it' asset into the Day 3 email, the packaging insert and a pinned comment."),
]

# ---------------------------------------------------------------------------
# THE FOUR ICPs - all 12 parts
# ---------------------------------------------------------------------------
ICPS = [
 dict(
  key="energy", name="Linda — Energy", tagline="The tired one who used to run everything",
  size="~55–60% of NMN buyers [I]", evidence="Strong — [M] orders, geography, timing · [R] ManyChat tag",
  colour="accent",
  headline_stats=[("Share of buyers", "~55–60% [I]"), ("AOV", "$60.37 [M]"), ("LTV", "$71.11 [M]"),
                  ("Repeat rate", "13.5% [M]"), ("Units/order", "2.94 [M]")],
  parts={
   "1. Who she is": "62, female, born 1955–1975, sweet spot 58–68 [R]. American (97.8% of traffic) [R]. "
     "Legacy email — AOL, Yahoo, Comcast, Juno — in ~40% of cases, meaning she adopted email 20–25 years ago and never moved [R]. "
     "First names cluster 1940s–1970s: Darlene, Polly, Janis, Peggy, Maureen [R]. Retired or working part-time. "
     "Married; her husband sees her as fine [R]. US-only in practice — 5,031 of 5,033 orders [M].",
   "2. Her day, hour by hour": "Current data, not the report's: order volume is essentially flat from 8 AM to midnight ET, "
     "peaking at 7 PM (296 orders) and 6 PM (291), with 11 AM fifth at 276 [M]. The only dead window is 2–7 AM [M]. "
     "The report's '11 AM is your single best hour' no longer holds. Day-of-week, controlled for spend: "
     "Friday best (1.25 ROAS, $48.47 CPA), Tuesday worst (0.99) [M]. Saturday is mid-pack; Monday is fine [M].",
   "3. How she finds you and what she buys": "Facebook ~60% of orders, Instagram ~34% — together 94% [R]. "
     "Google is 0.4% of orders but converts at 5.08%, the highest of any source [R]. Mobile 4.21% CVR, tablet 5.11% (highest), "
     "desktop 1.86% [R]. She is a bundle buyer: ~2.94 units per order now [M], down from the report's implied ~4.1 [R] — "
     "bundle size has fallen and that is a live AOV problem.",
   "4. Her geography": "Sun Belt and retirement corridor [R]. CA (588 orders), FL (396), TX (391), NY (219), IL (167), "
     "OH (162), GA (162), AZ (157) [R]. Arizona is the premium market — Tucson $82 AOV, Chicago $72, Henderson $67, "
     "New York $66 [R]. Houston ($43) and Miami ($47) are the weakest [R]. She lives where it is warm, in a house "
     "with a yard, near other retirees [I].",
   "5. Her deep insecurities": "Ranked: (1) I'm becoming invisible — she sits while others do; (2) I can't keep up with "
     "my grandchildren; (3) my body stopped listening to me — post-menopause; (4) I'm falling behind my friends; "
     "(5) I've been scammed before; (6) I can't afford to waste money; (7) my husband doesn't understand [R]. "
     "The surface pain is 'I'm tired all the time'. The real one is that her body is betraying the person she still "
     "believes she is [R].",
   "6. A day in her life": "Wakes 6:30, unrested after eight hours — the symptom that convinces her this is structural, "
     "not lifestyle [R]. Coffee and her existing supplement stack. Errands or volunteering 8:30–10. Sits down and scrolls "
     "late morning. The crash lands 2–4 PM and she considers a nap [R]. Evening in the recliner, TV on, phone in hand, "
     "Facebook Reels — this is now the peak buying window [M]. Bed around 10:30, and she will wake tired again [R].",
   "7. What she wants next": "Tier 1 — sleep support (she is demonstrably awake and ordering at midnight [M]), "
     "cognitive support, an ASTA+NMN bundle, a collagen+NMN bundle [R]. Tier 2 — menopause support, joint/mobility, "
     "eye health, a consolidated daily vitamin pack [R]. Her stack already exists; she wants it simplified, not extended [I].",
   "8. Her repeat behaviour": "13.5% of NMN-only buyers order more than once [M]; average 1.18 orders and $71.11 LTV [M]. "
     "The reorder window is 90–120 days, so a Day 75 email is the difference between a reorder and a defection [R]. "
     "Since June the subscription programme has overtaken this: 97% of orders now carry the subscription flag, and "
     "re-bills are the only profitable order type at $37.34 contribution against −$21.95 on acquisition [M].",
   "9. Male counterpart": "See ICP 4. Robert is 11.2% of named customers and outperforms her on both AOV and LTV [M].",
   "10. Discount and trust mechanics": "Zero discount codes used across 4,770 orders — the 75% is bundle structure, not a code [R]. "
     "She responds to the per-bottle anchor ($29.98 → $16.66), not to a percentage [R]. Effective discount has been stable "
     "at 33–37% since February [R][M]. The 'buy 3 get 3' works as a trust signal disguised as a discount [R]. "
     "But the trust mechanics are now actively broken — see the operational findings above [M].",
   "11. Best-friend card": "Linda, 62, Phoenix, retired teacher. Husband Bill, four grandchildren; the three-year-old is "
     "everything. She wakes unrested, walks the dog at 8, and by evening she is in the recliner with the TV on and her "
     "phone in her hand. She sees your ad, thinks that is exactly how I feel, and taps. She reads two reviews from women "
     "who sound like her, picks a bundle and pays with Apple Pay in four minutes. Three months later she runs out. "
     "Email her at Day 75 and she reorders; miss it and she buys elsewhere. [R]",
   "12. Emotion / JTBD / objection / trigger": "EMOTION — grief, for the person she used to be, under a surface of "
     "tiredness. JOB — 'get me back to being the one who does things, not the one who watches.' OBJECTION — "
     "'I've wasted money on supplements before and I'd be ashamed to do it again.' TRIGGER — sitting down while "
     "everyone else keeps moving; the 3 PM crash; declining something she'd once have said yes to. [R][I]",
  }),

 dict(
  key="clarity", name="Linda — Clarity", tagline="The one who is frightened of her own mind",
  size="Unsized — not measurable in the warehouse [R]", evidence="Weakest of the four — [R] only. Working hypothesis.",
  colour="warn",
  headline_stats=[("Share of buyers", "Unknown [R]"), ("AOV", "Not separable [—]"), ("LTV", "Not separable [—]"),
                  ("Repeat rate", "Not separable [—]"), ("Evidence", "Self-selection only [R]")],
  parts={
   "1. Who she is": "Demographically indistinguishable from Linda–Energy: same age band, geography, devices, email "
     "providers [R]. The difference is motivation, not profile. She self-selects 'Better focus / mental clarity' or "
     "'Longevity / healthy aging' in the ManyChat flow — tags NMN_Focus and NMN_Longevity [R]. "
     "CAVEAT: ManyChat tags are not in the warehouse. This segment cannot be sized, costed or tied to revenue with "
     "any data available here. Treat it as a working hypothesis for creative, not a measured segment.",
   "2. Her day, hour by hour": "Same pattern as Linda–Energy [M]. One difference worth testing: her fear is worst at "
     "night, and overnight ordering (127–206/hour, 11 PM–1 AM) is unusually high for this demographic [R][M]. "
     "Rumination is a plausible driver [I].",
   "3. How she finds you and what she buys": "Same channels [R]. She is the most likely of the four to research before "
     "buying, which makes her the natural fit for the untapped search channel — Google converts at 5.08% and is 0.4% "
     "of orders [R]. She reads the mechanism, not the offer [I].",
   "4. Her geography": "Indistinguishable from Linda–Energy [R].",
   "5. Her deep insecurities": "(1) Am I losing my mind — she watched her mother, aunt or friend go through dementia, "
     "and every forgotten name lands as a cold wave of fear that this is how it starts [R]; (2) I'm running out of time; "
     "(3) I'll become a burden to my children; (4) losing the word mid-sentence in front of people [R]. "
     "This is the most acute fear in the entire research and the least addressed in the creative [I].",
   "6. A day in her life": "The specific moments are social rather than physical: blanking on a grandchild's name at a "
     "birthday, stopping mid-sentence at dinner while people wait, re-reading the same paragraph [R][I]. "
     "She does not talk about it, including to her husband [R].",
   "7. What she wants next": "Cognitive support is the clearest Tier 1 opportunity in the report and maps directly to "
     "her [R]. Also eye health (ASTA_Eye_Health is an existing tag) [R]. She would buy a memory-specific SKU before "
     "she would buy a second energy SKU [I].",
   "8. Her repeat behaviour": "Not separable in the warehouse [—]. Hypothesis worth testing: fear-driven buyers retain "
     "better than benefit-driven ones because the fear does not resolve, so the subscription is easier to justify to "
     "herself [I]. If true she is your best retention segment; if false the whole ICP collapses into Linda–Energy.",
   "9. Male counterpart": "Robert's cognitive-sharpness motivation is the closest analogue, but his framing is "
     "performance and competence rather than dread [R].",
   "10. Discount and trust mechanics": "Price is least important to her of the four [I]. Third-party testing, dosage "
     "transparency and mechanism are what convert her — and the corpus shows exactly these being challenged in public: "
     "'This is not Third party tested. Also not GMP.' and complaints about proprietary blends hiding doses [M].",
   "11. Best-friend card": "Same woman as Linda, different 3 AM thought. She is not tired so much as frightened. "
     "She forgot her grandson's name at his birthday and sat in the car afterwards. She has not told anyone. "
     "She wants a smaller, fixable explanation than the one she is afraid of. [R][I]",
   "12. Emotion / JTBD / objection / trigger": "EMOTION — fear, sharp and specific, with shame attached to admitting it. "
     "JOB — 'give me a reason this is fixable and not the thing I watched my mother go through.' OBJECTION — "
     "'prove the mechanism; don't sell me hope.' TRIGGER — the witnessed blank; the pause at the dinner table while "
     "everyone waits. [R][I]",
  }),

 dict(
  key="mirror", name="Margaret — Mirror", tagline="The best customer you have, and you barely market to her",
  size="323 customers, 4.7% of buyers [M]", evidence="Strongest of the four — purchase is an observable event [M]",
  colour="good",
  headline_stats=[("Customers", "323 [M]"), ("AOV/LTV", "$98.44 LTV [M]"), ("vs NMN-only", "+38% LTV [M]"),
                  ("Repeat rate", "26.9% [M]"), ("Units/order", "4.70 [M]")],
  parts={
   "1. Who she is": "Same demographic core as Linda, identified by behaviour rather than profile: she has bought "
     "Astaxanthin alongside NMN [M]. 323 customers between January and August [M]. She is the most valuable buyer "
     "in the business on every measure available — LTV $98.44 against $71.10, repeat rate 26.9% against 13.5%, "
     "4.70 units per order against 3.48 [M]. She buys energy first and the mirror second [R].",
   "2. Her day, hour by hour": "Same windows as Linda [M]. Her distinct moment is the mirror — catching her reflection "
     "in a store window or seeing a photo she was tagged in [R]. That moment is not time-of-day bound, which makes her "
     "a retargeting rather than a dayparting opportunity [I].",
   "3. How she finds you and what she buys": "She does not usually arrive on an ASTA ad — she arrives on NMN and adds "
     "ASTA later [R]. ASTA is $12,475 gross across 206 orders at $42 AOV in the report period [R], 462 units since June [M]. "
     "The attach is the mechanic, not the acquisition [M][I].",
   "4. Her geography": "Indistinguishable from Linda [M]. Worth testing against the premium AZ/NV markets, where higher "
     "AOVs suggest more headroom for a two-product basket [I].",
   "5. Her deep insecurities": "(1) I look older than I feel inside — the mirror is lying, and the person she sees does "
     "not match the person she feels like [R]; (2) I'm falling behind my friends [R]; (3) the same energy fears as Linda, "
     "underneath [R]. The report is explicit that this is an identity crisis rather than vanity, and copy that treats it "
     "as vanity will miss [R].",
   "6. A day in her life": "Identical to Linda's until the mirror moment. Notably, the one unprompted positive comment "
     "about skin in the entire corpus is hers in spirit: 'I'm going to continue on an empty stomach. My skin looks "
     "better too.' — skin improvement is being discovered as a side effect of NMN, not sold [M].",
   "7. What she wants next": "The ASTA+NMN 'total transformation' bundle is the clearest Tier 1 opportunity in the "
     "report and she is the proof it works [R][M]. Collagen 'inside and outside' pairing next [R]. "
     "Calcium Balm currently carries a 40.9% discount on 68 units with null COGS — she is the only plausible buyer "
     "for it, and it should be a gift-with-purchase at her bundle tier rather than an ad spend line [M].",
   "8. Her repeat behaviour": "26.9% repeat, twice the NMN-only rate, on 1.33 orders and $98.44 LTV [M]. "
     "The strategic implication is large: moving even 10% of NMN-only buyers into the ASTA attach would add roughly "
     "$27 of LTV each. Across the 6,491 NMN-only customers that is a meaningful number and requires no new traffic [I].",
   "9. Male counterpart": "Effectively none. ASTA's skin positioning has no male analogue in the current range [I].",
   "10. Discount and trust mechanics": "The corpus contains an ASTA-specific trust question — 'Is it true that a lot of "
     "people are selling fake astaxthantin?' [M] — which is the same category-quality anxiety that makes the "
     "'not all X is created equal' angle the best-performing structure in the account [M].",
   "11. Best-friend card": "Margaret bought NMN for her energy in March. By May she noticed her skin looked better and "
     "went looking for why. She added ASTA on her second order and now buys both. She spends 38% more over her lifetime "
     "than a Linda who never made that jump, and she orders twice as often. Nobody has ever sent her an ad about it. [M][I]",
   "12. Emotion / JTBD / objection / trigger": "EMOTION — grief moving to hope; the mirror is the wound, the improvement "
     "is the reward. JOB — 'make the outside match the person I still feel like inside.' OBJECTION — 'is this the real "
     "form of the ingredient, or another cheap one?' TRIGGER — the reflection in a shop window; a photo someone else "
     "tagged her in; a compliment she did not expect. [R][M]",
  }),

 dict(
  key="robert", name="Robert — The male buyer", tagline="Spends more, stays longer, and has never been advertised to",
  size="765 customers, 11.2% of named buyers [M]", evidence="Good — [M] name-inferred purchase data · [R] the ROAS claim",
  colour="neg",
  headline_stats=[("Customers", "765 [M]"), ("AOV", "$66.48 [M]"), ("LTV", "$82.55 [M]"),
                  ("vs female", "+10% AOV, +16% LTV [M]"), ("Units/order", "3.33 [M]")],
  parts={
   "1. Who he is": "60–72, retired professional, veteran or tradesman [R]. 765 identifiable male customers on a "
     "conservative first-name match — a floor, not a ceiling, since the match misses many names [M]. "
     "AOV $66.48 against $60.37 and LTV $82.55 against $71.11 [M]: he measurably spends more and stays longer. "
     "Gmail and iCloud rather than AOL and Yahoo [R]. Same cities as Linda [R]. "
     "The research puts him at 1.81 ROAS, the most efficient demographic in the account — that figure is not "
     "verifiable in the warehouse and should be confirmed in Ads Manager before budget moves against it [R].",
   "2. His day, hour by hour": "No separable pattern in the data [—]. Assume Linda's windows until a dedicated ad set "
     "produces its own [I].",
   "3. How he finds you and what he buys": "Same channels [R]. Buys $100+ bundles more frequently than she does [R], "
     "consistent with the measured 3.33 units per order against 2.94 [M]. He is more likely to research the spec first, "
     "which again points at the untapped search channel [I].",
   "4. His geography": "Phoenix, Las Vegas, Houston, San Diego — the same Sun Belt corridor [R].",
   "5. His deep insecurities": "(1) I'm becoming my father — he watched him slow down, lose his edge and become "
     "dependent, and refuses to let it happen [R]; (2) I've lost a step and I'm the only one who has noticed; "
     "(3) I won't be a burden; (4) recovery takes days now [R][I]. His register is refusal, not repair.",
   "6. A day in his life": "Not documented in the research [—]. What is known is what motivates him: recovery, "
     "cognitive sharpness, physical performance, staying active [R]. The observable version is the task he can still "
     "do alone — the ladder, the boat, the garage [I].",
   "7. What he wants next": "Joint and mobility support fits him at least as well as it fits Linda [R][I]. "
     "The highest-value near-term move is not a new product but the household expansion: his wife is already a customer, "
     "the card is on file, and the top VIP in the business (7 orders, $424) is a male-leaning name [R].",
   "8. His repeat behaviour": "LTV $82.55 on 950 orders across 765 customers [M]. VIPs cluster at $260–424 across "
     "3–7 orders and consistently buy the mid-to-large bundle — they do not downgrade [R].",
   "9. What he looks like": "This ICP is Part 9 of the original report, promoted here to a full profile because the "
     "measured data supports it and no creative has ever addressed him [M].",
   "10. Discount and trust mechanics": "Spec converts him where story converts her [I]. Milligrams, purity, "
     "third-party testing, in the first ten seconds. The corpus shows a male commenter doing exactly this analysis in "
     "public and rejecting the product on it: 'Yes, 1,000 mg is the best dose. However, this is not Third party tested. "
     "Also not GMP.' [M] — that is the whole Robert objection in one comment.",
   "11. Best-friend card": "Robert, 66, Henderson. Retired tradesman. He watched his father stop driving at 71 and "
     "swore he would not go that way. He is a step slower and nobody else has noticed yet. He will read a supplement "
     "facts panel before he reads a headline, and he will buy the big bundle if the numbers hold up. "
     "He spends 16% more than Linda over his lifetime. There is not one ad in your account written to him. [M][R][I]",
   "12. Emotion / JTBD / objection / trigger": "EMOTION — fear reframed as pride and defiance; he will not describe it "
     "as fear. JOB — 'keep me capable and independent, and don't make me ask for help.' OBJECTION — 'show me the "
     "dosage, the purity and the third-party test, or you're selling hope.' TRIGGER — a task that used to be easy "
     "taking noticeably longer; watching a peer decline. [R][M][I]",
  }),
]

# ---------------------------------------------------------------------------
# QUOTE BANK - verbatim only, from social_media_comments_table
# flags: time_place, sensation, former_self, embarrassing, plain, under12
# ---------------------------------------------------------------------------
def q(cid, dt, text, emotion, jtbd, kind, obj, trigger, icp, flags):
    return dict(cid=cid, dt=dt, text=text, emotion=emotion, jtbd=jtbd, kind=kind,
                obj=obj, trigger=trigger, icp=icp, flags=flags)

QUOTES = [
 # ---- SUBSCRIPTION TRAP ----
 q("122134106379199246_1580883133432860","2026-08-13","I wanna order but I don't want a subscription and it says you can opt out below but I can't find the opt out selection or I would've purchased","Anger","Buy once without being locked in","Objection","Forced subscription / no opt-out","At checkout, trying to find the opt-out","All",["plain"]),
 q("122131240809199246_1823863192322985","2026-07-16","You need to make it available For a single purchase.... The subscription is stopping me .","Anger","Buy once without being locked in","Objection","Forced subscription","Reading the offer, deciding not to buy","All",["plain","under12"]),
 q("122132348223199246_1547631093571800","2026-07-10","I want to order, but I'm afraid I might get stuck on a subscription.","Fear","Buy without risk of entrapment","Objection","Fear of subscription trap","Pre-purchase hesitation","All",["plain","under12"]),
 q("122128728963199246_1550652850181638","2026-06-23","How can I buy it without a subscription?  I only want 1 bottle to start","Fear","Try it small before committing","Objection","Wants a single bottle trial","First-time consideration","Linda — Energy",["plain","under12"]),
 q("122131612425199246_1465619425327610","2026-07-25","I bought this one time and they kept sending more every month and kept billing me. I had to change my account to get them to stop","Anger","Stop unwanted charges","Objection","Billed repeatedly, could not cancel","Discovering repeat charges on her statement","All",["plain","time_place"]),
 q("122128325661199246_3592106930938476","2026-07-07","They have hidden an automatic renewal, so if you order make sure to unchecked that box or in 3 months they will take a lot of money out of you account","Anger","Warn other buyers","Objection","Hidden auto-renewal","Warning others in the comments","All",["plain"]),
 q("122132877891199246_2542169586254349","2026-08-09","Be careful when ordering!! This is on a monthly subscription!!","Anger","Warn other buyers","Objection","Undisclosed subscription","Public warning under a live ad","All",["plain","under12"]),
 q("122129136735199246_2073060109947334","2026-06-27","The discounts only apply if you commit to a subscription","Anger","Understand the real price","Objection","Discount conditional on subscription","Comparing the offer to the checkout","All",["plain","under12"]),
 q("122131612425199246_1003137959164114","2026-07-15","I only by 1get 1 which would be buy 1get 1 I'm so upset I can't get it","Anger","Buy the bundle she wants","Objection","Cannot get the bundle tier she wants","Blocked at bundle selection","Linda — Energy",["plain","embarrassing"]),
 q("122128721823199246_2065907488135194","2026-07-09","I didn't see where you can order 1 time only","Fear","Buy once","Objection","One-time option not findable","Scanning the order page","All",["plain","under12"]),

 # ---- NEVER SHIPPED ----
 q("122118177405199246_1211245200994774","2026-05-28","Scam alert!  Took my payment and never got my product. I also cannot get communication other then the automated 'page responded privately' comment.","Anger","Get the product she paid for","Objection","Non-delivery + no support","Weeks after ordering, no product","All",["plain","time_place"]),
 q("122118098865199246_1481577093437011","2026-05-22","I ordered a product on May 10th and have still not received it, I called Prime Ingredients or what I thought was and it was a completely different website, they said they have been getting calls for about a year.  What's up are you legit??","Fear","Confirm the company is real","Objection","Non-delivery, unreachable, wrong phone number","Twelve days after ordering, phoning around","All",["plain","time_place"]),
 q("122118053391199246_1352495773462756","2026-05-29","I'll comment SCAM and continue to get this rogue company off Facebook. Just reported and intend to escalate further","Anger","Punish the company / protect others","Objection","Escalating to platform reports","After a failed order and no response","All",["plain"]),
 q("122118083625199246_2109889542901677","2026-05-29","Scam.  Stay away from this company. Also please report so they can get booted from Facebook, tik tok and instagram. This products is great. Ended up getting mine off Amazon after paying this company and never receiving my order","Anger","Get the product elsewhere","Objection","Paid, never received, bought from Amazon instead","Giving up and re-buying elsewhere","All",["plain"]),
 q("122133477945199246_3433888670121176","2026-07-17","Beware! Took my money and never sent product!","Anger","Warn other buyers","Objection","Non-delivery","Public warning","All",["plain","under12"]),
 q("122131612425199246_1874514823507800","2026-07-21","Where's my order???????? It's been two weeks no tracking number nothing !!! Scam!!!!","Anger","Track the order","Objection","No tracking, no communication","Two weeks post-purchase","All",["plain","time_place","under12"]),
 q("122134276587199246_2242483559877632","2026-07-24","I ordered on July 3rd they still have not arrived.","Anger","Receive the order","Objection","Delivery delay","Three weeks post-purchase","All",["plain","time_place","under12"]),
 q("122122408935199246_1472096188033916","2026-04-21","Ordered and paid in March, still waiting for my order to be delivered","Anger","Receive the order","Objection","Month-plus delay","Waiting since the previous month","All",["plain","time_place","under12"]),
 q("122129136903199246_1730873807949273","2026-07-14","I ordered July 6th and I dont have an order number, I'm giving it til the 16th before i contact my credit card. Can't find any emails","Fear","Get confirmation the order is real","Objection","No order number or confirmation email","Eight days in, preparing to dispute","All",["plain","time_place"]),
 q("122117698671199246_979635434734082","2026-04-07","I ordered and once again find 8 days out after shipping still not here. Re checked website and again duped! Site showed made in USA well from tracking order its coming from China! Never ever again","Anger","Buy American-made","Objection","Origin claim vs tracking mismatch","Checking the tracking and seeing China","All",["plain","time_place"]),
 q("122133480861199246_1357022546629817","2026-07-27","That's really cool, BUT it never arrives.","Anger","Receive the order","Objection","Non-delivery","Reacting to a product claim","All",["plain","under12"]),

 # ---- MICRO INGREDIENTS / BRAND CONFUSION ----
 q("122134094355199246_1060713203578352","2026-07-23","You show MicroIngredients bottle in your ad, but sell a different brand… fake and buyer beware… buy only on MicroIngredients site.","Anger","Buy the real product","Objection","Ad shows a competitor's bottle","Comparing the ad to the shop page","All",["plain"]),
 q("122128721823199246_1037081915492356","2026-07-09","that video and the product in the video is from Micro Ingredients (do a screen shot and zoom in). Micro ingredients has their own Amazon shop and their own website. This company is trying to use the images of Micro Ingredients","Anger","Warn other buyers","Objection","Alleged use of competitor footage","Zooming in on the ad video","All",["plain"]),
 q("122134339089199246_2032097447482270","2026-08-07","Why is the bottle different from the one the lady on the commercial is holding. Hers has the letter M at the top of the bottle and the one that would be purchased says Prime up top?","Fear","Confirm what she is actually buying","Objection","Bottle in ad ≠ bottle sold","Mid-purchase, noticing the mismatch","All",["plain","sensation"]),
 q("122128722453199246_1784972486243425","2026-06-15","The labels you have are BLUE in the video! The ones for sale on the shop now button are PURPLE! That a RED flag for me!","Fear","Avoid being deceived","Objection","Label colour mismatch","Clicking through from ad to shop","All",["plain"]),
 q("122131612425199246_1367029588705650","2026-07-18","Why do the bottles initially shown have a brand of Micro Ingredients and the ones on the purchase page read Prime Ingredients? Kind of fishy!","Fear","Verify the brand","Objection","Brand mismatch ad vs page","At the purchase page","All",["plain"]),
 q("122135253765199246_1591914178957609","2026-08-04","Do not order from this company.  You'll never receive your order.  They claim \"overwhelming demand\".   Not true.  It's a Chinese knock off of the brand micro Ingredients","Anger","Warn other buyers","Objection","Knock-off allegation + non-delivery","After a failed order","All",["plain"]),
 q("122128722429199246_1037367565478165","2026-07-17","The person talking says that this product is from micro ingredients and the website that is shown and the bottle say prime ingredients so somebody is lying about something about this product","Anger","Establish who is telling the truth","Objection","Spokesperson claim contradicts the page","Watching the ad through to the page","All",["plain"]),
 q("122128342989199246_1690445611998135","2026-06-06","Why are you using microingredients product and packaging if your brand is legit?","Fear","Verify legitimacy","Objection","Packaging provenance","Assessing whether to trust the brand","All",["plain","under12"]),
 q("122134339305199246_2811247982579340","2026-07-29","This looks exactly like the NMN from Microingredients, is it the same company?","Fear","Understand what she is buying","Objection","Brand confusion","First exposure to the ad","All",["plain","under12"]),
 q("122131612425199246_1269948981792513","2026-07-30","Is prime ingredients and Micro ingredients the same company? The first pic shows micro and the it goes to the prime ingredients page to buy ive been using ihe micro and need to know","Fear","Avoid buying a fake","Objection","Existing competitor customer, confused","Clicking through as an existing Micro buyer","All",["plain"]),

 # ---- CAPSULE COUNT / VALUE ----
 q("122129136903199246_1015238754592779","2026-07-13","It says 120 in the bottle but mine only had 30 in each one, why?","Anger","Get what was advertised","Objection","Capsule count mismatch","Opening the delivered bottle","All",["plain","time_place","under12"]),
 q("122131846503199246_1555434015982068","2026-07-09","30 capsules per bottle, that's two bottles per month which is $80/mo-- what a rip off","Anger","Understand the true monthly cost","Objection","Cost per month once count is known","Doing the maths after delivery","All",["plain"]),
 q("122134605039199246_2102162640720796","2026-07-28","I got 6 bottles, barely enough pills in each bottle to cover the bottom, I literally dumped all six into one & there's still room in the bottle","Anger","Get fair value","Objection","Perceived under-fill / packaging waste","Unboxing six bottles","All",["plain","sensation","time_place"]),
 q("122129137335199246_1554107039603342","2026-07-06","30 capsules only,...if we take 2/ day,to get 1000 mg. we'll have it just for 15 days!","Anger","Make the supply last","Objection","Supply duration vs price","Calculating the dose schedule","All",["plain"]),
 q("122134339089199246_1371773341757513","2026-08-05","Rip off bottle less than half full don't buy","Anger","Warn other buyers","Objection","Under-filled bottle","Opening the package","All",["plain","under12"]),
 q("122130041835199246_1525526915930916","2026-06-21","There's only 30 capsules in the bottle go to micro ingredients they sell 120 for 39","Anger","Get better value elsewhere","Objection","Direct competitor price comparison","Post-delivery comparison","All",["plain","under12"]),

 # ---- PRICE / BAIT AND SWITCH ----
 q("122134610097199246_1026596133581403","2026-08-09","Yea it says $40 and then you get to checkout and it's suddenly$80. Scam","Anger","Pay the advertised price","Objection","Checkout price ≠ ad price","At checkout","All",["plain","time_place","under12"]),
 q("122134843623199246_895032503219293","2026-07-31","Trying to correct my cart... they want to charge me $199.00 for 12 bottles!! Scared to order anything  from them now.  Amazon here is come.","Fear","Buy the quantity she wants at a fair price","Objection","Cart total shock","Editing the cart","All",["plain","time_place"]),
 q("122131612425199246_1345477503887309","2026-08-02","Rip off...bought some...twice the competitors price...","Anger","Not overpay","Objection","Competitor price comparison","Post-purchase comparison","All",["plain","under12"]),
 q("122109427737199246_1635809694313924","2026-05-07","How do you get a discount code? Don't want to order then see a discount code…","Fear","Avoid buyer's remorse","Objection","Fear of missing a better price","Immediately pre-purchase","Linda — Energy",["plain"]),
 q("122131612425199246_1590096676060229","2026-07-24","I won't miss out. And I will not be paying for shipping. Lots of suppliers that don't charge for shipping, Goodbye.","Anger","Avoid shipping fees","Objection","Shipping cost","At checkout","All",["plain"]),

 # ---- EFFICACY DOUBT ----
 q("122128325637199246_1461464005748389","2026-06-25","I've been taking this combo for a month, and I don't notice a difference in my energy levels at all. 😔","Grief","Feel the energy difference","Objection","No perceived result at 30 days","One month in, still tired","Linda — Energy",["plain","time_place","sensation"]),
 q("122128722453199246_4420216254922904","2026-06-17","I'm on my second month of daily mnm,    no visible results. All hype,  now im being told i need to take nicootinomide with it.","Anger","Get the promised result","Objection","No result at 60 days","Two months in","Linda — Energy",["plain","time_place"]),
 q("122134114089199246_2553008935173996","2026-08-04","Been taking all of these for a year no change","Grief","Feel different","Objection","No result at 12 months","A year in","Linda — Energy",["plain","time_place","under12"]),
 q("122109427737199246_846748311243255","2026-05-14","Im a week in using this stuff and nothing yet.","Fear","Know if it is working","Objection","Impatience at day 7 — the churn window","One week in","Linda — Energy",["plain","time_place","under12"]),
 q("122126785149199246_2443014686213126","2026-05-31","I have taken them for over a month and nothing has changed","Grief","Feel different","Objection","No result at 30 days","One month in","Linda — Energy",["plain","time_place","under12"]),
 q("122128722255199246_1175966851393591","2026-07-10","I was getting an NAD shots then I switched to this and I don't notice it working.","Grief","Match the effect of NAD injections","Objection","Weaker than the IV alternative","After switching from injections","Linda — Clarity",["plain","former_self"]),

 # ---- TRUST / SPEC / QUALITY ----
 q("122128721823199246_1027671486908303","2026-07-11","Yes, 1,000 mg is the best dose. However, This is not Third party tested. Also not GMP. There's not a \"complex of ingredients\" in this product, which would certainly help with absorption.","Fear","Verify quality before buying","Objection","No third-party testing or GMP","Reading the supplement facts panel","Robert — The male buyer",["plain"]),
 q("122128722429199246_1674200973697060","2026-07-15","LOL , Proprietary Blend , we don't want to disclose how much of each ingredient we put in our products because it's not enough to make a difference, we just want your money for our under-dosed  products","Anger","Know the actual doses","Objection","Proprietary blend hides dosing","Reading the label","Robert — The male buyer",["plain"]),
 q("122127720465199246_2055748398679581","2026-06-13","Just curious, I googled the top 5 NMN products, and your NMN was never mentioned.  And this was after clicking on about 5 links reporting the top 5.  So what makes your NMN better?","Fear","Validate the brand independently","Objection","Absent from third-party rankings","Googling before buying","Robert — The male buyer",["plain","time_place"]),
 q("122130710271199246_1575364164163416","2026-07-28","There is no phone number to call. Don't trust companies that make you email","Fear","Reach a human","Objection","No phone contact","Looking for support before buying","Linda — Energy",["plain","under12"]),
 q("122131241481199246_2282183105890991","2026-07-23","This is sold on Amazon, how can I trust it?","Fear","Buy from a legitimate source","Objection","Marketplace availability undermines trust","Cross-checking the brand","All",["plain","under12"]),
 q("122128729047199246_908379488329243","2026-06-14","This is NOT NMN. \nI've tested it. It's garbage.","Anger","Get genuine NMN","Objection","Authenticity claim","After independent testing","Robert — The male buyer",["plain","under12"]),
 q("122131848315199246_3478139035685974","2026-07-04","That's because if you have early stage cancer it was found to encourage its growth. Don't buy this unless they can promise it's been stabilized, how, and that they can guarantee it's what they say it is - 3rd party testing, guaranteed stabilized.","Fear","Avoid harm","Objection","Safety concern — needs medical review","Researching risks before buying","Linda — Clarity",["plain"]),

 # ---- SPOKESPERSON BACKLASH ----
 q("122131249125199246_803966126072313","2026-07-27","Liar,...it's all plastic surgery...please pls don't believe anything this woman says....","Anger","Not be deceived by an unrealistic model","Objection","Spokesperson credibility","Seeing the celebrity in the ad","Margaret — Mirror",["plain","under12"]),
 q("122131249125199246_1819021955742610","2026-07-19","Because no one wants to be like the Kardashians. Be a Beth!","Anger","See someone like herself","Objection","Aspirational figure is wrong for the audience","Seeing the celebrity in the ad","Linda — Energy",["plain","under12"]),
 q("122131249125199246_1002131459265839","2026-07-17","Seriously. A woman that had ribs taken out so her waist would shrink. More plastic than the Michelin Tyre guy. Enough surgery for a small nation . This is your spokesperson","Anger","See authentic proof","Objection","Spokesperson undermines authenticity","Seeing the celebrity in the ad","Margaret — Mirror",["plain"]),
 q("122133831009199246_1711341796786849","2026-07-24","I'm 70 I look 30, and I don't even use that stuff. How about that","Pride","Assert she does not need it","Objection","Rejects the premise of decline","Reacting to an ageing-related claim","Linda — Energy",["plain","former_self","under12"]),

 # ---- HOW TO TAKE IT ----
 q("122132877891199246_2027522881222347","2026-08-07","Some say take on an empty stomach, some say take with food? Which is it? I was taking with food and heard another doctor say take on an empty stomach! Geesh.. I started taking on an empty stomach with no problems.","Relief","Take it correctly","Benefit","Resolved her own dosing confusion","Weeks into taking it, still unsure","Linda — Energy",["plain","time_place"]),
 q("122132877891199246_2223349125185435","2026-08-08","Better absorption on empty. Give it 30-60 minutes then eat something.","Relief","Help another customer take it right","Benefit","Peer-to-peer dosing advice","Answering another commenter","Linda — Energy",["plain","under12"]),
 q("122133293679199246_1316581873969556","2026-07-14","You have to take three capsules at once.  Why","Fear","Understand the protocol","Objection","Dose size friction","Reading the directions","Linda — Energy",["plain","under12"]),
 q("122132877891199246_1049013311053658","2026-08-11","Take with an ounce of tart cherry juice and Pom and a bite of cheese and it also helped my sleep.","Relief","Improve sleep alongside energy","Benefit","Self-devised protocol that worked","Sharing her own routine","Linda — Energy",["plain","sensation"]),

 # ---- THE POSITIVES (the entire benefit-side corpus) ----
 q("122132877891199246_939991329155377","2026-08-08","I've been taking it on an empty stomach for about 4 months now. It really keeps me energized throughout my day. I forgot to take it in the morning a few times, so I took it in the evening. I wouldn't recommend that, it led to a few sleepless nights.","Relief","Have energy through the whole day","Benefit","Sustained energy at 4 months","Four months of consistent use","Linda — Energy",["plain","time_place","sensation"]),
 q("122132877891199246_1724809792136749","2026-08-08","Nick Vujnovich thank you. I'm going to continue on an empty stomach. My skin looks better too.","Relief","Look better as well as feel better","Benefit","Unprompted skin improvement","Noticing a side benefit she did not buy for","Margaret — Mirror",["plain","sensation","under12"]),
 q("122131846503199246_1787375932433540","2026-07-11","Sandy Martinelli I got 2 bottles, 120 capsules. Buy one get one free. Flash sale, TikTok.","Relief","Confirm the offer is real","Benefit","Received the advertised quantity","Answering another buyer's doubt","Linda — Energy",["plain","under12"]),
 q("122134114059199246_2271599893584415","2026-07-24","Susan, notice the extra 10 ingredients in this NMN.","Pride","Justify the choice to a peer","Benefit","Formulation breadth as a differentiator","Defending the product to another commenter","Robert — The male buyer",["plain","under12"]),

 # ---- MEDICAL ELIGIBILITY (unanswered = lost buyers) ----
 q("122132877891199246_1025430576921378","2026-08-10","Can I take this of o have gastric by pass 8 years ago","Fear","Know if it is safe for her","Objection","Eligibility unanswered","Ready to buy, blocked by a safety question","Linda — Energy",["plain","time_place","under12"]),
 q("122131240809199246_4441542532758881","2026-07-20","Can you take this if you are a dialysis patient ?","Fear","Know if it is safe for her","Objection","Eligibility unanswered","Ready to buy, blocked by a safety question","Linda — Energy",["plain","under12"]),
 q("122129137089199246_4022976407999906","2026-07-08","Is NMNs good for women who have osteoporosis?????","Fear","Know if it helps her condition","Objection","Eligibility unanswered","Considering purchase","Linda — Energy",["plain","under12"]),
 q("122133476643199246_909778788151515","2026-07-19","Does this help with neuropathy? I'm seeing mixed reports.","Fear","Know if it treats her condition","Objection","Conflicting information","Researching before buying","Linda — Clarity",["plain","under12"]),
 q("122131240809199246_797356996733395","2026-07-18","I'd like to purchase but not subscription as well. Is it too late if you are already in your 50's?","Fear","Know it is not too late for her","Objection","Age eligibility + subscription","Ready to buy, two blockers at once","Linda — Clarity",["plain","under12"]),
 q("122122402209199246_1884326708894425","2026-04-17","How about if your 70 and just starting glp1? I'm losing weight but want to take it slow bc don't want yo hollow out my face .. I'm working out to keep muscle tone. Am I too old for NAD and NMN","Fear","Fit it into an existing regimen","Objection","Interaction and age eligibility","On GLP-1, worried about facial volume","Margaret — Mirror",["plain","sensation","former_self"]),
]

EMOTIONS = ["Fear", "Shame", "Hope", "Relief", "Pride", "Anger", "Grief"]
FLAG_LABELS = [
    ("time_place", "Specific time or place"),
    ("sensation", "Physical sensation"),
    ("former_self", "Comparison to former self"),
    ("embarrassing", "Embarrassing admission"),
    ("plain", "Plain unbranded language"),
    ("under12", "Under 12 words"),
]

HARVEST = [
 dict(rank=1, source="Okendo / Yotpo review feed", est="5,128 reviews already exist",
      why="The landing page cites 5,128 reviews but `reviews_table` returns zero rows — the platform is not piped into Triple Whale. This is the single largest untapped store of positive customer language, and it is already written.",
      effort="Low — an integration toggle"),
 dict(rank=2, source="Post-purchase survey", est="~450 responses/month at current volume",
      why="`post_purchase_survey_table` is empty. One question — 'what made you finally order?' — harvests trigger moments, which is the axis the current corpus is thinnest on.",
      effort="Low — one app, one question"),
 dict(rank=3, source="Klaviyo reply inbox", est="Unknown, likely hundreds",
      why="The Day 12 'notice anything yet?' email in the messaging system is designed to generate exactly the hope/relief/pride language the corpus lacks. Klaviyo currently sends Triple Whale no engagement data at all.",
      effort="Medium — fix the integration, then run the flow"),
 dict(rank=4, source="ManyChat DM transcripts", est="13 tags, 6 flows already running",
      why="Customers self-describe their goal in the DM flow. Those free-text answers are first-person motivation statements and they are already being collected.",
      effort="Medium — export and tag"),
 dict(rank=5, source="Support tickets / email", est="Unknown",
      why="Given the volume of delivery complaints in the comment corpus, the support inbox is likely the richest source of objection language and the fastest read on whether fulfilment is genuinely broken.",
      effort="Low — export and read"),
 dict(rank=6, source="Meta ad comments (ongoing)", est="468 to date, ~80/month",
      why="The source of this bank. Keep harvesting monthly — it is free, unprompted, and it is where problems surface before they show up in the revenue.",
      effort="Very low — already flowing"),
]
