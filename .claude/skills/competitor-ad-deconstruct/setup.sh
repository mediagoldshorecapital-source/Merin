#!/usr/bin/env bash
# One-time setup for the competitor-ad-deconstruct skill.
#   bash .claude/skills/competitor-ad-deconstruct/setup.sh
#   bash .claude/skills/competitor-ad-deconstruct/setup.sh --model medium   # smaller/faster
set -uo pipefail

MODEL="large-v3"
SKIP_MODEL=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --model) MODEL="$2"; shift 2 ;;
    --skip-model) SKIP_MODEL=1; shift ;;
    -h|--help) echo "usage: setup.sh [--model large-v3|medium|small] [--skip-model]"; exit 0 ;;
    *) echo "unknown option: $1"; exit 1 ;;
  esac
done

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
say() { printf "\n\033[1m==> %s\033[0m\n" "$1"; }

# ---------- 1. ffmpeg ----------
say "Checking ffmpeg"
if command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg already installed: $(command -v ffmpeg)"
elif [[ "$(uname -s)" == "Darwin" ]]; then
  if command -v brew >/dev/null 2>&1; then
    brew install ffmpeg
  else
    echo "Homebrew not found. Install it from https://brew.sh then re-run this script."
    exit 1
  fi
elif command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update && sudo apt-get install -y ffmpeg
elif command -v dnf >/dev/null 2>&1; then
  sudo dnf install -y ffmpeg
else
  echo "Could not detect a package manager. Install ffmpeg manually, then re-run."
  exit 1
fi

# ---------- 2. python packages ----------
say "Installing Python packages"
PY="$(command -v python3 || command -v python)"
[[ -z "$PY" ]] && { echo "python3 not found — install Python 3.9+ first."; exit 1; }

# Apple Silicon gets mlx-whisper too; it is markedly faster on M-series chips.
EXTRA=""
if [[ "$(uname -s)" == "Darwin" && "$(uname -m)" == "arm64" ]]; then
  EXTRA="mlx-whisper"
fi
"$PY" -m pip install --upgrade pip >/dev/null 2>&1
if ! "$PY" -m pip install faster-whisper python-docx $EXTRA; then
  echo "pip install failed. If your Python is externally managed, try:"
  echo "  $PY -m venv ~/.venvs/ads && source ~/.venvs/ads/bin/activate && bash $0"
  exit 1
fi

# ---------- 3. pre-download the model ----------
# Doing this now means the first real ad doesn't stall on a multi-GB download
# midway through a transcription.
if [[ "$SKIP_MODEL" -eq 0 ]]; then
  say "Pre-downloading Whisper model: $MODEL (one-time, large-v3 is ~3GB)"
  if ! "$PY" - "$MODEL" <<'PYCHECK'
import sys
from faster_whisper import WhisperModel
m = sys.argv[1]
print(f"fetching {m} ...")
WhisperModel(m, device="cpu", compute_type="int8")
print("model cached OK")
PYCHECK
  then
    echo
    echo "Model download failed (firewall, proxy, or offline?)."
    echo "Everything else is installed. Re-run later, or use --model with a smaller"
    echo "size, or point transcribe.py --model at a local model directory."
  fi
fi

# ---------- 4. verify ----------
say "Preflight"
"$PY" "$HERE/scripts/preflight.py"

say "Done"
echo "Try it:  \"here's a competitor ad, break it down\"  with a video file path."
