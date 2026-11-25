# GDD — Delta

**Document status: DRAFT v0.1, agent-drafted, unapproved.**

- Written on 2026-11-17, after the game was built.
- Built only from evidence in the two source folders, the Godot project, its automated playtest and the film captures.
- It records what the game already is. Where the sources say nothing, the gap is marked PENDING rather than filled in.
- No human has signed off any section, and nobody has playtested the game by hand.

## Status vocabulary

| Label | Meaning | Evidence |
|---|---|---|
| **SOURCE** | Present in the recovered Unity C# | `delta-godot/unity-scripts/scripts/**/*.cs` |
| **AUTHORED** | New in the Godot rebuild; no Unity counterpart | Godot code only |
| **IMPLEMENTED** | Present in the Godot code | A file under `scripts/` |
| **OBSERVED** | Asserted by the game's playtest or by a scripted-input capture of the real build | `playtest.log`, `captures/*-inputs.jsonl` |
| **PROPOSED** | Written by the agent in this document | This document only |
| **PENDING** | Needs a human decision that has not been made | §15 |

## 1. Metadata

| Field | Value | Evidence |
|---|---|---|
| Name | Delta | `project.godot` `config/name`; the Unity export carries the Delta logo and icon |
| What it is | A Godot rebuild of a Unity first-person puzzle game, completed with twelve designed levels | README |
| Engine | Godot 4.7.2.stable, Forward+ renderer, Jolt physics at 60 ticks/s, 1280×720 logical view | `project.godot` |
| Code | 27 GDScript files + 3 shaders, 5,319 lines | `wc -l scripts/*` |
| Unity source read | 64 game scripts, 5,091 lines (`unity-scripts/scripts`). Starter Assets, TextMesh Pro, the URP glitch and explosion packs are third-party packages. No Unity scenes, levels or audio files were delivered | `unity-scripts/` |
| Art in the source folder | A sci-fi modular kit, energy devices (battery, generator, gate, cell socket, charging station, button stand), the atomic core, robotic eye, hex and 6×6 platforms, turbine, hi-tech energy cell, asteroids, a space skybox, the Delta logo and the damage overlay | `delta-godot/art` |
| Exports | macOS `.app`: boots headless with exit 0. Windows `.exe`: built, **never run** | `export-boot.log` |

## 2. Vision

**SOURCE:** the Unity scripts describe a first-person game on a station split into two dimensions. `DimensionSwitcher` moves the player 50 m between them with a glitch effect. Energy cells (`EnergyCell`, 3000 capacity) are carried between sockets, chargers, dischargers, arc gates, a duplicator and a teleporter that power doors, bridges and platforms. A final boss level (`BossManager`, `FinalBoss`) ends at a stabiliser.

**PROPOSED vision statement:** *Fold yourself between two layers of a broken station, carry energy where it is needed, and walk the unstable core past its guardians to the stabiliser.*

Who the game is for is PENDING (OQ-02).

## 3. Pillars (PROPOSED)

1. **One floor plan, two layers.** Upper and Lower Delta share a grid 50 m apart; a wall in one layer is a corridor in the other (`levels.gd`, `level.gd` `switch_target`).
2. **Energy is a thing you carry.** Puzzles are solved by moving one cell's charge: charge, drain, copy, teleport (`pickable.gd`, `socket.gd`, `charger.gd`, `gate.gd`, `duplicator.gd`, `teleporter.gd`).
3. **The narrator teaches, the level tests.** Each level introduces one device through VEGA's subtitles, then uses it (`levels.gd` `lines`).

## 4. Core loop (IMPLEMENTED, OBSERVED)

1. A level opens with its banner and VEGA's first line.
2. Look at a cell or device; the crosshair prompt says what `F` or `E` will do.
3. Carry cells to the devices that need them; shift layers with `Q` or the right mouse button.
4. Reach the exit lift. A Level Complete panel shows the time, the best time and resets.
5. After level 12, the ending plays, the credits roll, and the menu offers Continue and Select level.

`playtest.log` plays every level's solution with the real player physics: PASS in 446 simulated seconds. The film captures play the same solutions with real key, mouse and gamepad events, with the guardians attacking (§13).

## 5. Player-experience goals (PROPOSED, all PENDING a human playtest)

| ID | Goal | How to test |
|---|---|---|
| PX-01 | A first-time player understands layer shifting by the end of Fold | Ask players after level 2 |
| PX-02 | The arc gate puzzle (Arc) is solved without a hint | Time-to-solve over 5 new players |
| PX-03 | Players read the guardian's strike warning and get clear | Count strike deaths in level 12 over 10 runs |
| PX-04 | The final level feels like a finale, not a wall | Compare resets per level |

## 6. Mechanics

