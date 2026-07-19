# SHOTLIST — pemdas-ambiguity

**Slug**: pemdas-ambiguity  
**Style**: CLI / NikBearBrown  
**Palette**: teardown  
**Aspect**: 16:9  
**Total beats**: 10  
**Color law**: CRIMSON for the "1" answer (implicit mult. binding), INK for the "16" answer (left-to-right). CRIMSON for warnings and the key verdict.

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
Props: topic="COLLEGE ALGEBRA", lines=["Nik Bear Brown", "PEMDAS Ambiguity", "When the convention breaks"]

**B02** — NikBearBrownTerminalAsk  
command: `claude "write a Manim scene showing two interpretations of 8÷2(2+2): one where implicit multiplication binds tighter than division (answer=1) and one where left-to-right division applies first (answer=16)"`  
runningText: "generating disambiguation..."

**B03** — NikBearBrownCodeBlock  
filename: `pemdas_debug.py`  
Two interpretations: A = 8/(2*(2+2)) = 1; B = (8/2)*(2+2) = 16

**B05** — NikBearBrownTerminalAsk  
command: `claude "add the fix: rewrite the expression unambiguously as both (8÷2)(2+2) and 8÷(2(2+2)) and show which answer each gives"`  
runningText: "adding fix..."

**B09** — NikBearBrownOutro

---

## Manim beats

**B04** — `B04_PEMDASAmbiguity` in `vox_scenes.py`  
Expression at top. Vertical divider. Left column: implicit mult. binds (→ 1, CRIMSON). Right column: left-to-right (→ 16, CRIMSON for final answer). Verdict at bottom.

**B06** — `B06_PEMDASFixed` in `vox_scenes.py`  
PEMDAS rule table with 4 rows. Two boxed expressions at bottom: (8÷2)(2+2)=16 in INK box; 8÷(2(2+2))=1 in CRIMSON box. Note at bottom.

---

## Slate beats

**B01** — Hold. Narration: viral expression, genuine disagreement, implicit multiplication ambiguity.  
**B07** — Hold. Narration: write explicit parentheses every time.  
**B08** — Hold. Narration: rewrite any implicit-multiplication expression both ways.
