# SHOTLIST — The Keyword That Cried Wolf
## Total: 135.353s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.049s | Silent title card: "The Keyword That Cried Wolf" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 14.904s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_TwoMisfiresHook (scenes.py) | 13.56s | Two real title cards side by side, stamped "10/CRITICAL" and "9/CRITICAL" |
| B03 | SETUP | manim | GRAPHIC | B03_ScoringRuleVerbatim (scenes.py) | 11.472s | The real scoring rule quoted verbatim: `if (text.includes('immediate') \|\| text.includes('emergency')) score += 3;` |
| B04 | DISCOVERY | manim | GRAPHIC | B04_WordInContext (scenes.py) | 23.208s | Both real titles, trigger word alone vs. the same word highlighted in its real context, side by side |
| B05 | FIX | manim | GRAPHIC | B05_FailOpenFlowDiagram (scenes.py) | 25.608s | Flow diagram: item -> local model review -> confirm/downgrade, plus explicit 3rd branch "model fails -> goes through anyway (fail-open)" |
| B06 | PROOF | manim | GRAPHIC | B06_ThreeCaseResultsTable (scenes.py) | 18.48s | 3-row results table, all 3 cases visible together: Medicare (downgrade), Nasdaq (downgrade), SEC (untouched, "not reviewed — below alert threshold") |
| B07 | HONEST-LIMITS | manim | GRAPHIC | B07_HonestLimitsCards (scenes.py) | 18.528s | 3 limitation cards at full weight: conservative correction (High, not Medium/Low), small sample (2 patterns), real added latency |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 5.544s | @HumanitariansAI brand card, "fixed with Claude Code", "in for Sai Pranavi J." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No
  pantry stills, no Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`,
  `clear_of_divider()`, `box_around()`, `inline_highlight()`) copied from
  this fellow's closest siblings
  `2026-09-14-rag-why-looking-it-up-isnt-enough` and
  `2026-09-14-b3-the-link-that-pointed-nowhere` (same fellow, same voice,
  same series) for house-style consistency.
- Every quoted string on screen (B03's scoring rule, B04's two real titles
  and trigger-word contexts, B05's fail-open branch wording, B06's 3-case
  table, B07's 3 limitations) is verbatim from
  `/Users/pranavijs/mycroft/scripts/regulatory-intel/C2-VERIFICATION.md` —
  see `SOURCES.md`'s claim -> source mapping. Nothing paraphrased.
- B04 is this reel's most legibility-critical beat: the trigger word is
  shown ALONE first (as the keyword scorer effectively "sees" it), then in
  its real, harmless context — both real titles, side by side.
- B05 explicitly shows the fail-open branch as its own reveal (not bundled
  silently with confirm/downgrade) — this reel's single most
  safety-critical visual element per `FACTCHECK.md`/`BEAT-SHEET.md`'s
  Legibility Contract.
- B06 shows all 3 outcomes together (not sequential reveals that hide the
  comparison), with the SEC row's label per `FACTCHECK.md` item #1
  (resolved): "not reviewed — below alert threshold", never implying it was
  reviewed-and-approved.
- B07's 3 limitations are shown at full weight, none softened or omitted
  (`FACTCHECK.md` resolution for this beat).

## Vertical companion
`vertical/SHOTLIST.md` documents the native-portrait redesign of all 9
beats built via `./art vertical` — see that file for the per-beat
side-by-side -> stacked notes for B04, B05 and B06 (this reel's
side-by-side/multi-branch beats).

## QC status
See `BUILD-LOG.md` for GATE A/W/V results and per-beat visual-inspection
findings once the render pipeline has run.
