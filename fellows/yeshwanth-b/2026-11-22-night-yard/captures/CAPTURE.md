# CAPTURE.md — Night Yard film captures

This is the shared gameplay evidence for three films:

- `claude-liam-nightyard-gdd`
- `claude-liam-nightyard-walkthrough`
- `claude-liam-nightyard-gamedev`

**These are scripted-input captures, not human playtests.** A driver played the game. No person judged whether it is fun, fair or readable.

## Build under capture

| Field | Value |
|---|---|
| Game | `inside/inside-godot-completed/` (not a git repository) |
| Snapshot | 449 files: everything except `builds/` and `.godot/`; listed with their SHA-256 in `build-files.txt` |
| `build_id` | `54ad5ab3eab7d97e341b1ff7fc6f5aef0549e4819a46b9a0c7b2e4d0cdf9f550` |
| Engine | Godot 4.7.2.stable.official.ed1daf0bf, Forward+ renderer, Jolt physics |
| Machine | Apple Silicon Mac, macOS |
| Exports | macOS `Night Yard.app` boots headless for 300 frames, exit 0 (`export-boot.log`). The Windows `NightYard.exe` (SHA-256 prefix `e07765776af12cf0`) was not run |

**How `build_id` is computed:**

1. Sort the snapshot files by POSIX path.
2. Feed each one into one SHA-256 as `path NUL sha256(file) LF`.

## The isolated copy

The game folder was never modified. It was copied to `capture/`, and only harness settings were changed there. `capture-project.diff`:

- **Own save folder:** `custom_user_dir_name="nightyard-filmcapture"`. The captures never touch your real save. The folder was emptied before `campaign`.
- **Window:** 3840×2160, `borderless`, `always_on_top`. Nothing else: no script, scene, asset or tuning value was changed.

**The game's own test,** re-run on this copy: `_tools/playtest.tscn` PASS, all 6 levels in 418 simulated seconds (`playtest.log`). It attaches the bots' brain (`scripts/ai.gd` in autopilot mode) to the player as `player.brain`, which sets the player's input flags directly, and it sets `level.autopilot`, which turns off the hit-stop.

## Method

**Driver.** `capture_driver.gd` is a `SceneTree` script, concatenated from `core.gd` and `takes.gd` by `record_all.sh`.

- It boots `run/main_scene` and plays only through `Input.parse_input_event`: key presses, mouse motion and buttons, and joypad axis and button events.
- It reads game state to decide what to press and to assert outcomes.
- It never moves anything, never calls a game method on the player or the level, and never teleports.

**Who decides in the levels.** The game's own bot brain, as in the playtest, but kept off the player:

- The driver creates an `ai.gd` brain with `autopilot = true`, gives it the level and the player to read, and adds it to the tree on its own. `player.brain` stays null, so the player runs its normal `_manual_input()` and reads `Input` like a person's game. The input log records `player_brain_is_null: true` at every `bridge_on`.
- Each physics tick the driver chooses the brain's goal with `_tools/playtest.gd`'s rule: the boss first, then the nearest light, then a bot, then the gate. It skips a goal after 30 s. Then it calls `brain.think()` and reads the eight flags the brain wants (`l r u d j a b t`).
- **One write to disclose:** `think()` ends by calling `fighter.set_input()` on the player. The player's `_physics_process` runs `_manual_input()` first, which overwrites all eight flags from `Input` before anything reads them. So only the key presses act.
- The wanted flags become keys sent with `Input.parse_input_event`: A, D, W, S, Space, J (attack), K (block), Shift (run). The engine applies input once per frame, so a flag wanted on a tick is pressed for at least one frame.
- **Stall guard.** If a level shows no progress (ground, score or boss HP) for 60 s, the driver restarts it from the pause menu. It is logged as `stall_restart`, at most twice a level.
- Menus, the character select and the manual moves are scripted directly: mouse clicks on buttons, hovering the Y Bots, and key and joypad sequences.

**Randomness.** The driver seeds Godot's global RNG before booting (seed 1 for every take). The bots and the backdrop draw from it. Runs are close to reproducible, but not identical: headless trials and the windowed takes drift apart in timing, and level times differ between runs.

**Clock.** `--fixed-fps 60`: each engine frame is exactly 1/60 s of game time, one 60 Hz physics tick, as the game is tuned. Every second rendered frame is saved, so the films are 30 fps of game time. Nothing is retimed.

**Wall-clock note.** The game times a double-tap run on the wall clock (`fighter.gd:266`; GDD R-02). Recording runs at about 7 saved frames a second, far slower than real time, so double taps never trigger in the takes. The driver and the brain run with Shift. In headless trials, which run far faster than real time, a manual press right after the bridge's could count as a double tap. The driver pauses 0.3 s of wall time before its manual presses.

