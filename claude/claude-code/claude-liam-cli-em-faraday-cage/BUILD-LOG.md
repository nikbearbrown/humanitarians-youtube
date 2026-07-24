# BUILD-LOG — claude-liam-cli-em-faraday-cage

## Scaffold (2026-07-15)

Picked source card: physics-electromagnetism/youtube/cli-ideas.md — Candidate 01
  "Build the Faraday Cage: How Much Shielding Does a Copper Box Provide?"
  Score: 9/10, Lane: BUILD (Claude Code), Output: Manim

Files created:
- beat_sheet.json — full 10-beat CLI spine (B00-B09)
- scenes.py — Manim: B04_SkinDepth, B06_Materials
- PEDAGOGY.md — GATE P: VERDICT: PASS
- FACTCHECK.md — verified all physics claims
- SHOTLIST.md — machine/human beat breakdown
- PROMPTS.md — beat-prefixed prompts for open slots
- description.txt — YouTube description
- BUILD-PROMPT.md, BUILD-LOG.md — this file

Key physics verified:
- δ(Cu, 64 MHz) = 8.15 μm ≈ 8.4 μm ✓
- A_dB(Cu, 1mm, 64 MHz) ≈ 1033 dB ✓
- δ(SS304, 64 MHz) ≈ 54 μm → ratio 6.6× copper ✓

## Audio (to run)
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  physics-electromagnetism/youtube/claude-liam-cli-em-faraday-cage

## Compile (to run after audio)
bash brutalist-art/runtime/scripts/run.sh \
  physics-electromagnetism/youtube/claude-liam-cli-em-faraday-cage

## Expected outputs
- physics-electromagnetism/youtube/claude-liam-cli-em-faraday-cage/claude-liam-cli-em-faraday-cage-slate.mp4
- physics-electromagnetism/youtube/claude-liam-cli-em-faraday-cage/claude-liam-cli-em-faraday-cage.mp4
  (final cut only available if all slates are filled — B01 and B07 ship as slates)
