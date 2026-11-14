# BUILD-PROMPT — What We Ask For.

The single paste-ready prompt that rebuilds this reel end to end. Run from the toolkit
root (`brutalist.art-main/`). Never publishes.

```
Rebuild the reel at /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-what-we-ask-for
("What We Ask For." — @Yatra, Kokoro af_bella, intro fixed verbatim:
"Hi, this is Yatra, Social Media Manager at Humanitarians AI"; ends on the question
"what are we actually asking for, when we ask for art?").

Read skills/make/ai-explainer/SKILL.md completely first, then FACTCHECK.md. Seven supplied
findings, five sources. Hard rules:
  1. No figure beyond them; values print verbatim ("20–40% more", "58%"); numeric props only draw.
  2. B03 is a schematic — no data plotted, caption stays.
  3. Every figure keeps its own source line; B14 keeps the causation caveat + falsifier.
  4. Narration spells "E.U. A.I. Act", "Article fifty", spoken years for Kokoro.

Steps:
  1. GATE CHECK — 18 SHOW/CARD / 0 PUNT (CHECKS-REPORT.md); numeral sweep per FACTCHECK.md.
  2. AUDIO: .venv/bin/python runtime/scripts/generate_audio_kokoro.py <REEL>
     then copy each beat's actual_duration_s into shot.remotion.props.data.durationS
     (Wwa* compositions read their length from that prop via calculateMetadata).
  3. RENDER: ART_CONCURRENCY=4 .venv/bin/python runtime/scripts/remotion_scenes.py <REEL>
  4. COMPILE: .venv/bin/python runtime/scripts/compile.py <REEL> --height 2160
  5. VISUAL QC — read sampled frames, 9-point rubric → QC-LOG.md.
  6. 9:16 FULL LENGTH (over the 3:00 cap on purpose):
     .venv/bin/python runtime/scripts/shorts.py <REEL> --drop --handle "@Yatra";
     regenerate short/media/END.png at 2160x3840; render short beats;
     .venv/bin/python runtime/scripts/compile.py <REEL>/short --height 3840
  7. QC the portrait cut separately (keep-out y~1440 / x~960).
  8. REPORT. Do not publish.
```
