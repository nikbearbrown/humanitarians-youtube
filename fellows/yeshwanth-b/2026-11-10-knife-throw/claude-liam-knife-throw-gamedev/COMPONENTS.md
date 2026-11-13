# COMPONENTS — Gino: Knife Throw, Inside the Godot Code

Every file of the game is assigned to a component in `gamedev-evidence.json`; `builds/` is excluded (exports, boot-tested separately).

| Component | What it is | Beats |
|---|---|---|
| scenes | Six thin scenes; each level is one Node2D with level.gd and a level_id | B02, B03, B04, B27 |
| level-build | level.gd builds everything from the ASCII maps in levels.gd | B02, B05, B06 |
| player | run, jump, coyote time, buffer, jump cut; playtest autopilot hook | B07, B08 |
| combat | combo chain, HITS table, hit flash shader | B09–B12 |
| knife | substepped flight; dagger pickups | B13, B14 |
| enemies | enemy.gd base, walker, bat, plant | B15–B18 |
| health | damage, heal, death, heart HUD | B19, B20 |
| level-flow | door, level complete, game over, campaign and save | B21, B22 |
| input-map | `_configure_input` | B23, B24 |
| pause-restart | pause, resume, restart; the line-761 defect | B25, B26 |
| menus, audio, tools-and-tests, config, art-assets | summary pass | B27 |
