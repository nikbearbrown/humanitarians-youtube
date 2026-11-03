# BUILD-PROMPT — 2026-10-19-inside-the-black-box · Inside the Black Box, Part 1

Paste-ready, from `/Users/nikhilkunapareddy/Documents/brutalist.art`.
Part 2 has its own folder and BUILD-PROMPT: `weekly_updates/2026-10-23-inside-the-black-box-part-2/`.

```bash
REEL=weekly_updates/2026-10-19-inside-the-black-box
SLUG=claude-sai-inside-the-black-box-part-1

# STEP 0 — evidence (system python3 + numpy; ~30 s)
python3 $REEL/evidence/train_nets.py > $REEL/evidence/train_nets.out

# STEP 1 — the sheet is GENERATED; it reads B05's numbers from train_nets.out.
#          Never hand-edit the JSON; never run this while a render is in flight.
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py

# STEP 2 — GATE P (human): read PEDAGOGY.md, sign the VERDICT line.

# STEP 3 — audio (.venv: Kokoro), then re-cue
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 4 — the seven Remotion beats, one per call
for b in B00 B02 B04 B05 B06 B07 B08; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 5 — the two figure plates, both aspects (system python3: needs Pillow)
python3 $REEL/make_plates.py --preview && python3 $REEL/make_plates.py

# STEP 6 — 16:9 review cut + GATE V, then the clean master
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/$SLUG.mp4 $REEL/1019-$SLUG.mp4
mv $REEL/$SLUG.verified.json $REEL/1019-$SLUG.verified.json

# STEP 7 — the same film in 9:16
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B02 B04 B05 B06 B07 B08; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art final $REEL/vertical --height 3840 --out $REEL/vertical
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/1019-$SLUG-vertical.mp4
mv $REEL/vertical/$SLUG-vertical.verified.json $REEL/1019-$SLUG-vertical.verified.json

# STEP 8 — math QC: B02 at each row reveal and at 15/50/85%, BOTH aspects.
```

## Pronunciation respellings (narration_text only)

- `ReLU` → "ray-loo"; `2023` → "twenty twenty-three"
- B05's decimals are generated as words by `spoken()` ("minus point four three").

## Expected noise, not bugs

- SKIN LINT at B08 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).
