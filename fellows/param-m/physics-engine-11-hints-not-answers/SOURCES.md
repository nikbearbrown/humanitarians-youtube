# SOURCES.md — hints-not-answers

Retrieved 2026-10-31. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B01 | badges: "Verified - solved symbolically" / "Needs review - more than one principle applies" / "Unverified - AI reasoning, not symbolically checked"; "That visible status IS the product." | `engine/physics_mode.py` docstring and `_ROUTE_MAP` |
| B02 | "on the UNVERIFIED path the student is no worse off than with the toggle off, because that path IS the toggle off, labelled. There is no input for which turning this on degrades the answer" | `physics_mode.py` docstring |
| B02 | "Keeping the fallback out of the engine is what stops an unverified answer from ever leaving here wearing a verified label." | `PhysicsEngineMode` docstring |
| B03–B04 | the ladder, in order: givens/find; subtopic + principle (card name); applicability; symbolic relationship; pitfall; rearranged general formula; worked result | `physics_mode.py` `_hint_ladder()` |
| B03–B04 | Atwood card: subtopic Dynamics; applicability "Two masses, frictionless massless pulley, massless inextensible string."; equations T − m1·g = m1·a, m2·g − T = m2·a; pitfall "Inconsistent sign convention across the two masses' equations." | `engine/formula_kb.py` MECH-DYN-ATWOOD |
| B04 | a = g(m2 − m1)/(m1 + m2); MECH-003: a = 1.96 m/s², T = 47.04 N | `PHASE2.md` symbolic block; `golden_set_16.csv`. Hand check: T = 2·9.8·4·6/10 = 47.04 ✓ |
| B05 | ladder "derived entirely from the plan object -- no second LLM call"; "each rung reveals strictly less than the next, and the answer is last" | `_hint_ladder()` docstring |
| B05 | tutor render withholds answer, formula LaTeX, general answer, card id ("the card id names the principle, which is hint 2") and knowns | `physics_mode.py` lines 229–236 |
| B06 | hint "used to read `T - 39.2 = 4*a` — arithmetic already leaked. It now reads `T - g*m1 = a*m1`" | `MEASUREMENT.md` "Tutor hints got materially better" |
| B06 | caching: 6.30 ms/problem vs 11.04 ms before | `MEASUREMENT.md` "And it's 43% faster" |
| B06 | "no student has used this" | `EVALUATION.md` "Nothing is deployed" |

## Not claimed

The video does not claim the hints improve learning; that is untested (no students).

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported or hand-checked.
