# FACTCHECK — Gino: Knife Throw, Every Feature, Played

Every gameplay beat is an exact-frame window of a scripted-input take. `coverage.json` ties each of the 47 shown features to a frame inside its beat's window.

| Beats | Claim | Evidence |
|---|---|---|
| B00 | 3 levels, 3 enemy types, 14 scripts and a shader; 3 takes, 46 of 46 assertions | `scripts/` listing; `../knife-throw-captures/CAPTURE.md`; `capture/*-inputs.jsonl` |
| B02–B03 | Menu with best score 0; How to Play (keys, controller, rules); Esc back; New Game; level banner; hint crystals closed with Enter | take `campaign` 0–600 |
| B04–B06 | Walker chases and is slashed (hit flash, +25); dagger refill; bat; diamonds 10 / 50; spikes half a heart, pit costs the level (hint text); K knife, 30 damage; plants left alone; W at the door | take `campaign` 600–2000; `knife.gd` DAMAGE 30; `enemy.gd` POINTS 25; hint text in `levels.gd` |
| B07 | LEVEL COMPLETE: 135 points, 3 of 5 enemies; Thorn Hollow, red moon; bat hint | take `campaign` frame 2100 (panel reads 135, 6/10, 3/5, 0:43) |
| B08–B10 | The leap past the waiting walker is the driver's `guarded_descent` rule (frame 2400), the drop off the cliff its "drop" mode (frame 3521); bridge, ledges, knife at a bat, High Road hint; level 2 cleared with health 6 | take `campaign` 2300–3940; `knife-throw-captures/takes.gd` |
| B11 | 470 points, 17 of 22 diamonds; Moonlit Depths, dark tileset, 12 enemies | take `campaign` frame 4000; `levels.gd` level 3 map (4 walkers, 5 bats, 3 plants) |
| B12 | The first level 3 hit (frame 4816, health 6 → 5) is a floor spike: half a heart. The input log's nearest-enemy label says "bat"; the frame shows Gino on the spikes | take `campaign` frames 4808–4816 |
| B13 | Walker bite after the gap jump (frame 5366, health 5 → 3); walkers never walk off ledges | take `campaign`; `walker.gd` `_can_walk` |
| B14 | Level 3's bridge covers columns 91–97; the pit is 92–98, a 16 px hole at x 1568–1584. A headless trial (`trial/c1.log`, earlier driver) fell through it after a knockback | `levels.gd`, `level.gd` `_build_grid`; GDD R-01 |
| B15 | Plant snap (frame 6368, health 3 → 1); level 3 cleared at health 1 | take `campaign` |
| B16–B17 | 805 points, 9 of 12, 1:19; credits; Continue (Level 3); best score 805 | take `campaign` frames 6800, 6861–7686 |
| B18–B21 | Pause menu (Resume, Restart, Sound, Main Menu); single slashes and two-hit chains only (logged combo never above 2); pit death; GINO IS DOWN; Retry; R restart with SCRIPT ERROR at `level.gd:761` | take `defeat`; `capture/defeat-run.log` |
| B22–B23 | Menu Sound button; arrow keys; M; synthetic pad stick, A closes a hint, Start pauses and resumes | take `extras` |
| B24 | Verdict lines | the rows above |

**Not shown, listed in `coverage.json`:** the four-hit combo and magic blast, the jump attack, heart pickups, the X / C and pad slash and throw buttons, F11, Quit, the focus-loss pause, game audio.

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
