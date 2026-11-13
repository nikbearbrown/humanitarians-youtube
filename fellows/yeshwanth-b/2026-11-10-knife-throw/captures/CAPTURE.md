# CAPTURE.md — Gino: Knife Throw film captures

This is the shared gameplay evidence for three films:

- `claude-liam-knife-throw-gdd`
- `claude-liam-knife-throw-walkthrough`
- `claude-liam-knife-throw-gamedev`

**These are scripted-input captures, not human playtests.** A driver played the game. No person judged whether it is fun, fair or readable.

## Build under capture

| Field | Value |
|---|---|
| Game | `knife-throw/knife-throw-platformer-godot-completed/` (not a git repository) |
| Snapshot | 307 files: everything except `builds/` and `.godot/`; listed with their SHA-256 in `build-files.txt`. All 307 were unchanged after recording |
| `build_id` | `cffbb010b53686c92517a8df047786352e12f582137033b3caa1283f0be7bddc` |
| Engine | Godot 4.7.2.stable.official.ed1daf0bf |
| Machine | Apple Silicon Mac, macOS |
| Exports | macOS `.app` boots headless, exit 0 (`export-boot.log`). The Windows `.exe` was not run |

**How `build_id` is computed:**

1. Sort the snapshot files by POSIX path.
2. Feed each one into one SHA-256 as `path NUL sha256(file) LF`.

## The isolated copy

The game folder was never modified. It was copied to `capture/`, and only harness settings were changed there. `capture-project.diff`:

- **Own save folder:** `custom_user_dir_name="knife-throw-filmcapture"`. The game writes progress, best score and the sound setting to `user://knife_throw.cfg`; the captures never touch your real save. The folder was emptied before the campaign take.
- **Window:** 3840×2160, `borderless`, `always_on_top`. Nothing else: no script, scene, asset or tuning value was changed.
- **Focus:** the window takes focus, and the machine was left alone while recording. The game pauses itself when its window loses focus (`level.gd:763`).

**The game's own test,** re-run on this copy: `_tools/playtest.tscn` PASS in 121 simulated seconds (`playtest.log`). It removes enemies for its route phase and steers Gino through the test-only `autopilot` hook in `player.gd`. The captures below do not use that hook, and keep every enemy.

## Method

**Driver.** `capture_driver.gd` is a `SceneTree` script, concatenated from `core.gd` and `takes.gd` by `assemble.sh`:

- It boots `run/main_scene` and plays only through `Input.parse_input_event`: key presses, mouse motion and buttons, and joypad axis and button events.
- It reads game state (Gino, enemies, the level grid, menus) to decide what to press, and asserts outcomes.
- It never writes game state, never calls game methods and never teleports.

**Autopilot.** Gino follows the game's own door routes (`_tools/routes.json`, written by `_tools/levels.py`), edge by edge: walk segments and timed jumps. On top of that, the driver's own rules, all in `takes.gd`:

- **Fighting:** stand and let a walker or bat come into sword range (they chase slower than Gino runs), slash with J inside about 38 px, back off inside about 30 px, and keep pressing J during a swing to try to chain. Plants are never fought in melee: their snap outreaches the sword. Knives are thrown at enemies more than 64 px away on the same height.
- **Bats:** back off during the 0.7 s wind-up, then slash.
- **Guarded descents:** where a walker waits on the floor a jump drops to, the driver leaps long past it (`leap`) or steps off the rim to land short (`drop`), so the walker must walk into sword range. A walker across a gap is not waited for.
- **Footing:** fighting never walks Gino off his footing; a landing on a rock rim steers back onto it; a jump pressed during a slash is retried.

These rules were tuned in headless trials (`trial/`). They are why the takes survive, and they are not part of the game.

**Randomness.** The driver seeds Godot's global RNG before booting (seed 1 for every take). Combined with `--fixed-fps 30`, runs are close to reproducible but not identical: the windowed takes start one frame earlier than the headless trials and drift a little later on (the level 3 walker bite lands at frame 5329 headless, 5366 windowed). The same levels clear with the same health.

**Clock.** `--fixed-fps 30`: each frame is exactly 1/30 s of game time. Nothing is retimed.

