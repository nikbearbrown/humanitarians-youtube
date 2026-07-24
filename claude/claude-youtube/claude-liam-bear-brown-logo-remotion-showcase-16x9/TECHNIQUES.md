# TECHNIQUES.md — Bear Brown Logo, Every Remotion Move (16:9)

**Slug:** claude-liam-bear-brown-logo-remotion-showcase-16x9
**Format:** 1920×1080, 30 fps, 5879 frames, ~3:16
**Channel:** claude-liam · @HumanitariansAI · Kokoro af_kore
**Subject:** Bear Brown full logo mark (viewBox 0 0 7500 5000, single complex path)
**Rendered:** 2026-07-16
**Output:** mp4/claude-liam-bear-brown-logo-remotion-showcase-16x9.mp4 (29 MB)

## Beat → Timestamp Table

| Beat | Technique | Timestamp | Scene Component | Frames | Duration | Keep/Kill |
|------|-----------|-----------|-----------------|--------|----------|-----------|
| B00 | ClaudeComposerAsk cold open | 00:00 | ClaudeComposerAsk | 328 | 10.9s | KEEP |
| B01 | Spring Entrance | 00:10 | SpringEntrance | 200 | 6.7s | [ ] keep [ ] kill |
| B02 | Overshoot Spring | 00:17 | OvershootSpring | 253 | 8.4s | [ ] keep [ ] kill |
| B03 | Draw-On Stroke | 00:26 | DrawOnStroke | 255 | 8.5s | [ ] keep [ ] kill |
| B04 | Mask Reveal | 00:34 | MaskReveal | 225 | 7.5s | [ ] keep [ ] kill |
| B05 | Scale Zoom | 00:42 | ScaleZoom | 273 | 9.1s | [ ] keep [ ] kill |
| B06 | Rotation | 00:51 | Rotation | 230 | 7.7s | [ ] keep [ ] kill |
| B07 | Skew And Shear | 00:58 | SkewAndShear | 240 | 8.0s | [ ] keep [ ] kill |
| B08 | Opacity Through Blur | 01:06 | OpacityThroughBlur | 292 | 9.7s | [ ] keep [ ] kill |
| B09 | Color Interpolation | 01:16 | ColorInterpolation | 244 | 8.1s | [ ] keep [ ] kill |
| B10 | Kinetic Grid | 01:24 | KineticGrid | 289 | 9.6s | [ ] keep [ ] kill |
| B11 | Glitch Slices | 01:34 | GlitchSlices | 277 | 9.2s | [ ] keep [ ] kill |
| B12 | Trail Echo | 01:43 | TrailEcho | 266 | 8.9s | [ ] keep [ ] kill |
| B13 | Noise Wobble | 01:52 | NoiseWobble | 296 | 9.9s | [ ] keep [ ] kill |
| B14 | Elastic Physics | 02:02 | ElasticPhysics | 237 | 7.9s | [ ] keep [ ] kill |
| B15 | Card Flip | 02:10 | CardFlip | 289 | 9.6s | [ ] keep [ ] kill |
| B16 | Shadow Play | 02:19 | ShadowPlay | 214 | 7.1s | [ ] keep [ ] kill |
| B17 | Composer Summon | 02:26 | ComposerSummon | 311 | 10.4s | [ ] keep [ ] kill |
| B18 | Stroke Pulse | 02:37 | StrokePulse | 257 | 8.6s | [ ] keep [ ] kill |
| B19 | Scale Breathe | 02:45 | ScaleBreathe | 213 | 7.1s | [ ] keep [ ] kill |
| B20 | Exit Family | 02:52 | ExitFamily | 306 | 10.2s | [ ] keep [ ] kill |
| B21 | Your Turn (handoff) | 03:03 | ClaudeComposerAsk | 324 | 10.8s | KEEP |
| B22 | ClaudeTitleOutro | 03:13 | ClaudeTitleOutro | 60 | 2.0s | KEEP |

## Notes

- **B03 Draw-On Stroke** uses `@remotion/paths` `evolvePath()` on the full complex path (7500×5000 viewBox, single d-string). Stroke traces in terracotta, fill floods behind.
- **B09 Color Interpolation** is the one designated color treatment beat. Mark cycles black→terracotta→black.
- **B17 Composer Summon** shows the Claude composer card with a realistic prompt being typed, terracotta spark on send, mark materializes below.
- **B18 Stroke Pulse** uses `strokeDasharray` / `strokeDashoffset` cycling to create a heartbeat rhythm across the path in terracotta.
- **B20 Exit Family** runs three exit moves back-to-back in thirds: Shrink Spin → Blur Out → Mask Close.
- All SVG filters from the source file are dropped (per spec). The `<rect class="st0">` background rect is also dropped — cream PAGE is the stage.
- Logo ink: `#000000` on cream `#FAF9F5` except B09 (color treatment) and B17 (composer context).
- One terracotta `#D97757` accent moment per technique beat. No beat has two orange things.

## Source Files

- Component: `runtime/remotion/src/BearBrownLogoRemotionShowcase16x9.tsx`
- Timing: `runtime/remotion/src/bear-brown-logo-remotion-showcase-16x9-timing.json`
- Audio: `runtime/remotion/public/bear-brown-logo-mp3/beat-B{00-22}.mp3`
- Beat sheet: `youtube/claude-liam-bear-brown-logo-remotion-showcase-16x9/beat_sheet.json`
- MP4: `youtube/claude-liam-bear-brown-logo-remotion-showcase-16x9/mp4/claude-liam-bear-brown-logo-remotion-showcase-16x9.mp4`
