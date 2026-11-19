# CAPTURE.md — Delta film captures

This is the shared gameplay evidence for three films:

- `claude-liam-delta-gdd`
- `claude-liam-delta-walkthrough`
- `claude-liam-delta-gamedev`

**These are scripted-input captures, not human playtests.** A driver played the game. No person judged whether it is fun, fair or readable.

## Build under capture

| Field | Value |
|---|---|
| Game | `delta-godot-submission/delta-godot-completed/` (not a git repository) |
| Snapshot | 572 files: everything except `builds/` and `.godot/`; listed with their SHA-256 in `build-files.txt` |
| `build_id` | `25e03b23048ef709f1aa800e57e3103a9b8beef85f54d003c4cda363f539bc13` |
| Engine | Godot 4.7.2.stable.official.ed1daf0bf, Forward+ renderer, Jolt physics |
| Machine | Apple Silicon Mac, macOS |
| Exports | macOS `Delta.app` boots headless for 300 frames, exit 0 (`export-boot.log`). The Windows `Delta.exe` (SHA-256 prefix `fb27a2aee2ebcedd`) was not run |

**How `build_id` is computed:**

1. Sort the snapshot files by POSIX path.
2. Feed each one into one SHA-256 as `path NUL sha256(file) LF`.

## The isolated copy

The game folder was never modified. It was copied to `capture/`, and only harness settings were changed there. `capture-project.diff`:

- **Own save folder:** `custom_user_dir_name="delta-filmcapture"`. The game writes progress, best times and options to `user://delta.cfg`; the captures never touch your real save. The folder was emptied before `campaign1`.
- **Window:** 3840×2160, `borderless`, `always_on_top`. Nothing else: no script, scene, asset or tuning value was changed.
- **Focus:** the window takes focus, and the machine was left alone while recording. The game pauses itself when its window loses focus (`level.gd:827`). The driver does not set the playtest's `autopilot` tree meta, which would switch that pause off.

**The game's own test,** re-run on this copy: `_tools/playtest.tscn` PASS, all 12 levels in 446 simulated seconds (`playtest.log`). It steers through the player's test-only `autopilot` hook, sets the player's rotation directly, calls `try_pickup()` and `begin_switch()`, turns the guardians' attacks off and triggers the shield strike itself. The captures below do none of that.

## Method

**Driver.** `capture_driver.gd` is a `SceneTree` script, concatenated from `core.gd` and `takes.gd` by `assemble.sh`:

- It boots `run/main_scene` and plays only through `Input.parse_input_event`: key presses, mouse motion and buttons, and joypad axis and button events.
- It reads game state (the level's map data, the player, items, devices, the guardians' timers, menus) to decide what to press, and asserts outcomes. It re-implements the few grid lookups it needs (`walkable`, `cell_center`, `find_char`) instead of calling the level's methods, and does its own read-only physics queries for path checks and for "is the crosshair on it".
- It never writes game state, never calls game methods and never teleports.

**Looking.** In the windowed takes the mouse is captured, so the view is turned with real mouse motion (`relative` = degrees ÷ 0.11 × sensitivity). Headless trials cannot capture the mouse, so there the driver uses the gamepad right stick at the same rate. Both are capped at 5° a frame. The input log records which one was used (`look_input`): in the four takes it switches to the mouse in every level (14 times) and to the right stick only on Level Complete panels (12 times), where the mouse is released and the driver sends a zero turn.

**Autopilot.** The level solutions follow the game's own playtest (`_tools/playtest.gd`): grid path finding, walking to a free spot near a target, looking at it, `F` to pick up and drop, `E` to use, `Q` to shift. On top of that, the driver's own rules, all in `takes.gd`:

- **Walking:** hold `W` while facing within 40° of the next waypoint, release early enough to stop; back off and side-step (`S` + `A`/`D`) when stuck.
- **Shuttles:** board, then keep near the middle of the moving deck with short key presses, and step off at the far end. Standing still, the player creeps ahead of a moving deck (GDD R-03), so without this the player walks off the front.
- **Guardians (level 12):** jump (`Space`) a shockwave ring when it is about 3 m away; when a strike locks within 3.7 m, walk to a spot 4.6 m away with free floor all the way there. To destroy the shield generator, wait beside it until a strike locks there, then get clear.
- **Pause menu:** arrows and Enter (see "Found while capturing").

These rules were tuned in headless trials (`trial/`). They are why the takes survive, and they are not part of the game.

**Randomness.** The driver seeds Godot's global RNG before booting (seed 1 for every take). The guardians choose strike or shockwave with `randf()`. With `--fixed-fps 30`, runs are close to reproducible but not identical: headless trials and the windowed takes drift apart in timing (campaign1 is 8,516 frames headless, 11,534 windowed), but every take clears the same levels.

