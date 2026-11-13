# PROMPTS — How Caching Makes Applications Faster

## Project

Creator: Akshay Chavan
Channel: @HumanitariansAI
Format: Brutalist technical explainer
Topic: Application caching
Landscape master: 3840x2160
Frame rate: 24 fps
Narration engine: Kokoro
Voice: am_onyx

## Creative direction

Create a concise system-design explainer showing why applications use caching.

Use simple application, cache, database, request, cache-hit, cache-miss, storage, and TTL diagrams.

Maintain a dark Brutalist visual style with large typography, simple geometric components, strong contrast, and restrained accent colors.

Keep the title, diagram, and caption areas visually separated.

Do not allow arrows to pass through boxes, labels, titles, or captions.

Keep diagrams readable at YouTube viewing sizes.

## Beat plan

B00 — Show repeated requests traveling through an application to a database.

B01 — Show repeated queries increasing database workload.

B02 — Introduce a cache between the application and database.

B03 — Demonstrate a cache miss and fallback to the database.

B04 — Show the returned database result being stored in the cache.

B05 — Demonstrate a cache hit that avoids another database query.

B06 — Explain TTL by visually counting a cached entry toward expiration.

B07 — Summarize the payoff: faster responses and less database load.

## Production constraints

- Landscape source resolution: 3840x2160.
- Frame rate: 24 fps.
- Use native Manim graphics.
- Preserve protected title and caption zones.
- Avoid overlapping arrows, boxes, and text.
- Use final-frame holds when narration is longer than the animated portion.
- Narration timing is the authoritative beat duration.
