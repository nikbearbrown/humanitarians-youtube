# Revision: check the split first,
# then judge bots on clicks from
# BEFORE the test.
# SIMULATION of Fabijan et al. 5.3.
from random import random, randint
from random import seed
from abtest import z_test, fmt_p
from abtest import srm_check

seed(2019)
N = 200_000  # users per arm
BOT = 80     # clicks: above = bot


def user(arm):
    if random() < 0.015:  # fan
        pre, up = 60, 40
    else:
        pre = randint(0, 6)
        up = random() < 0.2
    return pre, pre + arm * up


ctrl = [user(0) for _ in range(N)]
test = [user(1) for _ in range(N)]


def kept(users, col):
    # col 1 = clicks during test
    # col 0 = clicks before test
    return [u[1] for u in users
            if u[col] <= BOT]


nc = len(kept(ctrl, 1))
nt = len(kept(test, 1))
chi2, p = srm_check(nc, nt)
print(f"split {nc} vs {nt}")
print(f"SRM p {fmt_p(p)}")

mc, mt, z, p = z_test(
    kept(ctrl, 0), kept(test, 0))
print(f"control {mc:.2f}")
print(f"test    {mt:.2f}")
print(f"z {z:.1f}   p {fmt_p(p)}")
