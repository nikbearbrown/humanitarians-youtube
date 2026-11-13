# Week 9: Automated Alerting & n8n Workflow Integration

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A terminal shows a "Magnitude Error" hallucination being blocked. But then, the screen zooms out, showing the blocked error just sitting there in a database, unseen by human eyes.
**VO:**
Hi, I am Onkar Bhujbal. Our Provenance Gatekeeper is doing its job—intercepting AI hallucinations and blocking them from production. But logging an error in a local SQLite database isn't enough. If a critical financial discrepancy occurs, the engineering team needs to know instantly. This week, we are connecting our microservice to the real world by integrating an automated n8n incident response pipeline.

### SCENE 2 — DOCKER ORCHESTRATION
**VISUAL** — A `docker-compose.yml` file sliding into view. The `gatekeeper` and `n8n` services link together via a glowing internal network line.
**VO:**
To ensure our local environment mirrors our eventual cloud deployment, we orchestrated both the FastAPI Gatekeeper and the n8n automation engine using Docker Compose. By running them on the same internal Docker network, the Gatekeeper can securely fire webhooks to n8n without exposing the automation platform to the public internet.

### SCENE 3 — THE WORKFLOW CANVAS
**VISUAL** — The n8n canvas. A payload drops into the Webhook node, flows through an IF condition (Severity Router), and lands in a Slack/Email formatting node.
**VO:**
Instead of hardcoding Slack or email APIs directly into our Python script—which creates technical debt—we export the incident payload to n8n. In the n8n visual canvas, we designed a workflow that catches the webhook, reads the JSON body, and routes it based on severity. A "Magnitude Error" gets instantly formatted into a high-priority alert.

### SCENE 4 — FIRING THE ADVERSARIAL PAYLOAD
**VISUAL** — The terminal running `test_n8n_alert.py`. It authenticates, fires a bad $4.5M claim, and gets rejected. Quick cut to the n8n "Executions" tab, showing the green "Success" checkmark matching the exact timestamp.
**VO:**
To test the integration, we fired our automated adversarial payload into the secure endpoint. The Gatekeeper rejected the false claim, generated the error explanation, and instantly fired the webhook. Seconds later, the payload successfully arrived in the n8n execution log, proving our autonomous incident reporting works flawlessly.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Decouple your alert logic.`
**VO:**
Don't clutter your microservices with third-party messaging APIs. Decouple your alert logic using webhooks and visual automation. 
Liam, for Onkar Bhujbal and Humanitarians AI.