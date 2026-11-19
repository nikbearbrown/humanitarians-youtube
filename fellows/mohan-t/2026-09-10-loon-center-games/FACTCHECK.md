# FACTCHECK.md — National Loon Center – Educational Games

Checked on 2026-10-29 against `hai-loon-center` (no git history) and Mohan's notes. No secrets or credentials exist in this project; nothing external was contacted.

| Claim | Evidence | Status |
|---|---|---|
| Four games: Nest Site (Spring), Deep Dive (Summer), Runway (Fall), Chick Taxi (Standalone) | app/page.tsx GAMES | VERIFIED IN CODE |
| Game descriptions (nesting, hunting by sight, quarter mile of open water, youngest visitors) | app/page.tsx descriptions | VERIFIED IN CODE |
| All four live; progress bar '4 of 4 games live' | app/page.tsx live: true ×4; progress label | VERIFIED IN CODE |
| Tiles with season, description, screenshot; game opens in an in-page window | app/page.tsx tile + modal iframe; public/screenshots | VERIFIED IN CODE |
| Godot web exports on WebAssembly | public/games/*/index.wasm, index.pck | VERIFIED (files) |
| Cross-origin headers for /games/* | next.config.js COOP + COEP | VERIFIED IN CODE |
| Adding a game: files in its folder, then live: true | README 'Adding the remaining three games' | VERIFIED (README) |
| Required credit to Shesh Narayan Gupta's book on every tile | app/page.tsx CREDIT | VERIFIED IN CODE |
| Next step: move into humanitarians.ai via a branch | README 'Moving this to the real humanitarians.ai subdomain' | VERIFIED (README) |
| Done in Mohan's first week; for the Loon Center museum experience | Mohan's note; app/page.tsx hero text | FROM MOHAN'S NOTES |

FROM MOHAN'S NOTES = Mohan's own first-person report; the evidence is outside this folder (the live website repo, the production database, or a design not yet built). The video states these as his account and adds no numbers beyond his notes.
