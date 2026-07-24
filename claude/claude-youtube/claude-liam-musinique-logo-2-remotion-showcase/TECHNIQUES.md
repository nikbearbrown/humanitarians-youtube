# TECHNIQUES.md — claude-liam-musinique-logo-2-remotion-showcase

Every motion technique in this reel, with timestamps, scene file, and a keep/kill checkbox.

**Subject:** `logos/musinique-logo-2.svg` — Musinique brand mark, viewBox 0 0 2048 2048, 1 complex path (99k chars), fill="black".
**Total runtime:** 2:58 (178.4s, 5350 frames @ 30fps)
**Channel:** claude-liam · @HumanitariansAI · Kokoro af_kore
**Scene file:** `runtime/remotion/src/MusiniqueLogo2RemotionShowcase.tsx`

---

| Beat | Technique | Start | Duration | Scene Component | Keep/Kill |
|------|-----------|-------|----------|-----------------|-----------|
| B00 | ClaudeComposerAsk (cold open) | 0:00 | 10.6s | `ClaudeComposerAsk` | KEEP — required bookend |
| B01 | Spring Entrance | 0:10 | 7.2s | `SpringEntrance` | [ ] |
| B02 | Overshoot Spring (squash+stretch) | 0:17 | 6.7s | `OvershootSpring` | [ ] |
| B03 | Draw-On Stroke (evolvePath trace → fill) | 0:24 | 7.6s | `DrawOnStroke` | [ ] |
| B04 | Mask Reveal (linear wipe + radial iris) | 0:32 | 7.6s | `MaskReveal` | [ ] |
| B05 | Scale Zoom (linear vs bezier) | 0:39 | 7.0s | `ScaleZoom` | [ ] |
| B06 | Rotation (pivot entrance + slow hold) | 0:46 | 7.4s | `Rotation` | [ ] |
| B07 | Skew And Shear (spring in, hold, release) | 0:54 | 8.5s | `SkewAndShear` | [ ] |
| B08 | Opacity Through Blur (arrives out of focus) | 1:02 | 7.3s | `OpacityThroughBlur` | [ ] |
| B09 | Color Interpolation (treatment beat — ink↔terracotta) | 1:09 | 7.2s | `ColorInterpolation` | [ ] |
| B10 | Kinetic Grid (3×4 tiled, staggered ripple) | 1:16 | 7.0s | `KineticGrid` | [ ] |
| B11 | Glitch Slices (7 slices, 8-frame burst) | 1:23 | 8.4s | `GlitchSlices` | [ ] |
| B12 | Trail Echo (slide + 5 ghost copies) | 1:32 | 8.7s | `TrailEcho` | [ ] |
| B13 | Noise Wobble (sine X/Y/rot, decaying amplitude) | 1:41 | 8.5s | `NoiseWobble` | [ ] |
| B14 | Elastic Physics (drop + squash, low damping) | 1:49 | 8.0s | `ElasticPhysics` | [ ] |
| B15 | Card Flip (perspective rotateY spring + slow spin) | 1:57 | 8.5s | `CardFlip` | [ ] |
| B16 | Shadow Play (independent shadow offset → snap) | 2:06 | 7.0s | `ShadowPlay` | [ ] |
| B17 | Composer Summon (type → send spark → mark arrives) | 2:13 | 8.3s | `ComposerSummon` | [ ] |
| B18 | Stroke Pulse (dashoffset heartbeat cycle) | 2:21 | 7.3s | `StrokePulse` | [ ] |
| B19 | Scale Breathe (very slow continuous oscillation) | 2:28 | 7.6s | `ScaleBreathe` | [ ] |
| B20 | Exit Family (shrink-spin → blur-out → mask-close) | 2:36 | 8.9s | `ExitFamily` | [ ] |
| B21 | Handoff (Your turn — ClaudeComposerAsk) | 2:45 | 11.1s | `ClaudeComposerAsk` | KEEP — required bookend |
| B22 | ClaudeTitleOutro (@HumanitariansAI) | 2:56 | 1.9s | `ClaudeTitleOutro` | KEEP — required bookend |

---

## Notes

- **B03 Draw-On Stroke:** uses `@remotion/paths` `evolvePath()` on the full 99k-char path. Works correctly but is compute-intensive per frame; the render was CPU-heavy on this beat.
- **B09 Color Interpolation:** this is the one treatment beat where the logo escapes its ink color — verified `interpolateColors` is available in the installed Remotion build (`function` type confirmed at runtime). Root.tsx imports were previously commented out with incorrect notes about unavailability; both have been restored.
- **B10 Kinetic Grid:** uses 3×4 = 12 tiles rather than 4×5 = 20 to keep tiles readable in portrait with the square 2048×2048 viewBox.
- **B18 Stroke Pulse / B19 Scale Breathe:** these two techniques are unique to this reel (not in the H-mark or HAI wordmark showcase); they exploit the single-path nature of the Musinique mark.
- **Path data:** extracted to `runtime/remotion/src/musinique-logo-2-path.ts` as a TS module (avoids JSON import path issues with Remotion's webpack bundler).

## File inventory

```
youtube/claude-liam-musinique-logo-2-remotion-showcase/
  beat_sheet.json                              — 23 beats, audio-measured durations
  claude-liam-musinique-logo-2-remotion-showcase.mp4  — master (1080×1920, 30fps, 178.4s, 22MB)
  mp3/beat-B00.mp3 … beat-B22.mp3             — 23 Kokoro af_kore audio files
  TECHNIQUES.md                                — this file

runtime/remotion/src/
  MusiniqueLogo2RemotionShowcase.tsx           — main composition (23 beats)
  musinique-logo-2-path.ts                     — SVG path data (99k chars, auto-generated)
  musinique-logo-2-remotion-showcase-timing.json  — beat→frames timing contract

runtime/remotion/public/
  musinique-logo-2-mp3/beat-B00.mp3 … B22.mp3 — audio symlinked for Remotion staticFile
  musinique-logo-2-path.json                   — JSON backup of path data
```
