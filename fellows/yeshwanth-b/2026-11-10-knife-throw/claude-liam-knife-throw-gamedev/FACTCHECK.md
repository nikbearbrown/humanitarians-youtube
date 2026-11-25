# FACTCHECK — Gino: Knife Throw, Inside the Godot Code

Every code panel is read verbatim from the game's files by line number at build time (`gamedev-evidence.json` `excerpts`). Every result beat is an exact-frame window of a scripted-input take of the same build (`cffbb01`).

| Pair | Claim | Evidence |
|---|---|---|
| B02 | Saved level scene is 1 node; live at 8 s, 200 nodes: tile map, 3 rock bodies, 61 prop sprites, 13 pickups, Gino and 5 enemies, camera, HUD and menu layers | `evidence/tree_probe.txt` (headless probe of `res://scenes/level_1.tscn`, no input) |
| B03–B04 | `level_1.tscn` is 7 lines with `level_id = 1` | `scenes/level_1.tscn`; take `campaign` 314– |
| B05–B06 | Map letters P, b/w/p, o/O/k/h, D, 1–9 become entities | `level.gd:380-436`; take `campaign` 420– |
| B07–B08 | RUN_SPEED, coyote/buffer jump, JUMP_CUT 0.45, gravity cap; the long jump is the driver's choice | `player.gd:157-175`; take `campaign` 2380– (driver note `guarded_descent`) |
| B09–B10 | Combo advances on a finished swing if queued, combo < 4, on floor; takes show at most 2-hit chains | `player.gd:256-267`; logged `combo` ≤ 2 in all takes |
| B11–B12 | HITS rows; 20 / 40 damage; five hits on the first walker, +25 | `player.gd:54-60`; take `campaign` slashes 731–830, kill 833 |
| B13–B14 | 4 substeps, 30 damage, rock check, 1.3 s lifetime | `knife.gd:28-45`; take `campaign` knife 1610 |
| B15–B16 | Walker faces, chases inside its range only if `_can_walk`; bite after the gap jump | `walker.gd:54-66`; take `campaign` hit 5366, kill 5452 |
| B17–B18 | Bat stops during the 0.7 s wind-up, then opens the strike box; cones both sides | `bat.gd:46-72`; take `campaign` 2880–3070 |
| B19–B20 | Hit ignored while invulnerable; HURT 0.35 s, INVULNERABLE 1.1 s; knockback (130, −170) | `player.gd:288-311`; spike hit at campaign 4816 (log label "bat" is the nearest enemy; frame shows spikes) |
| B21–B22 | Door → 0.8 s → complete_level, paused tree, panel text | `level.gd:821-839`; campaign 1996–2160 (panel 135, 6/10, 3/5, 0, 0:43) |
| B23–B24 | Input map built in `_configure_input` | `game_state.gd:170-192`; take `extras` |
| B25–B26 | `_restart()` then `get_viewport()` on line 761 | `level.gd:749-761`; `capture/defeat-run.log` SCRIPT ERROR at `level.gd:761` |
| B27 | Menus, credits, audio, `_tools` (levels.py, make_assets.py, screen, playtest with the `autopilot` hook) | `scripts/`, `_tools/`; `player.gd:75` |

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
