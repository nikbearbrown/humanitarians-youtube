# GDD — Stage Runner

**Document status: DRAFT v0.1, agent-drafted, unapproved.**

- Written on 2026-11-03, after the game was built.
- Built only from evidence in the two source folders, the Godot project, its automated playtest and the film captures.
- It records what the game already is. Where the sources say nothing, the gap is marked PENDING rather than filled in.
- No human has signed off any section, and nobody has playtested the game by hand.

## Status vocabulary

| Label | Meaning | Evidence |
|---|---|---|
| **SOURCE** | Present in the recovered Unity C# | `stage-runner-godot/unity-scripts/scenes/script/*.cs` |
| **AUTHORED** | New in the Godot rebuild; no Unity counterpart | Godot code only |
| **IMPLEMENTED** | Present in the Godot code | A file under `scripts/` |
| **OBSERVED** | Asserted by the game's playtest or by a scripted-input capture of the real build | `playtest.log`, `captures/*-inputs.jsonl` |
| **PROPOSED** | Written by the agent in this document | This document only |
| **PENDING** | Needs a human decision that has not been made | §15 |

## 1. Metadata

| Field | Value | Evidence |
|---|---|---|
| Name | Stage Runner | `project.godot` `config/name`. The Unity scripts carry no title; the name is PENDING (OQ-01) |
| What it is | A Godot rebuild of a two-stage Unity vertical shooter, completed with a third boss stage | README |
| Engine | Godot 4.7.2.stable, Compatibility renderer, 1280×720 logical view, `canvas_items` stretch | `project.godot` |
| Code | 14 GDScript files + 1 shader, 2,210 lines | `wc -l scripts/*` |
| Unity source read | 11 scripts, 479 lines. No Unity scenes or prefabs were delivered, so inspector values are unknown | `unity-scripts/scenes/script` |
| Art in the source folder | 3 stage paintings, the bullet, the game-over face (`1.png`), the Pixel Monster Pack (40 monsters at 64×64 and 32×32), a TextMesh Pro font and emoji sheet | `stage-runner-godot/art` |
| Exports | macOS `.app`: boots headless with exit 0. Windows `.exe`: built, **never run** | `export-boot.log` |

## 2. Vision

**SOURCE:** the Unity scripts describe a player who moves freely around the screen, holds `J` to fire straight up, and shoots monsters that walk down from the top. Two stages: monsters every 2 s, then every 0.7 s. One touch ends the game.

**PROPOSED vision statement:** *Fly a lone wisp up three ruined streets, thin out a monster army that keeps marching, and win the city back from the Cerberus at its gate.*

Who the game is for is PENDING (OQ-02).

## 3. Pillars (PROPOSED)

1. **Always firing, always moving.** Fire is held, not tapped, so the decision is where to stand, not when to shoot (`player.gd` `FIRE_RATE`).
2. **The street keeps coming.** Monsters never stop spawning until the goal, and they spawn faster as you score (`game.gd` `_current_interval`).
3. **One mistake costs, three end it.** Lives, a short invulnerability window and a mercy rule make a hit a setback, not an instant loss (`player.gd` `MAX_LIVES`, `INVULNERABLE_TIME`).

## 4. Core loop (IMPLEMENTED, OBSERVED)

1. A stage opens with its name and a 3, 2, 1, GO! countdown.
2. Monsters spawn above the street and walk down toward the player.
3. Hold fire and move to line up shots. Each bullet deals 1 damage; a kill adds points and may drop a triple shot or a heart.
4. Reach the stage's goal score (stages 1 and 2) or defeat the Cerberus (stage 3).
5. A Stage Clear screen totals the run; the credits roll after stage 3.

`playtest.log` drives this whole loop, the scene order and the game-over and retry path: PASS in 160 simulated seconds.

## 5. Player-experience goals (PROPOSED, all PENDING a human playtest)

| ID | Goal | How to test |
|---|---|---|
| PX-01 | A first-time player clears stage 1 on the first or second try | Observe 5 new players |
| PX-02 | Stage 2 feels like a step up, not a wall | Compare lives lost per stage over 10 runs |
| PX-03 | The Cerberus is readable: players can say which attack is coming | Ask players after the fight |
| PX-04 | Focus is discovered and used during the boss | Log focus time per stage |

## 6. Mechanics

### M-01 Movement and focus
- **SOURCE** (`Main Char.cs`): 8-way movement from the Horizontal and Vertical axes at `moveSpeed` 5, clamped to the camera bounds.
- **IMPLEMENTED** (`player.gd`): 5 units/s, where one Unity unit is 72 px (orthographic size 5 on a 720 px view), so 360 px/s. Clamped to the 640 px playfield, not the whole screen. Holding `Shift` (AUTHORED) halves the speed and shows a dot over the 13 px hitbox.

