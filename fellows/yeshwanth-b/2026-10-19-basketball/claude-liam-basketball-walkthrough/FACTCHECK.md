# FACTCHECK — Basketball Blaster: Every Feature, Played

Every gameplay beat is an exact-frame window of a scripted-input take. `coverage.json` ties each of the 42 shown features to a frame inside its beat's window.

| Beat | Claim | Evidence |
|---|---|---|
| B00 | 3 arenas, 8 scenes, 2,408 lines; 3 takes, 76 of 76 assertions | `wc -l`; `CAPTURE.md` (46 + 13 + 17) |
| B02 | How to Play lists every key, the controller and 7 rules | `instructions.gd`; take `campaign` 177–354 |
| B03 | Two clicks don't advance the briefing; Enter does and completes a line | assertions at frames 549, 594, 618, 622 |
| B04 | Walk, jump, double jump, jetpack, fire every 0.4 s, grenade; health 3 → 1 | `campaign` 1156–1694; log |
| B05 | Life lost, respawn, grenade kills 4 (MEGA KILL!), 10 kills with eggs still 1 / 5 | `campaign` 1694–2471; log frames 1728, 1795, 2471 |
| B06 | One life left; jetpack; 5 eggs; COURT CLEARED | `campaign` 2471–2999; log 2482, 2645–2866 |
| B07 | Pause, Resume, Main Menu, Continue: Arena 2 | `campaign` 2999–3398; assertions |
| B08 | Arena 2: 3 pipes, 6 eggs, cleared with 2 lives, 2 kills | log 3398–3859 |
| B09 | Arena 3: 4 pipes, 7 eggs, 4-hit chickens; cleared on the last life, 1 kill | log 3977–4622; `game.gd:147-160` |
| B10 | Victory 013 kills, 18 eggs; no Continue afterwards | frame 4780; assertion at 4965 |
| B11 | Esc skips the briefing; synthetic pad: stick, aim, RT, A, Start | `defeat` 0–379; assertions |
| B12 | R restarts; three lives lost walking into the flock | `defeat` 379–916 |
| B13 | Defeat text; Retry restores 3 lives | `defeat` 916–1216 |
| B14, B15 | Esc on How to Play, drop-through, F, G, LB, RB, Restart Arena, Quit (exit 0) | take `extras`; assertions; `godot.rc` |
| B16 | Two defects; eggs beat fighting; F11 and Play Again not shown | above; `coverage.json` `not_exercised` |

**Not shown, honestly listed:** F11 / Alt+Enter fullscreen, Play Again, Exit Game on the defeat screen, game audio. **Not judged:** fun, fairness, difficulty as felt.
