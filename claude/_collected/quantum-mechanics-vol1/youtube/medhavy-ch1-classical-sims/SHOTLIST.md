# SHOTLIST — medhavy-ch1-classical-sims

## Histogram
- 9 beats total
- 6 Remotion graphic beats (B01, B02, B04, B05, B07, B08)
- 3 Manim simulation beats (B03, B06, B09)
- 0 photo/still beats
- 0 AI image beats

## Rhythm (estimated durations)
B01 9s · B02 11s · B03 18s | B04 11s · B05 11s · B06 18s | B07 10s · B08 12s · B09 20s
Total: ~120s (2:00)

## Act map
- B01–B03: PHOTOELECTRIC EFFECT (ASK → CODE → RUN)
- B04–B06: COMPTON SCATTERING (ASK → CODE → RUN)
- B07–B09: ULTRAVIOLET CATASTROPHE (ASK → CODE → RUN)

## Color law
Medhavy / Okabe-Ito palette. TEAL #009E73 = correct/quantum result. CRIMSON #D55E00 = wrong/classical prediction. INK #000000 for all text. CREAM #F0EAD6 ground. No text in TEAL or CRIMSON — shape fills only (Gate W constraint: TEAL on CREAM = 2.84:1, below 3.0).

## Exclusions (from source card)
- No NikBearBrown outro — this is a Medhavy proof cut
- No EXAMPLE act
- No AI still beats
- Stop before publishing

---

## Beat-by-beat shot notes

### B01 — PHOTOELECTRIC EFFECT: ASK
GRAPHIC · remotion · fade · MedhavyTerminalAsk
Pattern props: command = `simulate photoelectric-effect --metal sodium --photons red green UV`
No fill-in slots. Fully generated.

### B02 — PHOTOELECTRIC EFFECT: CODE
GRAPHIC · remotion · fade · MedhavyCodeBlock
Pattern props: filename = `photoelectric.py`, code = photoelectric threshold code + output
No fill-in slots. Fully generated.

### B03 — PHOTOELECTRIC EFFECT: RUN
GRAPHIC · manim · fade · B03_PhotoelectricRun
Renders from vox_scenes.py. Three photon arrows + threshold chips + electron velocity arrow.
No fill-in slots. Fully generated.

### B04 — COMPTON SCATTERING: ASK
GRAPHIC · remotion · fade · MedhavyTerminalAsk
Pattern props: command = `simulate compton-scattering --angles 0 90 180`
No fill-in slots. Fully generated.

### B05 — COMPTON SCATTERING: CODE
GRAPHIC · remotion · fade · MedhavyCodeBlock
Pattern props: filename = `compton.py`, code = Δλ formula + angle loop + output
No fill-in slots. Fully generated.

### B06 — COMPTON SCATTERING: RUN
GRAPHIC · manim · fade · B06_ComptonRun
Three-panel layout: θ=0°/90°/180°. TEAL arrows = X-rays; CRIMSON arrows = electron recoil.
No fill-in slots. Fully generated.

### B07 — ULTRAVIOLET CATASTROPHE: ASK
GRAPHIC · remotion · fade · MedhavyTerminalAsk
Pattern props: command = `simulate blackbody-radiation --model classical planck --temp 3000`
No fill-in slots. Fully generated.

### B08 — ULTRAVIOLET CATASTROPHE: CODE
GRAPHIC · remotion · fade · MedhavyCodeBlock
Pattern props: filename = `blackbody.py`, code = planck() + rayleigh_jeans() + comparison loop
No fill-in slots. Fully generated.

### B09 — ULTRAVIOLET CATASTROPHE: RUN
GRAPHIC · manim · fade · B09_UVCatastropheRun
Axes plot. TEAL curve = Planck. CRIMSON curve = Rayleigh-Jeans. Annotations: coincide at low x, UV catastrophe at high x.
No fill-in slots. Fully generated.
