# CAPTURE.md — Stage Runner film captures

This is the shared gameplay evidence for three films:

- `claude-liam-stage-runner-gdd`
- `claude-liam-stage-runner-walkthrough`
- `claude-liam-stage-runner-gamedev`

**These are scripted-input captures, not human playtests.** A driver played the game. No person judged whether it is fun, fair or readable.

## Build under capture

| Field | Value |
|---|---|
| Game | `stage-runner/stage-runner-godot-completed/` (not a git repository) |
| Snapshot | 146 files: everything except `builds/` and `.godot/`; listed in `build-files.txt` |
| `build_id` | `d90fa194817a81e9dae3223ce3d7495d326226fc94fb3a8993cd69724c136aeb` |
| Engine | Godot 4.7.2.stable.official.ed1daf0bf, Compatibility renderer |
| Machine | Apple M4, macOS |
| Exports | macOS `.app` boots headless for 300 frames, exit 0 (`export-boot.log`). SHA-256 prefixes: `c59bacf547ba1c09` (`Stage Runner.pck`), `41df79fbf79373d3` (`Stage Runner.exe`). The Windows `.exe` was not run |

**How `build_id` is computed:**

1. Sort the snapshot files by POSIX path.
2. Feed each one into one SHA-256 as `path NUL sha256(file) LF`.

## The isolated copy

The game folder was never modified. It was copied to a scratch folder, and only harness settings were changed there. `capture-project.diff`:

- **Own save folder:** `custom_user_dir_name="stage-runner-filmcapture"`.
  - The game writes its best score and sound setting to `user://stage_runner.cfg`. The captures never touch your real save.
  - The folder was emptied before the campaign take.
- **Window:** 3840×2160, `borderless`, `always_on_top`. Nothing else: no script, scene, asset or tuning value was changed.
- **Focus:** the window takes focus, and the machine was left alone while recording. The game pauses itself when its window loses focus (`game.gd:608`). An earlier pilot with a no-focus window paused at frame 180, and two more stopped drawing when the window was covered. All three pilots were discarded.

**The game's own test,** re-run on this copy: `_tools/playtest.tscn` PASS in 160 simulated seconds (`playtest.log`). It steers the player through the test-only `autopilot` hook in `player.gd`. The captures below do not use that hook.

## Method

**Driver.** `capture_driver.gd` is a `SceneTree` script, concatenated from `core.gd` and `takes.gd` by `assemble.sh`:

- It boots `run/main_scene` and plays only through `Input.parse_input_event`: key presses, mouse motion and buttons, and joypad axis and button events.
- It reads game state (positions of the player, monsters, fireballs and pickups; scene; menus) to decide what to press, and asserts outcomes.
- It never writes game state, never calls game methods and never teleports.

**Autopilot.** The steering is a port of the game's own playtest look-ahead dodge:

- It lines up under the most urgent monster, or under a falling pickup.
- It tries nine headings, simulates 0.35 s ahead against monsters and fireballs, and keeps the safest.
- The chosen heading is turned into held keys (WASD or the arrows), or into left-stick values in the gamepad segment.
- Fire is held throughout, except where a segment shows another fire input or deliberately does not shoot.

**Deliberate contacts.** In `defeat` and in one `extras` segment, the driver steers into the nearest monster without firing, to show hits and game over. These are labelled in the films.

**Randomness.** Before booting the game, the driver seeds Godot's global RNG, which the game uses for spawn positions, monster choice and drops. Combined with `--fixed-fps 30`, this makes each take reproducible.

| Take | Seed | Why this seed |
|---|---|---|
| `campaign` | 1 | the first seed tried; it clears all three stages |
| `defeat` | 1 | the first seed tried |
| `extras` | 2 | chosen from 40 headless trial runs because a heart drops after the deliberate hit (seeds 2, 4, 10, 23, 27 and 39 do) |

A headless trial and a windowed run of `extras` with seed 2 produced identical input logs, line for line.

**Clock.** `--fixed-fps 30`: each frame is exactly 1/30 s of game time. Nothing is retimed.

