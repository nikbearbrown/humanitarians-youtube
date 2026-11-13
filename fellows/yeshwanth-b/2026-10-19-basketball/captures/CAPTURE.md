# CAPTURE.md — Basketball Blaster film captures

This is the shared gameplay evidence for three films:

- `claude-liam-basketball-gdd`
- `claude-liam-basketball-walkthrough`
- `claude-liam-basketball-gamedev`

Each film copies the takes it uses into its own `capture/` folder.

**These are scripted-input captures, not human playtests.** A driver played the game. No person judged whether it is fun, fair or readable.

## Build under capture

| Field | Value |
|---|---|
| Game | `basketball-game-godot-completed/` (not a git repository) |
| Snapshot | 188 files: everything except `builds/` and `.godot/`; listed in `build-files.txt` |
| `build_id` | `8f86cc812e234160bb7f95e65f7150d29662426a460f387d9a7ed77fd59248d5` |
| Engine | Godot 4.7.2.stable.official.ed1daf0bf (`~/Downloads/Godot.app`) |
| Machine | Apple M4, macOS. GL Compatibility renderer |

**How `build_id` is computed:**

1. Sort the snapshot files by POSIX path.
2. Feed each one into one SHA-256 as `path NUL sha256(file) LF`.

## The isolated copy

The game folder was never modified. It was copied to a scratch folder, and only window settings were changed there. `capture-project.diff`:

```diff
-window/size/mode=3
-window/size/window_width_override=1280
-window/size/window_height_override=720
+window/size/window_width_override=3840
+window/size/window_height_override=2160
+window/size/no_focus=true
+window/size/borderless=true
```

- **Window mode.** Fullscreen was turned off so the window can be exactly 3840×2160 on a 2560-wide display.
- **`no_focus` and `borderless`.** These keep OS focus changes out of a scripted run.
- **Nothing else.** No script, scene, asset or tuning value was changed. The game writes no save files, so `user://` isolation was not needed.

## Method

**Driver.** `capture_driver.gd` is a `SceneTree` script:

- It boots `run/main_scene` (`main_menu.tscn`). The game's own `change_scene_to_file` calls move it between scenes.
- It plays only through `Input.parse_input_event`. That covers keys (physical keycodes, as the game's InputMap uses), mouse motion, mouse buttons, and joypad axis and button events.
- It reads game state (positions, nests, chickens, flags) to decide *when and where* to press, and asserts outcomes.
- It never writes game state, never calls game methods and never teleports.
- A take exits nonzero if any assertion fails. Both exited 0.

**Arena autopilot:**

- Steers to the nearest egg nest with A/D, Space (and a second Space for the double jump), Shift for the jetpack, and S+Space to drop.
- Aims the mouse at the nearest chicken while holding left click.
- Right-clicks a grenade at clusters of two or more.
- In arena 1, a "fight" phase first holds one spot and fights. It ends after one mega kill and 10 kills, or at one life left.

**Clock.** `--fixed-fps 30`: every frame advances exactly 1/30 s of game time. Nothing is retimed afterwards.

**Pixels.**

- After every draw, the driver reads `root.get_texture().get_image()`: the engine's own render at 3840×2160.
- The game uses `canvas_items` stretch, so its 1280×720 canvas is re-rasterized at 2160 lines, not upscaled.
- Frames go to raw 150-frame chunks. `run_take.sh` encodes each chunk with x264 (crf 12, yuv420p), then joins them.

**Cursor:**

- In the arenas the game hides the OS cursor and draws its own orange crosshair. That crosshair is game UI.
- On menus the OS cursor is not part of the viewport texture. The driver draws a white arrow and an orange click ring on its own `CanvasLayer` (layer 128). This is a harness overlay, not game UI.

**Audio.** Game audio was not captured. The films carry Liam's narration only, and say so on screen ("game audio not captured").

**Film overlays,** added by `reelkit.py` when a clip is cut, never in the takes:

- The engine frame is shown at 90 %, inside title-safe. The dark strip below it is not game pixels.
- The strip carries "SCRIPTED INPUT · not a human playtest · build 8f86cc8 · Godot 4.7.2 · game audio not captured".
- On the right, each key, click or gamepad input from the log is shown for 1 s.
- Slowed footage is tagged "REPLAY 1/N speed"; extended last frames are tagged "HELD FRAME".

**Randomness.** The game's RNG is unseeded, so chicken colours, hops and flights differ per run. Each take is one real run, not a fixture.

## Takes

| Take | Frames | Length | Assertions | mp4 sha256 |
|---|---|---|---|---|
| `campaign` | 5,029 | 167.6 s | 46 / 46 pass | `025ff8566ac1850311f0ab1b03144277f73a6239d4e117f4601fb21da7dbf469` |
| `defeat` | 1,216 | 40.5 s | 13 / 13 pass | `8c1b6ced1ace1d15aeea6bc1237aefa97422f97822a20e5eaf123598ef9dbea9` |
| `extras` | 872 | 29.1 s | 17 / 17 pass; Quit → exit 0 | `e8cb6e0bef32311f6ad9a04ee371b5a43c9547bcc265570ca6de8c84d7028343` |

**`campaign`:**

- Main menu → How to Play → back → Play → the 8-line briefing.
- Two clicks fail to advance it (D-01); Enter does.
- Arena 1: move, jump, double jump and jetpack; shoot; grenade.
  - The fight phase gets one mega kill at frame 1795.
  - The egg route clears it at frame 2866: kills 10, lives 1.
- Next Arena → arena 2: pause (TIME OUT) → Resume; pause → Main Menu shows "Continue: Arena 2" → Continue.
  - Arena 2 clears at frame 3859.
- Arena 3 clears at frame 4622, with lives 1.
- Claim the Trophy → victory: "CHAMPION! YOU KILLED: 013 · EGGS: 18".
- Main Menu: no Continue button.

**`defeat`:**

- Play → Esc skips the briefing.
- Synthetic gamepad: left stick moves, right stick aims, RT fires, A jumps, Start pauses and resumes.
- R restarts the arena.
- The driver walks into the flock without shooting: three lives are lost, with fade-respawns at frames 578→612 and 759→793.
- Defeat screen ("THE FLOCK WON ARENA 1. RUN IT BACK?") → Retry Arena → three lives again.

**`extras`** (recorded after the first two, to cover inputs the autopilot never used):

- How to Play → Esc returns to the menu.
- Play → Esc skips the briefing.
- Arena 1: two Space presses land on the first platform; S+Space drops through it.
- F fires (held), G throws a grenade, pad LB throws a grenade, pad RB burns jetpack fuel.
- Pause → Restart Arena reloads the court; pause → Main Menu.
- Quit: the game process exits with code 0. The last frames were saved just before the click, so the take ends on the cursor over Quit.

`capture_driver.gd` is the final version, with all three takes. `extras` was added after `campaign` and `defeat` were recorded; their code paths did not change.

**Other machine checks** (same build):

- `smoke.gd` loads all 8 scenes for 150 frames each with no script error (`smoke.log`).
- The exported macOS app booted headless for 300 frames, exit 0 (`export-boot.log`).
- The Windows `.exe` was not run.
- `bar_probe.gd` measured the HUD bars at runtime: 80×34 and 76×34 px (asked for 14 px tall), with the hint labels at y 670 (`bar_probe.txt`).
- `tree_probe.gd` printed the live node tree of arena 1 after 3 s, headless with no input (`tree_probe.txt`).

**Dry runs.** Before recording, the driver was run several times with frame saving off, to debug it. Those runs found D-01: the second test click was added because the first failed. They are not evidence and were not kept.
