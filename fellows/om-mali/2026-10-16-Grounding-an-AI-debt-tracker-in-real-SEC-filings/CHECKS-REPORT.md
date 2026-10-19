# CHECKS-REPORT — grounding-an-ai-debt-tracker-in-real-sec-filings

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the week's actual instruction — *ground it before you build it* — and lands three answer lines, which are the three findings. COLD OPEN LAW: the ask lands ANSWERED. |
| B01 | SHOW | Claim: debt is paying for the build-out and nothing watched it. Two bars on **one scale**, so 4.3× is seen rather than asserted, with the gap named beneath them as the reason the project exists. |
| B02 | SHOW | Claim: what the agent will do. Four stages land left to right, the ledger accented; then the **tense note** lands, in writing, saying the boxes are a design and not a status. |
| B03 | SHOW | Claim: the answer is published after the evidence. A dashed rule **descends** from the filed ledger to the later report — the grading relation is drawn, not implied — and the refusal lands under both boxes. |
| B04 | SHOW | Claim: two ways it could fail, tested first. Two bars, each carrying its **own** pass mark, because the two marks are different numbers and both were written down beforehand. The conservative/raw split lands as a footnote. |
| B05 | SHOW | Claim: fifteen, not twenty-one. The assumption is bracketed **first**, in outline; the same 25 companies then fill in beneath it, partitioned three ways. One row, not three bars — the beat is that a fixed set splits differently once coverage is measured. |
| B06 | SHOW | Claim: 400 of 495 were never touched. The count breaks into its two parts with the held-back set accented and badged, then **one** gauge fills past its pass line, with the all-quarters figure as a footnote. |
| B07 | SHOW | Claim: the smallest model won. Three models on one scale under **one** dashed rule drawn straight down all three tracks, because one pass line was fixed before the test and all three were held to it. Loop counts sit beside each bar. |
| B08 | SHOW | Claim: five numbers and the limit that narrows each. Each limit is drawn **beside the claim it narrows**, never as a free-floating caveat list. The 99% takes the accent, because it is the number most likely to be over-read. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## ILLUSTRATE LAW — no two consecutive body beats share a scheme

```
B01  two bars, one scale, value beside each
B02  four bordered stage boxes in a row, joined by arrows
B03  two cards joined by a drawn dashed descent
B04  per-row bars, each with its OWN mark
B05  ONE partitioned row of 25, under a ghost bracket
B06  a count split into parts, then a single wide gauge
B07  three bars under ONE shared rule, with loop badges
B08  claim/limit pairs, no chart at all
```

B04, B05 and B07 all involve bars and are deliberately different objects: B04 gives each test
its own mark because the marks differ; B05 draws no marks at all, because its argument is a
partition and an overlay; B07 draws one continuous rule through all three tracks because one
rule was set for all three models. B06 sits between B05 and B07 and is a count plus a gauge.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B05's third
  segment at 0.44 and the ghost bracket's outline, which is a rule rather than a filled shape
- Comparisons shown side-by-side, held ≥2s ✓ — B01's two bars, B04's two tests, B05's assumed
  21 over the measured 15, B06's 95 against 400 and B07's three models all persist to the end
  of their beats

## Teaching arc

```
FRAMEWORK ✓      B01/B02 — the gap first, then what would fill it, with the tense stated
                 so the design is not mistaken for a status report
WORKED EXAMPLE ✓ B03/B04 — one real grading relation, followed to the refusal that makes it
                 honest, then the two failure modes actually tested on 46 real quarters
COMPLICATION ✓   B05/B06 — the answer key turns out to be coarser than assumed, which
                 changes what the agent may be graded on at all
MEASUREMENT ✓    B07 — three models, one prompt, one pass line fixed in advance
LIMITS ✓         B08 — every number above, paired with what narrows it
HANDOFF ✓        B10 — inspect your ground truth before you build on it
```

## SHOW-DON'T-TELL spot checks

- "4.3×" is never spoken as a claim: the two bars are drawn on one scale and the multiple is
  derived from them at injection.
- "Fifteen, not twenty-one" is drawn as an outline over a fill, so the viewer sees the
  assumption shrink rather than being told that it did.
- "Held back" is drawn as a badge on the larger of the two parts, not as a sentence.
- "The smallest won" is drawn by putting the 4B row first and letting its bar pass the other
  two under a shared rule.
- B02's "none of this is built yet" is the one place the reel tells rather than shows, and it
  does so deliberately: there is no honest way to *draw* the absence of an agent, and the
  alternative is a diagram that lies by implication.

## Known risks carried into QC

1. **B05 is the densest frame** — a partitioned row, a ghost bracket, three labels under their
   own segments, two examples and a gate note. If portrait underfills or the third segment's
   label crowds, rescale rather than dropping the gate note; the 4–4 tie is in FACTCHECK row 15.
2. **B07's shared rule is drawn past the top and bottom of each track** so the three segments
   read as one line. Check at 4K that the segments align, and that the rule is not mistaken
   for a bar edge.
3. **B01's value sits beside its bar.** The track reserves a fixed column for the value; the
   first build of this figure bled `$121bn` past the title-safe edge.
4. **B06 has two numeric blocks and a gauge**, which is a lot of baseline alignment. Watch the
   divider between the total and the parts in portrait, where it becomes horizontal.
