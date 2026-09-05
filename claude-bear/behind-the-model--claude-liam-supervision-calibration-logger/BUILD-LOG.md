# BUILD-LOG — behind-the-model--claude-liam-supervision-calibration-logger

## 2026-09-05 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/behind-the-model/claude-liam-supervision-calibration-logger/beat_sheet.json`
(a CLI-explainer build of a log/classify/audit supervision-calibration tool:
three commands — log, classify by Level I/II/III with an estimated fair
verification time, and audit for the top "gap" interactions — Level III
usage with under two minutes of verification; a 12-interaction demo week
scoring 50% with three danger-corner interactions; a revision adding a
recommended verification step per gap interaction; and a next-steps beat
to run the logger for a week and re-audit in two).

**The call:** register CLI/Teardown -> Plain, general audience. Dropped the
source's actual terminal commands, its Python code snippet (the gap
list-comprehension), and its named classifier model (claude-3-5-haiku) —
no invented or stale product specifics for a general viewer; the mechanism
survives as plain narration instead ("a small tool that does three
things..."). B00 replaced the source's `NikBearBrownOpen` title card with
`BrutalistHesitantWriter` per WRITER LAW: "careful" -> "calibrated" —
directly reusing the source's own key term ("Supervision Calibration
Logger", "calibration score") as the correction, which also seeds the
carry-out. Added a wrong-guess beat (B01: supervision as one flat personal
habit vs. logged task-by-task, falsified by "not every task hands Claude
the same amount of trust... a flat habit can't track that difference")
and an anchor (B03 -> B05: the source's own 12-interaction usage/
supervision grid, 3 danger-corner dots, literalized) per this factory's
PHASE 1 structure, since the source's CLI spine (INTRO/PROBLEM/ASK/CODE/
OUTPUT/CHANGE/OUTPUT-revised/SUMMARY/NEXT-STEPS, ~10 beats + BOOKEND
verdict/handoff/outro) carried neither in the Plain sense. Beat count
compressed from the source's ~10-plus-bookend CLI spine to 9 beats (B00,
B01-B05, BCRY, BHTF, BOUT) — the source's CODE beat is dropped entirely
(no code shown to a general audience) and its OUTPUT/CHANGE/OUTPUT-
revised/SUMMARY/NEXT-STEPS beats collapse into the anchor-planted (B03) /
mechanism-continued (B04) / anchor-payoff-and-both-directions (B05) arc.
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off.
See QUESTION.md for the full source-gap finding and CARRY-OUT.md for the
line and the wrong guess it defeats.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 9 beats, free, `am_onyx`, first pass, no
   retries. B00 landed at 11.78s (clear of the >=9s TIMING LAW floor) on
   the first narration draft (34 words + `lead_silence_s: 0.8`). Durations:
   B00 11.78s, B01 22.21s, B02 20.57s, B03 16.45s, B04 16.70s, B05 18.54s,
   BCRY 10.24s, BHTF 17.62s, BOUT 4.31s (+1.0s tail).
2. Verified B00's correction on frame pulls at t=3.0/4.2/6.0/9.5/11.0s:
   "careful" typed in accent color at t=3.0s, corrected to "calibrated" by
   t=4.2s, full question settled well before the 11.8s cutoff. TIMING LAW
   satisfied on the first pass — no rewrite needed.
3. Wrote `scenes.py` (5 Manim scenes, reel-unique names `SCB01Scene`
   through `SCB05Scene`) and `render_scenes.py`; rendered all five in the
   foreground, no render failures at any point.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The tool's own
   `--concurrency` flag does not exist in this version (rejected as an
   unrecognized argument); the plain invocation was used instead. The
   first foreground call was killed by the harness's default 120s Bash
   timeout mid-render (BCRY and BOUT had already completed); rather than
   backgrounding the remainder per the one-shot COMPLETION LAW, the same
   command was re-run in the foreground with an explicit 600s tool
   timeout, which picked up where it left off (`filled already (skip)`
   for BCRY/BOUT) and completed B00 and BHTF cleanly. All four beats
   native 3840x2160.
5. First `compile.py` pass -> 9/9 real (no slate), native 3840x2160 (THE
   4K LAW), GATE AUDIO mean_volume -23.8 dB inline. Non-blocking WARNING:
   motion histogram graphic:5 remotion:4 (55%, over the ~40% pantry cap)
   — structural, not a defect: this reel's source carried more distinct
   teaching beats (mechanism build, anchor plant, revision loop, anchor
   payoff) than the shorter siblings in this family, and hai-simple's
   4 fixed REMOTION slots (writer/carry-out/your-turn/outro) don't scale
   with body length.
6. GATE T (`type_check.py`) FAILED on the first pass: 1 pixel beat. B03's
   rotated y-axis label ("VERIFICATION TIME", rotated 90 degrees) reported
   a 14px smallest text-run height under the 20px/1080p-logical floor —
   rotation appears to confuse the pixel-run size check. Fix attempt 1
   (bump font_size 16->20, keep rotation) reduced but did not clear the
   failure (17px). Fix attempt 2: dropped the rotation entirely, shortened
   the label to "VERIFY TIME", and placed it unrotated to the left of the
   y-axis. Re-rendered B03 only, recompiled: GATE T -> PASS, 0 FAILs,
   third pass.
7. Gate V (visual, manual): pulled 28 frames at 5s spacing across the full
   139.4s runtime and read every one directly. All legible, correct
   content, no clipping or overlap; correct anchor payoff (B03->B05 grid,
   danger corner shrinking from 3 dots to 1, split into the two
   both-directions cards); correct carry-out/handoff/outro with
   `@HumanitariansAI` branding on B00 and BOUT.
8. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master -> mean_volume **-23.8 dB**, max -2.9 dB. Master mtime
   (1788605768) is newer than beat_sheet.json mtime (1788605170).

**Gates (final state):**
- content-check: PASS (9 beats, no violations)
- frame-check: PASS (3840x2160, 9 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), third pass (B03 font-size + de-rotation fix above)
- Gate V: PASS, first pass — no defects requiring a fix
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 139.44s; mp4 mtime newer than beat_sheet.json mtime

**Playlist resolution:** family `behind-the-model` matches the map's
`behind-the-model` key directly in
`skills/make/hai-simple/loop/playlists.json`, resolving to **Behind the
Model** — no fallback needed.

Metadata file written:
`behind-the-model--claude-liam-supervision-calibration-logger.md` (channel
@HumanitariansAI, Playlist: **Behind the Model**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate (after the GATE T
fix pass above). Proceeding to Phase 4 (4K render + deliver.py) in this
same invocation.
