# TECHNIQUES — HAI Wordmark Remotion Showcase · 16:9 Landscape

One wordmark (`HUMANITARIANS-AI-wordmark.outlined.svg`), 19 techniques, 1920×1080 landscape.
Mark keep/kill after watching the rendered cut.

| # | Beat | Technique | Layout | Start | Scene File | Keep / Kill |
|---|------|-----------|--------|-------|------------|-------------|
| — | B00 | Cold Open (ClaudeComposerAsk) | — | 0:00.00 | HaiWordmarkShowcase16x9.tsx B00 | — |
| 1 | B01 | Letter Cascade | H — Horizontal | 0:12.10 | HaiWordmarkShowcase16x9.tsx B01_LetterCascade | ☐ keep ☐ kill |
| 2 | B02 | Word Slam | H — Horizontal | 0:19.10 | HaiWordmarkShowcase16x9.tsx B02_WordSlam | ☐ keep ☐ kill |
| 3 | B03 | Draw-On Glyphs | H — Horizontal | 0:25.83 | HaiWordmarkShowcase16x9.tsx B03_DrawOnGlyphs | ☐ keep ☐ kill |
| 4 | B04 | Baseline Wave | H — Horizontal | 0:33.43 | HaiWordmarkShowcase16x9.tsx B04_BaselineWave | ☐ keep ☐ kill |
| 5 | B05 | Tracking Breathe | H — Horizontal | 0:41.37 | HaiWordmarkShowcase16x9.tsx B05_TrackingBreathe | ☐ keep ☐ kill |
| 6 | B06 | Typewriter | H — Horizontal | 0:49.57 | HaiWordmarkShowcase16x9.tsx B06_Typewriter | ☐ keep ☐ kill |
| 7 | B07 | Mask Wipe | A — Marquee | 0:57.03 | HaiWordmarkShowcase16x9.tsx B07_MaskWipe | ☐ keep ☐ kill |
| 8 | B08 | Highlight Sweep | H — Horizontal | 1:04.37 | HaiWordmarkShowcase16x9.tsx B08_HighlightSweep | ☐ keep ☐ kill |
| 9 | B09 | Ligature Spotlight | H — Horizontal | 1:10.67 | HaiWordmarkShowcase16x9.tsx B09_LigatureSpotlight | ☐ keep ☐ kill |
| 10 | B10 | Per-Letter Flip | H — Horizontal | 1:20.37 | HaiWordmarkShowcase16x9.tsx B10_PerLetterFlip | ☐ keep ☐ kill |
| 11 | B11 | Scale Focus | D — Focus Crop | 1:27.70 | HaiWordmarkShowcase16x9.tsx B11_ScaleFocus | ☐ keep ☐ kill |
| 12 | B12 | Blur Depth | H — Horizontal | 1:36.67 | HaiWordmarkShowcase16x9.tsx B12_BlurDepth | ☐ keep ☐ kill |
| 13 | B13 | Color Interpolation | H — Horizontal | 1:44.33 | HaiWordmarkShowcase16x9.tsx B13_ColorInterp | ☐ keep ☐ kill |
| 14 | B14 | Elastic Physics | H — Horizontal | 1:54.03 | HaiWordmarkShowcase16x9.tsx B14_ElasticPhysics | ☐ keep ☐ kill |
| 15 | B15 | Glitch Slices | H — Horizontal | 2:04.13 | HaiWordmarkShowcase16x9.tsx B15_GlitchSlices | ☐ keep ☐ kill |
| 16 | B16 | Kinetic Stack | K — Kinetic Stack | 2:12.57 | HaiWordmarkShowcase16x9.tsx B16_KineticStack | ☐ keep ☐ kill |
| 17 | B17 | Marquee Loop | A — Marquee | 2:22.27 | HaiWordmarkShowcase16x9.tsx B17_MarqueeLoop | ☐ keep ☐ kill |
| 18 | B18 | Assembly | H — Horizontal | 2:30.27 | HaiWordmarkShowcase16x9.tsx B18_Assembly | ☐ keep ☐ kill |
| 19 | B19 | Exit Family | H — Horizontal | 2:40.13 | HaiWordmarkShowcase16x9.tsx B19_ExitFamily | ☐ keep ☐ kill |
| — | B20 | Your Turn (handoff) | — | 2:49.37 | HaiWordmarkShowcase16x9.tsx B20 | — |
| — | B21 | Outro (ClaudeTitleOutro) | — | 2:56.57 | HaiWordmarkShowcase16x9.tsx B21 | — |

## Layout key

| Code | Description |
|------|-------------|
| H — Horizontal | Full wordmark in a single horizontal row, centered vertically — the primary landscape layout. The wordmark is 1060×133, so it fills the 1920px frame naturally at font-size ~90–110px. |
| A — Marquee | Full-size wordmark scrolling horizontally through the wider 1920px frame (three speed phases). |
| D — Focus Crop | Camera scales in from full wordmark to the AI ligature target (at ~94.5% of wordmark width) and back out. |
| K — Kinetic Stack | Two rows — HUMANITARIANS / AI+HUMANITARIANS — rippling horizontally in opposing phase. Used only for B16. |

## Layout adaptation from 9:16 portrait

The 9:16 version used four layouts: A (Marquee), B (Stacked: HUMANITARIANS over big AI), C (Rotate, unused), D (Focus Crop).

In 16:9 landscape, Layout B (Stacked) is replaced by Layout H (Horizontal) for all techniques
that previously stacked the word split. The wordmark is 1060.82×133.31 — an ultra-wide SVG
that fits in a single row at full width in 1920px, so no stacking is needed. Layout B (Stacked)
survives only as Layout K for B16 (Kinetic Stack), which explicitly shows two stacked rows
moving against each other as the technique being demonstrated.

## Notes

- B13 (Color Interpolation) is labeled as a **treatment beat**, not brand law — the terracotta
  palette sweep is intentional and temporary; the ink color returns by beat end.
- The H-mark and AI-diagonal are the custom ligature marks; B09 spotlights them specifically.
- In B02 (Word Slam), landscape layout puts HUMANITARIANS sliding from left and AI slamming
  from right, rather than top-to-bottom in the portrait version.
- In B11 (Scale Focus), the AI ligature is at ~94.5% of the wordmark width; transformOrigin
  is set to 94.5% 50% so the zoom stays on-target without translateX correction.
- B16 (Kinetic Stack) uses a second line "AI · HUMANITARIANS" so both lines have similar
  visual weight across the wide frame.
- Outlined SVG: `logos/HUMANITARIANS-AI-wordmark.outlined.svg`
- Full composition: `runtime/remotion/src/HaiWordmarkShowcase16x9.tsx`
- Timing JSON: `runtime/remotion/src/hai-wordmark-timing.json` (reused from 9:16)
- Audio: `runtime/remotion/public/hai-wordmark-mp3/` (Kokoro am_onyx, 21 beats — reused)
- Source 9:16 composition: `runtime/remotion/src/HaiWordmarkShowcase.tsx`
