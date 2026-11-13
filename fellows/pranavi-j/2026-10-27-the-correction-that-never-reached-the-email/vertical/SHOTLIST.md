# SHOTLIST — The Correction That Never Reached The Email
## Total: 159.61s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.10s | Silent title card: "The Correction That Never Reached The Email" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 17.14s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_IgnoredCorrectionHook (scenes.py) | 19.54s | Two tiles: what the LLM corrected the severity to ("High") vs. what the email still showed ("Critical") — mismatch flagged |
| B03 | SETUP | manim | GRAPHIC | B03_FieldWrittenFieldIgnored (scenes.py) | 27.07s | The real 4 fields `Layer 2 - LLM Re-Score` writes, verbatim, next to the real pre-fix 2-line bucketing from `Generate Email`; the `impact_level` substring flagged gold/crimson in both lines |
| B04 | DISCOVERY-FIX | manim | GRAPHIC | B04_EffectiveImpactDiff (scenes.py) | 19.82s | The real diff from the `Generate Email` node: old 2-line bucketing struck through, `effectiveImpact()` helper + 2 new filter lines added |
| B05 | VERIFICATION | manim | GRAPHIC | B05_HarnessTable (scenes.py) | 29.42s | The real before/after table from this session's own live Node.js harness run: 3 items, per-item bucket before/after, plus `critical_count`/`high_count` totals |
| B06 | HONEST-LIMITS | manim | GRAPHIC | B06_HonestLimits (scenes.py) | 29.83s | 2 honest-limit cards, full weight: (1) only this node's bucketing changed; (2) a separate, unfixed defect found the same week (dashboard stats) |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 11.18s | Statement card: a correction that's computed but never read isn't a correction |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — very short beat, narration is just "Explained with Claude Code." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py` (landscape) and
  `vertical/scenes.py` (native-portrait companion). No pantry stills, no Remotion components, no
  `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`) copied from this
  fellow's closest siblings, `2026-10-20-the-filter-that-didnt-know-its-own-labels` and
  `2026-10-21-calibration-why-confidence-isnt-accuracy` (same fellow, same voice, same series,
  same toolkit version), for house-style consistency.
- Every quoted field name (B03), every quoted code line (B03's pre-fix bucketing, B04's diff — both
  minus and plus sides), and every count/result (B05's harness table) is verbatim from the real
  source files cited in `SOURCES.md`. Nothing paraphrased except the B01/B02/B06/B07 on-screen
  summary/statement cards, which are intentionally shorter restatements of their own spoken
  narration (same convention as every sibling reel).
- B03 and B04 quote genuinely long real lines (the `effectiveImpact()` ternary is one long real
  statement in the actual source). Rather than hand-wrap mid-expression (which would risk
  misquoting), each multi-line code block is composed as a single VGroup and `fit()`-scaled as a
  WHOLE BLOCK to this reel's width budget — preserving the real line breaks exactly as they appear
  in `workflow.dev.json` and relative sizing across the block, documented in `BUILD-LOG.md`.
- B05 shows the full real before/after harness table together, per `FACTCHECK.md` item #6 and the
  Legibility Contract — this session's own run, cross-checked against `C3-VERIFICATION.md`'s
  independently reported counts (both match exactly).
- B06's two honest limits are stated at full weight, neither softened, per `FACTCHECK.md` items
  #7/#8 and house style; the second limit is clearly flagged as a separate, unfixed issue, not
  folded into this video's claim of what C3 actually closed.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats, built for `./art vertical`
— see that file's module docstring for the per-beat side-by-side -> stacked notes.

## QC status
See `BUILD-LOG.md` for GATE A/B/V results and per-beat visual-inspection findings from the render
pipeline.
