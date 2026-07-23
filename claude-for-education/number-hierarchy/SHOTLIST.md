# SHOTLIST — number-hierarchy

**Slug**: number-hierarchy  
**Style**: CLI / NikBearBrown  
**Palette**: teardown  
**Aspect**: 16:9  
**Total beats**: 10  
**Color law**: CRIMSON for the first two sets (ℕ, ℤ), INK for the middle two (ℚ, ℝ), SLATE for ℂ. CRIMSON for irrational/complex callouts.

---

## Beat inventory

| Beat | Act | Type | Source | Motion | Duration |
|------|-----|------|--------|--------|----------|
| B00 | INTRO | GRAPHIC | remotion | fade | 8s |
| B01 | PROBLEM | CARD | null (slate) | hold | 18s |
| B02 | ASK | GRAPHIC | remotion | fade | 12s |
| B03 | CODE | GRAPHIC | remotion | fade | 14s |
| B04 | OUTPUT | GRAPHIC | manim | fade | 20s |
| B05 | CHANGE | GRAPHIC | remotion | fade | 10s |
| B06 | OUTPUT | GRAPHIC | manim | fade | 14s |
| B07 | SUMMARY | CARD | null (slate) | hold | 12s |
| B08 | NEXT STEPS | CARD | null (slate) | hold | 10s |
| B09 | OUTRO | GRAPHIC | remotion | fade | 10s |

---

## Remotion beats

**B00** — NikBearBrownOpen  
Pattern: `NikBearBrownOpen`  
Props: topic="COLLEGE ALGEBRA", lines=["Nik Bear Brown", "The Number Hierarchy", "Every number you will ever need"]

**B02** — NikBearBrownTerminalAsk  
Pattern: `NikBearBrownTerminalAsk`  
command: `claude "write a Manim scene showing the number set hierarchy: N ⊂ Z ⊂ Q ⊂ R ⊂ C as nested boxes with labeled examples of each set"`  
runningText: "generating hierarchy..."

**B03** — NikBearBrownCodeBlock  
Pattern: `NikBearBrownCodeBlock`  
filename: `number_sets.py`  
Code: SETS list with 5 tuples, comment: "draws 5 nested boxes, left to right, with arrows"

**B05** — NikBearBrownTerminalAsk  
command: `claude "add one example number in each set ring showing exactly which rings it belongs to: use 3, -2, 1/2, pi, and sqrt(-1)"`  
runningText: "adding examples..."

**B09** — NikBearBrownOutro  
Pattern: `NikBearBrownOutro`

---

## Manim beats

**B04** — `B04_NumberHierarchy` in `vox_scenes.py`  
5 boxes left to right: ℕ, ℤ, ℚ, ℝ, ℂ. GrowFromCenter each box, FadeIn labels, GrowArrow between adjacent sets. Subtitle confirms total nesting.

**B06** — `B06_NumberHierarchy2` in `vox_scenes.py`  
5 rows: number, GrowArrow, membership string. Numbers: 3, −2, ½, π, √−1. π and √−1 in CRIMSON. Note at bottom about irrationality.

---

## Slate beats

**B01** — Hold slate. Narration: nested structure, operations safety.  
**B07** — Hold slate. Narration: nesting is total, direction doesn't hold downward.  
**B08** — Hold slate. Narration: classify 5 numbers, verify rational as p/q.
