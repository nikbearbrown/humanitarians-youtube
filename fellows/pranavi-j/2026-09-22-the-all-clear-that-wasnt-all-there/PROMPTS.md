# PROMPTS — The All-Clear That Wasn't All There

## Status: N/A — all Manim, no pantry stills, no Remotion, no image-generation prompts

All 9 beats (landscape `scenes.py` and the `vertical/scenes.py` companion)
are self-contained Manim `GRAPHIC` scenes built entirely from primitives
(`Text` via the `T()` helper, `RoundedRectangle`, `Line`, `Circle`, `Square`,
`Rectangle`, `VMobject` for the drawn checkmark) and the house
palette/helpers copied from this fellow's sibling reels
(`2026-09-14-rag-why-looking-it-up-isnt-enough/scenes.py` and
`2026-09-14-b3-the-link-that-pointed-nowhere/scenes.py`). No vox/stills, no
Smithsonian/pantry fetch, no Higgsfield AI video beats, and no Remotion
compositions were needed or used for this cut — there is nothing in the
`pantry/` asset-status sense to log here.

One substitution is worth recording (not an AI-image prompt, but the closest
thing to an "asset decision" this build made): the source material's card
labels carry a leading emoji glyph (e.g. "\U0001F4F0 SEC Press Releases").
Manim's text-to-SVG-path pipeline in this environment cannot rasterize
color-emoji glyphs — a direct test confirmed the glyph is silently dropped
(renders as blank space). Every card badge substitutes a small drawn circle +
short mono abbreviation (SEC / FED / FIN / CFTC / IAR) for the dropped emoji;
the verbatim text label is unchanged. See `scenes.py`'s module docstring,
`SHOTLIST.md`, and `BUILD-LOG.md` for the full empirical finding.

This file exists to satisfy the toolkit's `require_paperwork()` gate
(`runtime/scripts/build_safety.py`, effective 2026-09-07), which requires
`FACTCHECK.md`, `SHOTLIST.md`, and `PROMPTS.md` to all exist and be
non-empty before a final export is allowed to run.
