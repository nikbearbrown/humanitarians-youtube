# SHOTLIST — The Dashboard That Disagreed With Its Own Alerts
## Total: 144.78s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.10s | Silent title card: "The Dashboard That Disagreed With Its Own Alerts" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 14.28s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_DashboardVsEmailHook (scenes.py) | 17.95s | Two tiles: what the alert email reads (`impact_level`) vs. what the dashboard invents instead (`urgency_score` cutoff) — mismatch flagged |
| B03 | SETUP | manim | GRAPHIC | B03_OneQueryOneColumn (scenes.py) | 24.12s | The real pre-fix `urgency_score`-cutoff SQL, verbatim, next to the real `impact_level` column every other consumer (alert email, feed list, RAG context) already reads; both fields flagged gold/crimson/sage |
| B04 | DISCOVERY-FIX | manim | GRAPHIC | B04_FourLineDiff (scenes.py) | 17.88s | The real diff from `get_stats()`: 4 old `urgency_score` FILTER lines struck through, 4 new `impact_level` FILTER lines added |
| B05 | VERIFICATION | manim | GRAPHIC | B05_HarnessTable (scenes.py) | 24.55s | The real before/after table from this session's own live Python/SQL harness run: 4 tiers (Critical/High/Medium/Low), old vs. new counts, plus the 62/411 (15%) mismatch and the 41-item (30%) High overcount |
| B06 | HONEST-LIMITS | manim | GRAPHIC | B06_HonestLimits (scenes.py) | 29.11s | 2 honest-limit cards, full weight: (1) only this one query changed; (2) verified unwindowed against the full table, not against the endpoint's live rolling windows |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 11.28s | Statement card: a dashboard that re-derives its own answer from a different number isn't measuring the same thing |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — very short beat, narration is just "Explained with Claude Code." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py` (landscape) and
  `vertical/scenes.py` (native-portrait companion). No pantry stills, no Remotion components, no
  `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`) copied from this
  fellow's closest sibling, `2026-10-27-the-correction-that-never-reached-the-email` (same fellow,
  same voice, same series, same toolkit version), for house-style consistency.
- Every quoted SQL line (B03's pre-fix cutoffs, B04's diff — both minus and plus sides) and every
  count/result (B05's harness table) is verbatim from the real source files cited in `SOURCES.md`.
  Nothing paraphrased except the B01/B02/B06/B07 on-screen summary/statement cards, which are
  intentionally shorter restatements of their own spoken narration (same convention as every
  sibling reel).
- B05 shows the full real before/after harness table together, per `FACTCHECK.md` item #4 and the
  Legibility Contract — this session's own run, matching `D1-VERIFICATION.md`'s and `RUN_LOG.md`'s
  independently reported tables exactly.
- B06's two honest limits are stated at full weight, neither softened, per `FACTCHECK.md` items
  #5/#6 and house style; the second limit (unwindowed-only verification) is clearly flagged as an
  open, unresolved caveat, not folded into a claim that the fix is fully verified end-to-end.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats, built for `./art vertical`
— see that file's module docstring for the per-beat side-by-side -> stacked notes.

## QC status
See `BUILD-LOG.md` for GATE A/B/V results and per-beat visual-inspection findings from the render
pipeline.
