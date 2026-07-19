# SHOTLIST — domain-restrictions

**Slug**: domain-restrictions  
**Style**: CLI / NikBearBrown  
**Palette**: teardown  
**Aspect**: 16:9  
**Total beats**: 10  
**Color law**: CRIMSON for asymptote labels and the hole circle. INK for general body text and g(x) header. SLATE for axis lines and secondary labels.

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
Props: topic="COLLEGE ALGEBRA", lines=["Nik Bear Brown", "Domain Restrictions", "The hole that travels"]

**B02** — NikBearBrownTerminalAsk  
command: `claude "write a Manim scene showing two rational functions: f(x)=1/(x-2) with vertical asymptote, and g(x)=(x^2-4)/(x-2) which simplifies to x+2 but has a removable hole at x=2"`  
runningText: "generating domain graphs..."

**B03** — NikBearBrownCodeBlock  
filename: `domain_holes.py`  
Code: numpy arrays for both functions excluding x=2, prints asymptote vs. hole distinction.

**B05** — NikBearBrownTerminalAsk  
command: `claude "show g(x)=(x^2-4)/(x-2) simplified step by step and plot it with an open circle at x=2 to show the removable discontinuity"`  
runningText: "adding removable discontinuity..."

**B09** — NikBearBrownOutro

---

## Manim beats

**B04** — `B04_DomainHole` in `vox_scenes.py`  
Axes created. Two branches of 1/(x-2) in CRIMSON. DashedLine vertical asymptote at x=2 in CRIMSON. Label "x=2 (asymptote)". Domain string at bottom.

**B06** — `B06_DomainHole2` in `vox_scenes.py`  
Two panels divided by vertical line. Left (CRIMSON header): f(x) asymptote facts. Right (INK header): g(x) step-by-step factoring + "HOLE at (2,4)". Open circle (GrowFromCenter) at the hole position.

---

## Slate beats

**B01** — Hold. Narration: canceling creates a hole that travels forever.  
**B07** — Hold. Narration: asymptote vs hole distinction — why they look different because they are different.  
**B08** — Hold. Narration: classify 3 rational functions — holes vs asymptotes.
