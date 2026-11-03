# Explainer — API Security & JWT Authentication

**Week:** 19 Oct – 25 Oct 2026
**Type:** Work update

- **Drive:** https://drive.google.com/drive/folders/1U0tE86P57oXZZHeI3vV-kwXADD_wLMdH

## What it covers
Securing the Provenance Gatekeeper microservice using OAuth2 and JSON Web Tokens (JWT). It details the transition from `passlib` to raw `bcrypt` for password hashing to maintain compatibility with Python 3.13, and showcases the updated adversarial stress test negotiating a Bearer token.

## Why this topic, this week
As the microservice matures, it cannot remain an open endpoint. Without authentication, a malicious actor or a runaway internal script could easily spam the `/verify` route, filling the SQLite logs with garbage data and triggering endless false-positive webhooks. Locking it down ensures only authorized AI agents (like our upcoming n8n workflow) can request ledger verification.

## Limits
- Source files for the video: see the Drive folder.