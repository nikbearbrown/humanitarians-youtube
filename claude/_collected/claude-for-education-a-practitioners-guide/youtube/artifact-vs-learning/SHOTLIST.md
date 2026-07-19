# SHOTLIST — artifact-vs-learning
**Why a Polished Lesson Plan Can Fail Every Student in the Room**
Source: `claude-for-education-a-practitioners-guide/chapters/00-introduction-the-teacher-is-still-the-system.md`

---

## HISTOGRAM (shot type count)
| Type     | Beats                      | Count |
|----------|---------------------------|-------|
| CARD     | B01, B04, B07, B10, B13   | 5     |
| GRAPHIC  | B03, B05, B06, B08, B09, B11, B12 | 7 |
| STILL    | B02                        | 1     |

Rhythm check: B05-B06 are both GRAPHIC (consecutive). B08-B09 are both GRAPHIC (consecutive). No run of >2. PASS.

## ACT MAP
| Beat | Act             | Type    |
|------|-----------------|---------|
| B01  | COLD OPEN       | CARD    |
| B02  | COLD OPEN       | STILL   |
| B03  | COLD OPEN       | GRAPHIC |
| B04  | THE QUESTION    | CARD    |
| B05  | THE PROBLEM     | GRAPHIC |
| B06  | THE PROBLEM     | GRAPHIC |
| B07  | THE MECHANISM   | CARD    |
| B08  | THE EXAMPLE     | GRAPHIC |
| B09  | THE EXAMPLE     | GRAPHIC |
| B10  | THE IMPLICATION | CARD    |
| B11  | THE PRACTICE    | GRAPHIC |
| B12  | THE PRACTICE    | GRAPHIC |
| B13  | RECAP           | CARD    |

Duration: ~148s ≈ 2:28. Within 2–3 min band. PASS.

## COLOR LAW
- TEAL (#1F6F5C) = genuine learning / named outcome / cognitive work done
- CRIMSON (#BF3339) = artifact gap / surface fluency / missing link
- Never swapped mid-film.

## EXCLUSIONS CONFIRMED
- No AI detection tools
- No history of ed-tech failures
- No comparison to other AI tools
- No enumeration of all ways AI can fail

---

## FILL-IN BEATS

### B02 — STILL · ai
**Beat:** B02 — biology classroom, student with blank look after completing activities.

**Archive search:** None — invented illustrative scene. Generative only.

**Generative prompt:**
```
B02, high school biology classroom, desaturated editorial style, students seated at desks completing printed worksheets, warm overhead classroom light, one student in foreground has written "ATP = adenosine triphosphate" neatly on the worksheet but stares blankly ahead rather than at the paper, other students writing in background, flat documentary photograph style, aged newsprint tone, no brand logos, no digital devices visible
```

**Provenance:** Generative / illustrative. No real students depicted.

---

## OWN MANIM BEATS (GRAPHIC, source: own)

### B03 — GRAPHIC · own · `B03_PlanVsOutcome`
Two-column layout: left card = lesson plan (TEAL-border, neat bullet list); right card = exit ticket (blank answer field, CRIMSON-border). Labels below: "coherent artifact" (TEAL serif) / "no learning" (CRIMSON serif). Both cards fade in simultaneously, then labels appear.

### B05 — GRAPHIC · own · `B05_NaiveChain`
Three TEAL blocks left-to-right connected by arrows: "BETTER PLAN" → "FAITHFUL USE" → "STUDENT LEARNING". Each block fades in with arrow, chain reading clean.

### B06 — GRAPHIC · own · `B06_WhatClaudeMisses`
"BETTER PLAN" TEAL block at top-left remains. Three CRIMSON label chips appear in a column below it: "prior knowledge", "specific misconceptions", "evidence of understanding" — each has a strikethrough line. Serif label: "Claude cannot access this."

### B08 — GRAPHIC · own · `B08_ParkPlan`
A lesson-plan card with three activity slots stacked: "Diagram activity", "Vocabulary matching", "Fill-in-the-blank check". A student dot appears beside each and a TEAL tick appears when complete. All three ticks fill in sequence.

### B09 — GRAPHIC · own · `B09_ExitBlank`
IsotypeGrid of 28 student squares. 22 appear CRIMSON (blank). 6 appear TEAL (answered). Serif label below: "22 of 28 — outcome never named."

### B11 — GRAPHIC · own · `B11_OutcomeFirst`
Two column cards side by side. Left (CRIMSON-border): "Understand the water cycle". Right (TEAL-border): "Explain why rain falls as liquid, not vapor." Serif label under right: "name this first — before the prompt."

### B12 — GRAPHIC · own · `B12_NaiveFixed`
The B05 three-block chain returns. A new TEAL block "NAMED OUTCOME" is inserted at the start (pushing others right). Chain reads: "NAMED OUTCOME" → "ALIGNED PLAN" → "STUDENT TRANSFER." The three CRIMSON chips from B06 fade out as NAMED OUTCOME slides in.
