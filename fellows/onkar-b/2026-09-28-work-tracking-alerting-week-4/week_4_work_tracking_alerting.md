# Week 4: Tracking & Alerting — Video Script

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A terminal snaps in with ephemeral text rapidly scrolling and disappearing.
`VERDICT: FAIL` [fades out]
**ON SCREEN:** `SILENT FAILURES`
**VO:**
I am Onkar Bhujbal, a software engineer. Intercepting an AI hallucination is useless if the system forgets it happened a millisecond later. An orchestrator without a memory is just a black box. This week, we finalized the Provenance Gatekeeper by building a persistent tracking database and an automated alerting system to make AI failures loud and permanent.

### SCENE 2 — THE FRAMEWORK
**VISUAL** — Two mono-text boxes snap in.
`01 THE AUDIT TRAIL` (SQLite)
`02 THE ALARM` (Webhook)
**VO:**
The final architecture operates on two principles: the audit trail and the alarm. First, every claim evaluated by the Gatekeeper is written to a local SQLite database, creating an immutable ledger of the AI's accuracy over time. Second, if the Gatekeeper detects a magnitude or directional error, it immediately fires an outbound webhook to notify human operators.

### SCENE 3 — WORKED EXAMPLE
**VISUAL** — Split frame. 
**TOP:** A SQL query executing: `SELECT * FROM evaluation_logs`
**BOTTOM:** A mock Slack alert snapping in: `🚨 Directional Error Intercepted.`
**VO:**
Here is the pipeline in action. When our evaluation layer flags a false claim, a new row is instantly committed to the SQLite tracking log detailing the exact variance. Simultaneously, the backend pushes a critical alert payload to our messaging platform via webhook, exposing the hallucination before it can propagate.

### SCENE 4 — FALSIFIABILITY 
**VISUAL** — The SQL table returns.
**ON SCREEN:** `ACCOUNTABILITY OVER TIME`
**VO:**
Why not just rely on ephemeral workflow logs? Because workflow logs are difficult to query for analytics. By maintaining a dedicated relational database, we can mathematically prove how often the underlying language model lies, what type of errors it favors, and whether its reliability degrades over time. 

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to a terminal command block.
`sqlite3 gatekeeper_logs.db "SELECT generated_claim FROM logs;"`
**VO:**
Audit the system. Run this SQLite command in your terminal to view the permanent record of every claim the AI attempted to pass through the Gatekeeper. You cannot fix a model you do not track.
Liam, for Onkar Bhujbal and Humanitarians AI.