# TECHNIQUES.md — H Logo Remotion Showcase

Review pass: mark each technique keep / kill in the checkbox column.

**File:** `claude-liam-h-logo-remotion-showcase.mp4`
**Duration:** 2:49 (169.7s, 5089 frames @ 30fps)
**Dimensions:** 1080 × 1920 (9:16 portrait)
**Voice:** Kokoro am_onyx (Liam, in for Bear)

---

| # | Beat | Technique | Timestamp | Duration | Scene file | Keep / Kill |
|---|------|-----------|-----------|----------|------------|-------------|
| 0 | B00 | Cold Open — ClaudeComposerAsk | 0:00.0 | 10.2s | `HLogoRemotionShowcase.tsx` / `ClaudeComposerAsk.tsx` | — |
| 1 | B01 | Spring Entrance | 0:10.2 | 6.8s | `HLogoRemotionShowcase.tsx` `SpringEntrance` | ☐ keep  ☐ kill |
| 2 | B02 | Overshoot Spring | 0:17.0 | 7.4s | `HLogoRemotionShowcase.tsx` `OvershootSpring` | ☐ keep  ☐ kill |
| 3 | B03 | Draw-On Stroke | 0:24.4 | 7.9s | `HLogoRemotionShowcase.tsx` `DrawOnStroke` | ☐ keep  ☐ kill |
| 4 | B04 | Per-Path Stagger | 0:32.2 | 7.2s | `HLogoRemotionShowcase.tsx` `PerPathStagger` | ☐ keep  ☐ kill |
| 5 | B05 | Mask Reveal | 0:39.4 | 7.1s | `HLogoRemotionShowcase.tsx` `MaskReveal` | ☐ keep  ☐ kill |
| 6 | B06 | Scale Zoom | 0:46.5 | 7.4s | `HLogoRemotionShowcase.tsx` `ScaleZoom` | ☐ keep  ☐ kill |
| 7 | B07 | Rotation | 0:54.0 | 7.8s | `HLogoRemotionShowcase.tsx` `Rotation` | ☐ keep  ☐ kill |
| 8 | B08 | Skew And Shear | 1:01.8 | 6.3s | `HLogoRemotionShowcase.tsx` `SkewAndShear` | ☐ keep  ☐ kill |
| 9 | B09 | Opacity Through Blur | 1:08.1 | 6.5s | `HLogoRemotionShowcase.tsx` `OpacityThroughBlur` | ☐ keep  ☐ kill |
| 10 | B10 | Color Interpolation | 1:14.6 | 9.8s | `HLogoRemotionShowcase.tsx` `ColorInterpolation` | ☐ keep  ☐ kill |
| 11 | B11 | Kinetic Grid | 1:24.4 | 7.2s | `HLogoRemotionShowcase.tsx` `KineticGrid` | ☐ keep  ☐ kill |
| 12 | B12 | Glitch Slices | 1:31.6 | 6.8s | `HLogoRemotionShowcase.tsx` `GlitchSlices` | ☐ keep  ☐ kill |
| 13 | B13 | Trail Echo | 1:38.3 | 6.7s | `HLogoRemotionShowcase.tsx` `TrailEcho` | ☐ keep  ☐ kill |
| 14 | B14 | Noise Wobble | 1:45.1 | 7.5s | `HLogoRemotionShowcase.tsx` `NoiseWobble` | ☐ keep  ☐ kill |
| 15 | B15 | Elastic Physics | 1:52.5 | 5.9s | `HLogoRemotionShowcase.tsx` `ElasticPhysics` | ☐ keep  ☐ kill |
| 16 | B16 | Orbit Parts | 1:58.4 | 8.9s | `HLogoRemotionShowcase.tsx` `OrbitParts` | ☐ keep  ☐ kill |
| 17 | B17 | Card Flip | 2:07.3 | 8.7s | `HLogoRemotionShowcase.tsx` `CardFlip` | ☐ keep  ☐ kill |
| 18 | B18 | Shadow Play | 2:16.0 | 7.7s | `HLogoRemotionShowcase.tsx` `ShadowPlay` | ☐ keep  ☐ kill |
| 19 | B19 | Composer Summon | 2:23.7 | 8.3s | `HLogoRemotionShowcase.tsx` `ComposerSummon` | ☐ keep  ☐ kill |
| 20 | B20 | Exit Family | 2:32.0 | 8.1s | `HLogoRemotionShowcase.tsx` `ExitFamily` | ☐ keep  ☐ kill |
| — | B21 | Handoff — Your Turn | 2:40.1 | 7.6s | `HLogoRemotionShowcase.tsx` / `ClaudeComposerAsk.tsx` | — |
| — | B22 | Outro — ClaudeTitleOutro | 2:47.7 | 1.9s | `HLogoRemotionShowcase.tsx` / `ClaudeTitleOutro.tsx` | — |

