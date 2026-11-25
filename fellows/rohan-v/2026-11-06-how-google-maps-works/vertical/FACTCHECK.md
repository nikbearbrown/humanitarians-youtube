# FACTCHECK — How Google Maps Works

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-11-09. "The run" means `maps.py` →
`evidence/run.log` / `evidence/results.json` / `evidence/scene.json`. It is a **simulation** (seed 1106): GPS
ranging from simulated satellites, solved for position and the phone's clock; a 30 × 30 grid city with 1,670 road
segments (local streets 30 km/h, avenues 50, a highway 90); rush-hour traffic with a crash on one avenue; 237
trips; one cafe's 8 Fridays; one bus route. **Nothing here is Google's data or Google's code**: the GPS, traffic,
arrival-time, busyness and crowding numbers are my simulation's. Google has never published which routing
algorithm Maps uses. Facts about Google Maps, with URLs and confidence levels: `week-11/_research/facts-maps.md`
(summarised in SOURCES.md). B01–B07 are HyperFrames compositions written by `build_hf.py` from the run's files.

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | I built a small version of each part: finding you, the route, traffic, how busy a cafe or a bus will be | `maps.py`, sections 1–6 | ✅ |
| 4 | B01 | Your phone times signals from at least four satellites; three pin down where you are, the fourth corrects its clock | facts-maps §1.1, §1.2; run: "3 satellites: 3 equations for 4 unknowns (x, y, z, clock): no unique answer" | ✅ |
| 5 | B01 | One millisecond off is three hundred kilometres | run: "a 1 ms clock error is 300 km of range error"; screen "A CLOCK 1 MS OFF · 300 km OF RANGE ERROR" | ✅ (299.8 km, below) |
| 6 | B01 | In my simulation, open sky gave about five metres | run: "open sky, 8 satellites, 3 m ranging noise: median error 5.3 m, 95% within 15.0 m"; screen "≈ 5 m" | ✅ measured |
| 7 | B01 | Between tall buildings, about seventy | run: "5 high satellites + reflections: median 68.8 m, 95% within 294.2 m"; screen "≈ 69 m" | ✅ measured |
| 8 | B01 | That's the blue circle: how unsure it is | Google Maps Help (§1.7: the light blue circle; smaller means more certain) | ✅ |
| 9 | B01 | On screen: eight satellites, three range rings and a clock on the fourth, the blue dot | the run's example fix (`scene.json` `gps.sats`: 8 satellites, error 2.7 m, clock recovered 1.0000 ms); rings drawn flat, a schematic | ✅ illustration of measured geometry |
| 10 | B02 | The map is built from Street View cars, satellite and aerial photos, data partners and people's edits | §2.1, §2.3, §2.4 (2019) | ✅ |
| 11 | B02 | AI reads signs and house numbers in the images | §2.5 (2017), §2.6 (2021); the plate "NO. 1106" is a drawn example | ✅ |
| 12 | B02 | More than two billion people use it every month | §2.8 ("more than 2 billion users per month", 6 Feb 2025); screen "2 billion+ PEOPLE A MONTH · 2025" | ✅ |
| 13 | B03 | The roads become a graph: corners joined by streets, each with a travel time | §3 safe line; `maps.py`: travel time = length ÷ speed limit | ✅ |
| 14 | B03 | A city with nine hundred corners | run: "explored 826 of 900 intersections"; screen "MY CITY · 900 CORNERS" | ✅ |
| 15 | B03 | Dijkstra's algorithm checked eight hundred and twenty-six | run: "Dijkstra: explored 826 of 900 intersections; best route 6.8 min, 44 segments"; §3.3 | ✅ measured |
| 16 | B03 | A-star, which aims at the destination, checked five hundred and forty-seven, and found the same route | run: "A*: explored 547 intersections (aims at the destination); same route: True, 6.8 min"; §3.4; screen "6.8 min · SAME ROUTE, BOTH WAYS" | ✅ measured |
| 17 | B03 | Google doesn't publish its exact recipe | §3 ground rule, §3.2, §3.7; screen, with Google's mark: "GOOGLE DOESN'T PUBLISH ITS RECIPE" | ✅ |
| 18 | B04 | Since 2009, phones with location on have sent anonymous speeds | Official Google Blog, 25 Aug 2009 (§4.1, §4.2); screen "SINCE 2009 · ANONYMOUS SPEEDS" | ✅ |
| 19 | B04 | Compared with how each road usually behaves | §4.3 (2020) | ✅ |
| 20 | B04 | In my city, history alone coloured eighty-seven percent of roads right | run, 0 phones: "colour right on 87.4% of roads"; screen "87%" | ✅ measured |
| 21 | B04 | … but missed a crash | run, 0 phones: "crash shown red on 0% of its segments"; screen "missed" | ✅ measured |
| 22 | B04 | Five hundred phones were enough to turn it red | run, 500 phones: "crash shown red on 100% of its segments" (100 phones: 50%); screen "500 phones · TURN THE CRASH RED · 100% OF ITS ROADS" | ✅ measured |
| 23 | B04 | On screen: green, amber, red, "MOVING / SLOW / JAMMED" | Maps' colours (§4.7); the levels are mine: red below 40% of the speed limit, amber below 75% | ✅ |
| 24 | B05 | Arrival times use both | historical plus live (§4.3, §5.6) | ✅ |
| 25 | B05 | From speed limits alone, my estimates were off by nineteen percent | run: "speed limits only: median error 18.7%"; screen "19%" | ✅ measured |
| 26 | B05 | History plus live phones: three percent | run: "history + live: median error 3.1%"; screen "3%" | ✅ measured (live alone 3.0%, below) |
| 27 | B05 | Google says its arrival times are accurate for over ninety-seven percent of trips | §5.1 (3 Sep 2020); screen "GOOGLE: ACCURATE FOR OVER 97% OF TRIPS (2020)" | ✅ Google's claim; "accurate" undefined |
| 28 | B05 | On screen: one trip, the directions card "8 min (4.9 km)", "THE ACTUAL TRIP 8.2 min", "SPEED LIMITS SAID 6.1 min" | `scene.json` `eta_example`: actual 8.25, limits 6.08, history + live 7.72 (rounded to 8); path 4.94 km. The card's "Fastest route now, with live traffic" is app-style wording | ✅ measured, drawn card |
| 29 | B06 | Popular times come from people who opted in, pooled and privacy-protected, shown only when enough people visit | §6.1, §6.3, §6.4 | ✅ |
| 30 | B06 | I counted a quarter of one cafe's visitors | run: "25% of visitors' phones counted"; "real visitors 2,276; counted 565"; screen "565 / 2,276 · VISITS COUNTED · A QUARTER" | ✅ measured |
| 31 | B06 | … and added privacy noise | run: "Laplace noise, epsilon 1.0", on each hour's total; a stand-in for Google's differential privacy, whose settings aren't published | ✅ |
| 32 | B06 | The bars still matched the real crowd, busiest at one o'clock | run: "correlation 0.988; busiest hour 13:00 (real 13:00)"; card "Fridays", "1 PM: Usually as busy as it gets", dashed bars = the real crowd | ✅ measured |
| 33 | B06 | A quiet shop had too little data, so it got no chart | run: "31 counted visits in 8 weeks; with a 100-visit minimum it shows no chart"; screen "QUIET SHOP · Not enough data · 31 VISITS COUNTED". The 100 is my threshold; Google publishes none (§6.3) | ✅ measured |
| 34 | B07 | Agencies publish timetables and live vehicle data in an open format called GTFS | gtfs.org and the GTFS Realtime reference (§7.1, §7.2); screen "OPEN FORMAT: TIMETABLES + LIVE VEHICLES" | ✅ |
| 35 | B07 | Crowding comes from riders answering a quick question | Google, 27 Jun 2019 (§7.5, §7.6); since 2021 also AI and location trends (§7.8) | ✅ simplified |
| 36 | B07 | With three in a hundred riders answering, my predictions were right for eighty-one percent of trips | run: "3% of riders answer"; "631 answers"; "predicted level matches the next day's real crowding on 81.2% of trips" (26 of 32); screen "81% · OF TRIPS RIGHT", "3 in 100 · RIDERS ANSWERED" | ✅ measured |
| 37 | B07 | On screen: "How crowded was it?" with three answers; 32 trips, predicted above the next day, a white mark on each of the 6 misses | `scene.json` `bus.pred`, `bus.truth`; the question card is drawn | ✅ measured, drawn card |
| 38 | B08 | When the blue circle is big, trust your eyes | B01; §1.7, §1.11 | ✅ as advice |
| 39 | B08 | Report crashes and closures | incident reports, including Crash and Lane closure (§4.8, §4.9) | ✅ as advice |
| 40 | B08 | Answer the crowding question: that's how the next rider knows | §7.6; B07 | ✅ as advice |
| 41 | B09 | "Satellites find you, a graph finds the route, and millions of phones fill in the rest" | summary of B01–B07; scale: over 5 million traffic updates a second (§4.6, 2026) | ✅ |

