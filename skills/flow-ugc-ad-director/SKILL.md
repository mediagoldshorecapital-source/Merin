---
name: flow-ugc-ad-director
description: Create UGC-style video ad briefs for Google Flow (Veo). Give it a product or script and get an original AI character to generate as a Flow Ingredient, plus segment-by-segment Veo prompts in Google's own prompt format with native dialogue and audio, ready to paste. Use this whenever the user wants UGC ads, creator-style ads, talking-head product ads, or phone-shot-looking video ads and they are working in Flow, Veo, Gemini, or Google's AI video tools — including when they only say "make me a UGC ad" without naming the tool. Also use when a Seedance or other-model ad prompt needs converting to Flow. For man-on-the-street or vox pop ads in Flow, use flow-street-interview-ad-director instead.
---

# Flow UGC Ad Director

Write UGC-style video ad briefs that Google Flow will actually generate, using Veo's own prompt grammar and staying inside Google's Generative AI Prohibited Use Policy.

The format goal is unchanged from any other UGC ad: it should look like a real person filmed themselves on a phone. What changes is that Flow refuses several things other video tools allow, and Veo reads prompts in a specific structure. Fight either and you burn generations.

---

## Why briefs written for other models fail here

Read this before writing anything, because these four differences drive every rule below.

**1. Flow blocks uploads of real people.** Likeness restrictions apply at upload, not just at generation, and a photo of a recognizable real person is rejected as a media-loading failure with no explanation. So the usual "find a face on Pinterest and upload it as your character reference" workflow cannot work here — and it was never on solid ground anyway, since it puts a real person's likeness in an ad they never agreed to appear in.

The replacement is better in every way: **generate an original character inside Flow**, save it as an Ingredient, and reuse it. It's Google's own recommended workflow, it can't be rejected at upload, and nobody owns the face but you.

**2. Veo clips are 4, 6, or 8 seconds.** Not 15. A 32-second ad is four 8-second segments, not two long ones. Plan the beats to that grid or the brief won't survive contact with the tool.

**3. Veo has a prompt formula.** `[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`, with dialogue in quotation marks, `SFX:` for sound effects, and `Ambient noise:` for the soundscape. Freeform prose gets read loosely; the formula gets read precisely.

**4. Flow takes up to three Ingredients per prompt.** Budget them deliberately.

---

## What you can and cannot write

Google's policy prohibits fabricated testimonials presented as real people's experiences, and prohibits misleading claims in sensitive areas like health. A UGC ad is *shaped* like a testimonial, so this is the line you work along constantly. Staying on the right side of it is a writing problem, not a workaround problem — and the ads read better for it.

**Write the character as a presenter, not a witness.** They can show the product, react to it, explain what it is, and have an opinion about it. What they cannot do is narrate a personal outcome as evidence: "this cleared my skin in two weeks" is fabricated testimony from a person who does not exist. "Okay so this is the one everyone's been talking about — let me actually look at what's in it" is a presenter, and it generates fine.

**Never write health, medical, or results claims.** No before/after framing, no timelines to results, no "doctors recommend," no implied treatment of a condition. This is both the most likely thing to trip a filter and the most likely thing to cause the user real trouble downstream.

**Never write it as real testimony.** Avoid "real customers, real results," "I'm not paid to say this," or anything asserting the speaker is a genuine unaffiliated user.

**Tell the user to disclose.** Every brief ends with a disclosure reminder. Flow embeds SynthID watermarking automatically, but that is invisible to viewers — the ad still needs an "AI-generated" label, both because ad platforms increasingly require it and because it is what keeps a synthetic presenter honest.

If the user's script contains a claim you can't write, keep the beat and rewrite the line to what it can legitimately say — then flag what you changed in one line at the end of the brief. Don't silently drop it, and don't refuse the whole job over one sentence.

---

## EXACT OUTPUT FORMAT — follow this structure every time

