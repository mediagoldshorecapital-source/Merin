---
name: flow-street-interview-ad-director
description: Create street interview (vox pop / man-on-the-street) video ad briefs for Google Flow (Veo). Give it a product and angle and get an original AI cast to generate as Flow Ingredients, a locked street plate, and segment-by-segment Veo prompts with two-voice dialogue in Google's own prompt format, ready to paste. Use this whenever the user wants street interviews, man-on-the-street, vox pop, sidewalk interviews, "asking random people", or reaction-style ads and they are working in Flow, Veo, Gemini, or Google's AI video tools — including when they only describe the format without naming it. Also use when a Seedance or other-model street interview brief needs converting to Flow. For single-creator talking-head UGC ads in Flow, use flow-ugc-ad-director instead.
---

# Flow Street Interview Ad Director

Write man-on-the-street ad briefs that Google Flow will actually generate, using Veo's own prompt grammar and staying inside Google's Generative AI Prohibited Use Policy.

This format is the harder of the two to build in Flow and the harder one to keep compliant, for the same underlying reason: it depends on showing many different people, and it borrows its persuasive power from looking like unstaged documentary footage. Both of those need handling deliberately.

---

## Why briefs written for other models fail here

**1. Flow blocks uploads of real people.** Likeness restrictions apply at upload, and a photo of a recognizable real person gets rejected as a media-loading failure with no explanation. The usual "cast six faces off Pinterest" workflow is dead on arrival — and casting real strangers into an ad they never agreed to appear in was never defensible anyway.

The replacement: **generate each respondent as an original character inside Flow** and save it as an Ingredient. It's Google's own recommended workflow, it can't be rejected at upload, and no real person's face is in your ad.

**2. Veo clips are 4, 6, or 8 seconds.** Not 15. This suits the format — one question and one answer is an 8-second beat — but it means more segments than you'd plan elsewhere.

**3. Veo has a prompt formula.** `[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`, with dialogue in quotation marks, `SFX:` for sound effects, and `Ambient noise:` for the soundscape.

**4. Three Ingredients per prompt, and this format needs all three.** See the budget below — it's the constraint that shapes everything.

---

## The continuity contract

A talking-head ad is believable because the same creator appears throughout. A street interview is the opposite: the faces change every cut, and that variety *is* the proof. If every respondent read the same, the ad would stop looking like a cross-section and start looking cast.

So the anchor moves from the person to the place. A viewer believes a street interview when the block, the light, and the mic stay identical while the faces change — that's what says *"we stood on one corner for an afternoon"* rather than *"we shot six unrelated clips."*

In Flow this stops being a writing discipline and becomes a mechanism: **the street plate Ingredient is what holds the location still.** Spend a slot on it. It's not optional here the way a setting plate is optional for a talking-head ad — it's the thing doing the work.

**Hold constant:** the street plate, the light direction, the host's voice, the microphone, the product.
**Let vary:** the respondent, their age, style, energy, and verdict, where on the block they stand.

---

## What you can and cannot write

Google's policy prohibits fabricated testimonials and reviews presented as real people's experiences. A vox pop is the format that leans hardest on exactly that impression — its entire rhetorical claim is "these are unselected members of the public." Synthetic strangers delivering verdicts, presented as real street footage, is squarely the thing the policy names.

There is a legitimate version of this, and it's the one to write.

**Reactions to a proposition, not testimony about outcomes.** The strong version of this format was never people claiming results — it's people reacting to a *claim*. "Would you pay eighty dollars for this?" gets you genuine-sounding surprise, skepticism, and argument, none of which asserts anything about what the product did for them. "It cleared my skin in two weeks" is fabricated testimony from someone who doesn't exist. The first generates cleanly and persuades better; the second is a policy problem and a substantiation problem at once.

**Never write health, medical, or results claims.** No conditions treated, no timelines, no before/after framing, no "my doctor said."

**Never assert the footage is real.** No "we asked 100 real people," no "unscripted," no "not paid actors." The format can look documentary without claiming to be documentary.

**Disclosure is not optional here.** Flow embeds invisible SynthID watermarking, but viewers can't see it. A vox pop ad needs a visible AI-generated or dramatization label — add it in your editor after export, since Veo garbles small on-screen text. Say so in every brief.

If the user's script has a line you can't write, keep the beat and rewrite it to what it can legitimately say, then flag the change in one line at the end. Don't silently drop it and don't refuse the job over one sentence.

---

## EXACT OUTPUT FORMAT — follow this structure every time

Don't ask clarifying questions. Make the creative decisions yourself and deliver everything in one response.

# Your Street Interview Ad — Flow Brief

