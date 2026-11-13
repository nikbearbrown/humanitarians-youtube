# PROMPTS - How API Gateways Manage Millions of API Requests

## Project

Creator: Akshay Chavan
Channel: @HumanitariansAI
Format: Brutalist technical explainer
Topic: API Gateways
Landscape master: 3840x2160
Frame rate: 24 fps
Narration engine: Kokoro
Voice: am_onyx

## Creative direction

Create a clear, high-contrast system-design explainer showing how an API Gateway orchestrates traffic, security, rate limiting, and caching for distributed microservices.

Use clean geometric components: CLIENTS, API GATEWAY, MICROSERVICES, TOKEN BUCKET, and EDGE CACHE.

Maintain a dark Brutalist visual style with large typography, simple geometric boxes, strong contrast, and restrained accent colors.

Keep title, primary architecture diagram, annotations, and caption areas visually separated.

Use fixed component positions whenever possible so the viewer can follow the architectural progression between beats.

Do not allow arrows to pass through boxes, labels, titles, captions, or other arrows.

Do not place labels directly on traffic paths.

Keep all text well inside safe margins.

Keep diagrams readable at YouTube viewing sizes.

## Beat plan

B00 - Show chaotic direct connections between multiple clients and microservices without a gateway.
B01 - Introduce the API Gateway as a single centralized entry point between clients and services.
B02 - Demonstrate request routing based on path rules (/users, /orders, /payments).
B03 - Show centralized authentication: edge JWT token validation and blocking unauthorized requests.
B04 - Illustrate token-bucket rate limiting buffering normal traffic and throttling traffic spikes.
B05 - Demonstrate load balancing across service instances and routing around an unhealthy node.
B06 - Show response caching serving frequent read requests directly from the gateway cache.
B07 - Summarize the core architectural pillars: SMART ROUTING, EDGE SECURITY, RATE LIMITING, RESPONSE CACHING.
B08 - Branded Humanitarians AI closing card.

## Production constraints

- Landscape source resolution: 3840x2160.
- Frame rate: 24 fps.
- Use native Manim graphics for B00-B07.
- Use ClaudeTitleOutro for B08.
- Preserve protected title and caption zones.
- Keep the primary architecture in the central region.
- Use generous horizontal and vertical spacing.
- Arrows terminate at object boundaries.
- Never draw arrows through text or boxes.
- Avoid crossing arrows.
- Avoid cropped text and edge collisions.
- Use conservative font sizes for long labels.
- Use final-frame holds when narration is longer than the animated portion.
- Narration timing is the authoritative beat duration.
- B08 is the branded Humanitarians AI outro and must not be omitted.
