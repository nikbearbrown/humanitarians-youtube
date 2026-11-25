# SHOTLIST — "How Google Maps Works"

10 beats, 156.94s (2:36). Every duration is the measured Kokoro narration length (plus, where noted, the listening clips appended by mix_listen.py); the visuals are cut to fit the audio, never the other way round.

**Word-clock choreographed.** `align.py` (faster-whisper) measured when every word is spoken, `cues.json` names an anchor phrase per reveal, and `sync_cues.py` wrote the resolved fractions into `shot.remotion.props.cues`. 51 cues authored, 51 resolved.

A tech explainer for the week of 2–6 Nov: how a maps app finds you, routes you, sees traffic and predicts crowds, on a simulated sky and city I built (maps.py). B01–B07 are HyperFrames compositions in a night-mode look (build_hf.py), rendered at 4K in both aspects; the intro, apply card and outro are the channel's standard Remotion cards. Nothing is Google's data or code; the Google Maps UI cards are drawn to resemble the app.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 13.59s | `ClaudeComposerAsk` | library |
| B01 | WHERE AM I | 0:13 | 21.72s | `HyperFrames:gps` | **new · HyperFrames** |
| B02 | THE MAP | 0:35 | 14.06s | `HyperFrames:build` | **new · HyperFrames** |
| B03 | THE ROUTE | 0:49 | 21.18s | `HyperFrames:route` | **new · HyperFrames** |
| B04 | TRAFFIC | 1:10 | 18.47s | `HyperFrames:traffic` | **new · HyperFrames** |
| B05 | ARRIVAL TIME | 1:29 | 14.53s | `HyperFrames:eta` | **new · HyperFrames** |
| B06 | HOW BUSY | 1:43 | 19.39s | `HyperFrames:busy` | **new · HyperFrames** |
| B07 | HOW CROWDED | 2:02 | 16.70s | `HyperFrames:bus` | **new · HyperFrames** |
| B08 | WHAT TO DO | 2:19 | 9.11s | `HaiApplyCard` | library |
| B09 | OUTRO | 2:28 | 8.19s | `HaiTitleOutro` | library |

## Choreography — what happens, and on which word

### B00 — ASK · `ClaudeComposerAsk`

> Hi, I am Row-Haan and this video is about how Google Maps works: how it finds you, picks a route, sees traffic, and knows how busy a cafe or a bus will be. I built a small version of each part to see how.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `finds` | “how it finds you” | 0.304 | 4.13s |
| `route` | “picks a route” | 0.392 | 5.33s |
| `busy` | “how busy” | 0.579 | 7.87s |
| `built` | “I built” | 0.797 | 10.83s |

### B01 — WHERE AM I · `HyperFrames:gps`

> First, where are you. Your phone times signals from at least four satellites. Three pin down where you are, and the fourth corrects your phone's clock, which matters: one millisecond off is three hundred kilometres. In my simulation, open sky gave about five metres. Between tall buildings, about seventy. That's the blue circle: how unsure it is.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `where` | “where are you” | 0.023 | 0.50s |
| `four` | “at least four” | 0.144 | 3.13s |
| `three` | “Three pin down” | 0.224 | 4.87s |
| `clock` | “corrects your” | 0.316 | 6.87s |
| `milli` | “one millisecond” | 0.434 | 9.43s |
| `open` | “open sky” | 0.638 | 13.87s |
| `tall` | “tall buildings” | 0.777 | 16.87s |
| `circle` | “the blue circle” | 0.895 | 19.43s |

### B02 — THE MAP · `HyperFrames:build`

> The map itself is built from Street View cars, satellite and aerial photos, data partners and people's edits, with AI reading signs and house numbers in the images. More than two billion people use it every month.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `street` | “Street View cars” | 0.102 | 1.43s |
| `photos` | “aerial photos” | 0.266 | 3.73s |
| `edits` | “edits” | 0.472 | 6.63s |
| `ai` | “with AI reading” | 0.529 | 7.43s |
| `billion` | “two billion” | 0.849 | 11.93s |

### B03 — THE ROUTE · `HyperFrames:route`

