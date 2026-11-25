# Week 12: Observability, Telemetry & Time-Series Metrics

**Series:** STEM AI Explainer
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A commercial airplane cockpit where every single dial, altimeter, and fuel gauge is covered in black duct tape.
**ON SCREEN:** `FLYING BLIND`
**VO:**
Hi, I am Onkar Bhujbal. Imagine flying a commercial jet with no altimeter, no speed gauge, and no fuel indicator—just a text log that prints "Engine Failed" after you have already crashed. That is what running an AI microservice without Observability looks like. Today, we are breaking down Telemetry, Time-Series Metrics, and how engineers keep production AI systems visible.

### SCENE 2 — THE THREE PILLARS
**VISUAL** — Three distinct vertical pillars rise on screen: `LOGS`, `METRICS`, and `TRACES`.
**VO:**
In modern software engineering, Observability rests on three pillars: Logs, Metrics, and Traces. Logs tell you *what* happened at a specific moment—like a single error message. Traces follow a single request as it hops across multiple microservices. Metrics, however, are numerical measurements collected over time—like CPU usage, response latency, or errors per second.

### SCENE 3 — TIME-SERIES DATABASES
**VISUAL** — A stream of timestamped data points `(t1: 12ms, t2: 14ms, t3: 450ms)` flows into a sleek cylindrical database, immediately plotting a sharp spike on a line graph.
**VO:**
Standard SQL databases are terrible at storing millions of rapid-fire measurements. That is why telemetry tools like Prometheus use Time-Series Databases. Every data point is strictly paired with a timestamp and a label. Instead of asking "What happened to User 42?", a time-series database lets you ask, "Did our average AI response time spike by 300% over the last ten minutes?"

### SCENE 4 — AI TELEMETRY & MODEL DRIFT
**VISUAL** — A line graph labeled `Hallucination Intercept Rate`. For weeks it stays flat near 2%. Suddenly, after a model update, it climbs steadily to 18%, triggering a warning highlight.
**VO:**
For AI systems, metrics are your early warning system against silent failure. An AI model rarely crashes with a 500 error; instead, it quietly degrades, drifts, or starts hallucinating more often. By tracking domain-specific telemetry—like cache hit ratios and hallucination rates—you catch silent degradation before your users ever notice.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Instrument your blind spots.`
**VO:**
Logs tell you why you crashed. Metrics keep you in the air. Instrument your blind spots.
Liam, for Onkar Bhujbal and Humanitarians AI.