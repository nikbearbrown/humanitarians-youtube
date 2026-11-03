# BUILD-LOG — Four Documents

## Output

| | |
|---|---|
| Master | `medhavy-it-requirements.mp4` (also at `$ART_HOME/renders/`) |
| Resolution | 3840 x 2160 · 24 fps |
| Duration | 157.5 s (2:37.5) |
| Audio | AAC 48 kHz stereo, Kokoro `am_onyx` |
| Beats | 9, all filled from `media/` |

## Architecture

Same as `medhavy-lti-verify`: toolkit read-only, visuals rendered out-of-tree by
`scenes/render_scenes.py` into `media/<beat>.mp4`. The renderer's core (layout,
fonts, elastic allocation, assembly) was reused verbatim from the first reel;
only the scene functions are new. `git status` on `$ART_HOME` empty before and
after.

## Duration drift

Script estimate 2:26 (491 words at the measured 3.35 words/sec from reel one).
Measured 2:37.5 — slightly *over*, unlike reel one, because B02 carries a long
list of remediations that Kokoro reads more slowly than average prose. No holds
padded; no narration trimmed.

## Defects found in QC and fixed

1. **B06 answer text overflowed its box** (found by frame inspection, not by a
   gate). The answer font was a constant 190 px while the box height came from a
   fraction of the available band, so `NO` / `NONE` / `CONFIRMING` crossed the
   lower border and read as struck-through. Fixed by deriving the font size from
   the box height (`int(bh * 0.44)`) and raising the box to 0.225 of the band.
2. **B04 crossed the title-safe right edge** — caught by GATE V as a BLOCKER on
   two sampled frames. The line `MEASURED — NOT PROMISED` was drawn from a
   hand-set x of 2200 at a fixed body size, running past 3588. Fixed by passing
   both that line and the measured values through `fit()` with a max width of
   `L.right - 2200`.

Both were renderer-source fixes, re-rendered and re-inspected. GATE V clean on
the rebuild: 18 frames, 0 blockers, 0 majors.

## Lints — reported, not silenced

- `SKIN LINT: NO RENDERABLE BEATS` — expected for this architecture; the same run
  reports `9/9 filled`.
- `'hard-snap' carries 5/9 beats (55%) — over the ~40% cap` — note this is the
  *opposite* label to reel one, where `step-reveal` was over. The labels come
  from the script's own shot list in both cases and were left as written.

## Judgment calls

- Speaker name "Surya" in B00, carried over from reel one. Still the operator's
  to correct.
- No subprocessor is named aloud or on screen, though the FERPA document names
  all six. B03 shows six anonymous blocks with the AI provider's marked
  `NO IDS` — the count and the property are the point, not the vendors.
- Row 11 of `FACTCHECK.md` (105 segments, 0 failures) is a point-in-time
  reading. Flagged there as needing re-measurement if the reel is rebuilt.

## Not done

- No 9:16 cut. At 2:37 it fits under the 180 s cap with no beats dropped, so one
  can be produced on request — it needs portrait scene layouts, not a centre-crop.
