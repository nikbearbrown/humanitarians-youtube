# PROMPTS - How Circuit Breakers Prevent Cascading Failures in Distributed Systems

## Project

Creator: Akshay Chavan
Channel: @HumanitariansAI
Format: Brutalist technical explainer
Topic: Circuit Breaker Pattern & Distributed Systems Resilience
Landscape master: 3840x2160
Portrait master: 2160x3840
Frame rate: 24 fps
Narration engine: Kokoro
Voice: am_onyx

## Creative direction

Create a high-contrast system-design explainer illustrating how the Circuit Breaker pattern isolates failing microservices, stops cascading timeouts, and self-heals in high-throughput distributed systems.

Use clean geometric components: CLIENT, CALLING SERVICE, CIRCUIT BREAKER SWITCH, DOWNSTREAM SERVICE, TIMEOUT BLOCKS, ROLLING METRIC WINDOW, and STATE BADGES.

Maintain a dark Brutalist visual style with large typography, simple geometric boxes, strong contrast, and restrained accent colors.

Keep title, primary architecture diagram, annotations, and caption areas visually separated.

Use fixed component positions whenever possible so the viewer can follow the architectural progression between beats.

Do not allow arrows to pass through boxes, labels, titles, captions, or other arrows.

Keep all text well inside safe margins.

Keep diagrams readable at YouTube viewing sizes.

## Beat plan

B00 - Cascading failure collapse: Downstream service slows down; thread pool exhaust upstream, triggering cluster-wide failure.
B01 - Circuit breaker concept: Intercepting client calls with an automated resilience proxy.
B02 - Closed state: Normal operation; traffic flows freely while tracking metrics in a rolling window.
B03 - Failure threshold trip: Error rate crosses the threshold; breaker trips open, severing network calls.
B04 - Open state: Fail fast at 0ms; return fallback defaults and shield downstream service from overload.
B05 - Half-Open state: Sleep timer elapses; canary probe requests test downstream service health.
B06 - Self-healing or retrip: Successful probes reset to Closed; failures retrip to Open.
B07 - Resilience architecture payoff: Circuit breakers, bulkheads, timeouts, and fallback caches.
B08 - Branded Humanitarians AI closing card.

## Production constraints

- Landscape source resolution: 3840x2160.
- Portrait source resolution: 2160x3840.
- Frame rate: 24 fps.
- Use native Manim graphics for B00-B07.
- Use ClaudeTitleOutro / ClaudeTitleOutro916 for B08.
- Preserve protected title and caption zones.
- Keep the primary architecture in the central region.
- Container strokes: #5D584F (luminance < 130).
- Minimum font size: >= 26pt (ensuring >= 41px physical height).
- B08 is the branded Humanitarians AI outro and must not be omitted.
