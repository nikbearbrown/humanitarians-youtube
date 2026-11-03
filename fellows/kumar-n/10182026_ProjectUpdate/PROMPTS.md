# PROMPTS — sers-ml-4-6-update

This file records the prompts that appear in the reel and how AI was used to make it.

## On-screen prompts

| Beat | Where | Prompt text | Purpose |
|------|-------|-------------|---------|
| B00 | Composer, typed | `/review what changed in section 4.6?` | Frames the reel's founding question |
| B00 | Composer output | 1. Compute → reframed as a recommendation · 2. Interpretability → updated with new methods · 3. Generalization → qualified, not closed | Outline answer |
| B06 | Composer, typed | `/check would my model survive a new instrument?` | Follow-up the viewer can apply to their own model |

These are displayed text; no model output is shown as if it were a live response. The B00 output lines are an author-approved outline, not generated at render time.

## Generation prompts (how the reel was made)

- **Beat sheet and Manim scenes.** Written with Claude from the author's original §4.6 draft, the revised §4.6, and the change log, under the brutalist.art beat-sheet rules. The beat structure was approved by the author before any files were written.
- **Fact-check.** Claims were checked against the sources in FACTCHECK.md. The check surfaced one new SERS study (Mahmud et al.) that changed the generalization framing; the author approved the change.
- **Narration audio.** Kokoro TTS, voice `am_liam`, from each beat's `narration_text`. No voice cloning.
- **Images.** None generated. All visuals are code-rendered (Remotion components and Manim scenes).

## Suggested viewer prompt (B06, full form)

> Here's how I validated my SERS model: which instruments, sites, and substrate batches were in training and which were in testing. Tell me which kinds of deployment shift my evaluation actually covers, which it doesn't, and the smallest experiment that would test the biggest gap.
