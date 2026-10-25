# PEDAGOGY.md — rolling-wheel (Chapter 11.1, Rolling Motion)

## Concept
Rolling without slipping is the superposition of a translation (every point
moves with v_CM) and a rotation about the center (rim points move tangent to
the circle with speed R omega). The no-slip condition is v_CM = R omega
(textbook Eq. 11.1, derived from v_P = -R omega i + v_CM i = 0 at the contact
point P). Hence the top of the wheel moves at 2 v_CM and the contact point is
instantaneously at rest.

## Physics check (against 11-angular-momentum/1-rolling-motion.mdx)
- Wheel rolls to the right, so it rotates clockwise (omega into the page).
  Rotational velocity of a rim point at angle phi (from +x, about the center):
  omega x r = R omega (sin phi, -cos phi). Top (phi = 90 deg): +x. Front
  (phi = 0): -y (down). Bottom (phi = -90 deg): -x. Matches storyboard and the
  textbook's "-R omega i at P".
- Resultant = v (1 + sin phi, -cos phi) with R omega = v: |top| = 2v,
  front = v(1, -1) (diagonal down, magnitude sqrt(2) v), bottom = 0. All arrows
  are computed from this formula in the script, not eyeballed.
- Textbook Fig. 11.2: "the bottom of the wheel is instantaneously at rest" —
  narration's "for an instant, perfectly still" matches.

## Audit against the bar
- **Single tension:** every point of a rolling wheel seems to move, yet the cycloid has a cusp at the ground — how fast is the contact point moving?
- **Single resolution:** translation plus rotation, with R omega = v, cancel exactly at the contact point.
- **One primary visual object:** the wheel (two copies only in B01's side-by-side decomposition, which is the same object shown twice).
- **<=6 elements per scene:** B00 ground, wheel, dot, trail; B01 two wheels, two arrow sets, two labels; B02 wheel, ground, header, top/front/bottom constructions (resultants replace components); B03 wheel, ground, arrow field, ring; B04 dimmed wheel, top arrow + label, ring + label.
- **Self-contained:** assumes vector addition and the idea of angular speed only.

## Exclusions honored
No angular acceleration, no torque, no rolling energy, no numbers or units.

## Style deviations from storyboard (forced by the locked style)
Storyboard specified a dark background with yellow/cyan/white vectors. The
locked medhavy style is a white background, so: translation = TEAL,
rotation = CRIMSON, resultant = INK (black). The tracked rim point is GOLD
with an ink outline (yellow alone is too faint on white); its trail is dotted
SLATE. Color coding is kept fixed across all beats. In the portrait short
the B03 sweep keeps the wheel centered and scrolls ground tick marks
backwards (camera tracking the wheel), because a 4.5-unit-wide frame cannot
hold a full revolution at readable size; the arrows drawn are still
velocities relative to the ground.

## VERDICT: PASS
