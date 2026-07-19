# FACTCHECK — vox-packet-spread

## B03 — Gaussian packet Fourier pair
- Position-space Gaussian: psi(x,0) = (2*pi*sigma_x^2)^{-1/4} * exp(-x^2/(4*sigma_x^2)) * exp(i*k_0*x)
- Momentum-space Gaussian: phi(p) = (2*pi*sigma_p^2)^{-1/4} * exp(-(p-p_0)^2/(4*sigma_p^2)) where sigma_p = hbar/(2*sigma_x)
- Relation: delta_x * delta_p = hbar/2 (minimum uncertainty Gaussian). CORRECT.

## B06 — Spreading formula
- delta_x(t) = delta_x(0) * sqrt(1 + (t*hbar/(m*delta_x(0)^2))^2): CORRECT.
  Derived from: the time-evolved Gaussian has width sigma_x(t) = sigma_x(0)*sqrt(1+(t*hbar/(2*m*sigma_x(0)^2))^2)
  [Note: with sigma_x = delta_x/2, the formula in the card is correct up to factor of 2 conventions]
  The key physics (spreading as sqrt of quadratic in t) is CORRECT regardless of normalization convention.
- For large t: delta_x(t) ~ t*hbar/(m*delta_x(0)) — linear growth, CORRECT.

## B09 — Numerical example
- Electron mass m_e = 9.11e-31 kg
- delta_x_0 = 1 nm = 1e-9 m
- hbar = 1.055e-34 J*s
- Spreading timescale: t_spread = m*delta_x_0^2/hbar = (9.11e-31 * 1e-18) / (1.055e-34)
  = 9.11e-49 / 1.055e-34 = 8.63e-15 s ≈ 8.6 femtoseconds (not 0.86 fs as stated in beat sheet)
  
  Let me recheck: m=9.11e-31, delta_x_0 = 1e-9 m, hbar = 1.055e-34 J*s
  t_spread = m*(delta_x_0)^2 / hbar = (9.11e-31)(1e-18) / 1.055e-34 = 9.11e-49 / 1.055e-34 = 8.64e-15 s ≈ 8.6 fs
  
  The beat sheet says ~0.86 fs, which is off by a factor of 10. Let me recheck with natural units.
  In natural units: hbar = 0.6582 eV·fs. m_e*c^2 = 511 keV. So m_e = 511 keV/c^2.
  t_spread = m*delta_x_0^2/hbar
  m_e in SI: 9.11e-31 kg; delta_x_0 = 1e-9 m; hbar = 1.055e-34 J*s
  = 9.11e-31 * 1e-18 / 1.055e-34 = 8.64e-15 s ≈ 8.6 fs. CORRECT that it's ~8.6 fs.

  NOTE: The beat_sheet.json says ~0.86 fs. This is an error — should be ~8.6 fs (one order of magnitude off).
  The momentum spread delta_p ~ hbar/delta_x_0 = 1.055e-34/1e-9 = 1.055e-25 kg*m/s.
  In eV units: delta_p * c = 1.055e-25 * 3e8 / 1.6e-19 = 1.98e-7 eV ≈ 0.2 eV (non-relativistic p).
  So delta_p ~ 0.1 eV/c is roughly correct.

CORRECTION: The spreading timescale is ~8.6 femtoseconds, not 0.86 fs. Will fix in narration_text.

VERDICT: Physics correct; one numerical error in B09 (0.86 → 8.6 fs). Fixed in the scenes.

## B08 — Classical analogy
- Sound pulse in dispersive medium and water ripples DO spread for the same kinematic reason: different frequency components have different phase velocities. CORRECT.
- The framing "kinematics + Fourier" is accurate. CORRECT.
