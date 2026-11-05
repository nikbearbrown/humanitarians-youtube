# PEDAGOGY.md — gyroscope-precession (Chapter 11.4, Precession of a Gyroscope)

## Concept
Gravity's torque about the pivot of a tilted top, tau = r x Mg, is
horizontal and perpendicular to L. Since dL = tau dt, it changes the
direction of L but not its magnitude or tilt, so a spinning top precesses
about the vertical instead of falling. A non-spinning top has no L to turn,
acquires angular momentum along tau, and falls.

## Physics check (against 11-angular-momentum/4-precession-of-a-gyroscope.mdx)
- "If the top is placed on a flat surface ... at an angle to the vertical and is not spinning, it will fall over ... if the top is spinning on its axis, rather than topple over ... it precesses about the vertical" (Fig. 11.21) -> B00 shows both cases.
- "The torque produced is perpendicular to the angular momentum vector. This changes the direction of ... L according to dL = tau dt, but not its magnitude. The top precesses around a vertical axis, since the torque is always horizontal and perpendicular to L." -> B01-B03.
- Directions in the script (z up, pivot at origin, axis unit a = (sin th cos phi, sin th sin phi, cos th), th = 25 deg): tau = r x (-Mg z) = d M g sin th (-sin phi, cos phi, 0), horizontal, along increasing phi. Spin angular velocity is along +a (stripes turn counterclockwise seen from the spindle end), so L is along +a and dL/dt = tau makes phi increase: precession counterclockwise seen from above. Torque arrow, L arrow and precession sense are all computed from these formulas each frame.
- "the precession angular velocity is much less than the angular velocity of the gyroscope disk" -> spin rate drawn about 8x the precession rate.

## Audit against the bar
- **Single tension:** a tilted top should fall under gravity, yet a spinning one circles.
- **Single resolution:** the torque is perpendicular to L, so it turns L (precession) instead of tipping it.
- **One primary visual object:** the top (B02's diagram isolates its own L vector only).
- **<=6 elements per scene:** floor, top, Mg, L, tau, cone/label (B02: L, fall ghost + X, tau dt, right-angle mark, faint copies).
- **Self-contained:** uses tau = r x F and tau = dL/dt only.

## Exclusions honored
No Euler angles, no nutation, no precession-rate formula.

## Style deviations from storyboard
Storyboard colors (red gravity, blue L, orange torque on dark) are mapped to
the locked medhavy palette: gravity CRIMSON, L TEAL, torque GOLD with an ink
outline (gold alone is too faint on white). The top is drawn as a wooden toy
(tan body, slate stripes) in a fixed oblique 3D projection computed in the
script, since MedhavyScene is a 2D Scene.

## VERDICT: PASS
