# SHOTLIST — pagination-bug-dangerous-middle

**Why the Most Dangerous Claude Output Is the One That Passes Every Test**
Source: `claude-code-for-students/chapters/09-handoff-conditions-dangerous-middle.md`
Topic kicker: CLAUDE CODE

---

## Histogram & Rhythm Check

| Beat | Type | Source | Motion | Act |
|------|------|--------|--------|-----|
| B01 | CARD | own | hold | COLD OPEN |
| B02 | CARD | own | hold | THE QUESTION |
| B03 | GRAPHIC | own | drawon | THE PROBLEM |
| B04 | GRAPHIC | own | accumulate | THE PROBLEM |
| B05 | STILL | ai | kenburns | THE MECHANISM |
| B06 | GRAPHIC | own | drawon | THE MECHANISM |
| B07 | CARD | own | hold | THE MECHANISM (kicker) |
| B08 | GRAPHIC | own | drawon | THE EXAMPLE |
| B09 | GRAPHIC | own | drawon | THE PRACTICE |
| B10 | CARD | own | hold | RECAP |

**Type histogram:** CARD x 4, GRAPHIC x 5, STILL x 1. No >2 consecutive same-type. Rhythm: clean.

**Act map:**
- COLD OPEN: B01 (Seth's pagination: all tests pass; Avery's flashlight doesn't exist)
- THE QUESTION: B02 (all tests passed — why did 251 items fail?)
- THE PROBLEM: B03–B04 (every test was a multiple of 50; the bug fires at page_size × n + 1)
- THE MECHANISM: B05–B07 (the joint between function and calling loop; the handoff condition that was never written; pre-condition shapes, post-hoc rationalizes)
- THE EXAMPLE: B08 (Priya's leaderboard, 41 players, 41st never appears)
- THE PRACTICE: B09 (write the non-obvious case; page_size × n + 1)
- RECAP: B10 (the most dangerous output passes every test you thought to write)

**Color law:** CRIMSON = tests passing but wrong / dangerous middle / the missing handoff. INK = the handoff condition / the non-obvious case / verified output. Single accent. Never swap.

**Exclusions confirmed:** no formal Hoare-triple proof notation; no security vulnerability taxonomy; no property-based testing frameworks.

**Estimated duration:** ~210s ≈ 3:30.

---

## Open Slot: B05 (STILL · ai)

### B05 — code on screen looking correct, developer about to commit

**Beat:** B05 — developer looking at passing tests, hand on mouse, about to click commit — the moment before the dangerous middle ships.

**Generative prompt:**
```
B05, a developer at a desk with a laptop showing a terminal with green passing tests, hand on mouse about to click, confident expression — the calm before a subtle bug ships — editorial flat desaturated treatment, warm desk lamp, centered composition, no readable text on screen
```

---

## Non-fill beats (own Manim scenes)

B01, B02, B03, B04, B06, B07, B08, B09, B10 — rendered by vox_scenes.py.