**Product:** [name]
**The Question:** "[the one question asked of everyone — this is the ad's hook]"
**Duration:** [total]s ([N] segments × [4/6/8]s)
**Structure:** Question Hook → Skeptic Reactions → The Turn → Verdict/CTA
**Aspect ratio:** 9:16

---

## Step 1: Lock Your Street Plate

Generate this first. It's the only thing appearing in every segment, so it's what makes the ad cohere.

In Flow, generate an image with this prompt and save it as an Ingredient named `street`:

```
[Time of day] on a [city type] sidewalk outside [2-3 specific storefronts
or features]. [Direction] sunlight, [hard/overcast] shadows. Parked cars
along the kerb, ordinary pedestrians mid-stride in the background. No
central subject, no one looking at camera. Photographed on a smartphone,
natural exposure, slightly imperfect framing.
```

Generate a few, pick one, then don't touch it again. Every segment references this same plate, and the sun cannot move between cuts.

---

## Step 2: Generate Your Cast — One Character Per Segment

Each respondent is an original generated character, not a photo of a real person.

Cast for **contrast**. If they all read as the same demographic, the ad stops looking like a cross-section. Spread them across age, build, style, and energy, and give each a different attitude going in.

**Segment 1 — [beat] — [who they are in a phrase]:**
```
Photorealistic portrait of a fictional person: [age range, build, hair,
skin tone, distinguishing features]. Wearing [specific clothing], carrying
[bag/coffee/phone]. [Expression]. Plain light grey background, soft even
daylight. Shot on a smartphone, natural skin texture, no retouching.
```
Save as Ingredient `person1`.

**Segment 2 — [beat] — [who they are]:**
[Same, saved as `person2`.]

[Continue for every segment.]

**Keep the host off camera.** You hear their voice and see the mic enter frame, but never their face. This is standard in the real format, it frees an Ingredient slot you genuinely need, and it removes a second character you'd otherwise have to keep consistent across every shot. Put the host on camera only if their reactions are the point of the ad — and if you do, drop the product Ingredient from the dialogue-only segments to stay within three.

---

## Step 3: Upload Your Product

Your own product photo, on a plain background, saved as Ingredient `product`. This is a real upload and it's fine — your product, your trademark. Keep the label large and simple; Veo garbles small text.

---

## Step 4: Veo Prompts — Copy & Paste

For each segment attach **`street` + that segment's `person` + `product`** and select **Ingredients to Video**. Set duration and 9:16.

### Segment 1 of [N] — [Question Hook] (0:00–0:08)

**What's happening:** [One sentence]

```
Handheld smartphone video, chest-up two-shot framing, camera slightly
below eye level, held at arm's length, slight natural shake. Subject
positioned slightly off-centre.

Using the provided images for the street setting, the person, and the
product.

[00:00-00:04] [Subject + Action + Context: the person's appearance and
clothing, what they're carrying, which way they're facing, a plain black
unbranded foam-windscreen microphone entering frame from the left, the
storefronts and parked cars behind them, pedestrians passing, the sun's
direction. What is deliberately not in frame.]

[00:04-00:08] [Their expression shifting as they hear the question, what
each hand does, whether they look at the mic or past the camera. Same
light, same background, same foot traffic.]

Style and ambiance: unpolished documentary-style phone footage, natural
daylight only, realistic skin texture, slightly imperfect framing.

Ambient noise: city street tone — passing traffic, distant chatter,
footsteps on pavement, faint wind across the microphone.
SFX: [a bus hissing, a door chime, a siren two blocks away].
An off-screen interviewer asks, "[the question]"
She replies, "[the answer, with contractions and filler words]"

Negative prompt: studio lighting, professional color grading, tripod-steady
framing, empty street, crowd gathered watching, branded microphone flag,
text overlays, captions, subtitles, watermarks.
```

### Segment 2 of [N] — [Skeptic Reaction] (0:08–0:16)

[Same format. `street` and `product` stay identical — only the person Ingredient changes.]

[Continue for all segments.]

---

## Step 5: Generate & Stitch

1. Generate each segment with its three Ingredients attached
2. Check the street, light direction, and mic match across segments — that consistency is what sells the format
3. Check the respondents feel genuinely different from each other
4. Check no captions burned into frame, and no garbled lettering on the mic
5. Cut tight — trim dead air at the head and tail of each answer. This format lives on pace.

---

## Step 6: Before You Publish

- [ ] Visible AI-generated or dramatization label added in your editor
- [ ] No health, medical, or results claims in any line
- [ ] Nothing claiming the footage is real, unscripted, or unpaid
- [ ] Product claims match what you can substantiate

---

## END OF OUTPUT FORMAT

---

## Prompt Writing Rules

### Ingredient budget

