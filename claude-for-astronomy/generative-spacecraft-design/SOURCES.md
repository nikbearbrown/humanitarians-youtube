# SOURCES — *Nothing Left To Remove.*

Ep. 11 · `generative-spacecraft-design` · AI in Astronomy & Space Science
Checked from primary sources on **2026-10-02**, during this build.

---

## Published — a real AI-designed part that actually flew

**NASA Space Technology 5 evolved X-band antenna.**
Lohn, Hornby, Linden et al., NASA Ames Research Center.
- Hornby, Lohn, Linden, "Computer-Automated Evolution of an X-Band Antenna
  for NASA's Space Technology 5 Mission", *Evolutionary Computation* (2011).
- Lohn et al., "An Evolved Antenna for Deployment on NASA's Space
  Technology 5 Mission", *Genetic Programming Theory and Practice* (2004).
  NTRS citation 20040152147.

What the sources support, and nothing more:
- Two evolutionary algorithms were used — one genetic-algorithm
  representation that did **not** allow branching in the antenna arms, one
  genetic-programming tree representation that **did**.
- The best antennas from both were fabricated and tested, and both were
  **comparable in performance to a hand-designed antenna produced by a
  contractor for the mission** — the basis of the "human-competitive" claim.
- The design was approved for flight and **three copies flew on ST5 between
  22 March and 30 June 2006**.
- Described as the first evolved hardware, and the first evolved antennas,
  deployed in space.

The driving requirement was the combination of a **wide beamwidth for a
circularly-polarised wave with wide bandwidth** — i.e. the antenna was hard
to design by hand, which is why it is the right anchor for this episode.

**ESA Sentinel-1 upper S-band antenna support.**
ESA image caption, 2014-11 —
`esa.int/ESA_Multimedia/Images/2014/11/3D-printed_antenna_support`.
Quoted verbatim:

> "3D-printed prototype version of the support structure for ESA's
> Sentinel-1's upper S-band antenna, produced by RUAG Space Switzerland, with
> Altair and EOS. Produced in metal using selective laser melting, the
> redesigned part has a mass of 0.94 kg compared to the original part's mass
> of 1.4 kg, and also boasts improved stability. It was designed using
> 'topology optimisation', where software decides where material needs to go
> in order to best meet the part's function, constrained by its stress load
> and interface points with the rest of the satellite."

**A correction applied, per DOUBLE-CHECK LAW.** Vendor and trade-press
write-ups of this same part state "**40% weight reduction**" and "exceeded
stiffness requirements by 30%". ESA's own caption gives 1.4 kg → 0.94 kg,
which is a **32.9%** reduction, and says only "improved stability" with no
figure. **The reel uses ESA's numbers and says "a third lighter."** The 40%
and the 30% are not used anywhere, in the voice or on screen.

---

## Published — the weakness this episode measures

**Jansen, Lombaert, Schevenels, Sigmund (2014), "Topology optimization of
fail-safe structures using a simplified local damage model", *Structural and
Multidisciplinary Optimization* 49(4), 657–666.**

The damage model used in this reel is theirs: damage is introduced as a
**square void zone of a required size, placed one instance at a time at
locations across the design domain**, and the optimisation problem is posed
as minimising compliance **under the worst damage** — the damage that gives
the maximum compliance. This reel's survey is the same construction, used as
an *evaluation* rather than inside the optimiser.

**The standard statement of the problem**, from the fail-safe topology
optimisation literature (as surveyed in *Structural and Multidisciplinary
Optimization*, incl. doi 10.1007/s00158-021-02984-2 and the review in
doi 10.3390/app14020878):

> minimising compliance subject to a volume restriction "usually gives a
> structure that resembles a statically determinate structure with no
> redundant parts, meaning if one of the structural members was to break,
> there would not exist any alternative load-paths"

and, on the cost of fixing it:

> "Optimal topologies obtained by fail-safe methods are more complex and have
> greater volume than those from traditional topology optimization"

Also supported by that literature and used in the reel's framing:
- Fail-safe design with redundant load paths **is a requirement** in
  aerospace, and originated there.
- Local volume constraints are one accepted route to redundancy, because
  they force more, thinner members.

This matters for honesty: the reel's measured result is not a novel finding
and is not presented as one. The literature says single-load topology optima
are not fail-safe; this reel **measures how much that costs** on one concrete
bracket, and prices the fix in mass.

