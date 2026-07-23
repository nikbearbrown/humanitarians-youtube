# FACTCHECK — medhavy-vol3-stm-tunneling

## Physics Claims

### WKB tunneling formula
T ≈ exp(−2κd), κ = √(2mφ)/ℏ
For φ = 4 eV (typical metal work function):
  m = 9.109×10⁻³¹ kg
  φ = 4 eV = 4×1.602×10⁻¹⁹ J = 6.408×10⁻¹⁹ J
  ℏ = 1.055×10⁻³⁴ J·s
  κ = √(2 × 9.109×10⁻³¹ × 6.408×10⁻¹⁹) / (1.055×10⁻³⁴)
    = √(1.168×10⁻⁴⁹) / 1.055×10⁻³⁴
    = 1.081×10⁻²⁵ / 1.055×10⁻³⁴
    ≈ 1.024×10⁹ m⁻¹ = 1.024 Å⁻¹

Source: WKB approximation, Griffiths QM Chapter 9. VERIFIED.

### Seven-times rule (Binnig-Rohrer)
Factor per +1 Å: exp(2κ × 1 Å) = exp(2 × 1.024) = exp(2.048) ≈ 7.75
Commonly quoted as "factor of e² ≈ 7.4" or "roughly 7–10 per Å"
The scene uses exp(2.048) ≈ 7.7 which is consistent with the published rule.

Source: Binnig & Rohrer, Rev. Mod. Phys. 59, 615 (1987). VERIFIED.

### Testable predictions
P1: slope of ln(I) vs d = −2κ ≈ −2.05 Å⁻¹ (for φ=4 eV)
P2: current ratio over 1 Å gap change = exp(2κ) ≈ 7.7 (Binnig-Rohrer rule)

VERDICT: PASS
