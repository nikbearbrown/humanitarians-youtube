"""What 'calibrated' means, as a constructed illustration — NOT a Jev measurement.

A forecaster is calibrated when, among all the answers it gives probability p,
the fraction that turn out true is about p:  Pr(true | p_hat = p) = p.
TypeSafe says Jev's probabilities are "optimized against outcomes" and that
"Calibration is measured across groups of predictions; it does not guarantee
that an individual answer is correct" (sources/typesafe-docs-system-one.html).

This script simulates a perfectly calibrated source that says 0.8 every time,
so the only thing it demonstrates is the definition and its group-level nature.
"""
import random

P, SEED = 0.8, 20260925
rng = random.Random(SEED)
for n in (10, 100, 10_000):
    right = sum(rng.random() < P for _ in range(n))
    print(f"n={n:>6}  said {P} each time  ->  {right:>5} true, {n - right:>5} false  ({right / n:.3f})")
print("\nexpected at n=100: 100 x 0.8 = 80 true, 20 false  (seed %d)" % SEED)
print("any single answer at 0.8 is still false 1 time in 5 on average")
