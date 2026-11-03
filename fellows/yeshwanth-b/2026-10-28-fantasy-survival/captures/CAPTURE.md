# CAPTURE.md — Fantasy Survival Crafting film captures

This is the shared gameplay evidence for three films:

- `claude-liam-fantasy-gdd`
- `claude-liam-fantasy-walkthrough`
- `claude-liam-fantasy-gamedev`

**These are scripted-input captures, not human playtests.** A driver played the game. No person judged whether it is fun, fair or readable.

## Build under capture

| Field | Value |
|---|---|
| Game | `fantasy-survival-crafting-godot/fantasy-survival-crafting-godot/` (not a git repository) |
| Snapshot | 446 files: everything except `builds/`, `.godot/` and `submission/`; listed in `build-files.txt` |
| `build_id` | `a5144381d771f6311baea35f13239d9812457fd52f69997470b3bbde908cc82d` |
| Engine | Godot 4.7.2.stable.official.ed1daf0bf, Forward+ |
| Machine | Apple M4, macOS |
| Exports | macOS `.app` boots headless for 300 frames, exit 0 (`export-boot.log`); hashes `284db3f744a32188` (`.pck`) and `6b4cce1a10088c67` (`.exe`) match the game's VERIFICATION.md. The Windows `.exe` was not run |

**How `build_id` is computed:**

1. Sort the snapshot files by POSIX path.
2. Feed each one into one SHA-256 as `path NUL sha256(file) LF`.

## The isolated copy

The game folder was never modified. It was copied to a scratch folder, and only harness settings were changed there. `capture-project.diff`:

- **Own save folder:** `custom_user_dir_name="fantasy-survival-filmcapture"`.
  - The game writes `user://savegame.json` and `settings.cfg`. The captures never touch your real save or settings.
  - The folder was emptied before the day take.
- **Window:**
  - fullscreen off;
  - 3840×2160;
  - `no_focus`, `borderless`, `always_on_top`.
- **Nothing else.** No script, scene, asset or tuning value was changed.

**The game's own tests,** re-run on this copy:

- `_tools/playtest.tscn`: 32/32 (`playtest.log`).
- `_tools/playtest_load.tscn`: 10/10 (`playtest_load.log`).

Those tests call game functions directly. The captures below do not.

## Method

**Driver.** `capture_driver.gd` is a `SceneTree` script, assembled from `core.gd`, `survival.gd` and `takes.gd` by `assemble.sh`:

- It boots `run/main_scene` and plays only through `Input.parse_input_event`. That covers keys, relative mouse motion (look), mouse buttons, and joypad axis and button events.
- It reads game state (positions, entities, the player's ray target, the HUD prompt) to decide when and where to press, and asserts outcomes.
- It never writes game state, never calls game methods and never teleports.

**Look.**

- Turns are relative mouse motion, at most 0.085 rad per frame.
- The game reads `event.relative` in viewport units, so the driver scales motion by the window's stretch factor. A turn is the same at any window size.

**Walking.**

- W, plus Shift beyond 7 m.
- If the player is blocked, the driver side-steps with A or D and presses Space.

**Using things.** The driver aims the centre ray at the object and presses E (or left-clicks to chop and hunt) only when the game's own `player.target` is that object.

**Clock.**

- `--fixed-fps 30`: each frame is exactly 1/30 s of game time. Nothing is retimed.
- The game's own clock runs 24 s per game hour by day and 12 s by night, and 9× faster while resting.

**Pixels.**

- After every draw, the driver reads `root.get_texture().get_image()`: the engine's own render at 3840×2160.
- Frames go to raw 150-frame chunks. `run_take.sh` encodes each chunk with x264 (crf 12), then joins them.

**Cursor.**

- In play, the game captures the mouse and draws its own crosshair dot.
- When the game frees the cursor (menus, inventory, crafting), the driver draws a white arrow on its own CanvasLayer. The game's custom cursor image is not part of the viewport texture.

**Audio.** Game audio was not captured. The films carry narration only, and say so on screen.

**Drawing watchdog.**

- macOS stops drawing a covered or sleeping window while game logic keeps running.
- Two earlier 4K attempts stopped this way, at frames 1,245 and 5,823. They were discarded; none of their footage is used.
- The driver now aborts any take where no frame is drawn for 60 iterations. `record_all.sh` retries such a take from the save it depends on.
- The final takes all completed on the first attempt.

## Takes

The run is split across three takes, which continue from one another through the game's own Save Game and Load Game:

| Take | Frames | Length | Assertions | mp4 sha256 |
|---|---|---|---|---|
| `day` | 5,170 | 172.3 s | 45 / 45 | `ce475fd0939c868328736d5dbd16eb86b911191c2dda215c5fcfde1253624a85` |
| `night` | 6,061 | 202.0 s | 15 / 15 | `3faeb08f07b36b3b8d5ef4eb7d9cc00a926fe76ae3a15f00cab1f12b5663b97e` |
| `defeat` | 1,551 | 51.7 s | 14 / 14 | `9b34f642b113b3e32f0e5a32a799b1b93c16c92b88bfabc04540ba3bf01e0f07` |

**`day`** (07:30 → 13:09), a new game from an empty save folder:

- Main menu (no Load Game) → How to Play → back → New Game → the three intro pages.
- Look around; open the empty inventory and crafting screens; press 1 with no axe.
- Pick an apple from an orchard tree.
- In the west grove: 3 Sticks and a Mushroom. At the standing stones: 3 Gold and 3 Stones.
- Craft the Axe; equip it with 1.
- Fell two pines, 4 swings each, and collect 4 Logs. Craft the Campfire.
- Hunt a rabbit and collect the meat.
- Drink from the lake.
- Try to place the fire facing the water: refused, "You can't build a fire in the water". Walk inland and place it.
- Cook the meat. Hover the item info, drag an item to the last slot, and eat the Cooked Meat, Apple and Mushroom.
- Menu: Settings → Back → Save Game → Save. This is the day save.

**`night`** (13:09 → dawn):

- Load Game (the day save).
- Wait beside the fire through dusk; "Night falls".
- Warm by the fire; Save Game at 20:20. This is the night save.
- E at the fire: rest, 9× time.
- Dawn: "Dawn Breaks" (day 2, 16 items, 2 trees, 1 rabbit).
- Main Menu now shows Load Game.

**`defeat`:**

- Load Game (the night save).
- Synthetic pad: the right stick looks, Y opens and closes the inventory.
- Walk 30 m away from the fire: "You are freezing!", with the cold overlay.
- 8 presses of N, the debug-damage key kept from the Unity source, 10 health each. Then the cold drains the rest.
- "Lost to the Wilds: You froze in the night" → Load Save → back at the fire, alive → Main Menu.

**Observed defect (all takes):** once a recipe consumes its materials, the ticked objectives read "[x] Gather 3 Sticks (0/3)" and "[x] Gather 3 Gold nuggets (0/3)". The same happens to Logs and Stones after the campfire. The counters show the current inventory, not what was gathered (`world.gd:759-773`).

**Not captured:**

- F11 fullscreen;
- the Quit buttons;
- Play Again;
- the volume and sensitivity sliders (the Settings page was opened, not changed);
- sprint-jump over obstacles as a feature (jumps happen only inside unstick moves);
- Red Cap, Bread and Water Flask pickups;
- the apples lying on the ground.
