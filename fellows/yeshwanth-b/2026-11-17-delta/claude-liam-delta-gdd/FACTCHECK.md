# FACTCHECK — Delta: The Design Document Came Last

Board excerpts are read from `GDD.md` by line at build time (`gdd-evidence.json`). Gameplay beats are exact-frame cuts of the scripted-input takes in `../delta-captures`.

| Beats | Claim | Evidence |
|---|---|---|
| B00–B01 | Unity left 64 scripts and art but no levels, scenes or sound; the GDD was written after the build | `unity-scripts/scripts` (64 `.cs`, 5,091 lines); game README "The Unity export had the scripts and art but no scenes, levels or audio" |
| B02 | 27 GDScript files + 3 shaders, 5,319 lines; 90 film assertions; 0 human playtests | `wc -l scripts/*`; `capture/*-inputs.jsonl` (25 + 21 + 28 + 16 passes, 0 fails) |
| B04 | Banner → F pick → E socket → door → lift → panel | take `campaign1` frames 304–1115 |
| B05 | No death in the campaign takes; the driver reads the guardian timers (`spark_locked`, `wave_radius`) | `capture/campaign*-inputs.jsonl` (`dead` never true); `../delta-captures/takes.gd` `_guard` |
| B06–B07 | FirstPersonController MoveSpeed 4, Sprint 6, JumpHeight 1.2, SpeedChangeRate 10; coyote 0.1 s; mouse 0.11° / px; look only while captured | `FirstPersonController.cs`; `player.gd` constants and line 121; take `extras` 568–738 |
| B08–B09 | 3 m ray; F / E; the prompt; charger | `InteractionManager.cs` interactionDistance; `player.gd:254-298`; take `campaign1` 2730–2920 |
| B10–B11 | 0.3 s glitch, ±50 m; refusal added | `DimensionSwitcher.cs`; `level.gd:673-694`; take `campaign1` 1235–1345 |
| B12–B13 | 11 device types; arc gate rejects charged cells; duplicator; console scan and teleport | `scripts/*.gd`; take `campaign2` 2010–4455 |
| B14–B15 | Die() reload; respawn; item respawn; plasma | `HealthManager.cs`, `RespawnTrigger.cs`; take `defeat` 1935–5815 |
| B16–B17 | First attack at 17 s, every 20 s, follow 5 s, lock 3 s, 3 m; shield destroyed by a strike | `BossManager.cs` `CallWithDelay(StartAttacks, 17f)`, `timeBetweenAttacks = 20f`; `final.gd`; take `campaign2` 9240–13640 |
| B18–B19 | 12 ASCII maps on a 5 m grid; level banners | `levels.gd`; take `campaign2` |
| B20–B21 | Pause menu clicks blocked by the options `CenterContainer`; R while paused ignored | `hud.gd:313-318`; `level.gd:804-818`; take `defeat` 2063–2483 |
| B22–B23 | 33 effects, 3 loops, 3 music tracks synthesized; one node per level | game README; `scenes/level_01.tscn` |
| B24 | R-01 to R-06; the playtest never pauses and steers the player directly | `GDD.md` §12; `_tools/playtest.gd` |

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
