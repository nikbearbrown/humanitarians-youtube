# BUILD-PROMPT — Be the Sentence.

The single paste-ready prompt that rebuilds this reel end to end. Run from the toolkit
root (`brutalist.art-main/`). Never publishes.

```
Rebuild the reel at /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-be-the-sentence
("Be the Sentence." — @Yatra, Kokoro af_bella, intro fixed verbatim:
"Hi, this is Yatra, Social Media Manager at Humanitarians AI").

Read skills/make/ai-explainer/SKILL.md completely first, then FACTCHECK.md. Seven supplied
findings, six sources. Hard rules:
  1. No figure beyond them; values print verbatim (`~94%`, `3.2×`); `bar` only draws.
  2. No gap / remainder / growth-multiple numbers (GeoGap has a label, not a number).
  3. Every figure keeps its own source line; B10 keeps the correlation falsifier.
  4. Narration spells "S.E.O." and spoken years ("twenty twenty-six") for Kokoro.

Steps:
  1. GATE CHECK — 14 SHOW / 0 PUNT (CHECKS-REPORT.md); numeral sweep per FACTCHECK.md.
  2. AUDIO: .venv/bin/python runtime/scripts/generate_audio_kokoro.py <REEL>
     If narration changes, retarget each Geo* durationInFrames in Root.tsx (seconds x 30).
  3. RENDER: ART_CONCURRENCY=4 .venv/bin/python runtime/scripts/remotion_scenes.py <REEL>
  4. COMPILE: .venv/bin/python runtime/scripts/compile.py <REEL> --height 2160
  5. VISUAL QC — read sampled frames, 9-point rubric → _qc/QC-LOG.md.
  6. 9:16: .venv/bin/python runtime/scripts/shorts.py <REEL> --drop --handle "@Yatra";
     regenerate short/media/END.png at 2160x3840; render short beats;
     .venv/bin/python runtime/scripts/compile.py <REEL>/short --height 3840
  7. QC the portrait cut separately (keep-out y~1440 / x~960).
  8. REPORT. Do not publish.
```
