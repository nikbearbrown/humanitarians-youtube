# TECHNIQUES — Bear Brown Initials Remotion Showcase 16:9

`claude-liam-bear-brown-initials-remotion-showcase-16x9`  
1920×1080 · 30fps · Kokoro am_onyx · Liam, in for Bear · 4:05 total

Source mark: `logos/bear-brown-initials-black.svg` — viewBox 0 0 7500 5000 (3:2),
one complex `<path>` (cls-2), one transparent `<rect>`. Filters dropped. Ink #3D3929 on cream #FAF9F5.

Scene file: `runtime/remotion/src/BearBrownInitialsShowcase169.tsx`  
Composition ID: `BearBrownInitialsShowcase169`

---

| Beat | Technique | Start (s) | Start (mm:ss) | Frames | Scene Component | Status |
|------|-----------|-----------|---------------|--------|-----------------|--------|
| B00 | ClaudeComposerAsk cold open | 0.0 | 0:00 | 329 | `ClaudeComposerAsk` | [x] keep |
| B01 | Spring Entrance | 11.0 | 0:11 | 286 | `SpringEntrance` | [ ] keep / [ ] kill |
| B02 | Overshoot Spring | 20.5 | 0:21 | 338 | `OvershootSpring` | [ ] keep / [ ] kill |
| B03 | Draw-On Stroke | 31.8 | 0:32 | 318 | `DrawOnStroke` (evolvePath) | [ ] keep / [ ] kill |
| B04 | Mask Reveal | 42.4 | 0:42 | 331 | `MaskReveal` | [ ] keep / [ ] kill |
| B05 | Scale Zoom | 53.4 | 0:53 | 381 | `ScaleZoom` | [ ] keep / [ ] kill |
| B06 | Rotation | 66.1 | 1:06 | 329 | `Rotation` | [ ] keep / [ ] kill |
| B07 | Skew And Shear | 77.1 | 1:17 | 339 | `SkewAndShear` | [ ] keep / [ ] kill |
| B08 | Opacity Through Blur | 88.4 | 1:28 | 323 | `OpacityThroughBlur` | [ ] keep / [ ] kill |
| B09 | Color Interpolation | 99.2 | 1:39 | 352 | `ColorInterpolation` | [ ] keep / [ ] kill |
| B10 | Kinetic Grid | 110.9 | 1:51 | 334 | `KineticGrid` (4×3) | [ ] keep / [ ] kill |
| B11 | Glitch Slices | 122.1 | 2:02 | 287 | `GlitchSlices` | [ ] keep / [ ] kill |
| B12 | Trail Echo | 131.7 | 2:12 | 322 | `TrailEcho` | [ ] keep / [ ] kill |
| B13 | Noise Wobble | 142.4 | 2:22 | 320 | `NoiseWobble` | [ ] keep / [ ] kill |
| B14 | Elastic Physics | 153.1 | 2:33 | 327 | `ElasticPhysics` | [ ] keep / [ ] kill |
| B15 | Card Flip | 164.0 | 2:44 | 366 | `CardFlip` (perspective rotateY) | [ ] keep / [ ] kill |
| B16 | Shadow Play | 176.2 | 2:56 | 332 | `ShadowPlay` | [ ] keep / [ ] kill |
| B17 | Composer Summon | 187.3 | 3:07 | 331 | `ComposerSummon` | [ ] keep / [ ] kill |
| B18 | Stroke Pulse | 198.3 | 3:18 | 326 | `StrokePulse` | [ ] keep / [ ] kill |
| B19 | Scale Breathe | 209.2 | 3:29 | 356 | `ScaleBreathe` | [ ] keep / [ ] kill |
| B20 | Exit Family | 221.1 | 3:41 | 305 | `ExitFamily` (3 exits) | [ ] keep / [ ] kill |
| B21 | Your Turn (handoff) | 231.3 | 3:51 | 254 | `ClaudeComposerAsk` | [x] keep |
| B22 | ClaudeTitleOutro | 239.8 | 3:60 | 165 | `ClaudeTitleOutro` | [x] keep |

---

## Notes

- **B03 Draw-On Stroke**: uses `@remotion/paths` `evolvePath()` — the correct Remotion-native path tracing API. Stroke traces first, fill floods after midpoint.
- **B09 Color Interpolation**: intentional palette violation (treatment beat). `interpolateColors` sweeps ink→terracotta→ink. Narration calls it out.
- **B10 Kinetic Grid**: 4×3 tile layout for landscape (4 cols × 3 rows). Staggered spring entrance, continuous ripple wave.
- **B12 Trail Echo**: 600px lateral travel range (wider than portrait) — horizontal canvas used deliberately.
- **B15 Card Flip**: `perspective: 1200`, `preserve-3d`, back face shows terracotta during 90–270° window.
- **B17 Composer Summon**: landscape split layout — composer card left, mark assembles right. ASK→RESULT law applied.
- **B20 Exit Family**: three sub-exits in one beat (shrink-spin, blur-out, mask-close iris), each taking one third of the beat duration.

## Output

- `mp4/claude-liam-bear-brown-initials-remotion-showcase-16x9.mp4` — 1920×1080, 30fps, 245s, 33MB
- `mp3/beat-B00.mp3` through `beat-B21.mp3` — Kokoro am_onyx narration
- `beat_sheet.json` — full beat metadata with measured audio durations
