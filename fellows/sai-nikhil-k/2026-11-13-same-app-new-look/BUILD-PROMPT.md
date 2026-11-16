# BUILD-PROMPT — 2026-11-13-same-app-new-look · Same App, New Look

Paste-ready, from `/Users/nikhilkunapareddy/Documents/brutalist.art`.

```bash
REEL=weekly_updates/2026-11-13-same-app-new-look
SLUG=claude-sai-same-app-new-look

# STEP 0 — evidence: see PROMPTS.md (contrast.py; recapture.mjs on both versions)

# STEP 1 — the sheet is GENERATED; every number is read from evidence/
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py

# STEP 2 — GATE P (human): read PEDAGOGY.md, sign the VERDICT line.

# STEP 3 — audio (.venv: Kokoro), then re-cue (reveals are authored in comp time)
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 4 — the before/after plate, both aspects (system python3: needs Pillow)
python3 $REEL/make_plates.py --preview && python3 $REEL/make_plates.py

# STEP 5 — the six Remotion beats, one per call
for b in B00 B02 B03 B04 B05 B06; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 6 — 16:9 review cut + GATE V, then the clean master
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/$SLUG.mp4 $REEL/1113-$SLUG.mp4
mv $REEL/$SLUG.verified.json $REEL/1113-$SLUG.verified.json

# STEP 7 — the same film in 9:16
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B02 B03 B04 B05 B06; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art final $REEL/vertical --height 3840 --out $REEL/vertical
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/1113-$SLUG-vertical.mp4
mv $REEL/vertical/$SLUG-vertical.verified.json $REEL/1113-$SLUG-vertical.verified.json
```

## If the changes get approved before posting

B04's narration ("But all five changes are proposals on a branch. None ships
until I approve it.") and the verdict card's line 4 become false. Edit them in
`build_beats.py`, then STEP 3 → B04 with `--force` → STEP 6 → STEP 7.

## Pronunciation respellings

- `Inter` → "Inntur" (narration only; the screen keeps "Inter").

## Expected noise, not bugs

- SKIN LINT at B00 (portrait) / B06 asking for other cold-open/outro patterns — wrong for this channel.
- The portrait slate (`./art run $REEL/vertical`) reports 14 BLOCKER edge-bleed: its own burn-in.
  The clean candidate's gate (`vertical/_qc/REPORT.md` after `./art final`) is 0 / 0.
