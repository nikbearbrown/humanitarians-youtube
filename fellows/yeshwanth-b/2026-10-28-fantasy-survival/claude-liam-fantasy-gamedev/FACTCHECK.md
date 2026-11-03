# FACTCHECK — Fantasy Survival Crafting: Inside the Godot Code

Code panels show verbatim lines of the game at build `a514438`; the checker verifies each against the file. Each code beat is followed by real engine output of the same build.

| Beat | Claim | Evidence |
|---|---|---|
| B02 | game.tscn: 1 node; live at 2 s: 1,976 nodes (266 props, 82 pickups, 36 pines, 9 rabbits, 47 grass chunks) | `evidence/tree_probe.txt` |
| B03 | game.tscn is 6 lines | the file |
| B05 | Materials rebuilt; Z-up packs rotated −90° | `model_library.gd:89-100` |
| B07 | Relative look, gated by open windows; pitch ±89° | `player.gd:105-114` |
| B09 | 4 m centre ray re-cast every physics frame; target needs `get_prompt` | `player.gd:161-172` |
| B11 | Requirement colour; Craft button visible only when affordable; fire distance check | `crafting_ui.gd:81-94` |
| B13, B14 | Ticked objectives read (0/3): the counter reads the inventory, the flag remembers the craft | `world.gd:759-773`; zoomed frames of take `day` 2420–2509 |
| B15 | 4 hits; fall away from the player | `choppable_tree.gd:37-47` |
| B17 | Flee within 5 m at 5.5 m/s | `rabbit.gd:51-62` |
| B19 | Spot 2.6 m ahead; refused below water + 0.2 m | `world.gd:723-731` |
| B21 | Drop moves or swaps; right-click uses | `inventory_slot.gd:54-63` |
| B23 | 24 / 12 s per hour, rest 9×, victory conditions | `world.gd:587-605` |
| B25 | Starve 1/s; cold 1 per 1.4 s; causes recorded | `player_state.gd:62-72` |
| B27 | Save dictionary fields | `world.gd:807-829` |
| B29 | 6 scenes; 23 scripts + 3 shaders; 185 assets; 2 playtests (42 checks) that call functions directly | file listing; `_tools/` |