**Pixels.**
- After every saved draw, the driver reads `root.get_texture().get_image()`: the engine's own render at 3840×2160.
- Frames go to raw 150-frame chunks, and `run_take.sh` encodes each with x264 (crf 12), then joins them.

**Cursor.** The OS cursor is not part of the viewport texture. On menus the driver draws a white arrow on its own CanvasLayer where its mouse is, and fades it out after 2 s without movement.

**Audio.** Game audio was not captured. The films carry narration only, and say so on screen.

**Drawing watchdog.** The driver aborts any take where no frame is drawn for 60 iterations; `record_all.sh` retries it.

## Takes

All three were recorded on the first attempt, in this order, sharing one save folder.

| Take | Frames | Length | Assertions | mp4 sha256 |
|---|---|---|---|---|
| `campaign` | 16,213 | 540.4 s | 39 / 39 | `d67e69cb41e86d48587da1306986c33330546fe4bc1ef5f1bb6662543e4f1c32` |
| `defeat` | 2,313 | 77.1 s | 22 / 22 | `1cbc975b80a764b292704becda3a433c8c0c4dbfc2574e97fdd493875a4d7f51` |
| `extras` | 1,836 | 61.2 s | 17 / 17 | `837fc147990ef5d0938f172d39ab72d5906a2015e46a7ecb8e4d2ce7694c8055` |

**`campaign`** (empty save): main menu → How to play → Back → New game → the character select (hover each Y Bot, click Yellow, Play) → levels 1–6 played by the bridge, Next level on each Level Clear panel → Credits → back to the menu.
- Level times: 41.6, 57.3, 73.4, 45.3, 52.7 and 104.4 s (1:44 on the level 6 panel). Level 6 was K.O.'d 5 times; no other level had a K.O.
- Signature moves, as the playtest checks them: level 1 ledge grabs 2, level 2 wall jumps 1 and climbs 5, level 3 throws 2, level 4 takedowns 1 and slides 1, level 5 hammers 4, and the Forewoman down.
- **Stall restart:** in level 6 the player stood on a container (x 17.4) without progress from about frame 9,800. The stall guard pressed Esc and Restart level at frame 11,551; the second try won. The films show the restart and do not use the stuck stretch.

**`defeat`**: Select level (best times shown) → 01:
- the bridge plays to the ground before the pit, then the driver walks into it: a fall K.O., back at the start;
- the bridge plays to the checkpoint, and the driver steps onto the spike plate: killed by the spikes, and the respawn is at the checkpoint;
- Esc pauses, and R restarts the level while paused;
- Esc → Options → Back → Resume → Esc: the R-01 defect (`defect_options_eats_pause`);
- Quit to menu.

**`extras`**: main-menu Options → Back → Change fighter. The arrow keys pressed Right, Right, Left and chose Green, but left the focus on Back, so Enter returned to the menu without saving the choice (GDD R-02). Then Select level → 01:
- the move showcase: jab, cross, up + J uppercut, K block, down + J hammer, and Shift + down slide;
- a synthetic gamepad: left stick, A, X ×3, Start;
- Quit to menu → Credits → Esc.

78 of 78 assertions pass across the three takes.

## Found while capturing

- **After Options in the pause menu, the pause key stops pausing.** `hud.gd` `_open_options` hides the options container on Back, but the `OptionsPanel` inside it keeps `visible == true`. Its `_unhandled_input` (`options_panel.gd:52-55`) checks its own `visible`, takes every Esc, P or Start, and emits `closed`, which shows the pause panel again without pausing the tree. Recorded in `defeat` (event `defect_options_eats_pause`).
- **The double tap is timed on the wall clock**, not game time (`fighter.gd:266`); see the wall-clock note above.
- **Wall jumps need prompt input.** In 30 fps headless trials, one level-2 run in five stuck in the wall-jump shaft. That setup runs two physics ticks per frame and applies input once per frame. At 60 fps, five of five passed, and the takes were recorded at 60 fps.
- None of these were fixed: the game folder is not modified.

## Not captured

- Red and Green in play: every level ran with Yellow (R-02 lost the Green choice).
- The stomp, dragon punch, sweep, air smash and flying kick by key: the brain chose its own attacks, and the showcase covered jab, cross, uppercut, block, hammer and slide.
- The left and right mouse buttons for attack and block, the double-tap run, F11 / Alt+Enter, Exit.
- Changing an option value.
- Game audio.
