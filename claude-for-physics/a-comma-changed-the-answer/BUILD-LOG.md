# BUILD-LOG — a-comma-changed-the-answer

Physics Engine series, 2 of 17. Built 2026-10-30.

## Order of work

1. Study figures verified against the paper itself (Singh & Strouse 2024,
   arXiv:2402.14903); repo facts pinned to `jashshah127/humanitariansai@2dc4aa4`.
2. Beat sheet (11 beats), PEDAGOGY.md, SOURCES.md written; scenes in
   `PhysicsEngine02.tsx`, typechecked; preview stills QC'd before audio.
3. GATE P: standing approval from Param Madan in chat for the series → Kokoro
   `af_bella` audio, 238.7 s.
4. Transcribed with faster-whisper (tiny.en) to check pronunciation.
5. Registered 9 reel-local compositions at measured durations; rendered at
   `--scale=2` (3840×2160); frames checked at p≈0.5 and p≈0.93 on every beat.
6. `./art final` → 4K master.

## What broke, and the fix

- **Unverifiable figure dropped.** A search summary gave GPT-4 as 84.4% → 98.9%;
  the paper's text has no such pair (its 98.9% is a formatting-adherence figure).
  Only the GPT-3.5 numbers are used.
- **Kokoro sentence break after "A.I."** B07 "ask the A.I. to write…" was voiced
  as two sentences ("ask the AI. To write…"). Reworded to "ask it to write…" and
  regenerated B07 alone.
- **Durations estimated before audio.** Root.tsx was registered with estimates for
  preview stills; updated to round(sec × 30) of the measured audio before render.
- **Project code not executed.** The auto-mode permission check blocks running the
  repo's Python; results are cited as repo-reported. MECH-003 a = 1.96 re-derived
  by hand.
- `ClaudeComposerAsk` is a shared 900-frame composition; B00 (22.6 s) and B08
  (9.2 s) are trimmed tails, as expected.

## Credits

Host and credit line supplied by Param Madan: "Video by Param Madan · Engine by
Jash Shah, Harsh Gujarati, Atharva & Param Madan". GitHub contributors on the
source repo: jashshah127, harshgujarati, Addy-9595.
