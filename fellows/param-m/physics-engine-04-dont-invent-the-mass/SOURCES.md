# SOURCES.md — dont-invent-the-mass

Retrieved 2026-10-31. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B00, B04 | the parser reported `m=1.0, q=1.0` for a problem that contained no numbers | `PHASE2.md`, "Symbolic input mode" |
| B01 | parse is reading comprehension only; must NOT solve, rearrange, or compute | `engine/parse.py` docstring and PARSE_PROMPT first paragraph |
| B01 | a wrong parse "solves cleanly and returns a confidently WRONG verified answer" | `engine/parse.py` StubLLM comment (found that way in testing) |
| B02 | "Use EXACTLY these variable names. Do not invent new ones" | PARSE_PROMPT |
| B02 | aliases `initial_velocity` → `v0`; `mass_1` → `m1` | `engine/variable_glossary.py` lines 48–49, 74 |
| B02 | before canonical naming, answers came out as `9.8*(-mass_1 + mass_2)/(mass_1 + mass_2)` — "useless to a student and unmatchable against a benchmark" | `engine/parse.py` comment above `symbolic_names` |
| B03 | 25 km → 25000; 100 uF → 0.0001; `theta_deg` stays in degrees; no constants (g, G, k_e, ε₀, μ₀), supplied automatically; "starts from rest" → v0 = 0 | PARSE_PROMPT rules |
| B04 | most of UGPhysics is stated in symbols (734 of 1,226 problems, 59.9%, have symbolic ground truth) | `PHASE2.md`; `MEASUREMENT.md` table |
| B05 | report symbolic quantities as `{"symbolic": true}`; do not invent a number like 1.0 | PARSE_PROMPT |
| B05 | `a = g*(m2 - m1)/(m1 + m2)`; verify `T - g*m1 = a*m1` simplifies to 0, "holds for all values" — a stronger check | `PHASE2.md` code block; `engine/pipeline.py` `verify()` docstring |
| B06 | every known includes the exact source phrase (traceability) | `engine/parse.py` TRACEABILITY note |
| B06 | `ParseError` is deliberately distinct from "parsed fine but nothing in the KB covers it" | `engine/parse.py` `ParseError` docstring |
| B06 | "Parse quality still unmeasured against a real model beyond spot checks" | `PHASE2.md`, "Honest status" table, Phase 1 row |
| B06 | newer Claude models don't accept temperature or a seed, so this stage can vary between runs | `engine/parse.py` `ClaudeLLM` docstring |

## Checked and noted

`PHASE2.md`'s status table still lists the invented-values bug as known for Phase 1,
while its "Symbolic input mode" section, in the same file, says it is fixed. The video
follows the section that describes the fix and shows its output.

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported. The pulley formula was checked by hand:
(m2 − m1)g/(m1 + m2) with m1 = 4, m2 = 6 gives 1.96 m/s², matching MECH-003.
