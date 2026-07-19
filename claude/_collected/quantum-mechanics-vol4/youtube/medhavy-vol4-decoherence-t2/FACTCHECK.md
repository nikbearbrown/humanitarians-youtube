# FACTCHECK — medhavy-vol4-decoherence-t2

## Formula: rho_01(t) = rho_01(0) * e^(-t/T2)
  Source: Breuer & Petruccione "The Theory of Open Quantum Systems" (2002) §3.3;
          Nielsen & Chuang "Quantum Computation and Quantum Information" §8.3
  Physical meaning: off-diagonal density matrix element (coherence) decays
  exponentially with dephasing time T2.

## Numbers:
  - T2 = 1 microsecond = 1e-6 s (typical NMR/superconducting qubit value)
  - At t=0: |rho_01| = 1 (maximum coherence)
  - At t=T2=1 us: |rho_01| = e^(-1) = 0.3679 ✓
  - At t=2*T2=2 us: |rho_01| = e^(-2) = 0.1353
  - At t=3*T2=3 us: |rho_01| = e^(-3) = 0.0498 approx 0.05

## Two testable predictions:
  P1: |rho_01(T2)| / |rho_01(0)| = 1/e = 0.3679 exactly ✓
  P2: Doubling gamma_dephasing halves T2: T2 = 1/gamma_dephasing
      If gamma doubles, T2 halves => at same t the decay is twice as fast ✓

VERDICT: PASS
