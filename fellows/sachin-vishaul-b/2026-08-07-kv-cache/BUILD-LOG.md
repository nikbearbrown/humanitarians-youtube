# BUILD-LOG — "Claude, Cached."

Session date: 2026-08-31 · Toolkit: `brutalist.art` (ai-explainer skill,
concept-explainer mode) · Cost: $0.00 · Register: Teardown, claude-liam
channel.

## What was built

9-beat `ai-explainer` reel. Per ILLUSTRATE LAW, Claude UI appears only at
the bookends (B00 cold open, B06 verdict, B07 handoff, B08 outro); every
body beat (B01-B05) is a hand-written Manim scene (`scenes.py`) — the
toolkit's shared C2/C3 illustration-component library
(`LayerStack`/`SourceFlow`/`ChipGrid`/`PredictCard`, the five rhetorical
patterns) turned out not to be registered/renderable in this install
(`./art scenes --check` confirmed), so every diagram here is original.

## Toolkit fix that made this possible

`manim` was not resolvable on PATH at all in this environment (only
`python3` had a working shim). Added a matching shim
(`/c/Users/sachi/bin/manim` → the toolkit's venv `manim.exe`) and verified
it with a throwaway smoke-test render before authoring any real content.
This reel is the first one built after that fix, and rendered clean on the
first real pipeline run — no beat-specific GATE A/B/W failures, unlike the
`consistent-hashing` reel built alongside it (see that folder's
`BUILD-LOG.md` for the layout-audit bugs found and fixed there).

## Known gaps in this submission

- **9:16 cut not built.** Only 16:9 exists.
- **PROOF-REVIEW: pending.** `PROOF.md` not yet supplied.
