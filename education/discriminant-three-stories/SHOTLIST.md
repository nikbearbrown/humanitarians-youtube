# SHOTLIST — discriminant-three-stories

**Slug**: discriminant-three-stories  
**Style**: CLI / NikBearBrown  
**Palette**: teardown  
**Aspect**: 16:9  
**Total beats**: 10  
**Color law**: CRIMSON for Δ>0 parabola and the Δ>0 case label. INK for Δ=0 parabola. SLATE for Δ<0 parabola. GOLD box for discriminant highlight in formula. CRIMSON for all discriminant labels.

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
Props: topic="COLLEGE ALGEBRA", lines=["Nik Bear Brown", "The Discriminant", "Three parabolas, three stories"]

**B02** — NikBearBrownTerminalAsk  
command: `claude "write a Manim scene showing three parabolas side by side: one with discriminant>0 (2 roots), one with discriminant=0 (1 root), one with discriminant<0 (0 real roots), and show the discriminant value below each"`  
runningText: "generating three parabolas..."

**B03** — NikBearBrownCodeBlock  
filename: `discriminant_plots.py`  
Code: 3 cases list with (a,b,c,desc) tuples and discriminant computed.

**B05** — NikBearBrownTerminalAsk  
command: `claude "add the quadratic formula with the discriminant highlighted and arrow pointing to each case"`  
runningText: "adding formula callout..."

**B09** — NikBearBrownOutro

---

## Manim beats

**B04** — `B04_DiscriminantThree` in `vox_scenes.py`  
Three mini Axes side by side at x=−4.5, 0, +4.5. Each plots its parabola (CRIMSON / INK / SLATE). D label below each. Three parabolas created in sequence.

**B06** — `B06_DiscriminantFormula` in `vox_scenes.py`  
Quadratic formula at top (INK bold). GOLD box highlights b²−4ac with CRIMSON label "Δ (the Discriminant)". Arrow down. Three case rows: Δ>0 (CRIMSON), Δ=0 (INK), Δ<0 (SLATE) with GrowArrow and description.

---

## Slate beats

**B01** — Hold. Narration: discriminant as diagnostic, three possible outcomes.  
**B07** — Hold. Narration: compute discriminant first, stop if negative.  
**B08** — Hold. Narration: predict root count before solving, verify.
