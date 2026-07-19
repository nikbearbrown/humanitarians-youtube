# SHOTLIST — slopsquatting-hallucinated-package

**Why Slopsquatting Turns Claude's Wrong Answer Into a Security Hole**
Source: `claude-code-for-students/chapters/05-five-supervisory-capacities.md`
Topic kicker: CLAUDE CODE

---

## Histogram & Rhythm Check

| Beat | Type | Source | Motion | Act |
|------|------|--------|--------|-----|
| B01 | CARD | own | hold | COLD OPEN |
| B02 | CARD | own | hold | THE QUESTION |
| B03 | GRAPHIC | own | drawon | THE PROBLEM |
| B04 | GRAPHIC | own | drawon | THE PROBLEM |
| B05 | GRAPHIC | own | drawon | THE MECHANISM |
| B06 | CARD | own | hold | THE MECHANISM (kicker) |
| B07 | STILL | ai | kenburns | THE MECHANISM |
| B08 | GRAPHIC | own | drawon | THE PRACTICE |
| B09 | CARD | own | hold | RECAP |

**Type histogram:** CARD x 4, GRAPHIC x 4, STILL x 1. No >2 consecutive same-type. Rhythm: clean.

**Act map:**
- COLD OPEN: B01 (Fatima: Claude writes the import, pip install succeeds, attacker's code runs)
- THE QUESTION: B02 (package exists — why does it run attacker's code?)
- THE PROBLEM: B03–B04 (models hallucinate ~20% package names; 58% recur — predictable, targetable)
- THE MECHANISM: B05–B07 (three-step attack; slopsquatting named; Fatima's default workflow is the exploit)
- THE PRACTICE: B08 (verify every package on pypi.org/npmjs.com before installing)
- RECAP: B09 (Claude's suggested import is not a verified package — verify before you install)

**Color law:** CRIMSON = hallucinated package / attacker / silent compromise. INK = verified package / plausibility audit / the defense. Single accent. Never swap.

**Exclusions confirmed:** no full supply-chain security methodology; no PyPI moderation policy; no formal threat-modeling framework; no cross-ecosystem comparison.

**Estimated duration:** ~168s ≈ 2:48.

---

## Open Slot: B07 (STILL · ai)

### B07 — Fatima at her laptop, running a script, unaware

**Beat:** B07 — student running code, confident expression, no visible sign anything is wrong — the silent compromise in progress.

**Generative prompt:**
```
B07, a student at a laptop typing a command in a terminal, relaxed confident expression, no sign of anything wrong — the moment before they discover the problem — editorial flat desaturated treatment, warm desk lamp, centered composition, no readable text on screen
```

---

## Non-fill beats (own Manim scenes)

B01, B02, B03, B04, B05, B06, B08, B09 — rendered by vox_scenes.py.
