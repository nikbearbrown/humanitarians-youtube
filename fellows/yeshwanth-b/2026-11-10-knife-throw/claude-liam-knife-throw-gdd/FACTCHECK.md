# FACTCHECK — Gino: Knife Throw, The Design Document Came Last

Board excerpts are read from `GDD.md` by line at build time (`gdd-evidence.json`). Gameplay beats are exact-frame cuts of the scripted-input takes in `../knife-throw-captures`.

| Beats | Claim | Evidence |
|---|---|---|
| B00–B01 | Unity left 40 scripts and art but no levels, scenes or sound; the GDD was written after the build | `unity-scripts/scripts` (40 `.cs`, 1,865 lines); game README "The Unity export had the scripts and art but no scenes, levels or audio" |
| B02 | 14 GDScript files + 1 shader, 2,620 lines; 46 film assertions; 0 human playtests | `wc -l scripts/*`; `capture/*-inputs.jsonl` (20 + 15 + 11 passes, 0 fails) |
| B03 | Wind-ups 0.2 / 0.7 / 0.6 s; combo 20 + 20 + 20 + 40; 3 knives, 30 damage | `walker.gd` BITE_DELAY, `bat.gd` WINDUP, `plant.gd` WINDUP, `player.gd` HITS, `knife.gd` DAMAGE |
| B04 | Banner → fight → door (W) → LEVEL COMPLETE | take `campaign` frames 318–2253 |
| B05 | Level 1 in 0:43 with no hits; combo never above 2; level 3 cleared on health 1 | take `campaign` panel frame 2100; logged `combo`; frame 6695 assert "level 3 cleared (health 1)" |
| B06 | Unity `speed` 50 AddForce; 105 px/s; coyote 0.1 s; buffer 0.12 s; jump cut 0.45 | `PlayerController.cs`; `player.gd` constants |
| B07 | Jump speed 320 px/s; the long jump past the walker is the driver's `guarded_descent` | `player.gd` JUMP_SPEED; take `campaign` frame 2400 note |
| B08–B09 | `AttackTrigger.cs` dmg 20; Attack4 40; single slashes and two-hit chains only in the takes | `player.gd` HITS; take `defeat` 640–1033 |
| B10–B11 | 420 px/s, 1.3 s, 30 damage, leaves 0.15 s in; knife hits the walker at frame 1610 | `knife.gd`, `player.gd` THROW_DELAY; take `campaign` |
| B12–B13 | `EnemyAttack.cs` dmg = 2; 100 HP and 25 points authored; plant cone reaches 46 px | `enemy.gd`; `plant.gd` CONE Rect2(6, -34, 40, 34) |
| B14–B16 | maxHealth 6; enemy 2, spike 1, pit = level; 1.1 s invulnerable; spike at frame 4816 (log label says bat; the frame shows spikes); bite at 5366; pit at defeat 1487; Retry | `player.gd`; takes `campaign`, `defeat` |
| B17–B18 | Levels are ASCII maps checked and route-simulated by `_tools/levels.py`; 5 / 7 / 12 enemies; bridge columns 91–97 vs pit 92–98 | `levels.gd`; `level.gd` `_build_grid`; trial log `trial/c1.log` |
| B19–B20 | Unity menus; Continue, How to Play, M, R added; SCRIPT ERROR at `level.gd:761` | `level.gd`; `capture/defeat-run.log` |
| B21–B22 | 16 px tiles, light and dark; 23 effects and 3 loops synthesized; one node per level scene | `level.gd` TILE; `audio.gd`; `scenes/level_1.tscn` |
| B23 | R-01 to R-06; 5 open questions | `GDD.md` §12, §15 |

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
