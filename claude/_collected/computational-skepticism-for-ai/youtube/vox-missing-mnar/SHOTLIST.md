# SHOTLIST — vox-missing-mnar

## Rhythm check
13 beats | measured ~183s ≈ 3:03 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · DOCUMENT · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow; B01_Title |
| B02 | COLD OPEN | GRAPHIC | own | decay | Income survey: 18% of income fields blank |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | Three kinds of missing (plain-language, no MCAR/MAR vocab) |
| B05 | THE PROBLEM | GRAPHIC | own | trace | MNAR looks exactly like the benign kinds |
| B06 | THE MECHANISM | STILL | ai | kenburns | Slate — spreadsheet, top-income cells blank (see PROMPTS.md) |
| B07 | THE MECHANISM | GRAPHIC | own | decay | Imputing with the visible mean drags the estimate down |
| B08 | THE MECHANISM | DOCUMENT | own | highlight | "probability of being missing depends on the value itself" |
| B09 | THE IMPLICATION | GRAPHIC | own | compare | Standard EDA can't detect it — patterns look identical |
| B10 | THE IMPLICATION | DOCUMENT | own | highlight | "who would not report this, and why?" |
| B11 | THE IMPLICATION | GRAPHIC | own | trace | The per-column question standard tools never ask |
| B12 | THE EXAMPLE | GRAPHIC | own | accumulate | Clinical trial: 43 dropouts (severe effects) missing → result too optimistic |
| B13 | RECAP | CARD | own | endcard | "The visible distribution silently lies." |

## Color semantics
- TEAL = present / visible data
- CRIMSON = missing / the gap
- GOLD = the key insight / the direction of bias
- SLATE = the imputed values / naive fix
- Never swapped mid-film ✓

## STILL economy
~165s → 1–2 stills allowed (1 per 90s); used: 1 (B06, act boundary into THE MECHANISM) ✓

## Exclusions honored
- No MCAR/MAR formal definitions ✓ (B04 is plain-language)
- No imputation-method catalog ✓ (B07 shows one naive mean-fill only)
- No missingno tooling ✓
- No join-failure case ✓ (that's vox-silent-join's film)

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS the pattern: blanks concentrated at the TOP of the income
column — wrong = blanks scattered randomly, or a generic "spreadsheet" stock
look. Real-asset alternatives (unlikely to beat a generated one, but check):
- https://commons.wikimedia.org/w/index.php?search=census+income+survey+form&title=Special:MediaSearch&type=image
- https://www.loc.gov/photos/?q=census+enumeration+income
Drop the result in `pantry/` as `B06-<anything>.png`; set `shot.focus` toward
the blank upper cells after intake.
