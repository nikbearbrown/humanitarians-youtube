# Frictional Log — 2026-11-12

**Learnings:** Putting canary and blue-green theory into practice on a real Cloud Run service — watching golden-signal metrics (error rate, p95 latency) as the validation signal during a traffic ramp, and keeping a prior revision warm as the rollback path.

**Implemented work:** Ran a tagged canary revision on `medas-frontend-stage`, ramped 5% → 25% → 100% while watching error rate and p95 latency; validated a tagged green revision for a riskier change in isolation at zero live traffic before an atomic cutover; kept the previous revision warm so rollback stays a one-line traffic flip.
