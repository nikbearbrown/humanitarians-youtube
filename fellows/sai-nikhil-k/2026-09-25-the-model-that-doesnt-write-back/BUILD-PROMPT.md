# BUILD-PROMPT — 2026-09-25-the-model-that-doesnt-write-back · The Model That Doesn't Write Back

Paste-ready. Run from the toolkit root,
`/Users/nikhilkunapareddy/Documents/brutalist.art`.

```bash
REEL=weekly_updates/2026-09-25-the-model-that-doesnt-write-back
SLUG=claude-sai-the-model-that-doesnt-write-back

# STEP 0 — the sheet is GENERATED from build_beats.py (narration, patterns,
#          typeset math, photo panels + cue words). Never hand-edit the JSON,
#          and NEVER run build_beats.py while remotion_scenes.py is rendering:
#          the renderer writes its start-of-run copy of the sheet back.
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py

# STEP 1 — GATE P (human): read PEDAGOGY.md, sign the VERDICT line.

# STEP 2 — audio, then re-cue math rows, data rows and photo reveals to it
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 3 — the eight Remotion beats, one per call
for b in B00 B02 B04 B05 B07 B08 B09 B10; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 4 — the three photo plates, both aspects (system python3: needs Pillow)
#          → media/B01|B03|B06.mp4  and  pantry/B01|B03|B06-916.mp4
python3 $REEL/make_plates.py --preview      # look at images/_preview-*.png first
python3 $REEL/make_plates.py

# STEP 5 — 16:9 review cut + GATE V, then the clean master
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/$SLUG.mp4 $REEL/0925-$SLUG.mp4

# STEP 6 — the same film in 9:16. shorts.py takes the photo beats from pantry/.
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B02 B04 B05 B07 B08 B09 B10; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art final $REEL/vertical --height 3840 --out $REEL/vertical
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/0925-$SLUG-vertical.mp4

# STEP 7 — math QC: B04 at each row reveal and at 15/50/85%, BOTH aspects.
```

## Changing a photo

1. `python3 $REEL/evidence/commons_search.py "<query>"` — lists only PD / CC0 /
   CC BY / CC BY-SA files with author and license.
2. `cd $REEL/evidence && python3 commons_fetch.py "File:<title>" <slug>` —
   downloads to `images/src/` with a license sidecar.
3. Edit the panel and the `CREDIT` line in `build_beats.py`; add a focus point
   in `make_plates.py` if the subject is off-centre.
4. `build_beats.py` → `make_plates.py --only B0X` → STEP 5 → STEP 6.

## Expected noise, not bugs

- SKIN LINT at B10 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate from `./art run $REEL/vertical` reports edge-bleed on
  every frame (its own timecode burn-in). `./art final`'s gate is the verdict.
