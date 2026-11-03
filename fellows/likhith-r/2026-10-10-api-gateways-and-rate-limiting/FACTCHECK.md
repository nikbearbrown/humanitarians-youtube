# FACTCHECK — API Gateways and Rate Limiting

Status: claims checked by Claude Code against the primary sources in SOURCES.md. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

Sign-off: I, Likhith, reviewed the 16:9 and 9:16 review cuts and approve the claims above as spoken and shown. I'm signing off for the final master.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Ten services each needing auth, logging and overload protection means ten copies (30 on screen) | PASS | 10 × 3 = 30; the cross-cutting-concern duplication the gateway pattern addresses (microservices.io) | Framed as a question, per brief |
| 2 | B03 | An API gateway is one entry point in front of the services; shared work is done once | PASS | microservices.io API Gateway pattern | "30 copies → 3, shared" is the toy count, not a measurement |
| 3 | B04 | It checks identity, routes to the right backend, and logs the request | PASS | Gateway responsibilities: authentication, routing, logging/monitoring (microservices.io; common gateway products) | Request, key and log line labelled "illustrative request" |
| 4 | B05 | Rate limiting caps a client's requests per time window; the excess is refused with 429 | PASS | RFC 6585 §4 | "so floods never reach the backend" = the excess is stopped at the gateway; outcome 5/5 from evidence script |
| 5 | B06 | Token bucket refills at a steady rate; bursts spend saved tokens; a sustained flood runs dry | PASS | RFC 2697 token-bucket metering; outcome pattern from evidence script (11 pass / 4 rejected) | Bucket size and tick are illustrative |
| 6 | B07 | A fixed window resets on the clock, so a burst straddling the reset gets twice the limit through; a sliding window counts the last 60 s | PASS | Cloudflare 2017 (boundary problem); evidence script: fixed 10 pass, sliding 5 | Limit 5/min illustrative |
| 7 | B08 | AI model calls are expensive; per-user limits stop one client draining shared capacity; real limits count requests and model tokens per minute | PASS | Anthropic rate-limit docs (RPM + input/output TPM, per org/key) | Slot counts illustrative; no vendor figures |
| 8 | B09 | A gateway turns scattered, duplicated protection into one consistent layer every request passes through | PASS | Summary of 1–7 | — |
| 9 | B10 | Blocked clients see 429 + Retry-After | PASS (softened) | RFC 6585: Retry-After MAY be included | Shown as an expected answer line, not a guarantee |
