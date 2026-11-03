# BUILD-PROMPT

Run from `brutalist.art`. No paid calls, no upload.

```text
Rebuild REEL = .../youtube/claude-liam-walker-towerdefense-gamedev.

1. Confirm the takes in ../walker-towerdefense-captures match CAPTURE.md.
   To re-capture, use capture_driver.gd on an isolated git-archive copy,
   with harness config only.

2. python3 make_sheet.py author
3. python3 runtime/scripts/generate_audio_kokoro.py REEL
4. python3 make_sheet.py finish  (then, after rendering: python3 make_sheet.py ledger)
      It cuts exact-frame clips and writes coverage.json. It must print no
      unexpected held frames.
5. ./art godot-gamedev --check REEL --game <game>/godot
6. python3 runtime/scripts/remotion_scenes.py REEL
7. ./art final REEL --height 2160 --fps 30 --out REEL/exports/landscape
8. ./art godot-gamedev --check REEL --game <game>/godot
9. Inspect every beat at 15/50/85% from the master, and the outro.

Never retime gameplay. Never present the staged failure as normal play.
```
