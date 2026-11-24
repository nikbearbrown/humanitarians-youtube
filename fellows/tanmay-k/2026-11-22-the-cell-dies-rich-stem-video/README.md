# Week 32 topic video

*The Cell Dies Rich.* Tanmay Kulkarni, in for Humanitarians AI.
Text and code only. The two masters are uploaded to YouTube.

## The topic

**Chosen topic: `claude-for-computer-science/cli-brownout`** in the `humanitarians-youtube` repository (library film: "A Battery Can Be Full and Still Crash Your Device"). Our film starts from the same puzzle, a device that resets while its battery is not empty, and asks the question it leaves open: when the reset happens, how much of the cell is left, and what decides it?

- **Selection:** a draw over topics no fellow (including us) has covered, with read-only commands only (`TOPIC-DECISION.md`).
- **Angle:** *a coin cell is finished for a device when its resistance crosses (open voltage minus reset voltage) divided by the burst, not when its charge runs out; how much is left behind depends on the burst.* Boundaries are in `ANGLE.md`.
- **Method the film teaches:** one rule, done on paper: biggest burst = (open V minus reset V) divided by resistance, then the viewer's two numbers to look up (the device's biggest draw and its chip's reset voltage).
- **Measurements:** our own simulation of a CR2032-class cell (`experiment/`, `MEASUREMENTS.md`), fitted to two manufacturers' published graphs. Share of the cell left unspent at the first reset: 8 mA or less 0%, 10 mA about 1%, 30 mA 16.5%, 60 mA 48%, 100 mA 100%. A model, not a bench measurement.
- **Public values** (each with its source in `FACTCHECK.md`): Duracell's CR2032 datasheet (3.0 V, 225 mAh) and Energizer's coin handbook (a fresh 2032 near 10 ohm; resistance climbing to about 65 ohm over the cell's life in a roughly 30 mA pulse test; a high cutoff "may leave significant capacity unused").

## The files

| | Film | Format | Audio |
|---|---|---|---|
| **Long** | The Cell Dies Rich | 3840x2160 · 30 fps · 4:23 (263.1 s) | -14.7 LUFS, true peak -1.9 dBTP |
| **Short** | The Cell Dies Rich (Short) | 2160x3840 · 30 fps · 1:56 (115.7 s) | -14.6 LUFS, true peak -1.9 dBTP |

Narration is Kokoro `am_onyx` at natural speed. Visuals are original code-drawn animations (the manufacturers' graphs are redrawn from our own readings, not reproduced); the type is Arial and Menlo (macOS system fonts); colours are tagged BT.709.

**Structure:**
- **Long:** one scene from the first frame, a tank (the charge left) and a chart whose line is the biggest burst the cell can pass; the hidden resistor and the rule, the line falling as the cell is used, three asks (8, 30 and 60 mA) run down the same line, the sum on paper, what moves the answer, what the model leaves out, and the viewer's turn.
- **Short:** one persistent scene; the first words state the puzzle, then what is inside the battery and what the line means, the line falling, two asks, the limits; the last frame returns to the first, so it loops, and it ends on the long film's exact title.

## How it was checked

| | Long | Short |
|---|---|---|
| Rubric | teaching rubric /12 + production gate | Shorts rubric /12 + measured compiled-file gate |
| Result | 12/12, every measured check passes (`PROOF-REVIEW.md`) | 12/12, every measured check passes (`PROOF-REVIEW.md`) |
| Gate P (narration read aloud) | signed 2026-11-23, B10 re-signed the same day (`PEDAGOGY.md`) | signed 2026-11-23 (`PEDAGOGY.md`) |
| Numbers | each figure traced to our own run or a cited manufacturer value in `FACTCHECK.md` | same |

## Records in this folder

`TOPIC-DECISION.md`, `ANGLE.md`, `READ-ALOUD.md` and `READ-ALOUD-SHORT.md` (the signed narration), `beat_sheet.json` and `beat_sheet-short.json` (narration, picture plan and measured timing per beat; voice `am_onyx`), `FACTCHECK.md`, `MEASUREMENTS.md` with its code in `experiment/`, `PEDAGOGY.md`, `FRICTIONAL.md`, `PROOF-REVIEW.md`.

## Links

| | Link |
|---|---|
| Long film (YouTube) | <!-- YOUTUBE_LINK_LONG --> (when published on YouTube, this placeholder will be updated) |
| Short (YouTube) | <!-- YOUTUBE_LINK_SHORT --> (when published on YouTube, this placeholder will be updated) |