> To find a route, the roads become a graph: corners joined by streets, each with a travel time. I built a city with nine hundred corners. Dijkstra's algorithm checked eight hundred and twenty-six of them. A-star, which aims at the destination, checked five hundred and forty-seven, and found the same route. Google doesn't publish its exact recipe.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `graph` | “become a graph” | 0.057 | 1.20s |
| `corners` | “corners joined” | 0.121 | 2.57s |
| `built` | “I built a” | 0.288 | 6.10s |
| `dijkstra` | “Dijkstra's” | 0.415 | 8.80s |
| `astar` | “A-star” | 0.595 | 12.60s |
| `same` | “same route” | 0.831 | 17.60s |
| `recipe` | “exact recipe” | 0.946 | 20.03s |

### B04 — TRAFFIC · `HyperFrames:traffic`

> Traffic comes from phones. Since two thousand nine, phones with location on have sent anonymous speeds, compared with how each road usually behaves. In my city, history alone coloured eighty-seven percent of roads right, but missed a crash. Five hundred phones were enough to turn it red.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `phones` | “Traffic comes from phones” | 0.000 | 0.00s |
| `since` | “Since two thousand nine” | 0.105 | 1.93s |
| `usually` | “usually behaves” | 0.444 | 8.20s |
| `history` | “history alone” | 0.599 | 11.07s |
| `crash` | “missed a crash” | 0.794 | 14.67s |
| `five` | “Five hundred phones” | 0.850 | 15.70s |
| `red` | “turn it red” | 0.951 | 17.57s |

### B05 — ARRIVAL TIME · `HyperFrames:eta`

> Arrival times use both. From speed limits alone, my estimates were off by nineteen percent. History plus live phones: three percent. Google says its arrival times are accurate for over ninety-seven percent of trips.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `both` | “use both” | 0.060 | 0.87s |
| `limits` | “speed limits” | 0.163 | 2.37s |
| `live` | “History plus” | 0.445 | 6.47s |
| `google` | “Google says” | 0.686 | 9.97s |

### B06 — HOW BUSY · `HyperFrames:busy`

> Popular times come from people who opted in, pooled and privacy-protected, and shown only when enough people visit. I counted a quarter of one cafe's visitors and added privacy noise. The bars still matched the real crowd, busiest at one o'clock. A quiet shop had too little data, so it got no chart.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `opted` | “opted in” | 0.093 | 1.80s |
| `enough` | “enough people” | 0.292 | 5.67s |
| `quarter` | “a quarter” | 0.397 | 7.70s |
| `noise` | “privacy noise” | 0.519 | 10.07s |
| `matched` | “still matched” | 0.622 | 12.07s |
| `one` | “one o'clock” | 0.758 | 14.70s |
| `shop` | “quiet shop” | 0.832 | 16.13s |

### B07 — HOW CROWDED · `HyperFrames:bus`

> For buses and trains, agencies publish timetables and live vehicle data in an open format called GTFS. Crowding comes from riders answering a quick question. With three in a hundred riders answering, my predictions were right for eighty-one percent of trips.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `agencies` | “agencies publish” | 0.100 | 1.67s |
| `gtfs` | “GTFS” | 0.365 | 6.10s |
| `riders` | “riders answering” | 0.525 | 8.77s |
| `three` | “three in a hundred” | 0.685 | 11.43s |
| `eighty` | “eighty-one” | 0.924 | 15.43s |

### B08 — WHAT TO DO · `HaiApplyCard`

> So: when the blue circle is big, trust your eyes. Report crashes and closures. And answer the crowding question. That's how the next rider knows.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `circle` | “blue circle” | 0.066 | 0.60s |
| `report` | “Report crashes” | 0.359 | 3.27s |
| `answer` | “answer the crowding” | 0.611 | 5.57s |

### B09 — OUTRO · `HaiTitleOutro`

> Satellites find you, a graph finds the route, and millions of phones fill in the rest. I'm Row-Haan, for Humanitarians AI.

| cue | anchor phrase | fraction | at |
|---|---|---|---|
| `close` | “millions of phones” | 0.362 | 2.97s |

