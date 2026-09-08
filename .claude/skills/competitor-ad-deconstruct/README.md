# competitor-ad-deconstruct

Turns a competitor video ad into a verified, compliant 6-phase creative
deconstruction for Prime Ingredients NMN Ultimate 10-in-1.

## Install (once per machine)

```bash
bash .claude/skills/competitor-ad-deconstruct/setup.sh
```

Installs ffmpeg, faster-whisper and python-docx, pre-downloads the Whisper model
so your first real ad doesn't stall on a multi-GB fetch mid-transcription, and
runs preflight. Use `--model medium` for a smaller/faster model, or
`--skip-model` to defer the download.

Manual equivalent:

```bash
brew install ffmpeg            # macOS   (Linux: sudo apt-get install -y ffmpeg)
pip install faster-whisper python-docx
python3 scripts/preflight.py   # confirms both are visible
```

**Firewalled or offline machines:** model weights come from huggingface.co. If
that host is blocked, `transcribe.py` says so explicitly and tells you how to
copy a cache over or point `--model` at a local model directory — it will not
quietly fall back to guessing.

## Use

Just point Claude at a file — "here's a competitor ad, break it down" is enough
to trigger the skill. Under the hood it runs:

```bash
python3 scripts/transcribe.py ad.mp4 --outdir work/ --model large-v3
python3 scripts/extract_frames.py ad.mp4 --outdir work/ --every 2
# ... report is written to work/ad-deconstruction.md ...
python3 scripts/verify_report.py work/ad-deconstruction.md --transcript work/transcript.json
python3 scripts/build_docx.py work/ad-deconstruction.md --out COMPETITOR_ADS_2.docx
```

## How it avoids making things up

Claude cannot hear audio or watch video, so left alone it would write a
*plausible* ad script rather than *this* ad's script. Three mechanisms prevent that:

1. **Real ASR is the only source of quotes.** `transcribe.py` runs Whisper and
   writes `transcript.txt`; the skill quotes from that file and nothing else. No
   transcript, no report — the script exits with an error instead of degrading.
2. **The recognizer's own uncertainty is surfaced.** `flags.md` lists low-confidence
   words, silence-hallucinated boilerplate and repeated segments, which get marked
   `[unclear: …]` / `[inaudible …]` in the report instead of being smoothed over.
3. **A verifier proves it afterwards.** `verify_report.py` checks every quoted
   fragment against the ASR output, checks beat timestamps against the real
   duration, and blocks drug/disease claims, banned tropes, competitor brand names
   and off-spec prices in the Prime copy. It exits non-zero until they're fixed.

Visuals work the same way: frames are extracted and looked at before any
on-screen text is described.

## Editing the rules

`references/compliance_rules.json` is the single source of truth for banned
claims, competitor brands, approved prices and product specs — the verifier reads
it directly. Change prices or add a competitor there, not in the prose docs.
