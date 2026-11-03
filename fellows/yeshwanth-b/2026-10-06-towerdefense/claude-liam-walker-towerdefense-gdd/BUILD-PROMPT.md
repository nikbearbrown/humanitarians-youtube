# BUILD-PROMPT — rebuild this film end to end

Paste into Claude Code, run from the toolkit (`brutalist.art`). No paid calls; never publishes.

```text
Rebuild the film in ../Humanitarians AI Walker/TowerDefense-Godot/youtube/claude-liam-walker-towerdefense-gdd.

1. Verify the source has not moved:
   shasum -a 256 <game>/GDD.md must equal gdd-evidence.json document.sha256.
   If it differs, stop: excerpts are line-addressed.

2. Captures:
   ../walker-towerdefense-captures/takes/*.mp4 must match CAPTURE.md.
   To re-capture, follow CAPTURE.md exactly: isolated `git archive` copy,
   harness-only project.godot changes, capture_driver.gd, encode_take.sh.

3. Run:
   python3 make_sheet.py author
   python3 runtime/scripts/generate_audio_kokoro.py REEL
       (needs the Kokoro model and kokoro_onnx; espeak data must sit on a
       path under ~160 chars — see BUILD-LOG.md)
   python3 make_sheet.py finish
   ./art godot-gdd --check REEL --gdd <game>/GDD.md
   python3 runtime/scripts/remotion_scenes.py REEL      (pilot one beat first; inspect it)
   ./art final REEL --height 2160 --fps 30 --out REEL/exports/landscape
   ./art godot-gdd --check REEL --gdd <game>/GDD.md

4. Visual QC:
   Sample frames at 2 fps and at 15/50/85% of every beat, and READ them.
   Check the excerpts are verbatim, the status labels, the gameplay overlays,
   and the outro (title, @NikBearBrown, mascot, Liam reading the title,
   no jingle). Log the results in _qc/REPORT.md.

Never edit the game. Never claim it is finished, balanced, playtested, or
that it looks like the original. Do not upload.
```
