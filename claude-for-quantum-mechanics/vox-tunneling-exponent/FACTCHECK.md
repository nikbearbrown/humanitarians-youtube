# FACTCHECK — vox-tunneling-exponent

## Claims → Verdict + Source

| Claim | Verdict | Source |
|-------|---------|--------|
| Transmission T = e^(-2*kappa*L) through rectangular barrier | VERIFIED | M-13: "T approx e^(-2kL), kappa = sqrt(2m(V0-E))/hbar" |
| Kappa for 1 eV barrier above electron energy: ~5.1 nm^-1 | VERIFIED | M-13: "Useful numbers for electrons with V0-E=1 eV: kappa approx 5.1 nm^-1" |
| Every 2.3 units of 2*kappa*L reduces T by one order of magnitude | VERIFIED | M-13: "Rule of thumb: each 2.3 units of 2*kappa*L reduces T by one order of magnitude (e^(-2.303) = 10^(-1))" |
| At 2kL=20, T approx 2e-9 | VERIFIED | M-13 table: "2kL=20: T approx 2×10^-9, negligible" |
| STM current changes by factor e per angstrom | VERIFIED | M-13: "current changes by a factor of e per angstrom of tip height" |
| T = e^(-2kL) in the classically forbidden region (E < V) | VERIFIED | M-13: "T has the same e^(-lambda*t) structure as radioactive decay, but in the spatial variable x" |

## Illustrative Numbers / Examples
- B10 uses kappa=10.8 nm^-1 (barrier 4.5 eV above electron energy), gap 0.3 nm, then 0.2 nm. Narration explicitly labels "these are illustrative values." Derivation: kappa = sqrt(2*9.11e-31*4.5*1.6e-19)/(1.055e-34) ≈ 10.86 nm^-1. 2*kappa*0.3 = 6.52; T=e^(-6.52)≈0.00147. 2*kappa*0.2 = 4.34; T=e^(-4.34)≈0.013. Ratio ≈ 8.8x (~10x order-of-magnitude). Consistent with theme.

## Terms Table
| Term | Debut beat | Need created by |
|------|------------|-----------------|
| tunneling | B01 (hook) | implicit from STM hook |
| classically forbidden region | B03 | B02 question — "why can't classical explain" |
| wavefunction | B03 | B03 setup |
| kappa (decay rate) | B03–B04 | B03 establishes decaying exponential |
| transmission probability T | B05 | B03-B04 established decay |
| semi-log scale | B07 | B06 established log relationship |

## Exclusions Confirmed
- WKB derivation: absent
- Gamow factor: absent
- Tunneling setup derivation: absent
- Only rectangular barrier formula T=e^(-2kL) shown
