# COMPONENTS — Delta: Inside the Godot Code

Every file of the game is assigned to a component in `gamedev-evidence.json`; `builds/` is excluded (exports, boot-tested separately).

| Component | What it is | Beats |
|---|---|---|
| scenes | Fifteen thin scenes; each level is one Node3D with level.gd and a level_id | B02–B04, B29 |
| levels | The twelve ASCII maps; level.gd builds them | B02, B05, B06 |
| player | movement, look, input | B07, B08 |
| interaction | the ray, pickable items, holder devices | B09, B10 |
| shifting | DimensionSwitcher port, switch_target, glitch shader | B11–B14 |
| devices | power ports and every device | B15–B20 |
| guardians | final.gd | B21–B24 |
| hud | HUD, pause, options | B25, B26 |
| level-flow | pause input, completion, campaign and save | B27, B28 |
| menus, audio, kit, tools-and-tests, config, art-assets | summary pass | B29 |
