# Frictional log — Finishing Your Sentences

## 2026-10-12 — 4:17, 21 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `build_beat_sheet.py`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A kid-friendly explainer of a from-scratch GPT notebook
(hand-written autodiff, two gradient checks, a copy-task sanity exam).

**What I tried, and what I expected.** I expected the hard part to be explaining
attention.

**Where it resisted, and what I did next.**
* It wasn't. The hard part was making loss mean anything to a child. Converting it with
  `exp(loss)` into "how many letters is it still choosing between" gave **96 → 11.5 →
  4.6**, which is exact — perplexity *is* `exp(loss)` — and immediately legible.
* I shipped a **3.1-second verdict beat**: six dense lines on screen with one short
  sentence of narration. Unreadable. Rewrote it to 20.4s.
* The attention lines all drew at the same height and stacked into one flat bar. Arcs
  fixed it.
* Spent three attempts on an escaping bug: the merge tokens hold a *literal* backslash
  plus "n" because the notebook printed the repr, and my own Python heredoc mangled the
  backslashes while I was fixing it.

**What Claude contributed, and what I did with it.** Mine: the `exp(loss)` framing as
the spine. Claude's: 9 scenes, the parsing, the fixes.

**What I understand now, and what I still do not.**
* Understood: the right unit change can do more explanatory work than any animation.
* Not resolved: the attention visual is schematic. Real attention maps are messier, and
  the reel does not pretend otherwise.
