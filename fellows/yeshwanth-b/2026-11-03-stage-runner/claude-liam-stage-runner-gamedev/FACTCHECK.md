# FACTCHECK — Stage Runner: Inside the Godot Code

Code panels are Godot editor reconstructions; their text is read verbatim from the hashed source files at build time. Each is followed by real engine output of the same build (`d90fa19`), cut from the scripted-input takes without retiming.

| Pair | Source | Observed result |
|---|---|---|
| B03 → B04 | `scenes/stage_1.tscn:1-7` | Stage 1 loads fully built: scrolling street, side panels, STAGE 1 banner, countdown, first monsters. |
| B05 → B06 | `scripts/game.gd:19-34` | Stage 1 HUD shows five Incoming monster icons and "Reach 2000 points to clear the stage." |
| B07 → B08 | `scripts/player.gd:95-102` | With Shift held the wisp slows and the white hitbox dot appears. |
| B09 → B10 | `scripts/player.gd:122-131` | After collecting a triple shot, each shot fires three bullets in a fan. |
| B11 → B12 | `scripts/enemy.gd:96-108` | Stage 2 shows weaving, hunting and hopping monsters together. |
| B13 → B14 | `scripts/game.gd:511-516` | With 2 lives, a heart drops and is collected: +1 LIFE, three hearts. |
| B15 → B16 | `scripts/player.gd:152-164` | Three deliberate contacts: two lives lost with blinking, then the wisp bursts. |
| B17 → B18 | `scripts/game.gd:550-558` | GAME OVER menu with the crying face and "Score: 0 /2000"; Try Again restarts. |
| B19 → B20 | `scripts/game.gd:576-591` | STAGE CLEAR! banner, the wisp flies off the top, then the Stage 1 Clear card. |
| B21 → B22 | `scripts/boss.gd:94-106` | The Cerberus fires a red fan, an orange ring, another fan, then summons minions. |
| B23 → B24 | `scripts/boss.gd:135-150` | Shots are absorbed during the walk-in; at 55 HP the boss is tinted red and enraged. |
| B25 → B26 | `scripts/game_state.gd:122-136` | Arrows + Z, held left mouse, and synthetic pad stick + A all move and fire. |
| B27 → B28 | `scripts/game.gd:595-606` | R on the pause menu restarts the stage; extras-run.log records the SCRIPT ERROR at game.gd:606. |
| B29 → B30 | `scripts/game_clear.gd:94-106` | Credits scroll up over the restored city and stop; Main Menu is clicked. |

**Other claims.**
- B01, B02: 7 scenes, 14 scripts and a shader, 2,210 lines (`wc -l`). `stage_1.tscn` is 7 lines; 113 live nodes at 8 s (`evidence/tree_probe.txt`).
- B31: 15 sounds and 3 loops (`audio.gd`), synthesized by `_tools/make_assets.py`. The playtest steers through `player.autopilot` (`player.gd:30`, `_tools/playtest.gd`).
- B28: the script error appears only in `capture/extras-run.log`; the screen shows a normal restart.
- **Visual exemption.** Result beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
