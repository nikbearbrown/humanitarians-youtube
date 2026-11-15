# SOURCES.md — where-it-went-wrong

Retrieved 2026-10-31. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B00, B03 | student submits a = −1.96 for Atwood; grade mode "says the value matches what you get from reversing a difference, and quotes the card's own warning about sign convention" | `PHASE2.md` grade mode, worked example |
| B01 | diagnoses rather than marks; tests the student's value against specific wrong formulas derived from the card's symbolic solution; quotes `card.pitfalls` | `engine/grade_mode.py` docstring and feedback string; `PHASE2.md` |
| B02 | patterns: `sign_flip`, `reciprocal`, `factor_2_high` / `factor_2_low`, `sqrt2_low` / `sqrt2_high` (escape vs orbital), `sqrt_forgotten` | `grade_mode.py` `_candidate_misconceptions()` lines 106–167; `PHASE2.md` table |
| B03 | MECH-003: m1 = 4 kg, m2 = 6 kg → a = 1.96 m/s²; Atwood pitfall "Inconsistent sign convention across the two masses' equations." | `golden_set_16.csv`; `formula_kb.py` MECH-DYN-ATWOOD. Hand check: (6−4)/10 × 9.8 = 1.96 ✓ |
| B04 | divergence: first quantity that departs from the reference; "a student with I = 0.125 instead of 0.0625 gets pointed at the moment of inertia, not at the final angular speed" | `PHASE2.md` "Divergence detection"; `grade_mode.py` lines 280–290 |
| B04 | disk M = 2 kg, R = 0.25 m: I = ½MR² = 0.0625; MR² = 0.125 | `golden_set_16.csv` MECH-007; hand check ✓ |
| B05 | `TOL = 0.02`; "marking 3.2 wrong when the answer is 3.2026 teaches nothing except that the grader is pedantic" | `grade_mode.py` lines 43–46 |
| B05 | five assessments: correct, wrong_value, wrong_method, incomplete, not_assessable | `grade_mode.py` `Assessment` |
| B06 | no verified reference → `not_assessable` → human review; a CI check | `PHASE2.md`; `eval/ci_check.py` lines 112–118 |
| B06 | "This module therefore does NOT store anything … Persisting graded work is a separate decision gated on Q6 (data processing agreement / IRB), still open" | `grade_mode.py` docstring "IDENTITY AND FERPA" |
| B06 | "Nothing is deployed. No running service, no integration into Medhavy, no student has used this." | `EVALUATION.md` |

## Not claimed

`grade_mode.py`'s docstring pairs "3.27 instead of 1.96" with `g(m1+m2)/(m1-m2)`, which
gives −49 m/s² for these masses, not 3.27; that example is not used. The video uses
`PHASE2.md`'s −1.96 sign-flip example instead.

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported or hand-checked.
