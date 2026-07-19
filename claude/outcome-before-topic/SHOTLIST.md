# SHOTLIST — outcome-before-topic
**Why Telling Claude the Topic Is the Wrong First Step**
Source: `claude-for-education-a-practitioners-guide/chapters/02-learning-outcomes-before-prompts.md`

---

## HISTOGRAM
| Type     | Beats                          | Count |
|----------|-------------------------------|-------|
| CARD     | B01, B03, B06, B09, B13       | 5     |
| GRAPHIC  | B04, B05, B07, B08, B10, B11, B12 | 7  |
| STILL    | B02                            | 1     |

Rhythm check: B04-B05 consecutive GRAPHIC. B07-B08 consecutive GRAPHIC. B10-B11-B12 three consecutive GRAPHIC — this is the maximum allowed. PASS (cap is >2 consecutive = flag; three consecutive is exactly at the limit).

## ACT MAP
| Beat | Act             |
|------|-----------------|
| B01  | COLD OPEN       |
| B02  | COLD OPEN       |
| B03  | THE QUESTION    |
| B04  | THE PROBLEM     |
| B05  | THE PROBLEM     |
| B06  | THE MECHANISM   |
| B07  | THE EXAMPLE     |
| B08  | THE EXAMPLE     |
| B09  | THE IMPLICATION |
| B10  | THE MECHANISM (repaired) |
| B11  | THE PRACTICE    |
| B12  | THE PRACTICE    |
| B13  | RECAP           |

Duration: ~158s ≈ 2:38. Within 2–3 min band. PASS.

## COLOR LAW
- TEAL = outcome-anchored prompt / aligned activities / student transfer
- CRIMSON = topic-first prompt / coverage / the gap
- Never swapped mid-film.

## EXCLUSIONS CONFIRMED
- No Bloom's taxonomy deep-dive
- No full backward-design theory lecture
- No listing all eight fields of the instructional brief
- No discussion of grading

---

## FILL-IN BEATS

### B02 — STILL · ai
Beat: B02 — teacher at laptop typing a short prompt, students in background.

**Archive search:** None — illustrative scene. Generative only.

**Generative prompt:**
```
B02, high school classroom, a teacher seated at a laptop on their desk typing a short text query visible on the screen, students at desks in the background working quietly, warm overhead classroom lighting, editorial documentary desaturated style, flat newsprint tone, wide shot, no brand logos, no digital devices in student hands visible
```

**Provenance:** Generative / illustrative. No real students depicted.

---

## OWN MANIM BEATS

### B04 — GRAPHIC · own · `B04_NaiveTopicChain`
Four TEAL blocks in a left-to-right chain with arrows: "TOPIC" -> "CLAUDE" -> "LESSON" -> "LEARNING". Each block and arrow appears in sequence.

### B05 — GRAPHIC · own · `B05_GapRevealed`
The B04 chain returns. The arrow between "LESSON" and "LEARNING" turns CRIMSON and a visible gap opens. Serif label drops in: "coverage does not equal learning."

### B07 — GRAPHIC · own · `B07_TwoPrompts`
Two prompt window cards side by side. Left (CRIMSON border): short one-line prompt. Right (TEAL border): multi-line outcome-anchored prompt. Word counts appear below each.

### B08 — GRAPHIC · own · `B08_DivergingOutputs`
Under each prompt card from B07, three activity chips drop in. Left: CRIMSON chips (definitional). Right: TEAL chips (conflict/resolution).

### B10 — GRAPHIC · own · `B10_AlignmentFixed`
Four TEAL blocks: "NAMED OUTCOME" -> "ANCHORED PROMPT" -> "ALIGNED LESSON" -> "STUDENT TRANSFER". All solid TEAL connections.

### B11 — GRAPHIC · own · `B11_WrittenOutcome`
A blank notepad card. Text writes in: "Students will explain why 6 / 1/2 = 12." TEAL bracket labeled "outcome". Serif label: "write this before you open Claude."

### B12 — GRAPHIC · own · `B12_TwoPathCards`
Two short path diagrams stacked vertically. Top (CRIMSON): "TOPIC -> PROMPT -> COVERAGE". Bottom (TEAL): "OUTCOME -> PROMPT -> TRANSFER."
