# SHOTLIST — code-runs-ships-wrong

**Why the Code Runs Fine and Still Ships Wrong**
Source: `claude-code-for-students/chapters/02-division-of-labor.md`
Topic kicker: CLAUDE CODE

---

## Histogram & Rhythm Check

| Beat | Type | Source | Motion | Act |
|------|------|--------|--------|-----|
| B01 | CARD | own | hold | COLD OPEN |
| B02 | CARD | own | hold | THE QUESTION |
| B03 | GRAPHIC | own | drawon | THE PROBLEM |
| B04 | STILL | ai | kenburns | THE PROBLEM |
| B05 | GRAPHIC | own | drawon | THE MECHANISM |
| B06 | CARD | own | hold | THE MECHANISM |
| B07 | GRAPHIC | own | drawon | THE EXAMPLE |
| B08 | GRAPHIC | own | drawon | THE IMPLICATION |
| B09 | GRAPHIC | own | drawon | THE MECHANISM (contd) |
| B10 | CARD | own | hold | THE PRACTICE |
| B11 | GRAPHIC | own | drawon | THE EXAMPLE (full) |
| B12 | CARD | own | hold | RECAP / ENDCARD |

**Type histogram:** CARD x 5, GRAPHIC x 5, STILL x 1. No >2 consecutive same-type. Rhythm: clean.

**Act map:**
- COLD OPEN: B01 (Seth's sort bug: compiles, passes, wrong)
- THE QUESTION: B02 (audit said looks good — why was it still wrong?)
- THE PROBLEM: B03–B04 (Claude's genuine pattern strength; fluency trap)
- THE MECHANISM: B05–B06, B09 (same weights = not independent; audit requires what Claude cannot see; solve vs verify asymmetry)
- THE EXAMPLE: B07 (Priya's leaderboard); B11 (Run Two — full supervisory sequence)
- THE PRACTICE: B10 (name the supervisory move)
- RECAP: B12 (the model is fine; supervision is missing)

**Color law:** CRIMSON = the bug / wrong output / invisible failure. INK = verified / the supervisory move. Single accent. Never swap.

**Exclusions confirmed:** no formal proof theory, no hallucination taxonomy, no Copilot stats, no RAG.

**Estimated duration:** ~150s = 2:30.

---

## Open Slot: B04 (STILL · ai)

### B04 — the plausibility-as-truth moment

**Beat:** B04 — developer looking at a clean sort function, nodding — the moment fluency overrides audit.

**Generative prompt:**
```
B04, a developer staring at a screen showing a clean sorting function in Python, leaning forward slightly, expression of confident recognition — they see the pattern and it looks right, editorial flat desaturated treatment, warm interior light, no text overlays, no phone, centered composition
```

---

## Non-fill beats (own Manim scenes)

B01, B02, B03, B05, B06, B07, B08, B09, B10, B11, B12 — rendered by vox_scenes.py.