### M-02 Shooting
- **SOURCE** (`Shooting.cs`, `bullet.cs`): hold `J`; `fireRate` 0.2 s; `bulletSpeed` 10 upward. The bullet is destroyed when it touches an enemy.
- **IMPLEMENTED** (`player.gd`, `bullet.gd`): the same rate and speed (720 px/s). `Space`, `Z`, left mouse, pad A and RT also fire. Each bullet deals exactly 1 damage.

### M-03 The army
- **SOURCE** (`Army.cs`, `ArmyStage2.cs`, `Enemy.cs`): `InvokeRepeating(createArmy, 0, 2)` in stage 1 and `0.7` in stage 2 picks a random prefab. Each enemy starts at a random x in ±4.5 units, moves at `speed` −1, has 3 health and is worth 100 points.
- **IMPLEMENTED** (`game.gd`, `enemy.gd`): the first monster spawns immediately, then at the stage interval. In stage 1 the interval shrinks from 2.0 s toward 1.3 s as the score nears the goal (AUTHORED). Monsters spawn within ±288 px of the centre. That is 4 Unity units, not the 4.5 the code comment and README state: 4.5 × 72 is 324 px, which would fall outside the 640 px street.

| Monster | HP | Speed (px/s) | Points | Pattern | Stages |
|---|---|---|---|---|---|
| worm_green | 3 | 85 | 100 | fall | 1 |
| worm_brown | 3 | 95 | 100 | weave | 1 |
| slime_green | 3 | 72 | 100 | hop | 1 |
| rat_brown | 2 | 140 | 100 | fall | 1 |
| boneworm_green | 5 | 62 | 150 | fall | 1 |
| spider_black | 3 | 115 | 150 | weave | 2 |
| wolf_black | 3 | 195 | 150 | fall | 2 |
| ooze_green | 6 | 66 | 200 | hop | 2 |
| scorpion_green | 4 | 105 | 150 | hunt | 2 |
| slime_red | 3 | 95 | 100 | weave | 2 |
| rat_black | 2 | 165 | 100 | hunt | 2, 3 |
| skull_red | 2 | 150 | 100 | hunt | 3 |
| slime_black | 4 | 92 | 150 | weave | 3 |

- The per-monster values are AUTHORED. Unity's per-prefab values lived in prefabs that were not delivered, apart from the script defaults (3 HP, 100 points, speed −1 = 72 px/s).
- **Patterns:** fall walks straight down; weave sways ±70 px; hop squashes as it walks; hunt drifts toward the player's x at 70 px/s until it passes them.

### M-04 Lives, hits and drops (AUTHORED)
- Unity ended the game on the first touch (`gameOverScreen.SetActive(true); Time.timeScale = 0`).
- The rebuild gives 3 lives per stage. A hit flashes the screen red, shakes the camera, and starts 1.6 s of invulnerability with a blinking sprite. A mercy rule pops every fireball on screen, so one hit never chains into another.
- A kill drops a pickup with a 7%, 6% or 14% chance by stage. It is a heart (+1 life, up to 3) 40% of the time when a life is missing; otherwise a triple shot, which fires 3 bullets at −0.2, 0 and +0.2 rad for 10 s.

### M-05 Stages and goals

| Stage | Name | Goal | Spawn interval | Drop chance | Music |
|---|---|---|---|---|---|
| 1 | Ruined Street | 2000 points | 2.0 → 1.3 s | 7% | stage |
| 2 | Overgrown Avenue | 4000 points | 0.7 s | 6% | stage |
| 3 | The Gatekeeper | defeat the Cerberus | 5 s, at most 4 on screen | 14% | boss |

- **SOURCE:** `GameManager.cs` loads FinishStageOne when `score >= goalScore` in stage 0, otherwise ClearTheGame. `goalScore` is an inspector value, and the scenes were not delivered, so **the 2000 and 4000 goals are AUTHORED**.
- **IMPLEMENTED:** the HUD keeps Unity's readout format, `Score: x     /goal`. Stage 3 reuses the stage 1 street, tinted for dusk.

### M-06 The Cerberus (AUTHORED)
- 110 HP and worth 5000 points. It walks in from the top over 2.6 s, shielded: shots are absorbed.
- It sways across the street and attacks every 1.3 s, in a repeating cycle: aimed fan of 5 → ring of 12 → aimed fan of 5 → summon 2 minions, or a tight fan of 3 if 4 monsters are already on screen.
- At half health or less it is enraged. Attacks come every 0.95 s, fans widen to 7 and rings to 16. Touching it costs a life but does not destroy it.

