# BUILD-PROMPT — 2026-11-06-same-app-new-plants · Same App, New Plants

Paste-ready, from `/Users/nikhilkunapareddy/Documents/brutalist.art`.

```bash
REEL=weekly_updates/2026-11-06-same-app-new-plants
SLUG=claude-sai-same-app-new-plants

# STEP 0 — evidence: see PROMPTS.md (Gavia's evaluate + look-alike check at v0.5.0)

# STEP 1 — the sheet is GENERATED; every number is read from evidence/*.out
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py

# STEP 2 — GATE P (human): read PEDAGOGY.md, sign the VERDICT line.

# STEP 3 — audio (.venv: Kokoro), then re-cue
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 4 — the three image plates, both aspects (system python3: needs Pillow)
python3 $REEL/make_plates.py --preview && python3 $REEL/make_plates.py

# STEP 5 — the seven Remotion beats, one per call
for b in B00 B02 B04 B06 B07 B08 B09; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 6 — 16:9 review cut + GATE V, then the clean master
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/$SLUG.mp4 $REEL/1106-$SLUG.mp4
mv $REEL/$SLUG.verified.json $REEL/1106-$SLUG.verified.json

# STEP 7 — the same film in 9:16
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B02 B04 B06 B07 B08 B09; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art final $REEL/vertical --height 3840 --out $REEL/vertical
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/1106-$SLUG-vertical.mp4
mv $REEL/vertical/$SLUG-vertical.verified.json $REEL/1106-$SLUG-vertical.verified.json
```

## Re-taking the app screenshots

As in `../2026-10-30-every-three-seconds/BUILD-PROMPT.md`: scratch `GAVIA_DATA_DIR`,
window at (60, 40, 1396, 880) pt on the built-in display, AX helpers + an AXPress
helper ("Check for invasive plants" sits below the fold), `screencapture -x
-R60,40,1396,880`, re-place the window before each capture. The Model choice
lives in shared WebKit storage: it was Vegnet before and after.

## Pronunciation respellings

- `Vegnet` → "Veg Net" · `Loonet` → "Loon Net" · `Phragmites` → "frag-MY-teez".

## Expected noise, not bugs

- SKIN LINT at B09 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).
