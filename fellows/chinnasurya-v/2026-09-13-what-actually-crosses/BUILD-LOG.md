# BUILD-LOG — What Actually Crosses

## Output

| | |
|---|---|
| Master | `medhavy-canvas-sync.mp4` (also at `$ART_HOME/renders/`) |
| Resolution | 3840 x 2160 · 24 fps |
| Duration | 129.125 s (2:09.1) |
| Audio | AAC 48 kHz stereo, Kokoro `am_onyx`, per-beat timeline |
| Beats | 9, all filled from `media/` |
| Size | 4.5 MB |

## Timeline

Script written 2026-09-13 and unchanged since. Built 2026-10-28. The gap is
recorded in `FRICTIONAL.md`: the script was finished in the same session as the
two reels that did render, and this one simply did not get built that night.

## Architecture

Same as `medhavy-lti-verify` and `medhavy-it-requirements`: toolkit used
read-only, narration via `generate_audio_kokoro.py`, conform via `./art final`,
all visuals rendered out of tree by `scenes/render_scenes.py` (Pillow) into
`media/<beat>.mp4`, which `compile.py:resolve_slot()` consumes at the top of its
precedence order. The renderer's core — layout, fonts, `fit()`, elastic
allocation, frame assembly — is reused verbatim from `medhavy-it-requirements`;
only the nine scene functions are new. `git status` on `$ART_HOME` was empty
before and after.

## Environment rebuild

The Python environment for the toolkit was gone and had to be rebuilt before
anything could render. `./setup --install` failed on the system Python 3.9:
`kokoro-onnx` requires `onnxruntime>=1.20.1`, which publishes no wheel for 3.9,
so pip reported `ResolutionImpossible`. Rebuilt against Homebrew Python 3.12 in a
venv outside the toolkit tree, installing only what this architecture needs —
`kokoro-onnx`, `mutagen`, `Pillow`, `numpy` — and skipping `manim` and
`faster-whisper`, which these reels do not use. Kokoro model files were already
on disk. Smoke test synthesised at -21.8 dB.

`./setup --install` also left `runtime/remotion/package-lock.json` modified by its
npm step. Restored, so the toolkit is unmodified.

## Duration drift

Script estimate 126 s from 423 words at the 3.35 words/sec measured on reel one.
Measured 128.9 s of narration, 129.1 s conformed. Within 3 seconds of estimate,
which is the closest of the three reels, because the estimate now uses a measured
rate rather than an assumed one. No holds padded, no narration trimmed.

| Beat | Measured |
|---|---|
| B00 | 8.98 |
| B01 | 13.55 |
| B02 | 14.68 |
| B03 | 14.21 |
| B04 | 19.75 |
| B05 | 14.74 |
| B06 | 19.46 |
| B07 | 15.27 |
| B08 | 8.26 |

## Defects found in QC and fixed

Four, from inspecting the contact sheet. No gate caught any of them.

1. **B01 said the opposite of the script.** The script calls for a mute
   two-headed arrow struck through in signal. A horizontal strike drawn over a
   horizontal arrow is invisible: it merged with the arrow body and the frame read
   as a live red two-way sync, which is precisely the assumption the beat exists to
   refuse. Replaced with a signal X drawn as two thick straight segments across the
   arrow. Unambiguous, and still only straight segments.
2. **B00 and B08 title cards collided with the footer.** Three display lines at
   430 px placed from a hand-set `y` of `0.24 * h` pushed the last line's descender
   past the subtitle rule, and the subtitle at `h1` then overlapped the footer rule
   and footer text. Fixed by deriving both the subtitle rule position and the title
   size from the footer upward — `ry = bottom - 92 - 60 - sub.size - 50`, title
   capped at `(ry - 90 - y) / 3.30` — and by dropping the subtitle from `h1` to
   `h2`. Both title states now share one `title_card()` so the outro cannot drift
   from the intro again.
3. **B04's strike crossed its own subtitle text.** The card strike sits at the
   card's vertical centre, and the subtitle sat at `0.56 h` — close enough to the
   centre that the strike read as striking the words rather than the card. Moved the title to `0.08 h` and the subtitle to `0.68 h`, leaving
   the centre band clear.
4. **B06's closing caption overflowed the title-safe right edge** and its terminal
   block was too narrow for its own text. The caption was drawn at a constant
   `L.body` with no width check. Passed it through `fit()`, widened the terminal
   block by changing the slot divisor from `n + 1` to `n + 1.45`, and raised the
   block's text from `0.21 h` to `0.26 h`.

Defect 2 is the same class of error as the one found on reel one: geometry placed
by hand-set fraction of the frame rather than derived from the element it has to
clear. Reel one's fix moved content off pixel offsets onto fractions of the band;
this one moves the title off a fraction of the frame onto a measurement from the
footer. The lesson is the same each time and I keep paying for it in a re-render.

## Lints — reported, not silenced

- `SKIN LINT: NO RENDERABLE BEATS` — expected. No beat carries a
  `shot.remotion.pattern` because visuals are pre-rendered out of tree. The same
  run reports `9/9 filled`. False positive for this architecture.
- `'hard-snap' carries 5/9 beats (55%) — over the ~40% cap` — the motion labels
  come from the script's own shot list. Relabelling them to satisfy the linter
  would misdescribe the motion, so they were left as written. Note this is the
  same label that was over on `medhavy-it-requirements`.

## Judgment calls

- B00 says "I am Surya". On the two September reels this was flagged as taken from
  conversation context rather than from the script. Here it is in the script, and
  it is correct: this is my own fellowship reel.
- The identifier pairs in B03 are abstract placeholders, visibly truncated. They
  are not real subject identifiers from any database.
- The two code findings the research turned up are not on camera. They are in
  `FACTCHECK.md` and in the project's research plan, because they belong in a
  ticket rather than in an explainer.

## Not done

- No 9:16 cut. At 2:09 it fits under the 180 s cap without dropping beats, so one
  can be produced, but it needs portrait scene layouts rather than a centre crop.
- No captions or word clock. `faster-whisper` was deliberately not installed in
  the rebuilt environment.
- `PEDAGOGY.md` carries `VERDICT: PENDING`. Not self-signed.
