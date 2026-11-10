# SOURCES — How Google Maps Works

Full notes, URLs, confidence levels and the "do not say" list: `week-11/_research/facts-maps.md`. Checked 2026-11-09.

## Finding you

- ESA Navipedia, "An intuitive approach to the GNSS positioning": ranges from satellites, and why four. B01.
- GPS.gov, GPS Accuracy and Space Segment. Background for B01; not stated.
- Google Maps Help, "Find & improve your location's accuracy": the blue dot and the light blue circle. B01, B08.

## The map

- blog.google, "Google Maps 101: how we map the world" and "how imagery powers our map" (2019): data partners,
  Street View, imagery, user edits. B02.
- Google Research, "Updating Google Maps with Deep Learning and Street View" (2017): reading signs and house
  numbers. B02.
- blog.google, "Google Maps celebrates 20 years with 20 favorite features" (Feb 2025): more than 2 billion users a
  month. B02.

## The route

- "A note on two problems in connexion with graphs," Numerische Mathematik, 1959 (Dijkstra's algorithm). B03.
- "A Formal Basis for the Heuristic Determination of Minimum Cost Paths," IEEE Transactions on Systems Science
  and Cybernetics, 1968 (A-star). B03.
- "Route Planning in Transportation Networks," arXiv:1504.05140: companies keep their routing algorithms
  private. B03.
- Google Research, "World scale inverse reinforcement learning in Google Maps" (2023). Background; not stated.

## Traffic and arrival times

- Official Google Blog, "The bright side of sitting in traffic: Crowdsourcing road congestion data" (2009). B04.
- blog.google, "Google Maps 101: How AI helps predict traffic and determine routes" (2020): history plus live;
  arrival times accurate for over 97% of trips. B04, B05.
- Google Maps Help: traffic colours; incident reports. B04, B08.

## How busy, how crowded

- Google Business Profile Help, "Popular times, wait times, and visit duration": opted-in, aggregated, shown only
  with enough visits. B06.
- Google Developers Blog, on differential privacy (2019); Google Maps Help, "Get information about busy areas".
  B06.
- gtfs.org and the GTFS Realtime reference. B07.
- blog.google, "Grab a seat and be on time with new transit updates on Google Maps" and "Transit crowdedness
  trends from around the world" (2019): crowding from riders' answers. B07, B08.

## Evidence

- `maps.py`, `build_hf.py` and `evidence/` in this folder.
