# GDD — Gino: Knife Throw

**Document status: DRAFT v0.1, agent-drafted, unapproved.**

- Written on 2026-11-10, after the game was built.
- Built only from evidence in the two source folders, the Godot project, its automated playtest and the film captures.
- It records what the game already is. Where the sources say nothing, the gap is marked PENDING rather than filled in.
- No human has signed off any section, and nobody has playtested the game by hand.

## Status vocabulary

| Label | Meaning | Evidence |
|---|---|---|
| **SOURCE** | Present in the recovered Unity C# | `knife-throw-platformer-godot/unity-scripts/scripts/**/*.cs` |
| **AUTHORED** | New in the Godot rebuild; no Unity counterpart | Godot code only |
| **IMPLEMENTED** | Present in the Godot code | A file under `scripts/` |
| **OBSERVED** | Asserted by the game's playtest or by a scripted-input capture of the real build | `playtest.log`, `captures/*-inputs.jsonl` |
| **PROPOSED** | Written by the agent in this document | This document only |
| **PENDING** | Needs a human decision that has not been made | §15 |

## 1. Metadata

| Field | Value | Evidence |
|---|---|---|
| Name | Gino: Knife Throw (window title "Gino Knife Throw") | `project.godot` `config/name`, README. The Unity scripts carry no title; the name is PENDING (OQ-01) |
| What it is | A Godot rebuild of a Unity 2D action platformer, completed with three designed levels | README |
| Engine | Godot 4.7.2.stable, 1280×720 logical view, `canvas_items` stretch, 16 px tiles | `project.godot`, `scripts/level.gd` |
| Code | 14 GDScript files + 1 shader, 2,620 lines | `wc -l scripts/*` |
| Unity source read | 40 scripts, 1,865 lines (`unity-scripts/scripts`). The A* Pathfinding Project and TextMesh Pro samples under `mod/` are Unity packages, not game code. No Unity scenes, prefabs or levels were delivered | `unity-scripts/` |
| Art in the source folder | The Rocky World pack: Gino, three enemies, two terrain sheets, props, collectibles, effects, HUD pieces, backgrounds, icon and fonts | `knife-throw-platformer-godot/art` |
| Exports | macOS `.app`: boots headless with exit 0. Windows `.exe`: built, **never run** | `export-boot.log` |

## 2. Vision

**SOURCE:** the Unity scripts describe a side-on platformer. Gino runs and jumps, slashes with a chained sword combo, throws a limited stock of knives, collects coins and knives, and is hurt by three kinds of enemy, spikes and pits. A door ends the level; hint signs explain the controls; a heart bar shows six half-hearts.

**PROPOSED vision statement:** *Take Gino home through three hostile valleys with a sword, three knives and three hearts, learning to read each enemy's wind-up before it strikes.*

Who the game is for is PENDING (OQ-02).

## 3. Pillars (PROPOSED)

1. **Read the wind-up.** Every enemy telegraphs: the walker bites 0.2 s after its cone fires, the bat curls into an orb for 0.7 s, the plant rears up for 0.6 s (`walker.gd`, `bat.gd`, `plant.gd`).
2. **Commit to the combo.** Four chained slashes deal 20 + 20 + 20 + 40, exactly an enemy's 100 HP, and lock Gino in place while they play (`player.gd` `HITS`).
3. **Knives are scarce.** Three at most, 30 damage each, refilled only by glowing daggers (`knife.gd`, `pickup.gd`).

## 4. Core loop (IMPLEMENTED, OBSERVED)

1. A level opens with its name banner. Hint crystals pause play to teach the next idea.
2. Run and jump along the level, collecting diamonds, daggers and hearts.
3. Fight or avoid walkers, bats and plants with the sword combo and knives; jump spikes and pits.
4. Stand in front of the door and press W. A Level Complete panel totals diamonds, enemies, knives and time.
5. After level 3, Finish rolls the credits, which return to the main menu.

`playtest.log` drives the routes through all three levels and the credits, plus 18 mechanics checks: PASS in 121 simulated seconds. The film captures play the same campaign with real key events (§13).

## 5. Player-experience goals (PROPOSED, all PENDING a human playtest)

| ID | Goal | How to test |
|---|---|---|
| PX-01 | A first-time player finishes Rocky Outskirts on the first try | Observe 5 new players |
| PX-02 | Players learn to step back from a curled-up bat instead of slashing into it | Count bat hits per level over 10 runs |
| PX-03 | The full four-hit combo is discovered without reading the README | Ask players after level 1 |
| PX-04 | Moonlit Depths feels like a finale, not a wall | Compare hearts lost per level |

## 6. Mechanics

