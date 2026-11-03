# FACTCHECK — Fantasy Survival Crafting: The Design Document Came Last

Board excerpts are read from `fantasy-survival-crafting-godot/submission/GDD.md` by line number at build time. Other claims:

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00, B01 | The Walker prompt is reconstructed; the game was rebuilt before its GDD; the Unity source had no scenes, no audio and no win state | GDD status line; README "Added to complete the game" | as stated |
| B02 | 23 GDScript files + 3 shaders, 3,303 lines; 42 game checks; 74 film assertions (45 + 15 + 14); 0 playtests | `wc -l`; `playtest.log`, `playtest_load.log` (re-run); `CAPTURE.md` | measured |
| B04, B07 | Stick pickup, axe craft, four-swing fell, campfire: cuts from take `day`, in order | take `day` frames 1430–4220 | observed |
| B05 | Fire placed at 12:25; calories 100 → 35 (lowest, 12:47); 3 meals → 100 | take `day` log (frames 4205, 4463, 4541–4720) | measured, scripted |
| B06 | Unity 12 m/s, jumpHeight 3; Godot 5.5 / 8.5 m/s, 1.2 m | `PlayerMovement.cs` via the GDD; `player.gd` constants | source |
| B08, B09 | Swing and chop sounds declared in Unity, never played; 4 hits; rabbit flees within 5 m; rabbit in motion | GDD M-06; `choppable_tree.gd`, `rabbit.gd`; take `day` 3400–3580 | observed |
| B10, B12 | 24 s per hour by day, 12 at night, rest 9×, warmth 9 m; dawn summary: day 2, 16 items, 2 trees, 1 rabbit | `world.gd` constants; take `night` 4920–5890 | observed |
| B11 | Fire refused in the water: the spot is 2.6 m ahead | `world.gd:723-731`; take `day` 3872 | observed |
| B13 | Drain and damage rates | `player_state.gd` | source |
| B14 | Cook, hover, drag, eat; calories 35 → 100 | take `day` 4205–4740 | observed |
| B15 | Full-slot drop swaps (Unity: no change); one JSON save slot | GDD M-03, M-09; `inventory_ui.gd:112`; `game_state.gd` | source |
| B16 | Freezing away from the fire; N = 10 damage (Unity debug key); defeat; Load Save | take `defeat` 224–1360 | observed |
| B18 | game.tscn is 6 lines; 1,976 live nodes at 2 s | `scenes/game.tscn`; `tree_probe.txt` | measured |
| B19 | Ticked objectives read "(0/3)" after crafting (not in the GDD); rabbit now seen in motion (GDD R-04) | takes `day` and `night`; `world.gd:759-773` | observed |

**Not claimed:** fun, tension, balance, fairness. No person has played the build.
