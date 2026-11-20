# Frictional log — Observability & Telemetry

## 2026-11-19 — the project update, in two aspect ratios

**What I was working on.** A STEM explainer covering Observability, Telemetry, and Time-Series Databases for AI systems.

**What I tried, and what I expected.**
- I initially drafted the script around PromQL syntax and how Prometheus stores chunks on disk.

**Where it resisted, and what I did next.**
- Diving into PromQL query syntax made the video feel like a dry manual rather than a conceptual STEM explainer.
- I zoomed out to the Three Pillars of Observability and anchored Scene 4 on "silent AI failure"—the idea that unlike traditional software, AI can return a `200 OK` while still being completely wrong.

**What Claude contributed, and what I did with it.**
- Mine: The contrast between SQLite event logs and time-series aggregations.
- Claude's: The duct-taped cockpit hook and framing AI metrics as a defense against silent degradation.

**What I understand now, and what I still do not.**
- Understood: Observability isn't just about catching crashes; in AI engineering, it is about spotting statistical shifts in model behavior over time.