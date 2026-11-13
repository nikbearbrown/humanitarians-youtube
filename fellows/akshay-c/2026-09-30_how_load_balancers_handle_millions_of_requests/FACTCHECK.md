# Fact Check — How Load Balancers Handle Millions of Requests

## B00 — High request volume
Claim: Popular applications can receive millions of requests.
Status: PASS
Notes: Large-scale internet services routinely operate at request volumes reaching millions of requests over short time intervals. The narration uses this as a general scale illustration rather than a claim about a specific service.

## B01 — Single-server bottleneck
Claim: Sending very high traffic to a single server can overwhelm it.
Status: PASS
Notes: A server has finite CPU, memory, network, connection, and request-processing capacity. Traffic beyond available capacity can increase latency, cause request failures, or exhaust resources.

## B02 — Horizontal scaling requires traffic distribution
Claim: Adding servers introduces the need to determine which server handles each incoming request.
Status: PASS
Notes: Horizontally scaled services require a mechanism for distributing incoming traffic among available backend instances.

## B03 — Load balancer placement
Claim: A load balancer can sit between clients and backend servers and distribute requests.
Status: PASS
Notes: This accurately describes the standard role of a load balancer in a client-to-backend architecture.

## B04 — Round-robin routing
Claim: Round robin can send successive requests to successive servers.
Status: PASS
Notes: Round robin is a standard load-balancing strategy that cycles through available backend servers.

## B05 — Least-connections routing
Claim: A load balancer can route traffic based on the number of active connections.
Status: PASS
Notes: Least-connections is a standard load-balancing strategy that favors backend servers with fewer active connections.

## B06 — Health checks
Claim: Load balancers can perform health checks to identify servers that stop responding.
Status: PASS
Notes: Health checks are commonly used to determine whether backend targets are healthy enough to receive traffic.

## B07 — Routing around unhealthy servers
Claim: Traffic can be sent only to healthy servers when a backend becomes unavailable.
Status: PASS
Notes: Load balancers commonly remove or temporarily exclude unhealthy targets from normal traffic distribution until they recover.

## B08 — Scalability and resilience
Claim: Load balancing helps a pool of servers operate as a scalable and resilient service.
Status: PASS
Notes: Distributing requests across multiple healthy backend instances supports horizontal scaling and improves service availability when individual instances fail.

## B09 — Outro
Claim: No technical claim requiring verification.
Status: PASS
Notes: Humanitarians AI branded closing message.

## Overall
Status: PASS

The narration presents a simplified conceptual model of application load balancing. Actual implementations vary by load-balancer layer, protocol, routing algorithm, health-check configuration, session requirements, infrastructure architecture, and provider.
