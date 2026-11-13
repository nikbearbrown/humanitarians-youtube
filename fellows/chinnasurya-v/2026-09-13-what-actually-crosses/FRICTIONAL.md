# Frictional — What Actually Crosses

## 2026-09-13 — script written, build not started

Wrote the full script and art direction in the same session as the two reels that
did get built. The art direction is deliberately identical to
`2026-09-13-canvas-launch-explainer`: four colours, two type families, hard cuts
only, no screenshots, nothing key-shaped or hostname-shaped on screen.

Did the research against the code rather than against my own documents, which was
the right way round and is the reason this script took longer than the other
three. Reading `lib/lti-utils.ts` and the quiz submit route to see what actually
crosses, instead of reading the security review that describes what crosses,
turned up the thing the reel is built on: the interesting part is what is absent.
No gradebook scope, no roster scope, so neither can cross even by accident.

## 2026-09-13 — why it stopped here

Two reels rendered that day and this one did not. No technical reason, I ran out
of session. It has been sitting as a finished script since.

## 2026-10-28 — open

Script is complete and unmodified since 13 September. Render pending. Recording
this honestly rather than filing it as finished work: this is a written script,
not a video.

## 2026-10-28 — built, six weeks later

Rendered it. Before anything could run I had to rebuild the Python environment
for the toolkit, which was simply gone. `./setup --install` failed on the system
Python 3.9 because `kokoro-onnx` needs `onnxruntime>=1.20.1` and there is no 3.9
wheel for it, so pip gave up with `ResolutionImpossible`. Rebuilt on Homebrew
Python 3.12 in a venv outside the toolkit tree, installing only what this
architecture actually uses and skipping `manim` and `faster-whisper`. That is the
second time a stale environment has cost me more than the work itself.

Reusing the September renderer's core paid off again: layout, fonts, `fit()`,
elastic allocation and frame assembly came over verbatim and only the nine scene
functions are new.

Four defects, all found by looking at the contact sheet and none by a gate. The
one that mattered was **B01 saying the opposite of the script**. The script asks
for a mute two-headed arrow struck through in signal. A horizontal strike over a
horizontal arrow is invisible — it merged into the arrow body, and the frame read
as a live red two-way sync, which is exactly the assumption that beat exists to
refuse. Replaced it with a red X of two thick straight segments. I would not have
caught that from the mp4 duration or from a gate report; it needed a human
looking at a picture and asking whether the picture says what the words say.

The other three were geometry: the title cards collided with the footer, B04's
strike crossed its own subtitle, and B06's caption ran past the title-safe edge.
The title card fix is the interesting one, because it is the same mistake as reel
one in a different costume. Reel one put content at hand-set pixel offsets and I
fixed it by moving to fractions of the band. Here I put the title at a fraction of
the frame, which is still a guess, and it collided with an element whose position
I never measured. Now the subtitle rule and the title size are both derived from
the footer upward, and both title states share one `title_card()` so the outro
cannot drift away from the intro again.

`./setup --install` also left `runtime/remotion/package-lock.json` modified by its
npm step. Restored it; `git status` on the toolkit is empty.

Still open: no 9:16 cut, no captions, and `PEDAGOGY.md` is not self-signed.
