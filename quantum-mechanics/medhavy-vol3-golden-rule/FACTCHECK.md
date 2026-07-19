# FACTCHECK — medhavy-vol3-golden-rule

## Physics Claims

### Fermi's Golden Rule
Γ = (2π/ℏ) |⟨f|V̂|i⟩|² ρ(E_f)
Rate is proportional to |matrix element|² and density of states at final energy.

Source: Fermi (1950), Dirac (1927). Standard QM result. VERIFIED.

### Hydrogen 2p→1s transition
A coefficient (Einstein A, spontaneous emission rate):
  A(2p→1s) = 6.27×10⁸ s⁻¹  (NIST Atomic Spectra Database)
  Lifetime τ = 1/A ≈ 1.595 ns ≈ 1.6 ns
  Lyman-α photon energy: E = 13.6(1 - 1/4) = 10.2 eV → λ = hc/E ≈ 121.6 nm

Source: NIST ASD. VERIFIED.

### Matrix element (Lyman-alpha)
The electric-dipole matrix element for H 2p→1s is:
  |⟨1s|er|2p⟩| ≈ 0.745 a₀ × e ≈ 0.745 × 0.529 Å × 1.6×10⁻¹⁹ C
In energy units for this reel's quadratic plot, we use V = |⟨f|Ĥ'|i⟩| normalized
so that Γ(V_H) = A_H = 6.27×10⁸ s⁻¹ at V_H ≈ 4.2×10⁻⁵ eV.
This is a rescaled display coupling — the key physics is the V² scaling.

### Testable predictions
P1: rate scales as V² (log-log slope = 2; doubling V → 4× rate)
P2: at V = V_H: Γ = A_H = 6.27×10⁸ s⁻¹ (matches NIST)

VERDICT: PASS
