#!/bin/zsh
# Encode a take's saved viewport frames (3049x2160, the engine's own render)
# into a 3840x2160 30 fps H.264 file. The game frame is centred; the side bars
# (#1f2329) are padding added here, not game pixels.
set -eu
frames="$1"; out="$2"
ffmpeg -v error -y -framerate 30 -i "$frames/%05d.png" \
  -vf "pad=3840:2160:395:0:color=0x1f2329,format=yuv420p" \
  -c:v libx264 -preset medium -crf 14 -r 30 -movflags +faststart "$out"
