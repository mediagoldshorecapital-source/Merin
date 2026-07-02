#!/usr/bin/env bash
# Convert the July 4th video into an email-friendly GIF.
#
# Usage:
#   ./make-gif.sh                # downloads the video, writes july4.gif
#   ./make-gif.sh input.mp4      # convert a local file instead
#
# Requires ffmpeg (https://ffmpeg.org). On Mac: brew install ffmpeg
# If the result is over ~3 MB, lower FPS to 10 or add a duration cap
# (e.g. TRIM="-t 6" below) — email clients load big GIFs slowly.

set -euo pipefail

VIDEO_URL="https://d3k81ch9hvuctc.cloudfront.net/company/U8pRQr/videos/01KWHNTPHZANKJTDAXM70HXWR7.mp4"
IN="${1:-july4-source.mp4}"
OUT="july4.gif"
FPS=12          # smooth enough for email; raise to 15 if the file stays small
WIDTH=552       # matches the GIF slot width in email.html
TRIM=""         # e.g. TRIM="-ss 0 -t 6" to keep only the first 6 seconds

if [ ! -f "$IN" ]; then
  echo "Downloading video..."
  curl -sSL -o "$IN" "$VIDEO_URL"
fi

# Two-pass palette conversion = far better colors than a naive gif encode.
ffmpeg -y $TRIM -i "$IN" \
  -vf "fps=${FPS},scale=${WIDTH}:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4" \
  -loop 0 "$OUT"

echo ""
echo "Wrote $OUT ($(du -h "$OUT" | cut -f1))"
echo "Next: upload $OUT to Klaviyo (Content > Images), copy its hosted URL,"
echo "and paste it into the GIF slot in email.html (search for REPLACE-WITH-KLAVIYO-GIF-URL)."
