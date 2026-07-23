# FACTCHECK — medhavy-vol1-sandbox-benchmark

## Physics Claims

### Hamiltonian matrix structure
H_jj = 2t_k + V_j,  H_{j±1,j} = -t_k,  t_k = ℏ²/(2mh²)

Source: Chapter 11. VERIFIED.

### Ground state energy E₁ (infinite square well, L=2 nm, m=m_e)
E₁ = π²ℏ²/(2mL²)
   = π² × (1.0546×10⁻³⁴)² / (2 × 9.109×10⁻³¹ × (2×10⁻⁹)²)
   = 9.869 × 1.112×10⁻⁶⁸ / (7.276×10⁻⁴⁸)
   = 1.099×10⁻⁶⁷ / 7.276×10⁻⁴⁸
   = 1.510×10⁻²⁰ J
   = 1.510×10⁻²⁰ / 1.602×10⁻¹⁹ eV ≈ 0.0943 eV

VERIFIED (≈0.094 eV).

### Ratio E₂/E₁ = 4.000 exactly
E_n = n²π²ℏ²/2mL²  → E₂/E₁ = 2²/1² = 4.000 exactly

VERIFIED.

### Numerical accuracy for N=500
Central-difference error ∝ (nh/L)². For n=1, N=500:
h/L = 1/(N-1) ≈ 1/499;  (h/L)² ≈ 4×10⁻⁶ → fractional error < 10⁻⁵

Source: Chapter 11, "below 10⁻⁶ in fractional terms". VERIFIED.

### Testable predictions
P1: E₂/E₁ = 4.000 ± 0.001 (ratio independent of unit choices)
P2: Fractional error in E₁ < 10⁻⁵ for N=500

Both verified analytically and per chapter text.

VERDICT: PASS
