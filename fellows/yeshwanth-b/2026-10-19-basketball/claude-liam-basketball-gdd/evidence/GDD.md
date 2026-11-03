# GDD — Basketball Blaster: Fowl Play

**Document status: DRAFT v0.1 — agent-drafted, unapproved.**

- It was written on 2026-10-15, after the game was built.
- It is built only from evidence in this folder: the Godot project, its README, and the recovered Unity scripts.
- It also uses the scripted-input captures made for the films.
- It records what the game already is. Where the folder is silent, it says so instead of inventing an answer.
- No human has signed off any section.

## Status vocabulary

Every claim carries one of these labels.

| Label | Meaning | Evidence |
|---|---|---|
| **SOURCE** | Present in the recovered Unity C# | A file in `basketball-game-godot/unity-scripts/scripts/` |
| **README** | Stated by the project's own README | `basketball-game-godot-completed/README.md` |
| **AUTHORED** | New in the Godot port: not in the Unity scripts | Godot code, with no Unity counterpart |
| **IMPLEMENTED** | Present in the Godot code | A file and line under `scripts/` |
| **OBSERVED** | Seen in a scripted-input capture of the real build | A take name and frame in `CAPTURE.md` |
| **PROPOSED** | Written by the agent in this document | This document only |
| **PENDING** | Needs a human judgment that has not been made | Section 16 |

A mechanic can be IMPLEMENTED and OBSERVED while its player-experience claim stays PENDING. That is the state of the whole game: it runs end to end, and no person has playtested it.

## 1. Metadata

| Field | Value | Evidence |
|---|---|---|
| Name | Basketball Blaster: Fowl Play | `project.godot` `config/name` |
| What it is | A Godot 4 port of a Unity 2D arena shooter, extended to three arenas | README |
| Engine | Godot 4.7.2.stable.official.ed1daf0bf, GL Compatibility renderer | `Godot --version`; `project.godot` |
| Canvas | 1280×720, `canvas_items` stretch; starts fullscreen | `project.godot` `[display]` |
| Code | 14 GDScript files + 1 shader, 2,408 lines | `wc -l scripts/*` |
| Scenes | 8 thin `.tscn` files; every node is built in code | `scenes/` |
| Unity source read | 29 C# game scripts, 2,012 lines (the imported Cartoon FX scripts are separate) | `unity-scripts/scripts/` |
| Exports | macOS universal app (ad-hoc signed; boots headless, exit 0). Windows x86-64 `.exe` present, **never run** | `builds/`; run 2026-10-15 |
| Build under film | Snapshot `build_id 8f86cc8…` (188 files, `builds/` and `.godot/` excluded) | `CAPTURE.md` |

## 2. Vision

**README:** "A Godot 4.7.2 port of the Unity project … The gameplay and scene flow are rewritten in GDScript."

**PROPOSED vision statement:** *A short, loud arena shooter. You are Mr. Block with a basketball gun. Grab every egg while chickens pour out of pipes.*

The README describes a port and its additions. No document says who the game is for or why someone should play it. The vision is therefore PENDING (OQ-01).

## 3. Pillars

No pillars were ever written. These three are PROPOSED, read off what the code makes true:

1. **Objective over body count.** A level ends when the last egg is taken, never on kills (`game.gd:559-560`).
2. **Always moving.** Double jump, jetpack, one-way platforms and a drop-through make the arena vertical (`player.gd`).
3. **Every hit is loud.** Each hit gets screen shake, a hit flash, feathers, a splatter and a sound (`game.gd`, `effects.gd`).

## 4. Core loop

1. Enter an arena at the respawn gate.
2. Chickens drop from pipes every few seconds.
3. Move and jump to the egg nests, shooting chickens on the way.
4. Contact costs one health; three hits cost a life; respawn at the gate.
5. Collect every egg: "COURT CLEARED!" → next arena.
6. Clear all three arenas → victory. Lose three lives → defeat, then retry that arena.

**IMPLEMENTED** in `game.gd` (`_check_eggs`, `_player_hit`, `_lose_life`, `_level_complete`) and `game_state.gd`. **OBSERVED** in takes `campaign` and `defeat`.

## 5. Player-experience goals

All PROPOSED, all PENDING a human playtest:

- **PX-01** A first-time player understands the goal (eggs, not kills) within the first arena.
- **PX-02** Each arena feels harder than the last.
- **PX-03** Fighting the flock is worthwhile, not only something to avoid.
- **PX-04** A defeat feels fair, and the player wants to retry.

**Counter-evidence from the film captures (OBSERVED, scripted, not a playtest):**

- An autopilot that steers to the nearest egg and shoots whatever is near collected every egg in 12.6 s (arena 1), 13.6 s (arena 2) and 18.7 s (arena 3) of game time.
- Holding one spot in arena 1 and fighting for 25.6 s earned 10 kills and one mega kill, cost one life, and collected no eggs.

On this build, rushing the eggs beats fighting. That challenges PX-02 and PX-03.

## 6. Mechanics

