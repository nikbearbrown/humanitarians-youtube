# FACTCHECK — Night Yard: The Design Document Came Last

Board excerpts are read from `GDD.md` by line at build time (`gdd-evidence.json`). Gameplay beats are exact-frame cuts of the scripted-input takes in `../inside-captures` (build 54ad5ab).

| Beats | Claim | Evidence |
|---|---|---|
| B00–B01 | Unity left 150 scripts and art but no scenes, levels or sound; the GDD was written after the build | `inside-godot/unity-scripts` (150 `.cs`, 9,615 lines); game README "The Unity export had the scripts and the art but no scenes, animator controllers, ability assets or audio" |
| B02 | 17 GDScript files, 5,215 lines; 78 film assertions; 0 human playtests | `wc -l scripts/*.gd`; `capture/*-inputs.jsonl` (39 + 22 + 17 passes, 0 fails) |
| B04 | Banner, a light (+10), a flying-kick K.O. (+10), the gate at 100, Level Clear | take `campaign` frames 700–2030 (`clips.py` core_loop) |
| B05 | The script knows the map; 5 K.O.s by the Forewoman | the bot brain plans over `nav.gd` links; Level Clear panel "Times K.O.'d 5" (campaign frame 14800) |
| B06–B07 | walk 1.65 m/s, run 5.2 m/s, 0.18 s double tap on the wall clock; walk, Shift run, jump in play | `fighter.gd` constants and line 266; take `campaign` 785–960 (Shift down 785, up 811; Space 936) |
| B08–B09 | jump 9.6 m/s (apex 2.1 m), ledge for 3–4 m walls, 3-wide running jump, wall slide 2.2 m/s; the shaft | `fighter.gd` constants; `levels.gd` movement rules; take `campaign` 2690–2810 (WALL_SLIDE 2734, WALL_JUMP 2735, HANG 2746) |
| B10–B11 | 16 attacks; jab → cross → kick 0.34 / 0.34 / 0.5; hammer 9.0, unblockable, 9 s | `fighter.gd` `ATTACKS`, `HAMMER_COOLDOWN`; take `extras` 790–1020 (jab 800, cross 810, uppercut 852, block 897, hammer 953) |
| B12–B13 | axe pick up, swing, throw (run + attack), put down; flies straight, spinning | `fighter.gd:372-382`, `weapon.gd`; take `campaign` 3960–4060 (PICKUP 3984, throw 4002) |
| B14–B15 | maxHP 100, maxScore 100, light 10; plate fires 0.4 s after a step, retracts after 1.5 s; respawn at the checkpoint | `HPManager.cs`, `ScoreManager.cs`, `PickupItem.cs`; `spike_trap.gd`; take `defeat` 1560–1760 (DEAD 1645) |
| B16–B17 | the Unity AI ported; bots start unaware; Sophie 12 HP, blocks, hammer | `ai.gd` `_notice`; `level.gd` enemy table (`"S": hp 12.0, block 0.6`); take `campaign` 12560–12700, 13880–13990 |
| B18 | 6 ASCII maps on a 1 m grid, one move each | `levels.gd` |
| B19–B20 | hover light, click, Return / Play; added menus | `character_select.gd`; take `campaign` 430–700 (click Yellow 609, Play 688) |
| B21 | seeded backdrop, cutaway, SkeletonProfileHumanoid retargeting, 31 sounds synthesized | game README; `level.gd`; `_tools/make_assets.py` |
| B22 | one fighter class, 8 input flags | `fighter.gd:196-205` |
| B23–B24 | R-01: after Options in the pause menu, Esc shows the panel without pausing | `hud.gd:225-235`, `options_panel.gd:52-55`; take `defeat` 1965–2265 (event `defect_options_eats_pause` at 2234: `tree_paused false`, `pause_panel_shown true`) |
| B25 | the playtest attaches the brain to the player; the captures keep `player.brain` null | `_tools/playtest.gd` (`player.brain = brain`); `capture/*-inputs.jsonl` `bridge_on` (`player_brain_is_null: true`) |
| B26 | verdict lines | the rows above |

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
