# FACTCHECK — *Nothing Left To Remove.*

Ep. 11 · `generative-spacecraft-design` · checked from primary sources on
**2026-10-02**, during this build.

**Two kinds of number appear and they are never mixed.** *Published* figures
come from the cited sources and carry a source line. *Computed here* figures
come out of `assets/gen_struct.py`, which runs a real finite-element model
and a SIMP topology optimiser and asserts three central claims. B03 and B09
are published and say so on screen; B04–B08 and B10 are computed here and
say so.

## Claims on screen or in the narration

| # | Claim | Where | Verdict | Source |
|---|---|---|---|---|
| 1 | Generative design / topology optimisation is given a volume, loads and a mass budget, and software decides where material goes | B00, B02, B04 | ✅ | ESA's own caption describes topology optimisation as "software decides where material needs to go in order to best meet the part's function, constrained by its stress load and interface points with the rest of the satellite." |
| 2 | The Sentinel-1 upper S-band antenna support was designed this way | B03 | ✅ | ESA image caption, 2014-11, verbatim in SOURCES.md. RUAG Space Switzerland with Altair and EOS. |
| 3 | **1.4 kg → 0.94 kg**, a third lighter | B03 bar + narration | ✅ | ESA caption, verbatim: "the redesigned part has a mass of 0.94 kg compared to the original part's mass of 1.4 kg". 0.94/1.4 = 0.671, so 32.9% — stated as "a third lighter". |
| 4 | Made in metal by selective laser melting | B03 tag | ✅ | Same caption. |
| 5 | AI-designed spacecraft hardware has actually flown | B09 | ✅ | NASA ST5: the evolved X-band antenna design was approved for flight and three copies flew between 22 March and 30 June 2006 — described as the first evolved hardware, and first evolved antennas, in space. |
| 6 | The ST5 antennas were competitive with a human design | B09 (on screen only) | ✅ | Hornby/Lohn/Linden: the fabricated best-of-both-algorithms antennas were "comparable in performance to a hand-designed antenna produced by a contractor for the mission". |
| 7 | Minimum-compliance-at-fixed-volume optima have **no alternative load paths** | B07, B09, B11 | ✅ | Fail-safe topology optimisation literature, verbatim: such a formulation "usually gives a structure that resembles a statically determinate structure with no redundant parts, meaning if one of the structural members was to break, there would not exist any alternative load-paths". |
| 8 | Fail-safe design with redundant load paths is an aerospace **requirement** | B09 | ✅ | Same literature: "In aerospace applications, fail-safe design with redundancy in terms of load-paths is required," and the philosophy originated in that industry. |
| 9 | Making a design fail-safe costs volume | B10, B11 | ✅ | Same literature: "Optimal topologies obtained by fail-safe methods are more complex and have greater volume than those from traditional topology optimization." Independently measured here. |
| 10 | The damage model used is the published one | B08 cite | ✅ | Jansen, Lombaert, Schevenels, Sigmund (2014), *Struct Multidisc Optim* 49(4) 657–666: damage as "a square void zone of required size, placed one instance at a time" across the domain, with the objective taken under "the worst damage". |

## Computed in this reel (`assets/gen_struct.py` + `assets/topo.py`)

A 120 × 60 plane-stress cantilever (7,200 elements, 14,762 dofs), E = 1,
ν = 0.3, SIMP penalty 3, sensitivity filter radius 2.4, 90 optimality-criteria
iterations. The left edge is the bolted root; a 6 × 6 solid, non-design
mounting lug sits at the free end, mid-height, and is charged to the mass
budget. One unit load, straight down, on the lug. Damage is an 8 × 8 void
(0.89% of the domain) swept over 398 locations at a 4-element stride.

| Quantity | Value |
|---|---|
| Solid block, full mass | compliance 40.01 |
| Plate machined to 40% thickness | 100.03 undamaged · worst void 121.41 (**1.21×**) |
| Optimised bracket, 40% volume | 81.31 undamaged · worst void 2536.90 (**31.20×**) |
| Undamaged, equal mass | bracket **1.23× stiffer** than the plate |
| Worst-case damaged, equal mass | bracket **20.9× softer** than the plate |
| 90th-percentile damage | bracket **3.42×** · plate **1.08×** |
| Optimised bracket, 50% volume | 65.68 · worst 775.75 (11.81×) |
| Optimised bracket, 60% volume | 55.65 · worst 90.79 (**1.63×**), still **1.20× stiffer** than the plate at that mass |
| Mass saved vs solid, to get there | **60% → 40%** — a third of the saving given back |

**There is no random number in this pipeline.** SIMP from a uniform start is
deterministic given the problem, so there is no seed; the parameters above are
the whole specification.

### Validation of the finite-element core

A wrong stiffness matrix is still symmetric and still solves, so the core is
checked against things that actually constrain it (`scratchpad/fecheck.py`):

- exact symmetry, `max|K − Kᵀ| = 0`
- **exactly 3 zero eigenvalues** — the rigid-body modes of a plane element
- all three rigid-body motions (two translations and a rotation) annihilated
  to machine precision
