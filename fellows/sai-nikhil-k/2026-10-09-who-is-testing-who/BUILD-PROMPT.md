# BUILD-PROMPT — 2026-10-09-who-is-testing-who · Who Is Testing Who?

Paste-ready, from the toolkit root. Free end to end (Kokoro, Remotion, ffmpeg, pytest).

```bash
REEL=weekly_updates/2026-10-09-who-is-testing-who

# STEP 0 — evidence first (it feeds the sheet). A venv with pytest, coverage, mutmut 3.
python3 -m venv /tmp/wtw && /tmp/wtw/bin/pip install pytest coverage mutmut
cd $REEL/evidence/bookservice
/tmp/wtw/bin/python -m pytest -q tests_mock tests_db tests_pricing   # 29 passed
/tmp/wtw/bin/python experiment.py   > experiment.out
/tmp/wtw/bin/python mutation_run.py > mutation_run.out              # ~1 min
cd -

# STEP 1 — the sheet is GENERATED. Edit build_beats.py, never beat_sheet.json.
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 2 — GATE P (human): Sai signs PEDAGOGY.md's VERDICT line. Claude never signs.

# STEP 3 — audio (master clock), then re-cue (asserts B04/B05 reveals ≤ 14.5 s).
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py

# STEP 4 — render at true 4K, ONE BEAT PER CALL.
for b in B00 B01 B02 B03 B04 B05 B06 B07 B08 B09; do python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 5 — review cut + GATE V, then the clean 16:9 master into the reel.
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/claude-sai-who-is-testing-who.mp4 $REEL/1009-claude-sai-who-is-testing-who.mp4
mv $REEL/claude-sai-who-is-testing-who.verified.json $REEL/1009-claude-sai-who-is-testing-who.verified.json

# STEP 6 — the same film in 9:16, 4K portrait.
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B01 B02 B03 B04 B05 B06 B07 B08 B09; do python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art run $REEL/vertical --height 3840
./art final $REEL/vertical --height 3840 --out $REEL
#   then rename to 1009-claude-sai-who-is-testing-who-vertical.mp4 (+ .verified.json)

# STEP 7 — probe: 3840,2160 and 2160,3840
ffprobe -v error -show_entries stream=width,height -of csv=p=0 $REEL/1009-*.mp4
```

## Spoken respelling

`Gair-gay` (Gherghe) in narration_text only; the screen keeps the real name.

## If you change any wording

Edit `build_beats.py` → `generate_audio_kokoro.py --only B0X` → `build_beats.py` →
`remotion_scenes.py --force --only B0X` → `./art run` → re-derive the vertical.

## Portrait-only edits

**One** (2026-10-09, applied before the portrait render): B03 `data.question` →
`"Same behaviour, new code: which suite passes?"`. The parent's 65-character question
would wrap to three lines in `BinaryBranch916`'s fixed-height card (seen on the week's
other reel). Re-apply after every `shorts.py --vertical`.

## Expected noise, not bugs

SKIN LINT wants `ClaudeTitleOutro`; GATE V underfill on centred cards (B09 has
`qc.sparse`); the portrait slate's burn-in edge-bleed.
