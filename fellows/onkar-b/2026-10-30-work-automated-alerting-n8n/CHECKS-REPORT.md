# Explainer — Automated Alerting & n8n Workflow Integration

**Week:** 26 Oct – 01 Nov 2026
**Type:** Work update

- **Drive:** https://drive.google.com/drive/folders/1AmFC-mFOkf5jKHY0Cftu8l9-F4sfe72d

## What it covers
Deploying an n8n automation container alongside the Gatekeeper API using Docker Compose. It demonstrates how to decouple incident reporting from the core microservice logic by exporting hallucination data via JSON Webhooks into a visual routing pipeline.

## Why this topic, this week
Storing error logs is useless if no one looks at them. Now that our API is fully secured with JWT (Week 8), we needed to establish an outbound communication channel. By using n8n, we avoid hardcoding Slack or SendGrid APIs directly into our Python code. The Gatekeeper simply fires a standard HTTP payload, and n8n handles the complex third-party routing.

## Limits
- Source files for the video: see the Drive folder.