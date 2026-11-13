# Week 30 — Topic Selection

**Selected:** `claude-for-computer-science/claude-liam-lstm-ops`
**Source:** "The Smaller Model That Was Eighty Times Slower" (EMBEDDED AI — MODEL SELECTION), Humanitarians AI library
**Decided:** 2026-11-07

## How it was chosen
- **Read-only throughout.** No `git fetch`, checkout or any write. Branches and trees came from the GitHub API
  (`gh api`, GET only): 85 branches, no truncated trees. Nothing in any fellow's folder was touched.
- Pool v1: every `claude-for-*` topic path on every branch (`all-existing-topic-pairs.txt`, 2,191 paths) plus fellow
  folders (`fellows-folders.txt`, 1,128). `pool.py` strips variant prefixes repeatedly, keeps singletons, and drops
  anything recurring in our Weeks 15-29 notes -> 28 candidates, 5 real topics: lstm-ops, json, 256-bits, ai-slop,
  mma-vs-boxing (`pong` removed by hand: Week 29's topic; the filter ignores words of 4 letters or fewer).
- Draw 1 (`random.SystemRandom`): **json** -> rejected. Its folder name hides the film: it is the Bastani "AI help made
  students worse" slate (`vox-the-struggle`), and the same thesis already sits in `claude-for-video-production/vox-the-struggle`,
  `claude/claude-youtube/cognitive-friction-loop`, `ai-homework-fluency-trap`, `vox-struggle-mechanism`, `homework-quiz-gap`.
- Draw 2: **ai-slop** -> rejected. Has a second copy outside `claude-for-*`
  (`claude/claude-research/claude-liam-medhavy-vox-ai-slop`), and its feedback-loop thesis sits next to Jainil's
  2026-10-16 "The Tails Go First".
- **Pool gap found and fixed:** pool v1 never scanned `claude/`, `codex/` or `claude-bear/`. Pool v2
  (`all-topic-paths-wide.txt`, 3,961 paths) shows `256-bits` also has a `claude/` copy. Only `lstm-ops` and
  `mma-vs-boxing` appear once library-wide.
- Draw 3 between those two: **lstm-ops**.

## Uniqueness sweep for lstm-ops
- Paths: 1, no variants, no fellow folder. Code search for the thesis (smaller model, more operations, per-time-step
  cost) returns only this folder. The adjacent embedded-AI items (`cli-int8-mash`, `quantization-hurts`,
  `vox-m-quantization`) are about quantization, a different mechanism.
- Our Weeks 15-29: no LSTM topic (word hits came from unrelated text).

## Build state of the source folder
Built by the pipeline: STATUS.md says 9/9 beats filled (Remotion + Manim), plus scenes.py, images, mp3, youtube.md.
Source is a short book-derived explainer: LSTM 0.2M parameters vs CNN 1.4M, 1.4 billion vs 17 million MACs (the 80x),
"parameters measure storage, ops measure time". Last commit Nik Bear Brown, 2026-08-27 snapshot.

## Open question for the angle
The existing film already states the 80x mechanism. Our angle must add something it does not, and must be checked
against its beats before any build work.

## Local files not in any pushed folder
Raw lists and scripts (`all-existing-topic-pairs.txt`, `fellows-folders.txt`, `all-topic-paths-wide.txt`,
`remote-branches.txt`, `pool.py`, `_*.json`, `_*.raw`) list other fellows' folders and stay local.
