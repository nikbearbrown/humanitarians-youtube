# Explainer — Stateless Authentication (JWT)

**Week:** 19 Oct – 25 Oct 2026
**Type:** STEM AI Explainer

- **Drive:** https://drive.google.com/drive/folders/1rWSQTUBMjUD6oNaLff2po-jhp2fm3djN

## What it covers
The architectural difference between stateful session management and stateless JSON Web Tokens (JWT). It breaks down the three components of a JWT (Header, Payload, Signature) and explains why cryptographic verification is superior for scaling distributed microservices.

## Why this topic, this week
Implementing OAuth2 in the Gatekeeper project provided the perfect technical backdrop to explain *why* we chose tokens over traditional login sessions. When building AI systems that will eventually rely on automated agents hitting endpoints thousands of times a minute, stateless authentication is a mandatory architectural pattern.

## Limits
- Source files for the video: see the Drive folder.