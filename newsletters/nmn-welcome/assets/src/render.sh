#!/usr/bin/env bash
# Re-render the NMN welcome newsletter illustrations from their SVG source.
# Flat-vector art, hand-authored (no AI), warm Prime Ingredients palette:
#   cream #F4E8DE · maroon #8A2A33 · gold #C99A3F · charcoal #2A2A33
#
# Requires a Chromium/Chrome binary (used headless to rasterize the SVG).
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$DIR/.."
CHROME="${CHROME:-$(command -v google-chrome || command -v chromium || echo /opt/pw-browsers/chromium-1194/chrome-linux/chrome)}"

shot () { # <src.html> <w> <h> <out.png>
  "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
    --force-device-scale-factor=1 --window-size="$2,$3" \
    --screenshot="$4" "file://$1" >/dev/null 2>&1
}

shot "$DIR/hero.svg.html"          1200 600 "$OUT/hero.png"
shot "$DIR/molecule-band.svg.html" 1200 220 "$OUT/molecule-band.png"
echo "Rendered: $OUT/hero.png, $OUT/molecule-band.png"
