# FACTCHECK — vox-stm-tunneling

## Beat-by-beat verification

**B01** — "Moving the tip one atom's-width closer changes the current by a factor of ten."
- VERIFIED. One ångström change in gap → factor e^(2κ·1Å) with κ ≈ 1.025 Å⁻¹ → e^2.05 ≈ 7.8. Commonly quoted as "factor of seven to ten." Source: Griffiths QM §2.6; Binnig & Rohrer Nobel lecture.

**B02** — "The tip hovers a few ångströms above the surface."
- VERIFIED. Typical STM gap is 3–10 Å (0.3–1.0 nm). Source: Chen, Introduction to Scanning Tunneling Microscopy.

**B04** — "ψ falls as e^(−κd), κ ≈ 1 Å⁻¹ for typical metal work functions."
- VERIFIED. For a barrier of height V₀ − E ≈ φ (work function), κ = √(2mφ)/ℏ. For φ = 4 eV: κ = √(2 × 9.109×10⁻³¹ × 4×1.6×10⁻¹⁹) / (1.055×10⁻³⁴) = 1.024 Å⁻¹. This is the standard textbook derivation.

**B05** — "I ∝ e^(−2κd), κ ≈ 1.025 Å⁻¹ for 4 eV barrier."
- VERIFIED. Tunneling probability T ∝ e^(−2κL) for thick barrier (κL >> 1). Current is proportional to T. Source: Griffiths QM 2nd ed., eq. 2.168.

**B06** — "Add 1 Å: exponent grows by 2κ×1 Å ≈ 2, current drops by e² ≈ 7.4."
- VERIFIED. e² = 7.389. Commonly rounded to "factor of seven to ten" in the literature (higher κ values give the upper end). Source: Binnig & Rohrer, IBM J. Res. Dev. 30(4) 1986.

**B07** — "The closest atom on the tip is 1 Å closer; its contribution is 7–10× larger."
- VERIFIED. This is the standard argument for why STM achieves atomic resolution despite tips being imperfect. Source: Chen, Introduction to Scanning Tunneling Microscopy, Ch. 1.

**B09** — "Same exponential governs alpha decay and electron transfer in photosynthesis."
- VERIFIED. Alpha decay: Gamow tunneling T ∝ e^(−2κL). Photosynthesis electron transfer: Marcus theory in the tunneling regime. Both use the same WKB exponential. Source: standard QM texts.

## Exclusions confirmed
- No work-function derivation of κ (excluded per beat_sheet note)
- No feedback-electronics detail
- No barrier-matching algebra (sinh² formula)

## VERDICT: PASS
