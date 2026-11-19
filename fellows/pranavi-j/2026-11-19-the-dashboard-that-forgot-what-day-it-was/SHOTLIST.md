# SHOTLIST — The Dashboard That Forgot What Day It Was
## Total: 149.69s measured Kokoro audio (B00 silent) / 149.833333s final render · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.10s | Silent title card: "The Dashboard That Forgot What Day It Was" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 16.51s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_StaleWindowHook (scenes.py) | 17.64s | Fixture date range (Jul 14-24, 2026) vs. today (Nov 19, 2026) vs. the pre-fix 7-day window — the arithmetic that guarantees zero rows |
| B03 | SETUP | manim | GRAPHIC | B03_TwoPanelsDisagree (scenes.py) | 24.17s | The real pre-fix `WHERE created_at >= NOW() - INTERVAL '7 days'` clause, the real `Stats.jsx` card labels with the real resulting 0/0 values, and the real unwindowed `list_feeds`/`App.jsx` `limit: 100` fetch, all verbatim |
| B04 | DISCOVERY-FIX | manim | GRAPHIC | B04_OneLineFix (scenes.py) | 24.84s | The real one-line diff removing the `WHERE` clause; `source_distribution`'s 30-day window and `recent_activity`'s 14-day window shown as deliberately kept |
| B05 | VERIFICATION | manim | GRAPHIC | B05_LiveQueryTable (scenes.py) | 25.37s | The real before/after table from this session's own live Postgres query run: 0/0/0/0 -> 33/98/280/0, plus the 24 Critical/8 High top-100 slice |
| B06 | HONEST-LIMITS | manim | GRAPHIC | B06_HonestLimits (scenes.py) | 25.49s | 2 honest-limit cards, full weight: (1) `source_distribution`'s own unaddressed 30-day window; (2) no live browser/frontend session this round |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 10.06s | Statement card: a dashboard's summary is only as honest as the window it looks through |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — very short beat |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py` (landscape) and
  `vertical/scenes.py` (native-portrait companion). No pantry stills, no Remotion components, no
  `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`) copied from this
  fellow's closest siblings, `2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts` and
  `2026-11-12-the-button-that-broke-every-next-question` (same fellow, same voice, same series,
  same toolkit version), for house-style consistency.
- Every quoted code line (B02/B03's real dates, `WHERE` clause, `Stats.jsx` labels; B04's diff) and
  every count/result (B05's live-query table) is verbatim from the real source files cited in
  `SOURCES.md`. Nothing paraphrased except the B01/B02/B06/B07 on-screen summary/statement cards,
  which are intentionally shorter restatements of their own spoken narration (same convention as
  every sibling reel).
- B05 shows the full real before/after live-DB query table together, per `FACTCHECK.md` item #6
  and the Legibility Contract — this session's own query run, matching `F1-VERIFICATION.md`'s
  reported numbers exactly (0/0/0/0 -> 33/98/280/0), plus the independently replicated 24
  Critical/8 High top-100 slice.
- B06's two honest limits are stated at full weight, neither softened, per `FACTCHECK.md` items
  #8/#9 and house style.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats, built for `./art vertical`
— see that file's module docstring for the per-beat side-by-side -> stacked notes.

## QC status
See `BUILD-LOG.md` for GATE A/B/V results and per-beat visual-inspection findings from the render
pipeline.
