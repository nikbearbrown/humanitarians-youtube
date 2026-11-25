# Gino: Knife Throw — three films — Yeshwanth Balaji

Three films about **Gino: Knife Throw**. It is a Godot 4.7.2 rebuild of a Unity 2D action platformer that arrived with scripts and art but no levels, scenes or sound; the rebuild adds three designed levels, synthesized audio and the full menu flow. Each film was made with a Brutalist Godot skill, run with the `walker` modifier.

| Film | Skill | Landscape | Vertical |
|---|---|---|---|
| Gino: Knife Throw, The Design Document Came Last | godot-gdd walker | 3840×2160, 6:14 | 2160×3840 |
| Gino: Knife Throw, Every Feature, Played | godot-waikthrough walker | 3840×2160, 7:03 | 2160×3840 |
| Gino: Knife Throw, Inside the Godot Code | godot-gamedev walker | 3840×2160, 6:27 | 2160×3840 |

This folder is the recipe only: the GDD, scripts and records. The videos are on Drive.

## This week's contribution

**Question.** What does the finished game actually do, how is it built, and what would its design document say? Can the films show that honestly, with no human playtest done yet?

**Built.**

- **Verified the game in the engine.**
  - The game's own playtest passes on an isolated copy: all three levels and the credits (enemies removed), then 18 mechanics checks, in 121 simulated seconds.
  - The exported macOS app boots headless with exit 0.
  - The Windows `.exe` was not run.
- **Three scripted-input captures of the real build,** at native 4K, 30 fps, with every enemy present. They were played only through key, mouse and gamepad events: no teleports and no game method calls. 46 of 46 assertions pass.
  - `campaign`: menu, How to Play, all three levels, the credits, and Continue (Level 3) with the saved best score.
  - `defeat`: pause and resume, real fights, a deliberate pit death, GINO IS DOWN, Retry, R restart, Main Menu.
  - `extras`: the menu Sound button, arrow keys, M, and a simulated gamepad (stick, A, Start).
- **`GDD.md`,** written after the game from the Unity scripts, the Godot project and the captures. Every claim is labelled SOURCE / AUTHORED / IMPLEMENTED / OBSERVED / PROPOSED / PENDING, and nothing is signed off.
- **Three films,** each pairing claims with real engine footage of the same build (`build_id cffbb01`).
  - The walkthrough shows 47 features and lists the 8 it did not exercise.
  - The gamedev film pairs 12 verbatim code excerpts with the result each one produces.

**Observed.** The captures and source reading found things a quick play would miss:

- **R-01, a hole in level 3's second rope bridge.** The `B` in the map sits at column 91, so the 7-tile span covers columns 91–97, but the pit runs 92–98. That leaves a 16 px gap at x 1568–1584 over the spikes. The routes jump it, so `_tools/levels.py` passes, but a trial run fell through it after a bat's knockback. Moving the `B` one column right closes it. Not fixed: the game folder was not modified.
- **R-02, a script error on restart.** R on the pause menu restarts the level, but Godot logs `SCRIPT ERROR: Cannot call method 'set_input_as_handled' on a null value` at `level.gd:761`. `_restart()` has already changed the scene (`captures/defeat-run.log`).
- **The four-hit combo never appears on screen.** The autopilot's J presses chain at most two hits, because each hit knocks the enemy back out of reach. The game's own playtest checks the full chain.
- **Walkers bite on landing.** A walker waiting below a drop bites Gino while he is still in the air. The autopilot needed its own rules to leap past or land short (GDD R-06, OQ-04).
- **Level 3 is close.** The script cleared it on one half heart: floor spikes, a walker bite, a plant snap. Levels 1 and 2 were cleared without a hit.
- **Built in code.** `level_1.tscn` is 7 lines; 8 seconds in, the level holds 200 live nodes (`captures/tree_probe.txt`).
- **Authored values.** Unity's prefabs were not delivered, so enemy health (100), points (25) and the 40-damage finisher are the rebuild's choices.

**Next experiment.** A human playtest of the four proposed experience goals (GDD §5), starting with PX-04 ("Moonlit Depths feels like a finale, not a wall").

## Human and AI work

**My decisions:**

- the game, and the request for the same three-film set as the earlier submissions;
- that the game is not modified;
- the Liam / @NikBearBrown narration, as in the Stage Runner films;
- where the films and submissions go, and that nothing is published from the toolkit.

**AI tools and voices:**

- Claude (Claude Code) wrote the GDD, the capture driver, beat sheets, narration and these records, and ran the renders.
- Narration is the AI voice "Liam" (Kokoro `am_onyx`, local), named in the narration. It is not a recording of me.

**Rejected or corrected during the build:**

