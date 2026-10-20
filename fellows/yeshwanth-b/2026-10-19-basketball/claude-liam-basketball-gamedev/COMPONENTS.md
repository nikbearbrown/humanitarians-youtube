# COMPONENTS — Basketball Blaster: Inside the Godot Code

Every file in the project (except `.godot/`, `.uid` and the `builds/` exports) is assigned to a component in `gamedev-evidence.json`.

| Component | Files | Beats |
|---|---|---|
| scenes | `scenes/level_1-3.tscn` | B02–B04 |
| level-builder, level-data | `scripts/game.gd` | B02, B04–B06 |
| input, state-and-config | `scripts/game_state.gd`, `project.godot`, bus layout, export presets, README | B07, B08, B29 |
| player | `scripts/player.gd` | B09–B14 |
| projectiles | `scripts/bullet.gd`, `scripts/grenade.gd` | B13–B16 |
| shader, chickens-and-pipes | `hit_flash.gdshader`, `chicken.gd`, `pipe.gd` | B17, B18 |
| mega-kill, damage, eggs, hud | `scripts/game.gd` | B19–B24, B27, B28 |
| briefing | `intro_briefing.gd`, `intro.tscn` | B25, B26 |
| menus-and-end-screens | `main_menu.gd`, `instructions.gd`, `end_screen.gd` and 4 scenes | B29 |
| audio, effects | `audio.gd`, `effects.gd`, `spotlight.gd` | B20, B29 |
| art-assets | all of `assets/` with `.import` sidecars | B29 |

**Excluded:** `builds/` (the macOS app and Windows .exe). These are export artefacts, boot-tested separately.
