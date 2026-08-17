# PROMPTS — The Pipeline That Was Lying to Me

## Status: no pantry assets needed

The original plan had B00 as a VOX still (a generated/dropped-in dashboard
image). During the build, all 7 beats — including B00 — were implemented as
self-contained Manim scenes in `scenes.py` instead, so no pantry image
generation was ever needed for this cut. See `BUILD-LOG.md` for why (the two
Remotion patterns the original plan named for B02/B06 don't exist in the
installed `brutalist` toolkit, and Manim kept everything self-contained
rather than requiring toolkit changes or external images).

`B00_CalmDashboard` in `scenes.py` renders the "calm feed log, nothing looks
wrong" beat directly: rows of plausible filing titles (SEC/FINRA/CFTC/FedReg)
ticking in against the cream palette, with a small cursor dot tracking down
the list.

This file is kept as a record — if a future cut of this reel wants a real
photographic/screen-capture still instead of the Manim version, the original
prompt is below.

---

### (unused) B00 pantry image prompt — for reference only

**Prompt:** A dark-mode developer terminal/dashboard showing a
regulatory-intelligence feed scrolling calmly — rows of filing titles from
SEC, FINRA, CFTC, and Federal Register sources ticking past in a monospace
log. Neutral, unremarkable, routine — nothing visually alarming, because the
point of this beat is that the pipeline looks fine even while silently
dropping data. Editorial screen-capture style, dark background, muted
syntax-highlight colors, no visible errors or red text. 1920x1080 minimum,
≥2000px on long edge.

**Ken Burns target:** slow annotate drift across the scrolling log (focus
x=0.5, y=0.5)
