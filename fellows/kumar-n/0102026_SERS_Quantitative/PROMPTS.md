# PROMPTS — sers-quantitative

This file records the prompts that appear in the reel and how AI was used to make it.

## On-screen prompts

| Beat | Where | Prompt text | Purpose |
|------|-------|-------------|---------|
| B00 | Composer, typed | `/explain why won't my SERS calibration curve stay straight?` | Frames the reel's founding question |
| B00 | Composer output | 1. The surface fills up: signal plateaus · 2. Hot spots make intensity swing · 3. Fix: ratio to an internal standard | Outline answer |
| B06 | Composer, typed | `/check where does my SERS calibration curve start to bend?` | Follow-up the viewer can apply to their own data |

These are displayed text; no model output is shown as if it were a live response. The B00 output lines are an author-approved outline, not generated at render time.

## Generation prompts (how the reel was made)

- **Topic selection.** Chosen with Claude as the second of three SERS explainers supporting the author's ML-for-SERS paper series.
- **Beat sheet and Manim scenes.** Written with Claude under the brutalist.art beat-sheet rules; structure and sources approved by the author before files were written.
- **Fact-check.** Claims checked against the sources in FACTCHECK.md before building.
- **Narration audio.** Kokoro TTS, voice `am_liam`. No voice cloning.
- **Images.** None generated. All visuals are code-rendered.

## Suggested viewer prompt (B06, full form)

> Here are my SERS calibration points: concentration, peak intensity, and replicate spread at each level. Tell me where the response stops being roughly linear, whether any of my unknowns fall past that point, and whether an internal standard would reduce my replicate spread.
