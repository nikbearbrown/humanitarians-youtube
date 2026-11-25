# BUILD-LOG — "How Spotify Picks Songs"

What broke, what it cost, and what changed because of it. Built Monday 2026-11-09 for the week of 2–6 Nov,
alongside this week's Google Maps reel.

## 1 — A service small enough to check

Spotify's data and code aren't available, and its recipe isn't published, so `recs.py` builds a made-up service:
songs in 8 Western genres, listeners whose tastes mix one to three genres, and play counts with a strong
popularity pull, so a few songs get most of the plays (the top 10% of songs get 46% of all plays). The
recommender is the textbook one for play counts, implicit-feedback matrix factorisation by alternating least
squares, written out in NumPy, so nothing was downloaded. Genre labels only build the data and grade the result.

## 2 — The first service was too easy

The first version of the data gave a 98% hit rate and put a song's nearest songs in its own genre 97.5% of the
time, and its feedback loop showed no bubble. A test that nearly everything passes doesn't show what the
recommender adds. The data was made sparser and the genres made to overlap. As it stands: 1,600 songs and 3,000 listeners;
indie and rock, pop and electronic, jazz and classical, country and rock, pop and hip-hop share listeners; every
listener plays a little of everything; most listeners are light (about 60 plays), a few heavy. Results now: hit
rate **74.1%** for the taste numbers, **65.3%** for "just the hits", **6.4%** for random; same-genre neighbours
**83.7%**, lowest for rock (62%) and pop (68%), the genres with the most overlap.

## 3 — The feedback loop broadened instead of narrowing

The expected story was a filter bubble: listeners play what they're shown, the model retrains, the lists narrow.
Over 8 rounds the run measured the opposite: genres per list rose from 4.05 to 4.66, the share of the catalogue
recommended rose from 69.1% to 76.2%, and the hits' share of slots fell from 76.4% to 63.2%. The narration
follows the measurement. It makes no filter-bubble claim; B06 shows only the with-and-without-exploration
comparison at round 0 (catalogue 69.1% → 99.5%, hits' share 76.4% → 63.4%). Spotify's own research on less varied
algorithmic listening is cited as a correlation in SOURCES and not narrated.

## 4 — Sanity checks on the run

- **"In nobody's list"**: `recs.py` prints the 0 as a constant, and `RecsPopularity` draws it the same way. A
  partial re-run from a copy of the script reproduced the accuracy section exactly and found every listener had at
  least 882 unheard songs scoring above zero, so a song scoring 0 cannot reach any top 10. The claim stands.
- **"Most boxes empty"**: 3.5% of the run's listener-song boxes have a play; the drawn corner, labelled
  ILLUSTRATION, fills about 6% so the lit boxes can be seen.
- **"Almost the whole catalogue"**: 99.5%, which the screen rounds to 100%; the narration says "almost".
- **The taste map** is a 2-D projection that keeps 16% of the variance; the 84% is measured on all 24 numbers.
- **The popularity curve** is drawn compressed so the long tail is visible; it is the shape of the run's 1/rank
  law, not to scale.
- **B01's listener rows and B02's taste-number values** are illustrations, and the scene headers say so.

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/SpotifyRecs_RohanV.mp4` | 3840×2160 | 126.17 s | `3d40a17b000001d84b9a98beb72a661bedde53e908a9a85a5b4fec8a0f5433ed` |
| 9:16 | `vertical/SpotifyRecs_RohanV.mp4` | 2160×3840 | 126.17 s | `4864b795391b73959992aacf39248006e8262a8fe50e19af2f1ad4d83eddbcd1` |

Gates on the accepted finals: GATE F pass; GATE T pass, 0 FAILs ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR (both cuts). Looked at by eye:
[qc-sheet-16x9.png](./qc-sheet-16x9.png), [qc-sheet-9x16.png](./qc-sheet-9x16.png) (one frame per beat at 85%, from the finals).

Gate notes: B03's taste map (1,600 coloured dots) is a data image, so `RecsNeighbours` and `RecsNeighbours916` joined
the diegetic list in `type_check.py` (§8.1, §8.3 and, new this week, §8.3b per-blob contrast now honour that list);
the scene's own labels pass at the floor. Phone layouts: after review, everything below the title sits in one
evenly spaced column and the closing line is dropped on the phone, so no panel or text overlaps.

Accepted on 2026-11-09 after re-renders for the phone layouts and the gate fixes above. Uploaded to Google Drive
`2026-11-06/landscape/` and `2026-11-06/vertical/`; md5 of each Drive copy matches the local master.
