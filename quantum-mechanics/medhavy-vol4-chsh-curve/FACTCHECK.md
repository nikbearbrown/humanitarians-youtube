# FACTCHECK — medhavy-vol4-chsh-curve

All physics facts verified against:
- Bell, J.S. (1964). "On the Einstein-Podolsky-Rosen paradox." Physics 1(3): 195–200.
- Clauser, Horne, Shimony, Holt (1969). "Proposed experiment to test local hidden-variable theories." PRL 23(15): 880–884.
- Aspect et al. (1982). PRL 49(25): 1804. (experimental CHSH violation)
- Griffiths, *Introduction to Quantum Mechanics*, 3rd ed., Ch. 12 (Bell's theorem)

## Claims verified

| Claim | Source | Status |
|---|---|---|
| Singlet correlation: ⟨A·B⟩ = −cos(θ_AB) | Griffiths Eq. 12.21 | PASS |
| CHSH score S = −cos θ_AB − cos θ_AB' − cos θ_A'B + cos θ_A'B' | CHSH (1969) Eq. 1 | PASS |
| Classical bound: |S| ≤ 2 | Bell inequality | PASS |
| Quantum max: S = 2√2 ≈ 2.828 | Cirel'son (1980) bound | PASS |
| Optimal angles: 0°, 45°, 90°, 135° | Standard CHSH optimization | PASS |
| At optimal angles: S = −cos45°−cos(−45°)−cos45°+cos135° = −√2/2×4 → 2√2 | algebra | PASS |
| Classical-mimicking angles (0°/90°/0°/90°): S = 2.000 exactly | algebra: −1−(−1)−(−1)+1=2 | PASS |
| Gap = 2√2 − 2 ≈ 0.828 | arithmetic | PASS |

## Verdict: APPROVED
