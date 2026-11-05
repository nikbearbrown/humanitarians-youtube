# PEDAGOGY.md — hydraulics (Chapter 14, 14.3 Pascal's Principle and Hydraulics)

## Concept
A small force F_1 on a small piston A_1 raises the fluid pressure by
F_1/A_1. By Pascal's principle that *change* in pressure is transmitted
undiminished throughout the enclosed fluid, so the wide piston (same height)
receives the same increase and feels F_2 = (A_2/A_1) F_1. Work is not
multiplied: incompressibility forces A_1 d_1 = A_2 d_2, hence F_1 d_1 = F_2 d_2.

## Audit against the bar
- **Single tension:** how can a small push hold up a car many times heavier?
- **Single resolution:** the same pressure change acts over a larger area, giving a larger force — paid for with a longer stroke.
- **One visual object:** the U-shaped jack (vessel + fluid + two pistons + car), persistent from first to last frame; only its pistons move, car translates straight up.
- **<=6 elements per scene:** jack, F_1 arrow, F_2 arrow (or pressure arrows), area markers, displacement arrows, one equation block. Area markers fade before displacement arrows arrive; the equation panel shows at most two lines.
- **Self-contained:** needs only p = F/A and work = force x distance.

## Physics check against 14.3
- Pascal's principle wording follows the text verbatim: "a change in pressure applied to an enclosed fluid ... is transmitted undiminished to all portions of the fluid and to the walls of its container."
- Storyboard correction: the storyboard's on-screen line "same P everywhere in the fluid" contradicts 14.3, which explicitly says the principle does NOT make pressure equal everywhere (it varies with depth); it applies to the *change*. Rendered instead as "same Δp everywhere in the fluid" and the equation is written Δp = F_1/A_1.
- F_1/A_1 = F_2/A_2 requires pistons at the same height and negligible friction (14.3); narration says "at the same height" and the jack starts with both pistons level.
- Number example (100 N -> 500 N for a five-times area) is the textbook's own example. The drawing uses a 5:1 width ratio; in this 2D cross-section the width stands in for area, so displayed d_1 : d_2 = 5 : 1 is consistent with A_1 d_1 = A_2 d_2.
- "Can increase force but cannot do more work than is done on it" — 14.3, Significance of the brake example.
- Fluid incompressible: 14.3 describes the hydraulic jack's fluid as incompressible.

## Exclusions honored
No compressibility corrections, no line losses, no cavitation. No brakes example. Storyboard's black background and logo replaced by the locked white, unbranded medhavy style.

## Bug patterns checked
- F_1 arrow sits above the rod, not through the piston; F_2 arrow is inside the fluid under the piston face, not through the car.
- Labels follow moving pistons via updaters, cleared after motion.
- Every mobject stored on self; area markers and pressure arrows faded when superseded.
- Portrait: everything above the caption band and inside safe_half_w/h; labels placed in the gap between cylinders.

VERDICT: PASS
