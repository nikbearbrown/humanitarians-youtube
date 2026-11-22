# GDD — Night Yard

**Document status: DRAFT v0.1, agent-drafted, unapproved.**

- Written on 2026-11-20, after the game was built.
- Built only from evidence in the two source folders, the Godot project, its automated playtest and the film captures.
- It records what the game already is. Where the sources say nothing, the gap is marked PENDING rather than filled in.
- No human has signed off any section, and nobody has playtested the game by hand.

## Status vocabulary

| Label | Meaning | Evidence |
|---|---|---|
| **SOURCE** | Present in the recovered Unity C# | `inside-godot/unity-scripts/**/*.cs` |
| **AUTHORED** | New in the Godot rebuild; no Unity counterpart | Godot code only |
| **IMPLEMENTED** | Present in the Godot code | A file under `scripts/` |
| **OBSERVED** | Asserted by the game's playtest or by a scripted-input capture of the real build | `playtest.log`, `captures/*-inputs.jsonl` |
| **PROPOSED** | Written by the agent in this document | This document only |
| **PENDING** | Needs a human decision that has not been made | §15 |

## 1. Metadata

| Field | Value | Evidence |
|---|---|---|
| Name | Night Yard (AUTHORED: the Unity project had no title; its scenes were `TutorialScene_CharacterSelect`, `TutorialScene_Sample` and `TutorialScene_Sample_Night`) | `project.godot` `config/name`; README |
| What it is | A Godot rebuild of a Unity 2.5D platformer, completed as a six-level brawler-platformer | README |
| Engine | Godot 4.7.2.stable, Forward+ renderer, Jolt physics at 60 ticks/s, 1280×720 logical view | `project.godot` |
| Code | 17 GDScript files, 5,215 lines | `wc -l scripts/*.gd` |
| Unity source read | 150 C# files, 9,615 lines (`unity-scripts/`). No Unity scenes, animator controllers, ability assets or audio were delivered | `unity-scripts/` |
| Art in the source folder | Y Bot, Amy and Sophie with 55 Mixamo and HumanIK clips; the industrial yard pack; the spike trap; the axe, the hammer, the pine tree; the fire smoke flipbook; the TextMesh Pro fonts | README, `inside-godot/art` |
| Exports | macOS `.app` and Windows `.exe` are built. The Windows build has **never been run** | README, `export-boot.log` |

## 2. Vision

**SOURCE:** the Unity scripts describe a side-view character controller with a full move set: walking, running, jumping, ledge grabs, wall slides and wall jumps, a combo attack system (`AttackManager`, `TransitionIndexer`), blocking, ragdoll deaths, takedowns from behind (`InstaKill`), a stomp, melee weapons that can be picked up, thrown and dropped, spike traps, pickups that score, and AI that path-finds over a NavMesh with jump links (`AIController`, `PathFindingAgent`). A character-select scene chooses between three Y Bots.

**PROPOSED vision statement:** *A night shift in a container yard: climb the stacks, fight your way past the yard bots, and take down the Forewoman who runs it.*

Who the game is for is PENDING (OQ-02).

## 3. Pillars (PROPOSED)

1. **Move like a stuntman.** Every obstacle is solved with a move from the Unity controller: a ledge grab, a wall jump, a slide, a running jump (`fighter.gd`, `levels.gd` movement rules).
2. **Fight with what you have.** A three-hit combo, directional attacks, the axe and the hammer; bots that block and combo back (`fighter.gd` `ATTACKS`, `ai.gd`).
3. **Read the yard.** Lights to collect, plates to jump, bots with their backs turned for a takedown (`levels.gd` legend, `spike_trap.gd`).

## 4. Core loop (IMPLEMENTED, OBSERVED)

1. Choose a Y Bot on the character-select stage.
2. A level opens with its banner. Collect yard lights (+10 each, +5 HP) and knock out bots (+10 each).
3. At 100 points the exit gate opens (level 6: when the Forewoman is down). Walk through it.
4. A Level Clear panel shows the time, the best time, the score, bots knocked out and times K.O.'d.
5. After level 6, the credits roll and the game returns to the menu.

