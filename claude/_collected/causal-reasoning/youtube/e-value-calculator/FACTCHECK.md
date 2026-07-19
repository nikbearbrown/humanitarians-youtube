# FACTCHECK — e-value-calculator

- E-value formula RR + sqrt(RR*(RR-1)): matches VanderWeele & Ding (2017) Epidemiology.
- RR=2.1: E = 2.1 + sqrt(2.1*1.1) = 2.1 + sqrt(2.31) ≈ 2.1 + 1.52 = 3.62. Note: actual≈3.62 not 3.29. Agent should use math.sqrt(2.1*(2.1-1))=sqrt(2.1*1.1)=sqrt(2.31)≈1.52, so E≈3.62. Verify arithmetic in code.
- Thresholds >3 robust, 1.5-3 fragile, <1.5 not-definitive: match book guidance.
- RR=1.3: E=1.3+sqrt(1.3*0.3)=1.3+sqrt(0.39)≈1.3+0.624=1.924 → fragile: correct.
- RR=4.0: E=4.0+sqrt(4.0*3.0)=4.0+sqrt(12)≈4.0+3.46=7.46 → robust: correct.