### M-01 Movement and jumping

**IMPLEMENTED** in `player.gd`:

| Value | |
|---|---|
| Run speed | 340 px/s; ground acceleration 2,800, air 1,900 |
| Jump velocity | −820; gravity 1,900 |
| Extra gravity | 1,300 more after 0.2 s in the air |
| Coyote time | 0.15 s |
| Jump buffer | 0.12 s |
| Double jump | One mid-air jump, restored on landing |
| Drop-through | `S + Space` on a platform turns platform collisions off for 0.25 s |

**SOURCE:** Unity `PlayerController.cs` has the jump, the extra gravity after 0.2 s, and coyote time (0.5 s in Unity). The port shortens coyote time to 0.15 s: an **AUTHORED** retune with no recorded reason. **OBSERVED** in `campaign`: walk, jump, double jump, landing.

### M-02 Jetpack

**AUTHORED / README:** "Unity shipped the jetpack sprite and a `FrameInput.Jetpack` field but never wired them up."

**SOURCE:** `PlayerInput.cs:44` declares `public bool Jetpack;` and no Unity script reads it.

**IMPLEMENTED:**

- Hold `Shift` to burn up to 1.6 s of fuel.
- Thrust 4,200 px/s², capped at a rise of 430 px/s.
- Fuel refills at 1.8/s on the ground and 0.225/s in the air.

**OBSERVED** in `campaign` (fuel bar drains).

### M-03 Basketball gun

**IMPLEMENTED:**

- Aim with the mouse or the right stick.
- Hold fire: one ball every 0.4 s.
- Each ball travels 900 px/s for up to 2 s, deals 1 damage and knocks back 320.
- Balls pass up through one-way platforms and stop on them only when travelling downward (`bullet.gd:46-48`).

**SOURCE:** `Gun.cs` fires every 0.5 s. The 0.4 s is an **AUTHORED** retune.

### M-04 Basketball grenade

**SOURCE + IMPLEMENTED:**

- Right-click lobs it. It blinks and beeps three times over 3 s, then explodes.
- Radius 230 px, 3 damage.
- It detonates early on touching a chicken.
- Cooldown 0.8 s.

Unity `Grenade.cs` has the same 3 blinks, 3 s fuse and 3 damage. **OBSERVED** in `campaign`.

### M-05 Chickens and pipes

**SOURCE + IMPLEMENTED:**

- Each pipe recolours itself and drops a chicken painted to match, from an 8-colour palette.
- Chickens turn at random every 3 s, hop every 4 s and fly every 6 s, as in Unity `Enemy.cs`.
- Chickens have 3 health (4 in arena 3).
- Spawning stops at a cap: 10 / 14 / 18 chickens alive.

### M-06 Damage, lives and respawn

**IMPLEMENTED:**

- Touching a chicken (within 58 px) costs 1 of 3 health, knocks you back and gives 1 s of invulnerability.
- At 0 health you lose 1 of 3 lives. The screen fades to black and you respawn at the gate with 2 s of invulnerability.
- Chickens within 260 px of the gate are removed so the respawn is fair (`game.gd:521-525`).

**SOURCE:** `GameManager.cs` has 3 lives and the fade-respawn. The Unity `Health.cs` default is 5 starting health, but the prefab value is not in the recovered files. The port uses 3.

**OBSERVED** in `defeat`: three lives lost, then the defeat screen.

### M-07 Eggs and the win condition

**SOURCE:** `GameManager.cs` asks for 5 rewards.

**IMPLEMENTED:**

- The arenas need 5 / 6 / 7 eggs.
- Pickup range is 62 px.
- The HUD reads "Collect N more eggs to win!".

**OBSERVED** in `campaign`: every egg in all three arenas.

### M-08 Mega kill

**SOURCE + IMPLEMENTED:**

- Three or more chickens dying before the next physics frame triggers "MEGA KILL!", the megakill sound and a shake (`game.gd:470-479`).

**OBSERVED** in `campaign`: one mega kill from a grenade in arena 1 (frame 1795).

## 7. Systems

| System | Owner | Notes |
|---|---|---|
| Input map | `game_state.gd:_configure_input` | Keys, mouse and joypad bound in code at boot; `project.godot` has no `[input]` section |
| Campaign state | `GameState` autoload | Kills and eggs carry across arenas; Continue and Retry read it |
| Audio | `Audio` autoload | 13 named sounds; 16 pooled voices; music persists across scenes |
| Level build | `game.gd:_get_level_config` | Data tables: width, pipes, spotlights, platforms, eggs, spawn rate, cap, tint |
| Effects | `effects.gd` (static) | Feathers, splatter, ball hit, dust, explosion, sparkle, floating text |
| Hit flash / tint | `hit_flash.gdshader` | One shader for both the palette tint and the white flash |

## 8. Progression

Three arenas in a fixed order. Each one is wider and has more pipes, faster spawns, a higher chicken cap and more eggs.

