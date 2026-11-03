# BUILD-PROMPT — The Mask Slips.

The single paste-ready prompt that rebuilds this reel end to end. Run from the toolkit
root (`brutalist.art-main/`). Never publishes.

---

```
Rebuild the reel at /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-the-mask-slips
("The Mask Slips." — @Yatra, narrated by Kokoro af_bella as "Bella, in for Yatra").

Read skills/make/ai-explainer/SKILL.md completely first, then the reel's
FACTCHECK.md. Three constraints are load-bearing and enforced by the component
types rather than by discipline — do not relax any of them:

  1. Every figure-bearing scene (MskSpike, MskMoney, MskDrop) REQUIRES a
     `source`. A number cannot reach the screen uncited. Do not add a scene
     that renders a figure without one.
  2. Every `value` is a STRING printed verbatim. "$13,700", "2.2 million",
     "roughly 50%" and the non-numeric "the same drop" must all survive
     intact. Nothing parses a displayed string; bars come from separate
     numeric props.
  3. There is no `name`/`handle`/`platform` prop anywhere in MaskSlips.tsx.
     Neither AI account was named to us, so neither can be named here.
     Do not add one.

  MskMoney REQUIRES a `stamp` ("reported" — the figure is not audited) and
  MskArc REQUIRES an `axisNote`: that curve has no numeric prop at all and
  must say on screen that it carries no figures.

Steps, in order:

  1. GATE CHECK — confirm 13 SHOW / 0 PUNT (CHECKS-REPORT.md) and re-run the
     numeral sweep in FACTCHECK.md. Every numeric token on screen must be one
     of the six supplied figures or the citation year.

  2. AUDIO (the master clock, always first):
       .venv/bin/python runtime/scripts/generate_audio_kokoro.py <REEL>

  3. CONFORM — if any narration changed, update that beat's durationInFrames
     in runtime/remotion/src/Root.tsx to the new measured length x 30. NEVER
     hand-tune timing in the beat sheet.

  4. RENDER each beat:
       ART_CONCURRENCY=3 .venv/bin/python runtime/scripts/remotion_scenes.py <REEL> --only B00
     ...through B12. Never hand-roll `npx remotion render` (house rule 4).
     The wrapper's --scale=2 is what makes the master TRUE 4K (3840x2160
     native, supersampled — not upscaled).

     RENDER ENVIRONMENT, learned the hard way on this build:
       * If renders fail with "Timed out ... while trying to connect to the
         browser", you have orphaned chrome-headless-shell processes and/or
         stale puppeteer_dev_chrome_profile-* dirs under /var/folders. Kill
         the processes and delete the profile dirs, then retry. This happens
         after a machine sleeps mid-render.
       * If renders fail with "Timeout (30000ms) exceeded rendering the
         component at frame N", raise ART_TIMEOUT (the wrapper now defaults
         to 120000). Remotion's own 30s default is not enough headroom for a
         scale=2 frame of full-bleed EB Garamond on a loaded machine.
       * Do not render and encode 4K at the same time — concurrent work is
         what pushes frames past the timeout in the first place.

  5. COMPILE the clean master:
       .venv/bin/python runtime/scripts/compile.py <REEL> --height 2160

  6. VISUAL QC — the mp4 probe is a FILE check and does NOT count. Sample
     frames and LOOK at them; audit the 9-point rubric; log to _qc/QC-LOG.md.
     Fix root causes in scene source and re-render until zero BLOCKER/MAJOR.

     GATE V (runtime/qc/final_frame_check.py) reports false BLOCKERs on every
     reel built in this tree — its BURN_IN_EXCLUDE masks the bottom strip
     while the review cut's label is drawn top-right. Measure ink coverage
     with its own analyze_frame() on the CLEAN master instead. Do not "fix"
     the reel to satisfy it. GATE T (scripts/type_check.py) is not present in
     this tree at all; substitute by inspection and log the substitution.

  7. THE 9:16 CUT:
       .venv/bin/python runtime/scripts/shorts.py <REEL> --drop --handle "@Yatra"
     The reel is 2:48.8, under the 3:00 cap, so NO beats are cut — pass
     --drop with no ids to make the empty plan explicit. PASS --handle
     "@Yatra": shorts.py defaults to @nikbearbrown and never reads the reel's
     own channel_handle.
     Then render the short's beats and:
       .venv/bin/python runtime/scripts/compile.py <REEL>/short --height 3840

     shorts.py hardcodes its endcard PNG at 1080x1920, so a --height 3840
     compile UPSCALES it and compile.py warns. Regenerate the endcard at
     2160x3840 (same design, all metrics doubled) before the final compile.

  8. QC THE PORTRAIT CUT SEPARATELY — it is re-banded, not scaled, so its
     layouts are different code. Check the Shorts keep-out: nothing critical
     below y~1440 or right of x~960.

  9. REPORT durations, resolutions, defects found and fixed. Do not publish.
```

---

## What this reel is, in one paragraph

A 2:48 concept explainer on AI influencer accounts that earn real money within days and
collapse once audiences identify them as AI. Thirteen beats: cold open, BLUF, the speed,
the money, one ask→result pair on the rise-and-fall arc, the mechanism of the reveal, the
engagement drop, why audiences turn rather than drift, a falsifiability beat, verdict,
handoff, outro. Eight purpose-built `Msk*` scenes, five bookends on the shared Claude UI
components. Every figure comes from one report (Garbage Day, October 2026) and is cited on
screen. Fully deterministic — no stills, no stock, no pantry media, no paid calls.
