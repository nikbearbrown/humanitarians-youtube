# COMPONENTS — Night Yard: Inside the Godot Code

Every file of the game snapshot belongs to a component (`gamedev-evidence.json`).

| Component | What it is | Beats |
|---|---|---|
| scenes | Ten thin scenes; each level is one Node3D with level.gd and a level_id. | B02, B03, B04, B31 |
| levels | levels.gd: the six ASCII maps, hints and legends; level.gd builds them, places the backdrop and runs the level. | B02, B05, B06 |
| fighter | fighter.gd: one CharacterBody3D for the player and every bot: movement, jumps, ledges, walls, attacks, hits and deaths. | B07, B08, B09, B10, B11, B12, B13, B14, B15, B16, B21, B22 |
| weapons | weapon.gd: the axe on the floor, in the hand, thrown and dropped; the hammer is spawned by fighter.gd. | B17, B18 |
| bots | ai.gd: the bots' brain (and the playtest autopilot); nav.gd: the grid links it paths over. | B19, B20 |
| traps | spike_trap.gd: the plates. | B23, B24 |
| level-flow | level.gd scoring, gate, checkpoints, death and respawn; game_state.gd campaign, input map and save. | B25, B26 |
| hud | hud.gd: HP, score, gate, hammer, boss bar, hints, K.O., pause, options and Level Clear; options_panel.gd. | B27, B28 |
| menus | main_menu.gd, character_select.gd, stage.gd (the select stage), instructions.gd and credits.gd. | B29, B30, B31 |
| audio | audio.gd autoload: named sounds, loops and music; bus layout. | B31 |
| kit | kit.gd autoload: characters, props, materials and hit effects. | B31 |
| tools-and-tests | _tools: asset converter, bone maps, import patch, animation baker, level drafting aid, icon, screenshots and the playtest. | B31 |
| config | project.godot (3 autoloads, Forward+, Jolt), export presets and README. | B02, B31 |
| art-assets | Y Bot, Amy and Sophie with their clips, the yard pack, props, textures, fonts, UI images and synthesized audio, with import settings. | B31 |
