# FACTCHECK — Stage Runner: The Design Document Came Last

Board excerpts are read from `GDD.md` (in this reel) by line number at build time. The game folder has no GDD of its own and was not modified. Other claims:

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00, B01 | The Walker prompt is reconstructed; the game was rebuilt before its GDD; Unity had two stages and one-touch death | GDD status line; README; `Main Char.cs` | as stated |
| B02 | 14 GDScript files + 1 shader, 2,210 lines; the game's playtest passes; 62 film assertions (23 + 14 + 25); 0 playtests | `wc -l`; `playtest.log` (re-run); `CAPTURE.md` | measured |
| B04 | Countdown, kills, stage clear, clear card: cuts from take `campaign`, in order | frames 350–1510 | observed |
| B05 | Stage 1 in 30.9 s of play, stage 2 in 38.3 s, 0 hits | take `campaign` log (frames 411–1338, 1648–2796) | measured, scripted |
| B06, B07 | moveSpeed 5 × 72 px = 360 px/s; 640 px street; focus 0.5; hitbox radius 13 on a 64 px sprite; fire rate 0.2 s | `Main Char.cs`, `Shooting.cs`; `player.gd`; take `campaign` 558–708 | source, observed |
| B08, B09 | Unity defaults 3 HP / 100 / speed −1; 13 authored types, 2–6 HP, 62–195 px/s; 0.7 s stage-2 interval | `Enemy.cs`, `ArmyStage2.cs`; `enemy.gd` TYPES; take `campaign` 1760–2030 | source, observed |
| B10, B11 | Unity: game over on first touch; rebuild: 3 lives, 1.6 s invulnerability, fireballs cleared on a hit; deliberate contacts, game over, Try Again | `Main Char.cs`; `player.gd`, `game.gd:524-531`; take `defeat` 185–530 | observed |
| B12 | Heart only while a life is missing; one deliberate hit, then a heart | `game.gd:513`; take `extras` 1440–2025 | observed |
| B13 | goalScore is an inspector value; 2000 / 4000 authored | `GameManager.cs`; `game.gd` STAGES | source |
| B14, B15 | 110 HP, 5000 points, shield, 4-step cycle, enrage at 55; victory 30.4 s after GO, 3 lives | `boss.gd`; take `campaign` 3106–4075 | observed |
| B16, B17 | Unity RestartGame() loads StageOne; rebuild restarts the current stage; R logs SCRIPT ERROR at game.gd:606 | `UI Manager.cs`; `game.gd:595-606`; `extras-run.log` | observed |
| B18 | Mirrored scrolling street; source art; 15 synthesized sounds and 3 loops | `game.gd` _build_background; `audio.gd`; `_tools/make_assets.py` | source |
| B19 | stage_1.tscn is 7 lines; 113 live nodes at 8 s | `scenes/stage_1.tscn`; `../stage-runner-captures/tree_probe.txt` | measured |
| B20 | Spawn comment says ±4.5 units; code uses ±288 px = 4 units | `enemy.gd:62-64`; README | source |
