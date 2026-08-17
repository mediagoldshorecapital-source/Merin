---
name: street-interview-ad-director
description: Create street interview (vox pop / man-on-the-street) video ad prompts for Seedance 2.0 — the format where a host stops strangers on the sidewalk and asks them about a product. Give it a product, angle, or rough script and get Pinterest casting links for the host and every respondent, plus segment-by-segment Seedance prompts with two-voice dialogue, ready to copy-paste. Use this whenever the user mentions street interviews, man-on-the-street, vox pop, sidewalk interviews, "asking random people", "stopping strangers", reaction ads, or any ad where several different people get interviewed on camera — including when they only describe the format without naming it. For single-creator talking-head UGC ads where one person films themselves, use seedance-20-ugc-ad-director instead.
---

# Street Interview Ad Director

This is the sibling of the UGC ad director, built for a format that breaks its central rule. A UGC ad works because **one creator** stays consistent across every shot. A street interview works because **many different people** appear — that variety is the entire proof. If everyone answering looks like they were cast by the same agency, the ad dies.

So the constant moves. Read the next section before anything else; it's the idea the whole skill hangs on.

---

## The continuity contract

In a talking-head UGC ad the anchor is the person. Here the person changes every cut, so the anchor becomes **the place**. A viewer believes a street interview when the block, the light, and the mic stay the same while the faces change — that's what says "we stood on one corner for an afternoon" rather than "we shot six unrelated clips."

Hold these constant across every single segment, and state them explicitly in every prompt:

| Constant | Why it matters |
|---|---|
| **The host** (`@Image1`) | Same person asking, same clothes, same voice. The one recurring face. |
| **The location** | Same street, same storefronts, same corner. Reuse the exact background wording. |
| **Time of day & light direction** | Sun can't jump from overhead to golden hour between cuts. Pick one and repeat it verbatim. |
| **The microphone** | Same handheld mic, same windscreen, in every shot. |
| **The product** (`@Image3`) | Same bottle, same label, same wear. |

Let these vary freely — variety here is the point:

- **The respondent** (`@Image2`) — new person each segment
- Their age, style, energy, and verdict
- Where exactly on the block they're standing
- Whether they're amused, skeptical, in a hurry, or won over

---

## EXACT OUTPUT FORMAT — follow this structure every time

Do not ask clarifying questions. Make the creative calls yourself and deliver everything in one response. Every output includes Pinterest links.

# Your Street Interview Ad — Director's Brief

**Product:** [name]
**The Question:** "[the one question the host asks everyone — this is the ad's hook]"
**Duration:** [total]s ([N] segments, [8-15]s each)
**Structure:** Question Hook → Skeptic Reactions → The Turn → Verdict/CTA

---

## Step 1: Cast Your Host on Pinterest

The host appears in every segment and is the only recurring face. Approachable beats polished — someone you'd actually stop for.

**Browse these and pick ONE:**

1. [Description] → [Pinterest URL]
2. [Description] → [Pinterest URL]
3. [Description] → [Pinterest URL]

**What to pick:** Natural daylight, casual clothes, relaxed posture, phone-quality feel. No studio lighting, no magazine poses, no heavy makeup.

**Only use CLEAN photos** — no emoji stickers, watermarks, text overlays, or app UI. Seedance recreates whatever it sees as a physical object, so a watermark becomes a floating artifact in your ad.

Your pick becomes **@Image1** and gets uploaded to every segment.

> **Host on camera or off?** Off-camera is the easier build — the audience only hears the host's voice and sees a hand holding the mic into frame, so you never fight to keep a second face consistent. Choose on-camera only if the ad needs the host's reactions. Say which one you picked in the brief, then write every prompt that way.

---

## Step 2: Cast Your Respondents — One Per Segment

Cast for **contrast**. If all [N] respondents read as the same demographic, the ad stops looking like a random sample and starts looking staged. Spread them across age, style, and energy, and give each one a different attitude going in.

