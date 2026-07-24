# TECHNIQUES.md — H Logo Remotion Showcase (16:9)

Review pass: mark each technique keep / kill in the checkbox column.

**File:** `claude-liam-h-logo-remotion-showcase-16x9.mp4`
**Duration:** 2:49 (169.7s, 5089 frames @ 30fps)
**Dimensions:** 1920 × 1080 (16:9 landscape)
**Voice:** Kokoro af_kore (Kore, in for Humanitarians AI)
**Source component:** `runtime/remotion/src/HLogoRemotionShowcase169.tsx`
**Audio source:** `runtime/remotion/public/h-logo-mp3/` (reused from 9:16 build — not regenerated)
**Rendered:** 2026-07-16

---

| # | Beat | Technique | Timestamp | Duration | Scene file | Keep / Kill |
|---|------|-----------|-----------|----------|------------|-------------|
| 0 | B00 | Cold Open — ClaudeComposerAsk | 0:00.0 | 10.2s | `HLogoRemotionShowcase169.tsx` / `ClaudeComposerAsk.tsx` | — |
| 1 | B01 | Spring Entrance | 0:10.2 | 6.8s | `HLogoRemotionShowcase169.tsx` `SpringEntrance` | ☐ keep  ☐ kill |
| 2 | B02 | Overshoot Spring | 0:17.0 | 7.4s | `HLogoRemotionShowcase169.tsx` `OvershootSpring` | ☐ keep  ☐ kill |
| 3 | B03 | Draw-On Stroke | 0:24.4 | 7.9s | `HLogoRemotionShowcase169.tsx` `DrawOnStroke` | ☐ keep  ☐ kill |
| 4 | B04 | Per-Path Stagger | 0:32.2 | 7.2s | `HLogoRemotionShowcase169.tsx` `PerPathStagger` | ☐ keep  ☐ kill |
| 5 | B05 | Mask Reveal | 0:39.4 | 7.1s | `HLogoRemotionShowcase169.tsx` `MaskReveal` | ☐ keep  ☐ kill |
| 6 | B06 | Scale Zoom | 0:46.5 | 7.4s | `HLogoRemotionShowcase169.tsx` `ScaleZoom` | ☐ keep  ☐ kill |
| 7 | B07 | Rotation | 0:54.0 | 7.8s | `HLogoRemotionShowcase169.tsx` `Rotation` | ☐ keep  ☐ kill |
| 8 | B08 | Skew And Shear | 1:01.8 | 6.3s | `HLogoRemotionShowcase169.tsx` `SkewAndShear` | ☐ keep  ☐ kill |
| 9 | B09 | Opacity Through Blur | 1:08.1 | 6.5s | `HLogoRemotionShowcase169.tsx` `OpacityThroughBlur` | ☐ keep  ☐ kill |
| 10 | B10 | Color Interpolation | 1:14.6 | 9.8s | `HLogoRemotionShowcase169.tsx` `ColorInterpolation` | ☐ keep  ☐ kill |
| 11 | B11 | Kinetic Grid | 1:24.4 | 7.2s | `HLogoRemotionShowcase169.tsx` `KineticGrid` (6×3 grid, 16:9 layout) | ☐ keep  ☐ kill |
| 12 | B12 | Glitch Slices | 1:31.6 | 6.8s | `HLogoRemotionShowcase169.tsx` `GlitchSlices` | ☐ keep  ☐ kill |
| 13 | B13 | Trail Echo | 1:38.3 | 6.7s | `HLogoRemotionShowcase169.tsx` `TrailEcho` | ☐ keep  ☐ kill |
| 14 | B14 | Noise Wobble | 1:45.1 | 7.5s | `HLogoRemotionShowcase169.tsx` `NoiseWobble` | ☐ keep  ☐ kill |
| 15 | B15 | Elastic Physics | 1:52.5 | 5.9s | `HLogoRemotionShowcase169.tsx` `ElasticPhysics` | ☐ keep  ☐ kill |
| 16 | B16 | Orbit Parts | 1:58.4 | 8.9s | `HLogoRemotionShowcase169.tsx` `OrbitParts` | ☐ keep  ☐ kill |
| 17 | B17 | Card Flip | 2:07.3 | 8.7s | `HLogoRemotionShowcase169.tsx` `CardFlip` | ☐ keep  ☐ kill |
| 18 | B18 | Shadow Play | 2:16.0 | 7.7s | `HLogoRemotionShowcase169.tsx` `ShadowPlay` | ☐ keep  ☐ kill |
| 19 | B19 | Composer Summon | 2:23.7 | 8.3s | `HLogoRemotionShowcase169.tsx` `ComposerSummon` | ☐ keep  ☐ kill |
| 20 | B20 | Exit Family | 2:32.0 | 8.1s | `HLogoRemotionShowcase169.tsx` `ExitFamily` | ☐ keep  ☐ kill |
| — | B21 | Handoff — Your Turn | 2:40.1 | 7.6s | `HLogoRemotionShowcase169.tsx` / `ClaudeComposerAsk.tsx` | — |
| — | B22 | Outro — ClaudeTitleOutro | 2:47.7 | 1.9s | `HLogoRemotionShowcase169.tsx` / `ClaudeTitleOutro.tsx` | — |

