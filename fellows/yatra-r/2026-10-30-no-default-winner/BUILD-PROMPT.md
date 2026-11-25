# BUILD-PROMPT — No Default Winner.

The single paste-ready prompt that rebuilds this reel end to end. Run from the toolkit
root (`brutalist.art-main/`). Never publishes.

---

```
Rebuild the reel at /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-no-default-winner
("No Default Winner." — @Yatra, narrated by Kokoro af_bella as "Bella, in for Yatra").

Read skills/make/ai-explainer/SKILL.md completely first, then FACTCHECK.md. Five figures,
all "Capacity, October 2026". Hard rules:

  1. No detail or number beyond them. "Equally likely to trust either" has NO figure —
     CtrScale has no numeric prop; never print 50/50.
  2. `value` is a verbatim string; `bar` drives drawing. No remainder is captioned.
  3. "Companies haven't caught up" is interpretation — keep the B06 caption and the B09
     falsifier that say so.
  4. Placeholder lines only in B03/B07; person icons stay neutral silhouettes.

Steps:
  1. GATE CHECK — 13 SHOW / 0 PUNT (CHECKS-REPORT.md); numeral sweep per FACTCHECK.md.
  2. AUDIO: .venv/bin/python runtime/scripts/generate_audio_kokoro.py <REEL>
     If narration changes, retarget each Ctr* durationInFrames in Root.tsx (seconds x 30).
  3. RENDER: ART_CONCURRENCY=4 .venv/bin/python runtime/scripts/remotion_scenes.py <REEL>
  4. COMPILE: .venv/bin/python runtime/scripts/compile.py <REEL> --height 2160
  5. VISUAL QC — read sampled frames, 9-point rubric → _qc/QC-LOG.md.
  6. 9:16: .venv/bin/python runtime/scripts/shorts.py <REEL> --drop --handle "@Yatra";
     regenerate short/media/END.png at 2160x3840; render short beats;
     .venv/bin/python runtime/scripts/compile.py <REEL>/short --height 3840
  7. QC the portrait cut separately (keep-out y~1440 / x~960).
  8. REPORT. Do not publish.
```
