#!/usr/bin/env python3
"""Check that this machine can actually transcribe. Prints install commands if not."""
import shutil, subprocess, sys, importlib.util, platform

def has_mod(name):
    try:
        return importlib.util.find_spec(name) is not None
    except Exception:
        return False

def main():
    ok = True
    print("=== Competitor Ad Deconstruct — preflight ===\n")

    ff = shutil.which("ffmpeg")
    fp = shutil.which("ffprobe")
    print(f"ffmpeg   : {ff or 'MISSING'}")
    print(f"ffprobe  : {fp or 'MISSING'}")
    if not (ff and fp):
        ok = False
        mac = platform.system() == "Darwin"
        print("  -> install: " + ("brew install ffmpeg" if mac else
              "sudo apt-get update && sudo apt-get install -y ffmpeg"))

    backends = []
    if has_mod("mlx_whisper"):     backends.append("mlx-whisper (Apple Silicon, fastest)")
    if has_mod("faster_whisper"):  backends.append("faster-whisper (recommended)")
    if has_mod("whisper"):         backends.append("openai-whisper")
    if shutil.which("whisper-cli") or shutil.which("whisper.cpp"):
        backends.append("whisper.cpp CLI")

    print(f"\nASR backend: {', '.join(backends) if backends else 'MISSING'}")
    if not backends:
        ok = False
        print("  -> install one:")
        print("     pip install faster-whisper          # recommended, CPU-friendly")
        print("     pip install -U openai-whisper       # fallback")
        print("     pip install mlx-whisper             # Apple Silicon only")

    print(f"\npython-docx (optional, .docx export): "
          f"{'OK' if has_mod('docx') else 'MISSING -> pip install python-docx'}")
    print(f"yt-dlp (optional, URL download): {shutil.which('yt-dlp') or 'MISSING -> pip install yt-dlp'}")

    print("\n" + ("READY — run transcribe.py next." if ok else
          "NOT READY — install the items above, or ask the user to paste a transcript.\n"
          "Do NOT proceed to analysis without a real transcript."))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
