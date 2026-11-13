# SHOTLIST — RAG: Why "Looking It Up" Doesn't Guarantee It's True

## ~2:18 (138.83s) measured total · 9 beats · all Manim, no pantry/toolkit assets

Durations below are the real Kokoro-measured `actual_duration_s` values from
`beat_sheet.json` (B00 is the fixed 4.049s silent-track target; B01-B08 are
measured `af_bella` narration lengths via `generate_audio_kokoro.py` +
ffprobe). `scenes.py` is authored and each scene's `self.wait()` budget is
tuned to these exact numbers — see that file's per-scene comments.

| Beat | Act | Lane | Medium | Scene class | Measured Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | `B00_TitleCard` | 4.05s | Silent title card, `audio_policy: "silence"`, real silent mp3 via ffmpeg anullsrc |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | `B01_ExecSummary` | 18.74s | Fellow name/role badge + spoken one-line thesis summary, streamed with narration |
| B02 | HOOK | manim | GRAPHIC | `B02_StaleDocHook` | 17.30s | Chat-style question, retrieved doc card stamped with an old date, confident answer bubble, then STALE/WRONG reveal — generic/hypothetical support-bot scenario |
| B03 | FRAMEWORK | manim | GRAPHIC | `B03_ThreeQuestionsFramework` | 26.35s | All 3 rubric questions (Relevant/Current/Grounded) shown together, skeleton-first, before any example |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | `B04_StaleDocResolved` | 17.14s | Retrieved (stale-dated) document AND the model's answer shown side by side; today's date and the document's date both legible together; divider clearance guaranteed via `clear_of_divider()` |
| B05 | FALSIFIABILITY | manim | GRAPHIC | `B05_RetrievalWorksFalsifiability` | 25.39s | "No retrieval" (invented, wrong) vs. "with retrieval" (correct, grounded) — two bordered panels with a visible gap, both clearly labeled, fair same-mechanism comparison |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | `B06_AuditChecklist` | 18.86s | The 3 questions restated as a literal checkbox checklist card — visually distinct from B03's numbered rubric |
| B07 | TAKEAWAY | manim | GRAPHIC | `B07_Statement` | 9.48s | 3-line statement card, dark background |
| B08 | SIGN-OFF | manim | GRAPHIC | `B08_BrandOutro` | 1.51s | @HumanitariansAI, in for Sai Pranavi J. — very short beat, single combined reveal |

## Side-by-side / split-screen legibility check

Two beats use a two-column layout: B04 (divider line at x=0, cleared via
`clear_of_divider()`, same helper and margin discipline as the sibling
2026-08-17 reel's v3.1 fix) and B05 (two separated bordered panels with a
visible ~1.4-unit gap and no divider line drawn through the frame at all).
Both were spot-checked by extracting real rendered frames after the first
`./art run` pass — see `BUILD-LOG.md` for the frame-by-frame findings.

## QC plan

- Pre-flight (before first render): GATE A/W static scene check
  (`runtime/scripts/build_safety.py` invoked via `./art run`) — catches
  shape-distinctness and margin/off-frame issues before spending a render.
- Post-render: GATE V `final_frame_check.py --lenient` on the true clean
  master (never the `-slate.mp4` watermarked review cut), plus manual frame
  extraction via ffmpeg at multiple timestamps per beat — especially B04 and
  B05 — looked at directly, not inferred from the BLOCKER/MAJOR count alone.
