# Week 5: Dashboards, Docker Persistence & Stress Tests

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A terminal window snaps in, scrolling endless errors until it is suddenly overlaid by a clean, formatted HTML table showing red and green verdicts.
**ON SCREEN:** `EXPOSE THE LEDGER`
**VO:**
Hi, I am Onkar Bhujbal, and this video is about moving the Provenance Gatekeeper into production. An AI security system is useless if human operators refuse to look at the logs. This week, we pulled the data out of the terminal, fixed a critical architecture crash, and pushed the pipeline to its breaking point.

### SCENE 2 — THE DASHBOARD & PERSISTENCE
**VISUAL** — Two Brutalist text boxes snap in.
`01 VISUAL DASHBOARD` 
`02 DOCKER VOLUMES`
**VO:**
Our production leap required two additions. First, a lightweight FastAPI HTML dashboard that queries our SQLite ledger in real-time. Second, a persistent Docker Compose configuration. By mounting our local database files directly to the container, we ensure our ChromaDB vectors and SQLite evaluation logs survive server restarts.

### SCENE 3 — OVERCOMING THE FATAL CRASH
**VISUAL** — Code block highlights the removal of the `async` keyword from the `/verify` route.
**VO:**
But production isn't just about UI; it is about stability. We encountered a silent, fatal C++ memory crash when our server tried to process heavy machine learning embeddings. By refactoring our FastAPI endpoint to run synchronously, we forced the framework to offload the heavy model inference to a safe background threadpool, stabilizing the entire application.

### SCENE 4 — ADVERSARIAL PAYLOADS
**VISUAL** — Split frame.
**TOP:** The Python `stress_test.py` script firing: `{"claim": "DROP TABLE logs;"}`
**BOTTOM:** The HTML dashboard auto-refreshing, instantly flagging the payload in red: `VERDICT: FAIL`
**VO:**
With the server stable, we fired an adversarial stress test at it. We deliberately bombarded our evaluation endpoint with null values, type mismatches, and SQL injections. The Gatekeeper perfectly intercepted the malformed data, compared it strictly against the ChromaDB ground truth, and safely logged the failures without crashing.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to a terminal command block.
`docker-compose up -d && python tests/stress_test.py`
**VO:**
Deploy the system. Spin up the Gatekeeper using our persistent Docker Compose configuration, navigate to the local dashboard port, and fire the adversarial test script. Watch how quickly the ledger fills with intercepted errors.
Liam, for Onkar Bhujbal and Humanitarians AI.