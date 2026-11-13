# BUILD-LOG — "How Google Maps Works"

What broke, what it cost, and what changed because of it. Built Monday 2026-11-09 for the week of 2–6 Nov,
alongside this week's Spotify reel. The first reel built with HyperFrames (B01–B07); B00, B08 and B09 are the
channel's Remotion cards.

## 1 — A sky and a city small enough to check

Google's data and code aren't available, and it has never said which routing algorithm Maps uses, so `maps.py`
simulates each job: satellite ranging solved for position and the phone's clock; a 30 × 30 grid city with local
streets, avenues and a highway, searched by Dijkstra's algorithm and A-star; rush-hour traffic with a jam and a
crash, estimated from phones; 300 drawn trips (237 over 1.5 km kept); one cafe's visits, a quarter counted, with
Laplace noise; one bus route with 3% of riders answering. Everything is seeded and in NumPy.

## 2 — The crash never turned red

At first no number of phones turned the crash red. The simulated phones planned their trips with the true live
speeds, so they all routed around the crash, and no phone ever drove it to report it. Real drivers don't know
about a crash before they reach it. Phones now plan with the usual (historical) speeds; after: 0 phones, 0% of the
crash's segments red; 100 phones, 50%; 500 or more, 100%, the figure B04 reports.

## 3 — "A star" became "uh star"

The narrator's pronunciation step read "A star" as "uh star", the article, not the letter. The narration now
spells it "A-star", and B03 was voiced again; the on-screen label is "A-STAR".

## 4 — HyperFrames instead of Remotion

Rohan asked to try HyperFrames for this video. B01–B07 are one HyperFrames composition per beat and aspect
(`hyperframes/B0x-l.html` at 3840×2160, `B0x-v.html` at 2160×3840), written by `build_hf.py` from the run's files
and rendered into `media/` and `pantry/`, where the Brutalist compiler picks them up like any beat clip. Their
beat-sheet shots keep props but no Remotion pattern, so `sync_cues.py` still writes the word-clock cues there and
the compositions read them; each reveal lands on its word.

## 5 — From cream to night city

The first HyperFrames version used the channel's cream cards (`build_hf_v1_cream.py`, kept). Rohan asked for a
more premium look that wasn't cream ("you are the best motion designer in the world") and for the Google Maps UI
elements to look exactly like the app. The look became a night city: a navy ground, the city as a tilted 3D
plane with glowing roads, a moving camera, light trails, glass panels; and Google-style night-mode cards, blue
dot, red pin and blue route, drawn from my run's numbers. They are illustrations, not screenshots, and FACTCHECK
and the description say so.

## 6 — Rendering on this machine

- **Nothing on C:.** The first HyperFrames render tried to put about 21 GB of temporary frames on C:. Rendering
  now sets `TEMP` and `TMP` to `D:/Rohan/Claude/HyperFrames/tmp` (`build_hf.py`, `render`).
- **C: full, memory low.** Renders failed while C: was full and memory was low, with Pro Tools holding about
  10 GB.
- **Cancelled from a hidden window.** After Rohan freed space, a render started from the hidden-window launcher
  (`week-11/hidden.ps1`, written so runs wouldn't put console windows on screen) ended with "render_cancelled";
  the same render run directly worked.
- **Windows on the screen.** HyperFrames runs opened visible windows on Rohan's screen, and he flagged it.

## 7 — Sanity checks on the run

- **"About five metres"** is the simulation's median with 3 m ranging noise; it sits near GPS.gov's 4.9 m by
  construction, not as a test of it, so the narration says "in my simulation".
- **"History plus live: three percent"**: 3.1%. Live alone was 3.0% in my city, so the narration doesn't say the
  blend beats live.
- **"Too little data"**: the 100-visit minimum is mine; Google publishes no number.
- **The 8 min card** is the history-plus-live estimate for the example trip (7.72 min), rounded.

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/GoogleMaps_RohanV.mp4` | 3840×2160 | 157.17 s | `512ecbc9a78cbe6c1f9c2c39b1385573e2be264f642c23e51bc7fbf42a4157e0` |
| 9:16 | `vertical/GoogleMaps_RohanV.mp4` | 2160×3840 | 157.17 s | `c667c773369650b44b96a504b296b81c0cddc08f6a42d524b887e0760c75344d` |

Gates on the accepted finals: GATE F pass; GATE T pass, 0 FAILs ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR (both cuts). Looked at by eye:
[qc-sheet-16x9.png](./qc-sheet-16x9.png), [qc-sheet-9x16.png](./qc-sheet-9x16.png) (one frame per beat at 85%, from the finals).

Gate notes: the HyperFrames clips were rendered first, then compiled by `./art final` like any beat clip
(B01–B07 from `media/` and, for the phone cut, `pantry/<beat>-916.mp4`). GATE T now names these beats
`HyperFrames:<composition>`; the moving phone and visitor dots in `traffic` and `busy` are data marks and joined the
diegetic list (§8.1, §8.3b, §8.6b). Gate V: the night-map look fills the frame with dim roads, so each HyperFrames beat
declares `qc.contrast_regions` (title + HUD text, tested on frames of the rendered clips) with a written reason
(`add_qc.py`); two phone beats (B02, B04) declare `sparse_by_design` because their panels reveal on cue. Edge-bleed
on four clips was fixed by moving the art in from the frame edge, not waived. On the phone, the HUD is laid out as
one evenly spaced column below the map, and the closing line is dropped, after review found overlaps.

Accepted on 2026-11-09 after re-renders for the phone layouts and the gate fixes above. Uploaded to Google Drive
`2026-11-06/landscape/` and `2026-11-06/vertical/`; md5 of each Drive copy matches the local master.
