# BUILD-PROMPT — 2026-10-09-small-enough-to-stay-offline · Small Enough to Stay Offline

Paste-ready, from the toolkit root. Free end to end (Kokoro, Remotion, ffmpeg, local models).

```bash
REEL=weekly_updates/2026-10-09-small-enough-to-stay-offline

# STEP 0 — evidence first (it feeds the sheet). Needs Ollama with qwen3.5:0.8b, :4b, :9b
#          (~11 GB) and Homebrew llama.cpp. ~12 min for local_bench, ~4 for llamacpp.
#          Close other heavy apps: the CPU rows are sensitive to load.
cd $REEL/evidence
python3 local_bench.py        > local_bench.out
python3 llamacpp_constrained.py > llamacpp_constrained.out
python3 grammar_probe.py      > grammar_probe.out
python3 model_facts.py        > model_facts.out
python3 crates_check.py       > crates_check.out
python3 osworld_check.py      > osworld_check.out
cd -

# STEP 1 — the sheet is GENERATED. Edit build_beats.py, never beat_sheet.json.
#          --check re-asserts every spoken figure against the evidence files, and the
#          string budgets. A re-run with new measurements WILL fail the asserts on
#          purpose: update the narration to the new numbers, then the asserts.
python3 $REEL/build_beats.py --check && python3 $REEL/build_beats.py && python3 $REEL/fill_narration.py

# STEP 2 — GATE P (human): Sai signs PEDAGOGY.md's VERDICT line. Claude never signs.

# STEP 3 — audio (master clock), then re-cue. The re-cue ASSERTS every B02/B04
#          reveal lands inside the 15 s comp.
.venv/bin/python runtime/scripts/generate_audio_kokoro.py $REEL
python3 $REEL/build_beats.py

# STEP 4 — render at true 4K, ONE BEAT PER CALL. Don't run build_beats.py while a
#          render is in flight (remotion_scenes.py writes the sheet back).
for b in B00 B01 B02 B03 B04 B05 B06 B07 B08 B09 B10; do python3 runtime/scripts/remotion_scenes.py $REEL --only $b; done

# STEP 5 — review cut + GATE V, then the clean 16:9 master into the reel.
./art run $REEL
./art final $REEL --out $REEL
mv $REEL/claude-sai-small-enough-to-stay-offline.mp4 $REEL/1009-claude-sai-small-enough-to-stay-offline.mp4
mv $REEL/claude-sai-small-enough-to-stay-offline.verified.json $REEL/1009-claude-sai-small-enough-to-stay-offline.verified.json

# STEP 6 — the same film in 9:16, 4K portrait.
python3 runtime/scripts/shorts.py $REEL --vertical
for b in B00 B01 B02 B03 B04 B05 B06 B07 B08 B09 B10; do python3 runtime/scripts/remotion_scenes.py $REEL/vertical --only $b; done
./art run $REEL/vertical --height 3840
./art final $REEL/vertical --height 3840 --out $REEL
#   then rename to 1009-claude-sai-small-enough-to-stay-offline-vertical.mp4 (+ .verified.json)

# STEP 7 — probe: 3840,2160 and 2160,3840
ffprobe -v error -show_entries stream=width,height -of csv=p=0 $REEL/1009-*.mp4
```

## Spoken respellings (narration_text only; the screen keeps the real names)

`llama dot C P P` (llama.cpp) · `Onix Runtime` (ONNX Runtime) · `Kwen` (Qwen) ·
`one point one billion` (1.1B) · `twenty twenty-four` (2024) · "Llama three's
eight-billion model" / "an eight-billion Llama" (Llama 3 8B / Llama 3.1 8B). Checked
with Kokoro's phonemizer before generating (`kokoro_onnx.tokenizer.Tokenizer.phonemize`).

## If you change any wording

Edit `build_beats.py` → `generate_audio_kokoro.py --only B0X` → `build_beats.py`
(re-cue; watch the 14.5 s assert) → `remotion_scenes.py --force --only B0X` →
`./art run` → re-derive the vertical.

## Portrait-only edits

**One** (2026-10-09 frame review): B03 `data.question` →
`"Same memory: bigger at 4 bits, or smaller at 16?"`. The parent's 68-character question
wraps to three lines in `BinaryBranch916`'s fixed-height card and the third line sits on
the border. Re-render with `remotion_scenes.py vertical --force --only B03`. Re-apply after
every `shorts.py --vertical`.

## Expected noise, not bugs

SKIN LINT wants `ClaudeTitleOutro` (wrong for this channel); GATE V underfill on centred
cards (B10 has `qc.sparse`); the portrait slate's burn-in edge-bleed.

## Disk

The three Qwen3.5 models take ~11 GB in `~/.ollama`. `qwen3.5:0.8b` and `:4b` were pulled
for this video (4.6 GB); remove with `ollama rm qwen3.5:0.8b qwen3.5:4b` if not needed.
