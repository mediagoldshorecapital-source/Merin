# UGC Talking-Head Ad

One person, filming themselves on a phone, showing a product. The kind of ad that looks like a friend's story rather than a commercial.

Read this with `SKILL.md` — the Flow constraints, compliance rules, and shared craft there all apply. This file covers only what's specific to the format.

**Deliver the whole brief in one response. Don't ask clarifying questions** — make the creative calls yourself. If the user gave you very little, invent sensible specifics and commit to them.

---

## What makes this format work

The believability rests on **one person appearing in every shot**. If the creator's face changed halfway through, the viewer would notice instantly and the ad would collapse. So the creator Ingredient is generated once and reused everywhere, unchanged.

The second thing holding it up is that it must not look produced. The whole persuasive weight is "a real person filmed this on their phone" — every instinct toward polish works against you.

---

## Ingredient budget

```
creator — the generated character   (SAME across all segments)
product — the user's product photo  (SAME across all segments)
setting — optional location plate   (only if the background keeps drifting)
```

Two is usually right. Add the setting plate only when the location won't hold still, since every slot spent narrows what the prompt text can steer.

---

## Output structure

# Your UGC Ad — Flow Brief

**Product:** [name]
**Duration:** [total]s ([N] segments × 8s)
**Ad Structure:** Hook → Problem/Proof → Benefit/Demo → CTA
**Aspect ratio:** 9:16

---

## Step 1: Generate Your Creator as an Ingredient

This character appears in every segment. You're generating an original person, not uploading a photo of a real one.

In Flow, generate an image with this prompt, then save it as an Ingredient named `creator`:

```
Photorealistic portrait of a fictional person: [age range, build, hair,
skin tone, distinguishing features — specific enough to be repeatable].
Wearing [specific casual clothing]. Neutral relaxed expression, looking
at camera. Plain light grey background, soft even daylight, no props.
Shot on a smartphone front camera, natural skin texture, no makeup
styling, no retouching.
```

Generate 3–4 variations and pick one. Then stop — regenerating the character mid-ad gives you a different person.

**Optional setting plate**, if you want the location locked:

```
[Room type] interior, [time of day] light from [direction], [2-3 specific
details]. No people. Photographed on a smartphone, natural exposure.
```

---

## Step 2: Upload Your Product as an Ingredient

Your own product photo, named `product`. Shoot or crop it on a plain background, and keep the label large and simple — Veo garbles small text, and a mangled label makes the ad unusable.

---

## Step 3: Veo Prompts — Copy & Paste

Attach `creator` and `product` for every segment. Select **Ingredients to Video**, 8s, 9:16.

### Segment 1 of [N] — [Hook] (0:00–0:08)

**What's happening:** [One sentence]

```
Handheld smartphone video, [shot size] framing, camera held at arm's
length, slight natural shake, filmed by the subject themselves.

Using the provided images for the creator and the product.

[00:00-00:04] [Subject, action, context: who they are and what they're
wearing, what each hand is doing, their expression, the surface in front
of them and what is deliberately not on it, the light source and its
direction, 2-3 background details.]

[00:04-00:08] [What changes: the movement, the expression shift, how the
product enters or moves in frame. Same light, same background.]

Style and ambiance: unpolished home video, natural [window/lamp/daylight]
light only, realistic skin texture, phone camera depth of field, slightly
imperfect framing.

Ambient noise: [room tone matching the setting].
SFX: [a specific sound — a lid clicking, fabric rustle, a cup set down].
She says, "[dialogue with contractions and filler words]."

Negative prompt: studio lighting, professional color grading, lens flare,
tripod-steady framing, text overlays, captions, subtitles, watermarks.
```

### Segment 2 of [N] — [Problem/Proof] (0:08–0:16)

[Same format. Same Ingredients, so the creator stays the same person.]

[Continue for all segments.]

---

## Step 4: Generate & Review

1. Generate each segment with both Ingredients attached
2. Check the creator looks like the same person across segments — regenerate any that drift rather than accepting them
3. Check the product label is legible and not garbled
4. Check no captions burned into frame
5. Stitch in order and export

---

## Step 5: Before You Publish

- [ ] Label the ad as AI-generated wherever you're running it
- [ ] No health, medical, or results claims in any line of dialogue
- [ ] Nothing framed as real customer testimony
- [ ] Product claims match what you can substantiate

---

## Craft notes for this format

### The phone-video look

**Say in the prompt:** `handheld smartphone video`, `camera held at arm's length`, `slight natural shake`, `natural window light`, `unpolished home video`, `realistic skin texture`, `phone camera depth of field`, `slightly imperfect framing`, `filmed by the subject themselves`

**Put in the negative prompt:** `studio lighting`, `professional color grading`, `lens flare`, `tripod-steady framing`, `shallow cinematic depth of field`, plus the standard caption block

Don't name camera brands or film stocks — they pull hard toward a produced look and add trademark exposure for no benefit.

### Room tone by setting

Match it or the clip sounds like a booth: bathroom gets slight tile reverb, bedroom soft and carpeted, kitchen open with faint appliance hum, car muffled and close, living room warm and furnished, outdoors natural ambience with slight wind.

### Dialogue

**Good:** "Okay so this is the one that's all over my feed right now — I wanna actually read the label."
**Bad:** "This revolutionary product has transformed my routine completely."
**Blocked:** "I've been using this for two weeks and my skin completely cleared up."

The third one is the trap. It's the most natural thing to write in this format and it's fabricated testimony from a person who doesn't exist. Rewrite to curiosity or observation and the line gets better anyway.
