# TECHNIQUES.md — claude-liam-musinique-logo-remotion-showcase

One logo (Musinique, 47 paths, viewBox 0 0 1698.01 1832.98), every motion
technique Remotion can perform — 9:16 portrait, 1080×1920, 30fps.
Narrated by Liam (am_onyx, Kokoro), in for Bear. @NikBearBrown.

**Review format:** for each beat, mark Keep or Kill based on whether the
technique serves the brand. Two-column checkout at the bottom.

---

## Beat → Timestamp Table

| Beat | Technique | Start | Duration | Scene file | Keep/Kill |
|------|-----------|-------|----------|------------|-----------|
| B00 | ClaudeComposerAsk cold open | 0:00.00 | 12.7s (382f) | `ClaudeComposerAsk (built-in)` | [ ] Keep / [ ] Kill |
| B01 | Spring Entrance | 0:12.73 | 8.2s (246f) | `MusiniquLogoRemotionShowcase.tsx / B01_SpringEntrance` | [ ] Keep / [ ] Kill |
| B02 | Overshoot Spring | 0:20.93 | 10.7s (322f) | `MusiniquLogoRemotionShowcase.tsx / B02_OvershootSpring` | [ ] Keep / [ ] Kill |
| B03 | Per-Path Stagger | 0:31.67 | 11.0s (330f) | `MusiniquLogoRemotionShowcase.tsx / B03_PerPathStagger` | [ ] Keep / [ ] Kill |
| B04 | Draw-On Stroke | 0:42.67 | 10.6s (318f) | `MusiniquLogoRemotionShowcase.tsx / B04_DrawOnStroke` | [ ] Keep / [ ] Kill |
| B05 | Mask Reveal | 0:53.27 | 9.8s (293f) | `MusiniquLogoRemotionShowcase.tsx / B05_MaskReveal` | [ ] Keep / [ ] Kill |
| B06 | Scale Zoom | 1:03.03 | 10.0s (301f) | `MusiniquLogoRemotionShowcase.tsx / B06_ScaleZoom` | [ ] Keep / [ ] Kill |
| B07 | Rotation | 1:13.07 | 9.4s (281f) | `MusiniquLogoRemotionShowcase.tsx / B07_Rotation` | [ ] Keep / [ ] Kill |
| B08 | Skew And Shear | 1:22.43 | 9.4s (282f) | `MusiniquLogoRemotionShowcase.tsx / B08_SkewAndShear` | [ ] Keep / [ ] Kill |
| B09 | Opacity Through Blur | 1:31.83 | 9.8s (295f) | `MusiniquLogoRemotionShowcase.tsx / B09_OpacityBlur` | [ ] Keep / [ ] Kill |
| B10 | Color Interpolation | 1:41.67 | 10.6s (318f) | `MusiniquLogoRemotionShowcase.tsx / B10_ColorInterp` | [ ] Keep / [ ] Kill |
| B11 | Kinetic Scatter | 1:52.27 | 11.5s (344f) | `MusiniquLogoRemotionShowcase.tsx / B11_KineticScatter` | [ ] Keep / [ ] Kill |
| B12 | Glitch Slices | 2:03.73 | 10.6s (318f) | `MusiniquLogoRemotionShowcase.tsx / B12_GlitchSlices` | [ ] Keep / [ ] Kill |
| B13 | Trail Echo | 2:14.33 | 8.3s (248f) | `MusiniquLogoRemotionShowcase.tsx / B13_TrailEcho` | [ ] Keep / [ ] Kill |
| B14 | Noise Wobble | 2:22.60 | 9.5s (285f) | `MusiniquLogoRemotionShowcase.tsx / B14_NoiseWobble` | [ ] Keep / [ ] Kill |
| B15 | Elastic Physics | 2:32.10 | 9.9s (297f) | `MusiniquLogoRemotionShowcase.tsx / B15_ElasticPhysics` | [ ] Keep / [ ] Kill |
| B16 | Path Cascade | 2:42.00 | 9.8s (294f) | `MusiniquLogoRemotionShowcase.tsx / B16_PathCascade` | [ ] Keep / [ ] Kill |
| B17 | Card Flip | 2:51.80 | 9.9s (297f) | `MusiniquLogoRemotionShowcase.tsx / B17_CardFlip` | [ ] Keep / [ ] Kill |
| B18 | Shadow Play | 3:01.70 | 9.2s (275f) | `MusiniquLogoRemotionShowcase.tsx / B18_ShadowPlay` | [ ] Keep / [ ] Kill |
| B19 | Composer Summon | 3:10.87 | 10.3s (308f) | `MusiniquLogoRemotionShowcase.tsx / B19_ComposerSummon` | [ ] Keep / [ ] Kill |
| B20 | Exit Family | 3:21.13 | 9.3s (278f) | `MusiniquLogoRemotionShowcase.tsx / B20_ExitFamily` | [ ] Keep / [ ] Kill |
| B21 | Your Turn (handoff) | 3:30.40 | 8.4s (253f) | `ClaudeComposerAsk (built-in)` | [ ] Keep / [ ] Kill |
| B22 | ClaudeTitleOutro | 3:38.83 | 4.0s (120f) | `ClaudeTitleOutro (built-in)` | [ ] Keep / [ ] Kill |

