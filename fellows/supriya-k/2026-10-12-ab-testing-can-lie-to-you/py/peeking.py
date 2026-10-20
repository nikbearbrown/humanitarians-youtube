# B08: 1,000 A/A tests (no real
# difference), 20 daily looks each.
from math import erfc, sqrt
from random import binomialvariate
from random import seed

seed(2015)
TESTS, DAYS = 1000, 20
PER_DAY, RATE = 500, 0.10


def p_value(xa, xb, n):
    pool = (xa + xb) / (2 * n)
    se = sqrt(2 * pool
              * (1 - pool) / n)
    z = (xb - xa) / n / se
    return erfc(abs(z) / sqrt(2))


def sig(xa, xb, n):
    return p_value(xa, xb, n) < .05


peek = once = 0
curve = [0] * DAYS
for _ in range(TESTS):
    xa = xb = n = 0
    won = False
    for d in range(DAYS):
        xa += binomialvariate(
            PER_DAY, RATE)
        xb += binomialvariate(
            PER_DAY, RATE)
        n += PER_DAY
        if sig(xa, xb, n):
            won = True  # ship it
        curve[d] += won
    peek += won
    once += sig(xa, xb, n)

pct = 100 / TESTS
print(f"peeking {peek*pct:.1f}%")
print(f"once    {once*pct:.1f}%")
print("by day", *curve)
