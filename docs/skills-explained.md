# Your Two Ad Skills, Explained in Plain English

*A guide to what these things actually are, what they do, and how to use them — written for a human, not a machine.*

---

## First: what even is a "skill"?

A **skill** is a written instruction sheet that Claude reads before it starts working.

That's genuinely all it is. It's a text file. There's no code, no software, no integration. If you printed it out and handed it to a freelance copywriter, they could follow it.

The only clever part is *when* it gets read. Claude keeps a list of every skill you've installed, along with a one-line summary of each. When you ask for something that matches one of those summaries, Claude opens that file and follows it. You don't have to say "use the skill" — you just say "make me an ad for my collagen powder," and the right instruction sheet loads on its own.

Think of it as the difference between explaining your brand rules to a new freelancer every single time, versus handing them a folder they already know to reach for.

**Why bother?** Because the instructions are long and specific. Nobody wants to retype "never use the word cinematic, always describe the light source, write dialogue with filler words" every time they want an ad. You write it once. It applies forever.

---

## What these two skills actually do

Both of them do the same fundamental job: **they write prompts for a video AI called Seedance 2.0.**

Important thing to be clear about, because it trips people up: neither skill makes video. They make *text* — very detailed text — that you then copy and paste into Seedance, which makes the video. The skill is the director writing the shot list. Seedance is the camera crew.

The output you get is a "director's brief" — a document containing casting links, shot descriptions, and dialogue, all formatted so you can work through it top to bottom.

### Skill 1 — `seedance-20-ugc-ad-director`

**The format:** One person, talking to their phone, recommending a product. The kind of ad that looks like a friend's Instagram story rather than a commercial.

**What it gives you:**

1. **Pinterest links to cast your creator.** It writes the search URLs for you. You click through, find a face you like, and save that photo. That one photo is used in every single shot so the same person appears throughout.
2. **More Pinterest links** for settings and product-holding poses, if you want them.
3. **The prompts themselves** — one per 15-second segment, broken into 5-second beats, each beat describing the camera, the person, their hands, their expression, the lighting, and the background in obsessive detail.
4. **Dialogue** written to sound unscripted — contractions, "honestly," "like," half-finished sentences.
5. **A checklist** for reviewing and stitching the clips together.

**The structure it follows:** Hook → Problem/Proof → Benefit/Demo → CTA. Standard direct-response ad shape.

### Skill 2 — `street-interview-ad-director`

**The format:** A host stops strangers on the street and asks them about a product. Several different people, cut together. The "man-on-the-street" or "vox pop" format.

**What it gives you:** Same shape of deliverable — casting links, prompts, dialogue, checklist — but adapted throughout for a format with multiple people in it.

**The structure it follows:** Question Hook → Skeptic Reactions → The Turn → Verdict/CTA.

---

## The one idea that separates them

This is worth understanding properly, because it explains nearly every difference between the two files.

**A talking-head UGC ad is believable because the same person appears in every shot.** If the creator's face changed halfway through, you'd notice instantly and the ad would fall apart. So that skill's most emphatic rule is: pick one person, use them everywhere, never change them.

**A street interview is believable because different people appear in every shot.** That variety *is* the evidence. Six strangers, six opinions — that's what makes it feel like a real sample rather than a paid testimonial. If everyone looked similar, it would read as staged.

So the two formats need opposite rules about the same thing.

The question the fork had to answer was: if the person can't be the constant, what is? The answer is **the place.**

> A viewer believes a street interview when the block, the light, and the mic stay the same while the faces change. That's what says *"we stood on one corner for an afternoon"* rather than *"we shot six unrelated clips."*

So in the street interview skill, these stay locked across every shot: the host, the street, the direction of the sunlight, the microphone, and the product. And these change freely: the respondent, their age, their style, their opinion.

| | UGC Ad Director | Street Interview Director |
|---|---|---|
| **What stays the same** | The creator's face | The street, light, host, and mic |
| **What changes** | Setting, beat of the ad | The person answering |
| **People on camera** | One | Two per shot, many across the ad |
| **Voices in the audio** | One | Two — interviewer and respondent |
| **Segment length** | 15 seconds, uniform | 6–15 seconds, deliberately varied |
| **Where it's shot** | Indoors, usually | Outdoors, one location |
| **Use it when** | One creator vouches for the product | Strangers react to the product |

---

## The jargon, decoded

The skill files are written for a machine, so they're dense with shorthand. Here's what all of it means.

**UGC** — "User-Generated Content." Industry term for ads deliberately made to look like an ordinary person filmed them, not an agency. The whole point is that it doesn't look like an ad.

**Vox pop / man-on-the-street** — Both mean the same thing: interviewing random members of the public. "Vox pop" is short for *vox populi*, Latin for "voice of the people." Journalism term that migrated into advertising.

**9:16** — The shape of the frame. Tall and narrow, the shape of a phone held upright. This is what TikTok, Reels, and Shorts want.

