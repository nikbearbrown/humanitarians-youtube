# BUILD-PROMPT — Both Sides of the Table.

The single paste-ready prompt that rebuilds this reel end to end. Run from the toolkit
root (`brutalist.art-main/`). Never publishes.

---

```
Rebuild the reel at /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-both-sides-of-the-table
("Both Sides of the Table." — @Yatra, narrated by Kokoro af_bella as "Bella,
in for Yatra").

Read skills/make/ai-explainer/SKILL.md completely first, then the reel's
FACTCHECK.md. This episode carries EIGHT supplied figures from FIVE different
publishers, and the main risk is that they get read as one dataset. Four
constraints are enforced by the component types — do not relax any of them:

  1. Every figure-bearing scene REQUIRES a `source`, and TblTrust requires a
     SEPARATE source on EACH of its two figures. The 26% and the 66% come
     from different studies of different populations. They are never merged,
     never added, never given a shared citation.
  2. `value` is a verbatim STRING; `bar` is a separate number that drives
     drawing. "4 in 5" must NEVER render as "80%". Nothing parses a displayed
     string — an earlier reel in this series shipped a bug where the house
     num() helper read "4-13%" as 413.
  3. TblInterview has NO `previous` prop and REQUIRES a `deltaNote`. Only the
     +13-point change was published; subtracting it from 63 to show an
     earlier figure would be inventing a data point.
  4. TblInject REQUIRES a `stamp` (self-reported) and renders only generic
     resume headings. Never render a working injection string.

  Also: no remainder is ever captioned. TblTrust's 26% leaves its track
  visibly unfilled and UNLABELLED, because 100-26 is arithmetic, not a
  published figure.

Steps, in order:

  1. GATE CHECK — confirm 14 SHOW / 0 PUNT (CHECKS-REPORT.md) and re-run the
     numeral sweep in FACTCHECK.md. Every on-screen numeric token must be one
     of the eight supplied figures or a citation year.

  2. AUDIO (the master clock, always first):
       .venv/bin/python runtime/scripts/generate_audio_kokoro.py <REEL>
     NOTE: this reel was trimmed twice to fit. The first pass ran 3:13.5 —
     over both the 1-3 minute brief AND the 3:00 Shorts cap. If you re-author
     narration, re-measure before building anything.

  3. CONFORM — update each affected composition's durationInFrames in
     runtime/remotion/src/Root.tsx to the new measured length x 30. TblSide
     backs TWO beats and must be registered at the SHORTER of them.

  4. RENDER each beat:
       ART_CONCURRENCY=3 .venv/bin/python runtime/scripts/remotion_scenes.py <REEL> --only B00
     ...through B13. Never hand-roll `npx remotion render`.

     RENDER ENVIRONMENT, learned the hard way on this build:
       * "Timed out ... while trying to connect to the browser" = orphaned
         chrome-headless-shell processes and/or stale
         puppeteer_dev_chrome_profile-* dirs under /var/folders. Kill and
         clear them, then retry. Happens after the machine sleeps mid-render.
       * "Timeout (30000ms) exceeded rendering the component at frame N" =
         raise ART_TIMEOUT (the wrapper now defaults to 120000).
       * Never render and encode 4K concurrently.

  5. COMPILE the clean master:
       .venv/bin/python runtime/scripts/compile.py <REEL> --height 2160

  6. VISUAL QC — the mp4 probe is a FILE check and does NOT count. Sample
     frames, LOOK at them, audit the 9-point rubric, log to _qc/QC-LOG.md.
     GATE V produces false BLOCKERs in this tree; GATE T is not shipped here.
     Substitute by inspection and log it rather than passing silently.

  7. THE 9:16 CUT:
       .venv/bin/python runtime/scripts/shorts.py <REEL> --drop --handle "@Yatra"
     2:49.4 is under the cap, so no beats are cut — pass --drop with no ids
     for an explicit empty plan. PASS --handle "@Yatra" (default is
     @nikbearbrown). Then render the short's beats and:
       .venv/bin/python runtime/scripts/compile.py <REEL>/short --height 3840
     Regenerate the endcard PNG at 2160x3840 first — shorts.py hardcodes
     1080x1920 and a 4K compile upscales it.

  8. QC THE PORTRAIT CUT SEPARATELY. Keep-out: nothing critical below y~1440
     or right of x~960.

  9. REPORT durations, resolutions, defects. Do not publish.
```

---

## What this reel is, in one paragraph

A 2:49 data explainer on hiring becoming a standoff between two AIs. Fourteen beats: cold
open, BLUF, the employers' side, the candidates' side, one ask→result pair on the
four-seat table, the AI interview and its six-month move, the share who walked away, the
two trust figures, the hidden-instruction escalation, a limits beat, verdict, handoff,
outro. Eight purpose-built `Tbl*` scenes, five bookends on the shared Claude UI
components. Eight supplied figures from five publishers, each cited on screen, none
altered. Fully deterministic — no stills, no stock, no pantry media, no paid calls.
