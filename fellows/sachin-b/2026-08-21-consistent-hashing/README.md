# Claude, Ringed.

Week 3 STEM video: consistent hashing — the ring, minimal remapping when a
node is added or removed, and why real systems add virtual nodes to smooth
uneven load. A system-design interview staple, explained mechanically.

| | |
|---|---|
| **Runtime** | 1:33 (92.7s) |
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
| B00 | Cold open | The mechanism, not just the buzzword |
| B01 | Executive summary | Hash servers and keys onto the same circle |
| B02 | Framework | The ring: a server per point, a key's owner is the next point clockwise |
| B03 | Worked example | Four keys, assigned by walking clockwise |
| B04 | Dynamic case | Add a 5th server — only the local arc remaps |
| B05 | Falsifiability | Few servers = uneven arcs; virtual nodes fix it |
| B06 | Verdict | Locality is real; fairness needs virtual nodes in production |
| B07 | Handoff | Your turn: build the ring, add/remove a node, measure the remap |
| B08 | Outro | "Claude, Ringed." |

## Sourcing

No invented numbers — the only quantitative claim ("~1/N keys move") is a
structural property of the algorithm. See `FACTCHECK.md`.
