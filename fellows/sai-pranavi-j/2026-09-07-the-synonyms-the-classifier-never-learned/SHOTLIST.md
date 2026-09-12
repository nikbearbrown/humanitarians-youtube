# SHOTLIST — The Synonyms the Classifier Never Learned
## Total: 131.60s (measured, 4K 3840x2160) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.05s | Silent title card: "The Synonyms the Classifier Never Learned" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 15.02s | Personal-intro card: name + role + 3-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_UnknownSourceHook (scenes.py) | 9.98s | 18-cell feed grid + red "18 -> UNKNOWN SOURCE" stamp |
| B03 | SETUP | manim | GRAPHIC | B03_FieldComparison (scenes.py) | 21.67s | Side-by-side: Federal Register's `dc:creator` (populated) vs. Google News's `<source>` (a law firm, "Mayer Brown") |
| B04 | DISCOVERY | manim | GRAPHIC | B04_TwoGroups (scenes.py) | 25.25s | Two real title examples side by side: recoverable ("Exempt Reporting Advisers") vs. not recoverable ("FCA Decision Notice...", UK regulator) |
| B05 | FIX-PROOF | manim | GRAPHIC | B05_FixAndProofTable (scenes.py) | 22.70s | All 5 live-feed rows (Federal Register-Securities 146/0/0, CFTC 12/0/0, SEC 25/0/0, FINRA 100/6/4, Investment Advisor 100/12/4); FINRA/Investment Advisor rows and the 18->8 total boxed |
| B06 | HONEST-LIMIT | manim | GRAPHIC | B06_HonestLimit (scenes.py) | 20.69s | The 2 remaining-failure categories (no named regulator; out-of-scope regulator) named, one real example title each; framed "LEFT OPEN -- BY DESIGN" |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 8.02s | "Not every fix should chase a hundred percent." |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 4.22s | @HumanitariansAI brand card, "in for Sai Pranavi Jeedigunta" |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No
  pantry stills, no Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `fit()`, `panel()`, `clear_of_divider()`,
  `box_around()`) copied from this fellow's closest sibling reel
  `2026-08-30-the-check-that-never-once-fired` (part 3 of the same
  Layer-1-hardening series; this reel is part 4) for house-style
  consistency.
- Every quoted string on screen (B03's XML fields, B04's two titles, B05's
  5-feed table, B06's two example titles) is verbatim from
  `/Users/pranavijs/mycroft/scripts/regulatory-intel/UNKNOWN-SOURCE-INVESTIGATION.md`
  — see `SOURCES.md`'s claim -> source mapping. Nothing paraphrased.
- B03 and B04 are this reel's side-by-side beats; both use
  `clear_of_divider()` and are verified by measuring real Manim object
  bounds (not eyeballed).
- B06's framing is FACTCHECK-locked (row #5): a deliberate, reasoned
  stopping point, never an unsolved bug or a "coming soon" promise.

## QC status
See `BUILD-LOG.md` for GATE A/W/B/V results once the render pipeline has run.