- Early autopilot versions died in levels 2 and 3. The fixes are driver rules, listed in `captures/CAPTURE.md`: leap past or drop short of a waiting walker, don't wait for a walker across a gap, steer back onto rock rims, never walk off footing while fighting, retry a jump pressed during a slash, back off during a bat's wind-up.
- The extras take first failed its pad pause check: the pad run reached a hint sign. The take now closes the hint with pad A first.
- The input log names the nearest enemy when Gino is hurt, so it labels the first level 3 hit "bat". The frame shows floor spikes; the films and records say spikes.
- Narration was rewritten to fit each clip after the first Kokoro pass, and two clip windows were moved so they need no held frames. One walkthrough clip (B04) still ends on 0.4 s of held frame, labelled HELD FRAME on screen.

**Unverified:**

- No human playtest.
- The Windows export was never run.
- These were not captured: the four-hit combo and magic blast, the jump attack, heart pickups, X / C and the pad slash and throw buttons in play, F11, Quit, and the focus-loss pause.
- Game audio was not captured; the films carry narration only.
- YouTube 4K processing has not been checked.

## Reproduce

| Item | Value |
|---|---|
| Brutalist version | brutalist.art at `a99b532`, Remotion 4.0.535 (the toolkit reports 4.0.542 as latest; not upgraded for this build) |
| Game source | `knife-throw-platformer-godot-completed/` (not a git repo), snapshot `build_id cffbb010b53686c92517a8df047786352e12f582137033b3caa1283f0be7bddc` (307 files; method in `captures/CAPTURE.md`); Godot 4.7.2.stable.official.ed1daf0bf |
| Captures | `captures/CAPTURE.md` (method, isolated copy, seeds, driver rules), `capture_driver.gd` (built from `core.gd` + `takes.gd` by `assemble.sh`), `run_take.sh`, `record_all.sh`, input logs `*-inputs.jsonl`, run logs `*-run.log`. The capture MP4s (about 200 MB) stay in the local working folder `youtube/knife-throw-captures/takes/`; their hashes are in `CAPTURE.md` |
| Each film | `make_sheet.py` (author → Kokoro → finish), then `BUILD-PROMPT.md`. Verticals: `captures/make_vertical_all.sh gdd\|walkthrough\|gamedev` |
| Checks | `./art godot-gdd --check` PASS (16 sections, 13 excerpts) · `godot-waikthrough --check` PASS (47 features, 8 not exercised) · `godot-gamedev --check` PASS (290 files, 12 code→result pairs). GATE T PASS and Gate V clean on all six masters; frames reviewed by eye |
| Approvals | none claimed; every GDD section is PENDING |

## Watch and review

| Video | Drive link | Size | Duration | SHA-256 |
|---|---|---|---|---|
| GDD, landscape (`knife-throw-gdd_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 373.8 s | `ccf87fbf28df6216fa8cecf31559cb1f7ea47fd41ed1ff6e08b5ed246d8802a2` |
| Walkthrough, landscape (`knife-throw-walkthrough_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 422.8 s | `0fe5f55035a354851aa4e31945a32a781d031f2c3fa1a5af70ec5d873600ac1d` |
| Gamedev, landscape (`knife-throw-gamedev_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 387.3 s | `4cedf556ff2315d6d9a427929df9d1b8e2b6f46dabe4a1cf03ca452432f9166d` |
| GDD, vertical (`knife-throw-gdd_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 373.8 s | `c544d1fd628e9ec48b11751cbadd380cbffb69b5706781227b532152307eed57` |
| Walkthrough, vertical (`knife-throw-walkthrough_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 422.8 s | `8d1486fa9d0e8aec55784baa8e6b40c0d8814c27c8b62b0c994a3c905ad9077e` |
| Gamedev, vertical (`knife-throw-gamedev_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 387.3 s | `0163b1895880df769261283c6834d1edad165b0d7b579b8a14d0262a874ae399` |

**How the verticals were made.** They are native 9:16, not crops of the landscape films. Narration and timing are identical to landscape.

- **Gameplay:** re-cut in portrait from the same source frames.
  - In-level clips show a 4:3 window of the game view (logical x 64–1024) at full width, keeping the hearts, score and Gino. They are labelled on screen as a crop of the right quarter.
  - Clips that touch the main menu, How to Play or the credits keep the whole 16:9 frame.
- **Boards and code panels:** redrawn as large-type portrait cards (`captures/portrait_cards.py`, `make_vertical_cards.py`). Quotes are verified verbatim against the GDD, and code lines are exact source lines.
- **Composer, writer and outro:** the toolkit's 916 compositions.

| Review step | Status |
|---|---|
| PM review | pending |
| YouTube 4K processing check | pending upload |
| Professors' publication decision | pending |
