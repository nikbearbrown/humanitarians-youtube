# SOURCES.md — the-engine-that-says-no

Retrieved 2026-10-31. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B00, B04 | "Across 60 UGPhysics problems the engine produced zero wrong answers — it declined nearly everything, because coverage is thin and most of the benchmark asks for derivations." | `PHASE2.md`, "Phase 3 should not be started" |
| B01 | closure check: "can every requested unknown actually be pinned down?" — run before solving | `engine/pipeline.py` `plan()` docstring |
| B01 | zero closing cards → `no_deterministic_path`: LLM or human handles it, logged as a coverage gap, not silently patched | `engine/README.md` V2 routing table; `pipeline.py` `solve_physics_problem()` docstring |
| B02 | three gap reasons: `missing knowns: [...]`; `solver raised <Error>`; `system did not resolve to a determinate solution` | `engine/pipeline.py` `plan()` return values |
| B02 | spring card needs `k` | `engine/formula_kb.py` MECH-ENE-SPRING `required_knowns` |
| B03 | damped oscillator, deliberately outside the KB, "correctly routes to unverified and lands in the coverage queue rather than getting a confident wrong answer" | `PHASE1.md` "Verified in this phase"; `eval/demo_phase1.py` line 78 |
| B04 | most of UGPhysics asks for derivations, not numbers | `MEASUREMENT.md` "What the other 82% is asking for" |
| B05 | symbolic problems declined because "the pipeline insisted on converting results to float at the very end. An interface limitation was being reported as a coverage gap, which is worse than an honest gap: it hid capability that already existed." | `PHASE2.md`, "Why this matters more than adding cards" |
| B06 | no verified reference → `not_assessable`, routed to human review; "That refusal is a CI check, not a convention." | `PHASE2.md` grade mode; `engine/grade_mode.py` line 53; `eval/ci_check.py` lines 112–118 |

## Not claimed

The video does not give an accuracy figure for the 60-problem run beyond "zero wrong";
the repo does not report how many of the 60 were answered, only "nearly everything" declined.

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported.
