# SOURCES — dae-your-feature-importance-is-lying

Two kinds of evidence, both strong: scikit-learn documents the failure in its
own docs, and `importance_evidence.py` in this folder reproduces it from
scratch with a fixed seed.

## Documented by the library itself

| # | Source | Verbatim wording relied on | Supports |
|---|---|---|---|
| S1 | [Permutation feature importance — scikit-learn](https://scikit-learn.org/stable/modules/permutation_importance.html) | "When two features are correlated and one of the features is permuted, the model still has access to the latter through its correlated feature. **This results in a lower reported importance value for both features, though they might actually be important.**" | The mechanism, stated by the library that ships the tool |
| S2 | Same page | "A naive interpretation would suggest that **all features are unimportant**" | That the failure can affect the whole ranking, not one row |
| S3 | Same page | "One way to handle the issue is to **cluster features that are correlated and only keep one feature from each cluster**." | The fix given in B06 |

## Primary evidence — generated locally

`importance_evidence.py`, pure numpy + ridge, `default_rng(0)`. Verbatim output:

```
TRUE MODEL:  y = 3.0*temp + 1.2*day + noise
             temperature matters 2.5x more than day_of_week

EXPERIMENT 1 — one twin halves the weight and quarters the importance
  1 copy(s):  each temp importance 1.6701   weight per copy 2.977
  2 copy(s):  each temp importance 0.3986   weight per copy 1.453

EXPERIMENT 2 — enough twins and the RANKING inverts
  1 copies: each temp 1.6774   day_of_week 0.2744   top = temp_copy1
  2 copies: each temp 0.5776   day_of_week 0.2705   top = temp_copy1
  3 copies: each temp 0.1219   day_of_week 0.2722   top = day_of_week   <-- WRONG
  4 copies: each temp 0.1645   day_of_week 0.2732   top = day_of_week   <-- WRONG
  5 copies: each temp 0.0669   day_of_week 0.2732   top = day_of_week   <-- WRONG
```

| # | Claim | Supported by |
|---|---|---|
| P1 | One twin roughly halves the fitted weight (2.977 → 1.453) | Experiment 1 |
| P2 | Importance falls faster than the weight — quartered, not halved | Experiment 1 (1.670 → 0.399); importance is quadratic in the weight for R² |
| P3 | At **three** copies the ranking inverts: day_of_week 0.272 outranks each temp copy at 0.122 | Experiment 2 |
| P4 | Temperature is the real driver in every run | The generating equation, printed by the script |

Numbers differ slightly between the two experiments because each twin draws its
own measurement noise; both are deterministic under the fixed seed.

## Corrected during production — stated for the record

The reel was first pitched on the claim that **both** copies report ~zero
importance. The experiment does not show that for a linear model: two copies
each measure ~0.40 against a true 1.67, and the correct feature still ranks
first. **Two copies are not enough to invert a ranking — three are.** The reel
says three, because that is what was measured.

## Deliberately NOT used

- Any claim about tree ensembles or random forests specifically. The mechanism
  is general and S1 states it generally, but this folder's evidence is a linear
  model, so no tree-specific behaviour is asserted.
- Any real-world case of a team deleting a feature this way. Plausible, not
  sourceable.
