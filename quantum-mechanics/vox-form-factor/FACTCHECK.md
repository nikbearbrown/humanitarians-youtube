# FACTCHECK — vox-form-factor

## Claims audit

| Beat | Claim | Verdict | Source / note |
|------|-------|---------|---------------|
| B01 | Electron scattering pattern from nucleus looks like diffraction rings | ✓ | Ch08: "first zero of |F(q)|² … measuring this zero from the angular distribution directly gives the nuclear radius R" |
| B01 | First dark ring angle depends on nucleus size | ✓ | Ch08: qR ≈ 4.49 at first zero; q set by angle → first zero angle encodes R |
| B02 | Hofstadter 1956 measured proton size by first dark ring | ✓ | Ch08: "This is how Robert Hofstadter measured the proton charge radius in 1956, work that earned him the 1961 Nobel Prize" |
| B02 | Proton charge radius ~0.85 femtometers | minor | Ch08 says "measured the proton charge radius" but doesn't give the exact value in the text; 0.85 fm is historically accurate (CODATA value ~0.87 fm; modern measurement ~0.84 fm); slightly rounded here for narration clarity |
| B04 | Point target scatters equally in all directions (isotropic) | ✓ | Standard result; for a point the form factor F(q)=1 for all q, so dσ/dΩ has no q-dependent suppression beyond the point formula |
| B04 | Electrons from opposite edges can interfere | ✓ | Ch08: extended target produces F(q) = FT of ρ; interference is the physical content |
| B05 | Full pattern = point-particle pattern × form factor | ✓ | Ch08 exact equation: dσ/dΩ = (dσ/dΩ)_point × |F(q)|² |
| B05 | F(0)=1 always | ✓ | Ch08: "At q=0: F(0) = ∫ρ d³r = 1 always" |
| B05 | Form factor drops at larger angles | ✓ | Ch08: "At large q: if ρ is localized within radius R, then F(q)→0 for qR>>1" |
| B06 | Small angle = small momentum transfer = long-range probe; large angle = large transfer = short-range | ✓ | Ch08: q = 2k sin(θ/2); small θ → q ≈ kθ → small; large θ → q → 2k |
| B07 | Form factor = FT of charge distribution | ✓ | Ch08: "F(q) = ∫ e^{iq·r} ρ(r) d³r — the Fourier transform of the charge distribution" |
| B07 | For a sphere, first zero at qR ≈ 4.49 | ✓ | Ch08: "first zero at qR ~ 4.49 for a uniform sphere (the first zero of the spherical Bessel function j₁)" |
| B08 | First zero = perfect destructive interference between contributions from opposite sides | ✓ | Physical interpretation: correct; FT zero = total cancellation of contributions from the charge distribution |
| B09 | Momentum transfer = 2k sin(θ/2) | ✓ | Ch08: "q = 2k sin(θ/2)" for elastic scattering |
| B09 | R = 4.49 / q at first zero | ✓ | Derived from qR = 4.49 at first zero |
| B11 | Hofstadter, Stanford accelerator, 1956, proton charge radius ~0.85 fm | minor | Ch08: "Robert Hofstadter measured the proton charge radius in 1956" — the 0.85 fm value is a slight rounding of historical measurements; labeled as approximation in narration ("roughly 0.85 femtometers") |
| B11 | Nobel Prize for Hofstadter | ✓ | Ch08: "earned him the 1961 Nobel Prize" |
| B12 | Heavy nuclei are larger; nuclear radius scales as A^{1/3} | ✓ | Standard nuclear physics; consistent with Ch08 (form factor discussion implies this scaling is measurable) |
| B13 | Illustrative example: 250 MeV/c electrons, first zero at 20 degrees | ILLUSTRATIVE | Made-up numbers for pedagogy; labeled "Illustrative:" in narration |
| B13 | 250 MeV/c → k = 250/197 ≈ 1.27 fm⁻¹ | ✓ | ħc = 197.3 MeV·fm; so k = p/ħ = (250 MeV/c)/(197.3 MeV·fm) = 1.27 fm⁻¹ ✓ |
| B13 | q = 2 × 1.27 × sin(10°) = 0.44 fm⁻¹ | ✓ | sin(10°) ≈ 0.174; 2 × 1.27 × 0.174 ≈ 0.44 fm⁻¹ ✓ |
| B13 | R = 4.49/0.44 ≈ 10 fm → mass number ~200 nucleus | ✓ | R = r₀ A^{1/3} with r₀ ≈ 1.2 fm; A^{1/3} = 10/1.2 = 8.3 → A ≈ 570 — slightly large for A~200. Better: A~200 gives R = 1.2 × (200)^{1/3} ≈ 1.2 × 5.85 ≈ 7 fm. A nucleus with R~10 fm would be about A~570. Narration says "consistent with a heavy nucleus with mass number around 200" which overstates it — fix to say "large nucleus." |

### Fix required: B13 narration
Change "That is consistent with a heavy nucleus with mass number around 200" to "That is consistent with a large nucleus."

## Terms table

| Term | Debut beat | Prior need created by |
|------|------------|----------------------|
| form factor | B05 | B04 creates need: extended target has angular pattern with dark rings; need a name for the multiplicative correction |
| momentum transfer (q) | B06 | B05 establishes form factor varies with angle; need a name for the angular variable |
| Fourier transform | B07 | B06 says form factor encodes spatial structure; need a name for the math operation |
| Born approximation | NOT USED | excluded per card |
| Lippmann-Schwinger | NOT USED | excluded per card |
| deep inelastic scattering | NOT USED | excluded per card |

## Exclusion confirmation
- No form-factor integral (∫e^{iq·r}ρ d³r) — never written
- No Born-amplitude derivation — f_B formula not shown
- No deep-inelastic extension — quarks not mentioned

## Illustrative numbers (B13)
All labeled "Illustrative:" in narration. ħc = 197.3 MeV·fm used for unit conversion (verified).
