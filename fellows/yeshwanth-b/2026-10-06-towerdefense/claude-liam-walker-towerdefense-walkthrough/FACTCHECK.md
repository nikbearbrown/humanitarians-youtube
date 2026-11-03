# FACTCHECK — Walker Tower Defense: Every Feature, Played

**Build:** `caf082c`, snapshot `f5035b75…3bdd`, Godot 4.7.2.

Every gameplay claim is anchored to a logged input frame in `capture/<take>-inputs.jsonl`. The frames were also inspected (`_qc/`).

| Beat | Claim | Evidence | Status |
|---|---|---|---|
| B00 | Prompt reconstructed, not a transcript | No GDD-first prompt exists; GDD written afterwards | ✅ |
| B01 | One map, four towers, endless waves; played by a script | `level_01.json`; D-04; `CAPTURE.md` | ✅ |
| B02 | Best wave zero on a fresh save; 50 gold, 5 lives | `opening` frame 51 (best 0); frame 111 | ✅ |
| B02 | Lava refused | `opening` frame 273, refusal kind 2 | ✅ |
| B03 | Ice placed, five gold left; Storm refused for gold; Esc leaves build mode | frames 511, 591, 627 | ✅ |
| B03 | Each kill pays four | gold 5 → 13 over wave 1 (2 kills) | ✅ |
| B04 | Speed button 2×, F 3×; lives drop to three; run over at wave three; best 3 | frames 959, 1005, 1032, 1366 | ✅ |
| B05 | Sell 10 / upgrade 30; chevron, MAXED; upgrades exactly once | frames 1676, 1720; `tower.gd:40` `can_upgrade` | ✅ |
| B06 | Monster in the way refused; both wave-1 monsters leak | `maze` frame 104 (kind 3); lives 5 → 3 by frame 318 | ✅ |
| B07 | Seal refused; message gone in 0.3 s; tower on road reroutes; sold for 10 | `maze` frames 486, 610, 896; `session.gd:42` | ✅ |
| B08 | F1 overlay barely readable: the board is drawn on top of it | `session.gd:599` vs Grid child `:92`, origin x 96 | ✅ defect |
| B09 | A poisoned monster goes pale, not green | `poison` frames 500–570; `monster.gd:84,115,147-148` | ✅ |
| B10 | The chain is on screen for a fifth of a second | `storm` beam pixels in frames 173–178 only | ✅ |
| B11 | Loses focus → pauses; stays paused until Enter | `focus` frames 191–192 (state 2), 266 (still 2), 272 (state 1) | ✅ |
| B12 | R restarts: wave 0, 50 gold | `lose` frame 785 | ✅ |
| B13 | Best wave three survived a relaunch; F2 skips twice; debug tools enabled | `relaunch` frame 61 (best 3); frames 214, 280; `CAPTURE.md` | ✅ disclosed |
| B14 | Error panel covered by the menu card; Enter starts a session that can't move | `broken` frames 121–385: state 1, wave 1, HUD frozen | ✅ staged |
| B15 | 33 features via real input; every scripted opening overrun by wave 5 | `coverage.json`; dry runs plus `opening` take (O-1) | ✅ scripted, not a playtest |
| B16 | Keyboard died with every test green | `PORTING_NOTES.md` §4.4; fix `51e4eec` | ✅ |

## Contradictions with documents (reported, not fixed)

- **GDD M-08, edge case 3** ("the session never enters PLAYING") is contradicted by the `broken` take.
- **`AUDIO-PLAN.md`** says a leak "currently has a red screen vignette". The vignette exists only on `feature/recovered-art`.

## Deliberately not claimed

- that the game is finished, balanced, playtested or fun;
- that it looks like the original;
- a commit count;
- frame-rate performance (Movie Maker and fixed-fps captures are offline).
