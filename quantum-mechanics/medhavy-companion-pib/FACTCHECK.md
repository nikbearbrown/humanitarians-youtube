# FACTCHECK — medhavy-companion-pib

## Formula: E_n = n²π²ℏ²/(2mL²)
  Source: Griffiths QM Ed.3 §2.2, Eq. 2.27
  Verified: E_1 = (π² × (1.0546e-34)²) / (2 × 9.109e-31 × (1e-9)²)
            = (9.870 × 1.112e-68) / (1.822e-48)
            = 1.098e-67 / 1.822e-48 = 6.026e-20 J
            = 6.026e-20 / 1.602e-19 eV = 0.3762 eV ≈ 0.376 eV ✓
  E_2 = 4 × 0.376 = 1.504 eV ✓
  E_3 = 9 × 0.376 = 3.384 eV ✓

## Numbers:
  - L = 1 nm = 1e-9 m (stated)
  - m_e = 9.109e-31 kg (NIST CODATA 2018)
  - ℏ = 1.0546e-34 J·s (NIST CODATA 2018)
  - E_1 ≈ 0.376 eV (computed above) ✓
  - E_2 ≈ 1.504 eV = 4 × E_1 ✓
  - Ratios 1:4:9 = n² law ✓

## Two testable predictions:
  P1: E_2/E_1 = 4.000 exactly (from n² law, n=2 vs n=1) ✓
  P2: Halving L from 1 nm to 0.5 nm → E_1 quadruples to 4 × 0.376 = 1.504 eV
      (E_1 ∝ 1/L² so (1/0.5)² = 4× factor) ✓

VERDICT: PASS
