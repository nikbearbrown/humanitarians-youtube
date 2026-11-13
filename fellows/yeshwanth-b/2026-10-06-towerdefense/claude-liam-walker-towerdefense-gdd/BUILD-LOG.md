# BUILD-LOG — claude-liam-walker-towerdefense-gdd

2026-10-05. Built by Claude in a Claude Code session, at the owner's request.

## Environment (toolkit untouched)

**Kokoro model.** It was absent, so the documented free model files were downloaded to `runtime/models/kokoro/` (gitignored):

- `kokoro-v1.0.onnx`, sha256 `7d5df8ec…`
- `voices-v1.0.bin`, sha256 `bca610b8…`

**Python packages.** `kokoro_onnx`, numpy and scipy were not installed system-wide. They were installed into an isolated virtualenv in the session scratchpad, not into Homebrew Python. The `./art` gates ran with that venv first on `PATH`.

**espeak path bug.** espeak-ng ignores a data path longer than its internal buffer. The venv path is 187 characters, so espeak fell back to its compiled-in build path and called `exit()`.

- Fixed by copying `espeak-ng-data` to `/tmp/espk-data` and symlinking the venv's copy to it.
- Verified with `setup_smoke_kokoro.py` → `kokoro synth OK — mean_volume -21.7 dB`.

**Remotion.** `runtime/remotion/node_modules` was absent. Installed with `npm ci` from the committed lockfile (gitignored).

**`consumers.json`.** `remotion_scenes.py` updates its usage index. That file shows no tracked change in the toolkit's git status.

## Corrections during the build

- **B07 rewritten.** The first narration said poison "tints it green". Frame inspection showed two things:
  - wave 1 was two Green-variant monsters, so there was no visible change;
  - poisoned monsters read pale white, because each poison tick resets `hit_flash`.
- **B08 replay window.** Moved from frames 175–181 to 173–178, after measuring beam pixels: the beam is present in exactly frames 173–178.
- **B15.** "A folder each" was removed; it was approximate.
- **B09.** Changed from an image layout to cards. GATE T §8.3 flagged terracotta-coloured text in the embedded still. That colour belongs to the game's own red refusal tile and hover tint, not to our typography. The refusal is shown live in B10.

## GATE T and gameplay beats

The first final export was refused by GATE T:

- B04, B07, B08, B10: §8.2 overflow and §8.3b local contrast;
- B09: §8.3.

On inspection, the overflow text in the gameplay beats is the game's own HUD top bar ("WALKER / TOWER DEFENSE", gold, lives) at 4K y ≈ 60–90. That is game pixels, not designed typography. The low-contrast blobs are monsters mid hit-flash on the pale board.

The gameplay beats are therefore typed `SCREEN`. In `type_check.py`, `SCREEN` covers a capture of an application's own UI, which is exempt from pixel checks.

This is **not** a relabel as a source report, and it does not exempt any designed beat. To compensate:

- Our own overlays (the disclosure labels, input chips and REPLAY / HELD FRAME tags) were moved inside the 90% title-safe box: left bar x 196–387, right bar x 3452–3644, everything above y 2032.
- Their contrast was chosen against `#1f2329`: label `#d9dee6` ≈ 12:1, sublabels `#a9b2bf` ≈ 7:1, hint `#8f99a6` ≈ 5:1.
- They were checked by eye in `_qc/`.
