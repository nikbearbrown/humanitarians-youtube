# PROMPTS — sers-ml-4-5-update

This file records the prompts that appear in the reel and how AI was used to make it.

## On-screen prompts

| Beat | Where | Prompt text | Purpose |
|------|-------|-------------|---------|
| B00 | Composer, typed | `/review what changed in section 4.5?` | Frames the reel's founding question |
| B00 | Composer output | 1. Strategy matched to the bottleneck · 2. Gap claim → SMAE + SemiRaman evidence · 3. Caveat: Raman, not yet SERS | Outline answer |
| B07 | Composer, typed | `/diagnose am I short on spectra or on labels?` | Follow-up the viewer can apply to their own project |

These are displayed text; no model output is shown as if it were a live response. The B00 output lines are an author-approved outline, not generated at render time.

## Generation prompts (how the reel was made)

- **Beat sheet and Manim scenes.** Written with Claude from the author's original §4.5 draft, the revised §4.5, and the change log, under the brutalist.art beat-sheet rules. The beat structure was approved by the author before any files were written.
- **Fact-check.** Claims were checked against the sources listed in FACTCHECK.md; SemiRaman's 5% / 10% figures were checked by the author against the full paper.
- **Narration audio.** Kokoro TTS, voice `am_liam`, from each beat's `narration_text`. No voice cloning.
- **Images.** None generated. All visuals are code-rendered (Remotion components and Manim scenes).

## Suggested viewer prompt (B07, full form)

> Here's my SERS dataset: how many spectra I have, how many are labeled, and what it costs me to label one more. Tell me whether my bottleneck is spectra or labels, and whether I should start with augmentation (and what noise levels to use, based on my instrument) or with self-supervised pretraining.
