# GDD — Fantasy Survival Crafting

**Document status: DRAFT v0.1, agent-drafted, unapproved.**

- Written on 2026-10-27, after the game was built.
- Built only from evidence in the two source folders, the Godot project and the automated playtests.
- It records what the game already is. Where the sources say nothing, the gap is marked PENDING rather than filled in.
- No human has signed off any section, and nobody has playtested the game by hand.

## Status vocabulary

| Label | Meaning | Evidence |
|---|---|---|
| **SOURCE** | Present in the recovered Unity C# | `fantasy-survival-crafting-godot 2/unity-scripts/scripts/*.cs` |
| **AUTHORED** | New in the Godot rebuild; no Unity counterpart | Godot code only |
| **IMPLEMENTED** | Present in the Godot code | A file under `scripts/` |
| **OBSERVED** | Asserted by an automated playtest or seen in a screenshot of the real build | `verification/*.log`, `screenshots/` |
| **PROPOSED** | Written by the agent in this document | This document only |
| **PENDING** | Needs a human decision that has not been made | §15 |

## 1. Metadata

| Field | Value | Evidence |
|---|---|---|
| Name | Fantasy Survival Crafting | `project.godot`. The Unity project had no title in its scripts; the name is PENDING (OQ-01) |
| What it is | A Godot rebuild of a Unity first-person survival-crafting prototype, completed into a one-night survival game | README |
| Engine | Godot 4.7.2.stable, Forward+ renderer | `project.godot` |
| Code | 23 GDScript files + 3 shaders, 3,303 lines | `wc -l scripts/*.gd scripts/shaders/*` |
| Unity source read | 20 game scripts, 1,431 lines (`unity-scripts/scripts`), plus vendor scripts (Bitgem water, first-person controller, rabbit demo, town door) | folder 2 |
| Source folders | Folder 2 holds the scripts and almost all the art. Folder 1 is a 353 MB subset that adds terrain heightmaps, the `soil_rocks` normal map and `WaterVolumeBase.cs` | `diff` of the two trees |
| Exports | macOS universal `.app`: boots with exit 0, and its packed data runs the game scene error-free. Windows x86-64 `.exe`: built, **never run** | `verification/VERIFICATION.md` |

## 2. Vision

**SOURCE:** the Unity scripts describe a first-person survivor who looks at an object and clicks to collect it. They manage a 21-slot inventory, craft an axe from gold and sticks, and watch health, calories and hydration.

**PROPOSED vision statement:** *Wake in an abandoned valley, gather and craft through one afternoon, and keep a fire burning until dawn.*

Who the game is for is PENDING (OQ-02).

## 3. Pillars (PROPOSED)

1. **Every tool comes from the land.** You can only craft from what you gathered; nothing is bought or given (`item_db.gd` BLUEPRINTS).
2. **The clock is the enemy.** Nightfall at 20:00 is the deadline, and the cold is the threat (`world.gd` `DUSK`, `player_state.gd` `COLD_DAMAGE`).
3. **Your body keeps score.** Walking burns calories and time burns water, so every trip has a cost (`player_state.gd`).

## 4. Core loop (IMPLEMENTED, OBSERVED)

1. Look at something within 4 m. Its name and the action you can take appear under the crosshair.
2. Collect sticks, gold, stones, food and water.
3. Craft the Axe, then fell pines for logs and hunt rabbits for meat.
4. Craft and place a Campfire before dusk.
5. Survive the night near the fire. Victory comes at dawn; defeat when health reaches 0.

`playtest.log` walks this whole loop through the real game code, 32/32 checks.

## 5. Player-experience goals (PROPOSED, all PENDING a human playtest)

| ID | Goal | How to test |
|---|---|---|
| PX-01 | A first-time player places the campfire before 20:00 without reading How to Play | Observe 5 new players |
| PX-02 | Food and water matter: at least one meal or drink is needed before dawn | Log stats over a full run |
| PX-03 | The night feels tense, not tedious | Ask players to rate it; check how often they choose to rest |
| PX-04 | Rabbits are worth chasing | Count hunts per run |

## 6. Mechanics

### M-01 Movement and look
- **SOURCE** (`PlayerMovement.cs`, `MouseMovement.cs`): CharacterController movement at 12 m/s, gravity −9.81 × 2, `jumpHeight` 3, jump velocity `sqrt(h × −2g)`. Pitch is clamped to ±90°. Look is disabled while the inventory, crafting or menu is open. The grass-walk sound plays while moving on the ground.
- **IMPLEMENTED** (`player.gd`): same gravity and jump formula and the same look gating. Walk speed is 5.5 m/s, sprint 8.5 m/s, jump height 1.2 m. Wading slows you to 55%. Footsteps play every 0.42 s. Right-stick look is added.

