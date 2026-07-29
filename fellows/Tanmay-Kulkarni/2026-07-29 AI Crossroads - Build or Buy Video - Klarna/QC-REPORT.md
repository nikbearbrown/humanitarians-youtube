# QC — The Artificial Intelligence Crossroads: Build or Buy? (Klarna case)

## Component QC (standalone renders, before compile)

All 6 illustration beats (B01 KlarnaStatBlock, B02/B04/B05 KlarnaSplitCard,
B03 KlarnaJCurve, B06 KlarnaStatBlock) sampled at 45%/85% of their own
span. All clean on first render: no edge bleed, no collisions, legible,
SAFE margins respected, one terracotta accent per beat.

One defect found and fixed: **B06's on-screen settle line** ("...because
the calibration work got done") repeated the same causal overreach the
narration fact-check had already caught and fixed in B07 — missed
initially because the fact-check audit only checked `narration_text`, not
visual-card prop strings. Fixed to "one year later — the hybrid model
holds" (states the recovery without asserting an unproven cause).
Re-rendered and confirmed. See `FACTCHECK.md` for the full correction log.

## Full master QC (`the-artificial-intelligence-crossroads-klarna.mp4`, 170.0s)

Checked the two most heavily time-conformed beats specifically:
- **B09** (outro): center-cut 8.0s → 5.4s (trimmed 1.3s, the largest cut
  proportionally in this reel). Confirmed the title card, handle, and
  subline all render fully intact — no clipping from the trim.
- **B01**: stretched 1.20x (the most aggressive stretch in this reel, to
  fill a 21.6s audio beat from an 18.0s clip). Confirmed no visual
  distortion — the stat cards and settle line remain crisp and legible at
  the slower pace.

Motion-language note (not a defect, same as the CommBank reel): compile.py
flagged `illustrate` at 60% of beats vs. the ~40% house guideline —
expected, since ILLUSTRATE LAW restricts the Claude UI to bookends only
(B00/B07/B08/B09).

STATUS: zero outstanding BLOCKER/MAJOR defects. First watchable cut is
complete.

## Pacing revision (2026-07-29): transition timing

Author feedback on the first cut: beats cut straight into each other with
no breathing room — "information overload," no time to process one section
before the next started. `compile.py` itself has no transition mechanism
at all (confirmed by reading the script — it's a hard-cut concat, nothing
else), so this needed a separate post-pass.

Two iterations:
1. **v1 — crossfade only (0.3s):** built by chaining `compile.py`'s own
   per-beat conformed clips (video) and per-beat Kokoro narration (audio)
   with `ffmpeg`'s `xfade`/`acrossfade`. Author feedback: crossfade wasn't
   the fix — a dissolve just softens the cut, it doesn't add time to
   process the finished visual.
2. **v2 — hold (0.6s) + longer crossfade (0.5s):** added a genuine fix —
   holding each beat's last frame (+ silence) for a beat before the next
   one starts, so the viewer sees the *completed*, settled visual for a
   moment before anything moves again. Confirmed via frame samples: at the
   hold point the visual is fully static (no more animating); the
   crossfade then dissolves from that settled frame, not a mid-reveal one.
3. **v3 — final: hold only (1.0s), no crossfade.** Author preferred a
   straight hard cut after a longer hold, rather than any dissolve at all.
   Confirmed via frame samples on both sides of the cut: clean static hold
   right up to the cut, then an instant cut into the next beat's own
   opening reveal. Approved as final ("this is perfect").

Total runtime grew from 170.0s (original hard-cut, no pauses) to 186.1s
(final, 1.0s hold before every one of the 10 internal cuts). This
transition pass is **not part of `compile.py`** — it's a separate script
that must be re-run manually if the beat sheet is edited and recompiled.
