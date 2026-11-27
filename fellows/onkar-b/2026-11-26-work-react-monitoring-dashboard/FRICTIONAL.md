# Frictional log — React Monitoring Dashboard

## 2026-11-26 — the project update, in two aspect ratios

**What I was working on.** Building the foundational React monitoring portal for the Provenance Gatekeeper using Vite.

**What I tried, and what I expected.**
- I initially considered wiring live `fetch()` calls straight to FastAPI and Prometheus in the same sprint as building the UI layout.

**Where it resisted, and what I did next.**
- Mixing UI layout design with CORS configuration, JWT token persistence, and backend endpoint changes created too many moving parts at once—debugging a blank table became guesswork between CSS/state bugs and 401 auth rejections.
- I decoupled the work into a strict frontend-first contract (`mockTelemetry.js`) matching our backend JSON schema. This let me validate filtering, responsive layout, and side-by-side ground-truth legibility immediately before tackling JWT binding in Week 14.

**What Claude contributed, and what I did with it.**
- Mine: The three-layer dashboard layout (KPI strip, five-service infrastructure health panel, and filterable hallucination ledger).
- Claude's: Structuring `mockTelemetry.js` to mirror the FastAPI + Prometheus schema and keeping CSS dependency-free for fast Vite iteration.

**What I understand now, and what I still do not.**
- Understood: Designing against a fixed mock data contract lets you ship and verify a clean frontend architecture without getting blocked by backend auth or CORS friction.