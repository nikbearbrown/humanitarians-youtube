# Stage Runner — three films — Yeshwanth Balaji

Three films about **Stage Runner**. It is a Godot 4.7.2 rebuild of a two-stage Unity vertical shooter, finished with lives, drops and a third boss stage. Each film was made with a Brutalist Godot skill, run with the `walker` modifier.

| Film | Skill | Landscape | Vertical |
|---|---|---|---|
| Stage Runner: The Design Document Came Last | godot-gdd walker | 3840×2160, 5:54 | 2160×3840 |
| Stage Runner: Every Feature, Played | godot-waikthrough walker | 3840×2160, 5:23 | 2160×3840 |
| Stage Runner: Inside the Godot Code | godot-gamedev walker | 3840×2160, 6:36 | 2160×3840 |

This folder is the recipe only: the GDD, scripts and records. The videos are on Drive.

## This week's contribution

**Question.** What does the finished game actually do, how is it built, and what would its design document say? Can the films show that honestly, with no human playtest done yet?

**Built.**

- **Verified the game in the engine.**
  - The game's own playtest passes on an isolated copy: all three stages, the credits, game over, retry and pause, in 160 simulated seconds.
  - The exported macOS app boots (headless, 300 frames, exit 0).
  - The Windows `.exe` was not run.
- **Three scripted-input captures of the real build,** at native 4K, 30 fps. They were played only through key, mouse and gamepad events: no teleports and no game method calls. 62 of 62 assertions pass.
  - `campaign`: menu, How to Play, stages 1 and 2, the Cerberus, the credits and the saved best score.
  - `defeat`: deliberate monster contacts, game over, Try Again, pause.
  - `extras`: audio buttons, every fire input, M, P, Esc and R, a simulated gamepad, and a heart drop after one deliberate hit.
- **`GDD.md`,** written after the game from the Unity scripts, the Godot project and the captures. Every claim is labelled SOURCE / AUTHORED / IMPLEMENTED / OBSERVED / PROPOSED / PENDING, and nothing is signed off.
- **Three films,** each pairing claims with real engine footage of the same build (`build_id d90fa19`).
  - The walkthrough shows 40 features and lists the 6 it did not exercise.
  - The gamedev film pairs 14 verbatim code excerpts with the result each one produces.

**Observed.** The captures and source reading found things a quick play would miss:

- **R-01, a script error on restart.** Pressing R on the pause menu restarts the stage, but Godot logs `SCRIPT ERROR: Cannot call method 'set_input_as_handled' on a null value` at `game.gd:606`. `_restart()` has already changed the scene, so the next line has no viewport (`captures/extras-run.log`).
- **R-04, a wrong comment.** The README and the comment in `enemy.gd` say monsters spawn within ±4.5 Unity units of centre. The code uses ±288 px, which is 4 units (4.5 × 72 = 324).
- **Focus pause.** The game pauses itself when its window loses focus (`game.gd:608`). A pilot capture was paused by it; the final captures kept the window focused.
- **Goals and roster are authored.** Unity's goal score and per-monster values lived in scene and prefab files that were not delivered. The 2000 and 4000 goals and all 13 monster types are the rebuild's choices.
- **Built in code.** `stage_1.tscn` is 7 lines; 8 seconds in, the stage holds 113 live nodes (`captures/tree_probe.txt`).
- **The autopilot never got hit** in the campaign: stage 1 in 30.9 s, stage 2 in 38.3 s and the boss in 30.4 s, all with 3 lives. A script that sees every position says nothing about difficulty for a person.

**Next experiment.** A human playtest of the four proposed experience goals (GDD §5), starting with PX-02 ("stage 2 feels like a step up, not a wall").

## Human and AI work

**My decisions:**

- the game, and the request for the same three-film set as the fantasy survival submission;
- that the game is not modified;
- where the films and submissions go, and that nothing is published from the toolkit.

**AI tools and voices:**

- Claude (Claude Code) wrote the GDD, the capture driver, beat sheets, narration and these records, and ran the renders.
- Narration is the AI voice "Liam" (Kokoro `am_onyx`, local), named in the narration. It is not a recording of me.

**Rejected or corrected during the build:**

