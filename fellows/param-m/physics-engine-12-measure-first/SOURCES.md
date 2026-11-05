# SOURCES.md — measure-first

Retrieved 2026-10-31. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B00, B01 | tier-3 fine-tuning/RLVR is conditional: "only if evals plateau below target with full KB coverage"; "That trigger has not fired" | `PHASE2.md` "Phase 3 should not be started"; `docs/Physics_Engine_Brief_v2.md` lines 42, 85 |
| B02 | golden set: 16 problems (8 mechanics, 8 E&M); engine 16/16 | `golden_set/golden_set_16.csv`; `engine/README.md` "Run it" |
| B02 | OpenStax *University Physics Vol. 1* Atwood (m1 = 2.00 kg, m2 = 4.00 kg): published a = 3.27 m/s²; engine 3.2667 | `EVALUATION.md` lines 45–46. Hand check: 9.8 × 2/6 = 3.2667 ✓ |
| B03 | UGPhysics: 1,226 problems (836 mechanics + 390 E&M); fully numeric, scorable today: 224 (18.3%); most ask for a derivation | `MEASUREMENT.md` table and "What the other 82% is asking for" |
| B03 | in a topic with at least one card: 970 / 1,226 (79%) — "a generous upper bound"; "Read every number below as a ceiling" | `COVERAGE.md` |
| B04 | 60 UGPhysics problems: "zero wrong answers — it declined nearly everything"; "Nothing plateaued. There is no evidence a better model would help, and considerable evidence that more formula cards would." | `PHASE2.md` |
| B05 | "exactly the kind of decision the decision log exists to prevent: doing the interesting work instead of the indicated work" | `PHASE2.md` |
| B05 | quantum deliberately not built: "the coverage number would go up while the thing the engine is for got worse" | `PHASE2.md` "Scope expansion" |
| B05 | "The golden set becomes the release gate: a fine-tuned model ships only when it beats the benchmark, never on hope." | `docs/Physics_Engine_Brief_v2.md` line 145 |
| B06 | golden set short of "the 150–300 problems originally scoped"; baseline "has not been run" | `PHASE2.md` "Honest status" table, Phase 0 row |
| B06 | the baseline is "the number the whole project is justified by" | `PHASE1.md` gap 2 |
| B06 | "Nothing is deployed." | `EVALUATION.md` |

## Not claimed

`PHASE2.md`'s status row says "Golden set is 31 cards", mixing cards and problems; the
video uses only the unambiguous part (short of the 150–300 problems scoped).

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported or hand-checked.
