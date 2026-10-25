# PEDAGOGY.md — pe-diagram-forbidden-zones (Chapter 8, Potential Energy Diagrams and Stability)

## Concept
On a potential energy diagram, the constant total energy E is a horizontal
line. Because K = E − U(x) can never be negative, every position where
U(x) > E is forbidden; the crossings U = E are turning points, and the
particle oscillates between them.

## Physics check (against the textbook, 8.4)
- "Since kinetic energy can never be negative, there is a maximum potential
  energy ... which an object with the given total energy cannot exceed" and
  the allowed range follows from 0 ≤ K ≤ E. B03 states exactly this.
- "K = 0 and U = E at a turning point"; "motion is confined to the region
  between the turning points" (Fig. 8.11). B04 matches.
- B01: for a particle on a frictionless track under gravity, U = m g y, so
  U(x) has the track's shape ("its weight times its height"). Correct.
- B02: no friction → mechanical energy conserved, E constant. Correct.
- B03: K = ½ m v² ≥ 0, so K < 0 is impossible. Correct.
- Animation: U(x) = 0.35 x² (a parabolic well), E = 2.2; turning points at
  x = ±√(E/0.35). The particle's motion on the graph is x(t) = x_t sin ωt,
  the exact motion in a quadratic potential, so it decelerates to rest
  exactly at the turning points and never enters the shaded zones. The
  moving teal bar is E − U(x) = K at the particle's position, shrinking to
  zero at the turning points.
- Storyboard asked for a 0.2–0.3 s pause at each turning point; not added,
  because a real particle is at rest there only instantaneously (the SHM
  motion already lingers visibly near the turning points).

## Audit against the bar
- **Single tension:** nothing on the track stops the particle, yet it never passes certain points.
- **Single resolution:** K = E − U(x) ≥ 0 forbids U(x) > E; the crossings are turning points.
- **One primary visual object:** the U(x) curve (the track, transformed) with the particle on it.
- **≤6 elements per scene:** B03 peak: graph (axes + curve), E line, crossing dots, equation card, K bars, shaded zones = 6. B04: graph, E line, dots, zones, particle + K bar, turning-point labels = 6.
- **Self-contained:** only K, U, E and conservation of energy; storyboard exclusions honored (no stability analysis, no force from slope).
- The equation card stays for the whole REVEAL beat (~20 s) rather than the storyboard's 6–7 s because the beat's narration is the card's content; it clears at the start of B04.

## Style compliance
- Medhavy palette on white (storyboard's black background superseded): curve INK, E line TEAL, forbidden zones CRIMSON at 22% opacity behind the curve, particle GOLD with an ink outline (kept the same from B00 to B05).
- Unbranded, formal, am_michael 0.85. Portrait: B00Q card + captions; landscape: none.
- Bug patterns checked: labels anchored with next_to(mobject); card placed above the graph (never over the curve); zone shading behind the curve via z-index; nothing below the summary label in portrait's caption band.

## VERDICT: PASS
