# SCRIPT — Docker and Kubernetes for AI

Narration as generated. **AI voice** (Kokoro `am_onyx`), not a recording of Likhith.

**B00 · ASK** — Hi, I am Likhith, and this video is about Docker and Kubernetes for AI workloads.

**B01 · BLUF** — Here's the idea. Deploying AI isn't just copying code to a server. Docker packs the model with everything it needs, and Kubernetes runs and scales it for you.

**B02 · HOOK** — Your model works on your laptop. In production, it crashes. Why?

**B03 · PROBLEM** — Machines differ: library versions, operating system, GPU drivers. One mismatch breaks it.

**B04 · MECHANISM** — Docker packs the model, its code, and every dependency into one image that runs anywhere.

**B05 · LIMIT** — One container can't handle a crowd: spikes, crashes, piling load.

**B06 · MECHANISM** — Kubernetes orchestrates many containers across many machines.

**B07 · WORKED EXAMPLE** — Demand rises? It adds copies. One fails? It's replaced. And traffic gets spread.

**B08 · SYNTHESIS** — Docker makes it portable. Kubernetes makes it scalable and resilient.

**B09 · VERDICT** — That's how AI serves thousands of users without hand-managed servers. For one small model, it's often overkill.

**B10 · YOUR_TURN** — Your turn. Ask Claude: write a Dockerfile and a Kubernetes deployment for my model, and explain every line.

**B11 · OUTRO** — Docker and Kubernetes for AI. At Humanitarians AI.
