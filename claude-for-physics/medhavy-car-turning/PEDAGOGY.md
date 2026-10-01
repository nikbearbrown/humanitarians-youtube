# PEDAGOGY.md — car-turning (Chapter 4, Acceleration Vector)

## Concept
A car rounding a curve at constant speed feels like it isn't accelerating
because the speedometer never moves. The tension: acceleration is the rate
of change of the velocity *vector*, not the speed. Since direction is
changing even though magnitude is not, the car is accelerating — and that
acceleration points toward the inside of the curve (centripetal).

## Audit against selection.md bar
- **Single tension:** "speedometer never moves — so am I accelerating?" — one sentence, no visual needed.
- **Single resolution:** velocity is a vector; same length + different direction = nonzero delta-v = nonzero acceleration, pointing inward.
- **One visual object:** the car on the curved road — every beat orbits this one image plus its velocity/acceleration arrows.
- **≤6 elements per scene:** confirmed per beat (B01: car + live v arrow + 3 faded snapshots = 5; B02: 2 vectors + delta-v arrow + equation = 4; B03: car + v + a = 3).
- **Self-contained:** understandable without the chapter — velocity-as-vector and Newton's second law are assumed-known prerequisites only.

## Exclusions honored
No centripetal force formula derivation, no non-uniform circular motion, no
banked curves. (Per storyboard.)

## Style compliance
- Palette: medhavy (Okabe-Ito) — white ground (professor override of stock
  cream), ink text/road, one rotating accent per beat (SLATE → CRIMSON →
  CRIMSON → SLATE → GOLD), car colored teal, never more than the beat's
  accent + the persistent v/a arrow colors live at once.
- No intro/brand card — B00 is the hook, first frame on screen (landscape only).
- No outro card, no "thanks for watching," no channel reference — B04 is a
  plain held final frame with one label.
- Register: formal, undergrad/grad audience — no casual asides, no "doodle"
  narration voice.
- Voice: am_michael (Kokoro).
- Short-form (9:16) variant adds: title card at start, burned-in Open Sans
  captions (one per beat, synced via explicit per-chunk self.wait — no
  scene-time updater, which silently freezes across long self.wait() calls
  due to Manim's frozen-frame optimization), reflowed narrow-frame geometry.

## VERDICT: PASS
