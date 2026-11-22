# Frictional log — Telemetry & Prometheus

## 2026-11-19 — the project update, in two aspect ratios

**What I was working on.** Exposing a `/metrics` endpoint on the FastAPI Gatekeeper and configuring a Prometheus container to scrape it.

**What I tried, and what I expected.**
- I added Prometheus to `docker-compose.yml`, updated `requirements.txt`, and ran `docker compose up -d --build`, expecting a quick rebuild and live metrics at `localhost:9090`.

**Where it resisted, and what I did next.**
- **The Scrape Target Trap:** Just like the n8n webhook in Week 9, pointing Prometheus to `localhost:8000` failed because `localhost` inside the Prometheus container refers to Prometheus itself. I updated the target in `prometheus.yml` to Docker's internal service name (`gatekeeper:8000`).
- **Missing Business Context:** The default FastAPI instrumentator only tracked generic HTTP status codes (`200 OK`, `500 Error`) and latency. I added custom `Counter` metrics using `prometheus_client` with explicit labels (`verdict`, `variance_type`, `status`) to capture domain-specific AI telemetry.
- **The 1GB+ GPU PyTorch Rebuild Crash:** Rebuilding the Docker image after updating `requirements.txt` pulled full CUDA/NVIDIA binaries (`triton`, `nvidia-cudnn`), which stalled mid-download and failed `pip`'s SHA256 hash check. Switching the `Dockerfile` to install CPU-only `torch` then hit a secondary snag: the base `python:3.10-slim` image shipped with `pip 23.0.1`, which rejected `typing_extensions` wheel metadata and failed looking for `flit_core`. Adding `RUN pip install --upgrade pip` right before the CPU-only PyTorch install resolved both issues and cut build times dramatically.

**What Claude contributed, and what I did with it.**
- Mine: The decision to track Redis cache hit/miss ratios alongside hallucination verdicts.
- Claude's: The `prometheus-fastapi-instrumentator` wiring, the labeled `Counter` pattern, and diagnosing the CPU-only PyTorch + `pip` upgrade fix for the `Dockerfile`.

**What I understand now, and what I still do not.**
- Understood: Standard HTTP metrics tell you if your server is alive, but custom labeled counters tell you if your AI pipeline is actually doing its job. Also, always pin CPU-only PyTorch and upgrade `pip` in slim Docker images to avoid multi-gigabyte CUDA downloads and wheel metadata bugs.