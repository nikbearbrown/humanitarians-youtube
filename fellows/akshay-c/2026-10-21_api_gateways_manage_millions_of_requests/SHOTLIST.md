# SHOTLIST - How API Gateways Manage Millions of API Requests

| Beat | Act | Visual Subject | Motion Type | Primary Source |
|---|---|---|---|---|
| B00 | PROBLEM | Chaotic direct connections from Web, Mobile, IoT clients to 3 microservices | annotate | manim |
| B01 | SOLUTION | API Gateway introduced as centralized reverse proxy between clients and services | annotate | manim |
| B02 | ROUTING | Path-based routing: /users, /orders, /payments directed to dedicated services | annotate | manim |
| B03 | SECURITY | Edge authentication: JWT token verified, invalid request blocked at edge | annotate | manim |
| B04 | RATE LIMITING | Token bucket rate limiting: normal flow allowed, spike throttled with 429 | annotate | manim |
| B05 | LOAD BALANCING | Traffic distributed across 3 instances, failing node bypassed automatically | annotate | manim |
| B06 | CACHING | In-memory edge cache returns high-frequency read response directly to client | annotate | manim |
| B07 | PAYOFF | Summary architecture diagram showing 4 pillars: Routing, Security, Throttling, Caching | hold | manim |
| B08 | OUTRO | Branded Humanitarians AI closing title card | hold | remotion |