**Pixels.**
- After every draw, the driver reads `root.get_texture().get_image()`: the engine's own render at 3840×2160. The 1280×720 logical view is drawn at 3× by `canvas_items` stretch.
- Frames go to raw 150-frame chunks. `run_take.sh` encodes each chunk with x264 (crf 12), then joins them.

**Cursor.** The OS cursor is not part of the viewport texture. The driver draws a white arrow on its own CanvasLayer where its mouse is, and fades it out after 2 s without movement.

**Audio.** Game audio was not captured. The films carry narration only, and say so on screen.

**Drawing watchdog.** macOS stops drawing a covered window while game logic keeps running. The driver aborts any take where no frame is drawn for 60 iterations, and `record_all.sh` retries it.

## Takes

The three takes are independent; each starts from the main menu, and the campaign starts from an empty save folder.

| Take | Frames | Length | Assertions | mp4 sha256 |
|---|---|---|---|---|
| `campaign` | 4,549 | 151.6 s | 23 / 23 | `a905a6015c4f5d9fa23b5439bdba915365a07a8f8c9930f9fabe37a56647f883` |
| `defeat` | 877 | 29.2 s | 14 / 14 | `8cc5f78dbf699f9b48c9599f0b763b72b16a063632b8da0caa51c163937480e3` |
| `extras` | 2,176 | 72.5 s | 25 / 25 | `c248b6dc136bc3e02449cd37ee35f7f45196bda04ac13e3ac1c52b708d1cc26a` |

**`campaign`** (seed 1), keyboard:
- Main menu (BEST SCORE 0) → How to Play → `Esc` back → Start Game.
- **Stage 1**, WASD + hold `J`, with `Shift` focus held for 3 s near the start. Two triple shots collected. Cleared at exactly 2000 points in 30.9 s of play (frames 411–1338), 18 monsters, no hits.
- Stage Clear card → Go to Stage 2.
- **Stage 2**, arrow keys + hold `Space`. Three triple shots collected. Cleared at 4050 in 38.3 s (frames 1648–2796), no hits.
- Stage Clear card → Go to Stage 3.
- **Stage 3**, WASD + `J`. The Cerberus enters at frame 3106 and starts attacking at 3184; it is enraged at 55 HP (frame 3739). It is defeated at frame 4019, 30.4 s after GO, with a stage score of 6200 and no hits.
- Credits roll and stop: final score 12250, 58 monsters, best 12250 → Main Menu, which now shows BEST SCORE 12250.

**`defeat`** (seed 1):
- Start Game. The driver steers into monsters without firing: hits at frames 209 and 257, the third at 319.
- GAME OVER with the crying face, `Score: 0 /2000`, the tree paused → Try Again: stage 1 restarts with score 0 and 3 lives.
- 5 s of play, `Esc` → PAUSED → Main Menu.

**`extras`** (seed 2):
- Main menu Audio On → Audio Off → Audio On.
- Start Game. Arrow keys + `Z`, then the left mouse button held as fire.
- `M` (Sound: Off) and `M` again.
- `P` → PAUSED → pause-menu Audio On → Audio Off → Resume.
- `Esc` → `R`: the stage restarts. The game logs `SCRIPT ERROR: Cannot call method 'set_input_as_handled' on a null value` at `game.gd:606` (`extras-run.log`).
- Synthetic gamepad: the left stick steers, A fires, LB focuses, Start pauses and resumes.
- One deliberate monster contact (frame 1459, 2 lives). Then normal play: a triple shot drops at 1810 (collected 1904), and a heart drops at 1958 and is collected at 1994, restoring the third life. `Esc` → Main Menu.
- Note on the log: in this last segment the driver re-enters its play loop every 30 frames, so its `pickup_dropped` and `triple_shot_collected` notes repeat while a pickup or triple shot is active. The game-state snapshot on every line is authoritative; the assertions are unaffected.

62 of 62 assertions pass across the three takes.

## Not captured

- F11 / Alt+Enter fullscreen (it would change the fixed capture window).
- The Quit button on the main menu.
- Play Again on the credits screen.
- Game over in the boss stage (its "The Cerberus still guards the gate." line).
- The focus-loss auto-pause as a demonstration (seen only in a discarded pilot).
- Game audio.
