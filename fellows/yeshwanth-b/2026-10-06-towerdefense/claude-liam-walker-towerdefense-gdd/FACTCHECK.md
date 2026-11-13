# FACTCHECK — Walker Tower Defense: The Design Document Came Last

**Document:** `Walker-Godot-TowerDefense/GDD.md`, v0.1 (agent-drafted, unapproved).

- **Committed in:** `64f6442`.
- **Hash:** sha256 `08a36c02…7af12`. The hash is unchanged at `caf082c`.

**Game build:** `caf082c`, snapshot `f5035b75…3bdd`, Godot 4.7.2.stable.official.ed1daf0bf.

Each spoken claim below was checked against the GDD, the code at `caf082c`, a test receipt, or the film's own capture.

## Spoken claims

| Beat | Claim | Verified against | Status |
|---|---|---|---|
| B00 | The prompt is a reconstruction; the game happened the other way round | GDD Vision; `GAME-BRIEF.md` §16.1. The repository has no GDD-first prompt | ✅ |
| B01 | Rebuilt from 27 surviving scripts | `ls unity-scripts/scripts/*.cs \| wc -l` → 27, re-run 2026-10-05 | ✅ |
| B01 | Every human sign-off is pending | GDD §1 (gates PENDING); `PLAYTEST-LOG.md` is blank | ✅ |
| B02 | 65 automated checks pass | receipts dated 2026-09-28T14:45: data 18, keyboard 9, mechanics 30, match 8 | ✅ |
| B02 | 0 of 22 playtest items done | `PLAYTEST-LOG.md`: 22 rows, all result cells empty | ✅ |
| B03 | Nobody wrote down what the game is for | GDD §2 | ✅ |
| B03 | The menu line was written by the agent | `hud.gd:75-76`. Authorship per `GAME-BRIEF.md` §8: the AI wrote `hud.gd` | ✅ |
| B03 | No pillars; three observed properties | GDD §3, OP-1 to OP-3 | ✅ |
| B04 | Wave one is two monsters, a beat apart | `wave_tuning.gd:19,22` (N+1, 0.8 s); `opening` take, frame 667 onward | ✅ |
| B04 | Each kill pays four gold | `monster_tuning.gd:30`; `opening` gold 5 → 13 across wave 1 | ✅ |
| B04 | No win state, by decision | GDD §4; D-04 | ✅ |
| B05 | All eight goals are proposed | GDD §5 | ✅ |
| B05 | A scripted Fire + Ice opening lost all five lives by wave three | `opening` take: game over at frame 1366, wave 3 (`capture/opening-inputs.jsonl`) | ✅ scripted input, not a playtest |
| B06 | No elemental damage system; one function subtracts one number | `monster.gd:112-120`; check `no-elemental-matrix` PASS | ✅ |
| B06 | The four colours are cosmetic | `monster_tuning.gd:1-16`; check `monster-variants-are-cosmetic` | ✅ |
| B06 | `hit_flash` is the one later line, and it is presentation | `b67653a` added it; `GAME-BRIEF.md` §7.2, as corrected in `caf082c` | ✅ |
| B07 | Wave one was two Green-variant monsters; poison's tint showed nothing | `poison` take, frames 215–300 (contact sheet inspected) | ✅ observed |
| B07 | A poisoned monster turns pale, not green | `poison` take, frames 500–570. Cause: each tick calls `take_damage` (`monster.gd:84`), which sets `hit_flash = 0.14` (`:115`); ticks come every 0.1 s, so the white lerp (`:147-148`) never decays | ✅ observed + code |
| B08 | The chain is on screen for about a fifth of a second | `storm` take: beam pixels present in frames 173–178 only (6 frames = 0.2 s), measured | ✅ |
| B08 | Checklist item eleven | `PLAYTEST-LOG.md` row 11 | ✅ |
| B09 | The Unity original teleported stranded monsters to the exit | `Monster.cs:190-201`, read 2026-10-05 | ✅ |
| B09 | The port checks the entrance and every live monster | `grid.gd:152-165` | ✅ |
| B10 | The reason is on screen for three-tenths of a second | `session.gd:42` `REFUSAL_FLASH := 0.3`. It decrements on real time (`session.gd:171-172`); faint by frame 490 of `maze` | ✅ |
| B10 | A tower on the road is allowed and the route bends | `maze` take: route changed at frame 610 (log `route.changed = true`) | ✅ |
| B11 | The ramp sat inside the per-monster loop and compounds | `wave_tuning.gd:6-9`; check `compounding-hp-curve` | ✅ |
| B11 | The only difficulty curve; kept, reset on restart | GDD M-04; O-03 / D-05 | ✅ |
| B12 | 50 gold, 5 lives, 4 per kill came from the source | `test_data.gd` checks `wave-economy-recovered` and `monster-recovered` | ✅ |
| B12 | Prices were authored, then approved | `tower_tuning.gd:8-10`; O-02 | ✅ |
| B12 | Only the best wave carries over | `session.gd:620-636`; D-08 | ✅ |
| B13 | 56 checks passed while the game was unplayable twice | Pre-`51e4eec` receipts show data 18 + mechanics 30 + match 8 = 56. Both bugs were HUMAN-OBSERVED (`PORTING_NOTES.md` §4.4) | ✅ |
| B13 | Faithful to a board of one unit per tile, not 64 px | `session.gd:21-29` | ✅ |
| B14 | The original level file held numbered levels | `LevelManager.cs:91-131` (reads by `levelNumber`) | ✅ |
| B15 | One scene file, a stub | `godot/game/main.tscn`, 6 lines | ✅ |
| B15 | Seven systems, all stepped from one session loop | GDD §7 (7 rows); `session.gd:168-201` steps monsters, towers and projectiles from one `_process` (D-09). An earlier draft said "a folder each"; that was cut because the systems span 6 feature folders plus `game/` and `ui/` | ✅ |
| B15 | No audio; the extract had none | `AUDIO-PLAN.md`; `find … -iname '*.wav'` → 0 | ✅ |
| B16 | Five stale claims, since corrected by the owner | GDD Appendix C listed them. The owner corrected them in `64f6442` and `caf082c` (2026-10-05) | ✅ |
| B17 | The AI traced every rule to a file | GDD citations | ✅ |

## Corrections found while making this film (not in the GDD)

- **The B07 narration was rewritten after looking at frames.** The first draft said the Poison tower "tints it green". The footage showed that was not what happens (see B07 above).
- **The level-load error surface: the GDD is wrong.** M-08 edge case 3 says "the session never enters PLAYING". In the staged `broken` take, Enter sets state PLAYING and Space starts wave 1, while the HUD stays frozen on the menu card. **This GDD sentence is false.** It is reported to the owner and not edited here. The claim came from the code comment at `session.gd:94-95`.
- **`AUDIO-PLAN.md` describes the art branch.** It says a leak "currently has a red screen vignette". On `main` there is no vignette; it exists only on `feature/recovered-art` (`session.gd:522` there).
- **The F1 debug overlay is covered by the board** (`session.gd:599` versus the Grid child at `:92`). This is not in the GDD; it is documented in `CAPTURE.md` O-2.

## Not claimed

These are deliberately absent from the narration:

- that the game is finished, balanced or playtested;
- that it looks like the original;
- that the AI built it from scratch;
- a commit count (it drifts; the owner asked for "around twenty");
- any wall-clock build time.
