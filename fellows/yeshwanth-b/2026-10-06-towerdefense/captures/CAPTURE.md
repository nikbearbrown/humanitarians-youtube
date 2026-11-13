# CAPTURE.md — walker-towerdefense film captures

Shared gameplay evidence for the three films:

- `claude-liam-walker-towerdefense-gdd`
- `claude-liam-walker-towerdefense-walkthrough`
- `claude-liam-walker-towerdefense-gamedev`

Each film copies the takes it uses into its own `capture/` folder. Hashes are recorded there.

**These are scripted-input captures. They are not human playtests.** A driver played the game. No person judged whether it is fun, fair or readable.

## Build under capture

| Field | Value |
|---|---|
| Game repo | `Walker-Godot-TowerDefense`, commit `caf082c7968bca13cf8751983d27787107b46b2d` |
| Snapshot | `git archive HEAD godot` → 43 files |
| `build_id` | `f5035b752564de8f6aebbe826f448928959aed280cab94d6e541e0076d4e3bdd` |
| Engine | `Godot 4.7.2.stable.official.ed1daf0bf` (regular build, `~/Downloads/Godot.app`) |
| Machine | Apple M4, macOS. GL Compatibility renderer |

**How `build_id` is computed.** Take every file under `godot/` in the archive, sorted by POSIX path. Feed each one into a single SHA-256 as `path NUL sha256(file) LF`.

## The isolated copy

The game repo was never modified. The archive was extracted to a scratch folder, and only harness configuration was changed there. The `project.godot` diff:

```diff
+config/use_custom_user_dir=true
+config/custom_user_dir_name="walker-towerdefense-filmcapture"
-window/size/window_width_override=1440
-window/size/window_height_override=1020
+window/size/window_width_override=3840
+window/size/window_height_override=2160
+window/size/no_focus=true
+window/size/borderless=true
+[editor]
+movie_writer/mjpeg_quality=0.9
```

- **Separate save folder.** The captures never touch your real `user://` high score. The folder was emptied before the first take, so `BEST` starts at 0. Later takes boot showing the best wave written by earlier ones. That is persistence across relaunches, observed directly.
- **`no_focus` and `borderless`.** These keep OS focus changes from pausing a scripted run, and let the window reach 3840×2160 on a 2940-wide display.
- **No gameplay script, scene, level or tuning value was changed.** A copy of the modified file is `capture-project.godot`.

## Method

**Driver.** `capture_driver.gd` (in this folder) is a `SceneTree` script. It works as follows:

- It instantiates `res://game/main.tscn`, the scene `project.godot` names in `run/main_scene`.
- It plays only through `Input.parse_input_event`: key presses, mouse motion and mouse buttons. These go through the real `_unhandled_input`.
- It reads game state to decide *when* to act, and asserts outcomes. It never writes game state or calls session methods.
- It never teleports anything, and it calls none of the tests' shortcuts.
- Every take exits nonzero if any assertion fails. All six exited 0.

**Clock.** Each take runs with `--fixed-fps 30`, so every frame advances exactly 1/30 s. The game applies its own 3× simulation clock and 1×/2×/3× toggle on top of that. Nothing is retimed afterwards.

**Pixels.**

- After every draw, the driver saves `root.get_texture().get_image()`: the engine's own rendered viewport, at 3049×2160.
- The game uses `canvas_items` stretch with `keep`, so its 960×680 logical canvas is re-rasterized at 2160 lines, not upscaled.
- `encode_take.sh` centers that frame in 3840×2160 with `#1f2329` side bars. **The bars are not game pixels.**

**Why not Movie Maker.** `--write-movie` was tried first. On this display it wrote a zoomed, cropped region of the oversized window, missing the top bar and most of the build bar. The engine viewport texture was complete and correct, so it was used instead.

**Cursor.** The game draws no mouse cursor. A white arrow and an orange click ring are drawn by the driver on its own `CanvasLayer` (layer 128), at the logical position of each synthetic mouse event. This is a harness overlay, not game UI.

**Film overlays, added in `reelkit.py` when a clip is cut, never in the takes:**

- The left bar shows "SCRIPTED INPUT · not a playtest · build caf082c · Godot 4.7.2".
- The right bar shows each key press or click from the input log for 1 s.
- Slowed footage is tagged "REPLAY 1/N speed". A replay repeats the same source frames N times; it is not a second run.
- Extended last frames are tagged "HELD FRAME".

**Randomness.** The game's RNG is unseeded, so monster colours and speed rolls differ per run. Each take is one real run, not a reproducible fixture.

## Takes

| Take | Frames | Length | Assertions passed | Inputs | mp4 sha256 |
|---|---|---|---|---|---|
| `opening` | 1984 | 66.1 s | 17 / 17 | 24 | `a72332a7ecf1fe98…` |
| `maze` | 967 | 32.2 s | 8 / 8 | 15 | `7dfbc5fc5605aacf…` |
| `poison` | 980 | 32.7 s | 7 / 7 | 11 | `29eea7fb71bc5226…` |
| `storm` | 425 | 14.2 s | 4 / 4 | 4 | `222c33e8d1a89ddb…` |
| `lose` | 829 | 27.6 s | 5 / 5 | 6 | `cdc97a223462ec3a…` |
| `relaunch` | 354 | 11.8 s | 4 / 4 | 7 | `ab270877fdae634b…` |
| `focus` | 336 | 11.2 s | 6 / 6 | 5 | `0fb2ccb9898b7930…` |
| `broken` (staged) | 389 | 13.0 s | 1 / 1 | 2 | `67c413c44d6aac1c…` |

