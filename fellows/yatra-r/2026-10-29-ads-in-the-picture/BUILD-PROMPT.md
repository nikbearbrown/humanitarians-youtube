# BUILD-PROMPT — Ads in the Picture.

The single paste-ready prompt that rebuilds this reel end to end. Run from the toolkit
root (`brutalist.art-main/`). Never publishes.

---

```
Rebuild the reel at /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-ads-in-the-picture
("Ads in the Picture." — @Yatra, narrated by Kokoro af_bella as "Bella, in for Yatra").

Read skills/make/ai-explainer/SKILL.md completely first, then the reel's FACTCHECK.md.
The reel states ONLY three supplied points, all cited "Jumpfly, October 2026". Hard rules:

  1. No detail or number beyond the three points. The only figure is "over 4,000" (apps),
     printed verbatim; the AdpDots tile field is decorative and REQUIRES its tileNote.
  2. Never say this is ChatGPT's "first" ad — earlier 2026 ads were reported; this is a new
     visual format (see FACTCHECK.md, "Correction applied").
  3. AdpCanvas is a redraw of a description: no ChatGPT/OpenAI chrome or logo, caption
     required. AdpRoom's bubbles are illustrative, caption required.

Steps:
  1. GATE CHECK — 13 SHOW / 0 PUNT (CHECKS-REPORT.md); numeral sweep per FACTCHECK.md.
  2. AUDIO:  .venv/bin/python runtime/scripts/generate_audio_kokoro.py <REEL>
     If narration changes, re-measure and retarget each Adp* durationInFrames in Root.tsx
     (measured seconds x 30). Keep total under 2:55 so the Short + 4.5s endcard fits 3:00.
  3. RENDER: ART_CONCURRENCY=4 .venv/bin/python runtime/scripts/remotion_scenes.py <REEL>
     (scale=2 default = true 3840x2160). Never hand-roll npx remotion render.
  4. COMPILE: .venv/bin/python runtime/scripts/compile.py <REEL> --height 2160
  5. VISUAL QC — sample frames, LOOK at them, 9-point rubric → _qc/QC-LOG.md.
  6. 9:16:  .venv/bin/python runtime/scripts/shorts.py <REEL> --drop --handle "@Yatra"
     Regenerate short/media/END.png at 2160x3840, render the short's beats, then
     .venv/bin/python runtime/scripts/compile.py <REEL>/short --height 3840
  7. QC the portrait cut separately (keep-out: nothing critical below y~1440 or right of x~960).
  8. REPORT durations, resolutions, defects. Do not publish.
```
