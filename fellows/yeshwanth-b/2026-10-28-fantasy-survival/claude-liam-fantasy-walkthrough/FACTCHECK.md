# FACTCHECK — Fantasy Survival Crafting: Every Feature, Played

Every gameplay beat is an exact-frame window of a scripted-input take. `coverage.json` ties each of the 43 shown features to a frame inside its beat's window.

| Beats | Claim | Evidence |
|---|---|---|
| B00 | 23 scripts, 260 m valley; 3 takes, 74 of 74 assertions | `wc -l`; GDD §7; `CAPTURE.md` |
| B02–B04 | Menu with no Load Game; How to Play; 3 intro pages; empty inventory; "Craft an axe first"; apple from a tree | take `day` 0–1143, assertions |
| B05–B06 | 3 sticks, mushroom, 3 gold by the ore rocks, 3 stones; Craft Axe; key 1 equips | take `day` 1143–2484 |
| B07 | Two pines felled in 4 swings each; 4 logs; objectives read (0/3) after crafting | take `day` 2484–3264; zoomed frame check |
| B08–B09 | Campfire crafted; rabbit hunted; lake drink to 100; fire in the water refused; fire placed inland | take `day` 3264–4205 |
| B10–B11 | Cooked meat; hover info; drag to slot 21; eat 3 foods; Settings; Save | take `day` 4205–5170 |
| B12–B14 | Load Game at 13:09; nearly 6 hours skipped between windows (cut between beats); night falls; warm; night save; rest 9×; Dawn Breaks (day 2, 16 items, 2 trees, 1 rabbit); Load Game on the menu | take `night` |
| B15–B17 | Pad right stick and Y; freezing; N debug damage ×8; Lost to the Wilds; Load Save | take `defeat` |

**Not shown, listed in `coverage.json`:** F11, Quit, Play Again, slider changes, Red Cap / Bread / Water Flask, sprint-jump as a separate demonstration, game audio.
