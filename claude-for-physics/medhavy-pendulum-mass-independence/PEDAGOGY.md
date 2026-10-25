# PEDAGOGY.md — pendulum-mass-independence (Chapter 15, 15.4 Pendulums)

## Concept
For a simple pendulum the restoring force along the arc is -mg sinθ and the
inertia resisting acceleration is m, so ma = -mg sinθ and m cancels:
a = -g sinθ. For small angles (sinθ ≈ θ) the motion is SHM with
ω = √(g/L), T = 2π√(L/g) — independent of mass.

## Audit against the bar
- **Single tension:** gravity pulls ten times harder on the heavy bob, yet both keep the same rhythm.
- **Single resolution:** mass multiplies both the restoring force and the inertia, and cancels.
- **One visual object:** the pair of equal-length pendulums swinging in lockstep, on screen from first to last frame (the lockstep is the evidence).
- **<=6 elements per scene:** beam+pendulums, mass labels, weight arrows (B01 only), one equation stack (at most three lines), period box, summary.
- **Self-contained:** needs Newton's second law and the sine component of weight.

## Physics check against 15.4
- Simple pendulum = point-mass bob on a massless string of length L (15.4 definition); bobs drawn small relative to L.
- Restoring force: "net force of -mg sinθ toward the equilibrium position — that is, a restoring force" (Fig. 15.20 caption).
- The text cancels m via the torque form, mL² d²θ/dt² = -L mg sinθ; the video uses the equivalent tangential form ma = -mg sinθ (a = L d²θ/dt²) — same cancellation, same result d²θ/dt² = -(g/L) sinθ.
- Small-angle condition: "for small angles (less than 15 degrees ...) sinθ and θ differ by less than 1%". Pendulums are animated at 12° amplitude, below 15°.
- T = 2π√(L/g), Eq. 15.19; "The period is completely independent of other factors, such as mass".
- Both bobs are driven by the same θ(t) = θ_0 cos(ωt) with ω = √(g/L) at a common scale, so lockstep is exact.
- Weight arrows drawn in a true 10 : 1 length ratio.

## Exclusions honored
No physical pendulum, no large-angle corrections, no anharmonic behaviour. Storyboard's doodle/marker lettering and logo replaced by the locked clean medhavy style with properly typeset math.

## Bug patterns checked
- Weight arrows start at the bob's bottom edge (never through the bob) and follow the bobs via always_redraw.
- Mass labels are fixed above the pivots so they never collide with moving bobs.
- Cross-out strokes are placed on the exact m glyphs (indexed MathTex parts).
- Every mobject stored on self; arrows and the naive-question text faded before the equations.

VERDICT: PASS
