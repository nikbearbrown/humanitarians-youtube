# BUILD-PROMPT.md — claude-hai-built-from-zero-compliance

Paste-ready prompt to rebuild this reel end to end.

```
Rebuild the reel at youtube/claude-hai-built-from-zero-compliance end to end:

1. Generate audio: python3 runtime/scripts/generate_audio_kokoro.py
   youtube/claude-hai-built-from-zero-compliance
   If B03's DamLifecycleReveal timing is off from a proportional split of
   the new duration against its 3 steps' word counts, recompute
   revealFrames and update beat_sheet.json before rendering.

2. Run ART_STRICT=0 bash runtime/scripts/run.sh
   youtube/claude-hai-built-from-zero-compliance
   ART_STRICT=0 is intentional — BOUT/BVDT are accepted shared-component
   warnings, and B03_50 is an accepted reveal-timing artifact. See
   CHECKS-REPORT.md.

3. If GATE V reports underfill on B01 or B04, do not assume the current
   component fixes automatically hold — both DamExecSummary (headline
   length scaling) and DamSopsChips (chip-count scaling) have already
   needed more than one revision across the three videos in this series.
   Verify visually before trusting the formula for a new content length
   or item count. See BUILD-LOG.md for the full history.

4. Note: B01's narration and on-screen content deliberately diverge as of
   2026-08-31 — the spoken narration includes a personal self-introduction
   the on-screen DamExecSummary card does not show. If regenerating B01,
   preserve this split rather than "fixing" the mismatch — see
   BUILD-LOG.md and PEDAGOGY.md for why.

5. Report final GATE L / GATE V status and the output path. Do not
   publish — that's a separate human decision.
```
