# SHOTLIST — The Check That Never Once Fired
## Total: 133.57s (measured, 4K 3840x2160) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.05s | Silent title card: "The Check That Never Once Fired" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 18.98s | Personal-intro card: name + role + 3-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_ZeroMatchesHook (scenes.py) | 11.38s | The CFTC-detection condition, quoted verbatim, boxed teal, red "0 MATCHES" stamp below |
| B03 | SETUP | manim | GRAPHIC | B03_ClassifierCondition (scenes.py) | 19.32s | The full `federalregister.gov` branch quoted verbatim; the two checks (teal) and the default (crimson) both highlighted |
| B04 | DISCOVERY | manim | GRAPHIC | B04_RealFilingVsCondition (scenes.py) | 19.66s | Real CFTC filing title/link (pulled live) side by side with the two checks, both marked ABSENT |
| B05 | PROOF | manim | GRAPHIC | B05_FiveFeedResultsTable (scenes.py) | 29.42s | All 5 live-feed rows: CFTC 12/12, term-search 83/146, SEC/FINRA/Investment-Advisor 0 changed; CFTC row (gold) and zero-regression rows (teal) boxed |
| B06 | FIX | manim | GRAPHIC | B06_BeforeAfterClassifier (scenes.py) | 13.94s | Before/after `identifySource()` branch side by side, the new `dc:creator`-based checks highlighted gold |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 10.56s | "A safeguard that's never once tested against real input isn't protecting anything." |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 6.26s | @HumanitariansAI brand card, "in for Sai Pranavi Jeedigunta" |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No
  pantry stills, no Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `fit()`, `panel()`, `clear_of_divider()`,
  `box_around()`) copied from this fellow's sibling reel
  `2026-08-30-the-update-that-almost-lied-about-what-it-sent` for
  house-style consistency (part 2 of the same Layer-1-hardening pair).
- Every code string on screen (B02/B03/B04/B06) is quoted verbatim from
  `B2-VERIFICATION.md` and the pre-fix/post-fix `workflow.dev.json`
  (commit `d59fbd5`) — see `SOURCES.md`'s claim -> source mapping. B06's
  AFTER panel condenses the untouched SEC/FINRA branches into one footer
  line for screen space; the dc:creator mechanism itself is verbatim.
- B04 is this reel's side-by-side beat; uses `clear_of_divider()` and is
  verified by measuring real Manim object bounds (not eyeballed). B06 also
  uses it as a second precaution.

## QC status
See `BUILD-LOG.md` for GATE A/W/B/V results once the render pipeline has run.
