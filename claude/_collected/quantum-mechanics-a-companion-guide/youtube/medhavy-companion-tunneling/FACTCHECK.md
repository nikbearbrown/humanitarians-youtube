# FACTCHECK — medhavy-companion-tunneling

## Formula: T approx e^(-2*kappa*d)
  Source: Griffiths QM Ed.3 §2.6, Eq. 2.169 (WKB/exact barrier transmission)
  kappa = sqrt(2*m*(V0-E)) / hbar
  Verified: V0=1 eV, E=0.5 eV, so (V0-E)=0.5 eV = 0.5*1.602e-19 = 8.01e-20 J
    kappa = sqrt(2 * 9.109e-31 * 8.01e-20) / 1.0546e-34
          = sqrt(1.459e-49) / 1.0546e-34
          = 1.208e-25 / 1.0546e-34
          = 1.146e9 m^-1 = 1.146 nm^-1 = 0.1146 Angstrom^-1
  Wait — the given value says "each Angstrom multiplies T by ~1/7.4"
  Check: e^(-2*kappa*1 Angstrom) = e^(-2*0.1146*10) = e^(-2.292) = 0.101 ≈ 1/9.9
  Hmm, the candidate says kappa=1.02 Angstrom^-1 for phi=4 eV (STM work function).
  For the companion tunneling: V0=1 eV, E=0.5 eV:
    kappa = sqrt(2*9.109e-31*(0.5*1.602e-19)) / 1.0546e-34
          = sqrt(2*9.109e-31*8.01e-20) / 1.0546e-34
          = 1.208e-25 / 1.0546e-34 = 1.146e9 m^-1 = 1.146 nm^-1
  Per-Angstrom factor: e^(-2*1.146e9*1e-10) = e^(-0.2292) = 0.795 per Angstrom
  So each Angstrom (0.1 nm) multiplies T by e^(-2*0.1146) = e^(-0.2292) ≈ 0.795
  Each nanometer: e^(-2*1.146) = e^(-2.292) ≈ 0.101

  For "each Angstrom multiplies T by ~1/7.4" the candidate notes this uses
  typical metal work function (phi~4 eV, kappa~1.02 Ang^-1). That's the STM context.
  For our V0=1 eV, E=0.5 eV: kappa=0.1146 Ang^-1, each Ang multiplies by e^(-0.229)=0.795.

  The slug says "each Angstrom multiplies T by e^2 approx 7.4" — this is from the
  SIMULATION IDEAS doc which uses V0-E=0.5 eV giving kappa=0.1146 Ang^-1 (not 1.02).
  Actually re-reading: "each Å step" — the 1/7.4 factor is for VOL3 STM context (phi=4 eV).
  For companion tunneling V0=1 eV, E=0.5 eV: factor per 1 nm = 0.101 = 1/9.9.

  The narration will say "each nanometer reduces T by about 10x" which is correct
  for these parameters. The "1/7.4" in the task spec refers to the vol3-stm reel.

## Numbers (companion tunneling, V0=1 eV, E=0.5 eV, L=1 nm range):
  - V0 = 1 eV, E = 0.5 eV (given)
  - kappa = 1.146 nm^-1 (computed above) ✓
  - At d=0.5 nm: T = e^(-2*1.146*0.5) = e^(-1.146) = 0.318
  - At d=1.0 nm: T = e^(-2*1.146*1.0) = e^(-2.292) = 0.101
  - At d=2.0 nm: T = e^(-2*1.146*2.0) = e^(-4.584) = 0.0102
  - log(T) vs d is linear with slope = -2*kappa = -2.292 per nm ✓

## Two testable predictions:
  P1: At d=0, T=1 (exponential starts at 1 when barrier width is zero) ✓
  P2: log(T) vs d is perfectly linear (slope = -2*kappa); each nanometer
      reduces T by factor e^(-2*1.146) = 0.101 approx 1/10 ✓

VERDICT: PASS
