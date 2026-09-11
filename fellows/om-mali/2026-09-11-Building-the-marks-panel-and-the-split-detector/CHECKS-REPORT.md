# CHECKS-REPORT — building-the-marks-panel-and-the-split-detector

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the ask and lands three answer lines — motion is the type-on and the result reveal. The interface IS the subject (COLD OPEN LAW). |
| B01 | SHOW | Claim: the arithmetic is one line and the judgment is the week. Enacted — the formula sets, the mark count resolves under it, two halves land with the detector in terracotta, and a `decide` chip lands and is **struck through**. The division of labour is performed, not announced. |
| B02 | SHOW | Claim: every filed row accounts for itself. The subtraction happens on screen — 5,806 counts up, 28 and 72 are deducted with their reasons, 5,706 rules off, and 5,479 marks resolve. "Reconciles" is shown, not asserted. |
| B03 | SHOW | Claim: a split is indistinguishable from a crash. A line runs flat and then falls off a cliff to the filed after-price; the −92% reading lands and is struck; the real cause replaces it. The viewer feels the drop before it is explained. |
| B04 | SHOW | Claim: the window was too narrow to catch its own test case. A number line draws, the old ±0.02 box is a visible sliver, the 11.93 mark lands **outside** it, and the gap between them is measured on screen. The new relative window then draws wide enough to contain the mark. |
| B05 | SHOW | Claim: the share count decides what the ratio cannot. Three real filed rows land; the share column lights on the ×10 step while the two filed values are bracketed as identical to the cent. |
| B06 | SHOW | Claim: a person made every call. The two-line rule sets first, then each case is tested against it — Anthropic's constant share count and reversing step, SpaceX's constant count and exact doubling, Perplexity's moving count. The reviewer's name lands against all three. |
| B07 | SHOW | Claim: ratio is not factor. 11.93 sets alone, decomposes into a 10-for-1 split and a 16% markdown, then two divisors are compared by what each does to a real price move. Only the correct one keeps the accent. |
| B08 | SHOW | Claim: six pass, one is unreachable, none fail — counted, not asserted. Seven rows tick in sequence, the seventh lands hollow carrying its reason, and the check that expected 4 managers resolves to the measured 10 in two clusters. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B07's
  wrong-divisor card at 0.72 and B04's old-window box at 0.55
- Comparisons shown side-by-side, held ≥2s ✓ — B01's two halves, B03's naive-vs-real pair,
  B04's two windows, B05's three filed rows, B06's three cases, B07's two divisors and
  B08's two price clusters all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01/B02 — what a mark is and where every one came from, stated before any
                 claim about the detector
WORKED EXAMPLE ✓ B03→B07 — one company, one step, followed the whole way: it looks like a
                 crash, the window missed it, the share count identifies it, a person rules
                 on it, and the ratio turns out not to be the factor
FALSIFIABILITY ✓ B04 is the author's own bug, on screen, measured: the window was too narrow
                 to catch the case plan.md names, and it looked fine only because a second
                 case happened to land inside it;
                 B08 publishes an unreachable check as unreachable rather than as a pass
SCAFFOLDED TASK ✓ B10 — find an absolute threshold in your own code, find the case it was
                 written for, and test whether it would still catch that case today
BOOKENDS ✓       B00 cold open · B01 BLUF · B09 verdict · B10 handoff · B11 outro
NO-SOURCE-NO-VERDICT ✓ every figure is a prop injected by build_beat_sheet.py from
                 figdata_week7.json; the injection ASSERTS the 5,806→5,706 reconciliation,
                 the 5,479 marks, the 301 blocks summing by reason, the 7 split-blocked
                 marks, the relative 1% rule, the 11.93 ratio against its 10.0000 decided
                 factor, the ×10 share count at an unchanged value to the cent, Anthropic's
                 single share count across 13 quarters, SpaceX's exact doubling, and the
                 6/0/1 check split — and fails the build otherwise
```

**0 violations.** Three authoring judgment calls are logged in `BUILD-LOG.md` rather than
passed silently: the six script sections split into eight body beats, naming the security
class on B05 and B04 so two different Perplexity lines are not conflated, and moving the five
source figures into `pantry/`.

## The one number not under an assertion

`figdata_week7.json` carries the tolerance that **ships** (relative 1%). It does not carry the
**old** absolute window, ±0.02 — that comes from `narration_script.md` and `plan.md`. It is
passed into the build as a named constant, and B04's on-screen source line says so rather than
citing a file that does not contain it. `FACTCHECK.md` row 9 is the row to read.

## What this cut is asked NOT to do, and does not

The README names two, and the script's Notes add three more:

| The source says | This cut |
|---|---|
| **The detector was not broken; it was too narrow** | B04's stamp reads "Not broken. Too narrow." The word "broken" appears nowhere in the narration, and the beat shows the step that *did* land inside the window — which is why the bug looked fine. |
| **The splits are not adjusted** | Nowhere. B02 shows the 7 marks blocked "awaiting adjustment (Week 8)", B07 ends on "Week 8 divides by the decided one", and B09 repeats it. |
| Say "ten-for-one", not "ten to one"; "nought point nought two", not "point oh two" | B04 and B07 narration use exactly those spoken forms. |
| Say the share counts slowly | B05 speaks both counts in full at 59 words over 17.3s, the slowest per-word pace of any body beat in the reel. |
| The strongest beat is "catching it is not deciding it" | B05 and B06 are two beats rather than one clause, and B06 opens on the rule at display size before any case is shown. |
| A "mark" is not a valuation of the company | B02's subtitle defines it: one fund's recorded price for one security at one period end. |
