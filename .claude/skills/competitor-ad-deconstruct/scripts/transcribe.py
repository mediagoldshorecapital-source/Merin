#!/usr/bin/env python3
"""
Verbatim ASR transcription for competitor ad analysis.

Produces transcript.txt / .json / .srt plus flags.md, which lists spans the
recognizer itself is unsure about. Whisper-family models fail in two ways that
look identical to good output -- they invent filler over silence/music, and they
silently smooth over words they didn't catch -- so every segment is scored and
suspicious ones are surfaced rather than buried.
"""
import argparse, json, os, re, shutil, subprocess, sys, importlib.util

AUDIO_EXT = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg", ".opus", ".wma"}
VIDEO_EXT = {".mp4", ".mov", ".webm", ".mkv", ".avi", ".m4v", ".mpg", ".mpeg", ".ts"}

# Biases the decoder toward keeping disfluencies instead of tidying them into
# clean prose. "Word for word" includes the ums -- they carry the cadence a
# creator team has to actually perform.
VERBATIM_PROMPT = ("Um, uh, like, you know, I mean, kinda, gonna, wanna, sorta, "
                   "right? So, okay, and, but, actually, literally.")

# Phrases Whisper emits over silence, music beds and end cards.
HALLUCINATION_PATTERNS = [
    r"^thanks? (?:so much )?for watching",
    r"^thank you for watching", r"^subscribe to", r"^please subscribe",
    r"^like and subscribe", r"^see you (?:in the )?next (?:video|time)",
    r"^\[?(?:music|applause|silence|laughter|blank[_ ]audio)\]?\.?$",
    r"^(?:bye|okay|thank you)[.!]?$", r"^www\.", r"^subtitles? by",
    r"^amara\.org", r"^transcription by",
]

def has_mod(n):
    try: return importlib.util.find_spec(n) is not None
    except Exception: return False

def die(msg, code=2):
    print(f"\nERROR: {msg}\n", file=sys.stderr)
    print("Do NOT write an analysis without a real transcript. Report this to the "
          "user and ask them to install the missing tool or paste a transcript.",
          file=sys.stderr)
    sys.exit(code)

NETWORK_HINTS = ("proxy", "403", "forbidden", "connection", "timeout", "timed out",
                 "network", "unreachable", "resolve", "ssl", "certificate",
                 "max retries", "connectionerror", "httperror", "offline",
                 "failed to download", "couldn't connect", "could not connect")

def is_network_error(exc):
    """Model weights come from the internet; a blocked download is not the same
    failure as a missing library, and sends the user somewhere completely
    different, so it gets its own message."""
    blob = f"{type(exc).__name__} {exc}".lower()
    return any(h in blob for h in NETWORK_HINTS)

def ts(sec, sep=":"):
    sec = max(0.0, float(sec)); m, s = divmod(int(sec), 60); h, m = divmod(m, 60)
    return f"{h}:{m:02d}{sep}{s:02d}" if h else f"{m}{sep}{s:02d}"

def srt_ts(sec):
    sec = max(0.0, float(sec)); ms = int(round((sec - int(sec)) * 1000))
    m, s = divmod(int(sec), 60); h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def probe_duration(path):
    if not shutil.which("ffprobe"): return None
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration", "-of",
                              "default=noprint_wrappers=1:nokey=1", path],
                             capture_output=True, text=True, check=True).stdout.strip()
        return float(out)
    except Exception:
        return None

def extract_audio(src, outdir):
    """16kHz mono PCM -- what every Whisper backend wants anyway."""
    if not shutil.which("ffmpeg"):
        if os.path.splitext(src)[1].lower() in AUDIO_EXT:
            return src  # backend can usually read plain audio directly
        die("ffmpeg is required to pull audio out of a video file.\n"
            "  macOS: brew install ffmpeg\n"
            "  Linux: sudo apt-get install -y ffmpeg")
    wav = os.path.join(outdir, "audio16k.wav")
    cmd = ["ffmpeg", "-y", "-i", src, "-vn", "-ac", "1", "-ar", "16000",
           "-c:a", "pcm_s16le", wav]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(wav):
        die(f"ffmpeg could not decode {src}.\n{r.stderr[-1500:]}")
    return wav

