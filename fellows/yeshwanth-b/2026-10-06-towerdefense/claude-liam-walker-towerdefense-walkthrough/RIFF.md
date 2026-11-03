# RIFF — Walker Tower Defense: Every Feature, Played

One row per implemented feature in `coverage.json`. Observations come from the frames; interpretation is separated out. Every run is scripted input, not a playtest.

| Feature | Capture · window (s) | Action at | Visible observation | Riff (interpretation) | Beat |
|---|---|---|---|---|---|
| `menu-and-best-readout` | `opening` 0.0–13.667 | 1.0 s | Boot shows the menu card; the top bar reads BEST 0 on a fresh save folder. | The best wave is the only thing the game remembers; a fresh save proves it starts from nothing. | B02 |
| `start-by-click` | `opening` 0.0–13.667 | 2.833 s | Clicking START enters play with 50 gold and 5 lives. | Mouse and keyboard both start a run; the mouse path never touched the InputMap, which is how the dead-keyboard bug hid. | B02 |
| `build-bar-pick` | `opening` 0.0–13.667 | 4.833 s | Clicking the Fire button highlights it and enters build mode. | The bar shows cost and a one-word skill, so the choice is legible before any tooltip. | B02 |
| `build-ghost-and-range` | `opening` 0.0–13.667 | 6.667 s | A ghost tower and its 2.5-tile range circle follow the cursor across the board. | Range is visible before spending, which matters when every tower also reshapes the road. | B02 |
| `refusal-cant-build-here` | `opening` 0.0–13.667 | 8.967 s | Clicking lava flashes the tile red with "Can't build here". | Lava is walkable but not buildable; the tint warns before the click. | B02 |
| `place-tower` | `opening` 0.0–13.667 | 11.967 s | Fire placed at (10,1); gold drops 50 to 30. | The corner covers both legs of the default L-shaped route. | B02 |
| `build-key-pick` | `opening` 0.0–13.667 | 12.967 s | Key 2 enters Ice build mode. | Keys 1 to 4 mirror the bar; they arrived in the Phase B input audit. | B02 |
| `cancel-build-right-click` | `opening` 13.667–30.067 | 15.167 s | Right-click cancels build mode; the ghost disappears. | A cheap undo before money is spent. | B03 |
| `refusal-not-enough-gold` | `opening` 13.667–30.067 | 19.567 s | Storm (35) with 5 gold is refused: "Not enough gold". | Gold is checked first, so even a lava click reports gold when you are broke. | B03 |
| `cancel-build-esc` | `opening` 13.667–30.067 | 20.633 s | Esc leaves build mode and does not pause. | One key, two meanings, ordered: cancel first, pause second. | B03 |
| `wave-release-and-route` | `opening` 13.667–30.067 | 22.233 s | Space releases wave 1; two monsters walk the tinted shortest route from IN to OUT. | The route tint is the whole maze readout; whether it is strong enough is checklist item 1. | B03 |
| `towers-fire-and-kill-reward` | `opening` 13.667–30.067 | 26.0 s | Fire and Ice shoot automatically; by the end of wave 1 gold has gone from 5 to 13. | Kill income is 4 gold flat; checklist item 14 asks whether that keeps a player building. | B03 |
| `speed-toggle` | `opening` 30.067–50.0 | 31.7 s | The SPEED button goes 1x to 2x; F goes to 3x and later back to 1x. | Speed multiplies the clock, not the rules, so outcomes should not change with speed. | B04 |
| `leak-costs-life` | `opening` 30.067–50.0 | 34.4 s | Two wave-2 monsters reach OUT; LIVES drops from 5 to 3. | A leak is the only way to lose; on main it is shown only by the LIVES counter, which turns red at two or fewer. (AUDIO-PLAN.md mentions a red vignette; that exists only on the unmerged art branch.) | B04 |
| `game-over-card` | `opening` 30.067–50.0 | 45.533 s | At 0 lives: "The exit was overrun. Furthest wave: 3  Best: 3". | Endless by decision: losing is the only end state. | B04 |
| `play-again-enter` | `opening` 30.067–50.0 | 48.867 s | Enter on the game-over card starts a fresh run: 50 gold, 5 lives, wave 0. | Retry is one key; the compounding ramp resets with it. | B04 |
| `select-tower-panel` | `opening` 50.0–66.133 | 55.2 s | Clicking a placed tower shows its range and SELL 10 / UPGRADE 30. | Sell and upgrade live in one panel, priced before you commit. | B05 |
| `upgrade-once` | `opening` 50.0–66.133 | 57.0 s | UPGRADE spends 30; a chevron appears; the button reads MAXED; SELL becomes 34. | One tier only; sale value adds round(0.8 x 30). | B05 |
| `right-click-clear-selection` | `opening` 50.0–66.133 | 59.6 s | Right-click with a tower selected clears the selection. | Same gesture as cancel, applied to the other mode. | B05 |
| `start-by-enter` | `maze` 1.0–11.1 | 1.367 s | Enter on the menu starts a run. | The keyboard path that was once dead now works on its own. | B06 |
| `refusal-monster-in-the-way` | `maze` 1.0–11.1 | 3.333 s | Trying to build on a tile a monster occupies is refused: "Monster in the way". | You cannot drop a tower on a monster to trap it. | B06 |
| `refusal-would-block` | `maze` 11.1–32.233 | 16.067 s | With Fire at (0,1), Fire at (1,0) would seal the spawn and is refused: "Would block the path". | The rule the Unity original lacked; the reason is visible for at most 0.3 s. | B07 |
| `reroute-around-tower` | `maze` 11.1–32.233 | 20.067 s | A tower placed on the road at (5,0) is accepted and the tinted route changes; wave 2 follows it. | This is the maze: building changes where they walk, not just what shoots them. | B07 |
| `sell-tower` | `maze` 11.1–32.233 | 29.6 s | Selecting the (0,1) tower and pressing SELL returns 10 gold. | Selling reopens the tile and re-paths everyone. | B07 |
| `debug-overlay-f1` | `poison` 1.667–14.833 | 6.833 s | F1 shows the debug overlay; only its left edge is visible, the rest is covered by the board. | Defect: drawn by the session under its own Grid child. | B08 |
| `pause-and-resume-keys` | `poison` 1.667–14.833 | 10.9 s | Esc mid-wave shows "Paused." and freezes the board; Enter resumes. | The card lists R and Esc; Enter also resumes. | B08 |
| `poison-status` | `poison` 14.833–24.267 | 17.0 s | A poisoned wave-2 monster turns pale white rather than green while the poison ticks. | Each 0.1 s tick is a hit, and each hit resets the white flash; checklist item 10. | B09 |
| `storm-chain` | `storm` 2.0–13.0 | 5.767 s | The Storm beam hits one monster and hops to its neighbour, visible for 6 frames (0.2 s) at 1x. | Shown again as a labelled 1/8-speed replay; checklist item 11. | B10 |
| `pause-on-focus-loss` | `focus` 2.267–11.167 | 6.367 s | When macOS brings Finder forward, the game pauses; it stays paused when focus returns until Enter. | Correct and conservative: regaining focus does not resume play. | B11 |
| `restart-r` | `lose` 17.333–27.633 | 25.967 s | R mid-wave restarts: wave 0, 50 gold, board cleared. | Restart resets the health ramp too (deviation D-05). | B12 |
| `best-persists-relaunch` | `relaunch` 0.0–11.8 | 1.0 s | A new process boots showing BEST 3, written by an earlier run. | The one value saved to disk survives a relaunch. | B13 |
| `wave-skip-f2-debug` | `relaunch` 0.0–11.8 | 6.933 s | With walker/debug/enabled=true, F2 jumps from wave 1 to 2, then to 3. | A playtest tool, off by default; this take enabled it on purpose. | B13 |
| `level-load-error-panel` | `broken` 0.0–12.967 | 2.033 s | With level_01.json missing "exit", an error panel is drawn but the menu card covers most of it; Enter then sets PLAYING and Space starts wave 1 behind a frozen HUD. | Staged in a copy. The failure surface exists, but a player cannot read it. | B14 |

## Planned, not built

- `audio-cues`: AUDIO-PLAN.md specifies eight cues; the source had no audio and none has been added.
- `recovered-art-on-main`: An unmerged branch wires recovered PNGs behind a default-off toggle; main ships no recovered art pending provenance review.

## Next experiments for a human

1. Item 6: time how long a tester takes to read "Would block the path". It is visible for 0.3 s.
2. Item 10: ask testers to point at the poisoned monsters (they read white), including on Green-variant monsters.
3. Item 11: show the Storm chain at 1× and ask what they saw. It is visible for 0.2 s.
4. Item 15: five full matches with the F1 overlay. Note the overlay is mostly hidden behind the board; the per-wave match log is the readable alternative.