| Arena | Width | Pipes | Spawn every | Cap | Chicken HP | Eggs |
|---|---|---|---|---|---|---|
| 1 Street Court | 36 tiles | 2 | 3.0 s | 10 | 3 | 5 |
| 2 Sunset Rooftops | 40 | 3 | 2.6 s | 14 | 3 | 6 |
| 3 Fowl Play Finals | 44 | 4 | 2.2 s | 18 | 4 | 7 |

There is no unlock, save or score persistence between sessions. **AUTHORED** (README): the Unity project had one playground.

## 9. World and levels

**IMPLEMENTED:**

- Each arena is one screen tall: 19 rows of 64 px.
- The ground row is 17. One-way platforms sit at rows 14, 11 and 8 (and 5 in arena 3).
- The respawn gate is at the left.
- The art comes from the Unity bar-street tiles; the backdrop parallaxes behind.
- Arena 2 has a 14 % orange tint and arena 3 a 38 % navy tint.

## 10. Narrative and characters

**AUTHORED:** an eight-line pre-game briefing (`intro_briefing.gd`). COACH explains the controls; MR. BLOCK replies.

There is no other story, and the arenas have no dialogue. Characters: Mr. Block (player), the Coach (briefing portrait), the chickens.

## 11. UI and controls

**IMPLEMENTED:**

- Main menu (Play, Continue when mid-campaign, How to Play, Quit).
- Briefing; How to Play.
- HUD: lives, health balls, kills, eggs, grenade and fuel bars.
- Pause (Resume, Restart Arena, Main Menu).
- Court-cleared card; victory and defeat screens.
- Controls are listed in the README, the How to Play screen and the pause screen.

**Gamepad:** left stick, right stick, A, RT, LB, RB and Start are bound. **OBSERVED** by synthetic joypad events in `defeat`. No physical controller was used.

## 12. Audio and art

- **README:** every sound and the music loop were synthesized for the port; the Unity export had no audio files.
- **Art:** reused from the Unity project and cropped, downscaled and sliced (README "Asset notes"). That includes:
  - Mr. Block, the gun and grenade;
  - the chicken sheets, pipe and nest;
  - the gate, spotlight and tiles;
  - the title, victory and game-over art.
- Rights and authorship of that art are not recorded anywhere in this folder: PENDING (OQ-05).

## 13. Out of scope

Not in this build and not proposed here:

- saves and high scores;
- difficulty settings or volume options;
- accessibility options;
- online play;
- additional weapons.

Fullscreen toggling (`F11` / `Alt+Enter`) exists in the source but was not captured.

## 14. Technical

- 2D physics layers: world 1, player 2, enemies 3, projectiles 4, platforms 5.
- The player collides with world and platforms.
- Chickens are found through the `chickens` group, and contact damage is a distance check, not a physics collision (`game.gd:481-489`).
- Automated tests: **none exist** in the project. The only machine checks are the film's smoke run (all 8 scenes load and run, no script errors) and the capture assertions.

## 15. Risks and known defects

**OBSERVED on build `8f86cc8`:**

- **D-01:** the briefing prompt says "ENTER / CLICK TO CONTINUE", but clicking never advances it.
  - A full-screen shade `ColorRect` (mouse filter STOP) consumes every click (`intro_briefing.gd:65-68`).
  - Enter and Esc work.
- **D-02:** the HUD hint labels "RMB / G" and "SHIFT" overlap the grenade and fuel bars.
  - The bars render taller than their 14 px size.
- **R-01:** rushing eggs is faster and safer than fighting (section 5).
- **R-02:** the Windows export has never been run.

## 16. Open questions

- **OQ-01** What is the game for, and who is it for?
- **OQ-02** Should fighting be rewarded (score, egg drops), or is avoiding the flock the intended play?
- **OQ-03** Are the retunes (fire 0.5 → 0.4 s, coyote 0.5 → 0.15 s, health 3) the intended feel?
- **OQ-04** Fix D-01 and D-02 before anyone plays it?
- **OQ-05** Who owns the reused Unity art and the title images, and may they be published?
- **OQ-06** Is a single sitting with no saves the intended length?

## Appendix A — Acceptance tests

| Test | Result | Kind |
|---|---|---|
| All 8 scenes load and run 150 frames with no script error | PASS | smoke run, 2026-10-15 |
| macOS export boots headless, exit 0 | PASS | `--headless --quit-after 300` |
| Campaign: menu → How to Play → briefing → 3 arenas cleared → victory | PASS (46/46 assertions) | scripted input |
| Defeat: lose 3 lives → defeat → Retry restores 3 lives | PASS (13/13 assertions) | scripted input |
| A person plays and judges PX-01 … PX-04 | **not run** | human playtest |

## Appendix B — Provenance

- **Godot project:** `basketball-game-godot-completed/`, unmodified.
- **Unity scripts:** `basketball-game-godot/unity-scripts/scripts/`.
- **Film captures:** made on an isolated copy where only window size and focus settings changed (`CAPTURE.md`).

## Appendix C — Changes

- **v0.1, 2026-10-15:** first draft, written for the film set.
