# SHOTLIST — vox-heavy-tail-yank

**Title:** Why One Data Point Can Beat Your Thousand-Point Average
**Total beats:** 16 | **Est. duration:** ~2:37 | **Slug:** vox-heavy-tail-yank

---

## Rhythm check

16 beats | ~157s ≈ 2:37 | under 5:00 cap ✓
CARD · GRAPHIC · GRAPHIC · CARD · GRAPHIC · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · COMPOSITE · GRAPHIC · STILL · GRAPHIC · DOCUMENT · GRAPHIC · CARD
Max run: 3 consecutive GRAPHIC (B02–B03 is only 2; B08–B09–B10 but B10=COMPOSITE) ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow; B01_Title |
| B02 | COLD OPEN | GRAPHIC | own | trace | Running average settles — setup |
| B03 | COLD OPEN | GRAPHIC | own | trace | Extreme case yanks the mean — payoff |
| B04 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B05 | THE PROBLEM | GRAPHIC | own | drawon | Gaussian bell — naive expectation |
| B06 | THE PROBLEM | GRAPHIC | own | drawon | Heavy-tail curve — the broken condition |
| B07 | THE PROBLEM | DOCUMENT | own | highlight | Quote: "no matter how many you have already collected" |
| B08 | THE MECHANISM | GRAPHIC | own | trace | Gaussian running mean converges |
| B09 | THE MECHANISM | GRAPHIC | own | trace | Heavy-tail running mean never settles |
| B10 | THE MECHANISM | COMPOSITE | own | compare | Split screen: converges (teal) vs. never settles (crimson) |
| B11 | THE MECHANISM | GRAPHIC | own | drawon | Extreme weight: teal cluster vs. crimson tail dots |
| B12 | THE IMPLICATION | STILL | ai | kenburns | Dashboard plate — stable average, then spike |
| B13 | THE IMPLICATION | GRAPHIC | own | drawon | Bar chart: 99 cheap errors vs. 1 giant outlier |
| B14 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "tail-aware metrics … extreme arrives" |
| B15 | THE EXAMPLE | GRAPHIC | own | accumulate | Document AI: 10 normal docs + 1 outlier → avg yanked to 27s |
| B16 | RECAP | CARD | own | endcard | "Averages converge when extremes are bounded." |

---

## Color semantics
- TEAL = the converging distribution / CLT holds / what works
- CRIMSON = the heavy tail / the lurching mean / the catastrophic outlier
- GOLD = editor's-pen highlight (fill only, never text)
- Never swapped mid-film ✓

## STILL economy
~157s → 1–2 stills allowed (1 per 90s); used: 1 (B12, THE IMPLICATION entry) ✓

## Exclusions honored
- No proof that the Cauchy mean is undefined ✓
- No CLT statement in full ✓
- No confidence-interval formulas ✓
- No power-law taxonomy (wealth/earthquakes list) ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B12 — STILL · ai · kenburns (THE IMPLICATION entry)
The content IS a performance monitoring dashboard showing a stable flat line then a sudden spike at the right edge.
Wrong = abstract network diagram, any image without the visible spike.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=performance+monitoring+chart+spike&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B12-<anything>.jpg`; set `shot.focus` toward the spike.