**Bendsøe & Sigmund, *Topology Optimization: Theory, Methods and
Applications*** — the SIMP scheme and the optimality-criteria update used in
`assets/topo.py`. The implementation is a port of Sigmund's widely used
reference code (the "99-line" / "88-line" MATLAB topology optimisation
programs) to numpy/scipy.

---

## Computed in this reel

`assets/topo.py` — the finite-element model and the SIMP optimiser.
`assets/gen_struct.py` — the experiment, the self-check, and all six plates.

**No random numbers anywhere.** SIMP from a uniform start is deterministic
given the problem, so there is no seed to log. The parameters are:

| | |
|---|---|
| Mesh | 120 × 60 bilinear quads, 7,200 elements, 14,762 dofs |
| Material | E = 1, ν = 0.3, plane stress; SIMP penalty p = 3, floor 1e-9 |
| Filter | sensitivity filter, radius 2.4 elements |
| Support | the whole left edge fixed (the bolted root) |
| Lug | 6 × 6 solid, non-design elements at the free end, mid-height, charged to the mass budget |
| Load | unit load, straight down, on the lug |
| Mass budgets | 40%, 50%, 60% of the design volume |
| Iterations | 90, optimality-criteria update, move limit 0.2 |
| Damage | 8 × 8 void (0.89% of the domain) swept over 398 locations at a 4-element stride; patches overlapping the lug excluded |

**FE validation** (`scratchpad/fecheck.py`, reported in FACTCHECK):
exact symmetry; exactly 3 zero eigenvalues; all three rigid-body motions in
the nullspace to machine precision; the uniaxial patch test exact to six
digits; and the solid cantilever 1.4–1.9% softer than Euler–Bernoulli, which
is the correct direction and magnitude for a short deep beam carrying shear.

**A correctness check that is also a result.** The domain, the support and
the load are all symmetric about mid-height, so the optimum must be too. The
generator asserts it (`max|x − mirror(x)| ≤ 0.02`) and the run reports the
measured value. An asymmetric answer would mean the element dof ordering is
wrong — a failure that would otherwise be invisible, because a mis-ordered
stiffness matrix is still symmetric and still solves.

---

## Verified, then deliberately NOT used

| Fact | Why |
|---|---|
| Airbus A320 "bionic partition" — generative design, quoted ~45% lighter | An aircraft cabin part, not spacecraft. The episode already has one flown spacecraft part (ESA/RUAG) and one flown AI-designed spacecraft part (ST5); a third example from a different industry would dilute both. |
| The "40% lighter / 30% stiffer" figures for the RUAG bracket | Contradicted by ESA's own caption. See the correction above. |
| Autodesk/JPL generative-design interplanetary lander concept | A concept study, never flown. The reel's claim is that this is *shipped* engineering, so a concept would weaken it. |
| Neural-network surrogates that accelerate topology optimisation (e.g. TopologyGAN and successors) | A genuinely interesting follow-on, but it changes the *speed* of the search, not what the search optimises — and the episode's whole point is about the problem statement, not the solver. Named nowhere. |
| Relativity Space and other 3D-printed launch hardware | Additive manufacturing is the enabling process, not the design method. The episode is about who chooses the shape. |

---

## Softened on purpose

- **"A third lighter"** for the Sentinel-1 bracket — ESA's 1.4 → 0.94 kg is
  32.9%, stated as a third, never as 40%.
- **The experiment is never presented as a model of the Sentinel-1 part or of
  any flight hardware.** Every computed beat carries "computed in this reel"
  on its citation line. The mesh, the loads and the mass budget are chosen to
  be *illustrative of the mechanism*; only the direction and the rough size
  of the effect are claimed.
- **"The optimiser removes the margin"** is a statement about this
  formulation — minimum compliance at a fixed volume, one load case — and the
  reel says so. It is not a claim that commercial generative-design tools
  ship without fail-safe options; they have them, and using them is the
  episode's own recommendation.
- **The worst-case damage figure is a worst case** and is named as one on
  screen. The 90th-percentile figure is shown beside it so the viewer can see
  the effect is broad and not one freak location.
- **Compliance, not stress.** This reel measures stiffness under damage, not
  failure. A real fail-safe assessment is a stress-and-fracture argument; the
  reel's claim is about load paths, which is what compliance sees.