# ---------------- backends ----------------

def run_faster_whisper(audio, model, lang, verbatim):
    from faster_whisper import WhisperModel
    # faster-whisper runs on CTranslate2, not torch; torch is only consulted to
    # detect a usable GPU, so its absence must never break the CPU path.
    device, compute = "cpu", "int8"
    try:
        import torch
        if torch.cuda.is_available():
            device, compute = "cuda", "float16"
    except Exception:
        pass
    print(f"[faster-whisper] model={model} device={device}", file=sys.stderr)
    m = WhisperModel(model, device=device, compute_type=compute)
    segs, info = m.transcribe(
        audio, language=lang, word_timestamps=True, beam_size=5,
        vad_filter=True, vad_parameters={"min_silence_duration_ms": 500},
        condition_on_previous_text=False,   # stops one hallucination seeding the next
        initial_prompt=VERBATIM_PROMPT if verbatim else None,
    )
    out = []
    for s in segs:
        out.append({
            "start": s.start, "end": s.end, "text": (s.text or "").strip(),
            "avg_logprob": getattr(s, "avg_logprob", None),
            "no_speech_prob": getattr(s, "no_speech_prob", None),
            "compression_ratio": getattr(s, "compression_ratio", None),
            "words": [{"start": w.start, "end": w.end, "word": w.word.strip(),
                       "probability": getattr(w, "probability", None)}
                      for w in (s.words or [])],
        })
        print(f"  [{ts(s.start)}] {out[-1]['text'][:90]}", file=sys.stderr)
    return out, getattr(info, "language", lang)

def run_openai_whisper(audio, model, lang, verbatim):
    import whisper
    print(f"[openai-whisper] model={model}", file=sys.stderr)
    m = whisper.load_model(model)
    r = m.transcribe(audio, language=lang, word_timestamps=True,
                     condition_on_previous_text=False, beam_size=5,
                     initial_prompt=VERBATIM_PROMPT if verbatim else None,
                     verbose=False)
    out = []
    for s in r.get("segments", []):
        out.append({
            "start": s["start"], "end": s["end"], "text": (s.get("text") or "").strip(),
            "avg_logprob": s.get("avg_logprob"), "no_speech_prob": s.get("no_speech_prob"),
            "compression_ratio": s.get("compression_ratio"),
            "words": [{"start": w.get("start"), "end": w.get("end"),
                       "word": (w.get("word") or "").strip(),
                       "probability": w.get("probability")}
                      for w in s.get("words", [])],
        })
    return out, r.get("language", lang)

def run_mlx_whisper(audio, model, lang, verbatim):
    import mlx_whisper
    repo = model if "/" in model else f"mlx-community/whisper-{model}-mlx"
    print(f"[mlx-whisper] model={repo}", file=sys.stderr)
    r = mlx_whisper.transcribe(audio, path_or_hf_repo=repo, language=lang,
                               word_timestamps=True, condition_on_previous_text=False,
                               initial_prompt=VERBATIM_PROMPT if verbatim else None)
    out = []
    for s in r.get("segments", []):
        out.append({
            "start": s["start"], "end": s["end"], "text": (s.get("text") or "").strip(),
            "avg_logprob": s.get("avg_logprob"), "no_speech_prob": s.get("no_speech_prob"),
            "compression_ratio": s.get("compression_ratio"),
            "words": [{"start": w.get("start"), "end": w.get("end"),
                       "word": (w.get("word") or "").strip(),
                       "probability": w.get("probability")}
                      for w in s.get("words", [])],
        })
    return out, r.get("language", lang)

