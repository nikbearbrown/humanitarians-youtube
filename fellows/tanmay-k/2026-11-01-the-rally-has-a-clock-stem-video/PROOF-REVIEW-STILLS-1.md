# PROOF review — review stills (long film, 16:9), pass 1

`build_slates.py` -> `_stills/B00-16x9.png` ... `B13-16x9.png`, all 3840 x 2160. Every figure on a slate is computed by
`sim_model.py`, which first asserts it against the signed narration (shots 6/14, 10/19, 7/27; lines 0.271, 0.215, 0.1875,
0.225; 4.24 and 12.56 speed-ups; no break in 200 shots without speed-up). Stills show the **moment of assertion**, not the motion.

## Found on first render and fixed before this review (re-rendered, re-read)
| Beat | Defect | Fix |
|---|---|---|
| B00 | "8.4 px short" floated away from the gap; the bar-marker line cut through the bar labels | bracket drawn at the gap, label below the ball path; marker starts at the bar |
| B02 | steering diagram spilled out of its card and sat on its caption | card enlarged, diagram redrawn inside it |
| B03 | card text touching its bottom edge | card taller |
| B04 | label crossed the extreme path | label moved clear |
| B05 | "a little over a quarter" on the card edge | card taller |
| B07 | title collided with chart; the 3.0 curve left the frame; right text clipped at the edge | axis to 480, caption above chart, text wrapped, labels clear |
| B08 | table ran to the page edge | columns narrowed |
| B09 | card text overflowed the card; two colours unlabelled; "defence" spelling | rows in columns, legend added, "defense" |
| B10 | table header sat on the field captions; fields empty | fields redrawn with the two extreme shots, table lowered |
| B13 | formula overlapped its caption; answer cards cramped | card and rows resized |

## Per-beat read (what the frame must show at the claim)
| Beat | Shows | Verdict |
|---|---|---|
| B00 Shot six | rally end state, six dots, 224 vs 232.5 bars, the 8.4 px gap | PASS. The framework bars are on screen from frame one. |
| B01 The claim | the two essay phrases, source line, the question | PASS. Right half is empty by design; the phrases carry it. |
| B02 The stage | field, up/down arrows, steering diagram, constants card | PASS. Constants on screen as FINDING 2 required. |
| B03 What the defender knows | folded path, 143 ticks, bars at shot one (286 vs 232.5) | PASS. Unfolded line not drawn; the narration does not need it. |
| B04 Worst shot | full fan, extremes lit, 262.5 less 30 = 232.5 | PASS. |
| B05 The line | bars, 0.27, the form, (525 - 60) / (2 x 858) = 0.271, search 0.272 | PASS. Card says 0.27 (narration: "a little over a quarter"); formula says 0.271. |
| B06 Turn the dial | three lanes: breaks at 1, 6, 14 | PASS, side by side. |
| B07 The clock | both speeds against the must-travel line, crossing marked at 6 and 14 | PASS. |
| B08 Predicted, then found | 4.24 -> sixth -> sixth; 12.56 -> fourteenth -> fourteenth | PASS. Formula line is small grey text (see risks). |
| B09 Second dial | wedge, 0.271 -> 0.215, strip with old and new breaks, predicted/found | PASS. Strip has no per-speed labels (2.0 and 3.0 pair by order). |
| B10 A different field | both fields, 0.271 vs 0.1875, three speeds predicted/found | PASS. Speech names two speeds; the table shows all three. |
| B11 Which rule | three cards: dial one, dial two, no speed-up | PASS. |
| B12 Does not claim | four exclusions | PASS. Right half empty by design. |
| B13 Your turn | formula, 0.225, quarter-speed above, fifth-speed below | PASS as the answer frame. The five-second withheld frame is a variant of this slate (answer lines hidden). |

## Production gate (stills level)
| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | PASS at 4K for the large type. **Risk:** the smallest captions are 24 logical px, about 5 px at phone width. Fine for a 16:9 long film on a TV or desktop; the Short must be laid out for its own size. |
| Sources on screen | PASS. "OUR MODEL" settings chip on every slate that uses the field; B01 carries the essay source line; formulas shown where the figure comes from. |
| Side-by-side at the moment of comparison | PASS. B06 lanes, B08 table, B09 strip + rows, B10 two fields + table. |

## Not yet tested (motion and timing)
Shot counter running, bars stepping down (B07 as animation), ticks-then-count (B09), five-second hold (B13), fades. Pillow fades must be
measured on pixels (alpha is ignored), per the earlier lesson. None of this is judged from stills.

## Do next
1. [EDIT] Your notes on the stills. Collect every change, apply once, rebuild once.
2. Then: audio (Kokoro phoneme check first), cue timing on the Whisper clock, motion for B00, B07, B09, B13, one compile, PROOF on frames.
