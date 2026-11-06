# Explainer — CI/CD & GitHub Actions

**Week:** 02 Nov – 08 Nov 2026
**Type:** Work update

- **Drive:** https://drive.google.com/drive/folders/1sjt7kQkPXuTWZVYu2eIQqI36UCaMrZuy

## What it covers
Implementing a GitHub Actions workflow (`ci.yml`) to automatically test and build the FastAPI Gatekeeper. It showcases the use of `pytest` and `TestClient` to programmatically verify endpoint health and authentication security before code can be merged.

## Why this topic, this week
This is the capstone of the Gatekeeper architecture. Week 9 proved that manual testing is inherently flawed (the phantom webhook bug). By wrapping the entire stack (FastAPI, ChromaDB, n8n) in a CI pipeline, we transition the project from a "local prototype" into a production-ready, enterprise-grade microservice that protects itself against future regressions.

## Limits
- Source files for the video: see the Drive folder.