def pick_backend(requested):
    avail = []
    if has_mod("mlx_whisper"):    avail.append("mlx")
    if has_mod("faster_whisper"): avail.append("faster")
    if has_mod("whisper"):        avail.append("openai")
    if requested != "auto":
        if requested not in avail:
            die(f"backend '{requested}' not installed (available: {avail or 'none'})")
        return requested
    if not avail:
        die("No speech-recognition backend installed.\n"
            "  pip install faster-whisper      # recommended\n"
            "  pip install -U openai-whisper   # fallback\n"
            "  pip install mlx-whisper         # Apple Silicon")
    for pref in ("faster", "mlx", "openai"):
        if pref in avail: return pref
    return avail[0]

# ---------------- confidence flagging ----------------

def flag_segments(segs):
    """Mark segments the model is unsure about, or that smell like invention."""
    seen = {}
    for i, s in enumerate(segs):
        f = []
        txt = (s["text"] or "").strip()
        low = txt.lower()
        nsp, alp, cr = s.get("no_speech_prob"), s.get("avg_logprob"), s.get("compression_ratio")

        if nsp is not None and nsp > 0.6:
            f.append(f"likely-no-speech (no_speech_prob={nsp:.2f})")
        if alp is not None and alp < -1.0:
            f.append(f"low-confidence (avg_logprob={alp:.2f})")
        if cr is not None and cr > 2.4:
            f.append(f"repetitive-output (compression_ratio={cr:.2f})")
        for pat in HALLUCINATION_PATTERNS:
            if re.search(pat, low):
                f.append("boilerplate-phrase (classic Whisper filler over silence)")
                break
        if low and low in seen and i - seen[low] <= 2:
            f.append("duplicate-of-previous-segment")
        if low: seen[low] = i

        words = [w for w in s.get("words", []) if w.get("probability") is not None]
        weak = [w["word"] for w in words if w["probability"] < 0.45]
        if weak:
            f.append("weak-words: " + ", ".join(f'"{w}"' for w in weak[:8]))
        if s["end"] - s["start"] > 0.5 and len(txt.split()) > 22:
            f.append("suspiciously-dense (check against audio)")

        s["flags"] = f
    return segs

# ---------------- writers ----------------

def write_outputs(segs, outdir, meta):
    with open(os.path.join(outdir, "transcript.json"), "w") as fh:
        json.dump({"meta": meta, "segments": segs}, fh, indent=2)

    lines = [f"# Verbatim transcript — {os.path.basename(meta['source'])}",
             f"# backend={meta['backend']} model={meta['model']} "
             f"language={meta['language']} duration={ts(meta['duration'] or 0)}",
             "# Quote ONLY from this file. Bracketed notes are uncertainty markers,",
             "# not spoken words.", ""]
    for s in segs:
        mark = "  <<FLAGGED: " + "; ".join(s["flags"]) + ">>" if s["flags"] else ""
        lines.append(f"[{ts(s['start'])}–{ts(s['end'])}] {s['text']}{mark}")
    lines += ["", "---", "## Continuous text (no timestamps)", "",
              " ".join(s["text"] for s in segs if not any(
                  x.startswith(("likely-no-speech", "boilerplate")) for x in s["flags"]))]
    open(os.path.join(outdir, "transcript.txt"), "w").write("\n".join(lines) + "\n")

    srt = []
    for i, s in enumerate(segs, 1):
        srt.append(f"{i}\n{srt_ts(s['start'])} --> {srt_ts(s['end'])}\n{s['text']}\n")
    open(os.path.join(outdir, "transcript.srt"), "w").write("\n".join(srt))

    flagged = [s for s in segs if s["flags"]]
    fm = ["# ASR confidence flags", "",
          f"{len(flagged)} of {len(segs)} segments need a human/eye check.", ""]
    if not flagged:
        fm.append("No suspicious segments. Transcript can be quoted as-is.")
    else:
        fm += ["Handle these in the report as:",
               '- low confidence -> keep the word, mark it `[unclear: "word" ~0:31]`',
               "- no-speech / boilerplate -> do NOT quote it; write `[no speech 0:52–0:58]`",
               "- inaudible -> `[inaudible 0:44–0:46]`", ""]
        for s in flagged:
            fm.append(f"- **[{ts(s['start'])}–{ts(s['end'])}]** \"{s['text']}\"")
            for x in s["flags"]:
                fm.append(f"    - {x}")
    open(os.path.join(outdir, "flags.md"), "w").write("\n".join(fm) + "\n")
    return len(flagged)

