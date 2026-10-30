# SOURCES.md — who-does-the-math

Retrieved 2026-10-30. Source repo pinned to commit
`2dc4aa408e02a78fd595e35cee8012017a9972e6` of
https://github.com/jashshah127/humanitariansai (folder `physics-engine/`).
Base URL below: `https://github.com/jashshah127/humanitariansai/blob/2dc4aa4/physics-engine/`

**Method note.** Every result figure is the project's own reported check, read
from its docs at the pinned commit. The project's code was not re-executed for
this video. The two pulley results were re-derived by hand (below).

| Beat | On screen / spoken | Source |
|---|---|---|
| B01 | LLM never does arithmetic or algebra; SymPy + pint do computation | `docs/Physics_Engine_Brief_v2.md` §"What I'm proposing to build now" |
| B02 | "not a game-style physics engine"; a tool Medhavy calls | same, same section |
| B03 | Parse → Retrieve → Plan (closure check, loop back on gap) → Solve (SymPy) → Verify (units, independent path) | brief §"Pipeline workflow"; `engine/README.md` §"What's real" |
| B04 | three routes `deterministic_script` / `ambiguous_multiple_deterministic_paths` / `no_deterministic_path`, decided before solving | `engine/README.md` §"V2 — script-vs-LLM routing" |
| B05 | 16/16 golden-set problems, mechanics + E&M | `EVALUATION.md` claim 3; `engine/README.md` §"Run it" |
| B05 | one problem ×10, byte-identical output | `EVALUATION.md` claim 2 |
| B05 | OpenStax *University Physics Vol. 1* Atwood (m₁=2.00 kg, m₂=4.00 kg): published a = 3.27 m/s²; engine 3.2667 | `EVALUATION.md` claim 3. Hand check: a = (4−2)/(4+2)·9.8 = 3.2667 m/s² ✓; T = 2·(9.8+3.2667) = 26.13 N ✓ |
| B06 | parse quality unmeasured; demo uses canned parses | `EVALUATION.md` §"What is NOT proven" |
| B06 | no baseline number yet | same |
| B06 | 1,226 UGPhysics problems; Rigid-Body Dynamics 180 problems, 1 card | `COVERAGE.md` table |
| B06 | not deployed, no student has used it | `EVALUATION.md` §"What is NOT proven" |

## Corrected during verification

`EVALUATION.md` still says Vibrations and Waves has "179 problems, zero cards".
`COVERAGE.md` at the same commit shows it now has **8 cards**. The video uses
the current figure (rigid-body, 180 : 1) and does not repeat the stale one.

## Expiring figures

Coverage ratios will move as cards are added. B05/B06 carry "commit 2dc4aa4 ·
Oct 2026"; B07 says the numbers change and the rule doesn't.
