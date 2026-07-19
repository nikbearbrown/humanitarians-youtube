# SHOTLIST -- cli-realtime-verdict
## Build a Real-Time Verdict Module with Claude Code

| Beat | Source | Duration | Description |
|------|--------|----------|-------------|
| B00  | remotion | 3.4s | NikBearBrownOpen -- Real-time verdict, taken apart |
| B01  | manim | 31.6s | B01_Problem -- mean vs WCET title card |
| B02  | remotion | 23.0s | NikBearBrownTerminalAsk -- realtime.py prompt |
| B03  | remotion | 25.1s | NikBearBrownCodeBlock -- realtime.py code |
| B04  | manim | 25.3s | B04_Realtime -- latency histogram + tail (illustrative) |
| B05  | remotion | 14.1s | NikBearBrownTerminalAsk -- add jitter change |
| B06  | manim | 24.2s | B06_RealtimeJitter -- GC jitter extends tail (illustrative) |
| B07  | manim | 18.4s | B07_Summary -- lesson card |
| B08  | manim | 25.4s | B08_NextSteps -- action items |
| B09  | remotion | 7.2s | NikBearBrownOutro |

**Total: 197.7s (~3:18)**

---

NOTE: B04 and B06 use synthetic/illustrative data.
Swap manim/B04.mp4 and manim/B06.mp4 with a real capture once
a real latency distribution (measured on target hardware during production
inference under full load) is available.