**Clock.** `--fixed-fps 30`: each frame is exactly 1/30 s of game time (two 60 Hz physics steps). Nothing is retimed.

**Pixels.**
- After every draw, the driver reads `root.get_texture().get_image()`: the engine's own render at 3840×2160.
- Frames go to raw 150-frame chunks. `run_take.sh` encodes each chunk with x264 (crf 12), then joins them. Recording ran at about 7 frames a second of wall time.

**Cursor.** The OS cursor is not part of the viewport texture. On menus the driver draws a white arrow on its own CanvasLayer where its mouse is, and fades it out after 2 s without movement. In levels the mouse is captured and no cursor is drawn.

**Audio.** Game audio was not captured. The films carry narration only, and say so on screen.

**Drawing watchdog.** The driver aborts any take where no frame is drawn for 60 iterations; `record_all.sh` retries it. No take stalled.

## Takes

All four were recorded on the first attempt, in this order, sharing one save folder.

| Take | Frames | Length | Assertions | mp4 sha256 |
|---|---|---|---|---|
| `campaign1` | 11,534 | 384.5 s | 25 / 25 | `8564057cb00cb0f4e6fbf84204906b8983df5e452725ee2acfe6b98b42d2ac7d` |
| `campaign2` | 17,382 | 579.4 s | 21 / 21 | `b227bff2ab11996b22d5e1cd21315a75dbddd2b186ec3fa0497cfc64e1a94bbb` |
| `defeat` | 5,983 | 199.4 s | 28 / 28 | `95da1a0468e980b05b20def1dbf2398c11d23d07cf185d90edd3f78d2a7707ec` |
| `extras` | 1,482 | 49.4 s | 16 / 16 | `d4e67d18205caeb433b04978485dcd5ad819176f8c945dc8e201c1ffd1177ee2` |

**`campaign1`** (empty save): main menu → How to play → Back → New game → levels 1–6, each completed by the exit lift, Continue on each panel; after level 6, Main menu.

**`campaign2`**: Continue (07 Crosswire) → levels 7–12. Level 11 includes one deliberate shift while holding the core (it explodes and rebuilds). Level 12 runs with the guardians attacking on their own: strikes escaped at frames 9270, 10470, 11070 and 11670, shockwaves jumped at 9764, 12759 and 13965, and the strike locked beside the shield generator at 13470 destroys it. The stabiliser takes the core at 15437; the ending, then the credits (16102), then the menu. No death in either campaign take.

**`defeat`**: Select level 07 → a refused shift (no floor below) → the door opened from Lower Delta → a deliberate walk into the plasma (death, level restarts) → the pause menu (below) → Restart level, Skip level (to 8), Main menu → Select level 06: the cell dropped into the open bridge gap returns to its spawn → Select level 12: a deliberate walk off the deck, back at the checkpoint → Main menu.
- Between frames 3286 and 5011 of `defeat`, the driver is stuck trying to reach the bridge gap in level 6 (a solid shape blocks it at x 17.9); it then drops the cell from where it stands. The films do not use that stretch.
- One assertion label reads "falling puts Gino back at the checkpoint": "Gino" is a leftover from the previous game's driver. It means the player.

**`extras`**: Options → Back → Credits → Esc → Select level (best times) → level 1: a mouse sweep left and right, the Up arrow with Shift (running), Space; then a synthetic gamepad: Y picks up the cell, X puts it in the socket, the left stick walks toward the door, and the keys finish the route. Main menu.

90 of 90 assertions pass across the four takes.

## Found while capturing

- **The pause menu ignores mouse clicks.** `hud.gd:313-318` adds a full-screen `CenterContainer` for the options panel on top of the pause panel; every click lands on it (the driver logs the control under the mouse: `CenterContainer`). Resume, Restart level, Skip level, Options and Main menu work only with the arrow keys and Enter. Recorded in `defeat` at frame 2123.
- **R, N and Esc do nothing while paused.** `level.gd:804` handles them in `_unhandled_input`, but the level node pauses with the tree. R while paused: no restart (frame 2411). Esc while paused does not resume.
- **The player creeps ahead of a moving shuttle** when standing still on it (seen in headless trials at the fixed 30 fps; the player gained about 11.5 m on an 8 m ride and walked off the front).
- **Continue on the Level Complete panel logs `Parent node is busy setting up children, add_child() failed`** (`hud.gd:364` via `game_state.gd:373`); the next level still loads (`campaign1-run.log`).
- None of these were fixed: the game folder is not modified.

## Not captured

- Right mouse to shift and left mouse to pick up (Q and F were used), pad A, RB, LT and Start.
- Changing an option value, F11 / Alt+Enter, Exit.
- Death by a guardian strike, and a shockwave knocking the core loose.
- The focus-loss auto-pause as a demonstration.
- Game audio.
