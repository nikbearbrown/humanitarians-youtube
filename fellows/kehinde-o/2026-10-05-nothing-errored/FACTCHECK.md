# FACTCHECK — Nothing Errored

Source of record: `github.com/Kenny0bi/loom`. Every figure below was **recomputed
in this session** from `assets/lifecycle.json`, the committed record of the
simulated year, not from the repo README (docs/EXECUTABLE-EVIDENCE.md).

| # | Claim on screen or spoken | Beat | Verdict | Where it comes from |
|---|---|---|---|---|
| 1 | Accuracy fell from about 0.64 to about 0.56 | B00, B02 | TRUE | `lifecycle.json`: week 6 = 0.6384, week 7 = 0.5551 |
| 2 | No request errored during the drop | B00, B02 | TRUE | Drift is a distribution shift, not a fault; decision field moves OK to RETRAIN with no error state |
| 3 | Quiet weeks sit near 0.02 to 0.03 PSI | B04 | TRUE | weeks 4 to 6: 0.0302, 0.0213, 0.0246 |
| 4 | Week 7 PSI reaches 1.72 | B04 | TRUE | `worst_psi` = 1.7151 |
| 5 | That is roughly seventy times higher | B04 | TRUE | 1.7151 / 0.0246 = 69.7 |
| 6 | Drift lands hardest on hydration and activity | B04 | TRUE | Per-feature PSI, the features the simulated routine change touches |
| 7 | Promote above z = +2, roll back below z = -2, a tie keeps the incumbent | B05 | TRUE | `loom/canary.py` decision rule |
| 8 | Week 8 candidate promoted at z = 5.4 | B05 | TRUE | PROMOTE verdict, z = 5.396 |
| 9 | That candidate scored 0.69 against the incumbent's 0.53 | B05 | TRUE | cand_acc 0.6915, inc_acc 0.5329 |
| 10 | A poisoned model's canary returned z = -12.2 | B06 | TRUE | ROLLBACK verdict, z = -12.244 |
| 11 | Its accuracy was 0.26 against the incumbent's 0.74 | B06 | TRUE | cand_acc 0.2628, inc_acc 0.7361 |
| 12 | Production rolled back automatically and the reason was written to the record | B06 | TRUE | `final_production`: v3, reason "rollback restore: canary z=-12.244" |
| 13 | The first weekly window had 112 samples and fired a false RETRAIN | B07 | TRUE | Repo README, "two bugs the demo caught in its own platform" |

## Note on a disagreement between the README and the data
The repo README narrates week 7 as "Accuracy 0.70 to 0.56". The committed
`lifecycle.json` records 0.6384 to 0.5551. The reel uses the run data and treats
the README as stale. That discrepancy should be fixed in the source repository.

## Math typesetting (docs/MATH-TYPESETTING.md)
B03 renders two structured SVG rows via `runtime/scripts/typeset_math.py`:
- PSI as a sum over buckets b, with a real fraction inside the logarithm
- The two-proportion z-test, with a real fraction bar and a radical

Symbols deliberately match the notation in my own Manim scene (B04), which writes
the same formula with live and reference terms, so the viewer does not see two
symbol sets for one quantity forty seconds apart.

Algebra check: in PSI, b is bound by the summation and each term is (live minus
reference) times the log of their ratio, the standard symmetrised form. The
z-test denominator uses the pooled proportion, so the hat is distinct from the
two group proportions.

## Deliberately not claimed
- The demo is a simulation on synthetic caregiver logs. It is not a clinical
  system, not deployed, and the reel makes no claim about real patients.
- No claim that this platform competes with managed MLOps tooling. The measured
  claim is what the run did: detected a drift, earned two promotions on live
  traffic, reverted a poisoned model automatically.
- The false RETRAIN at 112 samples is reported as a bug in my own monitor.
