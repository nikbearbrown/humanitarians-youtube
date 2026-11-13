# PEDAGOGY.md — centripetal-friction (Chapter 6, Centripetal Force)

## Concept
A car rounding a curve at constant speed needs an inward (centripetal) net
force even though its speed never changes. That force is supplied by static
friction between the tires and the road, acting perpendicular to the
velocity, toward the center of the arc. Remove it and the car obeys Newton's
first law: it goes straight, tangent to the curve.

## Audit against selection.md bar
- **Single tension:** "what invisible force turns the car if velocity always points forward?"
- **Single resolution:** static friction, acting sideways/inward, is the centripetal force.
- **One visual object:** the car, tracked continuously with its velocity and friction arrows.
- **≤6 elements per scene:** car, road/arc, velocity arrow, friction arrow, trace line, one label — never more than 6 at once.
- **Self-contained:** assumes only vectors and Newton's first law; no circular-motion kinematics (a = v²/r) is derived on screen, matching storyboard scope.

## Exclusions honored
No banked-turn derivation, no conical pendulum, no centrifugal-force
misconception discussion. (Per storyboard.)

## Style compliance
- Palette: medhavy (Okabe-Ito) — white ground, ink text, rotating accent per beat (SLATE -> SLATE -> CRIMSON -> TEAL -> GOLD -> CRIMSON -> GOLD).
- No intro/brand card (landscape) — B00 is the hook.
- No outro card, no "thanks for watching" — B06 is a plain held final frame.
- Register: formal, undergrad/grad audience.
- Voice: am_michael (Kokoro), 0.85x speed.
- Short-form (9:16) adds title card + burned-in Open Sans captions, same infrastructure as prior videos.
- Bug patterns checked: friction arrow offset from tire silhouette, velocity/friction arrows kept >=0.9x-scale apart, arc-trace stored on self.trace so B05 can toggle it, next_to() always anchored to a mobject not a bare coordinate.

## VERDICT: PASS
