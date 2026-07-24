# TECHNIQUES.md

Reel: claude-liam-musinique-logo-2-remotion-showcase-16x9
Duration: 3:45.9 (225.9s, 6777 frames @ 30fps)
Rendered: 2026-07-16
Subject: logos/musinique-logo-2.svg (viewBox 0 0 2048 2048, 1 path element, 73 subpaths)
Channel: claude-liam · @HumanitariansAI · Kokoro af_kore · Teardown register

| Beat | Technique | Start | Duration | Scene file | Keep/Kill |
|------|-----------|-------|----------|------------|-----------|
| B00 | ClaudeComposerAsk | 0:00.00 | 11.7s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B01 | Spring Entrance | 0:12.20 | 7.2s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B02 | Overshoot Spring | 0:19.87 | 10.2s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B03 | Draw-On Stroke | 0:30.57 | 7.5s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B04 | Mask Reveal | 0:38.53 | 9.1s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B05 | Scale Zoom | 0:48.13 | 8.9s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B06 | Rotation | 0:57.57 | 11.6s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B07 | Skew And Shear | 1:09.60 | 9.5s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B08 | Opacity Through Blur | 1:19.57 | 9.3s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B09 | Color Interpolation | 1:29.30 | 10.3s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B10 | Kinetic Grid | 1:40.03 | 9.3s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B11 | Glitch Slices | 1:49.87 | 9.3s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B12 | Trail Echo | 1:59.70 | 9.8s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B13 | Noise Wobble | 2:09.93 | 9.6s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B14 | Elastic Physics | 2:20.03 | 10.1s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B15 | Card Flip | 2:30.57 | 11.3s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B16 | Shadow Play | 2:42.33 | 9.4s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B17 | Composer Summon | 2:52.23 | 10.1s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B18 | Stroke Pulse | 3:02.83 | 9.2s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B19 | Scale Breathe | 3:12.50 | 8.8s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B20 | Exit Family | 3:21.80 | 11.5s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B21 | Your Turn (handoff) | 3:33.77 | 7.7s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |
| B22 | ClaudeTitleOutro (outro) | 3:41.90 | 4.0s | MusiniqueLogo2RemotionShowcase16x9.tsx | [ ] keep [ ] kill |

## Notes

- All 20 technique beats rendered clean — no slate fallbacks needed.
- B08 (Opacity Through Blur): at frame 2400 the mark is mid-reveal; the blur-sharpening effect is clearly visible.
- B09 (Color Interpolation): treatment beat — ink sweeps to terracotta, then to teal. Explicit palette violation, intentional.
- B10 (Kinetic Grid): 4×2 tile, staggered ripple wave uses sin() phase offset per column+row distance.
- B17 (Composer Summon): custom in-scene composer card (no ClaudeComposerAsk component) — mark assembles below as the "result".
- B03 (Draw-On Stroke): estimated strokeDasharray at 120000 — this is a conservative estimate for the 73-subpath logo; actual path length is longer. The reveal still reads as a draw-on because progress × STROKE_LEN always covers the visible portion of the stroke from the beginning.
- Root.tsx: two pre-existing portrait showcase files (MusiniquLogoRemotionShowcase.tsx — missing — and MusiniqueLogo2RemotionShowcase.tsx — uses `interpolateColors` not in this remotion build) are temporarily commented out in Root.tsx to unblock the bundle. They were already failing before this reel was built.
