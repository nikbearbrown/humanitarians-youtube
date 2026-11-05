# PEDAGOGY.md — orbit-energy-paradox (Chapter 13.4, Satellite Orbits and Energy)

## Concept
For a circular orbit, K = GMm/2r, U = -GMm/r, E = K + U = -GMm/2r = -K.
Adding energy (a forward burn) makes E less negative, which means a larger r
and a smaller K: the satellite ends higher and slower. Removing energy (a
backward burn) shrinks the orbit and raises K: lower and faster.

## Physics check (against 13-gravitation/4-satellite-orbits-and-energy.mdx)
- Textbook: "K = (1/2) m v^2 = G m M_E / 2r" and "E = K + U = G m M_E/2r - G m M_E/r = -G m M_E/2r ... the total energy is negative, with the same magnitude as the kinetic energy." -> B01 verbatim in substance.
- v = sqrt(GM/r): speed arrows are drawn with length proportional to r^(-1/2); energy bars with K proportional to 1/r, U = -2K, E = -K, all from one radius tracker.
- **Storyboard correction (physics error in the storyboard):** Scene 1 of the storyboard says a prograde burn puts the satellite in a *lower*, faster orbit. That is wrong: a prograde burn adds energy and raises the orbit (as the storyboard's own Scene 3 states). The hook is rewritten so the paradox is stated correctly: forward burn -> higher circular orbit -> slower. Scene 4's retrograde-burn -> lower, faster orbit is kept.
- Simplification flagged honestly: a single burn produces an elliptical orbit; the narration compares the circular orbit the satellite "settles into" (no Hohmann math, per exclusions). The circle radius change is animated as a continuous transform of the orbit.

## Audit against the bar
- **Single tension:** speeding up with a forward burn leaves the satellite slower.
- **Single resolution:** E = -K for circular orbits, so more energy means larger r and less kinetic energy.
- **One primary visual object:** the satellite's orbit around Earth.
- **<=6 elements per scene:** Earth, orbit, satellite + v arrow, thrust arrow, equation slot, energy bars.
- **Self-contained:** only K = mv^2/2, U = -GMm/r and the circular-orbit result are used.

## Exclusions honored
No Hohmann transfer math, no escape velocity, no Kepler's-law proofs. No logo
or bumpers inside the content (unbranded style; the studio intro/outro are
added only to the short by the pipeline).

## Style deviations from storyboard
Black background -> locked white medhavy ground. Velocity arrow INK, thrust
arrow CRIMSON, K bar TEAL, U bar CRIMSON, E bar INK/SLATE. Earth drawn in
Okabe-Ito sky blue with teal land, satellite with a gold body and slate solar
panels.

## VERDICT: PASS
