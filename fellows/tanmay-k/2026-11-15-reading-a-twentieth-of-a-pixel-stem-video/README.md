# Week 31 topic video

*Reading a Twentieth of a Pixel.* Tanmay Kulkarni, in for Humanitarians AI.
Text and code only. The two masters are uploaded to YouTube.

## The topic

**Chosen topic: `claude-for-design/galaxy-doppler`** in the `humanitarians-youtube` repository (library film: "How Astronomers Weigh a Galaxy Using Only Light"). Our film starts from the same puzzle, a color change that becomes a speed, and asks the question it leaves open: how finely can a shift be read, and what does that cost?

- **Selection:** a draw over topics no fellow (including us) has covered, with read-only commands only; the first draw was rejected and a redraw landed here (`TOPIC-DECISION.md`).
- **Angle:** *a Doppler shift is read to a twentieth of a pixel, and the price is photons: error = line width / square root of the photons counted.* Boundaries are in `ANGLE.md`.
- **Method the film teaches:** three numbers for any measured speed: how far the line moved, how wide it is, how many photons were counted. The viewer leaves with one rule and one calculation to run: for a 100 km/s line and a 5 km/s target, N = (42.5 / 5)^2 = 72.
- **Measurements:** our own simulations (`experiment/`, `MEASUREMENTS.md`). The measured error at 10, 100, 1,000, 10,000 and 100,000 photons is 14.6, 4.6, 1.45, 0.46 and 0.14 km/s, within 6 to 9% of the rule; ten times as many glow photons as line photons took the error at 1,000 photons from 1.4 to 3.4 km/s. The rotating disk is a labelled toy. No telescope data was used and the film says so.
- **Public values** (each with its source in `FACTCHECK.md`): H-alpha at 656.28 nm in air (NIST ASD), Andromeda about -300 km/s from the Sun and about -109 km/s in the Galactic frame.

## The files

| | Film | Format | Audio |
|---|---|---|---|
| **Long** | Reading a Twentieth of a Pixel | 3840x2160 · 30 fps · 3:30 (209.5 s) | -14.6 LUFS, true peak -1.8 dBTP |
| **Short** | Reading a Twentieth of a Pixel (Short) | 2160x3840 · 30 fps · 1:44 (104.2 s) | -14.6 LUFS, true peak -1.9 dBTP |

Narration is Kokoro `am_onyx`. Visuals are original code-drawn animations; the type is Arial and Menlo (macOS system fonts).

**Structure:**
- **Long:** a three-panel frame (MOVED, WIDE, COUNTED) is on screen empty from the first frame and fills as each number is earned; then the rule, the price of precision, what a shift also carries (our own motion), a toy disk, what was not tested, and the viewer's turn.
- **Short:** one persistent scene; the first words state the question, then how light gives a speed, what was built, ten photons, a thousand, the rule and its limit; the last frame returns to the first, so it loops, and it ends on the long film's exact title.

## How it was checked

| | Long | Short |
|---|---|---|
| Rubric | teaching rubric /12 + production gate | Shorts rubric /12 + measured compiled-file gate |
| Result | 12/12, every measured check passes (`PROOF-REVIEW.md`) | 12/12, every measured check passes (`PROOF-REVIEW.md`) |
| Gate P (narration read aloud) | signed 2026-11-16 (`PEDAGOGY.md`) | signed 2026-11-16 (`PEDAGOGY.md`) |
| Numbers | each figure traced to our own runs or a cited public value in `FACTCHECK.md` | same |

## Records in this folder

`TOPIC-DECISION.md`, `ANGLE.md`, `READ-ALOUD.md` and `READ-ALOUD-SHORT.md` (the signed narration), `beat_sheet.json` and `beat_sheet-short.json` (narration, picture plan and measured timing per beat; voice `am_onyx`), `FACTCHECK.md`, `MEASUREMENTS.md` with its code in `experiment/`, `PEDAGOGY.md`, `FRICTIONAL.md`, `PROOF-REVIEW.md`.

## Links

| | Link |
|---|---|
| Long film (YouTube) | <!-- YOUTUBE_LINK_LONG --> (when published on YouTube, this placeholder will be updated) |
| Short (YouTube) | <!-- YOUTUBE_LINK_SHORT --> (when published on YouTube, this placeholder will be updated) |
