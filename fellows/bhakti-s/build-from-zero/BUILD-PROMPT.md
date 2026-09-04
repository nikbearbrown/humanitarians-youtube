# BUILD-PROMPT.md — claude-hai-built-from-zero-thesis

Paste-ready prompt to rebuild this reel end to end.

```
Rebuild the reel at youtube/claude-hai-built-from-zero-thesis end to end:

1. Generate audio: python3 runtime/scripts/generate_audio_kokoro.py
   youtube/claude-hai-built-from-zero-thesis
   If B03's DamLifecycleReveal timing is off from a proportional split of
   the new duration against its 4 steps' word counts, recompute
   revealFrames and update beat_sheet.json before rendering.

2. Run ART_STRICT=0 bash runtime/scripts/run.sh
   youtube/claude-hai-built-from-zero-thesis
   ART_STRICT=0 is intentional — BOUT and BVDT are accepted shared-
   component underfill warnings, not something to fix here. B03_50's
   underfill is also accepted, as a reveal-timing artifact. See
   CHECKS-REPORT.md.

3. If GATE V reports NEW underfill on B01, B02, or B04 (the reused
   components), do not assume the existing scaling fixes still hold —
   they were tuned for specific content lengths. Re-verify visually
   before assuming the formulas generalize. See BUILD-LOG.md for the
   history of these components' scaling fixes.

4. Note: B01's narration and on-screen content deliberately diverge as of
   2026-08-31 — the spoken narration includes a personal self-introduction
   the on-screen DamExecSummary card does not show. This video is where
   that decision originated (a marginal GATE V finding — 55% fill against
   the 55% minimum — on the on-screen self-intro version prompted the
   narration-only approach across the whole series). If regenerating B01,
   preserve this split rather than "fixing" the mismatch — see
   BUILD-LOG.md and PEDAGOGY.md for the full reasoning.

5. Report final GATE L / GATE V status and the output path. Do not
   publish — that's a separate human decision.
```
