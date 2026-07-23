# SHOTLIST — polynomial-factoring

**Slug**: polynomial-factoring  
**Style**: CLI / NikBearBrown  
**Palette**: teardown  
**Aspect**: 16:9  
**Total beats**: 10  
**Color law**: CRIMSON for the key factored results and branching paths. INK for decision nodes. SLATE for secondary step labels. GOLD box for final answer.

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
Props: topic="COLLEGE ALGEBRA", lines=["Nik Bear Brown", "Polynomial Factoring", "The decision tree that replaces guessing"]

**B02** — NikBearBrownTerminalAsk  
command: `claude "write a Manim scene showing the polynomial factoring decision tree: check GCF → count terms → if 2 terms check difference of squares → if 3 terms use ac method or simple trinomial strategy"`  
runningText: "generating decision tree..."

**B03** — NikBearBrownCodeBlock  
filename: `factoring_tree.py`  
Code: factor_strategy() function returning 3-step list based on term count.

**B05** — NikBearBrownTerminalAsk  
command: `claude "add a worked example tracing x^2+5x+6 through the tree step by step"`  
runningText: "adding worked example..."

**B09** — NikBearBrownOutro

---

## Manim beats

**B04** — `B04_FactoringTree` in `vox_scenes.py`  
Top-to-bottom decision tree: GCF node → terms node → 2-term branch (diff of squares, CRIMSON) → 3-term branch (trinomial, CRIMSON) → (x+p)(x+q) leaf. RoundedRectangles with GrowArrow connectors.

**B06** — `B06_FactoringExample` in `vox_scenes.py`  
6 steps for x²+5x+6: GCF=none, trinomial strategy, p·q=6 p+q=5, pairs check, answer (x+2)(x+3), check expansion. GOLD box with CRIMSON label at bottom.

---

## Slate beats

**B01** — Hold. Narration: trial-and-error vs. systematic tree.  
**B07** — Hold. Narration: tree makes implicit explicit; GCF always first.  
**B08** — Hold. Narration: 4-term grouping practice exercise.