- A capture window that did not take focus was paused by the game itself; two more pilots stopped drawing when the window was covered. All three were discarded.
- Each take uses a fixed RNG seed so it is reproducible. The `extras` seed was chosen from 40 trial runs because a heart drops in it (`captures/CAPTURE.md`).
- Three GDD-film narration claims were corrected against the code before recording audio: the hitbox size (radius 13, not 13 px across), the invulnerability time (1.6 s), and a line naming monster types the footage could not show. One GDD clip was extended so the game-over menu it narrates is on screen.
- Seven gamedev code panels were clipped at the bottom. Four were re-rendered at a smaller size; three had their excerpts trimmed by a few lines so every highlighted line is visible.
- In the verticals, two portrait code cards were pinned to the lines that matter: B19 to the scene change, and B27 to the failing line 606. The whole-frame menu clips were re-laid out after the visual check flagged them as underfilled.

**Unverified:**

- No human playtest.
- The Windows export was never run.
- These were not captured:
  - F11 fullscreen, Quit and Play Again;
  - game over in the boss stage;
  - the focus-loss pause, except in a discarded pilot.
- Game audio was not captured; the films carry narration only.
- YouTube 4K processing has not been checked.

## Reproduce

| Item | Value |
|---|---|
| Brutalist version | brutalist.art at `a99b532` |
| Game source | `stage-runner-godot-completed/` (not a git repo), snapshot `build_id d90fa194817a81e9dae3223ce3d7495d326226fc94fb3a8993cd69724c136aeb` (146 files; method in `captures/CAPTURE.md`); Godot 4.7.2.stable.official.ed1daf0bf |
| Captures | `captures/CAPTURE.md` (method, isolated copy, seeds, overlays), `capture_driver.gd` (built from `core.gd` + `takes.gd` by `assemble.sh`), `run_take.sh`, `record_all.sh`, input logs `*-inputs.jsonl`, run logs `*-run.log`. The capture MP4s (448 MB) stay in the local working folder `youtube/stage-runner-captures/takes/`; their hashes are in `CAPTURE.md` |
| Each film | `make_sheet.py` (author → Kokoro → finish), then `BUILD-PROMPT.md`. Verticals: `captures/make_vertical_all.sh gdd\|walkthrough\|gamedev` |
| Checks | `./art godot-gdd --check` PASS (16 sections, 12 excerpts) · `godot-waikthrough --check` PASS (40 features, 6 not exercised) · `godot-gamedev --check` PASS (129 files, 14 code→result pairs). GATE T PASS and Gate V clean on all six masters; frames reviewed by eye |
| Approvals | none claimed; every GDD section is PENDING |

## Watch and review

| Video | Drive link | Size | Duration | SHA-256 |
|---|---|---|---|---|
| GDD, landscape (`stage-runner-gdd_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 353.7 s | `76e17c51ca045c0c2a1f786f392cff1c89a318069cf53a64963284030ae7f74f` |
| Walkthrough, landscape (`stage-runner-walkthrough_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 323.4 s | `79635c7488ce32253d45fdc223d1852a81db9592e83e1e107b1b8f9d3d17c01d` |
| Gamedev, landscape (`stage-runner-gamedev_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 396.2 s | `8156d0b4d17a842d3b88a1a67dead9e2c19477f2dee9dc566c0947dd9b0b9a95` |
| GDD, vertical (`stage-runner-gdd_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 353.7 s | `a4870fd163505fb70522c38c0dee013ce78438347c62be83da09158c3a03689e` |
| Walkthrough, vertical (`stage-runner-walkthrough_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 323.4 s | `f3be614932762c600e402c869aa1decca450988acfb11d0e98860d7701bc91bd` |
| Gamedev, vertical (`stage-runner-gamedev_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 396.2 s | `4569500072451ee083d3e6e6db4713b67a39e1cbfbd721a96b7e4dc4a2ca5e56` |

**How the verticals were made.** They are native 9:16, not crops of the landscape films. Narration and timing are identical to landscape.

- **Gameplay:** re-cut in portrait from the same source frames.
  - Stage, pause, game-over, clear and credits clips show the centre 640 px column of the game view (the street) at full width, labelled on screen as a crop of the side panels.
  - Clips that touch the main menu or How to Play keep the whole 16:9 frame.
- **Boards and code panels:** redrawn as large-type portrait cards (`captures/portrait_cards.py`, `make_vertical_cards.py`). Quotes are verified verbatim against the GDD, and code lines are exact source lines.
- **Composer, writer and outro:** the toolkit's 916 compositions.

| Review step | Status |
|---|---|
| PM review | pending |
| YouTube 4K processing check | pending upload |
| Professors' publication decision | pending |
