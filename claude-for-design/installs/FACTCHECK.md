# FACTCHECK — installs

All on-screen figures are either exact commands (factual) or clearly illustrative.

## Claims requiring verification

| Beat | Claim | Status |
|------|-------|--------|
| B00 | "set up once" — one-time setup framing | Editorial framing, accurate |
| B04 | npx runs pinned version from node_modules | Accurate per npx / Node docs |
| B06 | pip installs listed libs (manim, librosa, faster-whisper, Pillow, vtracer, google-api) | Accurate — from requirements.txt |
| B07 | numpy < 2 pin holds inside venv without touching system | Accurate — venv isolation |
| B08 | Terminal output (`ffmpeg ok`, `Pillow ok`, `manim ok`, `librosa ok`) | **Illustrative — sample ./setup output** |
| B11 | "30 minutes" to record a voice clone | **Estimate** — ElevenLabs recommends 30 min of clean audio |
| B13 | `./art keys` output (ElevenLabs valid, higgsfield logged in, YouTube valid) | **Illustrative — sample key-check output** |

## Verdict

- Terminal outputs (B08, B13): labeled "illustrative — sample CLI output" in the beat sheet
- "30 minutes" figure (B11): labeled an estimate per ElevenLabs documentation
- All other claims are factually accurate to the toolkit and standard tools
