# PEDAGOGY.md — steel-ship-buoyancy (Chapter 14, 14.4 Archimedes' Principle and Buoyancy)

## Concept
Buoyant force equals the weight of the fluid displaced (F_B = w_fl). A solid
steel block displaces only its own volume, whose water weighs ~1/8 of the
steel, so it sinks. The same steel shaped into a hollow hull encloses a much
larger volume; it settles until the displaced water weighs as much as the
ship, then floats. Equivalently its average density is below water's.

## Audit against the bar
- **Single tension:** steel sinks, yet a steel ship floats.
- **Single resolution:** shape sets the displaced volume, and displaced water weight is the buoyant force.
- **One visual object:** the one piece of steel (block, then the same steel morphed into a hull). The B01 ship is that hull, shown first to pose the contradiction.
- **<=6 elements per scene:** pool, steel object, displaced-volume ghost, W arrow, F_B arrow, equation block. The B01 ship fades before the block analysis begins; the block is consumed by the transform; in B05 the block returns only as the comparison partner while equations are cleared.
- **Self-contained:** needs only weight and density.

## Physics check against 14.4 (and table 14.1)
- Archimedes' principle stated verbatim: "The buoyant force on an object equals the weight of the fluid it displaces."
- Clay/steel-ship argument is the text's own: "Because of its shape, the clay boat displaces more water than the lump and experiences a greater buoyant force, even though its mass is the same. The same is true of steel ships."
- "Average density ... less than that of the surrounding fluid, it will float" — 14.4.
- "Nearly eight times as dense": table 14.1 lists iron at 7.86 x 10^3 kg/m^3 and water at 1.000 x 10^3; steel is essentially iron. Hence w_fl ≈ W/8 for the submerged block (shown as an approximation, ≈).
- Storyboard correction: the storyboard draws the floating ship's buoyant arrow *longer* than the weight. For a ship floating at rest the forces balance exactly, so the arrows are drawn equal in length, and the hull's W arrow is the same length as the block's W (same steel, same weight).
- Drawing is quantitatively consistent in 2D cross-section: hull wall area equals the block's area; the hull sits with submerged area = 7.86 x steel area (about 72% of its height).
- The block's force diagram is shown while it is fully submerged in mid-water (no floor normal force involved), then it sinks back to the floor.

## Exclusions honored
No stability/metacenter, no seawater vs freshwater, no submarines. Storyboard's doodle wobble and logo replaced by the locked clean, unbranded medhavy style.

## Bug patterns checked
- W and F_B arrows offset beside the block / placed inside the hull and under its floor, never through the steel.
- Hull interior is masked white so water does not appear inside the hull; ghost volume is teal dashed, distinct from water.
- Labels follow moving objects via updaters, cleared after motion; every mobject stored on self and faded when superseded.

VERDICT: PASS
