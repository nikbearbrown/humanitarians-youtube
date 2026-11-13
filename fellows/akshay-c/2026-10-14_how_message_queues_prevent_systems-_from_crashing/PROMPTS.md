# PROMPTS — How Message Queues Prevent Systems From Crashing

## Project

Creator: Akshay Chavan
Channel: @HumanitariansAI
Format: Brutalist technical explainer
Topic: Message queues
Landscape master: 3840x2160
Frame rate: 24 fps
Narration engine: Kokoro
Voice: am_onyx

## Creative direction

Create a concise system-design explainer showing how message queues buffer asynchronous work and protect downstream consumers during traffic spikes.

Use simple producer, queue, message, and consumer diagrams.

Maintain a dark Brutalist visual style with large typography, simple geometric components, strong contrast, and restrained accent colors.

Keep title, primary diagram, annotations, and caption areas visually separated.

Use fixed component positions whenever possible so the viewer can follow the architecture between beats.

Do not allow arrows to pass through boxes, labels, titles, captions, or other arrows.

Do not place labels directly on traffic paths.

Keep all text well inside safe margins.

Keep diagrams readable at YouTube viewing sizes.

## Beat plan

B00 — Show a sudden burst of incoming jobs reaching one service.

B01 — Show work arriving faster than the service can process it and an overload condition developing.

B02 — Introduce a message queue between producer and consumer.

B03 — Show producers publishing messages into the queue.

B04 — Show a consumer pulling queued messages at a controlled rate.

B05 — Show a traffic spike creating a temporary backlog inside the queue rather than overwhelming consumers.

B06 — Scale from one consumer to three consumers processing messages in parallel.

B07 — Summarize the architecture and benefits: BUFFER SPIKES, DECOUPLE SERVICES, STAY RESPONSIVE.

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
- B07 must render before B08 is compiled.
- B08 is the branded Humanitarians AI outro and must not be omitted.
