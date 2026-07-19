# Technique Log — claude-liam-musinique-logo-remotion-showcase-16x9

Scene file: `runtime/remotion/src/MusiniquLogoShowcase169.tsx`

| Beat | Technique | Start | Frames | Scene Component | Keep / Kill |
|------|-----------|-------|--------|-----------------|-------------|
| B00 | ClaudeComposerAsk cold open | 0:00 | 382 | ClaudeComposerAsk | [ ] keep [ ] kill |
| B01 | Spring Entrance | 0:12.7 | 246 | SpringEntrance | [ ] keep [ ] kill |
| B02 | Overshoot Spring | 0:21.0 | 322 | OvershootSpring | [ ] keep [ ] kill |
| B03 | Per-Path Stagger | 0:31.7 | 330 | PerPathStagger | [ ] keep [ ] kill |
| B04 | Draw-On Stroke | 0:42.7 | 318 | DrawOnStroke | [ ] keep [ ] kill |
| B05 | Mask Reveal | 0:53.3 | 293 | MaskReveal | [ ] keep [ ] kill |
| B06 | Scale Zoom | 1:03.1 | 301 | ScaleZoom | [ ] keep [ ] kill |
| B07 | Rotation | 1:13.1 | 281 | Rotation | [ ] keep [ ] kill |
| B08 | Skew And Shear | 1:22.5 | 282 | SkewAndShear | [ ] keep [ ] kill |
| B09 | Opacity Through Blur | 1:31.9 | 295 | OpacityThroughBlur | [ ] keep [ ] kill |
| B10 | Color Interpolation | 1:41.7 | 318 | ColorInterpolation | [ ] keep [ ] kill |
| B11 | Kinetic Scatter | 1:52.3 | 344 | KineticScatter | [ ] keep [ ] kill |
| B12 | Glitch Slices | 2:03.8 | 318 | GlitchSlices | [ ] keep [ ] kill |
| B13 | Trail Echo | 2:14.4 | 248 | TrailEcho | [ ] keep [ ] kill |
| B14 | Noise Wobble | 2:22.7 | 285 | NoiseWobble | [ ] keep [ ] kill |
| B15 | Elastic Physics | 2:32.2 | 297 | ElasticPhysics | [ ] keep [ ] kill |
| B16 | Path Cascade | 2:42.1 | 294 | PathCascade | [ ] keep [ ] kill |
| B17 | Card Flip | 2:51.9 | 297 | CardFlip | [ ] keep [ ] kill |
| B18 | Shadow Play | 3:01.8 | 275 | ShadowPlay | [ ] keep [ ] kill |
| B19 | Composer Summon | 3:11.0 | 308 | ComposerSummon | [ ] keep [ ] kill |
| B20 | Exit Family | 3:21.3 | 278 | ExitFamily | [ ] keep [ ] kill |
| B21 | Your Turn handoff | 3:30.6 | 253 | ClaudeComposerAsk | [ ] keep [ ] kill |
| B22 | ClaudeTitleOutro | 3:39.0 | 120 | ClaudeTitleOutro | [ ] keep [ ] kill |

**Total:** 6685 frames · 222.8 s · 3:42.8

---

## Notes

- All 20 techniques rendered; no slate fallbacks required.
- Color Interpolation (B10) is the only treatment beat — hue shift is the sole signal.
- Composer Summon (B19) reuses ClaudeComposerAsk typing animation; the prompt types itself in, then the mark arrives as the result.
- Exit Family (B20) chains three exits in one beat: shrink-spin → blur-out → mask-close.
- Glitch Slices (B12): 6 horizontal slices offset for 8 frames, then snap clean — aggressive and brief by design.
- Per-Path Stagger (B03) and Path Cascade (B16) both drive all 47 paths individually; Stagger is lateral/sequential, Cascade is vertical/waterfall.
- Kinetic Scatter (B11) drives per-path SVG-space translation outward then back; the reunion frame is the beat.
