# PROMPTS — Same App, New Animal

**No open generation slots.** Seven Remotion compositions and four plates of
real screenshots, a NOAA survey frame and Commons photos. No image model, no
paid API.

## B00 — the on-screen typed ask

> Gavia finds loons in photos, on your own computer. What would it take to make the same app count other wildlife, like seals or Maine's seabirds? Test it on them first.

## B09 — the handoff the viewer can paste

> Pick one animal near me. Find a labelled photo dataset whose licence lets me ship a trained model, tell me how many pixels the animal covers in a typical survey photo, and who counts it by hand today. Link every source.

## Evidence commands

```bash
REEL=weekly_updates/2026-10-23-same-app-new-animal
python3 $REEL/evidence/seal_split.py > $REEL/evidence/seal_split.out     # 20 frames, ~770 MB
python3 $REEL/evidence/seal_scale.py > $REEL/evidence/seal_scale.out
python3 $REEL/evidence/make_survey_crops.py
# Gavia's detector: clone github.com/nikhil-kunapareddy/gavia at v0.3.1, copy
# evidence/seal_check.rs into desktop/src-tauri/examples/, then in desktop/src-tauri:
cargo run --release --example seal_check -- --split $REEL/evidence/data/seals/split.txt
cargo run --release --example evaluate -- --split $REEL/evidence/data/seals/split.txt [--tiled]
```
