# BUILD-PROMPT — 2026-10-02-the-model-didnt-change-the-world-did · The Model Didn't Change. The World Did.

Paste-ready, from the toolkit root. Free end to end (Kokoro, Remotion, ffmpeg).

```bash
REEL=weekly_updates/2026-10-02-the-model-didnt-change-the-world-did

# STEP 0 — evidence first (it feeds the sheet). ~1 min, deterministic.
python3 $REEL/evidence/drift_run.py > $REEL/evidence/drift_run.out

# STEP 1 — the sheet is GENERATED from drift_run.csv. Edit build_beats.py, never
#          beat_sheet.json. --check re-asserts every spoken figure and the budgets.
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 2 — GATE P (human): Sai signs PEDAGOGY.md's VERDICT line. Claude never signs.

# STEP 3 — audio (master clock), then re-cue. The re-cue ASSERTS every B02/B03
#          reveal lands inside the 15 s comp; if it fails, move that row's cue earlier.
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py

# STEP 4 — render at true 4K, ONE BEAT PER CALL.
for b in B00 B01 B02 B03 B04 B05 B06 B07 B08; do python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 5 — review cut + GATE V, then the clean 16:9 master into the reel.
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/claude-sai-the-model-didnt-change-the-world-did.mp4 $REEL/1002-claude-sai-the-model-didnt-change-the-world-did.mp4
mv $REEL/claude-sai-the-model-didnt-change-the-world-did.verified.json $REEL/1002-claude-sai-the-model-didnt-change-the-world-did.verified.json

# STEP 6 — the same film in 9:16, 4K portrait.
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B01 B02 B03 B04 B05 B06 B07 B08; do python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art run $REEL/vertical --height 3840
./art final $REEL/vertical --height 3840 --out $REEL
#   then rename to 1002-claude-sai-the-model-didnt-change-the-world-did-vertical.mp4 (+ .verified.json)

# STEP 7 — probe: 3840,2160 and 2160,3840
ffprobe -v error -show_entries stream=width,height -of csv=p=0 $REEL/1002-*.mp4
```

## Data

`data/electricity.arff` is OpenML 151's file (md5 `8ca97867d960ae029ae3a9ac2c923d34`,
asserted by `drift_run.py`). To re-fetch:
`curl -sL https://openml.org/data/v1/download/2419/electricity.arff -o $REEL/data/electricity.arff`

## If you change any wording

Edit `build_beats.py` → audio → `build_beats.py` (re-cue; watch the 14.5 s assert)
→ `remotion_scenes.py --force --only B0X` → `./art run` → re-derive the vertical.

## Expected noise, not bugs

SKIN LINT wants `ClaudeTitleOutro` (wrong for this channel); GATE V underfill on
centred cards (B08 has `qc.sparse`); the portrait slate's burn-in edge-bleed.
