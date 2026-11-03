# SHOTLIST — The Link That Pointed Nowhere
## Total: 160.99s (measured audio, before final-frame rounding) · 10 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.05s | Silent title card: "The Link That Pointed Nowhere" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 17.18s | Personal-intro card: name + role + 3-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_DeadEndLinkHook (scenes.py) | 10.78s | Feed item card, a stored link, a click animation landing back on "Google News — not the article" |
| B03 | SETUP | manim | GRAPHIC | B03_RegexVsRealLink (scenes.py) | 18.82s | The failing regex `link.match(/url=([^&]+)/)` shown verbatim next to a real modern link `news.google.com/rss/articles/<opaque-id>?oc=5`, missing `url=` param boxed and labeled absent |
| B04 | DISCOVERY | manim | GRAPHIC | B04_ResolutionFlowDiagram (scenes.py) | 19.73s | 4-step flow: redirect page -> id/timestamp/signature -> POST to internal endpoint -> real URL, with a full-width legible caveat: "reverse-engineered — not a documented/official API" |
| B05 | NEAR-MISS | manim | GRAPHIC | B05_OrderingNearMiss (scenes.py) | 28.66s | Two call-order diagrams side by side: OLD ORDER (classify AFTER unwrap, breaks once fix ships) vs. FIXED ORDER (classify on rawLink BEFORE unwrap) |
| B06 | PROOF | manim | GRAPHIC | B06_ThreeRoundProof (scenes.py) | 23.54s | All 3 escalating verification rounds (20/20 script, 16/16 exact code ported, 6/6 real node live run) plus the final round's 6 real resolved domains and the "all 6 still correctly labeled" line |
| B07 | HONEST-LIMITS | manim | GRAPHIC | B07_HonestLimits (scenes.py) | 24.58s | Two limitation cards at full weight, side by side ("not yet verified on live n8n" / "~400 extra requests/run, by design, not parallelized"), plus the visibility log-line format |
| B08 | TAKEAWAY | manim | GRAPHIC | B08_Statement (scenes.py) | 7.87s | "A fix that works today isn't finished." |
| B09 | SIGN-OFF | manim | GRAPHIC | B09_BrandOutro (scenes.py) | 5.78s | @HumanitariansAI brand card, "fixed with Claude Code", "in for Sai Pranavi J." |

## Lane summary
- MANIM: all 10 beats, self-contained in this reel's own `scenes.py`. No
  pantry stills, no Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `fit()`, `panel()`, `clear_of_divider()`,
  `box_around()`) copied from this fellow's closest sibling reel
  `2026-09-07-the-synonyms-the-classifier-never-learned` (same genre, same
  fellow, same voice) for house-style consistency.
- Every quoted string on screen (B03's regex/link, B04's flow steps and
  caveat, B05's call orders, B06's round counts and 6 resolved domains, B07's
  two limitations and log-line format) is verbatim from
  `/Users/pranavijs/mycroft/scripts/regulatory-intel/B3-VERIFICATION.md` —
  see `SOURCES.md`'s claim -> source mapping. Nothing paraphrased.
- B05 and B07 are this reel's side-by-side beats; both use
  `clear_of_divider()` and are verified by measuring real Manim object
  bounds (not eyeballed).
- B04's caveat label is a FACTCHECK-required element (item #1, resolved):
  full-width, high-contrast, held on screen for the whole beat.
- B06 shows all 3 rounds, not just the strongest (FACTCHECK/SOURCES row 4).
- B07's two limitations are shown at full weight, side by side, neither
  softened or omitted (FACTCHECK.md resolution for this beat).

## Vertical companion
`vertical/SHOTLIST.md` documents the native-portrait redesign of all 10
beats built via `./art vertical` — see that file for the per-beat
top/bottom-stack notes for B05 and B07 (this reel's side-by-side beats).

## QC status
See `BUILD-LOG.md` for GATE A/W/B/V results once the render pipeline has run.
