"""Two ways to get a projectile's range: a closed-form answer vs stepping time forward."""
import math
v0, angle, g = 20.0, 45.0, 9.8           # m/s, degrees, m/s^2
a = math.radians(angle)
closed_range = v0**2 * math.sin(2 * a) / g
peak = (v0 * math.sin(a))**2 / (2 * g)
for dt in (0.1, 0.01):
    x, y = 0.0, 0.0
    vx, vy = v0 * math.cos(a), v0 * math.sin(a)
    while True:
        x, y, vy = x + vx*dt, y + vy*dt, vy - g*dt
        if y < 0: break
    print(f"stepped dt={dt}: range {x:.2f} m")
print(f"closed form:    range {closed_range:.2f} m, peak {peak:.2f} m")
