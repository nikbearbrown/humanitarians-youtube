# FACTCHECK — Night Yard, Every Feature, Played

Every gameplay beat is one exact-frame window of a scripted-input take in `../inside-captures` (build 54ad5ab); the windows and each feature's action frame are in `content.py` and `coverage.json`. Frames below are 30 fps video frames of the take named.

| Beats | Claim | Evidence |
|---|---|---|
| B00–B01 | 6 levels, 3 Y Bots, 17 scripts, 5,215 lines; 3 takes, 78 of 78 assertions | `wc -l scripts/*.gd`; `capture/*-inputs.jsonl` (39 + 22 + 17, 0 fails) |
| B03 | hover light, click Yellow, Play | campaign clicks at 609 ("Y Bot YELLOW") and 688 ("Play") |
| B05 | ledge grab and climb; flying kick; +10 a bot | campaign state HANG 1152, CLIMB 1153, attack flying_kick 1187; score 50 → 70 |
| B06 | the gate opens at 100 | campaign 1610 "Gate open"; score 100 |
| B07 | Level Clear: time, score, KOs, deaths | campaign 2000 (panel) |
| B09 | jab, cross, kick; wall slide 2734, wall jump 2735, grab 2746 | campaign state log |
| B12 | axe picked up 3984, thrown 4002 | campaign state log |
| B14 | ledge grab with the axe (4817, holding true), thrown from the catwalk (5132) | campaign state log |
| B15 | hammer 5550; 9 s recharge | campaign state log; `fighter.gd` `HAMMER_COOLDOWN` |
| B17 | slide 6434 | campaign state log |
| B19 | takedown 7321 | campaign state log; level 4 signature move takedowns 1 |
| B21–B24 | 14 bots, 14 KOs, 0 deaths in level 5; 3 Amys in the map | level_done at 9197 (kos 14, deaths 0); `levels.gd` level 5 ("m" ×3) |
| B26 | the stall guard restarted level 6 after 60 s without progress | event `stall_restart` at 11551 (x 17.4, score 30); click "Restart level" 11610 |
| B27 | four axe swings, the boss bar 12 → 10 | campaign attacks "axe" 11994–12237; boss_hp 12.0 → 10.0 |
| B28–B31 | five K.O.s; You Win 1:44 | campaign DEAD states; You Win panel (frame 14800): Time 1:44, Times K.O.'d 5 |
| B33 | Continue; Select level with best times | defeat 60 (Continue 06), 135–180 (best times) |
| B34 | the fall is a K.O.; back at the start | defeat DEAD 631 at y −3.4; respawn x 2.5 |
| B35 | the plate kills; respawn at the checkpoint | defeat DEAD 1645; assert "respawn at the checkpoint, not the start" |
| B36 | Esc pauses; R restarts while paused | defeat asserts "Esc pauses", "R restarts the level while paused" |
| B37 | R-01: after Options, Esc shows the panel without pausing | defeat event `defect_options_eats_pause` at 2234 (tree_paused false, pause_panel_shown true); `options_panel.gd:52-55` |
| B39 | R-02: arrows move the focus; Enter presses Back; Green not saved | extras 505 (selected GREEN, then Enter), fighter stays YELLOW; `character_select.gd:125-128, 170-176` |
| B41 | jab 800, cross 810, uppercut 852, block 897–937, hammer 953 | extras state log |
| B43 | pad stick, A, X, Start | extras joypad events; assert "Start pauses" |

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