### M-02 Selection and pickup
- **SOURCE** (`SelectionManager.cs`, `InteractableObject.cs`, `Collectible.cs`): a ray from the mouse position, an in-range check from a trigger, the item name in the UI, left click to add to the inventory if it isn't full, and a rotating collectible.
- **IMPLEMENTED** (`player.gd`, `pickup.gd`): the ray comes from the screen centre with a 4 m reach. The prompt shows the name and the action. Left click or `E` collects. Pickups dropped by trees and rabbits spin.

### M-03 Inventory
- **SOURCE** (`InventorySystem.cs`, `ItemSlot.cs`, `DragDrop.cs`, `InventoryItem.cs`):
  - 21 slots, opened with `I`.
  - The pickup popup shows for 2 s.
  - `CheckIfFull` counts 21.
  - `RemoveItem` iterates from the last slot backwards.
  - Dragging shows a 60% alpha preview.
  - Hovering shows the name, description and functionality.
  - Right-click consumes the item and clamps each stat to its maximum.
- **IMPLEMENTED** (`inventory_ui.gd`, `inventory_slot.gd`): all of the above. Dropping onto an occupied slot **swaps** the two items; Unity left the item where it was. Right-click also equips or places items.
- **OBSERVED:** drag/drop move, consume and place checks pass.

### M-04 Crafting
- **SOURCE** (`CraftingSystem.cs`, `Blueprint.cs`): `C` toggles the window. A Tools category button opens the tools screen. The Axe needs 3 Gold + 3 Stick. Requirement text reads "3 Gold [n]". The Craft button is hidden until the recipe is affordable. Crafting plays a sound, adds the item and removes the materials.
- **IMPLEMENTED** (`crafting_ui.gd`, `item_db.gd`): the same flow with two categories and three blueprints:

| Item | Category | Requires | Status |
|---|---|---|---|
| Axe | Tools | 3 Gold, 3 Stick | SOURCE |
| Campfire | Survival | 4 Log, 3 Stone | AUTHORED |
| Cooked Meat | Survival | 1 Rabbit Meat, and a campfire within 9 m | AUTHORED |

### M-05 Survival stats
- **SOURCE** (`PlayerState.cs`, the three bar scripts): health, calories and hydration start at their maximums. Calories drop by 1 for every 5 m travelled. Hydration drops 1% every 10 s. `N` deals 10 damage (debug). The bars show `current/max`, and hydration shows `%`.
- **IMPLEMENTED** (`player_state.gd`, `hud.gd`): the same, all with a maximum of 100, plus:
  - Hydration drops every 5 s.
  - 1 calorie burns every 25 s while idle.
  - Health drops 1 per second when calories or water are at 0.
  - Health drops 1 every 1.4 s when cold at night.
  - Health regenerates 1 every 4 s while calories and water are both above 60.
- These rates are PROPOSED tuning values and are PENDING (OQ-04).

### M-06 Chopping and hunting (AUTHORED)
- The Unity `SoundManager` declared `toolSwingSound` and `chopSound`, but no script used them.
- **Chopping:** pines take 4 axe hits, topple away from the player and leave a stump and 2 Logs.
- **Hunting:** rabbits follow the `AI_Movement.cs` port: walk in one of 4 directions for 3–6 s, wait 5–7 s. They also flee within 5 m. One axe hit plays the Dead clip and drops Rabbit Meat.
- **OBSERVED:** "two trees felled", "four logs dropped", "rabbit hunted", "rabbit dropped meat".

### M-07 Day, night and campfire (AUTHORED)
- The day runs 06:00–20:00 at 24 s per game hour; the night at 12 s per hour. The game starts at 07:30.
- The sky shader blends the Fantasy Skybox panoramas: `fs002_day`, `fs002_sunset` and `fs002_night`.
- A placed campfire warms anyone within 9 m. Pressing `E` at it during the night rests, which runs time 9× faster.
- **Victory** is reaching dawn after spending part of the night near a placed campfire.
- **OBSERVED:** "night has fallen", "not freezing by the fire", "survived the night: victory", "freezing away from the fire", "player died of cold".

### M-08 Food and water (AUTHORED values)

| Item | Health | Calories | Water | Source in the world |
|---|---|---|---|---|
| Apple | +5 | +20 | +10 | 6 orchard trees (3 each) and 3 on the ground |
| Mushroom | 0 | +15 | 0 | Pine groves |
| Red Cap | −10 | +25 | 0 | Meadows |
| Bread | 0 | +35 | −5 | Village carts |
| Water Flask | 0 | 0 | +35 | Village barrels |
| Rabbit Meat | −5 | +20 | 0 | Hunted rabbits |
| Cooked Meat | +15 | +50 | 0 | Crafted at a campfire |
| Lake | 0 | 0 | +20 per drink | Aim at the water |

