# Week 29 — Topic Selection

**Selected:** `claude-for-design/pong`
**Source:** Seth Brown, "Pong: Why the Simplest Game Is the Hardest to Explain" (Zebonastic; Humanitarians AI Fellow)
**Decided:** 2026-10-30

## How it was chosen
- `git fetch origin` (plain, no prune) refreshed the local `origin/*` refs (104 remote refs). Everything after was
  `ls-tree` / `show` / `grep` against a ref. Nothing checked out, pushed or modified.
- Pool: every `claude-for-*` topic path on every ref (`all-existing-topic-pairs.txt`, 2,190 paths) plus 1,011
  `fellows/*` folders (`fellows-folders.txt`). Variant prefixes stripped repeatedly (`pool.py`), singletons only,
  nothing recurring in our own Week 15-28 notes -> `candidates.txt`.
- Six real topics survived (the rest were lecture chapters): lstm-ops, json, 256-bits, ai-slop, pong, mma-vs-boxing.
  Drawn with `random.SystemRandom` (unseeded): **pong**.
- Rejected draw: `cli-int8-mash`. My first pool script stripped only one variant prefix and missed that it exists as
  `claude-liam-cli-`, `nbb-cli-` and `cli-` variants, beside `claude-liam-quantization-hurts` and a whole
  embedded-AI series. Script fixed, redrawn. (Caught by the uniqueness gate, before any angle work.)

## Uniqueness sweep for pong
- Path: 1 (`claude-for-design/pong`), no variants, no fellow folder. Content on origin/main: only
  `the-ultimate-history-of-video-games` (a history film that mentions Pong) and a term list. No mechanism content.
- Our Weeks 15-28: 0 hits for pong / atari.

## Build state of the folder
Unbuilt 10-beat essay conversion (July 2026): README, BUILD-PROMPT, SOURCES, `beat_sheet.json`, `mp3/timings.json`.
No STATUS/BUILD-LOG/FACTCHECK. Source HTML (`188648185.pong.html`) is not in the repo, so only the beat-sheet
extracts of the essay are visible: top-down view, paddles move only up/down, "no perfect defense", first to 11.
Last commit: Nik Bear Brown, 2026-08-27. Caveat: refs as of today's fetch.

## Local files not in the pushed folder
The raw lists this draw used (`all-existing-topic-pairs.txt`, `fellows-folders.txt`, `candidates.txt`, `sweep.out`) and the two scripts that made them (`pool.py`, `sweep.py`) list other fellows' folders, so they stay local.
