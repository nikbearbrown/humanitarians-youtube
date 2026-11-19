# FACTCHECK — Delta: Inside the Godot Code

Every code panel is read verbatim from the game's files by line number at build time (`gamedev-evidence.json` `excerpts`). Every result beat is an exact-frame window of a scripted-input take of the same build (`25e03b2`).

| Pair | Claim | Evidence |
|---|---|---|
| B02 | Saved level scene is 1 node; live at 8 s, 604 nodes | `evidence/tree_probe.txt` (headless probe of `res://scenes/level_01.tscn`, no input) |
| B03–B04 | `level_01.tscn` is 7 lines with `level_id = 1`; all 12 level scenes are 7 lines | `scenes/level_*.tscn`; take `campaign1` 304– |
| B05–B06 | Level 1 map and legend: c cell on a desk, S socket powers d1, D door | `levels.gd:29-47`; take `campaign1` 520– |
| B07–B08 | Mouse look only while captured; actions | `player.gd:118-131`; take `extras` 568– |
| B09–B10 | F drops or picks via the ray; items in a device come out with E | `player.gd:282-298`; take `campaign1` 575– |
| B11–B12 | Shift refused without floor or with overlap | `level.gd:673-694`; take `defeat` 380– (toast "Something solid is in the way on the other side") |
| B13–B14 | Shift with the core: damage, eject, critical | `player.gd:351-375`; take `campaign2` 7180– |
| B15–B16 | Charger 750 / s; busy while working | `charger.gd:63-80`; take `campaign1` 2740– |
| B17–B18 | Gate rejects a charged cell or the core and throws it back | `gate.gd:72-87`; take `campaign1` 7060– (rejection at 7115) |
| B19–B20 | Duplicator: no empty, no copy of a copy, previous copy removed | `duplicator.gd:72-87`; take `campaign2` 2010– |
| B21–B22 | Strike: follow 5 s, lock with a ring, strike 3 s later | `final.gd:481-509`; take `campaign2` 9180– |
| B23–B24 | Strike within 3 m destroys the shield generator or kills the player | `final.gd:524-532`; take `campaign2` 13440– |
| B25–B26 | Options `CenterContainer` added last over the pause panel | `hud.gd:313-318`; take `defeat` 2063– (`under_mouse: CenterContainer`) |
| B27–B28 | Pause keys handled by a node that pauses | `level.gd:804-818`; take `defeat` 2395– |

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
