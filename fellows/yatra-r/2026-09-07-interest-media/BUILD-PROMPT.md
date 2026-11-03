# BUILD-PROMPT — Interest Media.

The single paste-ready prompt that rebuilds this reel end to end. Run it from the toolkit
root (`brutalist.art-main/`). Never publishes.

---

```
Rebuild the reel at /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-interest-media
("Interest Media." — @Yatra, narrated by Kokoro af_bella as "Bella, in for Yatra").

Read skills/make/ai-explainer/SKILL.md completely first. Then read the reel's
FACTCHECK.md — two of its constraints are load-bearing and are enforced by the
component types, not by discipline:

  1. Gary Vaynerchuk is CREDITED and never QUOTED. ItmSource has a
     `claimParaphrase` field and no `quote` field. Do not add one.
  2. No numeric prop exists anywhere in the Itm* family. Do not add one.
     If a beat seems to need a figure, it does not — it needs an ordering.

Steps, in order:

  1. GATE CHECK — confirm beat_sheet.json still classifies 13 SHOW / 0 PUNT
     (CHECKS-REPORT.md), and re-run the numeral sweep over every
     shot.remotion.props string. Expected result: 0 matches.

  2. AUDIO (the master clock, always first):
       .venv/bin/python runtime/scripts/generate_audio_kokoro.py <REEL>
     Kokoro af_bella, free and local. Durations are ground truth.

  3. CONFORM THE COMPOSITIONS — if any narration changed, update that beat's
     durationInFrames in runtime/remotion/src/Root.tsx to the new measured
     length x 30. NEVER hand-tune timing in the beat sheet; regenerate and
     recompile instead.

  4. RENDER each beat:
       .venv/bin/python runtime/scripts/remotion_scenes.py <REEL> --only B00
     ...through B12. Do NOT hand-roll `npx remotion render` (house rule 4).
     The wrapper renders --scale=2 --image-format=png --crf=16, which is what
     makes the master TRUE 4K (3840x2160 native, not upscaled).

  5. COMPILE the clean master:
       .venv/bin/python runtime/scripts/compile.py <REEL> --height 2160

  6. VISUAL QC — the mp4 probe is a FILE check and does NOT count. Sample
     frames and actually LOOK at them:
       ffmpeg -i <master> -vf fps=2 _qc/frames/%05d.png
     plus each beat at ~15/50/85% of its span. Audit the 9-point rubric and
     log to _qc/QC-LOG.md. Fix root causes in scene source and re-render
     until zero BLOCKER and zero MAJOR remain.

     Known toolkit issue: GATE V (runtime/qc/final_frame_check.py) reports
     false BLOCKERs on every reel built in this tree — its BURN_IN_EXCLUDE
     masks the bottom strip while the review cut's beat label is drawn
     top-right. Measure ink coverage with its own analyze_frame() on the
     CLEAN master instead. Do not "fix" the reel to satisfy it.

     Known toolkit gap: GATE T (scripts/type_check.py) is not present in this
     tree. Substitute by inspection; log the substitution.

  7. THE 9:16 CUT:
       .venv/bin/python runtime/scripts/shorts.py <REEL>
     The reel is 2:29.6, under the 3:00 Shorts cap, so NO beats are cut —
     pass --drop with no ids to make the empty drop plan explicit. The ONDA
     CHECK rewires each <pattern> to <pattern>916; all sixteen portrait
     compositions are registered. Then render the short's beats and:
       .venv/bin/python runtime/scripts/compile.py <REEL>/short --height 3840

     If you edit the parent after deriving the short, RE-DERIVE the short —
     a stale short/beat_sheet.json holding an old duration is a known way to
     ship an over-long portrait beat.

  8. QC THE PORTRAIT CUT SEPARATELY. It is re-banded, not scaled, so its
     layouts are different code and need their own frame pass. Check the
     Shorts keep-out: nothing critical below y~1440 or right of x~960.

  9. REPORT: durations, resolutions, defects found and fixed. Do not publish.
     The master stays in the reel folder.
```

---

## What this reel is, in one paragraph

A 2:29 concept explainer on the shift from follower-sorted feeds to interest-sorted ones —
a framing the human credits to Gary Vaynerchuk and asked to have paraphrased rather than
quoted. Thirteen beats: cold open, BLUF, the source and the rename, the worked example on
the viewer's own feed, the volume that broke the old sort key, the mechanism swap, one
ask→result pair on the two reach models, the marketer's new question, a falsifiability
beat, verdict, handoff, outro. Eight purpose-built `Itm*` scenes, five bookends on the
shared Claude UI components. Fully deterministic — no stills, no stock, no pantry media,
no paid calls.
