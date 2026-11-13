# SOURCES — Walker Tower Defense: The Design Document Came Last

## Primary

| Source | Identity | Used for |
|---|---|---|
| `Walker-Godot-TowerDefense/GDD.md` | v0.1, committed `64f6442`, sha256 `08a36c02c4fb8d6e3d2f9ca8ceb827bd35d62160a67051003d8526cbb7d3af12`; byte copy in `evidence/GDD.md` | every excerpt (read by line number at build time) |
| Game source at `caf082c` | snapshot `f5035b752564de8f6aebbe826f448928959aed280cab94d6e541e0076d4e3bdd` (43 files under `godot/`) | code citations, cause of observed behaviour |
| `GAME-BRIEF.md`, `PORTING_NOTES.md`, `CHANGELOG.md`, `AUDIO-PLAN.md`, `ASSET-PLAN.md`, `PLAYTEST-LOG.md` | at `caf082c` | history, decisions, checklist |
| Test receipts | `evidence/*-1790606724…/…725*.json` in the game repo (2026-09-28T14:45) | 65 checks, 0 failures |
| Unity source | `../elemental-tower-defense-godot/unity-scripts/scripts/` (27 files, 2,620 lines) | `Monster.cs:190-201, 338-340`, `GameManager.cs:229`, `LevelManager.cs:91-131` |
| Scripted-input takes | `capture/opening.mp4`, `poison.mp4`, `storm.mp4`, `maze.mp4` + input logs; method in `../walker-towerdefense-captures/CAPTURE.md` | gameplay beats B04, B07, B08, B10; stills in `evidence/` |

Hashes for every evidence file are in `gdd-evidence.json`.

## Stills

Each still is one engine-viewport frame from a take, with the padding bars cropped:

| Beat | Take | Frame |
|---|---|---|
| B03 | `opening` | 40 |
| B05 | `opening` | 1400 |
| B09 | `maze` | 483 |
| B12 | `opening` | 1722 |
| B14 | `opening` | 112 |
| B15 | `poison` | 300 |

## Corrections applied (DOUBLE-CHECK LAW)

- **Line citation.** The spine line is cited as `monster.gd:112-120`, not the older `:109`. The owner also corrected this in `64f6442`.
- **Checklist count.** "22 playtest items", not 27.
- **Commit count.** Not spoken; it drifts.
- **B07.** Rewritten after frame inspection (poison reads white; wave 1 was Green-variant monsters).
- **B15.** "A folder each" removed.
- **Documentation conflicts found and reported, not fixed:**
  - GDD M-08 edge case 3 is contradicted by the `broken` take.
  - `AUDIO-PLAN.md` describes a red vignette that exists only on `feature/recovered-art`.

## Tools

- Godot 4.7.2.stable.official.ed1daf0bf, run from `~/Downloads/Godot.app`
- Kokoro-82M ONNX v1.0 (`kokoro-v1.0.onnx`, sha256 `7d5df8ec…`)
- Remotion 4 (`npm ci` from the toolkit lockfile)
- ffmpeg

All local and free.
