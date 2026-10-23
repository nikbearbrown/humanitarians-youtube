# CHECKS-REPORT — entity-resolution-and-the-golden-set

PROOF GATE, written **before** the first slate compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the ask and lands three answer lines — motion is the type-on and the result reveal. The interface IS the subject (COLD OPEN LAW). |
| B01 | SHOW | Claim: resolution gates pricing. Enacted — a three-link chain draws and the MIDDLE link visibly breaks, then two cards land and the second takes the accent while the first dims. The argument is made by which card survives. |
| B02 | SHOW | Claim: 128 spellings inside 3.2M names. Seven bars grow per company, a total resolves to 128, a column of REAL filed strings scrolls, and the haystack counter races to 3,204,853. |
| B03 | SHOW | Claim: one labelled set judges both systems. Two counters race to 322 and 7,276, then arrows fork out of the ONE card into two named systems — the fork is the claim. |
| B04 | SHOW | Claim: recall moved, precision did not, and the hardest cases went the other way. The recall cell lands terracotta, a delta note marks precision as noise, and a hardest-cases strip drops in showing the matcher LOSING. |
| B05 | SHOW | Claim: one character hid 85 holdings. Two spellings set at display size around a fixed-width dot slot — filled in one row, an empty dashed slot in the other — then the counter races to 85. |
| B06 | SHOW | Claim: OpenAir.com was OpenAI. Five real rows land at 687.6869, then the OpenAI anchor drops in beneath at the identical price in the same column, and the approved stamp is struck and re-set. |
| B07 | SHOW | Claim: the approval was withdrawn and both scores published. The written reason is struck through, three act chips land in sequence, and two score cards sit side by side — neither hidden. |
| B08 | SHOW | Claim: no cut-off separates four identical scores. A dashed cut-off sweeps down the score column and stalls; the four rows are then bracketed as a review band. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B01's
  dimmed first card at 0.58 and B08's un-lit row notes at 0.35→1.0 as they light
- Comparisons shown side-by-side, held ≥2s ✓ — B04's two metric rows, B05's two spellings,
  B07's two score cards and B08's four tied scores all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01/B03 — why resolution gates pricing, then the instrument built to test it,
                 both before any score is quoted
WORKED EXAMPLE ✓ B05 — one concrete string pair (X.AI CORP / XAI CORP) and exactly what it cost
FALSIFIABILITY ✓ B04 — the new system LOSES on the hardest cases and the beat says so;
                 B06/B07 — the test overturned a label the author had approved, and the
                 pre-fix score is published beside the post-fix one;
                 B08 — the limit that no threshold fixes
SCAFFOLDED TASK ✓ B10 — label 30 rows of your own data, score your existing logic against them,
                 then find out what your own labelling got wrong
BOOKENDS ✓       B00 cold open · B01 BLUF · B09 verdict · B10 handoff · B11 outro
NO-SOURCE-NO-VERDICT ✓ every figure is a prop injected from figdata_week4.json; the injection
                 ASSERTS the universe count (7) and spelling total (128) and fails the build
                 otherwise — the same class of error the worklog caught in the source figure
```

**0 violations.** Three authoring judgment calls are logged in `BUILD-LOG.md` rather than
passed silently: the three script-section splits, the ~130 words of connective narration added
to fill eight body beats, and the three wording changes recorded in `FACTCHECK.md`.
