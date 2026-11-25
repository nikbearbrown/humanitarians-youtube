# Week 29 topic video

*The Rally Has a Clock: When Is "No Perfect Defense" True in Pong?* Tanmay Kulkarni, in for Humanitarians AI.
Text and code only. The two masters are uploaded to YouTube.

## The topic

**Chosen topic: `claude-for-design/pong`** in the `humanitarians-youtube` repository: an essay by Seth Brown
(Zebonastic, Humanitarians AI Fellow), "Pong: Why the Simplest Game Is the Hardest to Explain". The film opens with two
phrases from it, "no perfect defense" and "a game to eleven", and builds the rest from our own model.

- **Selection:** a randomized, unseeded draw over the library's singleton topics (read-only; nothing in the shared repo
  was checked out, pushed or modified). A first draw (`cli-int8-mash`) was rejected as a duplicate (three variant
  folders plus a fellow's `quantization-hurts`). The draw, the rejection and the uniqueness checks are in
  `TOPIC-DECISION.md`.
- **Angle:** *the claim "no perfect defense" is one checkable ratio, and the ball's speed-up gives every rally a clock.*
  The angle and its boundaries are in `ANGLE.md`.
- **Method the film teaches:** compare the defender's reach in one flight with half the free height of the field. The form,
  (height minus paddle) divided by (2 times width), is the ratio of paddle speed to ball sideways speed above which a
  perfect defense exists. It is derived, then tested three times by predicting the shot where it first fails and
  counting it with a search that tries every aim; the viewer gets a fourth field to work.

## The files

| | File | | |
|---|---|---|---|
| **Long** | `the-rally-has-a-clock.mp4` | 3840×2160 · 30 fps · 4:27 (267.4 s) | −14.6 LUFS / −1.9 dBFS |
| **Short** | `the-rally-has-a-clock-short.mp4` | 2160×3840 · 30 fps · 1:19 (79.0 s) | −14.6 LUFS / −1.9 dBTP |

Each film carries its captions (`.srt` and `.vtt`) and its YouTube title, description, chapters and tags (`*-youtube.md`).
Narration is Kokoro `am_onyx`.

**Structure:**
- **Short, one continuous scene:** the bet in the first words, then what Pong is, the essay's claim and why a model, the count of six shots, the two bars, the clock that makes the sixth shot fail, the limits, and the long film's exact title; the scene settles back to its first frame so it loops. Its own script, written for a viewer who never sees the long film.
- **Long, "ONE RALLY, REPLAYED":** a shot counter and two bars (how far the paddle can travel, how far it must) on screen from
  the first frame; a cold open where a perfect defender loses on the sixth shot; the ratio derived; three predict-then-count
  tests; the claim failing when the ball never speeds up; a slate of what the model leaves out; a field for the viewer to
  work, then one open question.

## How it was checked

| | Long | Short |
|---|---|---|
| Rubric | `PROOF.md` teaching rubric /12 + production gate | Shorts rubric /12 + 11-point compiled-file gate |
| Result | 12/12, gate PASS on every measured check (`PROOF-REVIEW.md`, `PROOF-REVIEW-STILLS.md`, `PROOF-REVIEW-FRAMES.md`) | 12/12, gate 12/12 (`short/PROOF-REVIEW-SHORT.md`, `short/PROOF-REVIEW-SHORT-VIDEO.md`) |
| Gate P (narration read aloud) | signed 2026-10-30, three lines re-signed the same day (`GATE-P-SIGNOFF.md`) | signed 2026-10-30 (`short/GATE-P-SIGNOFF-SHORT.md`) |
| Numbers | every figure on screen is computed by `sim_model.py` and asserted against the signed narration; arithmetic reproduced in `FACTCHECK.md` |

## Links

| | Link |
|---|---|
| Long film (YouTube) | <!-- YOUTUBE_LINK_LONG --> (when published on YouTube, this placeholder will be updated) |
| Short (YouTube) | <!-- YOUTUBE_LINK_SHORT --> (when published on YouTube, this placeholder will be updated) |
