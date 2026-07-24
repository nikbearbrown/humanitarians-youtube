# TECHNIQUES.md — Bear Brown Logo Remotion Showcase

Review pass: mark each technique keep / kill in the checkbox column.

**File:** `claude-liam-bear-brown-logo-remotion-showcase.mp4`
**Duration:** 2:43 (163.8s, 4914 frames @ 30fps)
**Dimensions:** 1080 × 1920 (9:16 portrait)
**Voice:** Kokoro af_kore (Kore, in for Humanitarians AI)
**Logo:** `logos/bear-brown-logo-black.svg` — viewBox 0 0 7500 5000, one complex path, ink #171717

---

| # | Beat | Technique | Timestamp | Duration | Scene file | Keep / Kill |
|---|------|-----------|-----------|----------|------------|-------------|
| 0 | B00 | Cold Open — ClaudeComposerAsk | 0:00.0 | 9.9s | `BearBrownLogoRemotionShowcase.tsx` / `ClaudeComposerAsk.tsx` | — |
| 1 | B01 | Spring Entrance | 0:09.9 | 6.8s | `BearBrownLogoRemotionShowcase.tsx` `SpringEntrance` | ☐ keep  ☐ kill |
| 2 | B02 | Overshoot Spring | 0:16.7 | 7.7s | `BearBrownLogoRemotionShowcase.tsx` `OvershootSpring` | ☐ keep  ☐ kill |
| 3 | B03 | Draw-On Stroke | 0:24.4 | 7.2s | `BearBrownLogoRemotionShowcase.tsx` `DrawOnStroke` | ☐ keep  ☐ kill |
| 4 | B04 | Mask Reveal | 0:31.6 | 6.8s | `BearBrownLogoRemotionShowcase.tsx` `MaskReveal` | ☐ keep  ☐ kill |
| 5 | B05 | Scale Zoom | 0:38.4 | 7.0s | `BearBrownLogoRemotionShowcase.tsx` `ScaleZoom` | ☐ keep  ☐ kill |
| 6 | B06 | Rotation | 0:45.3 | 6.8s | `BearBrownLogoRemotionShowcase.tsx` `Rotation` | ☐ keep  ☐ kill |
| 7 | B07 | Skew And Shear | 0:52.1 | 6.6s | `BearBrownLogoRemotionShowcase.tsx` `SkewAndShear` | ☐ keep  ☐ kill |
| 8 | B08 | Opacity Through Blur | 0:58.7 | 7.6s | `BearBrownLogoRemotionShowcase.tsx` `OpacityThroughBlur` | ☐ keep  ☐ kill |
| 9 | B09 | Color Interpolation | 1:06.3 | 6.8s | `BearBrownLogoRemotionShowcase.tsx` `ColorInterpolation` | ☐ keep  ☐ kill |
| 10 | B10 | Kinetic Grid | 1:13.1 | 7.6s | `BearBrownLogoRemotionShowcase.tsx` `KineticGrid` | ☐ keep  ☐ kill |
| 11 | B11 | Glitch Slices | 1:20.7 | 8.4s | `BearBrownLogoRemotionShowcase.tsx` `GlitchSlices` | ☐ keep  ☐ kill |
| 12 | B12 | Trail Echo | 1:29.1 | 6.9s | `BearBrownLogoRemotionShowcase.tsx` `TrailEcho` | ☐ keep  ☐ kill |
| 13 | B13 | Noise Wobble | 1:36.0 | 8.0s | `BearBrownLogoRemotionShowcase.tsx` `NoiseWobble` | ☐ keep  ☐ kill |
| 14 | B14 | Elastic Physics | 1:44.0 | 7.1s | `BearBrownLogoRemotionShowcase.tsx` `ElasticPhysics` | ☐ keep  ☐ kill |
| 15 | B15 | Card Flip | 1:51.1 | 7.3s | `BearBrownLogoRemotionShowcase.tsx` `CardFlip` | ☐ keep  ☐ kill |
| 16 | B16 | Shadow Play | 1:58.4 | 7.7s | `BearBrownLogoRemotionShowcase.tsx` `ShadowPlay` | ☐ keep  ☐ kill |
| 17 | B17 | Composer Summon | 2:06.1 | 7.7s | `BearBrownLogoRemotionShowcase.tsx` `ComposerSummon` | ☐ keep  ☐ kill |
| 18 | B18 | Stroke Pulse | 2:13.8 | 6.4s | `BearBrownLogoRemotionShowcase.tsx` `StrokePulse` | ☐ keep  ☐ kill |
| 19 | B19 | Scale Breathe | 2:20.3 | 6.9s | `BearBrownLogoRemotionShowcase.tsx` `ScaleBreathe` | ☐ keep  ☐ kill |
| 20 | B20 | Exit Family | 2:27.2 | 6.3s | `BearBrownLogoRemotionShowcase.tsx` `ExitFamily` | ☐ keep  ☐ kill |
| — | B21 | Handoff — Your Turn | 2:33.5 | 8.3s | `BearBrownLogoRemotionShowcase.tsx` / `ClaudeComposerAsk.tsx` | — |
| — | B22 | Outro — ClaudeTitleOutro | 2:41.9 | 1.9s | `BearBrownLogoRemotionShowcase.tsx` / `ClaudeTitleOutro.tsx` | — |

---

## Technique notes

**B01 Spring Entrance** — Default spring (damping 24, stiffness 100). Pop-in from nothing. The Bear Brown mark is wide, so the spring weight reads differently than a compact initials mark. Look for: does the wide horizontal shape give the spring more or less apparent weight.