### M-01 Movement
- **SOURCE** (`PlayerController.cs`): `AddForce(Vector2.right * speed * horizontal)` with `speed` 50, Space jumps while grounded (`GroundCheck.cs`), the sprite flips with direction.
- **IMPLEMENTED** (`player.gd`): run 105 px/s (6.5 tiles/s, tuned up from Unity's 3 units/s), ground acceleration 1200 and deceleration 1600 px/s², jump speed 320 px/s with gravity 900. Releasing Space early cuts the jump to 45%. 0.1 s coyote time and a 0.12 s jump buffer are AUTHORED.

### M-02 Sword combo
- **SOURCE** (`PlayerAttack.cs`, `AttackTrigger.cs`, `Transition1–4Script`): J starts Attack1, further presses chain Attack2, Attack3 and Attack4 (the magic blast). Each trigger deals `dmg = 20`.
- **IMPLEMENTED:** Attack1–3 deal 20 each; Attack4 deals 40 (AUTHORED), so a full combo defeats a 100 HP enemy. In the air J plays a jump attack (20). The combo only chains on the ground.

### M-03 Knives
- **SOURCE** (`KnifeMove.cs`, `Knife.cs`, `GameMaster.cs`): K throws a knife that flies straight; a pickup adds a knife; the count is capped at 3.
- **IMPLEMENTED** (`knife.gd`): 420 px/s for 1.3 s (about 546 px), 30 damage, breaks on rock or an enemy. The knife leaves 0.15 s into the throw. Gino starts with none.

### M-04 Enemies

| Enemy | Unity source | HP | Movement | Attack | Telegraph |
|---|---|---|---|---|---|
| Walker (fish-cat) | `Enemy2`, `Range2`, `AttackCone2` | 100 | Faces Gino; runs at him at 50 px/s while he is within 120×44 px; never walks off ledges | Bite 0.2 s after its 22 px cone fires; cone back after 1 s | The turn and run |
| Bat | `Enemy1`, `Enemy1AI`, `AttackCone1` | 100 | Steers at Gino at 58 px/s once he is within 104 px; slides along rock (A* not ported) | Strike after a 0.7 s wind-up, 0.2 s long | Curls into an orb |
| Plant | `Enemy3`, `AttackCone3` | 100 | Rooted | Snap to one side after a 0.6 s wind-up; reaches about 46 px | Rears up |

- **SOURCE:** `EnemyAttack.cs` deals `dmg = 2`, one full heart. Unity's per-prefab health values were in prefabs that were not delivered; 100 HP and 25 points per enemy are AUTHORED.

### M-05 Health, hazards and pickups
- **SOURCE** (`PlayerController.cs`, `HeartUI.cs`, `Spike.cs`, `Hole.cs`): `maxHealth = 6`, shown as three hearts in halves. Spikes damage and knock Gino back; a hole kills him.
- **IMPLEMENTED:** an enemy hit costs 2 (a heart), spikes 1 (half a heart). A hit gives 1.1 s of invulnerability with a blink and 0.35 s of hurt knockback. A pit or zero health loses the level; Retry restarts it with the score and knives Gino entered it with.
- **Pickups:** small diamond 10 points, big diamond 50 (`Coin.changeScore`), dagger +1 knife below 3, heart +2 health when hurt. Heart pickups are AUTHORED; the sprites were in the pack but unused.

### M-06 Levels (AUTHORED)

| # | Name | Size (tiles) | Enemies (walker / bat / plant) | Diamonds | Daggers | Hearts | Spikes | Hints |
|---|---|---|---|---|---|---|---|---|
| 1 | Rocky Outskirts | 128 × 18 | 2 / 1 / 2 | 9 small, 1 big | 2 | 1 | 3 | 5 |
| 2 | Thorn Hollow | 142 × 22 | 2 / 3 / 2 | 21 small, 1 big | 1 | 1 | 11 | 2 |
| 3 | Moonlit Depths | 142 × 15 | 4 / 5 / 3 | 17 small, 2 big | 2 | 1 | 20 floor + 16 ceiling | 3 |

- Unity delivered no levels. All three are ASCII maps in `_tools/levels.py`, checked and route-simulated by that script, then written to `scripts/levels.gd` and `_tools/routes.json`.
- Level 1 is the tutorial; its five hint crystals teach moving, the combo, knives, hazards and doors.
- Level 2 adds a rope bridge over a spike pit, floating one-way ledges up to a long cliff top, and bats.
- Level 3 uses the dark tileset, ceiling spikes, two rock pillars between spike pits, and a second bridge.

### M-07 Menus, pause and scenes
- **SOURCE** (`MainMenu.cs`, `UI.cs`, `Pause.cs`, `Credit.cs`, `Door.cs`, `Hint.cs`, `SaveData`/`LoadData`/`UnitData`): main menu with Play, Quit and a music slider; Esc pause menu; victory panel with Next Level; game-over panel with Retry; credits; "Press W To Enter" at the door; data carried between levels.
- **IMPLEMENTED:**
  - Main menu: New Game, Continue (Level N) once a level is unlocked, How to Play, Sound, Quit.
  - `Esc` or `P` pauses (Resume, Restart, Sound, Main Menu). R restarts from the pause or game-over menu. `M` toggles sound anywhere.
  - The hint panel closes with Enter after 1.2 s (Unity: 3 s).
  - The game pauses itself when its window loses focus.
  - Progress, best score and audio settings save to `user://knife_throw.cfg`.

## 7. World (AUTHORED)

- 16 px tiles auto-tiled from `main_lev_build.png`: the light variant in levels 1 and 2, the dark variant in level 3. Props come from both level sheets.
- A SmoothDamp camera looks ahead in the facing direction and up, clamped to the level (`CameraFollow.cs` → `level.gd`).
- Three parallax background layers scroll with the camera (`ScollBG.cs`); level 2 adds the red moon.

## 8. Art and audio

- **Art:** the Rocky World pack from the source folder. `terrain_light.png` and `terrain_dark.png`, the 7-tile `bridge_span.png`, the moon and the collectible strips are built by `_tools/make_assets.py`. The watermarked `gui/*.jpg` mock-ups were not used; panels are drawn in the `gui.png` palette.
- **Audio:** the Unity export had a SoundManager but no audio files. 23 sound effects and three music loops (menu, level, cave) are synthesized by `_tools/make_assets.py`, using the Unity sound names.
- **Fonts:** `gamer.ttf` (the game's own), Bangers and Liberation Sans from the TextMesh Pro folder.

## 9. UI (IMPLEMENTED)

| Place | Element |
|---|---|
| HUD, top left | Gino's portrait, score, three hearts (full, half, empty), knife count |
| HUD, top right | Level number and name |
| Level start | Level name banner |
| Hint crystal | Hint panel, "Press Enter" after 1.2 s |
| Door | "Press W To Enter" |
| Overlays | Pause menu, GINO IS DOWN (Retry, Main Menu), LEVEL COMPLETE (Next Level or Finish, Main Menu) |

## 10. Out of scope

- More than three levels, difficulty settings and a level select beyond Continue.
- A* pathfinding for the bat; ledge-grab and slide (frames exist in the pack, unused).
- Online scores. The best score is local only.

## 11. Technical

- 2 autoloads: `Audio` and `GameState` (campaign, input map, theme, save).
- All 6 scenes are thin. Each level scene is one node running `level.gd` with a `level_id`; everything is built from the ASCII maps.
- The input map is built in code (`GameState._configure_input`), including the gamepad.
- Enemy attacks are rectangles opened for a fixed time (`enemy.gd` `open_attack`), not physics colliders.

## 12. Risks and known defects

| ID | Issue |
|---|---|
| R-01 | **Level 3's second rope bridge stops one tile short.** The `B` is at column 91, so the 7-tile span covers columns 91–97, but the pit runs from column 92 to 98. That leaves a 16 px hole at x 1568–1584 over the spike pit. The route jumps it, so `levels.py` passes, but in capture trials a Gino fighting a bat on the bridge stepped into it and died. Moving the `B` one column right closes it. |
| R-02 | Pressing R on the pause or game-over menu logs `SCRIPT ERROR: Cannot call method 'set_input_as_handled' on a null value` (`level.gd:761`). The level still restarts; the call runs after the scene has already changed. |
| R-03 | The Windows build has never been run. |
| R-04 | Nobody has played the game by hand. All tuning (§6) is untested with players. |
| R-05 | Enemy health, points and the 40-damage finisher are not from the Unity source; its prefabs were not delivered. |
| R-06 | A walker waiting below a ledge bites Gino as he lands, while he is still in the air. The capture autopilot needed a special rule to leap past it. A human may find these drops unfair (OQ-04). |

## 13. Acceptance tests (OBSERVED)

- `_tools/playtest.tscn`: with enemies removed, an autopilot plays all three levels and the credits along the routes; then 18 mechanics checks on level 1. PASS in 121 simulated seconds (`playtest.log`).
- It steers through the routes with the real player physics. The film captures go further: they drive the real build with key and gamepad events only, with every enemy present, and add their own assertions (`captures/*-inputs.jsonl`, `CAPTURE.md`).

## 14. Provenance

The Unity scripts and art came from `knife-throw-platformer-godot/` as delivered. Claude (Claude Code) did the porting, the levels, the audio synthesis and this document. No human has reviewed it.

## 15. Open questions (PENDING)

- **OQ-01** Final game title.
- **OQ-02** Target audience and platform.
- **OQ-03** Should the finisher stay at 40 damage, or should Unity's flat 20 return with lower enemy health?
- **OQ-04** Should walkers stop waiting under drops, or should those drops be redesigned?
- **OQ-05** Fix R-01 (move level 3's bridge one column right) before release.
