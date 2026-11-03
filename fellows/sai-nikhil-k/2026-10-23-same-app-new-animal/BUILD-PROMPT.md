# BUILD-PROMPT — 2026-10-23-same-app-new-animal · Same App, New Animal

Paste-ready, from `/Users/nikhilkunapareddy/Documents/brutalist.art`.

```bash
REEL=weekly_updates/2026-10-23-same-app-new-animal
SLUG=claude-sai-same-app-new-animal

# STEP 0 — evidence: see PROMPTS.md (seal split, Gavia's detector at v0.3.1, scale, crops)

# STEP 1 — the sheet is GENERATED; every number is read from evidence/*.out
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py

# STEP 2 — GATE P (human): read PEDAGOGY.md, sign the VERDICT line.

# STEP 3 — audio (.venv: Kokoro), then re-cue
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 4 — the four image plates, both aspects (system python3: needs Pillow)
python3 $REEL/make_plates.py --preview && python3 $REEL/make_plates.py

# STEP 5 — the seven Remotion beats, one per call
for b in B00 B02 B04 B06 B08 B09 B10; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 6 — 16:9 review cut + GATE V, then the clean master
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/$SLUG.mp4 $REEL/1023-$SLUG.mp4
mv $REEL/$SLUG.verified.json $REEL/1023-$SLUG.verified.json

# STEP 7 — the same film in 9:16
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B02 B04 B06 B08 B09 B10; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art final $REEL/vertical --height 3840 --out $REEL/vertical
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/1023-$SLUG-vertical.mp4
mv $REEL/vertical/$SLUG-vertical.verified.json $REEL/1023-$SLUG-vertical.verified.json
```

## Re-taking the app screenshots

Gavia must be frontmost on the built-in display; the session's host app needs
Screen Recording (System Settings → Privacy & Security). Launch a scratch copy so
the real history is untouched:
`open -n -a /Applications/Gavia.app --env GAVIA_DATA_DIR=<scratch>`, drive it with
the AX helpers from `../2026-10-02-refuse-dont-guess/ui/rec/` (`win`, `mouse`,
`allwins2`), capture with `screencapture -x -R x,y,w,h`. Don't touch the Updates
switch (it lives in shared WebKit storage).

## Pronunciation respellings

- `NOAA's` → "the NOAA …" (raw drops the 's).

## Expected noise, not bugs

- SKIN LINT at B10 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).