---

## Technique notes

**B01 Spring Entrance** — Default spring (damping 24, stiffness 100). Clean pop-in. Look for: does it feel weighted or cheap.

**B02 Overshoot Spring** — High stiffness (220), low damping (8), with sine-burst squash on landing. Look for: does the squash read as physical contact.

**B03 Draw-On Stroke** — `evolvePath()` from `@remotion/paths`. Outline traces (terracotta for P1, SEND color for P2 on a 4-frame delay), then fill floods in. Look for: pen feel vs progress-bar feel.

**B04 Per-Path Stagger** — H body arrives first from the left, A-diagonal follows from the right in a Sequence offset of 18 frames. P2 fills in terracotta (the accent beat for this technique).

**B05 Mask Reveal** — Phase 1: linear wipe left-to-right (first 50% of beat). Phase 2: radial iris open (next 40%). Look for: which phase feels more intentional.

**B06 Scale Zoom** — First half: linear scale 8x → 1x. Second half: bezier-eased 8x → 1x (ease-in-out cubic). Look for: whether the bezier landing is noticeably better.

**B07 Rotation** — Spring pivot entrance (-45° → 0°), then slow continuous 180° rotation. Look for: whether the continuous hold reads as calm or aimless.

**B08 Skew And Shear** — Spring-driven lean to 18° skewX, hold, then release back to 0. Look for: italic tension vs just wobbling.

**B09 Opacity Through Blur** — Slower spring (stiffness 90, mass 1.2) with blur going 18px → 0 as opacity goes 0 → 1. Look for: the focus arrival — is it a visual event or just a soft start.

**B10 Color Interpolation** — Full cycle: #171717 → SPARK (#D97757) → #171717. Peak orange at midpoint. Labeled as "Color Treatment Beat" (not brand law). Look for: whether the orange reads as signal or just decoration.

**B11 Kinetic Grid** — 4×5 tiled marks, each with a 3-frame stagger delay, plus a sin-wave ripple offset. Look for: whether the grid becomes texture or just noise.

**B12 Glitch Slices** — Calm entry, then 8 frames of horizontal slice offsets (deterministic from frame seed), then snaps clean. The P2 occasionally flashes terracotta during glitch. Look for: whether the snap-clean landing saves it.

**B13 Trail Echo** — 5 ghost copies at 4-frame lag each, opacity decreasing from 25% to ~5%. Mark slides across frame. Look for: whether the trail reads as speed blur or clutter.

**B14 Noise Wobble** — Sine-driven XY + rotation jitter, amplitude decaying from 8px to 0 over the beat. Look for: alive vs anxious.

**B15 Elastic Physics** — Spring drop (damping 10, stiffness 180) from -250px with frame-keyed squash burst at landing. Look for: whether the drop reads as gravity.

**B16 Orbit Parts** — P1 and P2 separate, orbit each other (P2 in terracotta), then reunite via a spring. Look for: whether the reunion has weight, and whether the orbit arc is legible.

**B17 Card Flip** — rotateY spring to 0, then a second slow 360° pass. P2 flips to terracotta on the back face. Look for: depth perception vs flat squash.

**B18 Shadow Play** — An independent offset/opacity shadow layer stretches ahead of the mark (up to +60px X, +40px Y), then snaps back. Look for: whether the shadow detachment reads as intended.

**B19 Composer Summon** — The Claude composer UI is the subject: prompt types in, send arms, terracotta spark burst fires, mark springs in from below. Look for: whether the UI origin story is legible in 8 seconds.

**B20 Exit Family** — Three exits in equal thirds: (1) shrink-spin, (2) blur-out, (3) iris close. Progress dots mark which exit is running. Look for: which exit is cleanest and whether the trio sequence works as a comparison.

---

## Render log

- Rendered clean on first attempt after fixing: non-monotonic `inputRange` in `OvershootSpring` and `ElasticPhysics` (spring values can exceed 1.0 — replaced with frame-keyed squash burst).
- No SVG filter dependency (original `soft-edge` filter removed; shadow in B18 re-implemented as offset/opacity layer).
- `@remotion/paths` installed for B03 `evolvePath()`.
