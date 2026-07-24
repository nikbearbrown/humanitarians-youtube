# PEDAGOGY — claude-liam-linear-api

## Skill
linear-api (claude-tag-plugins / linear)

## Learning objective
Understand Linear's GraphQL-only model, two ID systems, and the critical difference
between rate limiting (HTTP 400 not 429) and standard error handling (check .errors, not just HTTP status).

## Prior knowledge assumed
Knows what Linear is; has done REST API work; unfamiliar with GraphQL or Linear specifics.

## Key concepts
1. Single GraphQL endpoint — no REST paths exist
2. Two ID systems: UUID (API ops) vs identifier (ENG-123, human-readable)
3. HTTP 200 even on errors — always check .errors before trusting .data
4. Rate limit = HTTP 400 with code RATELIMITED (not 429)
5. UUID required for mutations — identifiers fail with INVALID_INPUT

## VERDICT: PASS

The skill covers GraphQL mechanics correctly. Key gap: rate limit HTTP 400 vs 429
distinction is easy to miss for developers coming from REST APIs.
