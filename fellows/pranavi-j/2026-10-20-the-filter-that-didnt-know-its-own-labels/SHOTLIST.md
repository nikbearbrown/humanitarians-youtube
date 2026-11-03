# SHOTLIST — The Filter That Didn't Know Its Own Labels
## Total: 142.79s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.05s | Silent title card: "The Filter That Didn't Know Its Own Labels" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 15.02s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_SixthLabelHook (scenes.py) | 12.24s | "5" fixed labels vs "+1" dynamic label, built live — the fixed-enum/dynamic-classifier mismatch |
| B03 | SETUP | manim | GRAPHIC | B03_EnumVsClassifier (scenes.py) | 23.98s | The real 5-value `SourceFeed` enum shown verbatim, next to the real `identifySource()` template string that builds a 6th kind of label; the template literal flagged gold/crimson via character-index slicing (no paraphrase) |
| B04 | DISCOVERY-FIX | manim | GRAPHIC | B04_TwoLineDiff (scenes.py) | 22.13s | The real 2-line diff from commit `565e84e` (param type widened, `.value` accessor dropped), struck-through before/after pairs |
| B05 | VERIFICATION | manim | GRAPHIC | B05_TestClientTable (scenes.py) | 27.12s | The real before/after FastAPI TestClient table (dynamic label: 422 -> 200; fixed label: 200 -> 200, unchanged) from this session's own live verification run |
| B06 | HONEST-LIMITS | manim | GRAPHIC | B06_HonestLimits (scenes.py) | 26.83s | 2 honest-limit cards, full weight: (1) a latent gap, not an observed incident; (2) the database layer was mocked, not live |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 9.91s | Statement card: when a classifier gets smarter, every consumer of its output has to keep up |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — very short beat, narration is just "Explained with Claude Code." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py` (landscape)
  and `vertical/scenes.py` (native-portrait companion). No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`)
  copied from this fellow's closest sibling,
  `2026-10-15-the-alert-that-waited-for-a-second-item` (same fellow, same
  voice, same series, same toolkit version), for house-style consistency.
- Every quoted enum value (B03), every quoted code line (B03's
  `identifySource()` template, B04's diff) and every status code/result
  (B05's TestClient table) is verbatim from the real source files cited in
  `SOURCES.md`. Nothing paraphrased except the B01/B02/B06/B07 on-screen
  summary/statement cards, which are intentionally shorter restatements of
  their own spoken narration (same convention as every sibling reel's
  exec-summary/hook/statement beats).
- B03 is this reel's most legibility-critical beat: the real 5-value enum and
  the real `identifySource()` dynamic-label branch are both shown in full
  (not paraphrased), with the exact template-literal substring isolated via
  Manim `Text` character-index slicing and boxed — per `FACTCHECK.md` items
  #1/#2 and the Legibility Contract.
- B04's diff matches the real committed fix exactly (`565e84e`), per
  `FACTCHECK.md` item #3.
- B05 shows the full real before/after TestClient table together, per
  `FACTCHECK.md` item #5 and the Legibility Contract.
- B06's two honest limits are stated at full weight, neither softened, per
  `FACTCHECK.md` items #6/#7 and house style.

## Vertical companion
`vertical/scenes.py` documents the native-portrait redesign of all 9 beats
built via `./art vertical` — parent's side-by-side panels (B02's 2-tile row,
B03's enum/code panel row, B05's 2-card row, B06's 2-card row) each become a
single stacked column; B03's and B04's code lines are re-wrapped across
more/narrower lines where needed (same verbatim substrings).

## QC status
See `BUILD-LOG.md` for GATE A/B/V results and per-beat visual-inspection
findings once the render pipeline has run.
