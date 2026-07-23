# FACTCHECK — medhavy-vol1-harmonic-ladder

## Formula: E_n = ℏω(n + 1/2)
  Source: Vol1 Ch7 §"Climbing the Ladder"; Griffiths §2.3
  Verified: Standard result from ladder operator algebra [a−, a+]=1.
  Ground state n=0: E_0 = ℏω/2 (not zero)
  Level spacing: E_{n+1} − E_n = ℏω (uniform)

## Numbers: ℏω for ω = 10¹⁴ rad/s
  Source: NIST CODATA 2018: ℏ = 1.0546×10⁻³⁴ J·s
  ℏω = 1.0546×10⁻³⁴ × 10¹⁴ = 1.0546×10⁻²⁰ J
  = 1.0546×10⁻²⁰ / 1.602×10⁻¹⁹ eV = 0.0659 eV ≈ 0.066 eV ✓

## Numbers: Ground state energy ℏω/2 ≈ 0.033 eV
  Source: E_0 = ℏω/2 = 0.066/2 = 0.033 eV ✓

## Testable prediction P1: E_1 − E_0 = E_2 − E_1 = ℏω exactly (uniform spacing)
  Source: E_n = ℏω(n+1/2) → spacing = ℏω regardless of n ✓

## Testable prediction P2: lowest rung at ℏω/2 > 0 (not zero)
  Source: n=0 is minimum (a−|0⟩ = 0 argument); E_0 = ℏω/2 > 0 ✓
  This is the zero-point energy; the harmonic oscillator ground state
  saturates the Kennard bound σ_x σ_p = ℏ/2 (verified in Ch11 exercise)

## Narration claim: "ladder cannot descend forever — there is a floor"
  Source: H = sum of squares of Hermitian operators → ⟨H⟩ ≥ 0;
  combined with ladder lowering by ℏω → ground state must exist where a−|0⟩=0 ✓

VERDICT: PASS
