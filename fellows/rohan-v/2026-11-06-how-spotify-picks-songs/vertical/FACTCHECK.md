# FACTCHECK — How Spotify Picks Songs

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-11-09. "The run" means `recs.py` →
`evidence/run.log` / `evidence/results.json` / `evidence/scene.json`. The music service is **made up**: 1,600 songs
in 8 Western genres, 3,000 listeners, 228,797 plays (seed 2026); genres are used only to build the data and to
grade the results, never shown to the model. The recommender is the textbook one for play counts: implicit-feedback
matrix factorisation fitted by alternating least squares, from "Collaborative Filtering for Implicit Feedback
Datasets" (ICDM 2008), 24 numbers per listener and per song. **Nothing here is Spotify's data or Spotify's code.**
Outside facts, with URLs and confidence levels: `week-11/_research/facts-recs.md` (summarised in SOURCES.md).

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | Spotify doesn't publish its recipe | facts-recs header (its current internal algorithm is unpublished) and §1's script caution (inputs, not the math) | ✅ |
| 4 | B00 | I built a small recommender; on screen: learn from plays, skips and saves, taste numbers, closest matches | `recs.py` | ✅ |
| 5 | B01 | Spotify says the most important input is your taste profile: what you search, play, skip and save | Spotify's "Understanding recommendations" page (facts-recs §1.2); the page says "listen to" | ✅ |
| 6 | B01 | No star ratings, so it learns from what you do | §1.2; implicit vs explicit feedback (§3.3, §3.4) | ✅ |
| 7 | B01 | It also looks at people with similar taste: collaborative filtering | Spotify Newsroom 2020 (§1.7); the idea (§3.1) | ✅ |
| 8 | B01 | On screen: Spotify's mark, "SPOTIFY SAYS: YOUR TASTE PROFILE"; two listener rows that share songs, so one's extra song is recommended to the other | §1.2; the rows are an **illustration** (`RecsSignals` header) | ✅ illustration |
| 9 | B01 | Spark line "No ratings. Just plays, skips and saves." | §1.2; Spotify also uses other inputs (device, location, trends, content characteristics, commercial factors, §1.3–1.5) | ✅ simplified |
| 10 | B02 | A giant grid, most boxes empty | run's data: 3.5% of the 4.8 million listener-song boxes have a play (checked separately, below); screen corner labelled ILLUSTRATION, drawn about 6% full | ✅ (drawn fuller than the run) |
| 11 | B02 | I made one up: three thousand listeners, sixteen hundred songs | run: "1600 songs in 8 Western genres, 3000 listeners"; screen "3,000", "1,600" | ✅ |
| 12 | B02 | Every listener and every song gets twenty-four hidden taste numbers | `results.json` `"k": 24`; latent factors, 20 to 100 in the literature (§3.10) | ✅ |
| 13 | B02 | A song's score is how well the two lists match | the dot product (§3.12); `recs.py` scores `X[u] @ Y.T`; the two drawn lists have **illustrative** values (`RecsGrid` header) | ✅ |
| 14 | B03 | It was never told a single genre | `recs.py`: genre labels only build the data and grade it. The data was made from genres, so the structure is there to be found | ✅ |
| 15 | B03 | A song's five closest songs were the same genre eighty-four percent of the time | run: "share its genre 83.7% of the time (chance: 12.5%)"; screen "84%", "CHANCE ALONE: 13%" | ✅ measured (rounded) |
| 16 | B03 | Because the same people play them | the model sees only who played what; lowest for rock 62% and pop 68% (run), the two genres built to overlap with two neighbours each | ✅ |
| 17 | B03 | Close means the two lists point the same way: cosine similarity | §4.7; `recs.py` normalises and takes the dot product | ✅ |
| 18 | B03 | On screen: all 1,600 songs placed by their taste numbers, coloured by genre at "eighty-four"; one song and its five nearest | `scene.json` `pca` (first two principal components, 8.5% + 7.8% of the variance, `pca_var`); example song #833, jazz: nearest #959, #949, #822, #837 jazz, #233 rock (run) | ✅ measured (a 2-D projection; the 84% is measured on all 24 numbers) |
| 19 | B04 | I hid a fifth of each listener's songs and asked for ten picks | run: "20% of each listener's songs hidden; 10 recommendations each" | ✅ |
| 20 | B04 | Seventy-four percent of listeners got at least one hidden song back | run: "74.1% of listeners get at least one hidden song back"; screen "74%" | ✅ measured |
| 21 | B04 | Just recommending the hits did nearly as well, sixty-five percent | run: "most popular: 65.3%"; screen "65%" | ✅ measured |
| 22 | B04 | Random picks: six | run: "random: 6.4%"; screen "6%" | ✅ measured |
| 23 | B05 | Only six percent of its picks came from the less popular half of the songs | run: "share of recommendations from the less popular half of the catalogue: 5.9%"; screen "6%" | ✅ measured |
| 24 | B05 | A quarter of all listening happens there | run: "(share of plays: 25.8%)"; screen "26%" | ✅ measured |
| 25 | B05 | A brand-new song, with no plays yet, appeared in nobody's list | run: "its taste vector is all zeros, score 0 for everyone; it ranks on average 1174 of 1601 and appears in 0 of 3000 top-10 lists"; screen "In 0 of 3,000 lists". The "0" is printed as a constant; checked separately (below) | ✅ measured + checked |
| 26 | B05 | That's the cold-start problem | §3.2, §5.1 | ✅ |
| 27 | B05 | On screen: the catalogue from biggest hit to least played, split in half | the run's popularity law, 1/rank; drawn compressed (height ∝ (1/rank)^0.35) so the tail is visible | ✅ (shape, not to scale) |
| 28 | B06 | I gave two of every ten slots to songs few people had heard | `recs.py` `loop(explore=True)`: 8 best matches + 2 unheard songs, weighted toward the least played | ✅ |
| 29 | B06 | Almost the whole catalogue came into play | run, round 0: "catalogue recommended 69.1% (with exploration 99.5%)"; screen "69%" → "100%" (99.5 rounded) | ✅ measured |
| 30 | B06 | The biggest hits' share of the slots fell from seventy-six to sixty-three percent | run, round 0: "top 10% of songs get 76.4% of slots (63.4%)"; screen "76%" → "63%". With vs without exploration, same round; not a change over time (see below) | ✅ measured |
| 31 | B06 | Spotify experiments with exploration too | Home bandit (§1.8, 2020), BaRT (§5.6, 2018), centralised exploration (§5.3, 2024), calibration (§5.13, 2025); safe-to-say list | ✅ |
| 32 | B07 | Play, skip and save on purpose: those are its signals | §1.2 | ✅ as advice |
| 33 | B07 | Exclude playlists like sleep sounds from your taste profile; screen adds kids' playlists | §1.13, §1.14 (Help's own sleep-music example); kids & family toggle (§1.15) | ✅ |
| 34 | B07 | Go looking for new music yourself | follows from B05 | ✅ as advice |
| 35 | B08 | "What you do goes in, taste numbers come out, with a lean toward the hits" | summary of B01–B06 | ✅ |

