# TECHNIQUES — HAI Wordmark Remotion Showcase

One wordmark (`HUMANITARIANS-AI-wordmark.outlined.svg`), 19 techniques, for review.
Mark keep/kill after watching the rendered cut.

| # | Beat | Technique | Layout | Start | Scene File | Keep / Kill |
|---|------|-----------|--------|-------|------------|-------------|
| — | B00 | Cold Open (ClaudeComposerAsk) | — | 0:00.00 | ClaudeComposerAsk | — |
| 1 | B01 | Letter Cascade | B — Stacked | 0:12.10 | HaiWordmarkShowcase.tsx B01_LetterCascade | ☐ keep ☐ kill |
| 2 | B02 | Word Slam | B — Stacked | 0:19.10 | HaiWordmarkShowcase.tsx B02_WordSlam | ☐ keep ☐ kill |
| 3 | B03 | Draw-On Glyphs | B — Stacked | 0:25.83 | HaiWordmarkShowcase.tsx B03_DrawOnGlyphs | ☐ keep ☐ kill |
| 4 | B04 | Baseline Wave | B — Stacked | 0:33.43 | HaiWordmarkShowcase.tsx B04_BaselineWave | ☐ keep ☐ kill |
| 5 | B05 | Tracking Breathe | B — Stacked | 0:41.37 | HaiWordmarkShowcase.tsx B05_TrackingBreathe | ☐ keep ☐ kill |
| 6 | B06 | Typewriter | B — Stacked | 0:49.57 | HaiWordmarkShowcase.tsx B06_Typewriter | ☐ keep ☐ kill |
| 7 | B07 | Mask Wipe | A — Marquee | 0:57.03 | HaiWordmarkShowcase.tsx B07_MaskWipe | ☐ keep ☐ kill |
| 8 | B08 | Highlight Sweep | B — Stacked | 1:04.37 | HaiWordmarkShowcase.tsx B08_HighlightSweep | ☐ keep ☐ kill |
| 9 | B09 | Ligature Spotlight | B — Stacked | 1:10.67 | HaiWordmarkShowcase.tsx B09_LigatureSpotlight | ☐ keep ☐ kill |
| 10 | B10 | Per-Letter Flip | B — Stacked | 1:20.37 | HaiWordmarkShowcase.tsx B10_PerLetterFlip | ☐ keep ☐ kill |
| 11 | B11 | Scale Focus | D — Focus Crop | 1:27.70 | HaiWordmarkShowcase.tsx B11_ScaleFocus | ☐ keep ☐ kill |
| 12 | B12 | Blur Depth | B — Stacked | 1:36.67 | HaiWordmarkShowcase.tsx B12_BlurDepth | ☐ keep ☐ kill |
| 13 | B13 | Color Interpolation | B — Stacked | 1:44.33 | HaiWordmarkShowcase.tsx B13_ColorInterp | ☐ keep ☐ kill |
| 14 | B14 | Elastic Physics | B — Stacked | 1:54.03 | HaiWordmarkShowcase.tsx B14_ElasticPhysics | ☐ keep ☐ kill |
| 15 | B15 | Glitch Slices | B — Stacked | 2:04.13 | HaiWordmarkShowcase.tsx B15_GlitchSlices | ☐ keep ☐ kill |
| 16 | B16 | Kinetic Stack | B — Stacked | 2:12.57 | HaiWordmarkShowcase.tsx B16_KineticStack | ☐ keep ☐ kill |
| 17 | B17 | Marquee Loop | A — Marquee | 2:22.27 | HaiWordmarkShowcase.tsx B17_MarqueeLoop | ☐ keep ☐ kill |
| 18 | B18 | Assembly | B — Stacked | 2:30.27 | HaiWordmarkShowcase.tsx B18_Assembly | ☐ keep ☐ kill |
| 19 | B19 | Exit Family | B — Stacked | 2:40.13 | HaiWordmarkShowcase.tsx B19_ExitFamily | ☐ keep ☐ kill |
| — | B20 | Your Turn (handoff) | — | 2:49.37 | ClaudeComposerAsk | — |
| — | B21 | Outro (ClaudeTitleOutro) | — | 2:56.57 | ClaudeTitleOutro | — |

## Layout key

| Code | Description |
|------|-------------|
| A — Marquee | Full-size wordmark scrolling horizontally through the 1080px frame |
| B — Stacked | "HUMANITARIANS" over "AI", each line sized to fill the width |
| C — Rotate Vertical | 90° spine (not used — Marquee / Stacked cover all technique demonstrations) |
| D — Focus Crop | Camera pans along word at full scale; AI ligature is the target |

## Notes

- B13 (Color Interpolation) is labeled as a **treatment beat**, not brand law — the terracotta palette
  sweep is intentional and temporary; the ink color returns by beat end.
- The H-mark and AI-diagonal are the custom ligature marks; B09 spotlights them specifically.
- Outlined SVG: `logos/HUMANITARIANS-AI-wordmark.outlined.svg` (converted from `logos/HUMANITARIANS-AI-wordmark.svg` via Inkscape 1.4.4 `--export-text-to-path`).
- Full composition: `runtime/remotion/src/HaiWordmarkShowcase.tsx`
- Timing JSON: `runtime/remotion/src/hai-wordmark-timing.json`
- Audio: `runtime/remotion/public/hai-wordmark-mp3/` (Kokoro af_kore, 21 beats)
