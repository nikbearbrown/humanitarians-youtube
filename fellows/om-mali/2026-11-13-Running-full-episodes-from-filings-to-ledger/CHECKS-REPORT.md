# CHECKS-REPORT — running-full-episodes-from-filings-to-ledger

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the week's actual instruction — *run the whole thing, then score it against doing nothing* — and lands three answer lines. COLD OPEN LAW: the ask lands ANSWERED, and the third answer line is the cost, not a reveal held for later. |
| B01 | SHOW | Claim: the pieces now run as one graph. Five nodes left to right, and **the middle node is not a node** — it is three readers drawn side by side under "in parallel (Send)", which is the one structural fact that is new this week. |
| B02 | SHOW | Claim: the second half is code, and the start was borrowed. Two ledger panels with **the four operations literally between them**, the opening panel wearing a BORROWED chip, and ASK accented with 53 beside it. |
| B03 | SHOW | Claim: one number up, one number down. Four bars, one scale; the accent means "the tracker" on both rows, so **the second pair reads as the accent bar falling short of the ink one**. |
| B04 | SHOW | Claim: carrying forward finds none of them. **34 cells, twice** — 30 filled in the accent, then a row of 34 that stays empty. |
| B05 | SHOW | Claim: 66 added, 26 of them wrong, and all 26 named. One band split five ways with its counts beneath, **bracketed into 40 real and 26 not**, then a legend carrying three defect ids and one explicit absence. |
| B06 | SHOW | Claim: the bug was a sense of time, not a misread. **Two windows against one boundary** — the first running past the quarter end, the second stopping at it — with both runs' precision beneath. |
| B07 | SHOW | Claim: three checks, and none of them says what it looks like it says. Five bars on one track with **one dashed line drawn on the track that owns it**, and a qualifier under each result. |
| B08 | SHOW | Claim: five numbers and the limit that narrows each — and nobody has checked any of it. The **gate record is drawn as the largest object on the frame**. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## ILLUSTRATE LAW — no two consecutive body beats share a scheme

```
B01  five process nodes left to right, the middle one exploded into a parallel fan-out
B02  two ledger panels with a four-row operation list between them — no arrows, no chain
B03  two metric pairs, four bars, ONE shared scale and a two-swatch legend
B04  the same 34 cells drawn twice: 30 filled, then 0 filled
B05  ONE continuous band of 66 split five ways, with brackets and a legend
B06  a span: two windows measured against one dashed boundary, then two figures
B07  five bars on one track, one dashed line on one of them, a qualifier under each
B08  claim/limit pairs, a boxed gate record, then a next-steps list
```

The two bar beats, **B03 and B07, are deliberately not adjacent**, and they are different
objects: B03 is two *pairs* on one scale where the comparison is between members of a pair
and there is no threshold at all; B07 is five independent results on one track with a single
threshold that belongs to exactly one of them and is drawn on that one only.

**B04 and B05 are adjacent and both count things**, which is the one adjacency that needed
work. They are different objects and deliberately so: B04 draws 34 *discrete, countable*
cells twice because the claim is about a zero that must be seen to be a row of missed
chances; B05 draws one *continuous* band split proportionally because the claim is about
shares of a whole. The adjacency is also the argument — the beat that counts what reading
found is immediately followed by the beat that counts what it cost, and neither is allowed
to stand alone.

**B01 and B02 are adjacent and both describe mechanism.** B01 is a chain of process nodes
with a fan-out; B02 has no chain at all — it is two end-state panels with a list of
operations sitting between them, and its subject is not the sequence but the fact that the
left-hand panel was handed over rather than computed.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B05's
  unnamed-misread segment at `GHOST` 0.55 and B04's unfilled cells, which are outlined at
  full border weight
- Comparisons shown side-by-side, held ≥2s ✓ — B03's four bars, B04's two cell rows, B05's
  five segments, B06's two windows and B07's five bars all persist to the end of their beats

## Teaching arc

