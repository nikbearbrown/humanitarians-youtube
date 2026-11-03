#!/bin/zsh
# Run one scripted-input capture take. capture_driver.gd appends every rendered
# engine frame (3840x2160 RGB) to 150-frame raw chunk files; this script encodes
# each finished chunk (x264 crf 12), deletes it, and finally joins the chunks.
set -u
take="$1"; out="$2"; here="${0:A:h}"
GD=/Users/yeshwanthbalaji/Downloads/Godot.app/Contents/MacOS/Godot
rm -rf "$out"; mkdir -p "$out/frames" "$out/chunks"
( cd "$here/.." && "$GD" --path . --fixed-fps 30 --script res://harness/capture_driver.gd -- "$take" "$out" > "$out/run.log" 2>&1; echo $? > "$out/godot.rc" ) &
k=0
while true; do
  base=$(printf "%s/frames/%05d" "$out" $k)
  if [[ -f "$base.ready" ]]; then
    ffmpeg -v error -y -f rawvideo -pix_fmt rgb24 -s 3840x2160 -r 30 -i "$base.raw" \
      -c:v libx264 -preset veryfast -crf 12 -pix_fmt yuv420p -r 30 "$out/chunks/$(printf %05d $k).mp4"
    rm -f "$base.raw" "$base.ready"; k=$((k + 1)); continue
  fi
  if [[ -f "$out/godot.rc" && ! -f "$base.ready" ]]; then break; fi
  sleep 1
done
ls "$out/chunks"/*.mp4 | sed "s/^/file '/; s/$/'/" > "$out/chunks/list.txt"
ffmpeg -v error -y -f concat -safe 0 -i "$out/chunks/list.txt" -c copy -movflags +faststart "$out/take.mp4"
mv "$out/frames/DONE" "$out/frames.count" 2>/dev/null
rm -rf "$out/chunks" "$out/frames"
exit $(cat "$out/godot.rc")
