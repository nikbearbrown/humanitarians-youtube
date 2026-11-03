# Frictional Log — API Gateways and Rate Limiting

> Append dated entries as you go; never rewrite an earlier one.

## 2026-10-10 — Build a 60-second explainer on API gateways and rate limiting, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I expected rate limiting to be a simple hard cap, and the two algorithms to be variations of the same thing. I wanted every on-screen outcome to come from code, so a small script reproduces each scenario.

- **Where it resisted, and what I did next:**
  The token bucket turned out to work almost the opposite of how I'd described it: it allows bursts rather than smoothing them away, so that point was sharpened. Fitting the video to exactly 60 seconds took heavy trimming across nearly every beat, and the 9:16 master had to be built in a later pass.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes and the rate-limit script, checked the claims against the RFCs and docs, and fixed the layout issues. I accepted the corrected token-bucket explanation and the note that real AI APIs count tokens as well as requests.

- **What I understand now, and what I still do not:**
  I understand how a gateway centralises protection and how the limiting algorithms differ under bursts. I haven't tested a limiter against real traffic yet.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
