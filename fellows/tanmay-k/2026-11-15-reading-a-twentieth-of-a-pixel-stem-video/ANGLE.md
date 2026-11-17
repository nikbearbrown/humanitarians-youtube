# Week 31 topic video — ANGLE (draft v1, 2026-11-16)

**Topic:** `claude-for-design/galaxy-doppler` (library film: "How Astronomers Weigh a Galaxy Using Only Light").
**Formats:** one 16:9 long film (3840x2160) and one 9:16 Short (2160x3840), built together, each with its own script.

## Thesis
A Doppler shift is a position on a ruler, and the ruler is read finer than its own marks. One kilometre per second
is a shift of 0.0022 nm at H-alpha, about a twentieth of a 0.05 nm detector pixel (our chosen, illustrative pixel).
Astronomers quote speeds to that level. The precision is bought with photons: the error in a line's centre falls as
**line width over the square root of the photons counted**. Count a hundred times the light, know the speed ten
times better. (Andromeda's observed Sun-frame shift is about 0.66 nm, thirteen pixels; the hard part is the last
kilometre per second, not the first three hundred.)

**Working title:** "Reading a Twentieth of a Pixel" (slug `a-twentieth-of-a-pixel`). The Short ends on this exact title.

## What the library film states, and what ours adds
The library film sets up the Doppler formula, Andromeda's blueshift, rotation curves, flat curves and dark matter,
and says "the shift gives the speed directly". It does not say how well a shift can be read. Ours starts from the
same puzzle (a colour change becomes a speed) and answers the question it leaves open: how small a shift, how
sure, at what cost in light. Nothing in the dark-matter argument is re-told or disputed.

## Our own evidence (not borrowed)
`experiment/photon_precision.py` (numpy, seed 31): one Gaussian line (FWHM 100 km/s = line sigma 42.5 km/s),
detector pixel 0.05 nm = 22.84 km/s, photons binned into pixels, centre recovered from the binned counts only.
Measured RMS error vs photons: 10 -> 14.6 km/s, 100 -> 4.6, 1,000 -> 1.45, 10,000 -> 0.46, 100,000 -> 0.14.
Ratio to sigma/sqrt(N) stays 1.06 to 1.09 over four decades (the small cost of binning). At 1,000 photons the error
is 6% of one pixel.

## Method the film teaches
Three numbers for any measured speed: **the shift** (how far the line moved), **the width** (how smeared the line
is), **the count** (how many photons). Error ~ width / sqrt(count). Viewer exercise: for a 100 km/s wide line, how
many photons to know the speed to 5 km/s? N = (42.5 / 5)^2 ~ 72.

## Boundaries (stated on screen, deliberate)
- Ideal case only: one clean line, no sky glow, no calibration error, no blended lines. Real spectra add all three
  and can do worse than sigma/sqrt(N).
- We measured nothing on a telescope. All error figures are from our own simulation.
- Whose speed? A shift is relative: it contains the observer's motion too. Reference-frame numbers (Andromeda's
  Sun-frame vs Galactic-frame approach speed) are public literature values and go through FACTCHECK before use.
- The rotation-curve beat shows error bars growing where light is faint; it does not re-argue dark matter.

## Structure (derived from the subject, not a template)
**Long, "ONE LINE, ONE COUNTER":** a row of detector pixels is on screen from the first frame. A single H-alpha line
is drawn by photons arriving one at a time; a marker shows our best guess of the centre and wobbles, then settles.
10 photons: wobbles. 100: calmer. 1,000: inside a sliver of a pixel. A dial (photons, log scale) turns and the
error bar shrinks as 1/sqrt(N), the same bar reappearing at each setting. Then the frame zooms out to a spiral
galaxy's rotation curve: outer points have fewer photons, so their bars are longer. Close on the boundaries and the
viewer's N = (width / error)^2 exercise.
**Short, one persistent scene:** same pixel row. Opens on the puzzle (0.24 nm shift, 0.05 nm pixel, speed to 1 km/s),
the photons fall in, the wobble settles, the dial turns twice, the scene returns to its first frame, last line is
the question the long film answers. Its own script; not a cut of the long.

## Tone arc
curious (how can a pixel hide a shift?) -> puzzled -> hands-on (watch the photons fall) -> surprised (it is just
square roots) -> careful (what this does not cover) -> handed over (your turn). Narration in first person, humane,
years in words (Kokoro), no politics, no third-party media: our own simulation and public physical constants only.

## Uniqueness
No fellow folder or our Weeks 15-30 notes cover Doppler, redshift or photon-limited measurement. Library has the one
film above (one persona variant plus a `claude/claude-youtube` copy). Re-run the thesis sweep on photon-count
precision / centroiding before BEATS-DRAFT.
