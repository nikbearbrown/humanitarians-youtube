# Claude, Nearest.

Week 2 STEM video: vector embeddings and ANN search — why "similar" text
ends up as nearby points in space, and how search actually finds them fast
at scale without checking every vector.

| | |
|---|---|
| **Runtime** | 1:34 (94.3s) |
| **Format** | 16:9, 3840×2160 (4K), 24 fps, h264/aac |
| **9:16 cut** | Not yet built (flagged — see BUILD-LOG.md) |
| **Voice** | Kokoro `am_onyx` — local, free, no API |
| **Beats** | 9 · Claude-skin bookends + 5 purpose-built Manim scenes |
| **Presenter** | Sachin Vishaul B |
| **Channel** | @HumanitariansAI (Mycroft) |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd (GATE V: 0 BLOCKER) · solo build, no independent reviewer · not published |

## What this video covers

| Beat | | |
|---|---|---|
| B00 | Cold open | "Similar" isn't a string match, it's a location |
| B01 | Executive summary | Text → vector → distance = similarity |
| B02 | Framework | A 2D toy map: related meaning clusters together |
| B03 | Worked example | A query point; nearest neighbors are just the closest dots |
| B04 | Mechanism at scale | Brute-force scan vs. a graph hop toward the neighborhood |
| B05 | Falsifiability | Approximate means it can miss the true nearest neighbor |
| B06 | Verdict | Recall / latency / memory — one knob, not three separate wins |
| B07 | Handoff | Your turn: brute-force vs. an ANN index, measure recall |
| B08 | Outro | "Claude, Nearest." |

## Sourcing

No invented numbers — the toy 2D map is explicitly a simplification of a
real high-dimensional space. See `FACTCHECK.md`.
