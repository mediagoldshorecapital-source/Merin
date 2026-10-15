#!/usr/bin/env python3
"""Recover speech that Whisper's silence filter dropped.

Whisper's VAD treats dialogue under loud music (animated stories, VSLs) as
silence, so whole sentences can vanish without a flag. This finds the holes in
transcript.json -- gaps over --min-gap seconds, or long segments with too few
words for their length -- re-transcribes just those windows with the VAD off,
and writes the merged result.

Usage:
    python3 recover_gaps.py <workdir> [--model large-v3] [--min-gap 4]
    python3 recover_gaps.py <workdir> --windows 59-176 193-219   # explicit seconds

Writes <workdir>/transcript.json (original kept as transcript.orig.json) and
appends a "Recovered spans" section to transcript.txt. Recovered segments carry
the flag "gap-fill (no VAD)"; check them against the burned-in captions.
"""
import argparse
import json
import os
import shutil
import wave

import numpy as np


def ts(sec):
    return f"{int(sec // 60)}:{int(sec % 60):02d}"


def find_windows(segs, duration, min_gap):
    wins, prev = [], 0.0
    for s in segs:
        if s["start"] - prev > min_gap:
            wins.append([max(0.0, prev - 1), s["start"] + 1])
        span = s["end"] - s["start"]
        if span > 12 and len(s["text"].split()) < span:  # under 1 word/sec over 12 s
            wins.append([s["start"] - 1, s["end"] + 1])
        prev = s["end"]
    if duration and duration - prev > min_gap:
        wins.append([prev - 1, duration])
    return widen(segs, wins)


def widen(segs, wins):
    """Grow each window to cover every segment it overlaps, then merge.

    Overlapping segments are discarded before the re-run, so a window that cut
    one in half would lose the half outside it.
    """
    wins = sorted([list(w) for w in wins])
    changed = True
    while changed:
        changed = False
        for w in wins:
            for s in segs:
                if s["start"] < w[1] and s["end"] > w[0]:
                    if s["start"] < w[0] or s["end"] > w[1]:
                        w[0], w[1] = min(w[0], s["start"]), max(w[1], s["end"])
                        changed = True
        wins.sort()
        merged = []
        for w in wins:
            if merged and w[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], w[1])
            else:
                merged.append(w)
        wins = merged
    return [(round(max(0.0, a), 2), round(b, 2)) for a, b in wins]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("workdir")
    p.add_argument("--model", default="large-v3")
    p.add_argument("--min-gap", type=float, default=4.0)
    p.add_argument("--windows", nargs="*", help="explicit start-end pairs in seconds")
    a = p.parse_args()

    tj = os.path.join(a.workdir, "transcript.json")
    wav = os.path.join(a.workdir, "audio16k.wav")
    d = json.load(open(tj))
    with wave.open(wav, "rb") as w:
        audio = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    duration = len(audio) / 16000

    wins = (widen(d["segments"], [tuple(map(float, x.split("-"))) for x in a.windows]) if a.windows
            else find_windows(d["segments"], duration, a.min_gap))
    if not wins:
        print("No gaps found; transcript unchanged.")
        return

    from faster_whisper import WhisperModel
    model = WhisperModel(a.model, device="auto", compute_type="int8")
    keep = [s for s in d["segments"] if not any(s["start"] < e and s["end"] > b for b, e in wins)]
    added = []
    for b, e in wins:
        res, _ = model.transcribe(audio[int(b * 16000):int(e * 16000)], language="en", vad_filter=False,
                                  word_timestamps=True, condition_on_previous_text=False)
        for g in res:
            added.append({
                "start": b + g.start, "end": b + g.end, "text": g.text.strip(),
                "avg_logprob": g.avg_logprob, "no_speech_prob": g.no_speech_prob,
                "compression_ratio": g.compression_ratio,
                "words": [{"start": b + x.start, "end": b + x.end, "word": x.word.strip(),
                           "probability": x.probability} for x in (g.words or [])],
                "flags": ["gap-fill (no VAD)"],
            })

    shutil.copy(tj, os.path.join(a.workdir, "transcript.orig.json"))
    d["segments"] = sorted(keep + added, key=lambda s: s["start"])
    d.setdefault("meta", {})["gap_fill"] = {"windows": wins, "model": a.model, "vad": False}
    json.dump(d, open(tj, "w"), indent=1)

    lines = ["", "---", "## Recovered spans (re-run without VAD — verify against captions)", ""]
    lines += [f"[{ts(s['start'])}–{ts(s['end'])}] {s['text']}" for s in added]
    with open(os.path.join(a.workdir, "transcript.txt"), "a") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Re-ran {len(wins)} window(s): " + ", ".join(f"{ts(b)}–{ts(e)}" for b, e in wins))
    print(f"Recovered {len(added)} segment(s); transcript.json updated.")


if __name__ == "__main__":
    main()
