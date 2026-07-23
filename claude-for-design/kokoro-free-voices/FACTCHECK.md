# FACTCHECK — Kokoro: Free Voices (With Names)

Built: 2026-07-13 · kokoro-onnx 0.4.7 · model files v1.0

## Voice cast — all 8 confirmed present in voices-v1.0.bin

| Beat | Voice ID | Grade (beat sheet) | Grade (VOICES.md) | Status |
|------|----------|--------------------|-------------------|--------|
| B01 | af_bella  | A-  | A-  | ✓ MATCH |
| B02 | af_sarah  | C+  | C+  | ✓ MATCH |
| B03 | am_adam   | F+  | F+  | ✓ MATCH |
| B04 | am_michael| C+  | C+  | ✓ MATCH |
| B05 | bf_emma   | B-  | B-  | ✓ MATCH |
| B06 | bm_george | C   | C   | ✓ MATCH |
| B07 | am_puck   | C+  | C+  | ✓ MATCH |
| B08 | am_santa  | D-  | D-  | ✓ MATCH |
| B09 | af_bella  | —   | A-  | returning voice, no card |
| B99 | bf_emma   | —   | B-  | outro, no card |

Grade source: hexgrad/Kokoro-82M VOICES.md, re-verified 2026-07-13.
No corrections needed — every grade in the beat sheet matches the pack.

## Roster count

`--list-voices` returns 54 total voices. English subset (af_/am_/bf_/bm_):
- af_* (American female): 11
- am_* (American male): 9
- bf_* (British female): 4
- bm_* (British male): 4
- **English total: 28**

Emma's narration "about twenty-eight of us, American and British" — **CONFIRMED ACCURATE**.
Non-English voices (ef_, em_, ff_, hf_, hm_, if_, im_, jf_, jm_, pf_, pm_, zf_, zm_): 26 voices.

## Model files

- kokoro-v1.0.onnx: 310 MB ✓
- voices-v1.0.bin: 27 MB ✓
- Location: runtime/models/kokoro/

## B00 engine

B00 uses ElevenLabs (engine: "elevenlabs") — Bear's clone. B01–B99 use Kokoro (engine: "kokoro").
generate_audio_kokoro.py skips engine≠"kokoro" beats automatically.

VERDICT: PASS — no corrections to beat sheet or graphics needed.
