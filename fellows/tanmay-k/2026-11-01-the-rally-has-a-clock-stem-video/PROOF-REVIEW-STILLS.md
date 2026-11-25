# Feedback: "The Rally Has a Clock" (Pong) — review stills, long film (16:9), review 2

**Rubric:** `PROOF.md` teaching rubric (six criteria, 0–2) plus the binary production gate, run on the **rendered frames** (`_stills/B00`–`B13`, plus `B13-hold`), each read against its signed narration line.
**Prior:** `PROOF-REVIEW-STILLS-1.md` (first render, ten layout defects fixed). Plan-level script review: `PROOF-REVIEW.md` (12/12).
**Verdict:** **clear-for-public at stills level.** Teaching **12/12**. Production gate **PASS at stills level**. Motion, audio and timing are not built, so public still requires the same review on the compiled film.
One line: the frames show the method before they ask anyone to trust it, and every figure on them reproduces from `sim_model.py`.

## Changes since the stills were sent (your note, plus two gaps found in this review)
| Beat | Change |
|---|---|
| B02 | "bottom: down" label moved up (steering lines flattened, diagram raised) so it clears the card edge. Your note. |
| B07 | The narration says "that bar keeps sinking toward the line", but the frame showed only the chart. Added the two framework bars at shot six (224 vs 232.5), labelled "CAN TRAVEL / MUST TRAVEL". |
| B13 | The five-second withheld frame did not exist. Built `B13-hold` (formula and the numbers, answer shown as "?"; no verdict cards, no closing question). |

## Rubric (these frames)
| Criterion | Score | Reason |
|---|---|---|
| Explicit framework | 2 | The two bars are in B00 (first frame), B03, B05 and B07; the line is drawn on all of them. Method precedes every dial. |
| Reusable rubric | 2 | B05 states the form and the formula; B10 applies it to a second field; B13 hands it over with a new case. |
| Worked example | 2 | B06 (outcomes), B07 (why), B08 (arithmetic then search): the reasoning step is on screen, not only the result. |
| Falsifiability / edge case | 2 | Three predicted-vs-found frames (B08, B09, B10), the no-speed-up card (B11), the exclusions slate (B12). |
| Active task | 2 | `B13-hold` is a task frame in its own right; `B13` shows the answer and what it means for a quarter-speed and a fifth-speed paddle. |
| Friction | 2 | B00's perfect defender that loses; B13's held "?". |
| **Total** | **12/12** | |

**Reverse-engineered-framework check: clean.** The bars/line are derived in B03–B05, then tested on settings they were not fitted to (B09 narrow aim, B10 different field, B13 the viewer's field).

## Narration-to-frame match
| Beat | Spoken claim | On the frame | Match |
|---|---|---|---|
| B00 | shots one to five defended; the sixth gets past | six dots, five filled, one orange; 8.4 px gap; 224 vs 232.5 | yes (end state; counter animates in motion) |
| B01 | the essay's two phrases | both phrases, source line | yes |
| B02 | rules; every number from the settings | field, arrows, steering diagram, constants card, chip | yes |
| B03 | direction fixed; the crossing is all the time; "the two bars in the corner" | folded path, 143 ticks, bars at shot one | yes, but see edit 1 |
| B04 | aim anywhere; wait in the middle; worst shot half a field away | full fan, extremes lit, 262.5 less 30 = 232.5 | yes |
| B05 | paddle covers about half the field less its reach; a little over a quarter | bars, 0.27, (525 − 60) ÷ (2 × 858) = 0.271 | yes |
| B06 | three speeds: first shot; sixth; fourteenth | three rows, breaks at 1, 6, 14 | yes (outcomes; lanes play in motion) |
| B07 | the ball speeds up; crossing shorter; that bar sinks toward the line | chart, crossings at 6 and 14, bars at shot six | yes (fixed this pass) |
| B08 | 4.24 to sixth; 12.56 to fourteenth; search matched | table | yes |
| B09 | line about 0.215; tenth and nineteenth; then the count | 0.271 → 0.215, strip, predicted and found rows | yes |
| B10 | 1200 by 500; line 0.188; seventh and twenty-seventh | two fields, 0.271 vs 0.1875, three-row table | yes (speech names two; table shows three) |
| B11 | two rules carry it; no speed-up never broke in 200 shots | three cards | yes |
| B12 | the four exclusions | four cards | yes |
| B13 | field 1000 by 500, paddle 50; point two two five; quarter-speed perfect, fifth not | `B13-hold` then `B13` | yes |

## Production gate (stills level)
| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | PASS at 4K. Smallest type is 24 logical px; fine for a 16:9 film, too small for phone width, so the Short needs its own layout. |
| Sources on screen, not just voiced | PASS. Constants chip or card on every slate that uses the field; B01 carries the essay credit line; formulas shown. |
| Side-by-side at the moment of comparison | PASS. B06, B08, B09, B10 each hold the pair together; each needs a hold of at least two seconds in motion. |

## The problem
None that blocks. The real risk is **motion, not the frames**: B06 shows outcomes, not three rallies playing, and B09's "predicted then counted" needs ticks that appear before the count lands on them.

## Do next (all [EDIT], to build)
1. **Pin the bars.** B03 says "the two bars in the corner"; they sit bottom-right in B00, B03 and B07 but top-left in B05. Pin the widget to one corner in every beat that has it, and keep B05 as the one enlarged frame.
2. **Strip review captions from the master:** B13's "answer shown after a five-second hold" and `B13-hold`'s "work it out" are review notes, not film text.
3. **B06 motion:** the rows fill dot by dot as shots play; hold the finished frame two seconds.
4. **B09 motion:** predicted ticks first, then the count runs and lands on them; two-line tally last.
5. **Animation fades:** Pillow ignores alpha on text; measure every fade on pixels before the compile.
6. Then: Kokoro phoneme check, audio, cue timing on the Whisper clock, one compile, this review again on frames.

## What works
- The two bars are on screen from the first frame, so B05's line is a recognition, not an introduction.
- Every figure is asserted against the signed narration before a pixel is drawn.
- B08, B09 and B10 give the viewer three chances to see the arithmetic lose, and it never does.
