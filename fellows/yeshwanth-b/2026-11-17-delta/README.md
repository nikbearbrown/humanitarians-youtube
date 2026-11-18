# Delta — three films — Yeshwanth Balaji

Three films about **Delta**. It is a Godot 4.7.2 rebuild of a Unity first-person puzzle game: a space station folded into two layers, energy cells carried between machines, and an unstable core taken past two guardians. The Unity source arrived with scripts and art but no scenes, levels or audio; the rebuild adds twelve designed levels, synthesized audio and the full menu flow. Each film was made with a Brutalist Godot skill, run with the `walker` modifier.

| Film | Skill | Landscape | Vertical |
|---|---|---|---|
| Delta: The Design Document Came Last | godot-gdd walker | 3840×2160, 6:21 | 2160×3840 |
| Delta, Every Feature, Played | godot-waikthrough walker | 3840×2160, 11:39 | 2160×3840 |
| Delta: Inside the Godot Code | godot-gamedev walker | 3840×2160, 6:10 | 2160×3840 |

This folder is the recipe only: the GDD, scripts and records. The videos are on Drive.

## This week's contribution

**Question.** What does the finished game actually do, how is it built, and what would its design document say? Can the films show that honestly, with no human playtest done yet?

**Built.**

- **Verified the game in the engine.**
  - The game's own playtest passes on an isolated copy: all 12 levels in 446 simulated seconds. It uses a test-only autopilot hook and turns the guardians' attacks off.
  - The exported macOS app boots headless with exit 0.
  - The Windows `.exe` was not run.
- **Four scripted-input captures of the real build,** at native 4K, 30 fps, with the guardians attacking on their own. They were played only through key, mouse and gamepad events: no teleports and no game method calls. 90 of 90 assertions pass.
  - `campaign1`: an empty save, the menu, How to Play, New game, levels 1–6.
  - `campaign2`: Continue, levels 7–12, the ending and the credits. Four strikes escaped, three shockwaves jumped, and a strike lured onto the shield generator.
  - `defeat`: a refused shift, a plasma death, the pause menu (Restart, Skip, Main menu), a dropped cell returning to its spawn, and a fall back to the checkpoint.
  - `extras`: Options, Credits, Select level with best times, a mouse sweep, running, jumping, and a simulated gamepad (Y, X, left stick).
- **`GDD.md`,** written after the game from the Unity scripts, the Godot project and the captures. Every claim is labelled SOURCE / AUTHORED / IMPLEMENTED / OBSERVED / PROPOSED / PENDING, and nothing is signed off.
- **Three films,** each pairing claims with real engine footage of the same build (`build_id 25e03b2`).
  - The walkthrough shows 51 features and lists the 8 it did not exercise.
  - The gamedev film pairs 13 verbatim code excerpts with the result each one produces.

**Observed.** The captures and source reading found things a quick play would miss:

- **R-01, the pause menu ignores mouse clicks.** `hud.gd:313-318` adds a full-screen `CenterContainer` for the options panel on top of the pause panel, and every click lands on it. Resume, Restart level, Skip level, Options and Main menu work only with the arrow keys and Enter (`defeat`, frame 2123).
- **R-02, R, N and Esc do nothing while paused.** `level.gd:804` handles them in `_unhandled_input`, but the level node pauses with the tree (`defeat`, frame 2411).
- **R-03, the player creeps ahead of a moving shuttle.** Standing still on it, the player gained about 11.5 m on an 8 m ride in headless trials and walked off the front. The driver keeps itself centred on the deck.
- **R-04, Continue on Level Complete logs an error:** `Parent node is busy setting up children, add_child() failed` (`hud.gd:364` via `game_state.gd:373`). The next level still loads.
- **Level 6's bridge gap is hard to reach.** A solid shape at x 17.9 blocks the walk to it; the driver drops the cell from where it stands. The films do not use the stuck stretch.
- **Built in code.** `level_01.tscn` is 7 lines; in play, the level holds 604 live nodes (`captures/tree_probe.txt`). Every level is built from an ASCII map in `levels.gd`.
- None of these were fixed: the game folder was not modified.

**Next experiment.** A human playtest of the proposed experience goals (GDD §5), starting with whether a first-time player understands layer shifting by level 2.

## Human and AI work

**My decisions:**

- the game, and the request for the same three-film set as the earlier submissions;
- that the game is not modified;
- the Liam / @NikBearBrown narration, as in the earlier films;
- where the films and submissions go, and that nothing is published from the toolkit.

**AI tools and voices:**

- Claude (Claude Code) wrote the GDD, the capture driver, beat sheets, narration and these records, and ran the renders.
- Narration is the AI voice "Liam" (Kokoro `am_onyx`, local), named in the narration. It is not a recording of me.

**Rejected or corrected during the build:**

