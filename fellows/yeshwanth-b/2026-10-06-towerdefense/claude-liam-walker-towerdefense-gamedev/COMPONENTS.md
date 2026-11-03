# COMPONENTS — Walker Tower Defense: Inside the Godot Code

Teaching contract `code-then-result-v1`: each code beat is immediately followed by a beat showing what those lines do in the real build (`caf082c`).

| Component | Files | Explanation | Beats |
|---|---|---|---|
| `scene-root` | `game/main.tscn`, `game/session.gd`, `project.godot` | One six-line scene; session.gd constructs and owns the board, HUD and entities; project settings. | B02, B03, B04 |
| `input` | `game/session.gd` | Runtime InputMap registration and _unhandled_input routing. | B05, B06 |
| `grid-and-routing` | `features/grid/grid.gd`, `features/grid/astar.gd`, `features/grid/tile_kinds.gd`, `levels/level_01.json` | Level JSON, tile rules, 4-neighbour A*, and the no-seal placement rule. | B07, B08 |
| `simulation-clock` | `game/session.gd` | One fixed-step world loop running at 3x the source rate, times a player 1x/2x/3x. | B09, B10 |
| `monsters-and-damage` | `features/monsters/monster.gd`, `features/monsters/monster_tuning.gd` | Monster movement, flat damage, status timers and drawing; recovered monster stats. | B11, B12, B13, B14 |
| `waves` | `features/waves/wave_spawner.gd`, `features/waves/wave_tuning.gd` | Wave release cadence and the compounding health ramp that feeds take_damage. | B11 |
| `projectiles` | `features/projectiles/projectile.gd` | Four delivery styles; Storm chain selection with the source coin flip. | B15, B16 |
| `debug-overlay` | `game/session.gd` | F1 playtest overlay drawn in session._draw beneath the Grid child. | B17, B18 |
| `towers-and-art` | `features/towers/tower.gd`, `features/towers/tower_tuning.gd`, `ui/hud.gd` | Tower targeting and procedural drawing shared with the HUD build bar and ghost; tower stat table. | B19, B20 |
| `tests` | `tests/test_keyboard.gd`, `tests/test_data.gd`, `tests/test_game.gd`, `tests/test_match.gd`, `tests/check_persistence.gd`, `tests/capture_game.gd`, `tests/capture_boot.gd` | Headless SceneTree suites; only the keyboard suite drives real input events. | B21, B22 |
| `level-load` | `game/session.gd`, `features/grid/grid.gd` | Level validation and the load-error surface. | B23, B24 |

**Excluded:**

- `.gitignore`: Version-control ignore list; no runtime role.
- `export_presets.cfg`: Export presets (macOS, Windows, Linux). Exports were not run or shown in this film; every capture ran the project from source.

## Code → result pairs

| Code beat | Excerpt | Result beat | Result evidence | Observed |
|---|---|---|---|---|
| B03 | `game/main.tscn:1-6` | B04 | take `opening` | Boot of the real main scene: board, HUD and menu card appear; START begins a run. |
| B05 | `game/session.gd:460-470` | B06 | take `opening` | Keys 2, 4 and Esc and a right-click, delivered as input events, drive build mode and refusals. |
| B07 | `features/grid/grid.gd:152-162` | B08 | take `maze` | Seal of the spawn corner refused with "Would block the path"; a tower on the road accepted and the route changes. |
| B09 | `game/session.gd:21-30` | B10 | take `opening` | SPEED button to 2x, F to 3x, F back to 1x, during waves 2 and 3. |
| B11 | `features/monsters/monster.gd:112-120` | B12 | take `opening` | Wave 1 against an upgraded Fire tower: hits flash white, bars drop, kills raise gold from 0 to 8. |
| B13 | `features/monsters/monster.gd:74-84` | B14 | take `poison` | The poisoned lead monster of wave 2 stays pale white rather than green. |
| B15 | `features/projectiles/projectile.gd:129-139` | B16 | take `storm` | The beam is visible for frames 173-178 (0.2 s) at real speed, then replayed at 1/8 speed, labelled. |
| B17 | `game/session.gd:596-600` | B18 | take `poison` | The F1 overlay is cut off at the board edge; only its left 88 logical px are visible. |
| B19 | `features/towers/tower.gd:135-142` | B20 | take `opening` | An upgraded Fire tower gains the chevron; the panel reads SELL 34 and MAXED. |
| B21 | `tests/test_keyboard.gd:33-41` | B22 | recorded test receipts (ExecutedData) | Receipt keyboard-1790012997.43825.json: 8 of 9 FAIL with the fix reverted; keyboard-1790606725.01996.json: 9 of 9 PASS. |
| B23 | `game/session.gd:91-96` | B24 | take `broken` (STAGED) | With level_01.json missing "exit": the error panel is covered by the menu card; Enter sets PLAYING and Space starts wave 1 behind a frozen HUD. |