**B02 Overshoot Spring** — High stiffness (220), low damping (8), with sine-burst squash on landing. transformOrigin bottom-center. Look for: does the squash read as physical contact given the mark's horizontal breadth.

**B03 Draw-On Stroke** — `evolvePath()` from `@remotion/paths` traces the 8929-char path outline in terracotta (strokeWidth 12 in SVG space). Fill floods in at 50% progress. Look for: the trace time on a complex calligraphic path — pen feel or loading bar.

**B04 Mask Reveal** — Phase 1: linear wipe left-to-right (first 50% of beat). Phase 2: radial iris open (next 40%). The mark's 3:2 ratio means the wipe reads as very horizontal. Look for: which phase feels more intentional on a wide mark.

**B05 Scale Zoom** — First half: linear scale 8x → 1x (accent fill changes to SPARK on phase 2). Second half: bezier-eased 8x → 1x (ease-in-out cubic). Look for: whether the bezier landing is perceptible on a wide, complex shape.

**B06 Rotation** — Spring pivot entrance (-45° → 0°), then slow continuous 180° rotation. The wide mark rotates through portrait in ways a square mark would not. Look for: whether it reads as calm during the hold or cuts awkwardly across the portrait frame.

**B07 Skew And Shear** — Spring-driven lean to 18° skewX, hold, then release back to 0. The horizontal mark makes skew read as a strong italic lean. Look for: does the release back to vertical satisfy.

**B08 Opacity Through Blur** — Slow spring (stiffness 90, mass 1.2) with blur 18px → 0 as opacity goes 0 → 1. Look for: the focus arrival — visual event or soft start.

**B09 Color Interpolation** — Labeled "Color Treatment Beat." Ink cycles #171717 → SPARK (#D97757) → #171717. Full cycle over beat duration. Look for: whether orange reads as signal on a complex calligraphic shape, or just decorates it.

**B10 Kinetic Grid** — 3×5 tiled marks (3 cols × 5 rows), each cell 88% cell width. The wide mark in portrait-grid cells means portrait cells are much wider than tall. Staggered delay (4 frames), sin-wave ripple. Look for: whether the grid reads as texture or noise.

**B11 Glitch Slices** — 6 horizontal slices, offset ±200px (SVG space = larger than H-mark glitch) on deterministic seed. 8 glitch frames then snaps clean. Some slices flash SPARK. Look for: whether the glitch is legible on such a detailed path.

**B12 Trail Echo** — 5 ghost copies at 4-frame lag each, opacity tapering. Mark slides 200px across frame. Look for: speed blur vs clutter on a wide shape.

**B13 Noise Wobble** — Sine XY + rotation jitter, amplitude decaying 8px → 0. Look for: alive vs anxious. The mark's calligraphic detail makes wobble read differently than a geometric mark.

**B14 Elastic Physics** — Spring drop (damping 10, stiffness 180) from -250px. Squash burst at frame 12. transformOrigin bottom-center. Look for: gravity on a wide horizontal shape.

**B15 Card Flip** — rotateY spring → 0 on a white card (CARD background, 16px radius, drop shadow). Fill switches to SPARK on back face. Second slow 360° pass. Look for: depth perception on a wide card in portrait.

**B16 Shadow Play** — Shadow offset layer stretches to +60px X, +40px Y, then snaps back. Opacity peaks at 35%. Look for: shadow detachment — is it clear the shadow is a separate layer.

**B17 Composer Summon** — Claude composer UI, prompt types in ("animate the Bear Brown mark — spring entrance"), send arms (SEND color), terracotta spark burst, mark springs in from below at renderWidth 820px. Look for: whether the UI origin story is legible in the beat's 7.7 seconds.

**B18 Stroke Pulse** — Unique to this reel (not in H-logo showcase). stroke-dasharray heartbeat pattern on the logo outline. Quick double-pulse at 1.2 Hz. Faint filled shape behind, stable ink hairline outline, SPARK dashing segment cycling. Look for: whether the rhythm is visible given the path complexity.

**B19 Scale Breathe** — Unique to this reel (not in H-logo showcase). Continuous sine oscillation at 0.4 Hz, ±1.5% amplitude. Spring entry, then perpetual breathing. Look for: whether the oscillation reads as life or is imperceptible at this scale.

**B20 Exit Family** — Three exits in equal thirds: (1) shrink-spin, (2) blur-out, (3) iris close (circle radius from 550px down to 0). Progress dots at bottom. Look for: which exit is cleanest on this mark, and whether the iris close at 550px radius works for the wide format.

---

## Logo facts

- **Source:** `logos/bear-brown-logo-black.svg`
- **viewBox:** `0 0 7500 5000` (3:2 landscape ratio)
- **Path complexity:** 8929-char d-string (complex calligraphic letterform)
- **Render width in portrait:** 920px (MARK_W constant), height 613px (MARK_H = MARK_W × 5000/7500)
- **SVG filter:** none — original `.st0 { fill: none }` rect is a bounding box, skipped
- **Ink:** `#171717` (near-black, not pure black — matches original logo)

---

## Render log

- Rendered clean on first attempt after TypeScript compile check passed.
- Version mismatch warning: `@remotion/paths` at 4.0.490 vs other packages at 4.0.486 — render succeeded despite warning.
- `evolvePath()` from `@remotion/paths` used for B03 Draw-On Stroke — same as H-logo showcase.
- B18 Stroke Pulse and B19 Scale Breathe are new techniques not present in the H-logo showcase.
- Wide (3:2) mark fits portrait with 80px margin each side at 920px render width, leaving vertical space for labels at top/bottom.
