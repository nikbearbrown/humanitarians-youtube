# RIFF — gameplay beats in the GDD film

Observations come from inspecting the actual frames (contact sheets in `_qc/`). Interpretation is separated from the code facts. Every run is scripted input, not a playtest.

| Beat | Artifact and window | Visible observation | Interpretation and source | Narration (summary) | Next experiment |
|---|---|---|---|---|---|
| B04 | `opening` frames 330–928 | Fire placed at (10,1), Ice at (6,1), gold 50→5. Space at frame 667; two monsters walk the tinted top row. Fire's burst lands; gold reaches 13 by wave end. | The core loop: build → release → defend → earn (GDD §4) | "Here's the core loop, played by a script…" | A tester narrates what they think each tower does before reading the bar |
| B07 | `poison` frames 196–828 | Wave 1 is two Green-variant monsters: no visible tint change. Esc at frame 327 shows "Paused."; Enter at 383 resumes. In wave 2 the poisoned lead monster stays pale white (frames 500–570). | Each poison tick is a hit (`monster.gd:84`), and each hit resets `hit_flash` (`:115`). Green tint plus a white wash reads as pale. | "…it turns pale, not green… Checklist item ten. Still open." | Ask testers to point at poisoned monsters; count right versus wrong |
| B08 | `storm` real frames 129–204, then a 1/8-speed replay of 173–178, then real frames 204–424, then a 140-frame HELD FRAME | The beam leaves the tower, hits one monster and hops to its neighbour; visible for 6 frames | Beam lifetimes run on the 3× simulation clock (`projectile.gd:16-18`, `session.gd:29`) | "…about a fifth of a second… chain, or a flicker?" | Show the chain to five people at real speed; ask what they saw |
| B10 | `maze` frames 330–884 | Fire at (0,1) accepted. Fire at (1,0) refused, "Would block the path"; the label is faint within about 8 frames. A tower on the road at (5,0) is accepted; the tint bends; wave 2 follows. The (0,1) tower is sold, +10 gold. | No-seal rule D-06 (`grid.gd:152-165`); `REFUSAL_FLASH := 0.3` (`session.gd:42`) | "It's a maze, not a gun line." | Time how long a tester needs to read the refusal reason |

**Failed or awkward renders kept in the record:** B08 ends on a 4.7 s labelled HELD FRAME, because the `storm` take ran out before the narration did.
