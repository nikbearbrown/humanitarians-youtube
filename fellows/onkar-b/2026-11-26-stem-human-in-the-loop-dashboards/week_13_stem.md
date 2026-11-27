# Week 13: Human-in-the-Loop & AI Governance Dashboards

**Series:** STEM AI Explainer
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. An autonomous car drives smoothly down a highway—with no steering wheel, no brake pedal, and no windshield for the passenger to see out of.
**ON SCREEN:** `THE BLACK BOX PROBLEM`
**VO:**
Hi, I am Onkar Bhujbal. You would never ride in a self-driving car that had no windshield and no emergency brake. Yet companies deploy autonomous AI agents into finance, healthcare, and legal workflows every day with zero visibility into what those models are actually saying. Today, we are exploring Human-in-the-Loop architecture and why AI Governance Dashboards are the steering wheel of production AI.

### SCENE 2 — AUTOMATION VS. OVERSIGHT
**VISUAL** — A split diagram. Left: `Fully Autonomous` (AI outputs go straight to the customer, including a red hallucination). Right: `Human-in-the-Loop` (a Gatekeeper intercepts the red claim and routes it to a dashboard for human review).
**VO:**
Pure automation is great for speed, but terrible for accountability. In high-stakes domains, you cannot rely on an AI to grade its own homework forever. Human-in-the-Loop, or HITL, design pairs automated guardrails with human judgment. The machine handles 99% of routine traffic at millisecond speed, and escalates the dangerous 1% to a human reviewer.

### SCENE 3 — ANATOMY OF AN AI CONTROL PLANE
**VISUAL** — A wireframe dashboard lights up in three zones: `System Health`, `Diff Comparison (Claim vs. Truth)`, and `Audit Trail`.
**VO:**
A good AI governance dashboard is not just pretty charts—it is a decision engine. To make a reviewer effective, the interface must show three things: live system health, a side-by-side comparison of what the AI claimed versus the verified source of truth, and a filterable audit trail for compliance.

### SCENE 4 — CLOSING THE FEEDBACK LOOP
**VISUAL** — A reviewer clicks "Confirm Hallucination" on the dashboard. A glowing arrow flows backward from the UI into the Vector Database and CI test suite, strengthening the system.
**VO:**
The real magic happens when the dashboard feeds back into engineering. Every blocked payload that a human inspects becomes a permanent regression test case. Over time, your monitoring portal doesn't just catch mistakes—it systematically trains your guardrails to become smarter.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Keep a human in the loop.`
**VO:**
Automate the scale. Keep humans in charge of the truth.
Liam, for Onkar Bhujbal and Humanitarians AI.