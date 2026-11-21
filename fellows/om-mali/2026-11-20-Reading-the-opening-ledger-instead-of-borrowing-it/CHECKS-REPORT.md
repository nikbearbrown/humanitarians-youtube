# CHECKS-REPORT — reading-the-opening-ledger-instead-of-borrowing-it

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the week's actual instruction — *stop handing the agent an opening ledger from the answer key* — and lands three answer lines. COLD OPEN LAW: the ask lands ANSWERED, and the third line says this week undoes last week's headline. |
| B01 | SHOW | Claim: twenty-six down to three. **Two bars on ONE count scale**, 6px per bond, so 3 against 26 is read as a length. Three actions beneath, each with its defect id, labelled as actions rather than as a breakdown. |
| B02 | SHOW | Claim: the model points, code reads. **Code → model → code**, the middle card the only accented one and the only one not labelled CODE, carrying the `qwen3:4b` chip. |
| B03 | SHOW | Claim: the model buys recall, not precision. **Two metric pairs on one scale**, each pair's gap printed — a large one on recall, an almost-flush one on precision. Both denominators (94 read, 43 graded) ride in the subtitle. |
| B04 | SHOW | Claim: the same report answers differently. **Two counts under a single bracket** that names the one report, so the frame cannot be read as two. |
| B05 | SHOW | Claim: the advantage was the borrowed ledger. **Six bars, one scale**: on recall the accent bar and the B0 bar end at the same place; on precision the accent bar runs past it. |
| B06 | SHOW | Claim: the gap is concentrated. **Four named companies**, each with the table it hid — and the one refusal set apart in its own accented block, because it is not a miss. |
| B07 | SHOW | Claim: it notices about a third of the time. **50 cells with 17 filled, 36 with 11**, so what the eye lands on is the 33 that got through. |
| B08 | SHOW | Claim: five numbers and the limit that narrows each. The **gate record is drawn as the largest object on the frame**; total debt takes the accent. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## ILLUSTRATE LAW — no two consecutive body beats share a scheme

```
B01  two bars on a COUNT scale (bonds, not percent) + a three-row action list
B02  three process cards, code → model → code, the middle one accented
B03  two metric PAIRS on a percent scale, each pair's gap printed
B04  two big counts in cards, under one bracket — no track, no scale
B05  three-row groups × two metrics: six bars on one percent scale
B06  four named rows, then one set-apart accented block
B07  two grids of countable cells (50 and 36), then a plain figure
B08  claim/limit pairs, a boxed gate record, then a next-steps list
```

**Three bar beats need separating, and two of them are adjacent to nothing.** B01 is a
*count* scale (bonds), has two bars and no percentages at all. B03 is two *pairs* where the
subject is the distance inside each pair. B05 is three *rows* per metric where the subject is
two bars ending level. B01→B03 are separated by B02; B03→B05 by B04.

**B04 and B06 both use rows of text** and are separated by B05. They are different objects:
B04 is two numerals at display size with almost no prose; B06 is four company names each with
a sentence, and ends in a bordered block rather than a figure.

**B07 is the only cell beat** in the reel.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B05's
  B0 rows at `SOFT` 0.74 and B07's unfilled cells, which keep a full-weight border
- Comparisons shown side-by-side, held ≥2s ✓ — B01's two bars, B03's two pairs, B04's two
  counts, B05's six bars and B07's two grids all persist to the end of their beats

## Teaching arc

```
MECHANISM ✓      B02 — what the opening reader is, and the rule it inherits
MEASUREMENT ✓    B01, B03 — the fixes landed; the reader scores what it scores
FALSIFIABILITY ✓ B04 — the same input, asked twice, gives two answers
THE CHECK ✓      B05 — the week's actual ablation, and the claim it takes away
DIAGNOSIS ✓      B06 — where the cost sits, by name, and which part is not a defect
SELF-KNOWLEDGE ✓ B07 — can the system tell when it got it wrong? A third of the time
LIMITS ✓         B08 — every number above, paired with what narrows it, and the gate
HANDOFF ✓        B10 — find the convenience inside your own evaluation and remove it
```

NO-SOURCE-NO-VERDICT ✓ — every body beat carries a `SOURCE:` line naming the project file
the figure came from, and every one of those files is named in `FACTCHECK.md`.

## SHOW-DON'T-TELL spot checks

- "Twenty-six down to three" is drawn by giving both bars one px-per-bond unit, so the
  second bar is a stub rather than a second number.
- "Level with doing nothing, not better" is drawn by printing B0's figure in the same
  sentence as the result, and by the build refusing to write a sheet if the gap exceeds a
  point.
- "The model points, code reads" is drawn by putting CODE on both sides of it and making
  the model's card the only one in the accent.
- "The model buys recall, not precision" is drawn by printing both gaps — one large, one
  almost nothing — beneath their own pairs.
- "Same report, different answer" is drawn by bracketing the two counts under the one
  report's name, which is the entire difference between variance and two measurements.
- "Level with doing nothing" is drawn by the accent bar and the B0 bar ending at the same x
  on the recall rows, with no annotation needed.
- "Most of it is a few companies" is drawn by naming the four and the table each one hid.
- "It notices a third of the time" is drawn as 33 empty cells beside 17 filled ones.
- "Nobody has reviewed this" is drawn by making the gate record the largest box on B08.
- B02's "deliberately" and B08's gate row are the two places the reel tells rather than
  shows: there is no honest way to *draw* an intention, or the absence of a review.

## Known risks carried into QC

1. **B05 is the densest layout in the reel** — two metric groups of three rows each, six
   bars, six labels with sub-notes, then a cost line and a verdict. It is the most likely to
   overrun its portrait column and let the FootNote rule draw through the line above it,
   which is exactly what week 5's B01 did. **Read this frame in 9:16 first.**
2. **B05's argument is two bars ending at the same x.** Agent 90.1% and B0 90.9% differ by
   0.8 points — about 8px on a 1000px track. Check at 4K that they read as level and that
   the B0 bar is very slightly longer, which is the truth.
3. **B07 draws 86 cells.** Landscape packs 50 into two rows of 25 and 36 into two of 18;
   portrait into five of ten and four of nine. Check no row is ragged in a way that makes
   the count look approximate, and that the cells stay inside the safe area.
4. **B01's two bars share a unit derived from the larger count.** The 3-bar is 11.5% of the
   track — small by design. Check it is still visibly a bar and not a seam.
5. **B03 prints a gap figure under each pair.** The precision pair's gap is +0.9 points,
   which is ~9px. Check the figure does not look like it is labelling the wrong pair.
6. **B04 uses display-size numerals (96px landscape).** Check the two cards do not crowd the
   bracket beneath them, and that the bracket's caption is legible at its smaller size.
7. **B06's rule block is bordered and accented** while the four cases above are plain rows.
   Check the block does not read as a fifth case.
8. **B08 carries five claim/limit pairs plus the gate and three next steps** — the same
   shape that has overrun before. Check the foot of the frame in both orientations.
9. **Portrait budgets.** Week 5's lesson is written into this chassis: portrait type on B06,
   B07 and B08 is set lower than landscape rather than inherited. Verify rather than trust.
