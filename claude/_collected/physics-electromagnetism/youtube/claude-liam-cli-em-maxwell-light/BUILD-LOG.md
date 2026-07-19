# BUILD-LOG — claude-liam-cli-em-maxwell-light

## Scaffold (2026-07-15)

Picked source card: physics-electromagnetism/youtube/cli-ideas.md — Candidate 05
  "Maxwell's Equations Consistency Checker: Light Falls Out"
  Score: 10/10, Lane: BUILD (Claude Code), Output: Manim

Files created:
- beat_sheet.json — full 10-beat CLI spine (B00-B09)
- scenes.py — Manim: B04_WavePacket, B06_Superposition
- PEDAGOGY.md — GATE P: VERDICT: PASS
- FACTCHECK.md — verified all physics claims
- SHOTLIST.md — machine/human beat breakdown
- PROMPTS.md — beat-prefixed prompts for open slots
- description.txt — YouTube description
- BUILD-PROMPT.md, BUILD-LOG.md — this file

Key physics verified:
- c_derived = 1/√(μ₀ε₀) = 2.997924e+08 m/s ✓
- scipy.constants.c = 2.99792458e+08 m/s ✓
- Fractional error ≈ 4e-07 ✓
- Courant = 0.5 → leapfrog stable ✓
- Superposition: linear wave eq → pulses unchanged ✓

SPARK-LINE LAW compliant:
- B02 ASK: greeting="The ask," ✓
- B05 CHANGE: greeting="The change," ✓
- B08 HANDOFF: greeting="Your turn." ✓
- B00 COLD OPEN: greeting="Bonjour, Liam" ✓

Human-needed beats (slates):
- B01 PROBLEM — graphic: Ampère→wave→c chain
- B07 SUMMARY — graphic: formula + Maxwell quote + "One fix. One formula. One unification."

## Audio (to run)
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  physics-electromagnetism/youtube/claude-liam-cli-em-maxwell-light

## Compile (to run after audio)
ART_QC=0 bash brutalist-art/runtime/scripts/run.sh \
  physics-electromagnetism/youtube/claude-liam-cli-em-maxwell-light

python3 brutalist-art/runtime/scripts/compile.py \
  physics-electromagnetism/youtube/claude-liam-cli-em-maxwell-light --allow-slates

## Expected outputs
- physics-electromagnetism/youtube/claude-liam-cli-em-maxwell-light/claude-liam-cli-em-maxwell-light-slate.mp4
- physics-electromagnetism/youtube/claude-liam-cli-em-maxwell-light/claude-liam-cli-em-maxwell-light.mp4
  (final cut only available with --allow-slates since B01 and B07 ship as slates)
