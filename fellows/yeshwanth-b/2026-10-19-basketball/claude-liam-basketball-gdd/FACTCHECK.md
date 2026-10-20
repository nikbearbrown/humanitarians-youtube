# FACTCHECK — Basketball Blaster: The Design Document Came Last

Every board excerpt is read from `GDD.md` by line number at build time (`make_sheet.py`). The table below covers the spoken and carded claims that are not excerpts.

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00 | The Walker prompt is a reconstruction; the game was built before its GDD | `GDD.md` status line; README | as stated, labelled on screen |
| B01 | A Unity arena shooter ported to Godot, three arenas | README "Ported from Unity", "Additions" | source |
| B02 | 14 GDScript files + 1 shader, 2,408 lines; 8 scenes | `wc -l scripts/*`; `scenes/` | measured 2026-10-15 |
| B02 | Two scripted takes, 59 of 59 assertions (46 + 13); 0 human playtests | `CAPTURE.md`; takes' input logs | measured. The third take, `extras` (17 more), postdates this film's claim and is not counted here |
| B03 | No document says who the game is for | README, GDD §2 | as stated |
| B04 | Life lost, respawn, eggs, COURT CLEARED; kills never end a level | take `campaign` frames 2440–2960; `game.gd:559-560` | observed + source |
| B05 | Egg routes took 12.6 / 13.6 / 18.7 s; the fight phase 25.6 s, 10 kills, 1 life, 0 eggs | input log frames (2471→2866, 3398→3859, 3977→4622, 1694→2471) | measured, scripted |
| B06 | Unity `PlayerInput.cs:44` declares `public bool Jetpack;`, nothing reads it | grep of `unity-scripts/scripts` | source |
| B06 | Jetpack: 1.6 s fuel, rise capped at 430 px/s; coyote 0.5 → 0.15 s; fire 0.5 → 0.4 s | `player.gd` constants; `PlayerController.cs`, `Gun.cs` | source |
| B07 | Walk, jump, double jump, jetpack, fire every 0.4 s, grenade; two hits | take `campaign` 1226–1694; health 3 → 1 in the log | observed |
| B08 | Mega kill = 3+ deaths before the next physics frame, from Unity's AudioManager | `AudioManager.cs` (`megaKillAmount = 3`); `game.gd:470-479` | source |
| B09 | Life lost at about frame 1728; grenade kills four (kills 0 → 4 at 1795) | input log | observed; the replay is labelled |
| B10 | 3 health, 1 s invulnerable, 2 s after respawn, gate cleared within 260 px; gate clearing is not in Unity | `game.gd:491-534`; `Fade.cs` only respawns | source |
| B11 | Three lives lost, defeat screen text, Retry restores 3 lives | take `defeat` 485–1150; assertions | observed |
| B12 | Contact is a distance check (58 px); no automated tests | `game.gd:481-489`; no test files in the project | source |
| B13, B14 | Arena table; arenas 2 and 3 on screen | `game.gd:_get_level_config`; take `campaign` | source + observed |
| B15, B16 | 8-line briefing; clicks don't advance; Enter does | `intro_briefing.gd`; take `campaign` 440–640 and assertions | observed (defect D-01) |
| B17 | Sounds synthesized; Unity export had no audio; art rights unrecorded | README "Additions", "Asset notes"; no licence file | as stated |
| B18 | HUD hints overlap the bars | still from take `defeat` frame 250, cropped; `bar_probe.txt` | observed (defect D-02) |
| B19 | Verdict lines | the rows above | summary |

**Not claimed:** fun, difficulty as felt, fairness, accessibility, balance. No person has played the build.