- Early autopilot versions kept walking after Level Complete, walked off the front of shuttles, escaped strikes into walls and lost the core to a shockwave. The fixes are driver rules, listed in `captures/CAPTURE.md`: stop on completion, stay centred on the deck, escape only along free floor, jump the ring earlier.
- The pause menu could not be driven by clicks (R-01), so the driver uses arrows and Enter. R and N are shown failing while paused (R-02), then the menu entries are used.
- The level 6 bridge gap was unreachable, so the cell is dropped where the driver stands; the deliberate fall moved to level 12.
- The first 9:16 GDD film cropped gameplay to a 4:3 window, which cut the HUD. It was discarded, and all three verticals were rebuilt with the whole frame.
- One gamedev portrait code card (B07, `player.gd` 118–131) overflowed the frame. Long code lines are now set smaller (down to 104 px) before anything is dropped, so every portrait code card keeps all its source lines.
- Two walkthrough clip windows sat on an edge frame of a feature and were moved by one frame, and repeated beat IDs in the tail of two films were renumbered.

**Unverified:**

- No human playtest.
- The Windows export was never run.
- These were not captured: right mouse to shift and left mouse to pick up (Q and F were used), pad A, RB, LT and Start, changing an option value, F11 / Alt+Enter, Exit, death by a guardian strike, a shockwave knocking the core loose, and the focus-loss pause.
- Game audio was not captured; the films carry narration only.
- One assertion label in `defeat` says "Gino" (left over from the previous game's driver); it means the player.
- YouTube 4K processing has not been checked.

## Reproduce

| Item | Value |
|---|---|
| Brutalist version | brutalist.art at `a99b532`, Remotion 4.0.535 (the toolkit reports 4.0.544 as latest; not upgraded for this build) |
| Game source | `delta-godot-completed/` (not a git repo), snapshot `build_id 25e03b23048ef709f1aa800e57e3103a9b8beef85f54d003c4cda363f539bc13` (572 files, re-verified unchanged after the renders; method in `captures/CAPTURE.md`); Godot 4.7.2.stable.official.ed1daf0bf |
| Captures | `captures/CAPTURE.md` (method, isolated copy, seeds, driver rules), `capture_driver.gd` (built from `core.gd` + `takes.gd` by `assemble.sh`), `run_take.sh`, `record_all.sh`, input logs `*-inputs.jsonl`, run logs `*-run.log`. The capture MP4s (about 6.9 GB) stay in the local working folder `youtube/delta-captures/takes/`; their hashes are in `CAPTURE.md` |
| Each film | `make_sheet.py` (author → Kokoro → finish), then `BUILD-PROMPT.md`. Verticals: `captures/make_vertical_all.sh gdd\|walkthrough\|gamedev` |
| Checks | `./art godot-gdd --check` PASS (16 sections, 14 excerpts) · `godot-waikthrough --check` PASS (51 features, 8 not exercised) · `godot-gamedev --check` PASS (538 files, 13 code→result pairs). GATE T PASS and Gate V clean on all six masters; frames reviewed by eye |
| Approvals | none claimed; every GDD section is PENDING |

## Watch and review

| Video | Drive link | Size | Duration | SHA-256 |
|---|---|---|---|---|
| GDD, landscape (`delta-gdd_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 380.9 s | `eb47375f4eb57ea6b6af58eac2f610f38ef197d7c884c9d6624892c2ef60d635` |
| Walkthrough, landscape (`delta-walkthrough_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 699.1 s | `d633d1b680e62b33adfcc926d9b0a5dd0747e2ac2ff6c8ac41f365a0fbeea7cd` |
| Gamedev, landscape (`delta-gamedev_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 370.1 s | `312deb9c3cbaa1bde0788294ce3d2453b9ae1a1f4b717f1cf8cb929b0b756a06` |
| GDD, vertical (`delta-gdd_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 380.9 s | `9d6b94282e86236f7de30b0572f757d5908f9f4fd2758b7ee1c5658720f03380` |
| Walkthrough, vertical (`delta-walkthrough_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 699.1 s | `91c4167129df7d5f772d13fce87df9119f6272ab3c43311ebc5115d1bf169ad7` |
| Gamedev, vertical (`delta-gamedev_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 370.1 s | `859a1fc054d216ece9638ed8363c7d55c3b7f6299067e0c384ea90c8b4d407e6` |

**How the verticals were made.** They are native 9:16, not crops of the landscape films. Narration and timing are identical to landscape.

- **Gameplay:** re-cut in portrait from the same source frames. Every clip keeps the whole 16:9 engine frame at full width (2160×1215), with the disclosure above and the input log below.
  - A centred 4:3 window was tried first and rejected after frame review. Delta's HUD sits at the frame edges (objective top-left, layer top-right, held item bottom-right), and the crop cut the objective mid-word.
- **Boards and code panels:** redrawn as large-type portrait cards (`captures/portrait_cards.py`, `make_vertical_cards.py`). Quotes are verified verbatim against the GDD, and code lines are exact source lines.
- **Composer, writer and outro:** the toolkit's 916 compositions.

| Review step | Status |
|---|---|
| PM review | pending |
| YouTube 4K processing check | pending upload |
| Professors' publication decision | pending |
