# FACTCHECK — medhavy-vol5-group-phase-velocity

## Formula: v_group = dw/dk; v_phase = w/k
  For quadratic dispersion w = hbar*k^2/(2*m):
  v_group = dw/dk = hbar*k/m
  v_phase = w/k = hbar*k/(2*m)
  So v_group = 2 * v_phase ✓
  Source: Griffiths QM Ed.3 §2.4; Shankar "Principles of Quantum Mechanics" Ch.4

## Numbers:
  - k0 = 1 nm^-1 = 1e9 m^-1 (electron with this wavevector)
  - hbar = 1.0546e-34 J*s
  - m_e = 9.109e-31 kg
  - v_group = hbar*k0/m_e = 1.0546e-34 * 1e9 / 9.109e-31
            = 1.0546e-25 / 9.109e-31 = 1.158e5 m/s approx 1.2e5 m/s ✓
  - v_phase = v_group/2 = 5.79e4 m/s ✓
  - w0 = hbar*k0^2/(2*m_e) = 1.0546e-34*(1e9)^2/(2*9.109e-31)
       = 1.0546e-34*1e18/1.822e-30 = 1.0546e-16/1.822e-30 = 5.79e13 rad/s ✓

## Two testable predictions:
  P1: v_group = 2 * v_phase for quadratic dispersion (from dw/dk = 2*w/k) ✓
  P2: Group velocity = centroid velocity of |psi|^2 (envelope peak tracks <x>(t)) ✓

VERDICT: PASS
