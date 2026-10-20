# SIMULATION of the mechanism in
# Fabijan et al., KDD 2019, 5.3.
# Not MSN's data.
from random import random, randint
from random import seed
from abtest import z_test, fmt_p

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


def keep(users):
    # drop "bots": too many clicks
    return [c for _, c in users
            if c <= BOT]


mc, mt, z, p = z_test(
    keep(ctrl), keep(test))
print(f"control {mc:.2f}")
print(f"test    {mt:.2f}")
print(f"z {z:.1f}   p {fmt_p(p)}")
