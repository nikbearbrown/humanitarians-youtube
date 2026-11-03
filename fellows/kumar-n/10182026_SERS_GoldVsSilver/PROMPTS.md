# PROMPTS — sers-gold-vs-silver

This file records the prompts that appear in the reel and how AI was used to make it.

## On-screen prompts

| Beat | Where | Prompt text | Purpose |
|------|-------|-------------|---------|
| B00 | Composer, typed | `/explain should I use gold or silver for my SERS substrate?` | Frames the reel's founding question |
| B00 | Composer output | 1. Match the metal to the laser · 2. Silver + 532 nm, gold + 785 nm · 3. Test on your real substrate | Outline answer |
| B07 | Composer, typed | `/check does my laser match my substrate?` | Follow-up the viewer can apply to their own setup |

These are displayed text; no model output is shown as if it were a live response. The B00 output lines are an author-approved outline, not generated at render time.

## Generation prompts (how the reel was made)

- **Topic selection.** Chosen with Claude as the third of three SERS explainers supporting the author's ML-for-SERS paper series.
- **Beat sheet and Manim scenes.** Written with Claude under the brutalist.art beat-sheet rules; structure and sources approved by the author before files were written.
- **Fact-check.** Claims checked against the sources in FACTCHECK.md before building.
- **Narration audio.** Kokoro TTS, voice `am_liam`. No voice cloning.
- **Images.** None generated. All visuals are code-rendered.

## Suggested viewer prompt (B07, full form)

> My Raman system uses a [wavelength] laser, and my SERS substrate is [metal, particle type, aggregated or not]. Was this substrate characterised at my wavelength? If not, what's the simplest experiment to check whether a different laser line or metal would give me a better signal?
