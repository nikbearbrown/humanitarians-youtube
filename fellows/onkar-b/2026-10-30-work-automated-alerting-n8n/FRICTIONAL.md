# Frictional log — Automated Alerting & n8n

## 2026-10-30 — the project update, in two aspect ratios

**What I was working on.** Integrating a local instance of n8n via Docker Compose to catch webhook alerts from the Gatekeeper.

**What I tried, and what I expected.** 
- I set up `docker-compose.yml` to run both services. I configured the Python Gatekeeper to send POST requests to the n8n webhook URL and expected the payloads to appear in the n8n Executions tab.

**Where it resisted, and what I did next.** 
- **The Internal Network Trap:** The Gatekeeper initially crashed with a `Connection Refused` on localhost. Inside a Docker network, `localhost` refers to the container itself. I had to route the webhook to Docker's internal DNS (`http://n8n:5678/webhook/hallucination-alert`).
- **The Phantom Payload:** My terminal reported `✅ Webhook triggered!`, but nothing arrived in n8n. I realized my Python code was only *printing* a fake success message to the console; I had forgotten to write the actual `requests.post()` logic.
- **The OOM Crash:** After fixing the code, the first test worked, but subsequent tests threw a fatal `RemoteDisconnected` error. Running a PyTorch `SentenceTransformer`, a `ChromaDB` vector store, and a Node.js `n8n` engine concurrently maxed out my Docker Desktop RAM, causing Linux to OOM-kill (Out of Memory) the FastAPI container. I fixed this by increasing my Docker memory limit to 8GB.

**What Claude contributed, and what I did with it.** 
- Mine: The Dockerfile architecture and the `test_n8n_alert.py` adversarial script.
- Claude's: The merged `docker-compose.yml`, spotting the missing `requests.post` call, and diagnosing the `RemoteDisconnected` crash as a Docker memory limit issue.

**What I understand now, and what I still do not.**
- Understood: Running an AI stack locally requires massive, explicit memory provisioning. Standard web apps can run on 1GB of Docker RAM; local ML pipelines combined with automation engines will instantly crash without 6GB+.