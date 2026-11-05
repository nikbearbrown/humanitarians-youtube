# PEDAGOGY.md — terminal-velocity (Chapter 6, Drag Force and Terminal Speed)

## Concept
A falling object accelerates under constant gravity while drag (growing with
speed squared) builds up an opposing force. When drag grows to equal gravity,
net force reaches zero and the object falls at a constant "terminal"
velocity — zero acceleration does not mean zero speed, it means the forces
have balanced.

## Audit against selection.md bar
- **Single tension:** "gravity is constant, so why does a falling object stop accelerating?"
- **Single resolution:** speed-dependent drag grows until it exactly cancels gravity — net force zero, constant speed.
- **One visual object:** the falling figure, tracked with its two force arrows and afterimage trail throughout.
- **≤6 elements per scene:** figure, afterimages (3-4), gravity arrow, drag arrow, one label — never more than 6 distinct elements.
- **Self-contained:** assumes only F=ma and vector addition; no drag-coefficient derivation, no Stokes' law, no laminar/turbulent distinction.

## Exclusions honored
No drag coefficient derivation, no Stokes' law, no laminar vs turbulent
distinction. All physics communicated through arrow length and afterimage
spacing only, no numbers/axes/graphs. (Per storyboard.)

## Style compliance
- Palette: medhavy (Okabe-Ito) — white ground, ink text, rotating accent per beat (CRIMSON -> TEAL -> GOLD -> GOLD).
- No intro/brand card (landscape) — B00 is the hook.
- No outro card — B03 is a plain held final frame with the TERMINAL VELOCITY stamp.
- Register: formal, undergrad/grad audience.
- Voice: am_michael (Kokoro), 0.85x speed.
- Short-form (9:16) adds title card + burned-in captions, same infrastructure as prior videos.
- Bug patterns checked: gravity arrow held at fixed length/position as sole visual anchor, drag arrow grown via discrete always_redraw-style steps not one smooth interpolation, afterimages stored on self so each beat can fade/replace them, arrows offset from the figure's body line so they don't visually pierce it.

## VERDICT: PASS
