# FACTCHECK — medhavy-vol5-group-phase-velocity/short

## Physics claims verified

1. **Quadratic dispersion**: omega = hbar*k^2/(2m). In natural units (hbar=m=1): omega = k^2/2.
   - Source: standard quantum mechanics; Griffiths, Sakurai.

2. **Phase velocity**: v_phase = omega/k = k/2 (for omega=k^2/2). At k0=2: v_phase = 1.
   - Verified: omega0 = k0^2/2 = 2; v_phase = omega0/k0 = 2/2 = 1. CORRECT.

3. **Group velocity**: v_group = domega/dk = k (for omega=k^2/2). At k0=2: v_group = 2.
   - Verified: d(k^2/2)/dk = k = 2 at k0=2. CORRECT.

4. **Ratio v_group/v_phase = 2**: From above, 2/1 = 2. This is exact for quadratic dispersion.
   - The ratio equals 2 for ANY k0, not just k0=2. Property of the dispersion relation.

5. **Wave packet shape**: psi(x,0) = cos(k0*x)*exp(-x^2/(2*sig^2))
   - Gaussian envelope with sigma=1.2, carrier frequency k0=2. Standard wave packet.
   - Envelope travels at v_group; carrier crests travel at v_phase.

6. **Crest slide**: For t>0, envelope peak at x = v_group*t = 2t; nearest crest of carrier
   at x satisfying k0*x - omega0*t = 0 => x = (omega0/k0)*t = v_phase*t = t.
   - Crests lag behind envelope: crest at t vs envelope at 2t. Verified.

VERDICT: All physics claims accurate.
