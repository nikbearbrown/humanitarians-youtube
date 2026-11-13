# BUILD-PROMPT — 2026-10-30-every-three-seconds · Every Three Seconds

Paste-ready, from `/Users/nikhilkunapareddy/Documents/brutalist.art`.

```bash
REEL=weekly_updates/2026-10-30-every-three-seconds
SLUG=claude-sai-every-three-seconds

# STEP 0 — evidence: see PROMPTS.md (drone test rebuilt, Gavia's detector at v0.5.0)

# STEP 1 — the sheet is GENERATED; every number is read from evidence/*.out
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py

# STEP 2 — GATE P (human): read PEDAGOGY.md, sign the VERDICT line.

# STEP 3 — audio (.venv: Kokoro), then re-cue
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 4 — the two image plates, both aspects (system python3: needs Pillow)
python3 $REEL/make_plates.py --preview && python3 $REEL/make_plates.py

# STEP 5 — the eight Remotion beats, one per call
for b in B00 B02 B03 B04 B05 B07 B08 B09; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 6 — 16:9 review cut + GATE V, then the clean master
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/$SLUG.mp4 $REEL/1030-$SLUG.mp4
mv $REEL/$SLUG.verified.json $REEL/1030-$SLUG.verified.json

# STEP 7 — the same film in 9:16
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B02 B03 B04 B05 B07 B08 B09; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art final $REEL/vertical --height 3840 --out $REEL/vertical
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/1030-$SLUG-vertical.mp4
mv $REEL/vertical/$SLUG-vertical.verified.json $REEL/1030-$SLUG-vertical.verified.json
```

## Re-taking the app screenshots

Gavia must be frontmost on the built-in display, at window (60, 40, 1396, 880) pt;
the session's host app needs Screen Recording. Launch a scratch copy so the real
history is untouched: `open -n -a /Applications/Gavia.app --env GAVIA_DATA_DIR=<scratch>`,
drive it with the AX helpers from `../2026-10-02-refuse-dont-guess/ui/rec/` (`win`,
`mouse`, `allwins2`) plus an AXPress helper for off-screen buttons, and capture
with `screencapture -x -R60,40,1396,880`. Re-place the window before every
capture: another window can slide over it. Don't touch the Updates switch or
the Model choice (shared WebKit storage with the real install; it was Vegnet).

## Pronunciation respellings

- `BirdNET` → "BirdNet" · `loonet` → "Loon Net" · `Mount Desert` → "Mount Dessert".

## Expected noise, not bugs

- SKIN LINT at B09 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).
