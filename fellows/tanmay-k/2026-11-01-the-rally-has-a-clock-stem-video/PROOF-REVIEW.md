# Feedback: "The Rally Has a Clock" (Pong) — long film (16:9), script review 2

**Rubric:** `PROOF.md` teaching rubric (six criteria, 0–2 each, /12) plus the binary production gate.
**Reviewed:** `READ-ALOUD.md` / `BEATS-DRAFT.md` draft 2 (881 words, 14 beats) against `FACTCHECK.md` draft 2. No frames exist, so legibility is *specified*, not measured.
**Prior review:** `PROOF-REVIEW-1.md` (9/12, gate FAIL).
**Verdict:** **clear-for-public at script level.** Teaching **12/12**. Production gate **PASS at plan level**; it must be re-measured on the render, and public still requires that.
One line: this film attempts to show that "no perfect defense" is one checkable ratio, and delivers it with three predictions the search could have refuted and a task the viewer can run.

## Where it improved vs review 1

| Criterion | Review 1 | Review 2 | What changed |
|---|---|---|---|
| Explicit framework | 1 | 2 | The two bars (can travel / must travel, with the line) are on screen from frame one in B00, unnarrated; named in B03, defined in B05. |
| Reusable rubric | 1 | 2 | B05 states the form ("reach in one flight against half the free height"); B10 reuses it on a different field; B13 hands it over. |
| Worked example | 2 | 2 | Unchanged: B06–B08. |
| Falsifiability / edge case | 2 | 2 | Stronger: B09 and B10 add two more predictions the search could have broken; B11 still shows the claim failing. |
| Active task | 1 | 2 | B13: a card, three numbers, the answer withheld five seconds, then 0.225 and what it means for a quarter-speed and a fifth-speed paddle. Then the open question. |
| Friction | 2 | 2 | Unchanged. |

## Rubric (this cut)

| Criterion | Score | Reason |
|---|---|---|
| Explicit framework | 2 | Bars visible from the first frame (B00), named B03, stated as a ratio B05, ahead of every dial and field. |
| Reusable rubric | 2 | One form, applied on three fields (858 x 525, the narrow-aim case, 1200 x 500) and handed to the viewer for a fourth (1000 x 500). |
| Worked example | 2 | B06–B08: three paddle speeds, arithmetic first, search second. |
| Falsifiability / edge case | 2 | B08, B09, B10: three predict-then-count tables, ten predictions in all, each matched. B11: the claim fails if the ball never speeds up. B12: what the model leaves out. |
| Active task | 2 | B13 gives a scaffold (the formula card), a case to run, and what a good answer looks like (0.225; quarter-speed defends, fifth does not). |
| Friction | 2 | Cold-open puzzle held until B07; B11's "conditional" turn. |
| **Total** | **12/12** | |

**Reverse-engineered-framework check: clean.** The ratio is derived from mechanics, then tested on settings it was not fitted to: a different aim range (B09) and a different field (B10), plus the viewer's case (B13, checked in `angle_check5.py`). Every prediction matched the search: 4 of 4 for narrow aim, 3 of 3 on the second field, 2 of 2 in B08, 4 of 4 ball speeds in B05.

## Production gate (plan level)

| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | PASS as specified. Re-measure at full 4K size on the render: B06 (three lanes) and the B08–B10 tables are the dense frames (BEATS.md: a thumbnail passes everything). |
| Sources on screen, not just voiced | PASS as specified. The settings chip (858 x 525, paddle 60, start speed 6, +5% per shot) is on screen from B02 and updates to 1200 x 500 / paddle 50 in B10. Essay phrases carry "from an essay in the Humanitarians AI repo"; the author is named in the README and description. The two files now agree. |
| Side-by-side at the moment of comparison | PASS as specified. B06 three lanes; B08, B09, B10 predicted-vs-found tables; B09 old breaks beside new. Each held at least two seconds. |

## The problem

None that blocks. The largest risk is **fatigue, not accuracy**: B08, B09 and B10 are three predicted-vs-found tables in a row,
and B10 speaks six ordinals in one breath ("the seventh, the eighteenth, the twenty-seventh").

## Findings from this pass

1. **[EDIT] Vary B08–B10 visually.** B08 keeps the table; B09 should be the wedge narrowing with a tally overlay (the table appears only at the end); B10 should lead with the redrawn field. Same device three times reads as a drill.
2. **[EDIT] Shorten B10's speech.** Two paddle speeds (one and a half, four) instead of three keeps the point. Three can stay in the on-screen table. This is a read-aloud call at Gate P.
3. **Timing.** 881 words is about 4:10 of speech and about 5:00 with holds and the five-second pause in B13, longer than Week 28 (4:45) and the original 4:30 plan. The Gate P read decides whether any beat is cut; B10 is the first candidate.
4. **Residual.** The bars are on screen from the first frame but named at about one minute (B03). The earlier film named its strip at about twenty seconds. If Gate P wants it sooner, move the naming line to B01.
5. **Open verification closed.** B13's 1000 x 500 case is now run (`angle_check5.py`); FACTCHECK updated.

## What works

- The cold open: a perfect defender loses on shot six, and the bars in the corner already hold the answer.
- Predict-then-count three times, on three different changes, each matching: the film's own form of "no source, no verdict".
- B11 and B12 state the claim's condition and the model's absences without apology.
- B13 ends on a task the viewer can run, then returns the one open question.

## Update (draft 2.1)
Findings 1 and 2 applied: B10 speaks two paddle speeds (table keeps all three); B08 table, B09 ticks-then-count with a closing tally, B10 field-first. Speech 2 ordinals shorter; findings 3-4 remain Gate P decisions. Score and gate unchanged (12/12, PASS at plan level).

## Do next

1. [EDIT] Gate P: read every line aloud once; decide findings 1–2 and the B03/B01 naming point; sign `PEDAGOGY.md`.
2. [EDIT] Generate audio only after Gate P; measure durations (they replace the 3.5 words/s plan).
3. At build: re-run this review on frames, with the production gate measured at full size.
