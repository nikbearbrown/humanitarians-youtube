# FACTCHECK - How API Gateways Manage Millions of API Requests

| Claim | Source / Technical Standard | Verdict | Implementation Note |
|---|---|---|---|
| Direct client-to-microservice coupling creates operational chaos at scale | Microservice Architecture Patterns (Richardson); AWS API Gateway Best Practices | TRUE | Direct coupling exposes internal topology, forces duplicate auth/TLS/rate-limiting across services, and increases client round trips. |
| API Gateway acts as a reverse proxy single entry point | RFC 7230 / NGINX / Envoy proxy architecture | TRUE | Clients connect to a single host/port; the gateway handles protocol negotiation, connection pooling, and downstream routing. |
| Path-based routing dispatches requests by URL, method, and headers | Envoy route configuration / Kong routing engine | TRUE | Incoming URI prefixes (/users, /orders, /payments) map deterministically to upstream clusters. |
| Edge authentication offloads token validation from internal services | OAuth 2.0 / JWT RFC 7519 edge verification specs | TRUE | Gateways verify cryptographic signatures (HMAC/RSA/ECDSA) and claims before passing validated user identity headers downstream. |
| Token bucket / leaky bucket rate limiting protects backend systems | RFC 6585 (429 Too Many Requests); Redis token bucket algorithms | TRUE | Rate limits prevent denial of service and noisy-neighbor starvation by throttling requests exceeding quota. |
| Gateway distributes traffic and routes around unhealthy nodes | Envoy outlier detection / Active health checking | TRUE | Passive and active health checks remove degraded instances from load balancing pools. |
| Edge caching eliminates downstream queries for repeated reads | HTTP caching RFC 7234; Cloudflare / Fastly reverse proxy cache | TRUE | Cache-Control and ETag headers allow the gateway to respond directly from in-memory cache without hitting microservices. |