### M-07 Menus, pause and scenes
- **SOURCE** (`MainMenuManager.cs`, `UI Manager.cs`, `AudioController.cs`, `Thanks.cs`):
  - Start Game, an instruction page, Go to Stage Two and Return to Main Menu.
  - A pause menu with Resume, Restart and Main Menu, and a game-over menu.
  - Music that survives scene changes, with an Audio On / Audio Off toggle.
  - Credits that scroll at 150 px/s and stop.
  - Unity's `RestartGame()` always loaded StageOne.
- **IMPLEMENTED:**
  - `Esc` or `P` pauses. R restarts the current stage from the pause or game-over menu.
  - `M` toggles sound anywhere, and the audio button appears on the main menu and the pause menu.
  - The game pauses itself when its window loses focus.
  - Firing during the credits jumps to their end. The best score is saved to `user://stage_runner.cfg`.

## 7. World (AUTHORED)

- A 640 px street in the middle of a 1280×720 view, with side panels left and right.
  - **Left panel:** title, stage, score, progress bar, kills, run total, best score, and the stage's incoming monsters.
  - **Right panel:** lives, the triple-shot timer, controls, the sound state and the objective.
- **Scrolling street:** the stage painting scrolls down at 70, 95 or 45 px/s. It alternates with a vertically mirrored copy, so the seam always matches.
- The restored city painting (`stage3`), which Unity used only behind its clear-the-game screen, sits under the credits.

## 8. Art and audio

- **Art:**
  - The stage paintings, the bullet, the game-over face and the Pixel Monster Pack come from the source folder.
  - The player is `skull_blue`, a pack monster renamed `player.png`.
  - Three of the "PNG" paintings were WebP files and were converted to JPEG.
  - The glow, ring, orb, particle, pixel and heart textures are generated by `_tools/make_assets.py`.
- **Audio:** the Unity export had an AudioSource but no audio files. Fifteen sound effects and three music loops (menu, stage, boss) are synthesized by `_tools/make_assets.py` from the Python standard library.
- **Fonts:** Liberation Sans from the TextMesh Pro folder; Bangers and Gixel shared with the Basketball Blaster port.

## 9. UI (IMPLEMENTED)

| Place | Element |
|---|---|
| Left panel | Stage name, `Score: x /goal`, progress bar, kills, run total and best, incoming monsters |
| Right panel | Hearts, triple-shot bar, controls list, sound state, objective |
| Street, top | Cerberus health bar (stage 3) |
| Street, centre | Stage banner, countdown, STAGE CLEAR! or VICTORY! |
| Overlays | Pause menu and game-over menu (with the crying face), both pausing the tree |

## 10. Out of scope

- More than three stages, difficulty settings and a stage select.
- Online scores. The best score is local only.
- Unity's emoji sheet and the combined monster sprite sheets were not carried over.

## 11. Technical

- 2 autoloads: `Audio` (music and a pool of 20 SFX voices) and `GameState` (campaign, input map, theme, save).
- All 7 scenes are thin; their nodes are built in code. The three stage scenes are seven lines each and set only `stage_id` on `game.gd`.
- The input map is built in code (`GameState._configure_input`), not in `project.godot`.
- Physics layers: 2 player, 3 enemies, 4 player bullets, 5 enemy bullets, 6 pickups. The player polls overlaps each frame, so a monster still touching it when invulnerability ends still counts.

## 12. Risks and known defects

| ID | Issue |
|---|---|
| R-01 | Pressing R on the pause menu logs `SCRIPT ERROR: Cannot call method 'set_input_as_handled' on a null value` (`game.gd:606`). The stage still restarts; the call runs after the scene has already changed. |
| R-02 | The Windows build has never been run. |
| R-03 | Nobody has played the game by hand. All tuning (§6 M-03 to M-06) is untested with players. |
| R-04 | The code comment and README say monsters spawn within ±4.5 Unity units; the code uses ±288 px, which is 4 units. |
| R-05 | The HUD controls list shows "Hold J / Space"; Z, the left mouse button and the pad also fire. |
| R-06 | The 2000 and 4000 goals are not from the Unity source; its scene files were not delivered. |

## 13. Acceptance tests (OBSERVED)

- `_tools/playtest.tscn`: an autopilot plays all three stages and the credits, then checks game over, retry and pause. It passes in 160 simulated seconds (`playtest.log`).
- It steers through the player's test-only `autopilot` hook, not through input events. The film captures replace that hook with real key, mouse and pad events and add their own assertions.

## 14. Provenance

The Unity scripts and art came from `stage-runner-godot/` as delivered. Claude (Claude Code) did the porting, the third stage, the audio synthesis and this document. No human has reviewed it.

## 15. Open questions (PENDING)

- **OQ-01** Final game title.
- **OQ-02** Target audience and platform.
- **OQ-03** Should stage 1 keep Unity's one-touch death as a hard mode?
- **OQ-04** Goal scores, spawn intervals and boss health after a human playtest.
- **OQ-05** Should the boss stage have its own painting instead of the tinted stage 1 street?
