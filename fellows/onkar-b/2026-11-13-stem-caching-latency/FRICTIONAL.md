# Frictional log — Caching & Latency

## 2026-11-13 — the project update, in two aspect ratios

**What I was working on.** A STEM explainer regarding caching strategies, latency reduction, and memory trade-offs.

**What I tried, and what I expected.** 
- I originally focused the script purely on the hardware differences between Solid State Drives (SSDs) and RAM, expecting that to be the clearest way to explain speed.

**Where it resisted, and what I did next.** 
- Explaining hardware specifics felt outdated and didn't connect to AI compute. The real bottleneck in AI isn't SSD read/write speeds; it's the GPU/CPU mathematical inference time. 
- I pivoted the script to focus on "Redundant Compute"—the idea that forcing a model to run the exact same math twice is the true waste.

**What Claude contributed, and what I did with it.** 
- Mine: The explanation of Redis as a volatile in-memory datastore.
- Claude's: Introducing the "Cache Invalidation Trap" in Scene 4. Explaining that speed comes with the severe risk of stale data made the video much more technically nuanced.

**What I understand now, and what I still do not.**
- Understood: In AI architecture, caching isn't just about bypassing the hard drive; it is about completely bypassing the machine learning model whenever possible.