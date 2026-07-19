# FACTCHECK — medhavy-vol3-variational-floor

## Physics Claims

### Variational Principle
⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E₀ for all normalized ψ_trial.
Equality only when ψ_trial = exact ground state.

Source: Standard QM. VERIFIED.

### Helium variational energy E(Z*)
Trial state: hydrogen-like with effective Z*; both electrons screened.
E(Z*) = E_h × [Z*² × 2 − 2 × Z × 2Z* + (5/8) × Z*]
where Z=2 (helium), E_h = 27.2 eV (2 × Rydberg = 1 Hartree)

Full expression:
E(Z*) = 27.2 × (Z*² − (27/8)Z*)  (from Griffiths Eq. 7.27)

At Z*=2: E = 27.2 × (4 - 6.75) = 27.2 × (-2.75) = -74.8 eV
At Z*=27/16=1.6875: E_min = 27.2 × (1.6875² - 3.375×1.6875) = 27.2 × (2.848 - 5.695) = 27.2 × (-2.848) = -77.5 eV
True ground state E₀ = -79.0 eV (NIST)

All trial energies ≥ -79.0 eV ✓ (variational principle)

Source: Griffiths QM Chapter 7, NIST ASD. VERIFIED.

### Testable predictions
P1: minimum at Z* = 27/16 = 1.6875, E_min = -77.5 eV (above floor)
P2: true E₀ = -79.0 eV → curve never crosses this floor

VERDICT: PASS
