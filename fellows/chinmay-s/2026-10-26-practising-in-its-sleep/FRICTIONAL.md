# Frictional log — Practising In Its Sleep

## 2026-10-26 — 4:55, 18 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `build_beat_sheet.py`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A kid-friendly explainer of a from-scratch World Models
notebook — a VAE, a memory, and a controller evolved entirely inside the model's dream.

**What I tried, and what I expected.** I expected the lead to be "it dreams."

**Where it resisted, and what I did next.**
* The dreaming is the mechanism, not the point. The point is one frame cannot show
  motion. Restructured so the reel opens with a single frame and two futures consistent
  with it, and everything after is a consequence — including why memory nearly doubles
  the catch rate (39.2% → 78.5%) and beats a cheat that sees the true ball (60.8%).
* Acted on the previous reel's lesson: the **build script** now fails if any dense scene
  gets under 12 seconds of projected narration. It passed, and I re-checked against the
  real audio afterwards.
* An assertion caught a bug of mine instantly. `Z_MEM > GREEDY` failed with
  `(60.8, 60.8)` — because `"greedy chaser (sees the true ball, no memory)"` contains the
  word "memory" and my row selector matched it. Without the guard the video would have
  shown the cheat's number as the dreamer's.

**What Claude contributed, and what I did with it.** Mine: leading with the one-frame
problem; the instruction to bake the duration check into the build. Claude's: 8 scenes,
the parsing, the assertions that caught the selector bug.

**What I understand now, and what I still do not.**
* Understood: assertions that encode the *argument*, not just the values, catch the
  errors that would otherwise ship silently and confidently.
* Not resolved: the game boards are drawn parametrically. The dynamics match; the
  specific frames are not a replay of the notebook's arrays.