### M-09 Menus and saving
- **SOURCE** (`MenuManager.cs`, `InGameMenu.cs`, `MainMenu.cs`): `M` toggles the menu canvas, hides the HUD and frees the cursor. The menu has main, save and settings pages and a Back To Main Menu button. The main menu has New Game and Quit. The Unity scripts contained no save code.
- **IMPLEMENTED:** `M` or `Esc` opens a paused menu with Resume, Save Game, Settings (mouse sensitivity, master volume), Main Menu and Quit. There is one JSON save slot. Load Game appears on the main menu, and Load Save on the defeat screen.
- **OBSERVED:** "game saved", "save holds inventory and campfire", and 7 save-restore checks.

## 7. World (AUTHORED)

- A procedural 260 × 260 m valley ringed by mountains. It has a shallow lake, a flattened village plot and a dirt path between them.
- It is textured with five Terrain Sample Asset layers: grass, dry grass, rock, sand and soil.
- **Village:** two wooden houses, two half-timber houses, a tavern, carts, barrels, sacks, and a fenced six-tree orchard.
- **Nature:**
  - Three choppable pine groves (36 trees) and 48 scenery trees, including willows on the lake shore.
  - Up to 34 boulders and a ring of 7 standing stones.
  - Up to 150 flowers and ferns, and 2,221 grass and poppy instances.
- **Resources in the seeded world:** 26 Sticks, 14 Gold, 17 Stones, 11 Mushrooms, 6 Red Caps, 3 Apples, 2 Bread, 3 Water Flasks, and 9 rabbits. These counts come from `playtest.log`; the tree, rabbit and grass counts come from a count of the built scene.

## 8. Art and audio

- **Art:** every model and texture comes from the asset packs in the two source folders:
  - Polytope Lowpoly Environments and Village, Fantasy Environments (plants, trees, town), Mountain Terrain Rocks and Tree.
  - Five Rabbits, Fantasy Skybox FREE, Fantasy Wooden GUI, GUI Parts, Terrain Sample Assets, the Bitgem water normals and the Almendra font.
- **Icons:** 12 item icons were rendered from the 3D models by `_tools/bake_icons.gd`. The axe icon is the pack's `stoneaxe.png`, with its painted checkerboard removed.
- **Audio:** the source folders contain no audio, so every sound in `assets/audio` was synthesized for this rebuild.

## 9. UI (IMPLEMENTED)

| Place | Element |
|---|---|
| HUD, top left | Objective list |
| HUD, top right | Clock |
| HUD, bottom left | Stat bars |
| HUD, centre | Crosshair and prompt |
| HUD, top centre | Pickup popup |
| HUD, bottom right | Equipped tool |
| Inventory window | Left side of the screen |
| Crafting window | Right side; both windows can be open at once, as in Unity |

## 10. Out of scope

- Multiple save slots.
- More than one night as a goal.
- Building beyond the campfire, enemies, and weather. The skybox pack includes rainy and snowy panoramas that go unused.

## 11. Technical

- 3 autoloads: `GameState`, `Audio`, `Models`. All 6 scenes are thin; their nodes are built in code.
- `model_library.gd` repairs the FBX imports: it rebuilds materials, strips LOD and UCX meshes, stands Z-up models upright and merges the rabbit animations.
- Physics layers: 1 world, 2 interactable, 3 water, 10 player.

## 12. Risks and known defects

| ID | Issue |
|---|---|
| R-01 | On a fresh import, Godot logs "Can't open file" for the FBX files' original texture paths. Harmless, but noisy for a reviewer. |
| R-02 | The Windows build has never been run. |
| R-03 | Nobody has played the game by hand. All tuning (§6 M-05, M-07, M-08) is untested with players. |
| R-04 | Rabbit animations were seen in stills only; a moving capture has not been reviewed. |
| R-05 | `_tools/playtest_load` depends on the save written by `_tools/playtest`. |
| R-06 | Fences use the trunk texture because the village atlas mapped them white or red. The intended fence texture is unknown. |

## 13. Acceptance tests (OBSERVED)

The 42 automated checks are listed in `verification/playtest.log` (32) and `verification/playtest_load.log` (10). All 6 scenes run for 300 frames with 0 script errors (`verification/scene_runs.log`).

## 14. Provenance

The Unity scripts and assets came from the two source folders as delivered. Claude (Claude Code) did all the porting, art repair, audio synthesis, level layout and this document. No human has reviewed it.

## 15. Open questions (PENDING)

- **OQ-01** Final game title.
- **OQ-02** Target audience and platform.
- **OQ-03** Should the game continue past the first night (days 2–3, more recipes)?
- **OQ-04** Stat drain rates and night length after a human playtest.
- **OQ-05** Should Red Caps be poisonous? This is an invented risk; Caesar's mushroom is edible in real life.
