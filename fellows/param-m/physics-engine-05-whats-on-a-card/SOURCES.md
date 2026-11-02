# SOURCES.md — whats-on-a-card

Retrieved 2026-10-31. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B00, B01 | cards = "curated knowledge base of cards (formula, applicability conditions, common pitfalls)"; solve is SymPy over card equations, zero hardcoded arithmetic | `engine/models.py` docstring; `engine/README.md` "What's real" |
| B01 | each starter card checked against the golden set (16/16) | `engine/README.md` "Run it" |
| B02 | MECH-ENE-SPRING: required_knowns m, k, x; solves_for v; ½kx² = ½mv²; output m/s; must_be_positive v | `engine/formula_kb.py` lines 118–133 |
| B03 | applicability "Ideal spring, frictionless surface, all spring PE converts to block KE." | same card |
| B03 | plan logs the card's applicability as an assumption in the solution | `engine/pipeline.py` `plan()`: `assumptions = [card.applicability]` |
| B03 | 2 kg, k = 500 N/m, x = 0.15 m → v = 2.3717 m/s | `golden_set/golden_set_16.csv` MECH-005. Hand check: ½·500·0.15² = 5.625 J; v = √(2·5.625/2) = 2.3717 ✓ |
| B04 | wave card pitfall: "Reading the coefficient of x as the wavelength -- it is the wave NUMBER; wavelength is 2*pi divided by it." | `formula_kb.py` WAVE-FROM-EQUATION |
| B04 | kinematics pitfall: "Forgetting v0=0 when 'starts from rest'" | `formula_kb.py` MECH-KIN-1D |
| B05 | Vibrations and Waves: 179 UGPhysics problems, zero cards → eight cards, each checked against published answers: wavelength 4 cm, wave speed 60 cm/s, Moon escape velocity 2.37 km/s — "All match." | `COVERAGE.md` "The finding that changed the backlog". Hand check: √(2GM/R) for the Moon = 2.375 km/s with M = 7.342e22 kg, R = 1.7374e6 m ✓ |
| B06 | "the KB has footholds in six of eight topics and nothing in two. Depth is the gap, not breadth."; Rigid-Body Dynamics 180 problems, 1 card | `COVERAGE.md` table and "What the ratios actually say" |
| B06 | `T` is tension on the Atwood card and period on two others; retrieve still picks the right card on all 16, "a coincidence"; at scale "some T-shaped … collision will eventually rank a wrong card first" | `engine/README.md` "Known limitation"; `solves_for` with `T` at `formula_kb.py` lines 194, 338 |

## Not claimed

The video does not say pitfalls are used to generate hints; the code at this commit
stores them on the card, and that is all the video says.

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported or hand-checked.
