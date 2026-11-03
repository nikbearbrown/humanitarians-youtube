# PEDAGOGY.md — bernoulli (Chapter 14, 14.6 Bernoulli's Equation)

## Concept
In a level pipe that narrows, continuity (A_1 v_1 = A_2 v_2, incompressible)
forces the fluid to speed up in the neck. Speeding up requires a net forward
force on each fluid element, supplied by higher pressure behind than ahead,
so the pressure in the neck is lower. Bernoulli's principle packages this as
p + ½ρv² = constant along a streamline (level, frictionless, incompressible).

## Audit against the bar
- **Single tension:** intuition says faster fluid pushes harder; does pressure rise or fall?
- **Single resolution:** it falls — pressure and kinetic energy density trade off with a constant sum.
- **One visual object:** the pipe with its steady flow (tracer dots on streamlines), present throughout; gauges and bars are read-outs attached to it.
- **<=6 elements per scene:** pipe+flow, gauges, velocity arrows, energy bars, one equation, summary. Velocity arrows fade before bars arrive; only one equation on screen at a time.
- **Self-contained:** needs only work-energy and the idea of pressure.

## Physics check against 14.6 (and 14.5 for continuity)
- "When a fluid flows into a narrower channel, its speed increases" (14.6 opening, referring to 14.5's continuity equation). Tracer-dot speed in the drawing is v(x) = v_1 A_1/A(x) (2D cross-section, width stands for area); streamlines stay parallel and smooth (laminar, no eddies).
- Causal account follows the text: "A pressure difference occurs when the channel narrows. This pressure difference results in a net force on the fluid ... and this net force does work ... The net work done increases the fluid's kinetic energy."
- Bernoulli's principle stated with its conditions from the text: incompressible, frictionless, constant depth (h_1 = h_2), along a streamline: p_1 + ½ρv_1² = p_2 + ½ρv_2²; "pressure drops as speed increases in a moving fluid".
- ½ρv² is called "kinetic energy per unit volume" (the text's "kinetic energy density"), not a stored "pressure energy"; the storyboard's "Energy in the fluid has to stay constant / pressure energy" wording was replaced by the textbook's formulation.
- Downstream gauge reads the same as upstream: same width, level, frictionless flow -> same speed -> same pressure (consistent with the equation; no viscosity).
- Bar heights computed from the drawn geometry: v_2/v_1 = h_1/h_2, so the neck's ½ρv² bar is (v_2/v_1)² times the upstream one, with p reduced by the same amount; totals equal.
- Lift/airfoils deliberately not mentioned (storyboard exclusion "no full lift derivation"; avoids the equal-transit-time myth entirely). Hook states the intuition as an intuition, not as fact.

## Exclusions honored
No viscosity, no turbulence, no compressibility, no lift. Storyboard's black background and logo replaced by the locked white, unbranded medhavy style.

## Bug patterns checked
- Gauge stems follow the pipe wall during the narrowing (redrawn each frame); dials stay fixed.
- Tracer dots are a single updater group; streamline fractions keep them inside the walls at all times.
- Every mobject stored on self; velocity arrows and the continuity equation faded when superseded.
- Portrait: content above the caption band, inside safe width; equation at the top.

VERDICT: PASS
