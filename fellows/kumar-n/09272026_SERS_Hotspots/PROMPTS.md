# PROMPTS — sers-hot-spots

This file records the prompts that appear in the reel and how AI was used to make it.

## On-screen prompts

| Beat | Where | Prompt text | Purpose |
|------|-------|-------------|---------|
| B00 | Composer, typed | `/explain why do my SERS spectra vary spot to spot?` | Frames the reel's founding question |
| B00 | Composer output | 1. Enhancement isn't uniform · 2. It piles up in nanometre gaps · 3. A few sites dominate the signal | Outline answer |
| B07 | Composer, typed | `/check do my splits keep spots from one substrate together?` | Follow-up the viewer can apply to their own data |

These are displayed text; no model output is shown as if it were a live response. The B00 output lines are an author-approved outline, not generated at render time.

## Generation prompts (how the reel was made)

- **Topic selection.** Chosen with Claude as the first of three SERS explainers supporting the author's ML-for-SERS paper series.
- **Beat sheet and Manim scenes.** Written with Claude under the brutalist.art beat-sheet rules; the beat structure and sources were approved by the author before files were written.
- **Fact-check.** Claims checked against the sources in FACTCHECK.md before building.
- **Narration audio.** Kokoro TTS, voice `am_liam`. No voice cloning.
- **Images.** None generated. All visuals are code-rendered (Remotion components and Manim scenes).

## Suggested viewer prompt (B07, full form)

> Here's how my SERS dataset is organised: which spectra came from which substrate, sample, and measurement spot, and how I split train and test. Tell me whether spectra from the same substrate or sample appear on both sides of the split, and how to regroup them so my test accuracy reflects new samples rather than repeat spots.
