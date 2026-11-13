# SOURCES — API Gateways and Rate Limiting

Brief supplied by the requester (Likhith), 7 points; each checked against the references below (2026-10-21).

- Chris Richardson, "Pattern: API Gateway / Backends for Frontends", microservices.io — https://microservices.io/patterns/apigateway.html (single entry point in front of services; request routing; cross-cutting concerns such as authentication handled at the gateway).
- RFC 6585, "Additional HTTP Status Codes", §4 — https://www.rfc-editor.org/rfc/rfc6585#section-4 (429 Too Many Requests; a response MAY include Retry-After).
- RFC 2697, "A Single Rate Three Color Marker" — https://www.rfc-editor.org/rfc/rfc2697 (token-bucket metering: a bucket of size CBS refilled at a committed rate; traffic within the bucket conforms).
- Cloudflare, "How we built rate limiting capable of scaling to millions of domains" (2017) — https://blog.cloudflare.com/counting-things-a-lot-of-different-things/ (fixed-window boundary problem; sliding-window counting).
- Anthropic, "Rate limits" (Claude API docs) — https://docs.claude.com/en/api/rate-limits (model APIs limit per organization/key in requests per minute and input/output tokens per minute; limits measured with a token bucket).

## Evidence (executed, not typed)
- `evidence/rate_limit_toy.py` → `evidence/rate_limit_toy.out.txt` — pure Python, deterministic, same inputs as the scene defaults in `runtime/remotion/src/ApiGateway.tsx`.
  B05 5 pass / 5 rejected · B06 burst ✓✓✓✓, flood ✓✓✓✓✓✓✕✕✓✕✕ (11 / 4) · B07 fixed 10 pass, sliding 5 pass · B08 A22/B1/C1 vs 8/8/8. The scenes compute the same outcomes in-component; the script is the independent check. sha256 at the end of the .out.txt.

## Corrections / de-sensationalising
- Brief point 5 "smooth out bursts rather than hard-blocking at a fixed count": sharpened. A token bucket *allows* short bursts up to its size and then holds clients to the refill rate; a sliding window removes the fixed window's reset-edge double burst. Both still reject excess traffic (429) — neither "never blocks". Narration says "a steady flood runs dry" and "edge bursts get through twice", not "no hard limits".
- Brief point 5 named two strategies; the fixed window is shown only as the foil the sliding window fixes.
- Brief point 6: real model APIs count requests *and* tokens per minute — stated on screen (B08 caption) instead of implying requests alone.
- All service names, keys, limits (5/s, 5/min, 5-token bucket, 24 slots) and traffic are illustrative and labelled so on screen. No vendor numbers are shown.
