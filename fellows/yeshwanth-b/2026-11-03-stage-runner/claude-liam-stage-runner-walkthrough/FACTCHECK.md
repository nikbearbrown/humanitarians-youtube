# FACTCHECK — Stage Runner: Every Feature, Played

Every gameplay beat is an exact-frame window of a scripted-input take. `coverage.json` ties each of the 40 shown features to a frame inside its beat's window.

| Beats | Claim | Evidence |
|---|---|---|
| B00 | 3 stages, 13 monster types, a boss, 14 scripts; 3 takes, 62 of 62 assertions | `enemy.gd` TYPES; `ls scripts`; `../stage-runner-captures/CAPTURE.md` |
| B02–B04 | Menu with BEST SCORE 0; How to Play; Esc back; countdown; WASD + J; Shift focus with the hitbox dot | take `campaign` 0–740 |
| B05–B06 | Triple shot (3 bullets, 10 s, timer bar); white hit flash; clear at exactly 2000 points; the wisp flies off | take `campaign` 740–1416; `player.gd` SPREAD_TIME |
| B07 | Clear card: 2000, 18 monsters; Stage 2 "three times as fast" | take `campaign` 1416–1700; intervals 2.0 and 0.7 s |
| B08–B09 | Arrows + Space; 0.7 s spawns; weave / sprint / hunt / ooze 6 HP; 0 hits; clear at 4050 | take `campaign` 1700–2874; `enemy.gd` TYPES |
| B10–B12 | Stage 3 tinted stage-1 street; shielded walk-in; fan 5 → ring 12 → fan 5 → 2 minions; enraged at 55 HP; fans 7, rings 16; +5000 | take `campaign` 2874–4097; `boss.gd` |
| B13 | Final score 12250, 58 monsters; BEST SCORE saved | take `campaign` 4097–4549 |
| B14–B15 | Deliberate contacts; red flash; game over with the crying face, Score 0 /2000, tree paused; Try Again; pause menu | take `defeat` |
| B16–B19 | Audio button; arrows + Z; mouse fire; M; P; pause-menu audio; Resume; Esc + R with SCRIPT ERROR at game.gd:606; pad stick / A / LB / Start | take `extras` 0–1419; `extras-run.log` |
| B20 | One deliberate hit (frame 1459); triple shot at 1904; heart dropped at 1958, collected at 1994 (lives 3) | take `extras` 1419–2176, game-state snapshots |

**Not shown, listed in `coverage.json`:** F11 fullscreen, Quit, Play Again, game over in stage 3, the focus-loss pause, game audio.

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
