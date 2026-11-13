# PROMPTS — sers-ml-4-4-update

This file records the prompts that appear in the reel and how AI was used to make it.

## On-screen prompts

| Beat | Where | Prompt text | Purpose |
|------|-------|-------------|---------|
| B00 | Composer, typed | `/review what changed in section 4.4?` | Frames the reel's founding question |
| B00 | Composer output | 1. Uncited claim → controlled counterpoint · 2. Missing mechanism → explained · 3. Citation [U-55] → corrected | Outline answer |
| B07 | Composer, typed | `/audit was my data split by sample or by spectrum?` | Follow-up the viewer can run on their own results |

These are displayed text; no model output is shown as if it were a live response. The B00 "output" lines are an author-written outline, not generated at render time.

## Generation prompts (how the reel was made)

- **Beat sheet and Manim scenes.** Written with Claude from the author's original §4.4 draft, the revised §4.4, and the change log, under the brutalist.art beat-sheet rules (cold open → BLUF → body → verdict → handoff → outro). The beat structure was approved by the author before any files were written.
- **Fact-check.** Claims were checked against the primary sources listed in FACTCHECK.md. Three on-screen claims were corrected as a result (see FACTCHECK.md, "Corrections made during checking").
- **Narration audio.** Kokoro TTS, voice `am_liam`, from each beat's `narration_text`. No voice cloning.
- **Images.** None generated. All visuals are code-rendered (Remotion components and Manim scenes).

## Suggested viewer prompt (B07, full form)

> I have a SERS classifier with high reported accuracy. Check my evaluation: were the train and test sets split by sample or patient, or by individual spectrum? Were PCA, scaling, or feature selection fit on training folds only? Tell me which leaks you find and what the accuracy likely means.
