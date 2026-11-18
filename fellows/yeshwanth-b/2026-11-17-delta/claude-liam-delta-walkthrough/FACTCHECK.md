# FACTCHECK — Delta, Every Feature, Played

Every gameplay beat is an exact-frame window of a scripted-input take. `coverage.json` ties each shown feature to a frame inside its beat's window.

| Beats | Claim | Evidence |
|---|---|---|
| B00 | 12 levels, 2 layers, 27 scripts and 3 shaders; 4 takes, 90 of 90 assertions | `scripts/` listing; `../delta-captures/CAPTURE.md`; `capture/*-inputs.jsonl` |
| B02–B04 | Menu, How to play, New game; VEGA subtitles (no voice files in the Unity export); F picks up; E places the cell; door; exit lift | take `campaign1` 0–1012; `levels.gd` level 1 lines |
| B05 | Q shifts 50 m to Lower Delta (warm tint) and back | take `campaign1` frames 1250, 1686; `level.gd` DIM_Y, DIM_TINT |
| B06 | Charger 750 / s to 3000 | `charger.gd` rate; `pickable.gd` capacity 3000; frames 2757–2900 |
| B07–B09 | Crate and cell on pressure plates; one indicator lamp per port | take `campaign1` 3789–6623; `door.gd` |
| B10–B13 | Arc gate throws a charged cell back (frame 7115); discharger 1500 / s; a flat cell passes; charger; socket | `gate.gd:72-87`; `charger.gd`; take `campaign1` |
| B14–B15 | Outdoor deck, catch field line; socket extends the bridge; shuttle never stops; the player creeps ahead of a moving deck | `levels.gd` level 6 lines; `platform.gd`; GDD R-03 |
| B16–B18 | Continue at 07; held cell shifts along; socket in Lower Delta powers the upper door; plasma only in Upper Delta | take `campaign2` 0–1565; `levels.gd` level 7 |
| B19–B20 | Duplicator copy (button, frame 2022); only one copy kept | `duplicator.gd:72-87`; take `campaign2` |
| B21–B22 | Console scan, hologram, teleport | `teleporter.gd`; take `campaign2` 3940–5185 |
| B23–B24 | Charger in Lower Delta, gate above, shuttle | take `campaign2` 5450–6900 |
| B25–B26 | Shifting with the core damages, ejects, explodes; it rebuilds at its spawn | `player.gd:351-375`; take `campaign2` frame 7198 |
| B27–B33 | Guardians every 20 s in the player's layer; strike follow 5 s, lock 3 s, 3 m; shockwave jumped; two generators open the vault; strike destroys the shield generator (frame ≈ 13560); final stage 200 m up; stabiliser at 15437; ending; credits | `final.gd`; take `campaign2` |
| B34–B39 | Refused shift with toast; plasma death and restart; pause click defect (frame 2123, `under_mouse: CenterContainer`); R while paused does nothing (2411); Restart and Skip via the menu; cell falls back; player falls back | take `defeat`; `hud.gd:313-318`; `level.gd:804-818` |
| B40–B42 | Options contents; Esc leaves credits; Select level best times; mouse look; Shift; Space; pad Y and X; left stick | take `extras` |

**Not shown, listed in `coverage.json`:** right mouse / left mouse actions, pad A / RB / LT / Start, changing options, F11, Exit, strike death, the focus-loss pause, game audio.

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
