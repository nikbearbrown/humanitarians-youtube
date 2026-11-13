# Frictional log — Dashboard & Stress Tests

## 2026-10-02 — the project update, in two aspect ratios

**What I was working on.** A project update explainer on exposing the Provenance Gatekeeper ledger via a dashboard and pushing the pipeline to its breaking point with adversarial payloads.

**What I tried, and what I expected.** 
- I attempted to run the stress test against the `/verify` endpoint while heavy machine learning inference (`SentenceTransformers`) was running asynchronously.
- I expected FastAPI to handle the traffic seamlessly and return `500` errors for bad payloads.

**Where it resisted, and what I did next.** 
- The local Uvicorn server suffered a silent, fatal C++ memory crash (`RemoteDisconnected`) the moment it tried to process the text embeddings. The heavy ML inference blocked the main async event loop.
- Additionally, port 8000 was locked in a conflict with a background Docker container.
- I tore down the Docker instance and refactored the `/verify` route to be entirely synchronous (removing `async def`), forcing FastAPI to offload the heavy model inference to a safe background threadpool.

**What Claude contributed, and what I did with it.** 
- Mine: The dashboard UI, the SQLite queries, and the initial adversarial test scripts.
- Claude's: Diagnosing the silent `Connection aborted` crash as a thread exhaustion issue rather than a logic error, and identifying the Uvicorn auto-reload bug. I accepted the synchronous refactor.

**What I understand now, and what I still do not.**
- Understood: In FastAPI, defining a route as `async def` is dangerous if the route contains heavy CPU-bound tasks (like loading an LLM or ML model). It blocks the event loop and crashes the server.