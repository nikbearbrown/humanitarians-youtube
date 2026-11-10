# Week 30 topic video

*Where the Eighty Lives: Why a Smaller Model Can Run Far Slower.* Tanmay K., in for Humanitarians AI.
Text and code only. The two masters are uploaded to YouTube.

## The topic

**Chosen topic: `claude-for-computer-science/claude-liam-lstm-ops`** in the `humanitarians-youtube` repository: a film in the library, "The Smaller Model That Was Eighty Times Slower" (Claude for Computer Science playlist). It reports a small recurrent model running about eighty times slower than a bigger convolutional one, even though the small one has fewer parameters. Our film starts from that observation and asks where the time can come from. Its "eighty" figure is credited on screen as reported there; we did not reproduce it, and we do not claim our numbers explain it.

- **Selection:** a randomized, unseeded draw over the library's singleton topics, with read-only commands only (branches and trees came from read-only GitHub API calls; nothing in the shared repo was fetched, checked out, pushed or modified). Two earlier draws were rejected before any angle work (`claude-for-design/json` and `claude-for-design/medhavy-vox-ai-slop`, each already covered under other names), which also exposed a gap in the pool script; the pool was rebuilt wider and the third draw landed here. The draws, the rejections and the uniqueness checks are in `TOPIC-DECISION.md`.
- **Angle:** *the arithmetic can be exactly equal while the time is not; the gap lives between the model and the chip.* The angle and its boundaries are in `ANGLE.md`.
- **Method the film teaches:** a model has three numbers. Parameters say what it stores, operations say what it computes, and overlap says how long it waits. The viewer leaves with one question to ask of any model (which of its steps have to wait for another) and one formula to work, the cost of one recurrent step, 4 × h × (h + x).
- **Measurements:** two tiny models share the same weight block (390 by 512, 199,680 weights) and the same arithmetic (19,968,000 multiply-adds over 100 steps, plus the same gate calculations), and differ only in dependency. Timed in compiled C on one laptop, one thread: about 1.0x when nothing can overlap, about 1.3x with weight reuse, about 3.7x with an optimized matrix multiply (3.3x to 3.8x from 25 to 400 steps; 16 times the steps costs 16 times the time). The most reached is about 4x, not 80x, and nothing was measured on a microcontroller. A first run, found not to be like for like during the fact-check, was corrected before anything was published and is kept as a labelled record in `measurements_v1/`.

## The files

| | Film | | |
|---|---|---|---|
| **Long** | 16:9 | 3840×2160 · 30 fps · 3:46 (226.2 s) | −14.6 LUFS / −1.9 dBFS |
| **Short** | 9:16 | 2160×3840 · 30 fps · 1:42 (102.3 s) | −14.6 LUFS / −1.9 dBFS |

The films are not in this repository: the two masters are uploaded to YouTube (links below). Narration is Kokoro `am_onyx` (recorded as `voice_kokoro` in both beat sheets).
Visuals are original code-drawn animations; the type is Arial and Menlo (macOS system fonts), not the open-licence fonts of Weeks 27 to 29.

**Structure:**
- **Long, "ONE DIAL, ONE OBJECT":** one time step is drawn, then two models that share its weights and its arithmetic. A three-panel frame (parameters store, operations compute, overlap waits) is on screen empty from the first frame and fills as each number is earned. The dial for how much the chip can do at once starts at zero (the two models take the same time), turns up (the gap opens), and a second axis, sequence length, stays quiet. Then the gap is placed between model and chip, the boundary is stated, and the viewer counts one step.
- **Short, one persistent scene:** the first words state the puzzle; then what a recurrent model is and why two models; the same two boxes carry the story from "small and bigger" through the dial to the three numbers, and the scene settles back to its first frame so it loops. It ends on the long film's exact title.

## How it was checked

- **Teaching rubric:** `PROOF.md` rubric 12/12 for the long film and the Shorts rubric 12/12 for the Short, with the production gate passing on every measured check on the compiled files (`PROOF-REVIEW.md`).
- **Gate P** (narration read aloud): signed 2026-11-07; six lines re-signed 2026-11-08 after the fact-check (`READ-ALOUD.md`, `READ-ALOUD-SHORT.md` are the signed text).
- **Numbers:** every figure traced to our own repeated measurements or to the library film (`FACTCHECK.md`); timings in `MEASUREMENTS.md` (median and range over repeated runs), with the code in `experiment/`.

## Records in this folder

`README.md`, `TOPIC-DECISION.md`, `ANGLE.md`, `READ-ALOUD.md` and `READ-ALOUD-SHORT.md`, `beat_sheet.json` and `beat_sheet-short.json`, `FACTCHECK.md`, `MEASUREMENTS.md`, `PEDAGOGY.md`, `FRICTIONAL.md` (drafted after the work from its records; awaiting the fellow's review), `PROOF-REVIEW.md`.
`experiment/`: the measurement code `MEASUREMENTS.md` cites: `measure_dependency.c`, `measure_scalar.c`, `measure_reuse.c` (compiled C, build lines in each header), `measurements_v2.json` (the repeated runs), and `cnn_fair.py`, `lstm_check.py` (the earlier Python checks). The superseded first run, the captions, the YouTube text, the build and check scripts and the other stage reviews are kept locally.

## Links

| | Link |
|---|---|
| Long film (YouTube) | <!-- YOUTUBE_LINK_LONG --> (when published on YouTube, this placeholder will be updated) |
| Short (YouTube) | <!-- YOUTUBE_LINK_SHORT --> (when published on YouTube, this placeholder will be updated) |
