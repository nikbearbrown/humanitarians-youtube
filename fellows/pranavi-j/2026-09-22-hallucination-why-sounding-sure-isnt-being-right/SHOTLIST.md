# SHOTLIST — Hallucination: Why Sounding Sure Isn't the Same as Being Right
## Total: 142.22s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.06s | Silent title card: "Hallucination: Why Sounding Sure Isn't the Same as Being Right" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 13.10s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_SameToneHook (scenes.py) | 12.50s | Two identically-styled confident answer bubbles, unlabeled, then revealed "REAL" / "FABRICATED" |
| B03 | FRAMEWORK | manim | GRAPHIC | B03_ThreeQuestionsFramework (scenes.py) | 25.75s | All 3 rubric questions shown together before any example: Checkable? / Would it hedge? / Confidence tracks difficulty? |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_FabricatedVsRealCitation (scenes.py) | 25.58s | Two generic citations, identical fluent styling, side by side; "CHECKABLE?" callout resolves one "VERIFIED" and one "DOESN'T EXIST" |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_TrueFactFalsifiability (scenes.py) | 25.42s | Same confident tone, genuinely true/easy fact (boiling point of water); all 3 rubric checks resolve CONFIRMED (sage), visually distinct from B04's failed case |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | B06_AuditChecklist (scenes.py) | 23.16s | The 3 questions restated as an actionable checklist card (checkboxes), distinct from B03's rubric card |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 11.14s | Statement card: tone is generated the same way whether right or wrong; the only question that matters is checkability |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — short card matching this beat's short approved narration |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No
  pantry stills, no Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`)
  copied from this fellow's closest siblings
  `2026-09-29-the-keyword-that-cried-wolf` and
  `2026-09-22-the-all-clear-that-wasnt-all-there` (same fellow, same voice,
  same series) for house-style consistency.
- This is a general AI/STEM topic explainer, not a report of real engineering
  work — B04's fabricated/real citation pair and B05's falsifiability case
  are both fully generic/hypothetical, with no resemblance to any real
  paper, model, or vendor (see FACTCHECK.md, SOURCES.md).
- B04 is this reel's most legibility-critical beat: both citations are shown
  in identical fluent styling first (the whole point is they're
  indistinguishable by tone alone), then one resolves "VERIFIED" and the
  other "DOESN'T EXIST".
- B05 stress-tests the rubric against a naive "confident tone = hallucination"
  over-trigger — same fluent tone as B04, but a genuinely true and easy
  case, with a visibly distinct (sage/CONFIRMED) resolution.
- B06's checklist is a concrete action (checkboxes, distinct composition),
  not a second copy of B03's rubric card.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats,
built for `./art vertical` — see that file's module docstring for the
per-beat side-by-side -> stacked notes (B02, B04, B05's side-by-side/row
layouts restacked for the narrow canvas).

## QC status
See `BUILD-LOG.md` for GATE A/V results and per-beat visual-inspection
findings from the render pipeline.