### M-01 Movement and look
- **SOURCE** (`FirstPersonController.cs`, Starter Assets): `MoveSpeed` 4, `SprintSpeed` 6, `SpeedChangeRate` 10, `JumpHeight` 1.2, `Gravity` −15, `JumpTimeout` 0.1, pitch clamp ±90.
- **IMPLEMENTED** (`player.gd`): the same values, pitch clamped to ±89°, mouse look at 0.11° per pixel × sensitivity, right stick at 150°/s. Coyote time 0.1 s is AUTHORED. Mouse look works only while the mouse is captured.

### M-02 Interaction
- **SOURCE** (`InteractionManager.cs`): a 3 m ray from the camera; `IInteractable` devices and `IPickableItem` items.
- **IMPLEMENTED:** `F` or the left mouse button picks up and drops; `E` uses a device, places or takes a cell. The prompt under the crosshair names the key. A held item is pulled to the hold point by velocity, so it still collides.

### M-03 Layer shifting
- **SOURCE** (`DimensionSwitcher.cs`): 0.3 s glitch up, move ±50 m with the held item, 0.3 s glitch down. Holding the unstable object at the glitch peak damages the player and ejects it in a critical state.
- **IMPLEMENTED:** the same, plus a refusal (AUTHORED): if the other layer has no floor at that spot or something solid is in the way, the shift is refused with a sound and a toast.

### M-04 Energy devices

| Device | Unity source | Behaviour (IMPLEMENTED) |
|---|---|---|
| Energy cell | `EnergyCell` | 3000 capacity; glow follows charge |
| Socket | `EnergyCellSocket` | powers its ports while it holds a charged cell; optional drain |
| Charging station / discharger | `ChargingStation`, `Discharger` | 750 / 1500 units per second; unusable while working |
| Sliding door | `SlidingDoor`, `PowerIndicator` | opens when every port is powered; one lamp per port |
| Pressure pad | `ActivationPadTrigger` | powered while the player or an item stands on it |
| Arc gate | `ElectricGate` | throws a charged cell back with a 0.3 s arc; a flat cell passes |
| Bridge / shuttle platform | `ExtendedPlatform`, `RetractedPlatform`, `MovingPlatform` | SmoothStep between two points, powered or oscillating |
| Duplicator | `ObjectDuplicator` | copies the item in its cradle; removes the previous copy |
| Teleporter | `Teleporter` | scan from the console, then teleport the scanned object |
| Plasma ball | `PlasmaBall` | fatal, only in its own layer |
| Generator | `Generator` | overcharges on power |

### M-05 Health and resets
- **SOURCE** (`HealthManager.cs`, `RespawnTrigger.cs`, `DeathTrigger.cs`): damage shows an overlay; `Die()` reloads the scene; falling players go back to a respawn point.
- **IMPLEMENTED:** falling off a deck returns the player to the last checkpoint; a fallen item returns to its spawn point; plasma and a guardian strike restart the level. Resets are counted on the complete panel.

### M-06 The guardians (level 12)
- **SOURCE** (`BossManager.cs`, `FinalBoss.cs`): attacks start 17 s in, then every 20 s. A strike's sparks follow the player for 5 s, lock for 3 s, then lightning hits the spot; a shockwave ring spreads from the guardian. `ShieldGenerator` falls to a strike.
- **IMPLEMENTED** (`final.gd`): the same timings; lightning kills within 3 m; the shockwave ring is jumped, and if it catches the player it knocks the held item loose. A guardian sits in each layer, and attacks come from the layer the player is in. The level's layout is AUTHORED: a generator in each layer opens the core vault, a strike must destroy the shield generator, and the final bridge leads 200 m up to the stabiliser.

### M-07 Levels (AUTHORED)

| # | Name | New idea |
|---|---|---|
| 1 | Cold Start | pick up a cell, plug it in |
| 2 | Fold | the corridor only exists in Lower Delta |
| 3 | Flat | charge an empty cell |
| 4 | Dead Weight | pressure plates: a crate, then two weights |
| 5 | Arc | the arc gate rejects charged cells |
| 6 | Span | a socket extends a bridge; an oscillating shuttle |
| 7 | Crosswire | a socket in one layer opens a door in the other; plasma |
| 8 | Echo | two sockets, one cell: the duplicator |
| 9 | Relay | a sealed cell, scanned and teleported |
| 10 | Overload | charger and gate in different layers, a shuttle between |
| 11 | Unstable | carry the reactor core; shifting makes it explode |
| 12 | Delta | two guardians, two generators, the shield, the stabiliser |

Unity delivered no levels. All twelve are ASCII maps on a 5 m grid in `scripts/levels.gd`, built at runtime from the modular kit.

