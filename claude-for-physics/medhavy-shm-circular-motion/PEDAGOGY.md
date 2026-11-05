# PEDAGOGY.md — shm-circular-motion (Chapter 15, 15.3 Comparing SHM and Circular Motion)

## Concept
A peg on a wheel of radius A turning at constant angular frequency ω, lit
from above, casts a shadow on a horizontal axis. The shadow's position is
x(t) = A cos(ωt): it oscillates between +A and -A exactly like a block on a
spring whose frequency satisfies ω = 2πf. SHM is the one-axis projection of
uniform circular motion.

## Audit against the bar
- **Single tension:** a line oscillator and a circular rotor look unrelated, yet "do the same thing".
- **Single resolution:** the oscillator is the shadow (projection) of the rotor.
- **One visual object:** the peg's shadow — first on the axis, then riding on the block, then drawn out as the trace; wheel and block are its two views.
- **<=6 elements per scene:** wheel+peg, projection line+shadow, block-spring, angle marker, trace, one equation/label block.
- **Self-contained:** needs only cos as the horizontal coordinate of a point on a circle.

## Physics check against 15.3
- Setup is the text's: "A peg ... attached to a vertical disk, rotating with a constant angular frequency ... If a lamp is placed above the disk and peg, the peg produces a shadow. Let the disk have a radius of r = A ... the shadow oscillates between x = +A and x = -A."
- Equation 15.14 x(t) = A cos(ωt); the wheel starts at θ = 0 with the shadow at x = +A, as in Figure 15.18(a), and turns counterclockwise.
- "The disk must turn at a constant angular frequency equal to 2π times the frequency of oscillation (ω = 2πf)" — used verbatim in B02.
- "Slowing at the ends, fastest through the center" follows from Eq. 15.15, v = -v_max sin(ωt) (not stated as an equation on screen).
- The block is drawn with x_block(t) = A cos(ωt) from the same clock as the wheel (one shared time value), so the sync is exact, not hand-timed. Constant ω throughout, no easing.
- Trace: position vs. time with time running downward (chart recorder), so the cosine shares the block's horizontal axis directly.

## Exclusions honored
No complex exponentials, no phase space, no damping. Storyboard's white-on-black colors replaced by the locked medhavy palette (peg/shadow gold with ink outline, block crimson, trace ink).

## Bug patterns checked
- Projection line redrawn every frame from the peg's current angle.
- Turning-point pulses are computed from cos(ωt) (|cos| near 1), so shadow and block pulse at the same frames.
- Every mobject stored on self; nothing fades in over the caption band in portrait; equation sits above the wheel in portrait, in the right panel in landscape.

VERDICT: PASS
