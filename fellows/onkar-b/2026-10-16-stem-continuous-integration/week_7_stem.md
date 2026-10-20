# Week 7: Continuous Integration for AI Systems

**Series:** STEM AI Explainer
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A graph shows an AI model's accuracy slowly degrading over time.
**ON SCREEN:** `THE REGRESSION PROBLEM`
**VO:**
Hi, I am Onkar Bhujbal, and this video is about why AI pipelines silently degrade. When you build traditional software, a function that adds two numbers today will still add them tomorrow. But when you build applications wrapper around Large Language Models, changes in model versions, system prompts, or upstream data can instantly break your downstream architecture. 

### SCENE 2 — DETERMINISTIC VS PROBABILISTIC TESTING
**VISUAL** — Two mono-text boxes snap in.
`01 STATIC CODE` 
`02 DYNAMIC INFERENCE`
**VO:**
Testing AI is fundamentally different from testing standard code. You cannot simply assert that an LLM's output will precisely match a hardcoded string. Instead, you must test the deterministic guardrails that surround the model. Continuous Integration for AI means continuously testing your parsers, your normalizers, and your fail-safes against a suite of known adversarial inputs.

### SCENE 3 — AUTOMATING THE DEFENSE
**VISUAL** — An animated gear mechanism. Code flows through a checkpoint labeled `CI/CD`. Bad code is deflected; good code passes through to `PRODUCTION`.
**VO:**
This is where Continuous Integration pipelines, like GitHub Actions, become mathematically necessary. A CI pipeline is an automated robot that lives in your code repository. Every time an engineer tries to update the system, the CI pipeline builds the application in a vacuum and fires malicious data at it. 

### SCENE 4 — BLOCKING DEPLOYMENT
**VISUAL** — A simulated pull request on GitHub. The "Merge" button is greyed out and locked behind a failing CI status check.
**VO:**
If a developer accidentally removes a security regex, or if a new model update starts bypassing the evaluation logic, the CI pipeline catches the failure in isolation. It physically locks the repository and prevents the compromised code from reaching production. It transforms hope into mathematical certainty.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Automate your regression tests.`
**VO:**
Never assume your AI guardrails will survive the next commit. Build an automated integration pipeline that aggressively attacks your system on every update.
Liam, for Onkar Bhujbal and Humanitarians AI.