**Total runtime:** 3:42.83 (6685 frames)

---

## Technique Notes

**B00 — Cold Open** `ClaudeComposerAsk`
  Liam introduces: one logo, 47 paths, every Remotion move.

**B01 — Spring Entrance** `spring({ damping: 22, stiffness: 180, mass: 0.9 })`
  Default spring. Mark enters as one unit. Nothing special — that's the point.

**B02 — Overshoot Spring** `spring({ damping: 4, stiffness: 400, mass: 1.5 })`
  Low damping + high stiffness = bounce. Squash/stretch at peak. Energy read.

**B03 — Per-Path Stagger** `4-frame offset × 47 paths`
  47 paths enter in sequence. The cascade is richer than any wordmark can deliver.

**B04 — Draw-On Stroke** `strokeDashoffset → fillProgress`
  SPARK terracotta outline traces, then ink fill floods. Corner fidelity note: complex paths.

**B05 — Mask Reveal** `clipPath: inset → inset round (iris)`
  Left-to-right wipe first half, iris close second half.

**B06 — Scale Zoom** `interpolate(8→1)` linear, then `spring` bezier
  Two easing comparisons in one beat — which one reads as a camera move?

**B07 — Rotation** `rotateZ(-180→0)` entrance, `rotateZ(slow hold)`
  Near-square mark: rotation lands differently than on a wide wordmark.

**B08 — Skew And Shear** `skewX(-18deg)` lean then release
  Lean-in, hold, release. Italic read vs. distortion threshold.

**B09 — Opacity Through Blur** `blur(24→0)` + `opacity(0→1)`
  Materialise from soft focus. If you're looking for the blur it's working.

**B10 — Color Interpolation** *(treatment beat — palette violation labeled)*
  Per-path color sweeps ink→terracotta→ink. The exception that proves the accent law.

**B11 — Kinetic Scatter** `translate(outward) → spring(back)`
  47 paths explode from center, spring home. 47 vectors = richer than text scatter.

**B12 — Glitch Slices** `6 slices × translateX offsets → snap`
  Horizontal slices offset ~8 frames then snap clean. Correction vs. decoration.

**B13 — Trail Echo** `5 ghost copies × lag offset`
  Low-opacity copies trail the fast slide across frame, mark settles center.

**B14 — Noise Wobble** `sin(frame + path_phase) × wobbleAmt → settles`
  Per-path sine jitter, amplitude decays to zero. Alive vs. broken read.

**B15 — Elastic Physics** `spring({ damping: 5, stiffness: 180, mass: 1.2 })`
  Drop → squash (scaleY) → rebound. Config is the whole design decision.

**B16 — Path Cascade** `47 paths rain from translateY(-800) staggered`
  Waterfall entry, paths in order. With 47 elements the texture is distinctive.

**B17 — Card Flip** `rotateY(0→180)` in perspective, front/back faces
  INK front, SPARK back. The hold after flip earns or wastes its frame time.

**B18 — Shadow Play** `shadow offset grows → spring back to zero`
  Offset-layer shadow animates independently then rejoins. Brand depth move.

**B19 — Composer Summon** `SPARK flash at send → mark materialises`
  Terracotta burst on the send action, logo springs in from nothing.

**B20 — Exit Family** Three exits: shrink-spin, blur-out, mask-close
  Three ways to leave. Only one works to cut to black on.

**B21 — Your Turn** `ClaudeComposerAsk` handoff prompt
  Suggest: Per-Path Stagger, Kinetic Scatter, Draw-On, Elastic, Mask Reveal.

**B22 — Outro** `ClaudeTitleOutro`
  'One Logo, 47 Paths, Every Move Remotion Knows.' · @NikBearBrown · Liam, in for Bear.

---

## Review Checklist

- [ ] B01 Spring Entrance — Keep / Kill
- [ ] B02 Overshoot Spring — Keep / Kill
- [ ] B03 Per-Path Stagger — Keep / Kill
- [ ] B04 Draw-On Stroke — Keep / Kill
- [ ] B05 Mask Reveal — Keep / Kill
- [ ] B06 Scale Zoom — Keep / Kill
- [ ] B07 Rotation — Keep / Kill
- [ ] B08 Skew And Shear — Keep / Kill
- [ ] B09 Opacity Through Blur — Keep / Kill
- [ ] B10 Color Interpolation (treatment) — Keep / Kill
- [ ] B11 Kinetic Scatter — Keep / Kill
- [ ] B12 Glitch Slices — Keep / Kill
- [ ] B13 Trail Echo — Keep / Kill
- [ ] B14 Noise Wobble — Keep / Kill
- [ ] B15 Elastic Physics — Keep / Kill
- [ ] B16 Path Cascade — Keep / Kill
- [ ] B17 Card Flip — Keep / Kill
- [ ] B18 Shadow Play — Keep / Kill
- [ ] B19 Composer Summon — Keep / Kill
- [ ] B20 Exit Family — Keep / Kill