- the uniaxial patch test exact to six digits against ½·E/(1−ν²)·ε²
- the solid cantilever **1.4–1.9% softer** than Euler–Bernoulli at two mesh
  densities — the correct direction and magnitude for a short deep beam that
  also carries shear

And one check that doubles as a result: the domain, the support and the load
are all symmetric about mid-height, so the optimum must be. The generator
asserts it and measures **max|x − mirror(x)| = 2.1 × 10⁻¹¹**. An asymmetric
answer would have meant the element dof ordering was wrong — a defect that is
otherwise invisible.

### Three errors this experiment caught, all mine

1. **I quoted a number that was really my density floor.** The first version
   put the three load cases at three different heights on the free edge. Two
   of those points sit in void, so the solve returned compliance ≈ 8.5 × 10⁹
   and the "ratio" came out at 89 million. That is EMIN restated, not an
   engineering result. Fixed by giving the bracket a solid, non-design
   mounting lug — which is what real hardware has, because the bolt interface
   is a requirement and not something the optimiser may delete.
2. **Then the effect was real but tiny.** With one lug and three load
   *directions*, the measured penalty was 1.07× — because on a short
   cantilever straight-down *is* the worst direction, so optimising for it is
   already nearly robust. True, and not the episode. The honest move was to
   find the mechanism that does carry a large effect (damage tolerance, which
   the literature names explicitly) rather than to dress up a 7% result.
3. **I set a threshold before measuring and the generator refused.** Claim 3
   asserted that the 60%-mass bracket's damage sensitivity would fall below
   1.5×. It reads **1.63×**, so the script wrote nothing. The fix was to
   rewrite the claim to what the experiment shows — the penalty *collapses*
   by a factor of 19 (31.2× → 1.63×) while the part stays stiffer than the
   plate — and to assert that, as a ratio against a measured quantity rather
   than against a number I guessed.

A fourth thing worth recording: the worst-case damage location for both
designs initially came out *on the mounting pad*, i.e. the same floor
artefact as error 1. Patches overlapping the lug are now excluded from the
sweep, and the reel says what is excluded and why — severing the fitting is a
different failure from cracking a web.

## Verified, then deliberately NOT used

| Fact | Why |
|---|---|
| Airbus A320 "bionic partition", ~45% lighter | An aircraft part. The episode already has a flown spacecraft part and a flown AI-designed spacecraft part; a third from another industry dilutes both. |
| "40% weight reduction" and "30% above stiffness requirement" for the same RUAG bracket | Contradicted by ESA's own caption (32.9%, and "improved stability" with no figure). See the correction below. |
| Autodesk/JPL generative-design lander concept | Never flown. The reel's claim is that this is shipped engineering. |
| Neural-network surrogates for topology optimisation | They change the *speed* of the search, not what is being optimised — and the episode is about the problem statement. |
| ST5 antenna gain and beamwidth figures | The reel's point is that it flew and was human-competitive, not its radiation pattern. Extra numbers with unfamiliar units. |

## Softened on purpose

- **"A third lighter"** — ESA's 1.4 → 0.94 kg is 32.9%. The widely repeated
  "40%" is vendor framing and appears nowhere in this reel.
- **No stiffness claim for the Sentinel-1 part in the voice.** ESA says
  "improved stability" with no number, so the narration says only "a third
  lighter, on a real satellite".
- **The experiment is never presented as a model of the Sentinel-1 part** or
  of any flight hardware. B04–B08 and B10 all carry "computed in this reel".
- **"Thirty-one times softer" is named as a worst case** on screen, and the
  90th-percentile figure (3.4×) is shown beside it so the viewer can see the
  effect is broad rather than one freak location.
- **"The optimiser deletes the margin"** is a statement about *this
  formulation* — minimum compliance, fixed volume, one load case — and the
  reel says so. It is not a claim that commercial tools ship without
  fail-safe options. They have them; using them is the episode's own
  recommendation.
- **Compliance, not stress.** This measures stiffness under damage, not
  fracture. A real fail-safe case is a stress-and-crack-growth argument; the
  reel's claim is about load paths, which is what compliance sees.

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is an under-specified objective**, and it is new to this
   series: for the first time the model is not wrong at all. The optimum is
   provably optimal for the problem as written, and the deletion of the
   margin is not an error — it is compliance with the brief.
2. **The centrepiece is an experiment, not an anecdote**, and it asserts its
   own result. It refused once.
3. **The pitch is given its due before the catch.** B03 and B06 let
   generative design be genuinely good — a flown part and a measured 23% —
   because an episode that only debunks would be dishonest about a technique
   that works.
4. **The fix is priced, not just demanded.** B10 gives the cost in the
   currency that actually governs spacecraft: mass.
5. **Published and computed-here are separated** on screen and in the voice.
6. **No real hardware imagery, no reproduced figures, no redrawn plots.**
   Every plate is generated here. The Sentinel-1 bracket appears only as an
   isotype silhouette and a mass bar, never as a photograph or a traced
   outline.
7. **No claim that any real programme shipped a part without fail-safe
   analysis.** The weakness is demonstrated in simulation; the published
   literature is cited for the diagnosis and the fix, both of which those
   authors state themselves.