**Pixels.**
- After every draw, the driver reads `root.get_texture().get_image()`: the engine's own render at 3840×2160. The 1280×720 logical view is drawn at 3× by `canvas_items` stretch.
- Frames go to raw 150-frame chunks. `run_take.sh` encodes each chunk with x264 (crf 12), then joins them.

**Cursor.** The OS cursor is not part of the viewport texture. The driver draws a white arrow on its own CanvasLayer where its mouse is, and fades it out after 2 s without movement.

**Audio.** Game audio was not captured. The films carry narration only, and say so on screen.

**Drawing watchdog.** The driver aborts any take where no frame is drawn for 60 iterations; `record_all.sh` retries it. No take stalled.

## Takes

The three takes are independent; each starts from the main menu, and the campaign starts from an empty save folder. All three were recorded on the first attempt.

| Take | Frames | Length | Assertions | mp4 sha256 |
|---|---|---|---|---|
| `campaign` | 7,686 | 256.2 s | 20 / 20 | `521355573357844c033661208950a3801b2de9919174547ac7e69038ed0567eb` |
| `defeat` | 1,973 | 65.8 s | 15 / 15 | `3eea6e75fa6028061b900cef0ad9cb27d8f661934766b62ae9ba92808cc155ab` |
| `extras` | 807 | 26.9 s | 11 / 11 | `4c9581a06bc60ccd8fe1bf92007faf9248837d94ef0224c3859c1f13562aee91` |

**`campaign`**, keyboard (A / D, Space, J, K, W, Enter):
- Main menu (best score 0) → How to Play → `Esc` back → New Game.
- **Level 1, Rocky Outskirts:** five hints closed with Enter; walker, bat and walker defeated (frames 833, 1307, 1741); one knife picked up (1299) and thrown (1610); plants passed. Door at 1996, no hits. Panel: 135 points, diamonds 6/10, enemies 3/5, 0:43.
- **Level 2, Thorn Hollow:** a `leap` past the walker under the rock (2400), a `drop` off the cliff (3521); five enemies defeated; no hits. Door at 3912. Panel: 470, 17/22, 5/7, 0:53.
- **Level 3, Moonlit Depths:** nine enemies defeated. Three hits: floor spikes at 4816 (6 → 5; the log's nearest-enemy label says "bat", the frame shows the spikes), a walker bite at 5366 (5 → 3), a plant snap at 6368 (3 → 1). Door at 6694 on health 1. Panel: 805, 7/19, 9/12, 1:19.
- Finish → credits (THE END, run totals) → the main menu, now with Continue (Level 3) and best score 805.

**`defeat`**:
- New Game. `Esc` → PAUSED (Resume, Restart, Sound, Main Menu) → Resume.
- Plays the start of level 1 with real fights (single slashes and two-hit chains).
- Runs Gino into the first pit on purpose (fall at 1443, dead at 1487): GINO IS DOWN → Retry restarts level 1 with full health.
- `Esc` → `R`: the level restarts. The game logs `SCRIPT ERROR: Cannot call method 'set_input_as_handled' on a null value` at `level.gd:761` (`defeat-run.log`).
- `Esc` → Main Menu.

**`extras`**:
- Main menu Sound: On → Off → On.
- New Game. Arrow keys + Space. `M` twice.
- Synthetic gamepad: the left stick runs Gino into the Sword Combo hint; pad A closes it; Start pauses and Start resumes. `Esc` → Main Menu.

46 of 46 assertions pass across the three takes.

## Found while capturing

- **Level 3's second rope bridge leaves a hole.** Its `B` sits at column 91, so the 7-tile span covers columns 91–97, but the pit runs 92–98: a 16 px hole at x 1568–1584 over the spikes. An earlier headless trial fell into it after a bat's knockback. The routes jump it, so `_tools/levels.py` passes. Not fixed: the game folder is not modified.
- **R restart logs a script error** (`level.gd:761`), as above. The restart still works.

## Not captured

- The full four-hit combo and the Attack4 magic blast. The driver's taps never chained past two hits, because each hit knocks the enemy back out of reach. The game's own playtest checks the four-hit chain.
- The jump attack, heart pickups, X / C, and the pad's slash and throw buttons in play.
- F11 / Alt+Enter fullscreen (it would change the fixed capture window), and the Quit button.
- The focus-loss auto-pause as a demonstration.
- Game audio.
