# SOURCES.md — force-is-not-time

Retrieved 2026-10-31. All claims are from the physics engine repo at commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B00, B04 | the unit audit "independently rediscovered the `T` symbol collision — tension (newtons) on one card, period (seconds) on two others — with dimensional evidence. Force versus time can't be a false alarm." | `PHASE1.md`, "The unit audit found a real defect" |
| B01, B03 | audit checks: every unit string parses to a genuine dimension (typos, nonsense units); card output unit vs glossary unit for the same variable ("catching a card that says `v` is in metres") | `engine/units.py` docstring and `audit_units()` |
| B01, B06 | "DOES NOT propagate units through the algebra itself"; "Unit PROPAGATION through the solve is still the open item" | `engine/units.py` docstring; `PHASE1.md` gap 3 |
| B02 | wave card pitfall: "Mixing units -- wavelength in cm with speed in m/s is the usual slip." | `engine/formula_kb.py` WAVE-BASIC-RELATION |
| B02 | cm → m is a factor of 100 | definition |
| B03 | unit audit is in the automated check suite: `check("unit/dimension consistency", units_consistent)` | `eval/ci_check.py` lines 53–59, 204 |
| B04 | `T` solves for tension on MECH-DYN-ATWOOD and for period on MECH-GRAV-ORBIT and EM-MAG-LORENTZ-CIRCULAR | `engine/formula_kb.py` `solves_for` lines 194, 338; `engine/README.md` "Known limitation" |
| B04 | "previously known only because someone noticed it by hand; it's now machine-detectable" | `PHASE1.md` |
| B05 | glossary `T`: "string TENSION (N) … OR orbital / cyclotron PERIOD (s) … -- read which from the problem", unit "N or s"; `R`: radius (m) OR resistance (ohm), unit "m or ohm" | `engine/variable_glossary.py` lines 87–92, 116–120 |
| B05 | "turns 'namespace the symbols eventually' from a judgement call into a check with an objective trigger" | `PHASE1.md` |
| B06 | pint not used "contrary to the brief's Phase 1 line"; couldn't be installed (no outbound network); `sympy.physics.units` used because it "was actually run" | `PHASE1.md` gap 3; `engine/units.py` "HONEST SCOPE" |

## Not claimed

The video does not repeat `PHASE2.md`'s claim that a Celsius temperature always pushes the
Carnot efficiency outside (0, 1); with typical values (227 °C / 27 °C) it does not, so the
claim was left out.

The repo's code was not executed for this video (blocked by the auto-mode permission
check); every result is repo-reported.
