# Week 10: Continuous Integration & GitHub Actions

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A flashback to last week’s terminal: the fake `✅ Webhook triggered!` message. A red stamp slams over it: `FALSE POSITIVE`.
**VO:**
Hi, I am Onkar Bhujbal. Last week, I pushed an update to our Provenance Gatekeeper that claimed it successfully fired a webhook to our n8n automation server. The problem? I had forgotten to write the actual HTTP request in the Python code. My manual testing failed me. This week, we are stripping away manual human deployment entirely and locking this project down with a GitHub Actions Continuous Integration pipeline.

### SCENE 2 — THE AUTOMATED RUNNER
**VISUAL** — The `.github/workflows/ci.yml` file types itself out on screen. 
**VO:**
To prevent broken code from ever reaching production, we wrote a YAML workflow file and placed it in our repository. Now, every single time I push code to the main branch, GitHub automatically spins up an isolated Ubuntu server in the cloud. It downloads our code, installs Python, and attempts to build our environment from scratch without any human intervention.

### SCENE 3 — PYTEST INTEGRATION
**VISUAL** — Split screen. Left: GitHub Actions terminal showing `pip install pytest`. Right: A fast scroll of `tests/test_api.py`.
**VO:**
But just booting the server isn't enough. We integrated Pytest into the pipeline alongside FastAPI's TestClient. Before GitHub allows the deployment to pass, the cloud runner executes a gauntlet of unit tests. It aggressively tests our JSON Web Token authentication, ensuring that adversarial payloads are rejected and the API endpoints respond correctly.

### SCENE 4 — THE GREEN CHECKMARK
**VISUAL** — A GitHub pull request screen. A yellow dot spins, running the checks. It turns into a bright green checkmark: `All checks have passed.` The "Merge" button glows green.
**VO:**
If a single test fails, or if our Docker container refuses to build because of a dependency conflict, the pipeline turns red and blocks the code from merging. This forces the engineering team to fix the bugs in the staging environment, ensuring that the Provenance Gatekeeper remains bulletproof when handling live AI financial data. 

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Automate your paranoia.`
**VO:**
Never trust your own manual testing. Let the robots test the robots.
Liam, for Onkar Bhujbal and Humanitarians AI.