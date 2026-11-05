# PEDAGOGY.md — standing-waves (Chapter 16, Standing Waves and Resonance)

## Concept
Two identical sinusoidal waves traveling in opposite directions superpose
into a standing wave, y(x,t) = [2A sin(kx)] cos(omega t): nodes at
x = n lambda/2 that never move, antinodes at odd multiples of lambda/4 that
swing between +-2A. The pattern is stationary even though both components
keep traveling.

## Audit against the bar
- **Single tension:** a wave that appears to stand still is built from two waves that are both moving -- how?
- **Single resolution:** superposition of opposite-traveling identical waves; the sum factorizes into a fixed spatial shape times a temporal oscillation.
- **One primary visual object:** the string's displacement curve on one shared axis (the live black sum), with its two components drawn faintly beneath.
- **<=6 elements per scene:** B00: 2 waves + 2 direction labels. B01: axis, 2 faint components, sum. B02: + node dots/guides group + one label. B03: + antinode bands + one label (node/antinode labels faded before B04). B04: equation, 2 components, sum, nodes, bands = 6. B05: equation replaced by summary line = 6.
- **Self-contained:** needs only the idea of a sinusoidal traveling wave and superposition; every term (node, antinode) is defined on screen as it is introduced.

## Physics check (against 16-waves/6-standing-waves-and-resonance.mdx)
- Components y1 = A sin(kx - omega t) (rightward, teal) and y2 = A sin(kx + omega t) (leftward, crimson); sum = 2A sin(kx) cos(omega t) -- Equation 16.14. The sum curve is computed in code as the literal y1 + y2 each frame, not from the closed form.
- Nodes: sin(kx) = 0 -> x = n lambda/2, n = 0, 1, 2, ... (textbook). Drawn at exactly those x.
- Antinodes: sin(kx) = +-1 -> x = lambda/4, 3lambda/4, ...; amplitude 2A (textbook text at Fig. 16.27 discussion: "oscillate between y = +-2A"). Bands centered there, height = 2 * 2A|cos(omega t)|, i.e. the actual envelope.
- Energy claim: a standing wave transports no net energy along the string; energy oscillates within each segment between nodes (consistent with the section's opening: traveling waves transport energy, standing waves are "effectively stationary"). Stated as "Energy no longer travels along the string. It oscillates in place, between the nodes." -- correct.
- Storyboard's "white NODE dots on black" and blue/red/green are remapped to the locked medhavy palette: teal = rightward, crimson = leftward, ink = sum, slate = nodes, gold = antinodes.

## Exclusions honored
No Fourier decomposition, no overtone series / normal-mode derivation, no 2D/3D standing waves, no boundary reflection.

## Style compliance
- Palette medhavy, white ground; accent rotates TEAL -> INK -> SLATE -> GOLD -> TEAL -> CRIMSON.
- Narration formal, describes physics not the screen. Voice am_michael 0.85.
- Portrait: question card from B00Q (reused near-verbatim from B00's question) + captions; landscape starts at B00.
- Bug patterns checked: all labels next_to() mobjects, nothing in caption band, all mobjects stored on self and faded when superseded, dt-driven clock keeps waves moving in every wait.

## VERDICT: PASS
