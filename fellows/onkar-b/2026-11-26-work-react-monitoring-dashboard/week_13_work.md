# Week 13: Building the React Monitoring Dashboard

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A terminal scrolls raw JSON logs and Prometheus metrics text. A financial compliance officer squints at the screen, confused.
**VO:**
Hi, I am Onkar Bhujbal. Over the last twelve weeks, we built an enterprise-grade AI backend—complete with ChromaDB vector search, JWT security, n8n alerts, Redis caching, and Prometheus telemetry. There is just one problem: normal human stakeholders do not read terminal logs or raw PromQL graphs. This week, we kick off Phase 3 of our roadmap by constructing the React monitoring dashboard for our Provenance Gatekeeper.

### SCENE 2 — SCAFFOLDING WITH VITE
**VISUAL** — Terminal runs `npm create vite@latest dashboard -- --template react`. The project tree cleanly unfolds: `App.jsx`, `App.css`, and `data/mockTelemetry.js`.
**VO:**
Instead of bolting HTML templates onto our FastAPI backend, we scaffolded a decoupled frontend application using React and Vite. Keeping the frontend completely independent from our Python microservice means we can scale, style, and deploy the UI without ever touching our core AI inference engine.

### SCENE 3 — COMPONENT ARCHITECTURE & KPIs
**VISUAL** — The dark-mode dashboard loads at `localhost:5173`. The camera pans across the four KPI cards: Claims Evaluated, Hallucinations Blocked, Redis Cache Hit Rate, and Average Latency.
**VO:**
We designed the dashboard around three operational layers. At the top, real-time KPI cards surface our Redis cache efficiency and total blocked hallucinations at a glance. Right beneath that sits a live infrastructure strip tracking the health of all five containers—FastAPI, Redis, ChromaDB, Prometheus, and n8n.

### SCENE 4 — THE INTERCEPTED PAYLOAD LEDGER
**VISUAL** — Cursor clicks the filter buttons (`Magnitude Error`, `Polarity Error`, `Unverified Entity`). The table rows smoothly filter, showing the AI's false claim side-by-side with the ChromaDB ground truth.
**VO:**
The centerpiece is the Intercepted Hallucination Ledger. Compliance teams can filter blocked payloads by variance type and immediately compare the AI's fabricated claim side-by-side against our verified ChromaDB ground truth. Right now it runs on a strict mock telemetry contract, preparing the exact state structure we will bind to live JWT-authenticated API endpoints next week.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Design for the human reviewer.`
**VO:**
Great backend architecture means nothing if your team cannot see what it is protecting. Design your UI for the human reviewer.
Liam, for Onkar Bhujbal and Humanitarians AI.