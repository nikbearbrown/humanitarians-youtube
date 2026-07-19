# FACTCHECK — vox-qubit-teleport

Source: `books/quantum-mechanics-vol4/chapters/05-quantum-teleportation-and-dense-coding.md`

## Claims audit

| Beat | Claim | Verdict | Source / Fix |
|------|-------|---------|-------------|
| B01 | Alice holds a state she can't read and can't copy | ✓ | Ch05 §No-Cloning: "she does not know them — a third party handed her the qubit"; no-cloning theorem |
| B02 | Measuring destroys the superposition | ✓ | Ch05: measurement collapses the state; the exact α,β are lost |
| B02 | Copying is forbidden by quantum mechanics | ✓ | Ch05 §No-Cloning: Wootters-Zurek 1982; Dieks 1982 |
| B02 | No quantum channel | ✓ | Ch05: "no quantum channel between them" is the protocol's premise |
| B04 | Measuring gives one bit (0 or 1), not the two amplitudes | ✓ | Ch05: computational-basis measurement collapses to |0⟩ or |1⟩; α,β are not recoverable from one shot |
| B05 | Alice and Bob pre-shared a Bell pair | ✓ | Ch05: "a pre-shared Bell pair" is the explicit resource; "Alice and Bob distributed the pair at some earlier time" |
| B05 | Alice holds qubit A, Bob holds qubit B | ✓ | Ch05 §Protocol Setup: "Qubit A belongs to Alice; qubit B belongs to Bob" |
| B06 | Neither qubit carries local information; Bell pair is maximally entangled | ✓ | Ch05 §Why No FTL: "Bob's reduced density matrix is I/2 — complete ignorance"; the pair is |Φ+⟩ which is maximally entangled |
| B08 | Alice runs her qubit and Bell-pair half through CNOT then Hadamard | ✓ | Ch05 Steps 1-2: "Alice applies CNOT (S control, A target)" then "Alice applies Hadamard to S" |
| B08 | This sorts the state into four branches (one per measurement outcome) | ✓ | Ch05: |Ψ₂⟩ is a sum of four terms with weights 1/2, each keyed by a two-bit outcome |00⟩, |01⟩, |10⟩, |11⟩ |
| B09 | Alice measures, gets one of four outcomes | ✓ | Ch05: "She gets one of four outcomes, each with probability 1/4" |
| B09 | Her qubit collapses; the superposition is gone | ✓ | Ch05: "Her qubit S collapses to a definite basis state — not to |ψ⟩. The state information has left S." |
| B10 | The state landed on Bob's qubit in scrambled form | ✓ | Ch05: after Alice's measurement, Bob's conditional state is one of I|ψ⟩, X|ψ⟩, Z|ψ⟩, or ZX|ψ⟩ |
| B11 | For outcome 10, Bob's qubit is Z applied to the original | ✓ | Ch05 correction table: outcome |10⟩ → Bob's conditional state is α|0⟩−β|1⟩ = Z|ψ⟩; correction: Z |
| B11 | The phase is flipped | ✓ | Z|ψ⟩ = α|0⟩−β|1⟩ — the sign on the |1⟩ component is negated |
| B12 | Alice sends two classical bits | ✓ | Ch05 Step 4: "She sends her two-bit outcome over the classical channel" |
| B12 | Bob applies Z for outcome 10, recovers |ψ⟩ | ✓ | Ch05 worked example: Z(α|0⟩−β|1⟩) = α|0⟩+β|1⟩ = |ψ⟩ ✓ |
| B13 | Before the call, Bob's qubit is completely random (I/2) | ✓ | Ch05: "The maximally mixed state. Whatever Alice measured, whatever α and β are, Bob sees the same thing: complete ignorance." ρ_B = I/2 explicitly derived |
| B13 | Teleportation is as fast as a phone call | ✓ | Ch05: "Those bits travel at or below the speed of light. Teleportation is as fast as a phone call, not faster." |
| B14 | Alice's example state: the plus state |+⟩ = (|0⟩+|1⟩)/√2 | ILLUSTRATIVE | Not from chapter; invented for pedagogical example. Labeled illustrative. |
| B14 | Outcome 10 for |+⟩ → Bob gets Z|+⟩ = |-⟩ = (|0⟩−|1⟩)/√2 | ILLUSTRATIVE (math is correct) | Z|+⟩ = Z(|0⟩+|1⟩)/√2 = (|0⟩−|1⟩)/√2 = |−⟩ ✓; invented scenario, labeled illustrative |
| B14 | Bob applies Z → recovers |+⟩ | ILLUSTRATIVE (math is correct) | Z|−⟩ = Z(|0⟩−|1⟩)/√2 = (|0⟩+|1⟩)/√2 = |+⟩ ✓ |
| B14 | One qubit moved, none copied | ✓ | Ch05: "The state has been teleported. Alice no longer has it. Bob does. No copy was made." |
| B15 | Resource accounting: 1 ebit + 2 cbits → 1 qubit transmitted | ✓ | Ch05 §Duality: "Teleportation: 1 ebit + 2 cbits → transmit 1 qubit" |

## Terms table

| Term | Debut beat | Need established by |
|------|-----------|-------------------|
| quantum state (superposition) | B01 | — (prerequisite) |
| copying forbidden / no-cloning | B02 | B01 (established the state Alice holds) |
| Bell pair / entangled pair | B05 | B02 (established the classical approach fails, so a resource is needed) |
| maximally entangled | B06 | B05 (Bell pair introduced) |
| CNOT gate | B08 | B07 (protocol section card frames what follows) |
| Hadamard gate | B08 | B08 (introduced together with CNOT as Alice's preparation step) |
| measurement outcome (00/01/10/11) | B09 | B08 (four branches explained) |
| collapses / collapsed | B09 | B08 (branches sorted; now one branch is selected) |
| scrambled / Z applied / phase flipped | B11 | B09 (measurement happened; result is on Bob's side) |
| classical bits | B12 | B07 (protocol intro); used throughout |
| maximally mixed state / I/2 | B13 | B12 (correction applied; now explaining why FTL is impossible) |
| plus state / minus state | B14 | B11-B12 (Z correction explained; example uses concrete states) |

## Exclusion confirmations

- **Three-qubit amplitude bookkeeping**: never shown. The |Ψ₀⟩, |Ψ₁⟩, |Ψ₂⟩ expansion does not appear anywhere.
- **Correction-table algebra**: the full 4-row table does not appear. Only outcome 10 → Z is shown, as part of the worked example.
- **Dense-coding dual**: not mentioned. The film treats only teleportation (1 ebit + 2 cbits → 1 qubit).

## Protocol reference

Bennett et al. (1993): Teleporting an unknown quantum state via dual classical and EPR channels. *Phys. Rev. Lett.* 70, 1895. ✓ (Ch05 cites this; the mechanism presented here matches the protocol in that paper.)
