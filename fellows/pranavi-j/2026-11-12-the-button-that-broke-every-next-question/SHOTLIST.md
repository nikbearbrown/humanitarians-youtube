# SHOTLIST — The Button That Broke Every Next Question
## Total: 154.34s measured Kokoro audio (B00 silent) / 154.541667s final render · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.10s | Silent title card: "The Button That Broke Every Next Question" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 14.06s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_CapVsNoCapHook (scenes.py) | 15.34s | Two tiles: the backend's real 10-feed cap vs. Select All's real pre-fix "no cap" code — mismatch flagged |
| B03 | SETUP | manim | GRAPHIC | B03_TwoBugsOneClick (scenes.py) | 28.73s | The real pre-fix `handleSelectAll`/`handleToggle`, the real backend `List[int] = Field(min_items=1, max_items=10)` field, and the real pre-fix generic error line, all verbatim |
| B04 | DISCOVERY-FIX | manim | GRAPHIC | B04_CapAndRealReason (scenes.py) | 18.38s | The real diff: `MAX_SELECTABLE_FEEDS = 10` added and both selection paths capped in `App.jsx`; the real detail-extraction block added to `ChatInterface.jsx` |
| B05 | VERIFICATION | manim | GRAPHIC | B05_HarnessTable (scenes.py) | 29.59s | The real before/after table from this session's own live Node harness run: 5 checks, 7 assertions, the real captured 422 message text |
| B06 | HONEST-LIMITS | manim | GRAPHIC | B06_HonestLimits (scenes.py) | 29.14s | 2 honest-limit cards, full weight: (1) no `vite build`/browser end-to-end check; (2) no UI indicator added once the cap is reached |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 13.49s | Statement card: the most obvious button needs to respect the system's real limits; showing the real reason turns an outage into something fixable |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — very short beat |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py` (landscape) and
  `vertical/scenes.py` (native-portrait companion). No pantry stills, no Remotion components, no
  `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`) copied from this
  fellow's closest sibling, `2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts` (same
  fellow, same voice, same series, same toolkit version), for house-style consistency.
- Every quoted code line (B02/B03's pre-fix selection/error logic, B04's diff — both minus and plus
  sides) and every count/result (B05's harness table) is verbatim from the real source files cited
  in `SOURCES.md`. Nothing paraphrased except the B01/B02/B06/B07 on-screen summary/statement cards,
  which are intentionally shorter restatements of their own spoken narration (same convention as
  every sibling reel).
- B05 shows the full real before/after harness table together, per `FACTCHECK.md` item #7 and the
  Legibility Contract — this session's own run, matching `E1-VERIFICATION.md`'s and `RUN_LOG.md`'s
  independently reported results exactly, including the real captured 422 message text.
- B06's two honest limits are stated at full weight, neither softened, per `FACTCHECK.md` items
  #8/#9 and house style.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats, built for `./art vertical`
— see that file's module docstring for the per-beat side-by-side -> stacked notes.

## QC status
See `BUILD-LOG.md` for GATE A/B/V results and per-beat visual-inspection findings from the render
pipeline.
