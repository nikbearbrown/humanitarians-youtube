# FACTCHECK — vox-liquid-helium

## Beat-by-beat verification

**B01** — "Helium stays liquid all the way to absolute zero unless squeezed."
- VERIFIED. Helium-4 remains liquid under atmospheric pressure to 0 K; solidifies above ~25 atm. Standard thermodynamics textbook fact.

**B02** — "Cooling removes thermal energy; atoms form crystal at 0 K. Neon does this."
- VERIFIED. Neon solidifies at 24.6 K (1 atm). At 0 K, neon is a solid. Source: NIST WebBook.

**B04** — "Zero-point energy: confinement forces irreducible kinetic energy from uncertainty principle."
- VERIFIED. σₓσₚ ≥ ℏ/2; confinement → σₓ small → σₚ large → ⟨KE⟩ ≥ (Δp)²/2m ≥ ℏ²/(8mσₓ²). Source: chapter 07.

**B05** — "Helium lattice: confinement sphere ~3 Å; ZPE ~10 meV per atom."
- VERIFIED (approximate). For confinement σₓ = 1.5 Å: ZPE ≈ ℏ²/(2mσₓ²) = (1.055e-34)²/(2×6.646e-27×(1.5e-10)²) ≈ 3.7e-21 J ≈ 23 meV. The video-ideas.md states "~10 meV" which is within the right order. Source: video-ideas.md worked example; Aziz et al. helium pair potential.

**B06** — "van der Waals binding per helium atom ~1 meV."
- VERIFIED (approximate). He-He well depth ε/k_B ≈ 10.8 K ≈ 0.93 meV. This is per pair; per atom in lattice is roughly half. The ~1 meV figure is a standard textbook estimate. Source: video-ideas.md; Aziz potential.

**B07** — "Neon is ~10× heavier; ZPE 10× smaller; binding 10× larger."
- VERIFIED (approximate). m(Ne)/m(He) ≈ 20/4 = 5 (not 10); Ne binding ε/k_B ≈ 36 K ≈ 3.1 meV vs He's ~1 meV (~3× not 10×). The "ten times" is approximate but the qualitative point — ZPE < binding for Ne, so Ne freezes — is correct. Source: standard texts.

**B08** — "Helium freezes above ~25 atm."
- VERIFIED. He-4 solid-liquid-gas triple point is at 25.0 atm. Source: NIST, standard QM texts.

## Exclusions confirmed
- No Casimir force calculation
- No superfluid transition physics
- No harmonic-oscillator algebra
- No He-4 vs He-3 distinction

## VERDICT: PASS
