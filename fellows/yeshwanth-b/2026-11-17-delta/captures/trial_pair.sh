#!/bin/zsh
# Headless trials of campaign1 then campaign2 from an empty save folder.
W="${0:A:h}"; GD=/Users/yeshwanthbalaji/Downloads/Godot.app/Contents/MacOS/Godot
rm -rf "$HOME/Library/Application Support/delta-filmcapture"
"$W/assemble.sh" || exit 1
cd "$W/capture"
for t in campaign1 campaign2; do
  $GD --headless --path . --fixed-fps 30 --script res://harness/capture_driver.gd -- $t "$W/trial/$t" nosave seed=${SEED:-1} > "$W/trial/$t.log" 2>&1
  echo "$t rc=$? fails=$(grep -c '"pass":false' "$W/trial/$t/inputs.jsonl")"
done
