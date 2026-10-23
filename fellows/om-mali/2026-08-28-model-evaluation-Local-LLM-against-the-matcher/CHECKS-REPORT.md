# CHECKS-REPORT — measuring-a-local-llm-against-the-matcher

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the ask and lands three answer lines — motion is the type-on and the result reveal. The interface IS the subject (COLD OPEN LAW). |
| B01 | SHOW | Claim: the rules keep the job, and the model fails in one direction. Enacted — two system cards land, a delta bar DRAWS the 5.1-point drop, a flat line confirms recall did not move, and NOT ADOPTED stamps. The verdict is reached on screen, not announced. |
| B02 | SHOW | Claim: both systems see the same evidence. Four field cards land one at a time carrying a REAL golden-set row; two withheld chips are struck through; the run stats count up to 322 / 0 / 3.24s / 17 min. |
| B03 | SHOW | Claim: five points is not survivable. Two precision rows set, then the frame switches UNIT and the same error re-counts as records — the 196 bar runs the full column against the 1. The unit switch is the argument. |
| B04 | SHOW | Claim: it invented a corporate fact. The model's own sentence is quoted verbatim, then the parent-company clause is struck through left-to-right while a rebuttal lands beneath and the confidence chip fills to 0.95. |
| B05 | SHOW | Claim: it matched on a resemblance, and that resemblance is priced. The shared characters light in BOTH strings; 32 record marks then fill one at a time and the running wrong-record count steps 1 → 33. |
| B06 | SHOW | Claim: there was nothing there to find. Twelve character slots land alone on the cream and exactly three light — the overlap is counted on screen, not asserted. |
| B07 | SHOW | Claim: confidence does not sort right answers from wrong ones. 322 dots fill and the 1.000 block lights as one mass. The 12 errors the model was **sure** about are solid terracotta INSIDE that mass; the 3 it was unsure about are hollow. The encoding carries the claim exactly — rendering all 15 solid would put three answers in the confident block that never claimed to be there. A legend states it. |
| B08 | SHOW | Claim: a perfect score on four rows is not evidence. Two direction counters (14 added, 1 removed) land, the four rows follow in full, then 1.0000 sets at display size and is struck by SWITCHED OFF with the sample size at the same weight. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`. B06 is deliberately the
  emptiest frame in the reel; the script asks for the code to sit alone.
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B07's
  pre-mass dot field at 0.30 rising to 0.92 as the block lights, and B05's unfilled record
  marks at 0.50
- Comparisons shown side-by-side, held ≥2s ✓ — B01's two system cards, B03's two precision
  rows AND two record bars, B05's two lit strings and B08's four rows all persist to the
  end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01/B02 — what is being compared and on what evidence, stated before any
                 score is quoted, including what BOTH systems are denied
WORKED EXAMPLE ✓ B04/B05/B06 — three concrete filed strings, the model's verbatim reason for
                 each, and the holdings each one would have mispriced
FALSIFIABILITY ✓ The whole reel is a negative result the author pre-committed to publishing.
                 B03 quantifies the loss; B07 kills the author's own stated plan for next
                 week; B08 refuses to quote a flattering 1.0000 without its sample size
SCAFFOLDED TASK ✓ B10 — pre-commit the decision rule BEFORE running the model, score both on
                 the same cases, then test whether confidence separates right from wrong
BOOKENDS ✓       B00 cold open · B01 BLUF · B09 verdict · B10 handoff · B11 outro
NO-SOURCE-NO-VERDICT ✓ every figure is a prop injected by build_beat_sheet.py from
                 figdata_week5.json; the injection ASSERTS the 8B size, the 322/0 call
                 count, the 11 candidates, both precisions, the 1→196 record count, the
                 14-added/1-removed direction, the 315-at-1.000 confidence block and the
                 4 veto rows, and fails the build otherwise
```

**0 violations.** Three authoring judgment calls are logged in `BUILD-LOG.md` rather than
passed silently: the five script sections split into eight body beats, the connective
narration added to fill them, and the shortening of the veto holding names at the exposure
clause (disclosed on screen).

## What this cut is asked NOT to do, and does not

The script's Notes carry five explicit prohibitions. Each is checked here because they are
the kind of thing a rebuild quietly loses:

| The script says | This cut |
|---|---|
| Do not apologise for the result | No apology anywhere. B01 states the outcome flatly in the first ten words; B08 says "I built it, measured it, and left it switched off" without softening. |
| Don't say the model is useless | B08's closing line is "a decent sceptic and a poor proposer" — mis-scoped, not useless. That distinction is the beat's payoff. |
| Say "x-A-I", not "x-dot-A-I"; "internal security code", not "ticker" | B06's narration spells the letters and says "an internal Fidelity security code — not a ticker". |
| If asked why not a bigger model: none was tried | Stated as an open question in `FACTCHECK.md` and in `description.txt`; the reel never claims AI cannot do this, only that this 8B model did not. |
| Don't quote the flattering number | The hardest-cases 100% is NOT on screen and NOT spoken. It is recorded in `FACTCHECK.md` under "what this cut deliberately does not claim", with the reason it would mislead. |