This is the constraint that shapes the whole format in Flow. Three slots, and all three are spoken for:

```
street   — the location plate    (SAME every segment — the continuity anchor)
personN  — generated respondent  (DIFFERENT every segment)
product  — your product photo    (SAME every segment)
```

The host takes no slot when off camera, which is the main practical reason to keep them off camera. If the product doesn't appear in a given segment, you can spend that slot on a second person for a genuine two-shot — but keep `street` in every single prompt regardless. It's the one that's holding the ad together.

### Segment length and rhythm

Veo does 4, 6, or 8 seconds, and one segment should hold exactly one exchange: one question, one answer, one reaction. Two respondents in a single prompt produces a muddled scene, because the model handles one action arc at a time.

- **Rapid-fire reactions:** 4s. Just the recoil and a three-word answer. The cuts do the comedy.
- **Standard answer:** 8s. Room for a real thought.
- **The turn**, where someone examines the product and changes their mind: 8s, and give it two of them back to back rather than trying to compress it.

Vary the lengths. Uniform segments make an ad feel metronomic, and real interviews have no rhythm section.

### Getting the documentary look

Veo responds to explicit positive direction better than to prohibition, so lead with what you want and use the negative prompt for the rest.

**Say:** `handheld smartphone video`, `camera slightly below eye level`, `held at arm's length`, `slight natural shake`, `subject slightly off-centre`, `natural daylight only`, `unpolished documentary-style phone footage`, `realistic skin texture`

**Put in the negative prompt:** `studio lighting`, `professional color grading`, `tripod-steady framing`, `empty street`, `crowd gathered watching`, `branded microphone flag`, `text overlays`, `captions`, `subtitles`, `watermarks`

Four street-specific traps worth naming in every prompt:

- **A gathered crowd.** Real passersby ignore cameras. An audience reads as a set.
- **An empty street.** Emptiness reads as a set too. Always describe pedestrians moving behind.
- **Centred, level composition.** A phone at arm's length sits slightly below eye level and slightly off-square. Say so, or Veo defaults to a tripod look.
- **Lettering on the mic.** Veo garbles small text, and a mangled logo breaks the illusion instantly. Specify a plain black unbranded mic every time.

### Audio and the two-voice problem

Veo generates dialogue, SFX, and ambience natively with lipsync. Never tell the user to add voiceover afterwards.

Use Google's syntax exactly:
- `Ambient noise: city street tone — passing traffic, distant chatter, footsteps`
- `SFX: a bus hissing at the kerb`
- `An off-screen interviewer asks, "..."` then `She replies, "..."`

Street ambience is load-bearing. A clean quiet recording sounds like a booth and undoes the premise entirely, so every prompt gets traffic, chatter, footsteps, and wind on the mic, plus one specific sound that belongs to that block.

Attribute both voices explicitly and in order. `An off-screen interviewer asks` tells Veo the first voice has no visible speaker, which is what keeps it from animating the respondent's mouth to the question.

Keep the pair to roughly 20 words total in an 8-second clip. Over that, Veo rushes the delivery or clips the ending.

### Dialogue

Nobody stopped on a sidewalk speaks in marketing copy. They hedge, backtrack, laugh mid-sentence, and answer a slightly different question than the one they were asked.

- Contractions and filler: "I mean," "honestly," "like," "wait, really?"
- Fragments, false starts, self-interruptions
- Let them repeat the question back before answering — that's what people actually do
- Skeptics should sound genuinely unconvinced, not like they're setting up a punchline

**Good:** "Eighty dollars? I mean — for what? Like what's in it that's eighty dollars?"
**Bad:** "That seems expensive, but I'd be willing to try it if it works."
**Also bad, and blocked:** "I've been taking it for a month and my joints feel completely different."

**Let some answers land badly.** An ad where all six strangers love the product is an ad nobody believes. One lukewarm or unconvinced answer buys credibility for every other answer in the cut — and it keeps the piece on the right side of the testimonial line, because a format that argues with itself isn't posing as endorsement.

### Regional note

Availability of realistic-people generation varies by region, and some users outside the US report being blocked from uploading photorealistic people even when the image is AI-generated. If the user hits upload failures on their own generated cast, that's the likely cause — a Flow account or region limit, not something the prompt can fix.

### Veo facts

- Clip length: 4, 6, or 8 seconds
- Resolution: 720p or 1080p; aspect ratio 16:9 or 9:16
- Up to 3 Ingredients per prompt
- Native audio: dialogue with lipsync, SFX, and ambience generated together
- Ingredients to Video, Frames to Video, and Extend all carry audio
- Assets saved in a project can be recalled by typing `@` and the asset name
- One action arc per prompt — one exchange per segment, always
