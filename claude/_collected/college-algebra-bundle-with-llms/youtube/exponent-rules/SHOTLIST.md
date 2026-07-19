# SHOTLIST — exponent-rules

**Slug**: exponent-rules  
**Style**: CLI / NikBearBrown  
**Palette**: teardown  
**Aspect**: 16:9  
**Total beats**: 10  
**Color law**: CRIMSON for the key result "a⁰ = 1" and rule labels. GOLD for the highlight box confirming a⁰ = 1. SLATE for caveat and secondary text. INK for body text.

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
Props: topic="COLLEGE ALGEBRA", lines=["Nik Bear Brown", "Exponent Rules", "Why a to the zero equals one"]

**B02** — NikBearBrownTerminalAsk  
command: `claude "write a Manim scene proving a^0=1 using the quotient rule: show a^3/a^3=a^(3-3)=a^0 and also =1, then animate all six exponent rules"`  
runningText: "generating exponent proof..."

**B03** — NikBearBrownCodeBlock  
filename: `exponent_rules.py`  
Code: prints a^3/a^3 proof then lists 6 RULES strings.

**B05** — NikBearBrownTerminalAsk  
command: `claude "add a worked example for each rule using base 2 with specific numbers"`  
runningText: "adding worked examples..."

**B09** — NikBearBrownOutro

---

## Manim beats

**B04** — `B04_ExponentProof` in `vox_scenes.py`  
4-step proof: Start with a³÷a³ → quotient rule → also equals 1 → therefore a⁰=1. GOLD box with CRIMSON label confirms result. SLATE caveat at bottom about 0⁰.

**B06** — `B06_ExponentRules` in `vox_scenes.py`  
6 rows: dot + name label (SLATE) + rule in CRIMSON bold + base-2 example in INK. All 6 rules with verified numerical examples.

---

## Slate beats

**B01** — Hold. Narration: zero exponent not a definition, derived from quotient rule.  
**B07** — Hold. Narration: zero and negative exponents are pattern extensions, not special cases.  
**B08** — Hold. Narration: derive power rule from product rule — count exponents manually.