### M-08 Menus, pause and scenes
- **SOURCE** (`PauseMenu.cs`, `OptionsMenuController.cs`, `PanelToggle.cs`, `AudioManager.cs`, `SceneLoader`, `GlobalData`): pause with restart and next level; options for volumes, sensitivity, resolution and quality; scene loading by a `Scene` enum.
- **IMPLEMENTED:**
  - Main menu: New game, Continue (furthest level), Select level (with best times), How to play, Options, Credits, Exit.
  - Pause (Esc or P): Resume, Restart level [R], Skip level [N], Options, Main menu.
  - Options: master, music, effects and narrator volume, mouse sensitivity, invert Y, fullscreen, quality.
  - Progress, best times and options save to `user://delta.cfg`. The game pauses itself when the window loses focus.

## 7. World (AUTHORED)

- A station on a 5 m grid: indoor floors with walls, windows onto space and lamps; outdoor decks with rails and floating asteroids; open gaps to space.
- Upper Delta is tinted cool and Lower Delta warm; the stabiliser stage sits 200 m up.

## 8. Art and audio

- **Art:** the kit and device meshes from the source folder, rebuilt as Godot materials by `_tools/make_assets.py` (Unity metallic-smoothness maps become ORM maps). Devices with no texture maps get flat colours in `kit.gd`.
- **Audio:** the Unity export had an AudioManager but no audio files. 33 sound effects, three loops and three music tracks are synthesized by `_tools/make_assets.py`. VEGA's lines are subtitles only.
- **Fonts:** Oswald, Roboto, Electronic Highway Sign and Liberation Sans from the TextMesh Pro folder.

## 9. UI (IMPLEMENTED)

| Place | Element |
|---|---|
| Centre | Crosshair and the interaction prompt (with a held cell's charge) |
| Bottom | VEGA's subtitle line |
| Top | Level banner, objective, layer name |
| Overlays | Pause menu, options, Level Complete (time, best, resets), damage flash, guardian warnings |

## 10. Out of scope

- Outline highlights (QuickOutline), audio-reactive objects and the VFX Graph arc were Unity-specific and not ported; the crosshair prompt replaces the outline.
- Voiced narration: the Unity export had no narrator audio.

## 11. Technical

- 3 autoloads: `Kit`, `Audio` and `GameState`.
- Every level scene is one node running `level.gd` with a `level_id`; the station, devices and power links are built from `levels.gd`.
- The input map, including the gamepad, is built in code (`GameState._configure_input`).

## 12. Risks and known defects

| ID | Issue |
|---|---|
| R-01 | **The pause menu ignores mouse clicks.** `hud.gd` adds a full-screen `CenterContainer` for the options panel on top of the pause panel, so every click lands on it. Resume, Restart, Skip, Options and Main menu work only with the keyboard (arrows and Enter). Observed in the `defeat` capture. |
| R-02 | **R, N and Esc do nothing while paused.** `level.gd` handles them in `_unhandled_input`, but the level node pauses with the tree and never receives them. The README lists R and N as pause shortcuts; Esc does not resume. Observed in the `defeat` capture. |
| R-03 | **A player standing still on a moving shuttle creeps ahead of it** and can walk off the front edge (observed at the capture's fixed 30 fps; the game's own playtest steers to the deck centre every frame). The capture driver keeps Gino near the middle with short key presses. |
| R-04 | Clicking Continue on the Level Complete panel logs `Parent node is busy setting up children, add_child() failed` (`hud.gd:364` via `game_state.gd:373`). The next level still loads. |
| R-05 | The Windows build has never been run. |
| R-06 | Nobody has played the game by hand. |

## 13. Acceptance tests (OBSERVED)

- `_tools/playtest.tscn`: plays all twelve levels' solutions with the real player physics; PASS in 446 simulated seconds (`playtest.log`). It steers through the player's `autopilot` hook, sets the player's rotation directly, disables the guardians' attacks and triggers the shield strike itself.
- The film captures replace all of that with key, mouse and gamepad events, with the guardians attacking on their own clock (`captures/CAPTURE.md`).

## 14. Provenance

The Unity scripts and art came from `delta-godot/` as delivered. Claude (Claude Code) did the porting, the levels, the audio synthesis and this document. No human has reviewed it.

## 15. Open questions (PENDING)

- **OQ-01** Should voiced narration be recorded for VEGA?
- **OQ-02** Target audience and platform.
- **OQ-03** Fix R-01 and R-02 (move the options container out of the click path; give the level node `PROCESS_MODE_ALWAYS` for pause input) before release.
- **OQ-04** Should the guardian attack only the layer the player is in, or both?
- **OQ-05** Is level 12's 20-second attack rhythm fair while the player carries the core?
