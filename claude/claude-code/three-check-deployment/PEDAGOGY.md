# PEDAGOGY — three-check-deployment

## Concept
Three-check deployment verification — functional, environment, pedagogical — each catching a different category of failure.

## Core question
What does the environment check catch that the functional check misses?

## Answer
Network dependencies the school blocks — CDN fonts, external APIs — that pass on the developer's machine but fail on the school network. The functional check only tests what runs locally; the environment check audits what the tool requires from the network.

## Teaching pattern
- B00: concrete failure — font blocked on school network, thirty students see blank screen
- B01: reframe — three checks, three failure categories
- B02-B03: generate the protocol — functional, environment, pedagogical sections
- B04: run the protocol — CDN failure caught before class
- B05-B06: add fourth check — accessibility catches what the three miss
- B07: fifteen-minute investment prevents forty-minute failure
- B08: forward link to post-build document

## Bloom's level
Applying → Evaluating: students can run the three-check protocol and identify which category each failure belongs to.

## Common misconception addressed
Teachers often test only functional correctness. The video establishes that environment failures are a distinct category — they pass locally and fail in the classroom specifically because the school network is different from the developer's machine.
