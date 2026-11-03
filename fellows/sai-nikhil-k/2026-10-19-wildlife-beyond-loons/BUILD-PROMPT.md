# BUILD-PROMPT — 2026-10-19-wildlife-beyond-loons · Seals Pass, Seabirds Wait

Paste-ready. Run from the toolkit root,
`/Users/nikhilkunapareddy/Documents/brutalist.art`.

```bash
REEL=weekly_updates/2026-10-19-wildlife-beyond-loons
SLUG=claude-sai-seals-pass-seabirds-wait

# STEP 0 — evidence (system python3, standard library; downloads public files if missing)
python3 $REEL/evidence/maine_labels.py > $REEL/evidence/maine_labels.out
python3 $REEL/evidence/seal_labels.py  > $REEL/evidence/seal_labels.out

# STEP 1 — the sheet is GENERATED from build_beats.py, which reads every number
#          from the two .out files. Never hand-edit the JSON, and NEVER run
#          build_beats.py while remotion_scenes.py is rendering.
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py

# STEP 2 — GATE P (human): read PEDAGOGY.md, sign the VERDICT line.

# STEP 3 — audio (.venv: Kokoro), then re-cue math rows, data rows and photo reveals
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 4 — the two photo plates, both aspects (system python3: needs Pillow)
python3 $REEL/make_plates.py --preview      # look at images/_preview-*.png first
python3 $REEL/make_plates.py

# STEP 5 — the nine Remotion beats, one per call
for b in B00 B01 B02 B03 B05 B07 B08 B09 B10; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 6 — 16:9 review cut + GATE V, then the clean master
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/$SLUG.mp4 $REEL/1019-$SLUG.mp4
mv $REEL/$SLUG.verified.json $REEL/1019-$SLUG.verified.json

# STEP 7 — the same film in 9:16. shorts.py takes the photo beats from pantry/.
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B01 B02 B03 B05 B07 B08 B09 B10; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art final $REEL/vertical --height 3840 --out $REEL/vertical
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/1019-$SLUG-vertical.mp4
mv $REEL/vertical/$SLUG-vertical.verified.json $REEL/1019-$SLUG-vertical.verified.json

# STEP 8 — math QC: B03 at each row reveal and at 15/50/85%, BOTH aspects.
```

## Pronunciation respellings (narration_text only — keep them on a rewrite)

- `2019` → "twenty nineteen"
- `BirdNET` → "Bird Net" (raw reads "bird N-E-T")
- `NOAA's` → "the NOAA" (raw drops the 's)

## Changing a photo

1. `cd $REEL/evidence && python3 commons_search.py "<query>"` — lists only PD /
   CC0 / CC BY / CC BY-SA files with author and licence.
2. `python3 commons_fetch.py "File:<title>" <slug> --out ../images/src`.
3. Edit the panel and its `CREDIT` line in `build_beats.py`; add a focus point
   in `make_plates.py` if the subject is off-centre.
4. `build_beats.py` → `make_plates.py --preview` → look → `make_plates.py --only B0X`
   → STEP 6 → STEP 7.

## Expected noise, not bugs

- SKIN LINT at B10 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate from `./art run $REEL/vertical` reports edge-bleed on
  every frame (its own timecode burn-in). `./art final`'s gate is the verdict.