def main():
    p = argparse.ArgumentParser(description="Verbatim ASR for competitor ad analysis")
    p.add_argument("input")
    p.add_argument("--outdir", default="./ad-workdir")
    p.add_argument("--model", default="large-v3",
                   help="large-v3 (best) | medium | small | base | tiny, "
                        "or a path to a locally downloaded model directory "
                        "(for offline / firewalled machines)")
    p.add_argument("--language", default="en", help="or 'auto'")
    p.add_argument("--backend", default="auto", choices=["auto", "faster", "openai", "mlx"])
    p.add_argument("--no-verbatim-prompt", action="store_true",
                   help="disable the disfluency-preserving prompt")
    a = p.parse_args()

    src = os.path.abspath(a.input)
    if not os.path.exists(src):
        die(f"input not found: {src}")
    ext = os.path.splitext(src)[1].lower()
    if ext not in AUDIO_EXT | VIDEO_EXT:
        die(f"unsupported extension '{ext}'. Give me a real audio/video file "
            f"(not a URL, screenshot, or document).")

    os.makedirs(a.outdir, exist_ok=True)
    duration = probe_duration(src)
    audio = extract_audio(src, a.outdir)
    backend = pick_backend(a.backend)
    lang = None if a.language == "auto" else a.language
    verbatim = not a.no_verbatim_prompt

    runner = {"faster": run_faster_whisper, "openai": run_openai_whisper,
              "mlx": run_mlx_whisper}[backend]
    try:
        segs, detected = runner(audio, a.model, lang, verbatim)
    except Exception as e:
        msg = f"{type(e).__name__}: {e}"
        if is_network_error(e):
            die(f"could not fetch the '{a.model}' model weights: {msg}\n\n"
                f"The backend is installed but the download was blocked — usually a\n"
                f"corporate firewall, an egress proxy, or an offline machine.\n"
                f"Options, in order of effort:\n"
                f"  1. Pre-download once on a machine with open internet, then copy\n"
                f"     the cache over:  ~/.cache/huggingface  (faster-whisper/mlx)\n"
                f"                      ~/.cache/whisper      (openai-whisper)\n"
                f"  2. Point --model at a local model directory:\n"
                f"     python3 transcribe.py ad.mp4 --model /path/to/faster-whisper-large-v3\n"
                f"  3. Allow huggingface.co (or openaipublic.azureedge.net for\n"
                f"     openai-whisper) through the network policy.\n\n"
                f"Until the weights are available this machine cannot transcribe. Ask\n"
                f"the user to paste a transcript rather than analyzing an ad unheard.")
        die(f"transcription failed with backend '{backend}': {msg}")

    if not segs:
        die("ASR returned zero segments — the file may have no speech track. "
            "Confirm with the user before going further.")

    segs = flag_segments(segs)
    if duration is None and segs:
        duration = segs[-1]["end"]
    meta = {"source": src, "backend": backend, "model": a.model,
            "language": detected or a.language, "duration": duration,
            "segment_count": len(segs),
            "word_count": sum(len(s["text"].split()) for s in segs)}
    nflag = write_outputs(segs, a.outdir, meta)

    print(f"\nTranscribed {meta['word_count']} words / {len(segs)} segments "
          f"({ts(duration or 0)}) -> {a.outdir}/transcript.txt")
    print(f"Flagged segments needing review: {nflag}  (see {a.outdir}/flags.md)")
    print("\nNext: read transcript.txt AND flags.md in full, then build the report.")

if __name__ == "__main__":
    main()
