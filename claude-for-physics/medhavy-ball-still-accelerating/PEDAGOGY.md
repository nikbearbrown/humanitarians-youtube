# PEDAGOGY.md — ball-still-accelerating (Chapter 3, Average and Instantaneous Acceleration)

## Concept
A ball thrown straight up has zero velocity at the top of its path, yet its
acceleration there is the same 9.8 m/s² downward as everywhere else in the
flight. Acceleration is the rate of change of velocity, not velocity itself;
at the peak the velocity is changing from upward, through zero, to downward.

## Physics check (against the textbook)
- 3.3: acceleration is the rate of change of velocity, a = dv/dt; it occurs
  whenever velocity changes in magnitude or direction. Narration B02 says
  "acceleration ... measures how quickly velocity changes" — matches.
- 3.5 (free fall), Example 3.14(d): "The acceleration is 9.8 m/s² everywhere,
  even when the velocity is zero at the top of the path. Although the velocity
  is zero at the top, it is changing at the rate of 9.8 m/s² downward."
  B02/B03/B04 state exactly this. Air resistance is explicitly set aside, as
  the textbook does for free fall.
- "Changes the velocity by 9.8 m/s downward every second" is the textbook's own
  reading of the unit m/s² (3.3: "by how many meters per second the velocity
  changes every second").
- Animation is physically correct: the ball's height follows a parabola in
  time (y = y_top - ½ g' (t - t_top)², scaled), the velocity arrow length is
  linear in time and passes through exactly zero at the peak, and the
  acceleration arrow never changes length or direction.

## Audit against the bar
- **Single tension:** zero velocity at the top seems to imply nothing is happening, so zero acceleration.
- **Single resolution:** acceleration is the rate of change of velocity, and that rate is constant (g downward) the whole time, including at the peak.
- **One primary visual object:** the red ball with its two arrows (teal v, black a).
- **≤6 elements per scene:** B00–B02: track, ball, v arrow + label, a arrow + label, one stamp (≤6). B03: three snapshot rows + column headers + gold box (6). B04: ball, v dot, a arrow + label, statement (5).
- **Self-contained:** needs only the idea of velocity as a vector; no calculus, no kinematic equations, no sign convention system (storyboard exclusions honored).

## Style compliance
- Medhavy palette: white ground, ball CRIMSON (red), velocity TEAL, acceleration INK (black, per storyboard), gold comparison box. Accent rotation TEAL → CRIMSON → INK → GOLD → CRIMSON.
- Unbranded (storyboard's logo/intro requests are superseded by the current pipeline). Formal register, am_michael at 0.85.
- Portrait: B00Q question card + captions; landscape: none.
- Bug patterns checked: arrows offset to either side of the ball (never through it), labels attached with next_to(mobject), every mobject stored on self and faded/transformed away, nothing in the portrait caption band.

## VERDICT: PASS
