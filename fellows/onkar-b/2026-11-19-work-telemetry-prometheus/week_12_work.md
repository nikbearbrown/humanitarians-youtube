# Week 12: Real-Time Telemetry & Metrics with Prometheus

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. The Gatekeeper is running fast with Redis, handling dozens of requests. Suddenly, the screen goes pitch black except for a single blinking cursor.
**VO:**
Hi, I am Onkar Bhujbal. Last week, we added Redis to make our Provenance Gatekeeper blazingly fast. The problem? Right now, we are flying blind. We know the cache works when we stare at terminal logs, but in production, nobody is reading raw console text. If our hallucination rate spikes at 3 AM, or our Redis cache stops hitting, we need hard numbers. This week, we are closing out Phase 2 by integrating Prometheus for real-time telemetry and metrics.

### SCENE 2 — EXPOSING THE METRICS ENDPOINT
**VISUAL** — `app/main.py` appears on screen, highlighting `Instrumentator().instrument(app).expose(app)` and the custom `Counter` definitions for `CLAIMS_EVALUATED` and `CACHE_EVENTS`.
**VO:**
To give our microservice a pulse, we wired the Prometheus FastAPI Instrumentator directly into our application. With just a few lines of code, our API automatically exposes a `/metrics` endpoint that tracks HTTP request counts and response latency. On top of that, we built custom business-logic counters to track every single cache hit, cache miss, and blocked hallucination by variance type.

### SCENE 3 — THE SCRAPE ARCHITECTURE
**VISUAL** — A `prometheus.yml` file slides in next to `docker-compose.yml`. A glowing pulse travels from the Prometheus container (port 9090) to the Gatekeeper container (port 8000) every 5 seconds.
**VO:**
Unlike webhooks, which push data out, Prometheus operates on a pull model. We spun up a Prometheus container in Docker Compose and configured it with a `prometheus.yml` file. Every five seconds, Prometheus reaches across our internal Docker network, scrapes the `/metrics` endpoint, and stores those snapshots in a time-series database.

### SCENE 4 — QUERYING LIVE TELEMETRY
**VISUAL** — The Prometheus Web UI at `localhost:9090`. A PromQL query (`gatekeeper_claims_evaluated_total`) runs, rendering a clean line graph showing `Magnitude Error` intercepts alongside `hit` vs `miss` cache metrics.
**VO:**
Now, instead of digging through SQLite tables or Docker logs, we can open the Prometheus dashboard at port 9090 and query our system's health in real time. We can see the exact ratio of Redis cache hits to misses, monitor our API latency down to the millisecond, and track hallucination trends as they happen.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Measure everything that matters.`
**VO:**
You cannot optimize what you cannot measure. Expose your metrics and stop flying blind.
Liam, for Onkar Bhujbal and Humanitarians AI.