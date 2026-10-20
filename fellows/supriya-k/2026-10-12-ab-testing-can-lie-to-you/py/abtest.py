# Stats helpers. Stdlib only.
from math import erfc, sqrt


def z_test(a, b):
    # two-sample z-test on means
    ma = sum(a) / len(a)
    mb = sum(b) / len(b)
    va = sum((x - ma) ** 2
             for x in a) / len(a)
    vb = sum((x - mb) ** 2
             for x in b) / len(b)
    se = sqrt(va / len(a)
              + vb / len(b))
    z = (mb - ma) / se
    return ma, mb, z, erfc(
        abs(z) / sqrt(2))


def srm_check(n_a, n_b):
    # chi-square vs a 50/50 split
    e = (n_a + n_b) / 2
    chi2 = ((n_a - e) ** 2
            + (n_b - e) ** 2) / e
    return chi2, erfc(
        sqrt(chi2 / 2))


def fmt_p(p):
    # tiny p underflows to 0.0
    return (f"{p:.0e}" if p > 1e-9
            else "< 1e-9")
