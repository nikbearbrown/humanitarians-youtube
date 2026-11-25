"""Boiling point of water at the summit of Mount Everest, from the Antoine equation.

    python3 boiling.py

Antoine constants for water, 1-100 °C (P in mmHg, T in °C): A 8.07131, B 1730.63, C 233.426.
Summit pressure: about 33.7 kPa (West et al., 1983, measured 253 mmHg on the summit).
"""
import math

A, B, C = 8.07131, 1730.63, 233.426
for label, mmhg in [('sea level, 760 mmHg', 760.0), ('Everest summit, 253 mmHg', 253.0)]:
    t = B / (A - math.log10(mmhg)) - C
    print(f'{label}: water boils at {t:.1f} °C')
