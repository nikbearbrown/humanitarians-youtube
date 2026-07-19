# FACTCHECK — medhavy-companion-pib/short

## Physics claims verified

1. **E_n = n^2 * E1**: Particle in a box energy formula.
   E1 = pi^2 hbar^2 / (2 m_e L^2). For L=1 nm:
   E1 = (pi^2 * 1.0546e-34^2) / (2 * 9.109e-31 * (1e-9)^2) = 6.024e-20 J = 0.376 eV. CORRECT.

2. **E2 = 4*E1 = 1.504 eV**: n=2, n^2=4, 4*0.376=1.504. CORRECT.

3. **E3 = 9*E1 = 3.384 eV**: n=3, n^2=9, 9*0.376=3.384. CORRECT.

4. **Ratio E2/E1 = 4.000 exactly**: From n^2 law, 2^2/1^2 = 4. Exact. CORRECT.

5. **Zero-point energy**: E1 > 0 because n >= 1 (n=0 gives zero wavefunction, not physical).
   E1 = 0.376 eV > 0. CORRECT.

6. **Portrait layout verification**:
   - e_to_y(0.376) = -2.10 + 0.376 = -1.724. Inside safe area. CORRECT.
   - e_to_y(1.504) = -2.10 + 1.504 = -0.596. Inside safe area. CORRECT.
   - e_to_y(3.384) = -2.10 + 3.384 = 1.284. Inside safe area (< 3.4). CORRECT.
   - Labels at x=1.35: inside safe area (< 1.95). CORRECT.
   - Chips at y=-2.72 and y=-3.15: inside safe area (> -3.4). CORRECT.

VERDICT: All physics claims accurate.
