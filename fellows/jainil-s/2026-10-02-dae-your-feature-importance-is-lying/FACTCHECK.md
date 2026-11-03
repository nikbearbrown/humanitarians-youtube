# FACTCHECK — Your Feature Importance Is Lying

Status: **GATE F CLOSED — 2026-10-02.** Two independent evidence sources:
scikit-learn's documented warning (verbatim) and `importance_evidence.py` in
this folder, which reproduces every number with a fixed seed.

| # | Beat | Claim (as spoken / shown) | Verdict | Source |
|---|---|---|---|---|
| 1 | B00 | Dropping low-importance columns can delete the best feature in the dataset | ✅ PASS | Demonstrated by P3 below — at three copies the real driver ranks last |
| 2 | B01 | An importance score measures what the model would *miss*, not what matters | ✅ PASS | Definitional to permutation importance, and the mechanism S1 describes |
| 3 | B02 | In the constructed world, temperature drives the outcome 2.5× harder than day_of_week | ✅ PASS | The generating equation, printed by the script: `y = 3.0*temp + 1.2*day + noise` |
| 4 | B02 | With one copy the ranking is correct — temp 1.68 vs day 0.27 | ✅ PASS | Script Experiment 2, k=1: temp **1.6774**, day **0.2744**. Chart rounds to 1.68 / 0.27. |
| 5 | B03 | A second copy is the same measurement in other units, carrying no new information | ✅ PASS | `temp_f = temp*1.8 + 32 + tiny noise`; correlation ≈ 0.99998 |
| 6 | B03 | With two copies each scores less — 0.58 each vs day 0.27 | ✅ PASS | Script Experiment 2, k=2: each temp **0.5776**, day **0.2705** |
| 7 | B03 | The model "leans on each about half as hard" | ✅ PASS | Experiment 1: fitted weight per copy **2.977 → 1.453** |
| 8 | B04 | At **three** copies each temp scores ~0.12 and day 0.27, so the ranking inverts | ✅ PASS | Script Experiment 2, k=3: each temp **0.1219**, day **0.2722**, top = day_of_week |
| 9 | B04 | Temperature is the real driver in every run | ✅ PASS | Fixed by the generating equation; unchanged across all k |
| 10 | B05 | The on-screen scikit-learn quotations | ✅ PASS | S1 and S2, **verbatim**, attributed on the card |
| 11 | B07 | Clustering correlated features and ranking clusters is the documented fix | ✅ PASS | S3, verbatim: "cluster features that are correlated and only keep one feature from each cluster" |
| 12 | B07 | "drop it, refit, watch the score" as the check that cannot be split | ✅ PASS | **Engineering advice**, framed as such. Follows from the mechanism; not presented as a measured result. |

## Correction made during production — on the record

This reel was first pitched on the claim that **both copies report ~zero
importance**. The experiment does not support that for a linear model:

- two copies each score **0.58** against a true **1.68** — reduced, not zero
- and with two copies the correct feature **still ranks first**

**Two copies are not enough to invert a ranking. Three are.** The reel says
three, and every number on screen is the three-copy result. The original,
stronger framing was discarded before authoring rather than softened.

## Claims deliberately CUT

- Anything specific to random forests or tree ensembles. The mechanism is
  general and S1 states it generally, but this folder's evidence is a linear
  model, so no tree-specific magnitude is asserted.
- Any real-world account of a team deleting a feature this way. Plausible,
  unsourceable.
- Any claim about how common multicollinearity is in practice.