Each take's input log is `takes/<take>-inputs.jsonl`: one JSON line per key, click, assertion and wave result, keyed to the saved frame number.

### What each take shows

**`opening`**

1. Menu, then click START.
2. Fire picked from the build bar. The ghost and range circle follow the cursor.
3. Lava clicked: refused, "Can't build here".
4. Fire built at (10,1).
5. Key 2 picks Ice; a right-click cancels it; key 2 again, and Ice is built at (6,1).
6. Key 4 picks Storm; the click is refused, "Not enough gold". Esc cancels build mode.
7. Wave 1 plays at 1×.
8. Wave 2: the SPEED button goes to 2×, F to 3×, F back to 1×.
9. Waves continue until **all five lives are lost at wave 3**, and the game-over card appears.
10. Enter: play again. Fire is built at (10,1), selected, and **upgraded**: chevron, SELL 34, MAXED.
11. Wave 1 again.

**`maze`**

1. Enter, then Space.
2. Key 1, then a click on a tile a monster is standing on: refused, "Monster in the way".
3. Wave 1 with no towers: two leaks.
4. Fire built at (0,1). Fire at (1,0) is refused, "Would block the path".
5. Fire built on the road at (5,0); the route changes.
6. Wave 2 follows the new route.
7. The (0,1) tower is selected and **sold** for 10.

**`poison`**

1. Enter. Poison built at (6,1) by key 3; Fire at (10,1) by key 1.
2. **F1 overlay on.**
3. Wave 1. Esc pauses mid-wave; Enter resumes.
4. Waves 2 and 3.

**`storm`**

1. Enter. Storm built at (6,1).
2. Wave 1. A chain with more than one hop was detected at frame 178.

**`lose`**

1. Enter. Waves with no towers until game over at wave 2.
2. Enter: play again.
3. Space, then **R restarts**.

**`relaunch`** (debug tools on, disclosed below)

1. Boots with `BEST 3`, written by an earlier take: the score survived a relaunch.
2. Enter. Fire built at (10,1).
3. F1 overlay, then Space.
4. **F2 skips** to wave 2, and again to wave 3.


**`focus`**

1. Enter. Fire built at (10,1). Space.
2. The driver runs `open -a Finder`, a real OS focus change. The game pauses within 1 frame.
3. The driver calls `DisplayServer.window_move_to_foreground()`, because macOS stops drawing a covered window. The game stays paused.
4. Enter resumes.

A few frames were not drawn while the window was covered; the game was already paused.

**`broken`** (staged failure)

This take ran on a second isolated copy. Its `levels/level_01.json` has the `"exit"` key removed; a copy is in `broken-level_01.json`.

1. Boot: the error panel is drawn, but the menu card covers most of it.
2. Enter at frame 121 sets PLAYING. Space at frame 213 starts wave 1.
3. The HUD never redraws: `session._process` returns early on `load_error`.

**Runtime tree probe.** `tree_probe.gd` boots the main scene, presses Enter, builds a Fire tower by key and click, presses Space, and prints the live tree to `tree_probe.txt`. Code-created nodes are unnamed (`@Node2D@2` and so on).

`relaunch` sets `walker/debug/enabled=true` before the scene's `_ready`. The F2 wave skip only exists when that project setting is on, and it is off by default. This is the only take with debug tools enabled.

## Observations from the footage

These are observations from scripted runs, not judgments. Each is a question for a human playtest.

| # | Observed | Where | Cause in code |
|---|---|---|---|
| O-1 | Every tried opening lost all lives by wave 3 to 5. Four dry runs, plus the `opening` take (lost at wave 3). | dry runs, `opening` | the inherited compounding ramp versus 4 gold per kill; balance is untuned (GDD R-02) |
| O-2 | **The F1 debug overlay is mostly hidden.** Only its left 88 of 330 logical px are visible; the per-tower damage numbers are covered. | `poison` from frame 205, `relaunch` | `session.gd:599` draws it at x 8–338 in the session's own `_draw()`. The Grid child (`session.gd:92`, origin x 96, `grid.gd:9`) draws after its parent and covers it. |
| O-3 | **Poisoned monsters turn pale white, not green.** | `poison` wave 2, frames 500–570 | Every poison tick calls `take_damage()` (`monster.gd:84`), which sets `hit_flash = 0.14` (`monster.gd:115`). Ticks come every 0.1 s, so the white wash (`monster.gd:147-148`) never fades. |
| O-4 | **Poison can be invisible on Green monsters.** Wave 1 was two Green-variant monsters. | `poison` frames 215–300 | the poison tint is green; one of the four cosmetic variants is also green |
| O-5 | **The Storm chain is on screen for 6 frames (0.2 s) at 1×.** | `storm` frames 173–178, measured by pixel count | beam lifetimes (0.4 s, 0.2 s) run on the 3× simulation clock |
| O-6 | **A refusal reason is readable for at most 0.3 s.** The label is faint within 8 frames. | `opening` frame 269, `maze` frame 482 | `REFUSAL_FLASH := 0.3` (`session.gd:42`) drives both the tile flash and the label alpha |

| O-7 | **The level-load error panel is covered by the menu card.** | `broken` frames 0–389 (staged) | the HUD is on a CanvasLayer above `session._draw`'s error panel |
| O-8 | **With a broken level, Enter still sets PLAYING and Space starts wave 1, behind a frozen HUD.** Contradicts the comment at `session.gd:94-95` and GDD M-08 edge case 3. | `broken` frames 121–385 | `_process` returns early, so the HUD never redraws; `start_session` has no load-error guard |

## Not exercised

- **Exported builds.** Every take ran the project from source in the editor binary.
- **Audio.** The game has none.
