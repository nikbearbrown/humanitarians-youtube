# FACTCHECK — vox-shapley-room

Source: `computational-skepticism-for-ai/chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| Shapley value | Average marginal contribution of a feature across all orderings of features entering a coalition | Lines 108–114 |
| Marginal contribution | Change in prediction when feature i is added to coalition S: v(S∪{i}) − v(S) | Lines 100–104 |
| Coalition | Subset of features already in the model at a given step | Lines 100, 114 |
| Efficiency axiom | Shapley values sum exactly to the prediction's deviation from baseline | Lines 130–134 |
| Symmetry axiom | Interchangeable features get equal attribution | Lines 136–140 |
| Dummy axiom | Features that never affect prediction get zero attribution | Lines 142–146 |
| Additivity axiom | Attributions for combined models equal sums of individual attributions | Lines 148–152 |
| Uniqueness result | Shapley values are the *unique* attribution satisfying all four axioms | Line 128 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | Model: income, debt, zip; prediction moves 55%→72% (+17 pts) | Lines 165–167: worked example with exactly these numbers | PASS |
| B04 | Adding income first vs last gives different marginal contributions | Lines 104, 171–178: orderings table shows +0.08 (arriving to ∅) vs +0.06 (arriving to {x2,x3}) | PASS |
| B05 | Three features → 6 orderings; average gives income Shapley = 0.073 | Lines 169–180: table of 6 orderings, average = 0.073 | PASS |
| B07 | Room metaphor: feature enters, finds coalition already there | Line 114: "think of the features entering a room in a random order. Every ordering is equally likely." | PASS |
| B08 | Income 0.073, debt 0.062, zip 0.035; sum = 0.17 | Line 182: exactly stated | PASS |
| B09 | Quote verbatim | Line 114: exact match | PASS |
| B10 | Four axioms: Efficiency, Symmetry, Dummy, Additivity; unique | Lines 128–152 | PASS |
| B11 | "nothing about the world" quote | Line 184: "it tells you nothing about the world" | PASS |

## Exclusions honored

- No closed-form weight-formula derivation (weights mentioned only qualitatively)
- No KernelSHAP/TreeSHAP approximations
- No correlated-feature conditional-sampling debate
- Rung 1 vs Rung 2 limited to one closing caption in B11

| B12 | Recommendation model: reading time 0.14, scroll depth 0.06, clicks 0.03, sum = 0.23; naive single-ordering gives different values | ILLUSTRATIVE — numbers are made-up to demonstrate mechanism; labeled illustrative | ILLUSTRATIVE |

## VERDICT: PASS
