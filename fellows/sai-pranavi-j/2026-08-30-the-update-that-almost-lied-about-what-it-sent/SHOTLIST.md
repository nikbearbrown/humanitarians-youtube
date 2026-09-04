# SHOTLIST — The Update That Almost Lied About What It Sent
## Total: 121.46s (measured, 4K 3840x2160) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.05s | Silent title card: "The Update That Almost Lied About What It Sent" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 18.02s | Personal-intro card: name + role + 2-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_MarkEmailSentNode (scenes.py) | 13.44s | The "Mark email sent" Postgres node, isolated, big "?" over its condition |
| B03 | SETUP | manim | GRAPHIC | B03_TwoConditions (scenes.py) | 16.68s | Two condition boxes side by side, legible simultaneously: `urgency_score > 6` (High Priority Filter) vs. old `urgency_score > 7 OR impact_level IN (...)` (Mark email sent) |
| B04 | DISCOVERY | manim | GRAPHIC | B04_ImpactLevelBypass (scenes.py) | 23.52s | `determineImpactLevel()` verbatim, the `isFraud`/`isEnforcement` bypass lines boxed in crimson |
| B05 | PROOF | manim | GRAPHIC | B05_LiveQueryProof (scenes.py) | 21.55s | Live query + count "12" + example row (id 153, SEC insider-trading case) all on screen together |
| B06 | FIX | manim | GRAPHIC | B06_BeforeAfterFix (scenes.py) | 7.97s | Before/after SQL side by side, `id = ANY($1::int[])` highlighted |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 10.61s | "Copying someone else's rule isn't wrong today. It's wrong the day the two drift apart." |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 5.62s | @HumanitariansAI brand card, "in for Sai Pranavi Jeedigunta" |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No
  pantry stills, no Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `fit()`, `panel()`, `clear_of_divider()`,
  `box_around()`) copied from this fellow's 2 sibling reels
  (`2026-07-26-recovering-the-silently-dropped-filings`,
  `2026-08-17-why-ai-generated-code-still-needs-a-human`) for house-style
  consistency.
- Every code/query string on screen (B02/B03/B04/B05/B06) is quoted
  verbatim from `A7-VERIFICATION.md` — see `SOURCES.md`'s claim -> source
  mapping. Nothing is paraphrased.
- B03 and B06 are side-by-side layouts; both use `clear_of_divider()` and
  were verified by measuring real Manim object bounds (not eyeballed) —
  both blocks clear the divider by >1.4 units on each side, no glyph
  crossing (see BUILD-LOG.md for the measured numbers).

## QC status
See `BUILD-LOG.md` for GATE A/W/V results once the render pipeline has run.