Don't ask clarifying questions. Make the creative decisions yourself and deliver everything in one response.

# Your UGC Ad — Flow Brief

**Product:** [name]
**Duration:** [total]s ([N] segments × 8s)
**Ad Structure:** Hook → Problem/Proof → Benefit/Demo → CTA
**Aspect ratio:** 9:16

---

## Step 1: Generate Your Creator as an Ingredient

This character appears in every segment. You're generating an original person, not uploading a photo of a real one — Flow rejects real-person uploads, and an original character can't be rejected or claimed by anyone.

In Flow, generate an image with this prompt, then save the result as an Ingredient named `creator`:

```
Photorealistic portrait of a fictional person: [age range, build, hair,
skin tone, distinguishing features — be specific enough to be repeatable].
Wearing [specific casual clothing]. Neutral relaxed expression, looking
at camera. Plain light grey background, soft even daylight, no props.
Shot on a smartphone front camera, natural skin texture, no makeup styling,
no retouching.
```

**Why the plain background:** Google's guidance for reference images is a plain or simple background and a consistent look across inputs. A busy reference photo bleeds its setting into every scene you generate.

**Generate 3–4 variations and pick one.** Then stop — that image is your creator for the whole ad. Re-generating the character mid-ad gives you a different person.

**Optional second Ingredient — the setting.** Same approach if you want a locked location:

```
[Room type] interior, [time of day] light from [direction], [2-3 specific
details]. No people. Photographed on a smartphone, natural exposure.
```

---

## Step 2: Upload Your Product as an Ingredient

Your own product photo, uploaded and named `product`. This one is a real upload and that's fine — it's your product and your trademark.

**Shoot or crop it on a plain background.** Same reason as above. And keep labels large and simple if you can: Veo garbles small text, and a mangled label is the fastest way to make an ad unusable.

---

## Step 3: Veo Prompts — Copy & Paste

Attach `creator` and `product` as Ingredients for every segment, and select **Ingredients to Video**. Set duration to 8s and aspect ratio to 9:16.

### Segment 1 of [N] — [Hook] (0:00–0:08)

**What's happening:** [One sentence]

```
Handheld smartphone video, [shot size] framing, camera held at arm's
length, slight natural shake, filmed by the subject themselves.

Using the provided images for the creator and the product.

[00:00-00:04] [Subject + Action + Context: who they are and what they're
wearing, what each hand is doing, their expression, the surface in front
of them and what is deliberately not on it, the light source and its
direction, 2-3 background details.]

[00:04-00:08] [What changes: the movement, the expression shift, how the
product enters or moves in frame. Same light, same background.]

Style and ambiance: unpolished home video, natural [window/lamp/daylight]
light only, realistic skin texture, phone camera depth of field, slightly
imperfect framing.

Ambient noise: [room tone that matches the setting].
SFX: [any specific sound — a lid clicking, fabric rustle, a cup set down].
She says, "[dialogue with contractions and filler words]."

Negative prompt: studio lighting, professional color grading, lens flare,
tripod-steady framing, text overlays, captions, subtitles, watermarks.
```

### Segment 2 of [N] — [Problem/Proof] (0:08–0:16)

[Same format. Same Ingredients, so the creator stays the same person.]

[Continue for all segments.]

---

## Step 4: Generate & Review

1. Generate each segment in Flow with both Ingredients attached
2. Check the creator looks like the same person across segments — if one drifts, regenerate it rather than accepting it
3. Check the product label is legible and not garbled
4. Check no captions or subtitles burned into the frame — Veo adds these unprompted, which is why every prompt carries a negative prompt against them
5. Stitch in order and export

---

## Step 5: Before You Publish

- [ ] Label the ad as AI-generated wherever you're running it
- [ ] No health, medical, or results claims in any line of dialogue
- [ ] Nothing framed as real customer testimony
- [ ] Product claims match what you can actually substantiate

---

