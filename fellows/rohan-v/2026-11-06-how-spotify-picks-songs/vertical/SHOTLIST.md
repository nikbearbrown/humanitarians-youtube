# SHOTLIST — "How Spotify Picks Songs"

9 beats, 125.97s (2:05). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 42 cues authored, 42 resolved.

A tech explainer for the week of 2–6 Nov: how a music app recommends songs, on a made-up service I built (recs.py: 1,600 songs in 8 Western genres, 3,000 listeners) and a textbook implicit-feedback ALS recommender. Nothing is Spotify's data or code.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 13.50s | `ClaudeComposerAsk` | library |
| B01 | SIGNALS | 0:13 | 15.62s | `RecsSignals` | **new** |
| B02 | THE GRID | 0:29 | 20.18s | `RecsGrid` | **new** |
| B03 | WHAT IT LEARNED | 0:49 | 15.34s | `RecsNeighbours` | **new** |
| B04 | THE TEST | 1:04 | 14.19s | `RecsAccuracy` | **new** |
| B05 | THE CATCH | 1:18 | 14.93s | `RecsPopularity` | **new** |
| B06 | EXPLORE | 1:33 | 14.38s | `RecsExplore` | **new** |
| B07 | WHAT TO DO | 1:48 | 10.88s | `HaiApplyCard` | library |
| B08 | OUTRO | 1:59 | 6.95s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how Spotify picks songs: how an app guesses what you'll want to hear next. Spotify doesn't publish its recipe, so I built a small recommender to see how the idea works.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `picks` | “how Spotify picks songs” | 0.180 | 2.43s |
| `guesses` | “guesses what” | 0.388 | 5.23s |
| `recipe` | “doesn't publish” | 0.603 | 8.13s |
| `built` | “I built” | 0.756 | 10.20s |

### B01 — SIGNALS · `RecsSignals`

> Spotify says the most important input is your taste profile: what you search, play, skip and save. There are no star ratings, so it learns from what you do. It also looks at people with similar taste. That idea is called collaborative filtering.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `profile` | “taste profile” | 0.156 | 2.43s |
| `search` | “what you search” | 0.247 | 3.87s |
| `skip` | “skip and save” | 0.356 | 5.57s |
| `stars` | “no star ratings” | 0.469 | 7.33s |
| `similar` | “similar taste” | 0.749 | 11.70s |
| `cf` | “collaborative filtering” | 0.905 | 14.13s |

### B02 — THE GRID · `RecsGrid`

> Picture a giant grid: listeners down the side, songs across the top, and most boxes empty. I made one up: three thousand listeners and sixteen hundred songs. Matrix factorisation fills it in by giving every listener and every song twenty-four hidden taste numbers. A song's score is how well the two lists match.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `grid` | “a giant grid” | 0.013 | 0.27s |
| `empty` | “most boxes empty” | 0.228 | 4.60s |
| `made` | “I made one up” | 0.320 | 6.47s |
| `fills` | “fills it in” | 0.606 | 12.23s |
| `numbers` | “twenty-four” | 0.758 | 15.30s |
| `score` | “A song's score” | 0.866 | 17.47s |

### B03 — WHAT IT LEARNED · `RecsNeighbours`

> It was never told a single genre. Still, a song's five closest songs were the same genre eighty-four percent of the time, because the same people play them. Close means the two lists of numbers point the same way. That's cosine similarity.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `never` | “never told” | 0.013 | 0.20s |
| `five` | “five closest” | 0.226 | 3.47s |
| `eighty` | “eighty-four” | 0.413 | 6.33s |
| `same` | “same people” | 0.552 | 8.47s |
| `point` | “point the” | 0.784 | 12.03s |
| `cosine` | “cosine similarity” | 0.928 | 14.23s |

### B04 — THE TEST · `RecsAccuracy`

> Then I hid a fifth of each listener's songs and asked for ten picks. Seventy-four percent of listeners got at least one hidden song back. Just recommending the hits did nearly as well, sixty-five percent. Random picks: six.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `hid` | “I hid a fifth” | 0.012 | 0.17s |
| `ten` | “ten picks” | 0.223 | 3.17s |
| `seventy` | “Seventy-four percent” | 0.298 | 4.23s |
| `hits` | “recommending the hits” | 0.585 | 8.30s |
| `random` | “Random” | 0.843 | 11.97s |

### B05 — THE CATCH · `RecsPopularity`

> But look at what it picks. Only six percent of its picks came from the less popular half of the songs, though a quarter of all listening happens there. And a brand-new song, with no plays yet, appeared in nobody's list. That's the cold-start problem.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `look` | “look at what it picks” | 0.007 | 0.10s |
| `six` | “Only six percent” | 0.109 | 1.63s |
| `quarter` | “a quarter” | 0.411 | 6.13s |
| `new` | “brand-new song” | 0.614 | 9.17s |
| `nobody` | “nobody's list” | 0.788 | 11.77s |
| `cold` | “cold-start” | 0.931 | 13.90s |

### B06 — EXPLORE · `RecsExplore`

> So I gave two of every ten slots to songs few people had heard. Almost the whole catalogue came into play, and the biggest hits' share of the slots fell from seventy-six to sixty-three percent. Spotify experiments with exploration too.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `two` | “two of every ten” | 0.025 | 0.37s |
| `whole` | “whole catalogue” | 0.308 | 4.43s |
| `share` | “share of the slots” | 0.498 | 7.17s |
| `fell` | “seventy-six to” | 0.633 | 9.10s |
| `spotify` | “Spotify experiments” | 0.776 | 11.17s |

### B07 — WHAT TO DO · `HaiApplyCard`

> What can you do? Play, skip and save on purpose: those are its signals. Exclude playlists like sleep sounds from your taste profile. And go looking for new music yourself.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `purpose` | “on purpose” | 0.199 | 2.17s |
| `exclude` | “Exclude playlists” | 0.466 | 5.07s |
| `looking` | “go looking” | 0.830 | 9.03s |

### B08 — OUTRO · `HaiTitleOutro`

> What you do goes in, taste numbers come out, with a lean toward the hits. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “lean toward the hits” | 0.389 | 2.70s |