---

## 16:9 layout notes

All 20 techniques render identically to the 9:16 version except:

**B11 Kinetic Grid** — Grid changed from 4×5 (portrait) to 6×3 (landscape). Uses `useVideoConfig()` to read canvas dimensions at runtime; tile size computed from the smaller of cellW/cellH so marks stay proportional on the wider canvas.

**All TechniqueBeat wrapper** — `top` for the label band shifted from `5%` to `6%`; mark stage uses `top: 18%, bottom: 18%` (same proportional centering on the shorter canvas height). Spark line at `bottom: 6%`. Font sizes bumped slightly (38→44 label, 24→28 spark line) to read at 1920px width.

**B19 Composer Summon** — Composer card horizontally bounded by `left: 20%, right: 20%` (was `8%`) to avoid over-stretching on the wider canvas. Mark arrives in the lower half of frame (`top: 48%`).

---

## Technique notes

**B01 Spring Entrance** — Default spring (damping 24, stiffness 100). Clean pop-in.

**B02 Overshoot Spring** — High stiffness (220), low damping (8), with sine-burst squash on landing.

**B03 Draw-On Stroke** — `evolvePath()` from `@remotion/paths`. Outline traces (terracotta for P1, SEND color for P2), then fill floods in.

**B04 Per-Path Stagger** — H body arrives first from the left, A-diagonal follows from the right (18-frame delay). P2 fills in terracotta.

**B05 Mask Reveal** — Phase 1: linear wipe left-to-right (first 50% of beat). Phase 2: radial iris open (next 40%).

**B06 Scale Zoom** — First half: linear scale 8x→1x. Second half: bezier-eased 8x→1x.

**B07 Rotation** — Spring pivot entrance (-45°→0°), then slow continuous 180° rotation.

**B08 Skew And Shear** — Spring-driven lean to 18° skewX, hold, then release back to 0.

**B09 Opacity Through Blur** — Slower spring (stiffness 90, mass 1.2) with blur going 18px→0 as opacity goes 0→1.

**B10 Color Interpolation** — Full cycle: #171717 → SPARK (#D97757) → #171717. Labeled as "Color Treatment Beat".

**B11 Kinetic Grid** — 6×3 tiled marks (landscape layout), each with a 3-frame stagger delay, plus sin-wave ripple offset.

**B12 Glitch Slices** — Calm entry, then 8 frames of horizontal slice offsets (deterministic from frame seed), then snaps clean.

**B13 Trail Echo** — 5 ghost copies at 4-frame lag each. Mark slides across frame.

**B14 Noise Wobble** — Sine-driven XY + rotation jitter, amplitude decaying from 8px to 0 over the beat.

**B15 Elastic Physics** — Spring drop (damping 10, stiffness 180) from -250px with frame-keyed squash burst at landing.

**B16 Orbit Parts** — P1 and P2 separate, orbit each other (P2 in terracotta), then reunite via a spring.

**B17 Card Flip** — rotateY spring to 0, then a second slow 360° pass. P2 flips to terracotta on the back face.

**B18 Shadow Play** — Independent offset/opacity shadow layer stretches ahead of the mark (+60px X, +40px Y), then snaps back.

**B19 Composer Summon** — Claude composer UI: prompt types in, send arms, terracotta spark burst fires, mark springs in from below.

**B20 Exit Family** — Three exits in equal thirds: (1) shrink-spin, (2) blur-out, (3) iris close.

---

## Render log

- First render: clean, all 5089 frames encoded, 11.3 MB output.
- No technique failures — no slate cards needed.
- TypeScript compile: clean (no errors before render).
- Verified: 1920×1080, h264+aac, 169.685s, 5089 video frames.
