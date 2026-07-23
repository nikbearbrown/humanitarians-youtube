# FACTCHECK — medhavy-vol1-pib-spectrum

## Formula: E_n = n²π²ℏ²/(2mL²)
  Source: Griffiths §2.2; Vol1 Ch5 §"The Derivation in Eight Steps"
  Verified: Standard result for infinite square well with hard walls at x=0 and x=L.
  E_n = n²·(π²ℏ²)/(2m_e L²). For L=2 nm, m=m_e:
    E_1 = (1)²×(π²×(1.055×10⁻³⁴)²)/(2×9.109×10⁻³¹×(2×10⁻⁹)²)
        = π²×1.113×10⁻⁶⁸/(7.287×10⁻⁴⁸)
        = 9.869×1.113×10⁻⁶⁸ / 7.287×10⁻⁴⁸
        = 1.510×10⁻²⁰ J = 0.0943 eV ≈ 0.094 eV ✓
  Source: NIST CODATA 2018: ℏ = 1.0546×10⁻³⁴ J·s, m_e = 9.1094×10⁻³¹ kg

## Numbers: E_1 ≈ 0.094 eV (L=2 nm, electron)
  Source: Vol1 Ch11 caption: "E_1 ≈ 0.094 eV" directly stated
  Verified: 0.0943 eV rounds to 0.094 eV ✓

## Numbers: E_2/E_1 = 4 exactly
  Source: E_n ∝ n², so E_2/E_1 = 4/1 = 4.000 exactly ✓

## Numbers: E_3/E_1 = 9 exactly
  Source: E_n ∝ n², so E_3/E_1 = 9/1 = 9.000 exactly ✓

## Numbers: halving L from 2 nm to 1 nm quadruples E_1
  Source: E_1 ∝ 1/L² → reducing L by factor 2 multiplies E_1 by 4 ✓
  E_1(L=1 nm) = 0.094 × 4 = 0.376 eV ✓

## Numbers: E_1(L=1 nm) ≈ 0.376 eV
  Source: direct calculation: π²ℏ²/(2m_e × (1×10⁻⁹)²) = 4 × 0.094 eV = 0.376 eV ✓

## Narration claim: "E_n grows as n-squared"
  Source: explicit in formula E_n = n²×E_1 ✓

## Narration claim: "ground state energy is not zero"
  Source: n starts at 1, never 0; E_1 = π²ℏ²/2mL² > 0 ✓

## Code claim: PHI=2.28 eV is NOT used in this reel
  This reel is purely about PIB; no work function referenced ✓

## Two testable predictions:
  P1: E₂/E₁ = 4.000 exactly (ratio test, unit-independent)
    → sim output must show ratio 4.000 ± 0.001
  P2: halving L from 2 nm to 1 nm quadruples E₁ (0.094 → 0.376 eV)
    → change L slider in CHANGE beat and verify

VERDICT: PASS
