# SOURCES.md — five-steps-one-answer

Retrieved 2026-10-30. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B00, B02 | the worked problem: car from rest, 2.5 m/s² for 12 s; expected v = 30.0, s = 180.0 | `golden_set/golden_set_16.csv`, MECH-001 |
| B01 | stages Parse → Retrieve → Plan → Closure check → Solve → Verify → Solution object | `engine/models.py` module docstring |
| B01, B02 | parse is "the only stage where a language model does anything" | `engine/parse.py` docstring |
| B01 | retrieve/plan are rule-based, not LLM-assisted | `engine/README.md`, "Retrieve/Plan judgment is currently rule-based" |
| B02 | "starts from rest" means v0 = 0; every known carries its source phrase; the model must not solve or compute | `engine/parse.py` PARSE_PROMPT rules; TRACEABILITY note |
| B03 | 31 cards: 8 mechanics + 8 E&M + 9 waves + 6 thermo | `engine/formula_kb.py` lines 202, 380, 594–595, 727, 729 |
| B03 | a card holds equations, applicability, pitfalls | `engine/models.py` `FormulaCard` fields |
| B03 | retrieve pulls every card whose `solves_for` overlaps the request and deliberately does not check knowns | `engine/pipeline.py` `retrieve()` docstring |
| B03 | six cards solve for `v` or `s`: MECH-KIN-1D, MECH-DYN-INCLINE, MECH-ENE-SPRING, MECH-GRAV-ORBIT, WAVE-BASIC-RELATION, WAVE-FROM-EQUATION | `engine/formula_kb.py` `solves_for=` lines 46, 111, 129, 194, 404, 430 |
| B04 | closure check: missing knowns → gap with reason; equations must resolve | `engine/pipeline.py` `plan()` |
| B04 | spring card needs `k`; others need `theta_deg/mu/d`, `h`, `f/lambda_`, `k_wave/omega` | `required_knowns=` at the same lines |
| B04 | no closing card → `no_deterministic_path`, logged as a coverage gap | `engine/README.md` V2 routing table |
| B05 | equations v = v0 + a·t, s = v0·t + a·t²/2; solved by `sympy.solve` | `formula_kb.py` `_mech001_eqs`; `pipeline.py` solve stage method string |
| B05 | arithmetic hand-checked: 0 + 2.5·12 = 30; ½·2.5·144 = 180 | by hand |
| B06 | residual check on every card; independent path for this card: s = (v² − v0²)/(2a) | `pipeline.py` `verify()`; `formula_kb.py` `_mech001_verify`. Hand check: 900/5 = 180 ✓ |
| B07 | solution object holds parse, retrieve, plan, solve, verify, final_answer, status, route | `engine/models.py` `solution_object()` |

## Not claimed

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported or hand-checked.