**Segment 1 — [beat] — [who they are, e.g. "woman, late 20s, gym clothes, in a hurry"]:**
→ [Pinterest URL]

**Segment 2 — [beat] — [who they are]:**
→ [Pinterest URL]

[Continue for every segment. Clean photos only.]

Each becomes **@Image2** for its own segment.

---

## Step 3: Location & Product References (Optional)

One location reference keeps your background wording honest across segments.

1. [Street/setting search] → [Pinterest URL]
2. [Product-in-hand search] → [Pinterest URL]

---

## Step 4: Seedance 2.0 Prompts — Copy & Paste

For each segment upload: **@Image1** (host), **@Image2** (that segment's respondent), **@Image3** (product photo — you provide this).

### Segment 1 of [N] — [Question Hook] ([0:00-0:10])

**What's happening:** [One sentence]

```
9:16. 10 seconds. Single continuous shot. Street interview. iPhone handheld,
slight camera shake, filmed at arm's length.

@Image1 is the interviewer. @Image2 is the person being stopped.
@Image3 is the product.

[0:00-0:04] [3-4 sentences. Where the camera sits and how high. The
respondent's full appearance — clothes, hair, what they're carrying, which
way they're facing. The unbranded foam-windscreen mic entering frame from
the left. The exact street: storefronts, parked cars, pedestrians passing
behind. The sun's direction and quality. What is NOT in frame.]

[0:04-0:07] [3-4 sentences. Their expression shifting as they hear the
question. What each hand does. Whether they look at the mic, the host, or
the camera. Same light, same background, same foot traffic.]

[0:07-0:10] [3-4 sentences. The final beat — the reaction that ends the
clip. Body position, eye line, product position if it's in frame.]

Audio: Street ambience — passing traffic, distant chatter, footsteps on
pavement, faint wind across the mic. Interviewer: [voice character — age,
gender, tone, energy], off-camera, slightly further from the mic.
Respondent: [voice character], close on the mic, natural street-volume
speech with pauses and filler words.
Interviewer: "[the question]"
Respondent: "[the answer, with contractions and filler words]"
```

### Segment 2 of [N] — [Skeptic Reaction] ([0:10-0:20])

[Same format. @Image1 and the street stay identical — only @Image2 changes.]

[Continue for all segments.]

---

## Step 5: Generate & Stitch

1. Generate every segment in Seedance 2.0
2. Check the host, mic, and background match across segments — that consistency is what sells the format
3. Check the respondents feel genuinely different from each other
4. Regenerate any segment that drifts, keeping the same @Image1
5. Cut them together tight — trim dead air at the head and tail of each answer. Street interviews live on pace.

---

## END OF OUTPUT FORMAT

Everything above is the structure to follow. Below are the rules for writing the prompts themselves.

---

## Prompt Writing Rules

### Segment length and rhythm

Seedance generates 4–15 seconds per run, and the format works best when **one segment holds exactly one exchange** — one question, one answer, one reaction. Trying to fit two respondents into a single prompt produces a muddled scene, because the model handles one action arc at a time.

- **Rapid-fire reaction montage:** 6–8s per segment, more segments. Punchy, and the cuts do the comedy.
- **Standard answer:** 10–12s. Enough for a real thought.
- **The turn** (someone actually tries the product): 15s. This beat needs room.

Vary them. Uniform segment lengths make an ad feel metronomic; real interviews don't have a rhythm section.

### Anti-cinematic rules

A street interview that looks *produced* reads as an ad and gets scrolled past. The whole persuasive weight of the format is "this is unedited footage of real reactions," so every craft instinct toward polish works against you here.

**Always use:** `iPhone handheld`, `slight camera shake`, `natural daylight`, `street interview`, `filmed at arm's length`, `casual`, `9:16`

**Never use:** `cinematic`, camera brands (`ARRI`, `RED`, `Blackmagic`), `anamorphic`, `film grain`, `dramatic lighting`, `speed ramp`, `lens flare`, `whip pan`, `crane`, `dolly`, `steadicam`, `gimbal`, `Dutch angle`, `color grade`, `LUT`, `bokeh`, `epic`, `stunning`, `slow motion` (unless "iPhone slow-mo"), `depth of field` alone (say "phone camera depth of field")

**Street-specific traps:**
- No crowd gathered watching the interview — real passersby ignore cameras
- No perfectly framed, centered composition — let the respondent sit slightly off-center
- No empty street. Emptiness reads as a set. Always describe pedestrians moving in the background.
- No branded mic flag or lettering on the mic. Seedance garbles small text, and a mangled logo is the fastest way to break the illusion. Specify a plain black or unbranded mic.

### Camera framing

Phone held at arm's length by a person of ordinary height means the camera sits **slightly below eye level**, chest-up on the respondent, tilted a few degrees. Say this explicitly — left alone, the model defaults to a level, well-composed shot that looks like a tripod.

### Detail level

Every 3–4 second block needs 3–4 sentences of specifics: what each hand is doing, the exact facial expression, what's in the background, the sun's direction, what is *not* in frame. Anything you leave undescribed, Seedance invents — and invention is where artifacts come from.

### Audio direction

Seedance 2.0 generates dialogue with lipsync, ambient sound, and room tone together, natively. Never tell the user to add voiceover in post.

Street audio is doing real work here: a clean, quiet recording sounds like a studio and undoes the whole premise. Every prompt gets **traffic, distant chatter, footsteps, and faint wind on the mic**, plus whatever suits the specific location (bus hiss, café clatter, construction two blocks over, a siren passing).

**Two-voice handling.** The interviewer and respondent are not at the same distance from the microphone, and getting that right is most of what makes the audio believable:

- **Interviewer:** slightly off-mic, a touch quieter and further away, whether or not they're on camera
- **Respondent:** close on the mic, clearest element in the mix
- Both raised to **street volume** — people talk louder outdoors without noticing

Write the exchange as labelled lines so the model knows who speaks when:

```
Interviewer: "Would you pay eighty bucks for a moisturizer?"
Respondent: "Eighty? For — no. Absolutely not."
```

### Dialogue rules

Nobody stopped on a sidewalk speaks in marketing copy. They hedge, backtrack, laugh mid-sentence, and answer a slightly different question than the one they were asked.

- Contractions and filler: "I mean," "honestly," "like," "wait, really?"
- Fragments, false starts, self-interruptions
- Let them repeat the question back before answering — that's what people actually do
- Skeptics should sound genuinely unconvinced, not like they're setting up a punchline

**Good:** "Eighty dollars? I mean — for what? Like, what's in it that's eighty dollars?"
**Bad:** "That seems expensive, but I'd be willing to try it if it works."

**Let some answers land badly.** An ad where all six strangers love the product is an ad nobody believes. One lukewarm or unconvinced answer buys credibility for every other answer in the cut.

### Pinterest URL format

`https://www.pinterest.com/search/pins/?q=WORDS+SEPARATED+BY+PLUS+SIGNS`

For the host, search interviewer or presenter energy. For respondents, combine demographic + clothing style + street setting so the results already look like people caught mid-errand: `young+woman+gym+clothes+walking+city+sidewalk`.

### Reference image mapping

```
@Image1 = host / interviewer   (SAME across all segments)
@Image2 = respondent            (DIFFERENT every segment)
@Image3 = product photo         (user provides; same across all segments)
```

This is the inversion that separates this skill from the UGC director, where `@Image1` was the single recurring creator and `@Image2` held a setting reference. Here the location lives in the prompt text instead — it has to be described in words anyway to stay consistent across cuts.

### Seedance 2.0 facts

- Input: up to 9 images + 3 videos + 3 audio (12 total) — three images per segment leaves plenty of headroom
- Output: 4–15 seconds per generation, up to 2K, 9:16 for social
- Native audio: dialogue with lipsync, ambient sound, and room tone generated together
- Handles long, detailed prompts well, especially with @Image references
- One action arc per prompt — one exchange per segment, always
