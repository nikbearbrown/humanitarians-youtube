# CHECKS-REPORT — building-the-answer-key-grader-and-baseline

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the week's actual instruction — *build what will grade it, before it exists* — and lands three answer lines, which are the three findings. COLD OPEN LAW: the ask lands ANSWERED. |
| B01 | SHOW | Claim: the answer key is big, and uneven. Three counts land, then **one** bar the width of the whole 1,093 splits into its three grading levels. The segments are the reports counted above them, so the partition is the same object, not a second chart. |
| B02 | SHOW | Claim: a score is only as honest as its rule. Three mode cards land coarsest-last — the order the grader falls back through — then the four field chips, then the pairing constraint in **its own block**, because it is the part a viewer would never guess. |
| B03 | SHOW | Claim: every disagreement was my bug. Five numbered rows, each naming the company whose printed table exposed it, then the verdict beneath them in the accent. Five concrete defects, not a sentence admitting mistakes. |
| B04 | SHOW | Claim: which of these two numbers is evidence. Two bars above a **dashed rule**, one below it. Above: the ten reports that found the fixes. Below: the three picked first and graded once. The rule is the argument. |
| B05 | SHOW | Claim: a flattering number with a zero inside it. The track is drawn and **held empty** at hero scale with the word inside it; the 90.7% and the 18 of 47 land underneath, smaller. |
| B06 | SHOW | Claim: the distance is the opportunity. One axis per claim, with the gap from what copying forward catches to what was announced drawn as a **span with an arrowhead**. Two bars would show two quantities; the distance is the beat. |
| B07 | SHOW | Claim: the evidence moved under the experiment. One filing's marker is drawn where it was, then travels along a dashed track to where it now is, with the shift named above it and the fix below. |
| B08 | SHOW | Claim: five numbers and the limit that narrows each. Each limit is drawn **beside the claim it narrows**, never as a free-floating caveat list. The 10 of 10 takes the accent, because it is the number most likely to be over-read. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## ILLUSTRATE LAW — no two consecutive body beats share a scheme

```
B01  three counts, then ONE partitioned full-width bar
B02  a rule card — mode boxes, field chips, a constraint block
B03  five numbered rows, no chart at all
B04  bars split by a dashed rule into calibrated and measured
B05  ONE outlined track, held EMPTY, with the numbers beneath it
B06  ONE axis per claim, with the gap drawn as a span
B07  a timeline whose marker travels
B08  claim/limit pairs, then a next-steps list
```

B04, B05 and B06 are the adjacency to watch, since all three involve a horizontal track. They
are deliberately different objects: **B04** fills bars and divides them with a rule; **B05**
draws one track and leaves it empty, which is the only thing on the frame doing any work;
**B06** puts two readings on a single axis and draws the distance between them. If any of the
three is ever "simplified" into ordinary bars, the beat it belongs to stops arguing.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B01's third
  level segment at 0.52
- Comparisons shown side-by-side, held ≥2s ✓ — B01's three levels, B04's calibrated pair
  against the measured one, B05's empty track against the two numbers below it, B06's two
  positions on each axis and B07's two markers all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01/B02 — what is being graded, and the exact rule it is graded by, before
                 any score appears
WORKED EXAMPLE ✓ B03 — ten printed tables, five real defects, each named with the company
                 that exposed it
COMPLICATION ✓   B04 — the score that followed the fixes is not evidence, and the one that is
                 is lower and smaller
MEASUREMENT ✓    B05/B06 — the floor, and the distance between the floor and what the filings
                 already announced
SURPRISE ✓       B07 — the timestamps moved, so the cut-off stopped depending on a clock
LIMITS ✓         B08 — every number above, paired with what narrows it
HANDOFF ✓        B10 — check the harness, not the model
```

## SHOW-DON'T-TELL spot checks

- "Most reports list debt bond by bond" is drawn by the width of one segment against the other
  two on a single bar, not asserted.
- "A calibration, not a score" is drawn as a rule with two bars above it and one below.
- "Caught none of them" is drawn by outlining a track and leaving it empty — and labelling the
  emptiness, so it cannot be read as a missing element.
- "The gap the agent has to win" is drawn as a measured distance with an arrowhead, on the
  same axis as both readings.
- B02's subtitle ("The agent is not written yet") and B08's last row are the two places the
  reel tells rather than shows, deliberately: there is no honest way to *draw* the absence of
  a thing, and the alternative is a frame that lies by implication.

## Known risks carried into QC

1. **B05's empty track is the one frame a fill check will dislike.** It is supposed to be
   mostly empty — that is the argument. If GATE V flags canvas fill on B05, read the frame
   before changing anything; the fix is never to put a bar in it.
2. **B06 positions labels absolutely against computed x offsets.** The baseline reading sits at
   x = 0 on both axes, so its label starts at the left edge; the announced label is
   right-aligned. Check at 4K that neither collides with the span's arrowhead.
3. **B07's two markers can overlap** if the shift distance is ever shortened. They are placed
   at 26% and 62% of the content width, far enough apart to read as two events.
4. **B01's legend carries the counts, not the segments.** A segment 41 of 1,093 wide cannot
   hold a label and shrinking type until it fits would make it unreadable. Do not move the
   numbers into the bar.
5. **Portrait will underfill.** Six of eight body beats did on week 1 and the fix was 73 raised
   `f(landscape, portrait)` values. Expect a second portrait pass here and budget for it.
