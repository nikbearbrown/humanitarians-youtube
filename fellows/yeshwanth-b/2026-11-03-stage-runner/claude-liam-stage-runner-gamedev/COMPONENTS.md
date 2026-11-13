# COMPONENTS — Stage Runner: Inside the Godot Code

Every project file (except `.godot/`, `.uid` and `builds/`) is assigned a component in `gamedev-evidence.json`. Components:

- **scenes**: Seven thin scenes; each stage is one Node2D with game.gd and a stage_id.
- **stage-config**: game.gd builds the background, world, HUD and overlay from the STAGES table.
- **player**: player.gd: input vector, focus, clamp, contacts and the playtest-only autopilot hook.
- **shooting**: player.gd _shoot and bullet.gd: fire rate, spread angles, one damage per bullet.
- **enemies**: enemy.gd TYPES and patterns, hit_flash.gdshader, effects.gd bursts and score popups.
- **drops**: _drop_pickup in game.gd and pickup.gd (heart or triple shot).
- **lives**: take_hit in player.gd and the mercy rule in game.gd.
- **game-over**: _show_game_over in game.gd: score text, menu, paused tree.
- **stage-flow**: _stage_clear in game.gd, stage_clear.gd, and the campaign state in game_state.gd.
- **boss**: boss.gd attack cycle, shield and enrage; enemy_bullet.gd fireballs.
- **input-map**: GameState._configure_input builds every key, mouse and pad binding at startup.
- **pause-restart**: _unhandled_input, _pause, _resume and _restart in game.gd; the line-606 defect.
- **credits**: game_clear.gd: Thanks.cs scroll, computed stop, Play Again and Main Menu.
- **menus**: main_menu.gd and instructions.gd: the title screen, best score, audio button and How to Play.
- **audio**: audio.gd autoload: 15 named sounds, 3 music loops, a pool of 20 voices, the audio toggle; bus layout.
- **tools-and-tests**: _tools: the asset synthesizer, a screenshot driver and the autopilot playtest.
- **config**: project.godot (2 autoloads, 1280×720, canvas_items), export presets and README.
- **art-assets**: Stage paintings, monster sprites, FX textures, UI images, fonts and audio files with their import settings.

**Excluded:** `builds/`: exports, boot-tested separately (`export-boot.log`).
