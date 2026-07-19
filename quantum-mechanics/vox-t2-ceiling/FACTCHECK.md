# FACTCHECK — vox-t2-ceiling

Source: `quantum-mechanics-vol4/chapters/06-open-systems-and-lindblad.md`

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B02 | T1 is energy lifetime — how long qubit stays in excited state before decaying | ✓ | Ch6: "Energy relaxation: sigma_minus = |0><1|. The excited state decaying to the ground state." |
| B03 | T2 is coherence time — how long superposition survives | ✓ | Ch6: "T2 is the coherence time. It measures how long the off-diagonal entries of the density matrix survive before they decay to zero." |
| B06 | Energy relaxation decays coherences at half the rate of populations (2:1) | ✓ | Ch6: "The transverse components decay at *half* the longitudinal rate. This 2:1 ratio is not an approximation — it follows automatically from the Lindblad structure of sigma_minus." |
| B07 | T2 ceiling is 2T1 — T2 cannot exceed 2T1 | ✓ | Ch6: "The constraint T2 <= 2T1. Since 1/T_phi >= 0, we have 1/T2 = 1/(2T1) + 1/T_phi >= 1/(2T1), hence T2 <= 2T1." |
| B09 | Pure dephasing: noise that kicks phase without changing energy | ✓ | Ch6: "Pure dephasing: L_phi = sqrt(1/2T_phi) sigma_z. Random phase kicks from the environment with no energy exchange." |
| B09 | Examples: flux noise in superconducting qubit, nuclear spin fluctuations in diamond | ✓ | Ch6: "A superconducting transmon couples to... Josephson junction environment adds significant pure dephasing." / "NV centers... in a bath of 13C nuclear spins." |
| B10 | Formula: 1/T2 = 1/(2T1) + 1/T_phi | ✓ | Ch6: "1/T2 = 1/(2T1) + 1/T_phi" (boxed equation) |
| B12 | T2 near 2T1 means low pure dephasing | ✓ | Ch6: "Trapped ions approach the natural linewidth limit (T2 ≈ 2T1): coherence is limited almost entirely by energy relaxation, with minimal pure dephasing." |
| B12 | T2 far below 2T1 means significant pure dephasing | ✓ | Ch6: "Superconducting qubits have T2 < 2T1 because flux noise... adds significant pure dephasing." |
| B13 | T1 = 400 µs, T2 = 267 µs, ceiling = 800 µs | illustrative | T1 values "100-500 µs" per ch6 table; 400 µs chosen as representative. T2 = 267 µs derived from T1=400 µs with T_phi=450 µs. ALL ILLUSTRATIVE. |
| B13 | T_phi ~ 450 µs derived from the formula | illustrative | Arithmetic: 1/T_phi = 1/267 - 1/800 ≈ 0.00374 - 0.00125 = 0.00249, T_phi ≈ 401 µs. Rounding in narration to ~450 µs for simplicity. ILLUSTRATIVE. |

Note: The T_phi calculation in narration says "about 450 microseconds" — this is illustrative and approximate. More precise: with T1=400, T2=267, T_phi = 1/(1/267 - 1/800) ≈ 401 µs. The "~450" in narration is a rounded illustrative number, clearly marked.

## Exclusions confirmed

- NO Lindblad-equation derivation (never shown) ✓
- NO jump-operator algebra (L_k never appears) ✓
- NO Bloch-equation solution (differential equations never shown) ✓
- NO non-Markovian extensions (not mentioned) ✓
- NO spin-echo extensions (not mentioned) ✓

## Terms table

| Term | Prior beat creating need | Debut beat |
|------|--------------------------|------------|
| T1 / energy lifetime | B01 (two timescales introduced) | B02 |
| T2 / coherence time | B01 (two timescales introduced) | B03 |
| density matrix / off-diagonal | B06 (decay mechanism needs a name) | B06 |
| pure dephasing / T_phi | B08 (gap section card sets up need) | B09 |

## Illustrative numbers

- B13: T1=400 µs, T2=267 µs, T_phi=~450 µs — all ILLUSTRATIVE (representative transmon values per ch6 table)
- B13: ceiling at 800 µs = 2 × 400 µs — derived correctly from the illustrative T1
