# BUILD-PROMPT — Film the Impossible.

The single paste-ready prompt that rebuilds this reel end to end. Run from the toolkit
root (`brutalist.art-main/`). Never publishes.

```
Rebuild the reel at /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-film-the-impossible
("Film the Impossible." — @Yatra, Kokoro af_bella, intro fixed verbatim:
"Hi, this is Yatra, Social Media Manager at Humanitarians AI").

Read skills/make/ai-explainer/SKILL.md completely first, then FACTCHECK.md. Three supplied
points, one source (Remake the Trend, Nov 17, 2026). Hard rules:
  1. No figures at all: no views, creator counts or tool names. The Ft* scenes have no numeric props.
  2. Paraphrase, never quote. Trend examples are flat sketches, never footage; no non-AI trend named.
  3. Every sourced beat keeps its source line; B07 keeps the know / don't-know ledger + viewer check.
  4. Keep the toolkit off iCloud eviction (low disk offloads node_modules and stalls renders).

Steps:
  1. GATE CHECK — 11 SHOW / 0 PUNT (CHECKS-REPORT.md); numeral sweep per FACTCHECK.md.
  2. AUDIO: .venv/bin/python runtime/scripts/generate_audio_kokoro.py <REEL>
     If narration changes, retarget each Ft* durationInFrames in Root.tsx (seconds x 30).
  3. RENDER: ART_CONCURRENCY=4 .venv/bin/python runtime/scripts/remotion_scenes.py <REEL>
  4. COMPILE: .venv/bin/python runtime/scripts/compile.py <REEL> --height 2160
  5. VISUAL QC — read sampled frames, 9-point rubric → QC-LOG.md.
  6. 9:16: .venv/bin/python runtime/scripts/shorts.py <REEL> --handle "@Yatra";
     regenerate short/media/END.png at 2160x3840; render short beats;
     .venv/bin/python runtime/scripts/compile.py <REEL>/short --height 3840
  7. QC the portrait cut separately (keep-out y~1440 / x~960).
  8. REPORT. Do not publish.
```
