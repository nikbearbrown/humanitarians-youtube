# FACTCHECK.md — Claude, Dispatched.

## Method note (read first)

No single source document — this reel covers well-established software
architecture: FastAPI and gRPC. Per the DOUBLE-CHECK LAW, every claim is
kept at the level of **stable, publicly documented mechanism**, never a
specific version number, named third-party product's exact feature
support, or a benchmark percentage (none of which were sourced or
verified for this build, and all of which would date the video or risk
an unverifiable claim).

## Claim-by-claim

| Beat | Claim | Category | Note |
|---|---|---|---|
| A1-2 | FastAPI is a Python web framework built on Starlette (ASGI) and Pydantic, speaking HTTP/JSON; gRPC is Google's framework built on HTTP/2 and Protocol Buffers | General/stable | Both frameworks' own documented architecture; foundational facts unlikely to change |
| A1-3 | JSON is text-based/human-readable/loosely typed at the wire; Protocol Buffers is a schema-first, compiled, strictly typed binary format | General/stable | Core, long-stable properties of each serialization format |
| A1-5 | HTTP/1.1 (one request per connection, roughly) vs. HTTP/2 (multiplexed streams on one connection) | General/stable | HTTP/1.1 and HTTP/2 RFC-level, vendor-neutral protocol facts |
| A2-1 through A2-6 | The gateway / Backend-for-Frontend (BFF) pattern: a public-facing service (e.g. FastAPI) fronting internal services that communicate via a different protocol (e.g. gRPC) | General/stable | A widely-documented, vendor-neutral microservices architecture pattern, not attributed to one specific company or product here |
| A3-2 | FastAPI generates interactive API documentation (OpenAPI-based) automatically from code | General/stable | FastAPI's own core, well-known feature |
| A3-3 | gRPC supports four call patterns including bidirectional streaming, uses persistent HTTP/2 connections, and typically produces smaller payloads than equivalent JSON | General/stable | gRPC's own documented core design; "typically smaller" stated qualitatively, no specific percentage or benchmark cited |
| A3-4/A3-5 | gRPC's compact binary encoding and persistent-connection streaming fit constrained-bandwidth/battery contexts such as IoT and mobile | General/stable | A widely-documented rationale for gRPC adoption in resource-constrained contexts; no specific product, device, or vendor named |
| A4-2 | Web browsers cannot natively originate or terminate gRPC's HTTP/2-trailer-based framing; bridging requires gRPC-Web plus a translating proxy | General/stable | A well-documented, real architectural limitation (the reason gRPC-Web exists as a separate project at all) — not a claim about any specific proxy product's current feature set |
| A4-3/A4-5 | Debugging a JSON/HTTP call is more directly accessible (browser dev tools, curl) than debugging a binary protobuf payload (requires the .proto schema or specialized tooling) | General/stable | A widely-acknowledged, practical tradeoff discussed across the industry, not sourced to one specific article |

## What was deliberately left out

- No specific version number for FastAPI, Starlette, Pydantic, gRPC, or
  Protocol Buffers.
- No specific benchmark numbers (e.g., "X% smaller payloads" or "Y times
  faster") — all size/speed comparisons are stated qualitatively.
- No claim about any one named gRPC-Web proxy product's current feature
  set or compatibility.

## Corrections applied

None — first draft, no prior version to correct against.
