# FACTCHECK — vox-bloch-sphere

Source: quantum-mechanics-vol1/chapters/10-measurement-and-the-qubit.md

## Claims checked

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B02 | Qubit has 2 complex amplitudes = 4 real params; normalization removes 1; global phase removes 1; 2 remain | PASS | Ch.10: "Two real parameters specify the state, up to a global phase" |
| B04 | State parametrization: cos(θ/2)|0⟩ + e^iφ sin(θ/2)|1⟩ | PASS | Ch.10 eq. |ψ⟩ = cos(θ/2)|0⟩ + e^iφ sin(θ/2)|1⟩ |
| B05 | North pole θ=0 → |0⟩; south pole θ=π → |1⟩; equator θ=π/2 → equal superpositions | PASS | Ch.10: "at θ=0 we get |0⟩; at θ=π we get...e^iφ|1⟩; at θ=π/2 we get the equatorial state" |
| B06 | Different φ at same θ = different superposition with different x/y spin measurement outcomes | PASS | Ch.10: "different values of φ at the same θ give different ⟨σ_x⟩ and ⟨σ_y⟩" |
| B07 | Global phase e^iγ is unobservable; states differing only in global phase map to same Bloch point | PASS | Ch.10: "every normalized qubit state, up to a global phase" |
| B08 | Bloch vector = (⟨σ_x⟩, ⟨σ_y⟩, ⟨σ_z⟩); |r|²=1 for pure states | PASS | Ch.10: "For pure states, |r|²=1 exactly. This makes a useful runtime check" |
| B09 | Electron spin, photon polarization, superconducting circuit are all physical qubits | PASS | Ch.10: "An electron's spin, a photon's polarization, the two lowest energy levels of a superconducting circuit — all are physical qubits" |

## Exclusions honored
- No expectation-value derivation of Bloch vector
- No gate operations (rotations on sphere)
- No theta/2 double-cover/spinor-720 subtlety

## Verdict: PASS
