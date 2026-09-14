# Gemini Gem setup — Prime Ad Architect

Everything needed to create the Gem. The instructions themselves are in
`GEM_INSTRUCTIONS.txt` (paste-ready, no commentary to strip out).

---

## 1. Name

```
Prime Ad Architect
```

Alternatives if you want the function in the name: `Prime Ad Deconstructor` ·
`Competitor Ad Teardown — Prime` · `Prime Creative Engine`.

## 2. Description

```
Transcribes competitor supplement video ads word-for-word with timestamps, then deconstructs them into a 6-phase teardown — funnel and awareness classification, customer-psychology audit, a compliant Prime Ingredients shooting script, a reusable skeleton, and 3 alternative hooks.
```

## 3. Instructions

Paste the entire contents of `GEM_INSTRUCTIONS.txt` into the Instructions box.
It is ~14,800 characters across 7 sections:

| Section | Purpose |
|---|---|
| 1 | The overriding rule — the transcript is evidence, not a guess |
| 2 | Three-pass transcription protocol, run before any analysis |
| 3 | What to refuse (links, screenshots, "just guess") |
| 4 | The 6-phase output format |
| 5 | Funnel/awareness definitions and the bias vocabulary |
| 6 | Compliance gate, product facts, approved pricing |
| 7 | Self-audit checklist + the verification block it must print |

If the box rejects it for length, cut **Section 5** first and upload it as a
knowledge file instead — it is reference vocabulary, not enforcement. Never cut
Sections 1, 2, 6 or 7; those are what stop the Gem inventing a script.

## 4. Knowledge files to upload

| File | Why |
|---|---|
| `COMPETITOR_ADS_1.docx` | Your existing teardown — the Gem matches its layout far more reliably from an example than from a description |
| Prime product spec sheet or label | Lets it ground dose, actives and trust signals in a real document |
| A screenshot of your live pricing page | Keeps the offer table honest as prices change |

Add a second finished teardown once you have one. Two examples pin the format
much harder than one.

---

## How to use it

Upload the video file directly to the chat and say what you want:

> Break this down.

> Here's a competitor ad — full teardown plus the Prime version for my editor.

> Transcribe this word for word first, then do the psychology table.

**Batches:** upload one ad per message rather than five at once. Video
understanding degrades across multiple long files in a single turn, and one
ad's wording bleeding into another's transcript is the exact failure this is
built to avoid. Ask for a combined document at the end.

---

## Check it's working

Run this on the first real ad:

1. **Does the transcript sound like a person or like an ad template?** Real
   speech has filler, false starts and half-finished sentences. A transcript with
   none of that, in clean marketing prose, is usually invented.
2. **Spot-check three timestamps.** Scrub to 0:15, 0:30, 0:45 in the video and
   confirm the words match.
3. **Check every number by ear.** Doses and prices are the highest-risk items in
   the whole document.
4. **Confirm the verification block is printed** at the end, and that it is not
   claiming a clean run while the report contains `[unclear]` markers.

If a transcript comes back suspiciously clean, reply: *"Re-run Pass 2 of the
transcription protocol and mark every word you are not certain about."* A Gem
that starts reporting uncertainty is working correctly — silence about
uncertainty is the warning sign, not the marker itself.

---

## Honest limits of the Gem version

The repo skill (`.claude/skills/competitor-ad-deconstruct/`) runs real Whisper
speech recognition and then a verifier script that mechanically checks every
quote against the ASR output and exits non-zero until they match. **The Gem has
no equivalent.** Section 7 asks the model to audit itself, which helps and is
not the same thing — a model checking its own output is exactly the mechanism
that can fail silently.

So: the Gem is the fast path for triage, exploration and first drafts. For a
script that is actually going into production spend, run the ad through the repo
version, where the transcript is machine-produced and the compliance gate is
enforced by code rather than by good intentions.
