# Explainer — Webhooks & Event-Driven Architecture

**Week:** 26 Oct – 01 Nov 2026
**Type:** STEM AI Explainer

- **Drive:** https://drive.google.com/drive/folders/1mMqoPqB6U4hFxY_35LUWXKX1L5Z6axCB

## What it covers
The fundamental differences between Polling (pull) and Webhooks (push). It explains why Event-Driven Architecture is strictly necessary for AI systems with long, asynchronous processing times, and breaks down how a webhook payload allows decoupled systems to communicate efficiently.

## Why this topic, this week
After integrating n8n into the Gatekeeper project, this video explains the underlying theory behind that integration. Instead of writing a separate monitoring script that constantly checks the Gatekeeper's SQLite database for new errors (polling), we built the Gatekeeper to automatically push the errors out the exact second they happen (webhooks).

## Limits
- Source files for the video: see the Drive folder.