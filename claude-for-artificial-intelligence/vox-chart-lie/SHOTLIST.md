# SHOTLIST — vox-chart-lie

## Rhythm check
13 beats | estimated ~175s ≈ 2:55 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · DOCUMENT · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow |
| B02 | COLD OPEN | GRAPHIC | own | morph | Honest bar chart: 55% vs 48%, zero baseline, equal colors, error bars |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | morph | Move 1: truncated axis — 7pt gap looks like a wall |
| B05 | THE PROBLEM | GRAPHIC | own | morph | Move 2: color asymmetry — green vs gray directs attention |
| B06 | THE MECHANISM | STILL | ai | kenburns | Slate — presenter gesturing at highlighted bars (see PROMPTS.md) |
| B07 | THE MECHANISM | GRAPHIC | own | morph | Move 3: remove error bars — overlapping CIs hidden |
| B08 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "visualization is not transparent communication…argument" |
| B09 | THE IMPLICATION | GRAPHIC | own | morph | Before/after all three moves: same CSV, different conclusion |
| B10 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "the choice is the difference — not anything visible in the pixels" |
| B11 | THE IMPLICATION | GRAPHIC | own | trace | Catalog: truncation / color asymmetry / selective uncertainty |
| B12 | THE EXAMPLE | GRAPHIC | own | compare | Retention chart: 81→87% on zero baseline (modest) vs truncated axis (wall) |
| B13 | RECAP | CARD | own | endcard | "Same data. Same CSV. Structural choices were the argument." |

## Color semantics
- TEAL = honest encoding / correct choice / zero baseline
- CRIMSON = misleading encoding / truncated axis / exaggerated effect
- GOLD = the structural choice / the argument
- SLATE = neutral/gray bars / de-emphasized data
- Never swapped mid-film ✓

## STILL economy
~175s → 1–2 stills allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- Only three catalog items (truncation, color asymmetry, hidden uncertainty) ✓
- No axis-inversion Reuters case ✓
- No FT question taxonomy ✓
- No Cleveland-McGill perception research ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS a presenter gesturing at highlighted bars in a chart.
Wrong = abstract data visualization without a human presenter, any chart without highlighted bars.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=bar+chart+presentation+screen&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B06-<anything>.jpg`; set `shot.focus` toward
the highlighted bars and presenter gesture after intake.
