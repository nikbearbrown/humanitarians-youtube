# Feedback: "The Rally Has a Clock" (Pong) — long film (16:9), script review 1

**Rubric:** `PROOF.md` teaching rubric (six criteria, 0–2 each, /12) plus the binary production gate.
**Reviewed:** `READ-ALOUD.md` draft 1 (688 words, 13 beats) against `BEATS-DRAFT.md` and `FACTCHECK.md`. No frames exist, so legibility is *specified*, not measured.
**Verdict:** **unlisted-until-fixed at script level.** Teaching **9/12** (passes the 8/12 bar). Production gate **FAIL at plan level**, on one item that is a cheap edit: the model's constants are not on screen anywhere, so the film's own numbers cannot be checked by a viewer.
One line: this film attempts to show that "no perfect defense" is one checkable ratio and delivers the ratio and a measured check, but states the method late and ends on a question with no scaffold.

## Rubric (this cut)

| Criterion | Score | Reason |
|---|---|---|
| Explicit framework | 1 | The framework (can the paddle cover half the free height in one crossing) first appears in B05, about 1:05 in. B00–B04 run a rally and a set-up before the viewer has any structure to hold. PROOF's phase gate wants the framework graphic in the first ~20 s, ahead of any example. |
| Reusable rubric | 1 | The test is stated only for this field: "the paddle needs a little over a quarter of the ball's sideways speed". Nothing hands the viewer the form they could re-use on a different field or a different game: *the defender's reach in one attack's flight time vs the spread of the attacker's options.* |
| Worked example | 2 | B06–B08 walk three paddle speeds through the line, then predict-and-count. The reasoning step (arithmetic first, search second) is on screen. |
| Falsifiability / edge case | 2 | B08 makes a prediction the search could have broken (4.24 → sixth shot; 12.56 → fourteenth). B10 shows the claim failing when the ball never speeds up. B11 lists the model's absences. |
| Active task | 1 | B12 is one open question. It is a fine closing line, but PROOF rule 2 asks for a scaffold the viewer can run, and there is none. |
| Friction | 2 | The cold open is a puzzle (a perfect defender loses) held for about two and a half minutes, then resolved by the viewer's own reading of the bars; B10's "it is conditional" turns the answer over once more. |
| **Total** | **9/12** | |

**Reverse-engineered-framework check: clean.** The ratio is derived from the mechanics (half the free height over one crossing), not fitted to the three paddle speeds shown. The speeds do not map one-per-category; the same line separates all of them. The check that could have broken it did not: the search matched the formula at four ball speeds, and at all three speeds in B08.

## Production gate (plan level)

| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | PASS as specified, with one caution. B06 puts three lanes of the same rally side by side; each lane must hold its counter, paddle and ball legible at **full 4K size** (BEATS.md: a thumbnail passes everything). Re-measure on the render. |
| Sources on screen, not just voiced | **FAIL.** Every number in B00, B05–B09 comes from our own constants (field 858 × 525, paddle 60, start speed 6, +5% per shot, paddle speeds, aim settings), but no beat puts those constants on screen. B02 says "my model" and stops. A viewer cannot verify 0.27, "sixth shot" or "fourteenth shot" without them. Second item in the same row: `BEATS-DRAFT.md` B01 says the two quoted phrases are "attributed to Seth Brown's essay" on screen, while `FACTCHECK.md` and the Week 28 house practice keep the essay as "an essay I read" with credit in the README and description. These two files disagree. |
| Side-by-side at the moment of comparison | PASS as specified. B06 three lanes together; B08 predicted vs found in one table; B09 old vs new counters together. Each needs a hold of at least 2 s. |

## The problem

**The method arrives at 1:05, and the film's best proof is half-used.** Two edits fix both. They also
remove most of the gate failure.

## Findings (all [EDIT]; two came from new measurements)

1. **[EDIT] Put the framework on screen from frame one.** Draw the two bars from B05 (paddle can travel / paddle must
   travel, with the line) beside the rally in B00, silent. Name them in B03–B05. Same device as Week 28's strip.
   Lifts *Explicit framework* 1 → 2.
2. **[EDIT] Show the constants.** At B02 (and permanently in a corner chip): field 858 × 525, paddle 60, ball starts at 6,
   +5% per shot. Required for the gate, and it is what lets a viewer rerun B08.
3. **[EDIT] Make B09 a prediction too.** Measured in `angle_check4.py`: with the aim limited to a quarter of the ball's
   sideways speed, the line moves from 0.271 to 0.215 (a quarter, less the paddle's own reach over twice the field width).
   The arithmetic predicts the tenth shot at paddle speed 2.0 and the nineteenth at 3.0, and the search found exactly those
   (also the fifth at 1.5 and the first at 1.0). B09 currently reports an observation; it can show a prediction that could have failed,
   same as B08. Replace "narrow the steering and the clock moves" with "predict, then count".
4. **[EDIT] Give the method a second field.** Same formula on a different field, 1200 × 500 with a paddle of 50: the line
   is 0.1875, and the arithmetic and the search agree at three paddle speeds (seventh, eighteenth and twenty-seventh shots;
   `angle_check4.py`). One short beat after B08, showing the line move when only the field changes, hands over the form
   *reach in one flight vs half the free height*. Lifts *Reusable rubric* 1 → 2. About 20 s.
5. **[EDIT] Replace the bare closing question with a scaffold, then the question.** B12 keeps the one open question, but
   first a card: *line = (height − paddle) ÷ (2 × width)*. Your turn: a field 1000 wide, 500 tall, paddle 50. Answer withheld for a beat
   (0.225), then shown. Then: "If you could set one dial, where would you put it?" Lifts *Active task* 1 → 2, and keeps the
   open ending (the "each film its own structure" practice).
6. **[EDIT] Reconcile the essay credit.** Choose one: on-screen "from an essay in the Humanitarians AI repo", name in the
   README and YouTube description (Week 28 practice). Update `BEATS-DRAFT.md` B01 to match `FACTCHECK.md`.
7. **[EDIT] Calibrate three lines (voice).** B07 "A rally … has a clock inside it" → "In my model, a rally has a clock inside it".
   B10 "defends perfectly, forever" → "never broke in two hundred shots, and the arithmetic says it never will".
   B12 "Every Pong has a clock" is already out; the replacement line is "Every Pong like this one".
8. **Note, not a finding.** At about 3:50 the film is shorter than Week 28 (4:45). Items 1, 3, 4 and 5 add roughly 40–50 s,
   which brings it near the 4:30 plan. No padding needed.

## What works

- The cold-open puzzle: a perfect defender loses, and nobody errs. It carries the whole film.
- Predict-then-count (B08) is the film's own form of "no source, no verdict": it names a result the search could have refuted.
- B10 and B11 state the claim's condition and the model's absences plainly, without apology.

## Do next

1. [EDIT] Apply findings 1–7 to `BEATS-DRAFT.md` and `READ-ALOUD.md`; re-run this review on the new draft.
2. [EDIT] Add `angle_check4.py` results to `FACTCHECK.md` (B09, the second field and the closing card's 0.225).
3. [EDIT] Then Gate P: read every line aloud once; sign `PEDAGOGY.md`.
4. At build: re-run this review on frames, with the production gate measured at full size.

**Projected after edits:** teaching 12/12, gate PASS at plan level.
