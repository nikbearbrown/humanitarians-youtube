# FACTCHECK — Night Yard: Inside the Godot Code

Code panels are verbatim excerpts of the game's source at build 54ad5ab, read by line at build time (`gamedev-evidence.json`). Each is followed by an exact-frame window of a scripted-input take in `../inside-captures`.

| Beats | Code | Result | Observation |
|---|---|---|---|
| B03–B04 | `scenes/level_01.tscn:1-7` | take `campaign` 700–900 | Level 1 loads fully built: yard backdrop, blocks and containers, lights, HUD, banner. |
| B05–B06 | `scripts/levels.gd:41-50` | take `campaign` 920–1250 | The block, lights, ledge and first bot sit where the level 1 map puts them. |
| B07–B08 | `scripts/fighter.gd:254-262` | take `campaign` 785–960 | D held; Shift toggles walk and run; Space jumps onto the block. |
| B09–B10 | `scripts/fighter.gd:372-402` | take `extras` 790–1020 | Jab, cross, uppercut, block and hammer from the key showcase. |
| B11–B12 | `scripts/fighter.gd:744-757` | take `campaign` 2440–2620 | Jab, cross and kick chain on the bots at the foot of the level 2 shaft. |
| B13–B14 | `scripts/fighter.gd:547-571` | take `campaign` 1120–1210 | The ledge on the level 1 block is grabbed and climbed. |
| B15–B16 | `scripts/fighter.gd:660-685` | take `campaign` 2690–2810 | Wall slide, wall jump and the grab at the top of the level 2 shaft. |
| B17–B18 | `scripts/fighter.gd:1068-1074` | take `campaign` 3960–4060 | The axe is picked up and thrown into a bot. |
| B19–B20 | `scripts/ai.gd:149-161` | take `campaign` 7230–7330 | The level 4 guard bot stays unaware as the player walks up behind it. |
| B21–B22 | `scripts/fighter.gd:1076-1087` | take `campaign` 7300–7420 | The takedown plays on the unaware bot. |
| B23–B24 | `scripts/spike_trap.gd:60-84` | take `defeat` 1560–1760 | The plate arms, fires and kills; the player respawns at the checkpoint. |
| B25–B26 | `scripts/level.gd:845-866` | take `defeat` 560–760 | A fall into the pit is a K.O.; the player respawns at the start. |
| B27–B28 | `scripts/options_panel.gd:52-55` | take `defeat` 1965–2265 | After Options in the pause menu, Esc shows the pause panel without pausing the tree. |
| B29–B30 | `scripts/character_select.gd:170-178` | take `extras` 283–560 | Green is chosen with the arrows; Enter presses Back and the choice is not saved. |

| Other | Claim | Evidence |
|---|---|---|
| B02 | level_01.tscn is 1 node; 385 live nodes at 8 s | `evidence/tree_probe.txt` (headless, no input, isolated copy) |
| B31 | 10 scenes, 17 scripts, 5,215 lines; 2 BoneMaps; audio synthesized | file listing; `wc -l scripts/*.gd`; README |
| B32 | R-01 `options_panel.gd:53`; R-02 arrow keys move the focus | defeat event `defect_options_eats_pause`; extras frame 505 (Green chosen, Yellow kept) |

**Visual exemption.** Gameplay beats show the game's own UI text. GATE T pixel checks on those beats are exempt; the overlays were verified by eye.
