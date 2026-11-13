# SHOTLIST — How Caching Makes Applications Faster

| Beat | Shot | Visual |
|---|---|---|
| B00 | Repeated requests | USER → APPLICATION → DATABASE with multiple request markers. |
| B01 | Growing database work | Multiple requests converge on the database; DATABASE LOAD increases. |
| B02 | Introduce cache | APPLICATION → CACHE → DATABASE. |
| B03 | Cache miss | Application checks cache, receives MISS, then accesses database. |
| B04 | Store result | Database result travels back and is stored in CACHE. |
| B05 | Cache hit | Application retrieves data from CACHE while DATABASE shows NO QUERY. |
| B06 | TTL expiration | Cached data displays TTL progression: 60s → 30s → 1s → EXPIRED. |
| B07 | Performance payoff | Requests are served primarily by CACHE; benefits show FASTER RESPONSES and LESS DATABASE LOAD. |

## Visual safety

- Keep titles in the upper safe zone.
- Keep explanatory captions in the lower safe zone.
- Keep the primary system diagram in the central region.
- Arrows terminate at object boundaries.
- Arrows must not cross labels or boxes.
- Avoid cropped text and edge collisions.
- Maintain sufficient spacing for all system components.

## Landscape render

Resolution: 3840x2160
Aspect ratio: 16:9
Frame rate: 24 fps
Source: Manim

## Review status

B00: Approved
B01: Approved
B02: Approved
B03: Approved
B04: Approved
B05: Approved
B06: Approved after TTL 0s was changed to TTL 1s for readability.
B07: Approved