## END OF OUTPUT FORMAT

---

## Prompt Writing Rules

### The Veo formula

Every prompt follows `[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`, with the audio lines after. The cinematography clause goes first and the style clause goes last — Veo weights both heavily, and burying them mid-paragraph is why "make it look like a phone video" often doesn't land.

The timestamp blocks are a Google-supported workflow for sequencing within a clip. Use `[00:00-00:04]` and `[00:04-00:08]` for an 8-second segment, or three shorter blocks when the beat has more movement in it.

### Getting the phone-video look

Other video models need a ban list because they default to polish. Veo responds better to explicit positive direction, so lead with what you want and use the negative prompt for the rest.

**Say:** `handheld smartphone video`, `camera held at arm's length`, `slight natural shake`, `natural window light`, `unpolished home video`, `realistic skin texture`, `phone camera depth of field`, `slightly imperfect framing`, `filmed by the subject themselves`

**Put in the negative prompt:** `studio lighting`, `professional color grading`, `lens flare`, `tripod-steady framing`, `shallow cinematic depth of field`, `text overlays`, `captions`, `subtitles`, `watermarks`

Don't name camera brands or film stocks. They pull hard toward a produced look and add trademark exposure for no benefit.

**Always negative-prompt captions and subtitles.** Veo has a habit of burning subtitles into dialogue clips. It's the single most common reason a good generation ends up unusable.

### Detail level

Each timestamp block wants 3–4 sentences of specifics: what each hand is doing, the exact expression, what's on the surface and what isn't, the light source and direction, the background. Anything left undescribed, Veo invents — and invented detail is where continuity breaks between segments.

### Audio

Veo generates dialogue, sound effects, and ambience natively with lipsync. Never tell the user to add voiceover afterwards.

Use Google's syntax exactly:
- `Ambient noise: warm kitchen room tone, faint refrigerator hum` — the soundscape
- `SFX: bottle cap clicking open` — discrete sounds
- `She says, "..."` — dialogue in quotation marks, attributed

Match ambience to the room, because silence sounds like a recording booth and makes everything feel staged: bathroom gets slight tile reverb, bedroom soft and carpeted, kitchen open with faint appliance hum, car muffled and close, outdoors natural ambience with slight wind.

### Dialogue

Nobody recommending something to a friend speaks in marketing copy.

- Contractions and filler: "I've been," "honestly," "like," "so basically"
- Fragments and run-ons are fine
- Genuinely curious or genuinely skeptical, never rehearsed
- Keep it to roughly 15–20 words per 8-second segment — more than that and Veo rushes the delivery or clips the ending

**Good:** "Okay so this is the one that's all over my feed right now — I wanna actually read the label."
**Bad:** "This revolutionary product has transformed my routine completely."
**Also bad, and blocked:** "I've been using this for two weeks and my skin completely cleared up."

### Ingredient budget

Flow takes up to three Ingredients per prompt.

```
creator  — the generated character   (same across ALL segments)
product  — your product photo        (same across ALL segments)
setting  — optional location plate   (only if the location keeps drifting)
```

Two is usually right. Add the setting plate only when the background won't hold still, since every slot you spend narrows what the prompt text can steer.

### Regional note

Availability of realistic-people generation varies by region, and some users outside the US report being blocked from uploading photorealistic people even when the image is AI-generated. If the user reports upload failures on their own generated character, that's the likely cause — and it's a Flow account/region limit, not something the prompt can fix.

### Veo facts

- Clip length: 4, 6, or 8 seconds
- Resolution: 720p or 1080p; aspect ratio 16:9 or 9:16
- Up to 3 Ingredients per prompt
- Native audio: dialogue with lipsync, SFX, and ambience generated together
- Ingredients to Video, Frames to Video, and Extend all carry audio
- Assets saved in a project can be recalled by typing `@` and the asset name
- One action arc per prompt — don't describe two scene changes in a single clip
