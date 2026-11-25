# Night Yard — three films — Yeshwanth Balaji

Three films about **Night Yard**. It is a Godot 4.7.2 rebuild of a Unity 2.5D platformer that arrived with scripts and art but no scenes, levels or sound. The rebuild adds six designed levels, a boss, synthesized audio and the full menu flow. Each film was made with a Brutalist Godot skill, run with the `walker` modifier.

| Film | Skill | Landscape | Vertical |
|---|---|---|---|
| Night Yard: The Design Document Came Last | godot-gdd walker | 3840×2160, 6:07 | 2160×3840 |
| Night Yard, Every Feature, Played | godot-waikthrough walker | 3840×2160, 7:51 | 2160×3840 |
| Night Yard: Inside the Godot Code | godot-gamedev walker | 3840×2160, 6:15 | 2160×3840 |

This folder is the recipe only: the GDD, scripts and records. The videos are on Drive: [Night Yard films](https://drive.google.com/drive/folders/1CkaEl8Rk8RBIMQMs8w6h9TdXL1yRku5J?usp=sharing).

## This week's contribution

**Question.** What does the finished game actually do, how is it built, and what would its design document say? Can the films show that honestly, with no human playtest done yet?

**Built.**

- **Verified the game in the engine.**
  - The game's own playtest passes on an isolated copy: all six levels in 418 simulated seconds.
  - The exported macOS app boots headless with exit 0.
  - The Windows `.exe` was not run.
- **Three scripted-input captures of the real build,** at native 4K and 30 fps of game time (engine at 60 fps, every second frame saved). 78 of 78 assertions pass.
  - The game's own bot brain decides the moves, as in its playtest, but it is kept off the player. Its decisions go to the game as real key presses through `Input.parse_input_event`, so the player reads input exactly as in a person's game.
  - Menus are clicked with the mouse; the move showcase and the gamepad are scripted directly.
  - `campaign`: menu, How to Play, the character select, all six levels, the Forewoman and the credits.
  - `defeat`: a fall into a pit, a spike-plate death, pause and the R restart, and the options defect below.
  - `extras`: options, the character select by keys, a move showcase (jab, cross, uppercut, block, hammer, slide) and a gamepad.
- **`GDD.md`,** written after the game from the Unity scripts, the Godot project and the captures. Every claim is labelled SOURCE / AUTHORED / IMPLEMENTED / OBSERVED / PROPOSED / PENDING, and nothing is signed off.
- **Three films,** each pairing claims with real engine footage of the same build (`build_id 54ad5ab`).
  - The walkthrough shows 55 features and lists the 8 it did not exercise.
  - The gamedev film pairs 14 verbatim code excerpts with the result each one produces.

**Observed.** The captures and source reading found things a quick play would miss:

- **R-01: after Options in the pause menu, the pause key stops pausing.** `hud.gd` hides the options container on Back, but the panel inside it stays `visible`, and `options_panel.gd:52-55` checks its own `visible`. So every later Esc, P or Start is taken by the hidden panel: the pause panel reappears, but the game keeps running behind it (`defeat`, frame 2234).
- **R-02: at the character select, the arrow keys also move the button focus.** Right, Right, Left chose Green but left the focus on Back, so Enter returned to the menu and the choice was lost. The README says the arrows choose and Enter plays (`extras`, frame 505).
- **R-03: the double-tap run is timed on the wall clock** (`fighter.gd:266`), so it depends on the frame rate.
- **The boss is hard.** The game's own autopilot is K.O.'d 4 times by the Forewoman in its playtest, and 5 times in the film capture, before it wins.
- **The scripted run got stuck once.** In level 6 the player stood on a container for about a minute; the driver's stall guard restarted the level from the pause menu. The walkthrough shows the restart.
- **Built in code.** `level_01.tscn` is 7 lines; 8 seconds in, the level holds 385 live nodes (`captures/tree_probe.txt`).
- None of these were fixed: the game folder was not modified.

**Next experiment.** A human playtest of the four proposed experience goals (GDD §5), starting with PX-04 ("The Forewoman feels like a fight, not a wall").

## Human and AI work

**My decisions:**

- the game, and the request for the same three-film set as the earlier submissions;
- that the game is not modified;
- the Liam / @NikBearBrown narration, as in the earlier Godot films;
- where the films and submissions go, and that nothing is published from the toolkit.

**AI tools and voices:**

- Claude (Claude Code) wrote the GDD, the capture driver, beat sheets, narration and these records, and ran the renders.
- Narration is the AI voice "Liam" (Kokoro `am_onyx`, local), named in the narration. It is not a recording of me.

**Rejected or corrected during the build:**

- The first driver ran the engine at 30 fps, two physics ticks a frame. A one-tick jump press from the brain was lost (pressed and released inside one frame), and level 2's wall-jump shaft stalled in one trial in five. The bridge now holds each wanted key for at least a frame, and the takes run at 60 fps; five of five trials passed.
- In fast headless trials, a manual press right after the bridge's counted as a double tap, which turns on running. The driver pauses briefly in real time before its own presses.
- The first defeat plan (a K.O. by a yard bot) failed because the brain had already knocked both bots out; the campaign's boss fight shows the K.O. screen instead.
- The first walkthrough cut ran 10:41 with long silent stretches; the windows were re-sized to the narration (7:51).
- Carried over from the Delta build: a 4:3 portrait crop cuts a HUD at the frame edges, so these verticals show the whole engine frame from the start.

**Unverified:**

- No human playtest.
- The Windows export was never run.
- Not captured: Red and Green in play, the stomp, dragon punch, sweep and air smash by key, the mouse buttons for attack and block, the double-tap run, F11, Exit, changing an option value.
- Game audio was not captured; the films carry narration only.
- YouTube 4K processing has not been checked.

## Reproduce

| Item | Value |
|---|---|
| Brutalist version | brutalist.art at `3a6d397`, Remotion 4.0.535 (the toolkit reports 4.0.545 as latest; not upgraded for this build) |
| Game source | `inside-godot-completed/` (not a git repo), snapshot `build_id 54ad5ab3eab7d97e341b1ff7fc6f5aef0549e4819a46b9a0c7b2e4d0cdf9f550` (449 files, re-verified unchanged after the renders; method in `captures/CAPTURE.md`); Godot 4.7.2.stable.official.ed1daf0bf |
| Captures | `captures/CAPTURE.md` (method, isolated copy, seed, the bridge), `capture_driver.gd` (built from `core.gd` + `takes.gd` by `record_all.sh`), `run_take.sh`, input logs `*-inputs.jsonl`, run logs `*-run.log`, `clips.py`. The capture MP4s (about 4.3 GB) stay in the local working folder `youtube/inside-captures/takes/`; their hashes are in `CAPTURE.md` |
| Each film | `make_sheet.py` (author → Kokoro → finish), then `BUILD-PROMPT.md`. Verticals: `captures/make_vertical_all.sh gdd\|walkthrough\|gamedev` |
| Checks | `./art godot-gdd --check` PASS (16 sections, 15 excerpts) · `godot-waikthrough --check` PASS (55 features, 8 not exercised) · `godot-gamedev --check` PASS (426 files, 14 code→result pairs). GATE T PASS and Gate V clean on all six masters; frames reviewed by eye |
| Approvals | none claimed; every GDD section is PENDING |

## Watch and review

| Video | Drive link | Size | Duration | SHA-256 |
|---|---|---|---|---|
| GDD, landscape (`night-yard-gdd_yeshwanth_16x9.mp4`) | [Drive folder](https://drive.google.com/drive/folders/1CkaEl8Rk8RBIMQMs8w6h9TdXL1yRku5J?usp=sharing) | 3840×2160 | 367.1 s | `4e989639c885a06bf7421ff03a37c774580a43266beb262b4ce5584fe21818d9` |
| Walkthrough, landscape (`night-yard-walkthrough_yeshwanth_16x9.mp4`) | [Drive folder](https://drive.google.com/drive/folders/1CkaEl8Rk8RBIMQMs8w6h9TdXL1yRku5J?usp=sharing) | 3840×2160 | 471.0 s | `c2f622d1ff97ff50e0c5b98988148fc85efd4beea5d0f1bbc80477cbc184ad4b` |
| Gamedev, landscape (`night-yard-gamedev_yeshwanth_16x9.mp4`) | [Drive folder](https://drive.google.com/drive/folders/1CkaEl8Rk8RBIMQMs8w6h9TdXL1yRku5J?usp=sharing) | 3840×2160 | 375.2 s | `1b19e0ca1b7b1d9f256ed598963227153d13f3a0b19ea4042ac07ed49c30d0c3` |
| GDD, vertical (`night-yard-gdd_yeshwanth_9x16.mp4`) | [Drive folder](https://drive.google.com/drive/folders/1CkaEl8Rk8RBIMQMs8w6h9TdXL1yRku5J?usp=sharing) | 2160×3840 | 367.1 s | `406099297bdd828c211605ef0687e2dbdc327c28dc98f18f0b74a606a5094687` |
| Walkthrough, vertical (`night-yard-walkthrough_yeshwanth_9x16.mp4`) | [Drive folder](https://drive.google.com/drive/folders/1CkaEl8Rk8RBIMQMs8w6h9TdXL1yRku5J?usp=sharing) | 2160×3840 | 471.0 s | `535d260a565071013db70ec2d6d576c0d829239a6959363d54fd6a235190c2a2` |
| Gamedev, vertical (`night-yard-gamedev_yeshwanth_9x16.mp4`) | [Drive folder](https://drive.google.com/drive/folders/1CkaEl8Rk8RBIMQMs8w6h9TdXL1yRku5J?usp=sharing) | 2160×3840 | 375.2 s | `9a9cb87c19730181b3afb7aa4430554f350dee1a8be117b95b58650ca98de09b` |

**How the verticals were made.** They are native 9:16, not crops of the landscape films. Narration and timing are identical to landscape.

- **Gameplay:** re-cut in portrait from the same source frames. Every clip keeps the whole 16:9 engine frame at full width (2160×1215), with the disclosure above and the input log below.
- **Boards and code panels:** redrawn as large-type portrait cards (`captures/portrait_cards.py`, `make_vertical_cards.py`). Quotes are verified verbatim against the GDD, and code lines are exact source lines.
- **Composer, writer and outro:** the toolkit's 916 compositions.

| Review step | Status |
|---|---|
| PM review | pending |
| YouTube 4K processing check | pending upload |
| Professors' publication decision | pending |
