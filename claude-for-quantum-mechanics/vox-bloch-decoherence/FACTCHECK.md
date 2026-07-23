# FACTCHECK — vox-bloch-decoherence

Source: `quantum-mechanics-vol4/chapters/06-open-systems-and-lindblad.md`

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B02 | A qubit's state is an arrow on a sphere; surface = pure, center = classical | ✓ | Ch6: "Pure states have |r|=1 and sit on the surface of the Bloch sphere. Mixed states have |r|<1 and sit inside. The maximally mixed state I/2 has r=0." |
| B02 | Surface means pure superposition | ✓ | Ch6: Bloch representation section |
| B02 | Center means classical coin | ✓ | Ch6: "The maximally mixed state I/2 has r=0" — equal probability of 0 or 1 in all bases |
| B03 | Arrow precesses and stays on the surface (free unitary evolution) | ✓ | Ch6: "The von Neumann equation for a closed system preserves purity. The Bloch vector stays on the sphere surface and precesses." |
| B05 | Environment entangles with qubit, hiding state in correlations | ✓ | Ch6: "After a short time, H_SE couples them: |Ψ(t)⟩ = α|0⟩|e0(t)⟩ + β|1⟩|e1(t)⟩" |
| B07 | The arrow's length equals the overlap of environment branches | ✓ | Ch6: "The off-diagonal terms are suppressed by the overlap ⟨e0(t)|e1(t)⟩... As the environment branches become more orthogonal... this overlap decays toward zero." |
| B08 | As branches become more different, overlap decays; arrow shrinks inward | ✓ | Ch6: "When ⟨e0(t)|e1(t)⟩ = 0, the density matrix is diagonal... Quantum coherence has leaked into the environment." |
| B09 | Center = maximally mixed = equal probability in every direction | ✓ | Ch6: "It is now equally likely to be found in |0⟩ or |1⟩, but in a classical mixture, not a quantum superposition." |
| B10 | T2 is the coherence time; it appears in qubit datasheets | ✓ | Ch6: "T2 is the coherence time. It measures how long the off-diagonal entries of the density matrix survive." |
| B11 | T2 is the timescale for off-diagonal elements to reach zero | ✓ | Ch6: exact definition |
| B12 | Superconducting qubit T2 ~200 µs | ✓ (illustrative) | Ch6 Table: "superconducting transmon (100–500 µs)"; 200 µs is representative/illustrative |
| B12 | Trapped ion T2 ~seconds | ✓ | Ch6 Table: "trapped ions (seconds–minutes, seconds...)" |
| B12 | Cat-sized object decoherence ~10^-36 s | ✓ | Ch6: "decoherence times for dust grains in air are ~10^-36 s" — using "cat-sized object" as a fair extension of the macroscopic-object argument; labeled illustrative |
| B13 | We don't see Schrodinger's cat superposition because decoherence is 10^-36 s | ✓ | Ch6: "why macroscopic superpositions are never observed (decoherence times for dust grains in air are ~10^-36 s)" |
| B14 | T2 = 200 µs for transmon example | illustrative | Representative; see B12 above. Labeled illustrative. |
| B15 | T2 can be improved by better isolation / colder baths / more shielding | ✓ | Ch6 implies engineering improvements extend T2; dynamical decoupling mentioned; general physical reasoning ✓ |
| B15 | T2 cannot be made infinite | ✓ | Ch6: "Real hardware always has some pure dephasing. Coherence is always at least as fragile as population." |

## Exclusions confirmed

- NO Lindblad-equation derivation (formula never shown) ✓
- NO T2=1/(2T1)+1/Tphi algebra (formula never shown) ✓
- NO jump-operator formalism (Lk operators never appear) ✓

## Terms table

| Term | Prior beat creating need | Debut beat |
|------|--------------------------|------------|
| Bloch sphere | — (established by title hook: "arrow on a sphere") | B02 |
| pure state | B02 (surface of sphere introduced) | B02 |
| maximally mixed | B09 (arrow reaches center, all directions equal) | B09 |
| T2 / coherence time | B09-B10 (center reached, time question arises) | B10 |
| superposition | B02 (surface = superposition) | B02 |
| entanglement (environment) | B05 (environment shown coupling to qubit) | B05 |
| density matrix off-diagonals | B11 (after visual arrow; now naming the math) | B11 |

## Illustrative numbers

- B12: "~200 microseconds" for transmon T2 — ILLUSTRATIVE (representative value from chapter table range 100–500 µs)
- B12: "~seconds" for trapped ion T2 — ILLUSTRATIVE (representative)
- B12: "10^-36 seconds" for cat-sized object — from chapter text; labeled as striking comparison
- B14: "200 µs" for worked example transmon — ILLUSTRATIVE
