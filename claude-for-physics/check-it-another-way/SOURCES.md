# SOURCES.md — check-it-another-way

Retrieved 2026-10-31. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B01, B02 | residual check on every card: equations re-evaluated with the solved values, `abs(val) < 1e-4` | `engine/pipeline.py` `verify()`; `engine/README.md` "a generic residual check on every card" |
| B01, B03 | positivity check on `must_be_positive` symbols ("where physically required") | `pipeline.py` `verify()`; `models.py` `must_be_positive`; README |
| B01, B06 | 11 of 31 cards carry an independent `verify_fn` (MECH-KIN-1D, MECH-KIN-PROJ, MECH-GRAV-ORBIT, EM-ELEC-GAUSS-SPHERE, EM-CIRC-SERIES-PARALLEL, EM-CIRC-RC-CHARGE-1TAU, EM-MAG-LORENTZ-CIRCULAR, WAVE-FROM-EQUATION, SHM-SPRING-PERIOD, MECH-GRAV-ESCAPE, THERMO-CARNOT-EFFICIENCY); 20 do not | `engine/formula_kb.py` `verify_fn=` lines 50, 78, 199, 264, 290, 316, 343, 436, 461, 591, 686 |
| B04 | KCL: `I_branch1 + I_branch2` vs `I_total`; golden EM-004: 1.2 + 1.0 = 2.2 A | `_em004_verify`; `golden_set_16.csv` EM-004 |
| B04 | capacitor at t = τ: `Vc/V0` vs `1 − 1/e`; golden EM-005: 9 V → 5.6891 V | `_em005_verify`; EM-005. Hand check: 9 × (1 − e⁻¹) = 9 × 0.63212 = 5.6891 ✓ |
| B04 | orbit period re-derived via `2π√(r³/GM)` | `_mech008_verify` |
| B05 | escape/orbital ratio must equal √2 | `_wave009_verify` |
| B05 | Carnot efficiency must lie strictly between 0 and 1 | `_th004_verify`; `PHASE2.md` "the second law used as a unit test" |
| B06 | status `verified` if all checks pass, else `flagged`; final status "solved — flagged for review" | `pipeline.py` `verify()` and `solve_physics_problem()` |
| B06 | symbolic mode: residual simplifies to 0 (stronger); positivity "indeterminate … not checked"; numeric cross-check "skipped in symbolic mode" | `pipeline.py` `verify()` docstring and branches |

## Not claimed

The video does not say the residual check catches every wrong answer; a wrong equation
solved correctly passes it, which is why the independent path exists (B00, B04).

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported or hand-checked.