## The Google Maps UI on screen is drawn, not captured

The directions card ("8 min"), the "Popular times" card, the "How crowded was it?" question, the blue dot, the red
pin and the blue route are drawn by `build_hf.py` (`gm_card`, `blue_dot`, `gm_pin`, `route_lines`) to resemble
the app's night mode. They are **illustrations built from my run's numbers, not screenshots**: no Google artwork
is used except Google's mark beside its name (LOGO LAW, `assets/google-01.svg`). Their wording ("Fastest route now,
with live traffic", "Usually as busy as it gets", "Many empty seats / Few empty seats / Standing room only")
follows the app's style and is not a sourced claim; the narration doesn't repeat it.

## Arithmetic, checked separately

- **Clock.** 0.001 s × 299,792,458 m/s = 299.8 km, shown as 300.
- **A-star.** Its guess of the time left is the straight-line distance at highway speed (90 km/h), which never
  overestimates, so it must find the same best route; it did (44 segments, 6.77 min in `results.json`).
- **Traffic.** A road gets a live speed when 3 or more phones drove it; otherwise history (the mean of 20 past
  days). Phones plan their own trips with usual speeds, so they don't avoid the crash (BUILD-LOG §2). The crash is
  4 avenue segments at 12% of the limit.
- **Arrival time.** Error = |predicted − actual| ÷ actual, over the 237 of 300 drawn trips longer than 1.5 km;
  "history + live" = 0.7 × live + 0.3 × history. Live alone was 3.0% and history alone 3.7%, so in my city the
  blend did not beat live alone; the narration only says history plus live came to three percent. The live speeds
  come from the same day's 2,000 phones, which flatters them.
- **Popular times.** 8 Fridays, 6:00–22:00; 565 / 2,276 = 24.8% counted; Laplace noise of scale 1/ε on each
  hour's total; bars scaled to the busiest hour.
- **Crowding.** Many seats below 24 riders (60% of 40 seats), few seats up to 40, standing above; a trip's
  prediction is its most common answer over 30 days, given 3 or more answers; all 32 trips had enough.

## Not claimed

- That Google Maps uses Dijkstra's algorithm, A-star or any named algorithm (facts-maps "do not say"): B03 tests
  both on my city.
- That a phone or Google Maps is accurate to 5 m: B01's 5 and 70 m are my simulation (3 m ranging noise, up to
  25 m of reflections), and GPS.gov's 4.9 m (§1.4) is not used.
- That 500 phones catch a crash on real roads, or any real coverage figure.
- What "accurate" means behind Google's 97% (§5.1), or that my 3% is comparable to it.
- A minimum number of visits for popular times (§6.3); that live traffic uses differential privacy (facts-maps
  "do not say").
- That crowding predictions come only from rider answers today (§7.8).
- That any card, pin, dot or route on screen is a screenshot of the app.
