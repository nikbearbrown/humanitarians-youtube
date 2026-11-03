# SHOTLIST — How Message Queues Prevent Systems From Crashing

| Beat | Shot | Visual |
|---|---|---|
| B00 | Traffic burst | Several incoming JOB markers approach one SERVICE without overlapping. |
| B01 | Service overload | Jobs accumulate in a dedicated backlog area while SERVICE shows OVERLOADED. |
| B02 | Introduce queue | PRODUCER → MESSAGE QUEUE → CONSUMER with wide horizontal separation. |
| B03 | Publish messages | PRODUCER sends three messages into MESSAGE QUEUE using one clean traffic lane. |
| B04 | Controlled consumption | MESSAGE QUEUE → CONSUMER; messages leave sequentially rather than simultaneously. |
| B05 | Absorb spike | Queue visibly contains a backlog while the consumer receives a controlled flow. |
| B06 | Scale consumers | MESSAGE QUEUE feeds three vertically separated consumers using separate non-crossing connectors. |
| B07 | Payoff | Clean PRODUCER → MESSAGE QUEUE → CONSUMERS architecture with three separated benefit labels. |
| B08 | Outro | ClaudeTitleOutro with @HumanitariansAI and Akshay Chavan attribution. |

## Visual safety

- Keep titles in the upper safe zone.
- Keep explanatory captions in the lower safe zone.
- Keep the primary system diagram in the central region.
- Keep long text away from left and right frame boundaries.
- Use fixed producer, queue, and consumer zones.
- Arrows terminate at object boundaries.
- Arrows must not cross labels or boxes.
- Avoid arrow-to-arrow crossings.
- Do not stack labels over connectors.
- Use short box labels.
- Keep benefit labels separated from the architecture.
- Avoid cropped text and edge collisions.
- B06 consumer connectors must use distinct destinations and sufficient vertical spacing.
- B07 must have a complete final-frame hold before transitioning to B08.

## Landscape render

Resolution: 3840x2160
Aspect ratio: 16:9
Frame rate: 24 fps
Source: Manim for B00-B07; Remotion for B08.

## Review status

B00: Pending render review
B01: Pending render review
B02: Pending render review
B03: Pending render review
B04: Pending render review
B05: Pending render review
B06: Pending render review
B07: Pending render review
B08: Pending render review