**@Image1 / @Image2 / @Image3** — These are labels for photos you upload to Seedance. When a prompt says "@Image1 is the creator," it's telling the AI *"the person in the first photo I gave you is the one in this scene."* It's how you keep the same face across multiple generations.

Here's how each skill assigns them:

```
UGC Ad Director                    Street Interview Director
─────────────────                  ─────────────────────────
@Image1 = the creator              @Image1 = the host        (same every shot)
          (same every shot)        @Image2 = the respondent  (different every shot)
@Image2 = setting reference        @Image3 = the product     (same every shot)
@Image3 = the product
```

Notice that in the street interview version, `@Image2` gets taken away from "setting" and given to the respondent. The setting has to be written out in words instead — which turns out to be necessary anyway, since the background has to be described identically in every prompt to stay consistent.

**Room tone** — The particular quiet sound of a specific space. A bathroom has a slight echo off the tiles. A car sounds muffled and close. A street has traffic and footsteps. Recording engineers capture this deliberately because silence sounds fake — total silence is the sound of a recording studio, and it makes everything feel staged.

**"Anti-cinematic"** — Both skills carry a long list of banned words: *cinematic*, *lens flare*, *bokeh*, *color grade*, *gimbal*, camera brands like ARRI and RED. These are all words that make video AI produce beautiful, expensive-looking footage. Which is exactly wrong here. Beautiful footage reads as an advertisement and gets scrolled past. The skills push hard in the opposite direction — handheld, shaky, natural light, phone-quality — because that's what makes someone stop and watch.

**Lipsync** — The mouth movements matching the words. Seedance 2.0 generates speech and matching mouth movement together, which is why both skills forbid telling you to "add voiceover in post." You don't need to. It's already there.

**Segment** — One generated clip. Seedance produces 4–15 seconds at a time, so a 60-second ad is built as several segments and stitched together afterward in an editor.

---

## How you actually use one

The workflow is the same for both:

**1. Describe your ad.** Tell Claude the product and roughly what you want. "Make me a street interview ad for our $80 collagen powder, angle is that people think it's overpriced until they hear what's in it." You don't need to name the skill — the right one loads on its own.

**2. Get your brief.** Claude outputs the whole thing in one response. It won't ask you follow-up questions; both skills specifically instruct it to make the creative decisions itself and deliver everything at once.

**3. Cast from Pinterest.** Click the search links. Find faces you like. Save those photos.

> **The one rule that actually matters here:** only save *clean* photos. No emoji stickers, no watermarks, no text overlays, no app interface visible. Seedance rebuilds everything it sees as a physical object in the scene — so a watermark becomes a weird floating artifact in your finished ad.

**4. Upload and generate.** Into Seedance, one segment at a time. Attach the right photos as @Image1, @Image2, @Image3. Paste the prompt. Generate.

**5. Check consistency.** Does the same face appear throughout (UGC)? Do the street, light, and mic match across cuts (street interview)? Regenerate anything that drifted.

**6. Stitch and export.** Assemble in order. For street interviews, cut tight — trim the dead air at the start and end of each answer, because the format lives on pace.

---

## Two opinions baked into the street interview skill

Worth knowing about, since they're editorial calls rather than technical ones. Both are a couple of lines to change if you disagree.

**It tells the AI to include one bad answer.** An ad where all six strangers love the product is the exact thing that makes viewers suspicious. One lukewarm or unconvinced response buys credibility for every other answer in the cut. It's counterintuitive, and it works.

**It defaults the host to off-camera.** You hear their voice and see a hand holding the mic into frame, but never their face. This is easier to produce — you're not fighting to keep a second face consistent across every shot — and it's extremely common in the real format. On-camera is available when you want the host's reactions to be part of the ad.

---

## Moving these to Google Gemini

You can rebuild both as **Gems**, which are Gemini's version of the same idea: a saved set of instructions that Gemini follows whenever you chat with it.

The mechanics differ in a few ways that affect how the instructions have to be written:

**A skill loads itself. A Gem doesn't.** Claude decides to open a skill based on what you asked for. A Gem is simply always on for as long as you're talking to it — you pick it from a list and then it's in effect. This means the description field stops being functional and becomes purely a label for you. It also means each format needs its own separate Gem; there's no automatic switching between them.

**Gems have no file structure.** A skill can be a folder with reference documents and scripts that get loaded when needed. A Gem is one text box. Everything has to live in it. Fine for these two — they're single files already — but it caps how far you can grow them.

**Gemini needs to be told to shut up more firmly.** It tends to open with "Certainly! Here's your brief:" and close with an offer to revise. It also asks clarifying questions more readily than Claude does. The Gem instructions include explicit lines to suppress all three, because the whole value here is getting a clean, complete, copy-pasteable document in one go.

**Gemini needs a persona statement.** Skills can open by describing a job. Gems work noticeably better when you start with a direct "You are a…" — so both Gem versions begin that way.

The two Gem specs — name, description, and full instruction text ready to paste — are in the files alongside this one.
