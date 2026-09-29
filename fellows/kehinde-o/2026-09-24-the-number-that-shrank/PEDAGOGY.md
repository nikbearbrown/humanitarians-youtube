# Pedagogy Review

## Topic
The Number That Shrank: why a disproportionality signal is only as good as the evidence
behind it (built on Kehinde's adverse-event-pipeline repo)

## Learning Objective
The viewer leaves able to ask two questions of any dramatic ratio they are shown: how many
observations does it rest on, and what was the expected count? They understand why a
method deliberately shrinks a large ratio built on thin evidence.

## Audience
General audience. No statistics background assumed. "Expected count" is defined on screen
and in narration before it is used.

## The ONE Idea
A ratio is not evidence. Observed over expected tells you the size of an effect; the
amount of data underneath tells you how much to believe it. Empirical Bayes shrinkage
formalises that, pulling thin evidence back toward the null while leaving well-supported
signals nearly untouched.

## Math Gate (docs/MATH-TYPESETTING.md)
B03 uses TypesetMath with structured SVG rows, not formula strings on a text card:
- Expected count under independence, as a real fraction with a proper bar
- The crude ratio as observed over expected
Algebra checked: expected = (row total x column total) / grand total, the standard
independence expectation for a 2x2 contingency table. Verified numerically against the
repo's own output for warfarin and gastrointestinal haemorrhage (62 observed, 2.925
expected).

## Evidence Gate (docs/EXECUTABLE-EVIDENCE.md)
No figure is copied from the repo README. Every number was recomputed in this session from
results/summary.json, results/positive_controls.csv and results/signals_top1000.csv. The
shrinkage percentages in B04 were calculated here as EBGM divided by crude ratio.

## Restraint Gate
- No clinical advice and no claim that any drug causes any effect. FAERS reports are
  voluntary and disproportionality is not causality. This is stated in the B03 conditions
  line.
- Esculin is used as an example of thin evidence, explicitly not as a safety claim.

## VERDICT: PASS
