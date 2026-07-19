# BUILD-PROMPT — Kokoro: Free Voices (With Names)

Video 6 (chapter_number 6) for the "Brutalist — Claude for Video Production" playlist.
Introduces the THIRD voice engine — Kokoro (free, local, named voices) — and THE CAST
CARRIES IT: Bear's ElevenLabs clone opens (B00 only), then eight named Kokoro voices
introduce themselves and teach the rest. beat_sheet.json is ALREADY AUTHORED (11 beats,
per-beat "voice" + "engine" fields) — do not re-author; PEDAGOGY.md carries VERDICT: PASS.

Standing rules #1–#4 (EXAMPLES-CAMPAIGN.md) apply. Read
runtime/scripts/generate_audio_kokoro.py's docstring first — it is the spec.

## Phase A — the engine (one-time setup)

1. pip install kokoro-onnx  (free, no key). Then the model files (~330MB, one-time):
   mkdir -p runtime/models/kokoro && cd runtime/models/kokoro
   curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
   curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
2. FACTCHECK the cast: python3 runtime/scripts/generate_audio_kokoro.py --list-voices
   — confirm af_bella, af_sarah, am_adam, am_michael, bf_emma, bm_george, am_puck,
   am_santa all exist, and the exact roster count. The grades in the beat sheet
   (A-/C+/F+/C+/B-/C/C+/D-) came from hexgrad/Kokoro-82M VOICES.md on 2026-07-13 —
   re-verify and correct sheet + graphics if the pack differs. Write FACTCHECK.md.

## Phase B — audio (audio-first; narration is the master clock)

3. Bear's open: python3 runtime/scripts/generate_audio.py youtube/kokoro-free-voices --only B00
   (the ONLY paid audio — record the cents in BUILD-LOG).
4. The cast: python3 runtime/scripts/generate_audio_kokoro.py youtube/kokoro-free-voices
   (skips B00 automatically via its engine field; everything else at $0.00).
   LISTEN to one beat per voice — if a voice reads a name or acronym badly, adjust the
   narration text (spoken forms), never the casting.

## Phase C — build

5. scenes.py manim beats per each graphic.production_viz (B01–B03, B05–B09: the name
   cards with grade chips are the visual signature — same card layout every time, only
   name/grade/flag varying). Remotion beats B00/B04/B99 via remotion_scenes.py
   (FOREGROUND — rule #3; props match zod — rule #4).
6. ./art run youtube/kokoro-free-voices → verify qc-sheet.png BY LOOKING (rule #2):
   11/11, every name card shows the right name + grade, B04 shows the casting field,
   no placeholders. GATE: report the review cut + which voices sounded rough; WAIT for
   human approval (he may recast a beat — one field change + re-run kokoro for that beat).
7. After approval: ./art final (master staged AFTER final — symlink convention),
   <slug>.srt from the sheet, publish unlisted to the Brutalist playlist (chapter 6,
   captions upload with the post). Description cross-links the cost-test video ("the
   paid engines' story"). Append to PUBLISH-LOG.md; findings to CAMPAIGN-FEEDBACK.md
   (first real generate_audio_kokoro.py run — anything rough is a finding).
