# SOURCES.md — same-problem-same-answer

Retrieved 2026-10-31. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B00 | Atwood problem run 10 times; "All 10 outputs byte-identical" | `eval/demo.py` V2 check 1 (line 136); `EVALUATION.md` claim 2; `ci_check.py` |
| B01 | "SymPy itself has no randomness — given the same equations and the same numbers, it returns the same answer every time" | `engine/README.md` V2, "Why this matters" |
| B01, B02 | variation "can only come from which formula gets selected being unstable … or from an LLM doing part of the reasoning and sampling differently" | same section |
| B02 | running it twice "would never catch anything on the script side, since SymPy can't disagree with itself" | same section |
| B03 | three routes: `deterministic_script` (exactly one card closes; final); `no_deterministic_path` (zero; LLM or human, logged as coverage gap); `ambiguous_multiple_deterministic_paths` (more than one; all candidates returned; LLM arbitrates "which formula applies, not to redo the arithmetic") | `engine/README.md` V2 routing table; `pipeline.py` `solve_physics_problem()` |
| B04 | constructed case: knowns `v0=0, a=2.5, t=12, m=2, k=500, x=0.15` close both MECH-KIN-1D and MECH-ENE-SPRING on `v`; v = 30.0 vs v ≈ 2.37; engine reports both and asks for arbitration | `eval/demo.py` V2 check 2 (lines 141–151); `engine/README.md` "Proof, not assertion" |
| B05 | grading fairness, debuggability, cost — the three reasons | `engine/README.md` "This is also why determinism is worth defending" |
| B06 | newer Claude models don't accept temperature or a seed; parse "CAN vary between runs" | `engine/parse.py` `ClaudeLLM` docstring |
| B06 | "Is the routing decision the right one, or is it just a way of avoiding hard problems?" | `EVALUATION.md` "The three questions worth asking", Q1 |

## Not claimed

The video does not say the whole engine is deterministic end to end; it says the solver
is, and that parsing can vary (B06).

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported.