## The feedback loop, and why the narration makes no filter-bubble claim

`recs.py` also runs a loop: each listener plays 3 of their 10 recommendations (the ones they like most, 1–3 plays
each), the model retrains, 8 rounds, with and without the two exploration slots. The expected story was that the
lists would narrow. They didn't. Without exploration, genres per list rose **4.05 → 4.66**, the share of the
catalogue recommended rose **69.1% → 76.2%**, and the top 10% of songs' share of slots fell **76.4% → 63.2%**
(with exploration: 4.65 → 5.18; 99.5% → 100.0%; 63.4% → 51.9%). So the narration says nothing about filter
bubbles, and B06 uses only round 0's with-and-without comparison. Spotify's own study of less varied algorithmic
listening ("Algorithmic Effects on the Diversity of Consumption on Spotify", WWW '20, facts-recs §5.9) is an
association, not a cause, and is cited only that way, in SOURCES.

## Arithmetic, checked separately

- **Hit rate.** The share of the 3,000 listeners whose 10 recommendations contain at least one of their hidden
  songs (20% of each listener's songs, at least one). Recall@10, not narrated: 0.179, 0.137, 0.008.
- **The less popular half.** Popularity ranks 801–1,600. Median rank of a recommended song 43, of a played song
  233 (run).
- **Cold start.** The run prints "appears in 0" as a constant. A partial re-run from a copy of `recs.py`
  (2026-11-09, not kept in `evidence/`) reproduced section 1 exactly (74.1%, 65.3%, 6.4%) and found that every
  listener had at least 882 unheard songs scoring above zero (median 1,124), so a song scoring 0 can never reach
  a top 10. The mean rank, 1,174, matched.
- **The grid.** 3.45% of listener-song boxes have at least one play (2.76% after hiding); 55.3 songs per
  listener on average (same re-run). The drawn corner fills about 6% of its boxes.
- **Confidence weighting.** `recs.py` uses c = 1 + 20·log(1 + plays), regularisation 0.1, 12 iterations; the
  paper's main form is linear, c = 1 + α·r with α = 40 (facts-recs §3.5).

## Not claimed

- That any of this is Spotify's data, code or algorithm; that Spotify uses this method, word2vec or Annoy today
  (facts-recs "do not say").
- That recommenders cause filter bubbles, on Spotify or in my test: my loop broadened.
- How much a skip or a save counts (unpublished, facts-recs §3).
- That popularity bias on Spotify is proven or disproven (§5.5 vs §5.7): B05's 6% is my recommender on my data.
- That exploration solves cold start: no brand-new songs were added during the loop.
- Discover Weekly figures, Spotify user counts, or the "three models" story.
