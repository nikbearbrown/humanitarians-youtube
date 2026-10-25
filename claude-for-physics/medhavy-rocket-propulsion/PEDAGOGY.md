# PEDAGOGY.md — rocket-propulsion (Chapter 9, Rocket Propulsion)

## Concept
A rocket needs nothing to push against: rocket + fuel is one system with
zero total momentum; ejecting exhaust backward at speed u (relative to the
rocket) gives the rocket forward momentum, m Δv = Δm u. With a steady burn
the remaining mass decreases, so each bit of exhaust produces a larger Δv —
the acceleration grows.

## Physics check (against the textbook, 9.7)
- Textbook derivation: m dv = dm_g u (after dropping dm_g dv). The on-screen
  equation m Δv = Δm u and B02's narration ("mass times change in velocity
  equals ejected mass times exhaust speed") are this result for one small
  puff. u is measured relative to the rocket, as the narration says.
- B01: no external force → system momentum conserved (zero for a system at
  rest), as in the textbook's isolated-system treatment.
- B03: a = (dm_g/dt) u / m. Constant burn rate and u → acceleration rises as m
  falls. "The acceleration grows as the fuel runs out" — correct.
- Animation kinematics are exact for a constant burn: m(t) = m₀(1 − kt) from
  m₀ to 0.4 m₀; v(t) = v₀ + u ln(m₀/m); position = ∫v dt in closed form.
  Each exhaust dot keeps its ground velocity v(t_e) − u; the camera rides
  with the rocket during the burn (stars scroll at a fixed parallax factor),
  so the rocket's growing speed shows as accelerating star motion and a
  lengthening v arrow. The fuel gauge drains in proportion to remaining fuel.
- The B02 single puff is slowed (same u : Δv ratio) so it stays in frame;
  the Δv arrow is drawn 3× its true ratio for legibility (noted in code).
- The storyboard's "Newton's third law demands it" phrasing was replaced by
  momentum conservation (the textbook's argument); B04 states the
  action–reaction pair (rocket pushes exhaust, exhaust pushes rocket)
  correctly. No Tsiolkovsky derivation, gravity turn, or staging (exclusions).
- The storyboard's shrinking rocket was replaced by a draining fuel gauge
  and a mass label m → 0.4 m₀: a rocket's size does not shrink, its mass does.

## Audit against the bar
- **Single tension:** nothing to push against in empty space, yet the rocket accelerates.
- **Single resolution:** total momentum stays zero; the rocket pushes on its own exhaust.
- **One primary visual object:** the rocket (with fuel gauge) and its exhaust.
- **≤6 elements per scene:** B03: stars, rocket, exhaust stream, v arrow + label, mass label, equation (6).
- **Self-contained:** momentum conservation only.

## Style compliance
- Medhavy palette on white (storyboard's black void superseded): light hull with CRIMSON nose and fins, GOLD fuel, CRIMSON exhaust, TEAL velocity, sparse SLATE stars.
- ReplacementTransform used only for the equation morph p_before = p_after → m Δv = Δm u.
- Unbranded, formal, am_michael 0.85. Portrait: B00Q card + captions; landscape: none.
- Bug patterns checked: no animation on a sub-group of the rocket (that left a stale rocket copy in preview — fixed); all beat mobjects removed when replaced; nothing in the caption band.

## VERDICT: PASS
