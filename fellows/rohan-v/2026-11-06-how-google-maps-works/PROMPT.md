# PROMPT — "How Google Maps Works"

The brief, and how each constraint was resolved.

## Constraints given

Rohan, for the week of 2–6 Nov: two STEM explainers, this one on how Google Maps works, the other on how Spotify
picks songs. Hours for the week: 20, across both videos. Built Monday 9 Nov. During the build he asked to try
HyperFrames instead of Remotion for this video, then for a more premium look that wasn't cream, and for the Google
Maps UI elements to look exactly like the app:

> you are the best motion designer in the world

## How each constraint was resolved

| Constraint | Resolution |
|---|---|
| A STEM topic | positioning, the road graph and shortest paths, traffic from phones, arrival times, popular times, transit crowding |
| Required opening line, AI disclosure | B00, verbatim; disclosure on screen |
| Executable evidence | `maps.py` simulates each part; every measured number in B01 and B03–B07 is the run's |
| Google's routing algorithm is unpublished | said in B03; Dijkstra's and A-star are tested on my city, not attributed to Google |
| Try HyperFrames | B01–B07 are HyperFrames compositions; B00, B08, B09 stay on the channel's Remotion cards |
| Premium, not cream | the "night city" look: a 3D city plane, a moving camera, light trails, glass panels (`build_hf.py`); the cream version is kept as `build_hf_v1_cream.py` |
| Google Maps UI that looks like the app | cards, blue dot, red pin and blue route drawn in the app's night-mode style from my run's numbers; not screenshots, and FACTCHECK says so |
| Nothing on C: (standing rule) | HyperFrames' temporary frames go to D: (BUILD-LOG §6) |
| Typeset math | none: errors are shown as percentages, the formulas are in FACTCHECK |
| 4K, both aspects, native 9:16 | 3840×2160 and 2160×3840; every HyperFrames beat has its own portrait composition |
| LOGO LAW | Google Maps is named on screen with Google's mark |
| No recordings | no footage or screenshots; everything is drawn from the simulation |
| No surname; no person icons | "Row-Haan" in narration, "Rohan V." on screen; phones and visitors are dots, no person drawn; no researcher named beyond Dijkstra's algorithm |