```
MECHANISM ✓      B01/B02 — the graph that runs a quarter, and the code that closes it —
                 including where its starting ledger came from
MEASUREMENT ✓    B03 — the result against doing nothing, both halves on one frame
WORKED MEANING ✓ B04 — what the metric that rose is actually about: new bonds
COMPLICATION ✓   B05 — and what the metric that fell is about: 26 additions, each named
FAILURE ✓        B06 — a bug the first run had, with the first run's number still on screen
FALSIFIABILITY ✓ B07 — three held-out checks, one of which failed last week on the same rule
LIMITS ✓         B08 — every number above, paired with what narrows it, and the gate record
HANDOFF ✓        B10 — measure doing nothing before you measure the clever version
```

NO-SOURCE-NO-VERDICT ✓ — every body beat carries a `SOURCE:` line naming the project file
the figure came from, and every one of those files is named in `FACTCHECK.md`.

## SHOW-DON'T-TELL spot checks

- "They run at the same time" is drawn by replacing one node with three stacked readers
  under a `Send` label — the only place in the chain where one box becomes several.
- "The opening ledger is borrowed" is drawn by putting a BORROWED chip on the left panel,
  on the same frame as the mechanism rather than in a footnote under it.
- "Anything it cannot place becomes a question" is drawn by making ASK the one accented
  operation and putting 53 beside it at display size.
- "Recall rose and precision fell" is drawn by giving the tracker the accent on both rows,
  so the second accent bar visibly stops short of the ink bar beneath it.
- "Carrying forward finds none of them" is drawn as 34 cells that stay empty beside 34 where
  30 fill — a zero as a row of missed chances rather than as an empty rectangle.
- "26 of the 66 were not in the report" is drawn by bracketing the band in two, under the
  counts, so the ratio is read off the width before any legend is read.
- "Not a misread — a bond in the wrong quarter" is drawn as two windows against one dashed
  boundary, because the bug was a span and not a value.
- "Both runs are reported" is drawn by printing 89.2% and 90.2% side by side at the same
  size, rather than quoting the better one and footnoting the other.
- "The reader is not more accurate" is drawn by letting B2's ink bar run longer than the
  accented reader bar on the same track.
- "Nobody has reviewed this" is drawn by making the gate record the largest box on B08.
- B02's BORROWED chip and B08's gate row are the two places the reel tells rather than
  shows: there is no honest way to *draw* the absence of a review, or the provenance of a
  ledger that was handed over.

## Known risks carried into QC

1. **B05's band has five segments and the smallest is 2 of 66.** At 1728 px that segment is
   ~19 px wide in landscape and ~28 px in portrait, and it carries a centred count beneath
   it. Check the "4" and the "2" do not collide, and that the unnamed segment is still
   visibly a segment rather than a seam. **Read this frame.**
2. **B05's bracket labels are centred under spans of very different widths.** The "26 not in
   the report" bracket spans only 39% of the band; its label is longer than its bracket.
   Check it does not run past the right edge.
3. **B04's cell grid is 17 per row in landscape and 9 in portrait**, so 34 forms two tidy
   rows in 16:9 and a ragged 9/9/9/7 in 9:16. Check the ragged last row still reads as
   "thirty-four" rather than as a rendering fault.
4. **B06's boundary is drawn from the fixed band's span**, not from a separate prop, so the
   dashed rule and the end of the second window are the same instant by construction. If the
   band spans are ever edited apart, the picture quietly stops being true — check they line
   up at 4K.
5. **B06's axis labels sit at the two ends of one row with the boundary label above.** The
   right-hand label is the longest string on the frame. Check it wraps inside its `maxWidth`
   and does not meet the boundary label in portrait.
6. **B07 is the densest beat in the reel** — five bars, a line label and three multi-line
   qualifiers, one of which runs to about 330 characters. It is the most likely to overflow
   its column and let the Source line draw across something. **Check the foot of the frame.**
7. **B03's legend and B07's pass line are both single-instance elements.** A legend that
   scrolls off, or a dashed line that lands under a full bar, breaks the only thing making
   the bars readable. Check both at 4K in both orientations.
8. **Portrait underfill.** It has been a risk every week since week 5 of the earlier series.
   Week 4 was the first episode to need no portrait body rescale, because every bar component
   computed a per-orientation `BESIDE`. Every bar component here does the same — but B01's
   five-node column and B04's four-row cell grid are new shapes in portrait and have never
   been laid out before. Budget for a rescale pass.
