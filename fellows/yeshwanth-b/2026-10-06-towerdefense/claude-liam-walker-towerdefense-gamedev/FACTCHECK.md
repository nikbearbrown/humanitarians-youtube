# FACTCHECK — Walker Tower Defense: Inside the Godot Code

**Build:** `caf082c`. Every code panel is verbatim, checked by `./art godot-gamedev --check` against hashed files.

| Beat | Claim | Evidence | Status |
|---|---|---|---|
| B00, B01 | One six-line scene; about 3,000 lines of GDScript; no image files | `main.tscn` (6 lines); 2,975 lines; no image files in `godot/` (inventory) | ✅ |
| B02 | Saved scene has one node; live nodes are unnamed | `main.tscn`; `tree_probe.txt` (live: `@Node2D@2`, …) | ✅. Note: `GAME-BRIEF.md` §6 labels them "Grid", "Hud" — descriptions, not node names |
| B03, B04 | Everything is built in code at start; START begins a run | `session.gd:80-109`; `opening` frames 0–290 | ✅ |
| B05 | Actions are registered at startup; the function once vanished; 56 checks stayed green | `session.gd:451-470`; `PORTING_NOTES.md` §4.4; pre-`51e4eec` receipts | ✅ |
| B06 | Real key events drive build mode and refusals | `opening` frames 389–619 (keys 2, 2, 4, Esc and a right-click) | ✅ |
| B07, B08 | Placement assumes the tower, then runs A* from the spawn and every monster | `grid.gd:152-162`; `maze` frames 482 (refused) and 602 (reroute) | ✅ |
| B09, B10 | 44 px/s before; 3× clock; 1×/2×/3× toggle | `session.gd:21-30`; `opening` frames 951, 999, 1032 | ✅ |
| B11, B12 | One number subtracted; `hit_flash` set first; health from the compounding ramp; kills pay 4 | `monster.gd:112-120`; `wave_spawner.gd:61-63`; `opening` gold 0 → 8 by frame 1968 | ✅ |
| B13, B14 | A tick every 0.1 s calls `take_damage`, which resets `hit_flash`; the poisoned monster reads pale | `monster.gd:74-84, 115, 147-148`; `poison` frames 500–570 | ✅ |
| B15, B16 | Nearest within reach; coin flip; 0.4 s / 0.2 s lifetimes on the 3× clock; chain visible for 6 frames | `projectile.gd:16-18, 129-139`; `storm` beam pixels in frames 173–178 | ✅ |
| B17, B18 | Overlay at x 8–338 in the session's `_draw`; Grid child at x 96 draws after its parent | `session.gd:92, 599`; `grid.gd:9`; `poison` frame 205 onward | ✅ |
| B19, B20 | One routine draws the tower, the bar miniature and the ghost; the chevron is shape plus colour | `tower.gd:116-142`; `hud.gd:113-115`; `session.gd:651`; `opening` frames 1600–1720 | ✅ |
| B21, B22 | The keyboard suite uses `Input.parse_input_event`; revert → 8 of 9 fail; current → 9 of 9 pass | `test_keyboard.gd:33-41`; `evidence/keyboard-1790012997.43825.json`, `keyboard-1790606725.01996.json` | ✅ |
| B23, B24 | Comment promises the session stays out of PLAYING; Enter sets PLAYING; HUD frozen | `session.gd:91-96`; `broken` take (staged copy), frames 213 and 385 | ✅ The comment, and GDD M-08, are contradicted |
| B25 | The defects are draw order and layering | O-2, O-3 and the staged error panel (see `CAPTURE.md`) | ✅ |

**Corrections made during the build:**
- The `_setup_input` and storm excerpts were trimmed to fit the code panel. The pilot showed clipping.
- The cues were re-pointed at the exact lines.
