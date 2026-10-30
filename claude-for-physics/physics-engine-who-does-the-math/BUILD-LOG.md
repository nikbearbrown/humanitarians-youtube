# BUILD-LOG — who-does-the-math

Physics Engine series, 1 of 17. Built 2026-10-30.

## Order of work

1. Source pinned to `jashshah127/humanitariansai@2dc4aa4`, folder `physics-engine/`
   (the separate `jashshah127/physics-engine` repo is empty).
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md written; scenes in
   `PhysicsEngine01.tsx`, typechecked.
3. GATE P signed by Param Madan in chat → Kokoro `af_bella` audio, 251.9 s.
4. Registered 9 reel-local compositions; rendered at `--scale=2` (3840×2160).
5. Visual QC at p≈0.5 and p≈0.93 on every beat; 8 beats fixed and re-rendered.
6. `./art final` → 4K master.

## What broke, and the fix

- **"A I" voiced as "eye."** Spelling acronyms with spaces (the house rule) fails
  for AI in Kokoro: whisper heard "the kind of eye behind a chatbot". Changed to
  `A.I.` in B00, B01, B04, B07 and regenerated those four; re-transcribed clean.
- **Stale fact in the source.** `EVALUATION.md` says Vibrations and Waves has zero
  cards; `COVERAGE.md` at the same commit says eight. B06 uses the rigid-body
  ratio (180 problems : 1 card) instead.
- **Project code not executed.** The auto-mode permission check blocked running
  the repo's Python, so results are cited as repo-reported, not re-run. Pulley
  math re-derived by hand.
- **QC pass 1 defects (render succeeded, frames were wrong):**
  - B02 strike-through was rotated and crossed the ball arc, not the label → straight
    terracotta strike through "Game engine"; layout scaled up.
  - B04 bottom ~40% empty (dead canvas) and the route name truncated to
    `ambiguous_multiple…` → taller cards, full name wrapped, lesson strip added.
  - B07 closing line touching the third card → cards tightened, line moved down.
  - B09 credit line wrapped with an orphaned "MADAN" → one credit per line,
    `whiteSpace: nowrap`.
  - B01, B03, B05, B06 content clustered high → scaled up to fill SAFE; B05 tile
    values centered vertically.
- `ClaudeComposerAsk` is a shared 900-frame composition; B00 (21 s) and B08 (13 s)
  are trimmed tails, as expected.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
