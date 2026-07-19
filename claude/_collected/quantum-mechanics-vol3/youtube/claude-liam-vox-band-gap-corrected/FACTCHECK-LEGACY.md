# FACTCHECK — vox-band-gap

## Claims Audit

| Claim | Beat | Verdict | Source/Note |
|-------|------|---------|-------------|
| Free-electron energy is parabola E = ℏ²k²/2m | B04 | ✓ | Ch10: standard free-electron dispersion |
| Bragg reflection couples k=π/a to k=-π/a at wavelength 2a | B05 | ✓ | Ch10: "At k = π/a, the de Broglie wavelength λ = 2a satisfies the Bragg condition" |
| Two standing waves form: ψ+ peaked on ions, ψ- peaked between | B06 | ✓ | Ch10: "The probability density |ψ+|² peaks at the ion positions; |ψ-|² peaks between them" |
| ψ+ has lower energy (on ions = attractive), ψ- higher | B07 | ✓ | Ch10: "In a crystal where ions attract electrons, ψ+ sees lower potential energy and ψ- sees higher" |
| Gap = 2|V_G1| (twice the Fourier component) | B08 | ✓ | Ch10: "Their energy difference is 2|V_{G_1}|. This is the gap" |
| Insulator = filled band with gap; metal = Fermi level in band; semiconductor = small gap ~1 eV | B09 | ✓ | Ch10 Fig 10.3: "metal has Fermi level cutting through partially filled band; semiconductor has small gap; insulator has wide gap" |
| Silicon: lattice constant 5.4 Å, band gap 1.1 eV | B10 | ✓ illustrative | Standard solid-state values; Ch10 doesn't give these explicitly but they are canonical |
| Fourier component ≈ half the gap | B10 | ✓ | Follows directly from Gap = 2|V_G| → |V_G| = gap/2 = 0.55 eV |

## Terms Table
| Term | Debut Beat | Prior beat creating need |
|------|-----------|--------------------------|
| Bragg reflection / zone boundary | B05 | B04 establishes free-electron parabola |
| standing waves / ψ+, ψ- | B06 | B05 establishes zone boundary degeneracy |
| band gap / forbidden zone | B07 | B06 establishes two standing waves |
| metal/insulator/semiconductor | B09 | B08 establishes gap physics |

## Illustrative Numbers Check
- B10: Silicon a=5.43 Å (standard), E_g=1.12 eV (standard). |V_G| = E_g/2 = 0.56 eV ≈ 0.55 eV. ✓
