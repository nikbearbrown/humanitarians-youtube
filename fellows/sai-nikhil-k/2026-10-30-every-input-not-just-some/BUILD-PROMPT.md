# BUILD-PROMPT — 2026-10-30-every-input-not-just-some · Every Input, Not Just Some

Paste-ready, from `/Users/nikhilkunapareddy/Documents/brutalist.art`.

```bash
REEL=weekly_updates/2026-10-30-every-input-not-just-some
SLUG=claude-sai-every-input-not-just-some

# STEP 0 — evidence: see PROMPTS.md (toy fuzz-vs-solver, Theorem index tally)

# STEP 1 — the sheet is GENERATED; every number is read from evidence/*.out
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py

# STEP 2 — GATE P (human): read PEDAGOGY.md, sign the VERDICT line.

# STEP 3 — audio (.venv: Kokoro), then re-cue
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 4 — the two image plates (B02, B05), both aspects (system python3: needs Pillow)
python3 $REEL/make_plates.py --preview && python3 $REEL/make_plates.py

# STEP 5 — the eight Remotion beats, one per call
for b in B00 B01 B03 B04 B06 B07 B08 B09; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 6 — 16:9 review cut + GATE V, then the clean master
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/$SLUG.mp4 $REEL/1030-$SLUG.mp4
mv $REEL/$SLUG.verified.json $REEL/1030-$SLUG.verified.json

# STEP 7 — the same film in 9:16
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B01 B03 B04 B06 B07 B08 B09; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art final $REEL/vertical --height 3840 --out $REEL/vertical
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/1030-$SLUG-vertical.mp4
mv $REEL/vertical/$SLUG-vertical.verified.json $REEL/1030-$SLUG-vertical.verified.json
```

## Images

Anthropic's figures come from the post's CDN (URLs in each sidecar); the GIF
chart is frame 474 of 598. Screenshots use Remotion's bundled
chrome-headless-shell (`--screenshot --force-device-scale-factor=2`), which never
touches the screen. Commons photos via `../2026-09-25-the-model-that-doesnt-write-back/evidence/commons_fetch.py`.

## Pronunciation respellings

- `seL4` → "S.E.L. four" · `RISC-V` → "risk five" · `ARM` → "Arm" · `AI` → "A.I.".

## Expected noise, not bugs

- SKIN LINT at B09 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).
