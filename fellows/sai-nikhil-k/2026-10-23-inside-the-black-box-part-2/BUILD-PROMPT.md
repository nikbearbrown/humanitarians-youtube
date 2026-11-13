# BUILD-PROMPT — 2026-10-23-inside-the-black-box-part-2 · Inside the Black Box, Part 2

Paste-ready, from `/Users/nikhilkunapareddy/Documents/brutalist.art`.
Part 1: `weekly_updates/2026-10-19-inside-the-black-box/`.

```bash
REEL=weekly_updates/2026-10-23-inside-the-black-box-part-2
SLUG=claude-sai-inside-the-black-box-part-2

# STEP 0 — evidence (system python3: numpy + safetensors + tokenizers; GPT-2 in the HF cache)
python3 $REEL/evidence/gpt2_inspect.py > $REEL/evidence/gpt2_inspect.out

# STEP 1 — the sheet is GENERATED; B02/B03/B05 numbers come from gpt2_inspect.out.
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py

# STEP 2 — GATE P (human): read PEDAGOGY.md, sign the VERDICT line.

# STEP 3 — audio (.venv: Kokoro), then re-cue
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 4 — the two figure plates, both aspects (system python3: needs Pillow)
python3 $REEL/make_plates.py --preview && python3 $REEL/make_plates.py

# STEP 5 — the six Remotion beats, one per call
for b in B00 B02 B03 B05 B06 B07; do
  python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 6 — 16:9 review cut + GATE V, then the clean master
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/$SLUG.mp4 $REEL/1023-$SLUG.mp4
mv $REEL/$SLUG.verified.json $REEL/1023-$SLUG.verified.json

# STEP 7 — the same film in 9:16
python3 runtime/scripts/shorts.py $REEL --vertical
python3 $REEL/fix_vertical.py      # B04's portrait contrast boxes — EVERY time after shorts.py
for b in B00 B02 B03 B05 B06 B07; do
  python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art final $REEL/vertical --height 3840 --out $REEL/vertical
mv $REEL/vertical/$SLUG-vertical.mp4 $REEL/1023-$SLUG-vertical.mp4
mv $REEL/vertical/$SLUG-vertical.verified.json $REEL/1023-$SLUG-vertical.verified.json

# STEP 8 — math QC: B03 at each row reveal and at 15/50/85%, BOTH aspects.
```

## GATE V: B04's contrast regions

B04 declares `qc.contrast_regions` (kicker, first caption, credit line) with a
written `contrast_reason`: the whole-frame average is dominated by Wolfram's pale
attention maps and weight "static" (0.26–0.27 < 0.30), not by text.
`shorts.py` copies the landscape boxes; `fix_vertical.py` writes portrait ones.

## Expected noise, not bugs

- SKIN LINT at B07 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).
