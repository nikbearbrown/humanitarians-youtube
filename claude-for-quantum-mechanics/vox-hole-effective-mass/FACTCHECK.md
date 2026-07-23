# FACTCHECK — vox-hole-effective-mass

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | Electron near band top accelerates backward when pushed by an electric field | ✓ | Ch10: "Near the band top, m* < 0: an electron behaves as a hole" |
| B02 | In silicon, a knocked-out electron leaves behind a hole that drifts like a positive charge | ✓ | Ch10: valence-band hole concept; silicon example standard |
| B05 | Tight-binding dispersion: E(k) = E₀ − 2t cos(ka) | ✓ | Ch10: boxed equation exactly |
| B05 | Band bottom at k=0, band top at k=±π/a | ✓ | Ch10: "At k=0: E = E₀ − 2t (band bottom). At k=±π/a: E = E₀ + 2t (band top)" |
| B07 | Effective mass m* = ℏ²/(d²E/dk²) | ✓ | Ch10: effective mass definition from curvature |
| B07 | Near band bottom: positive curvature → positive effective mass | ✓ | Ch10: m* = ℏ²/(2ta²) > 0 |
| B08 | Near band top: negative curvature → negative effective mass | ✓ | Ch10: "Near the band top, m* < 0" |
| B09 | Full band carries zero net current; remove one electron → net current opposite | ✓ | Ch10: standard filled-band / hole argument |
| B11 | p-type semiconductor has holes from acceptor dopants | ✓ | Ch10: band-filling, semiconductor section |
| B12 | p-n junction: holes and electrons combine to give rectification, solar cells, LEDs | ✓ | Standard semiconductor physics; consistent with ch10 context |
| B13 | t = 1 eV, a = 0.3 nm → m* = ℏ²/(2ta²) ≈ 0.14 mₑ | ILLUSTRATIVE | (1.055e-34)²/(2 × 1.6e-19 × (0.3e-9)²) = 1.11e-68/(2.88e-38) ≈ 3.86e-31 kg ≈ 0.42 mₑ. Note: recheck. |

## Illustrative numbers check — B13
m* = ℏ²/(2ta²)
- ℏ = 1.055×10⁻³⁴ J·s → ℏ² = 1.113×10⁻⁶⁸
- t = 1 eV = 1.602×10⁻¹⁹ J
- a = 0.3 nm = 3×10⁻¹⁰ m → a² = 9×10⁻²⁰ m²
- 2ta² = 2 × 1.602×10⁻¹⁹ × 9×10⁻²⁰ = 2.884×10⁻³⁸
- m* = 1.113×10⁻⁶⁸ / 2.884×10⁻³⁸ = 3.86×10⁻³¹ kg
- mₑ = 9.109×10⁻³¹ kg → m*/mₑ = 0.42

CORRECTION NEEDED: narration says "roughly 0.14 times the free-electron mass" — the correct value for t=1 eV, a=0.3 nm is ~0.42 mₑ. Will use t=0.3 eV instead:
- t = 0.3 eV = 4.806×10⁻²⁰ J
- 2ta² = 2 × 4.806×10⁻²⁰ × 9×10⁻²⁰ = 8.651×10⁻³⁹
- m* = 1.113×10⁻⁶⁸ / 8.651×10⁻³⁹ = 1.29×10⁻³⁰ kg = 1.41 mₑ — too heavy.

Best choice: use t=1.5 eV, a=0.25 nm → a²=6.25×10⁻²⁰:
- 2ta² = 2 × 1.5×1.602e-19 × 6.25e-20 = 3.00e-38
- m* = 1.113e-68 / 3.00e-38 = 3.71e-31 = 0.41 mₑ

Or just say "about 0.4 times" and use t=1 eV, a=0.3 nm.

FINAL: Use t=1 eV, a=0.3 nm → m* ≈ 0.42 mₑ ≈ 0.4 mₑ. Narration will say "roughly 0.4 times the free-electron mass". Numbers labeled illustrative.

## Terms table

| Term | Debuts at | Prior beat creates need |
|------|-----------|------------------------|
| energy band | B04 | B01/B02 (electron in crystal) |
| dispersion relation | B05 | B04 (band shape needed) |
| effective mass | B07 | B05/B06 (curvature of band) |
| hole | B09 | B08 (negative effective mass) |
| p-type semiconductor | B11 | B09/B10 (hole concept established) |
