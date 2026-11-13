# Walker Tower Defense: three films — Yeshwanth Balaji

These are three films about `walker-towerdefense`, a Godot 4.7.2 rebuild of a recovered Unity tower-defense game. Each film was made with a Brutalist Godot skill, run with the `walker` modifier:

| Film | Skill | Landscape | Vertical |
|---|---|---|---|
| Walker Tower Defense: The Design Document Came Last | godot-gdd walker | 3840×2160, 5:45 | 2160×3840 (pending render) |
| Walker Tower Defense: Every Feature, Played | godot-waikthrough walker | 3840×2160, 4:20 | 2160×3840 (pending render) |
| Walker Tower Defense: Inside the Godot Code | godot-gamedev walker | 3840×2160, 6:41 | 2160×3840 (pending render) |

This folder is the recipe only: source, scripts and records. The videos are on Drive.

## This week's contribution

**Question.** What does the game's design say, what does the build actually do, and how is the code put together? Can the films show that honestly, with no human playtest done yet?

**Built.**

- A GDD written from the repo's evidence only, with every sign-off left pending.
- A scripted-input capture of the real game: eight takes, 33 features, all through real key and mouse input.
- Three films that pair each claim with real engine footage of the same build (`caf082c`).

**Observed.** The footage shows defects that the 65 automated tests do not catch:

- The F1 debug overlay is covered by the board.
- The level-load error panel is covered by the menu card, and Enter still starts a run.
- Poisoned monsters read white, not green.
- The refusal reason is visible for 0.3 s, and the Storm chain for 0.2 s.
- Every scripted opening lost all five lives by wave 3 to 5.

**Next experiment.** A human playtest of the 22-item `PLAYTEST-LOG.md`, starting with items 6, 10 and 11.

## Human and AI work

**My decisions:**

- the films and their order;
- the GDD approach (PROPOSED labels, PENDING sign-offs);
- the corrections to GAME-BRIEF, PORTING_NOTES and CHANGELOG (commits `64f6442`, `caf082c`);
- the constraint that the game is not modified;
- where the films go, and that nothing is published.

**AI tools and voices:**

- Claude (Claude Code) drafted the GDD, wrote the capture driver, beat sheets, narration and these records, and ran the renders.
- Narration is the AI voice "Liam" (Kokoro `am_onyx`, local), named on screen and in the narration. It is not a recording of me.

**Rejected or corrected during the build** (see each `BUILD-LOG.md` and `FACTCHECK.md`):

- A narration line claiming poison "tints it green" was rewritten after the frames showed otherwise.
- A "folder each" approximation was removed.
- Code excerpts were trimmed after a pilot showed clipping.

**Unverified or failed:**

- No human playtest (0 of 22 items).
- The GDD's M-08 edge case 3 is contradicted by the footage.
- Windows and Linux exports were never run.
- YouTube 4K processing has not been checked.

## Reproduce

| Item | Value |
|---|---|
| Brutalist version | brutalist.art at `22264a3`, checked 2026-10-06 |
| Game source | `Walker-Godot-TowerDefense` at `caf082c` (snapshot sha256 `f5035b752564de8f6aebbe826f448928959aed280cab94d6e541e0076d4e3bdd`); Godot 4.7.2.stable.official.ed1daf0bf |
| Captures | `captures/CAPTURE.md` (method, isolated copy, overlays), `capture_driver.gd`, input logs `*-inputs.jsonl`. The capture MP4s are on Drive |
| Each film | `make_sheet.py` (author → Kokoro → finish), then `BUILD-PROMPT.md` for the full command list |
| Checks | `./art godot-gdd --check`, `godot-waikthrough --check` and `godot-gamedev --check`: all PASS. GATE T PASS; Gate V clean; review notes in `_qc/REVIEW.md`; receipts in `*.verified.json` |
| Approvals | none claimed; all design gates PENDING |

## Watch and review

| Video | Drive link | Size | Duration | SHA-256 |
|---|---|---|---|---|
| GDD, landscape | _add link_ | 3840×2160 | 344.6 s | `b01edeb784f254b67a52ba1a7842a6b07bea0f4a2a45e352a6edbabad7077032` |
| Walkthrough, landscape | _add link_ | 3840×2160 | 259.6 s | `033523aea820d38de6b5ef335ba3be57460dec214d494c98abe5349fe59a230d` |
| Gamedev, landscape | _add link_ | 3840×2160 | 401.3 s | `8c2814739d691c0ebe61fb9f8c83f76d7f2b0c0e4252935c3b8b94ddc6857671` |

Vertical links and hashes: _added when rendered_.

| Review step | Status |
|---|---|
| PM review | pending |
| YouTube 4K processing check | pending upload |
| Professors' publication decision | pending |