`playtest.log` plays every level with the real player physics, its input flags set by the bots' brain in autopilot mode: PASS in 418 simulated seconds. The film captures take the same brain's decisions and send them to the game as real key presses (§13).

## 5. Player-experience goals (PROPOSED, all PENDING a human playtest)

| ID | Goal | How to test |
|---|---|---|
| PX-01 | A first-time player finds the ledge grab in level 1 without dying in the pit | Count pit falls in level 1 over 5 new players |
| PX-02 | The wall-jump shaft in level 2 is learnable within three tries | Time in the shaft over 5 new players |
| PX-03 | Players discover the takedown from the hint in level 4 | Count takedowns over 10 runs |
| PX-04 | The Forewoman feels like a fight, not a wall | Compare K.O.s per level |

## 6. Mechanics

### M-01 Movement
- **SOURCE** (`MoveForward`, `MomentumCalculator`, `CheckTurbo`, `Turn180`, `ManualInput`): walk, turbo run, a running turn, a double tap that turns on turbo.
- **IMPLEMENTED** (`fighter.gd`): walk 1.65 m/s (the walking clip's stride), run 5.2 m/s, gravity 22 m/s². Run with Shift, or double-tap a direction within 0.18 s (`DOUBLE_TAP`, timed on the wall clock).

### M-02 Jumping and climbing
- **SOURCE** (`Jump`, `JumpPrep`, `LedgeChecker`, `WallSlide`, `WallJumpPrep`): jump prep then jump, ledge grabs, wall slides and wall jumps.
- **IMPLEMENTED:** jump speed 9.6 m/s (apex about 2.1 m, so a 2 m step can be jumped onto; 3–4 m walls need the ledge grab); a running jump at 9.8 m/s clears a 3-wide gap. Letting go of jump early cuts the climb. A ledge at hand height is grabbed; up climbs, down lets go. Holding into a wall while falling caps the fall at 2.2 m/s; jump kicks off. A fall higher than 3.2 m rolls on landing.
- **AUTHORED:** a mantle assist pops the player onto a wall whose top is just above the feet.

### M-03 Combat
- **SOURCE** (`Attack`, `AttackManager`, `TransitionIndexer`, `DamageDetector`, `Block`, `InstaKill`, `MarioStompAttack`): attacks chained by input in a window; damage only when the named body parts touch; blocking when facing the attacker; takedowns from behind; stomps.
- **IMPLEMENTED** (`fighter.gd` `ATTACKS`): 16 attacks, each with its clip range, a strike window measured from the clip, the hands, feet or blade that must touch, damage, knockback and death clip.

| Move | Input | Damage to a bot / to the player |
|---|---|---|
| Jab → cross → kick | attack ×3 | 0.34 → 0.34 → 0.5 / 8 → 8 → 12 |
| Uppercut | up + attack | 1.0 / 20 |
| Flying kick | run + attack | 1.0 / 22 |
| Dragon punch | run + up + attack | 1.0 / 20 |
| Hammer | down + attack (9 s cooldown) | 9.0 / 40, unblockable, a ground shock |
| Axe | attack while holding it | 1.0 / 30 |

### M-04 Weapons
- **SOURCE** (`MeleeWeapon`, `WeaponPickUp`, `WeaponPutDown`, `WeaponThrow`, `SpawnObject`): an axe picked up, swung, thrown and dropped; a hammer spawned for a slam.
- **IMPLEMENTED** (`weapon.gd`): attack while standing on the axe picks it up; run + attack throws it (it flies straight, spinning); down + attack puts it down. The hammer appears in the hand for `hammer_down` and recharges in 9 s.

### M-05 Health, score and resets
- **SOURCE** (`HPManager.maxHP` 100, `ScoreManager.maxScore` 100, `PickupItem.scoreValue` 10): HP, a score that wins at 100, pickups worth 10.
- **IMPLEMENTED:** each light is +10 and heals 5; each bot knocked out is +10. A K.O., a spike plate or a fall below y −3 sends the player back to the last checkpoint with full HP after 2.6 s. The three Y Bots differ (AUTHORED): Yellow 100 HP; Red 110 HP, 135% power, 92% speed; Green 95 HP, 85% power, 112% speed.

### M-06 Spike plates
- **SOURCE** (`TrapSpikes`, `Spike`): spikes fire after a short delay, hold for 1.5 s, retract, reload after 1 s.
- **IMPLEMENTED** (`spike_trap.gd`): the plate fires 0.4 s after something steps on it, kills whoever is still on it with the spike-death clip, retracts after 1.5 s and reloads after 1 s.

### M-07 The bots and the Forewoman
- **SOURCE** (`AIController`, `AIProgress`, `AITriggerAttack`, `AIAttack`, `PathFindingAgent`): path to the target over NavMesh links, jump up or walk off, a flying kick when rolled, attack in range, re-randomise the attack every 2 s, re-path when the target moves.
- **IMPLEMENTED** (`ai.gd`, `nav.gd`): the same, over the level grid's walk, drop, jump, ledge-climb, slide and wall-jump links.
- **AUTHORED:** bots start unaware (for takedowns) and notice the player in front of them, right behind them, or when the player runs close or fights nearby. Amy blocks and combos; runner bots flying-kick. Sophie, the Forewoman, has 12 HP, blocks often, shrugs off light hits and swings the hammer too.

### M-08 Levels (AUTHORED)

| # | Name | New idea |
|---|---|---|
| 1 | Clock In | walk, run, jump, the first ledge, the first bots, a spike plate |
| 2 | Stacks | container stacks and a wall-jump shaft; Amy on the roof |
| 3 | Axe to Grind | two axes, bots on the catwalks, throw from a distance |
| 4 | Spike Alley | spike plates, a 1 m tunnel to slide through, a bot with its back turned |
| 5 | Hangar Brawl | a crowd of 14, and the hammer |
| 6 | The Forewoman | the boss fight |

Unity delivered no levels. All six are ASCII maps on a 1 m grid in `scripts/levels.gd`, built at runtime. The yard behind the lane is placed from a seed.

### M-09 Menus, pause and scenes
- **SOURCE** (`CharacterSelect`, `MouseControl`, `CharacterHoverLight`, `PlayGame`, `ChangeScene`): click a Y Bot under a hover light; Return plays or logs "must select character first".
- **IMPLEMENTED:**
  - Main menu: New game, Continue (furthest level), Select level (with best times), Change fighter, How to play, Options, Credits, Exit.
  - Character select: hover and click, or arrow keys; Play or Enter.
  - Pause (Esc, P or Start): Resume, Restart level (R), Options, Quit to menu.
  - Options: volumes, fullscreen, quality, show hints. Progress and best times save to `night_yard.cfg`.

## 7. World (AUTHORED)

- A container yard at night on a 1 m side-view grid: concrete, containers scaled to their map rectangles, catwalks, crates.
- Behind the lane: fence, container stacks, hangars, tanks, pipes, trees, lamp posts and fire barrels, placed from a seed.
- A 2.5D cutaway fades out blocks between the camera and the player, for the slide tunnel and overhangs.

## 8. Art and audio

- **Art:** Y Bot, Amy and Sophie retargeted with Godot's `SkeletonProfileHumanoid` (one BoneMap for the Mixamo rig, one for the HumanIK clips), so every clip plays on all three. The yard pack's meshes get their `.tga` maps (converted to `.jpg`) as new materials (`kit.gd`).
- **Audio:** the Unity export had no audio files. 31 sound effects, a fire loop and three music tracks (menu, level, boss) are synthesised by `_tools/make_assets.py`.

## 9. UI (IMPLEMENTED)

| Place | Element |
|---|---|
| Top left | HP bar and "HP: x / 100", score and gate status, hammer charge |
| Top | Level banner; the boss bar on level 6 |
| Lower centre | Hints from the map's numbered cells, `+10` popups |
| Overlays | K.O. screen, pause, options, Level Clear |

## 10. Out of scope

- Unity editor tools and demo code: `AbilitySearch`, `ColliderRemover`, `HierarchyLabel`, `MaterialChanger`, the `generics_explained` weapon demo, the URP `SimpleCameraController`.
- Unused art: the Unity-chan meshes inside the HumanIK clips, `business_male.fbx`, `thor_hammer.dae`, `hammer2.fbx`, the workshop example assets, the URP tutorial icons, the emoji sprite sheet.

## 11. Technical

- 3 autoloads: `Kit`, `Audio` and `GameState`.
- One `CharacterBody3D` class (`fighter.gd`) for the player and every bot, with the same eight input flags (`move_left/right/up/down`, `jump`, `attack`, `block`, `turbo`). The player's flags come from `Input`; a bot's come from its brain (`ai.gd`).
- Every level scene is one node running `level.gd` with a `level_id`; the level, its bots and pickups are built from `levels.gd`.
- The input map, including the gamepad, is built in code (`GameState._configure_input`).

## 12. Risks and known defects

| ID | Issue |
|---|---|
| R-01 | **After Options in the pause menu, the pause key stops pausing.** `hud.gd` hides the options container on Back but leaves the `OptionsPanel` inside it visible, and `options_panel.gd:52-55` checks its own `visible`, not `is_visible_in_tree()`. Every later Esc, P or Start is taken by the hidden panel: the game keeps running and the pause panel reappears over it. Observed in the `defeat` capture. |
| R-02 | **At the character select, the arrow keys also move the button focus.** They choose a Y Bot (`character_select.gd` `_unhandled_input`), but as `ui_left` / `ui_right` they also move focus between **Back** and **Play**. Right, Right, Left leaves focus on Back, so Enter presses Back: the game returns to the menu and the choice is not saved. The README says the arrow keys choose and Enter plays. Observed in the `extras` capture (Green chosen, Yellow kept). |
| R-03 | **The double-tap run is timed on the wall clock** (`fighter.gd:266`, `Time.get_ticks_msec`), not game time, so it depends on the frame rate: at a low frame rate a double tap is missed, and at a very high one two separate presses can count as one. |
| R-04 | Quitting logs engine warnings: `ObjectDB instances were leaked` and `resources still in use at exit`; two `Lambda capture ... was freed` errors appear during level changes (`captures/*-run.log`). Nothing visible breaks. |
| R-05 | The Windows build has never been run. |
| R-06 | Nobody has played the game by hand. |

## 13. Acceptance tests (OBSERVED)

- `_tools/playtest.tscn`: plays all six levels with the real player physics; PASS in 418 simulated seconds (`playtest.log`). It attaches the AI brain to the player (`player.brain`), sets `level.autopilot` (which turns off the hit-stop) and checks each level's signature move.
- The film captures keep `player.brain` empty, so the player reads `Input` as in normal play. Three takes, 78 of 78 assertions pass: the campaign through all six levels and the credits, a defeat take (a fall, a spike plate, pause and restart) and an extras take (options, the character select by keys, a move showcase, a gamepad). The level 6 stall guard restarted the level once. The same brain runs on the driver's side, and its decisions become key presses (A, D, W, S, Space, J, K, Shift); menus are clicked with the mouse. See `captures/CAPTURE.md`.

## 14. Provenance

The Unity scripts and art came from `inside-godot/` as delivered. Claude (Claude Code) did the porting, the levels, the retargeting, the audio synthesis and this document. No human has reviewed it.

## 15. Open questions (PENDING)

- **OQ-01** Should the double-tap run use game time (R-03)?
- **OQ-02** Target audience and platform.
- **OQ-03** Fix R-01 and R-02 before release: check `is_visible_in_tree()` or free the panel on close; keep the arrow keys off the button focus at the character select.
- **OQ-04** Is the Forewoman's fight fair? The game's own autopilot is knocked out four times in the playtest, and five times in the film capture, before it wins.
- **OQ-05** Should the levels have a stated story, or is the yard enough?
