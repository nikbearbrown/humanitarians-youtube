# Shot List — How Load Balancers Handle Millions of Requests

## B00 — Millions of Requests
- Act: INTRO
- Source: Manim
- Visual: Large volume of incoming requests illustrating traffic at scale.
- Purpose: Establish the scale of traffic handled by popular applications.

## B01 — One Server Bottleneck
- Act: PROBLEM
- Source: Manim
- Visual: Incoming requests converge on a single server, showing it becoming overwhelmed.
- Purpose: Demonstrate the limitation of relying on one backend server.

## B02 — More Servers
- Act: PROBLEM
- Source: Manim
- Visual: Multiple backend servers appear, introducing the question of where requests should go.
- Purpose: Introduce horizontal scaling and the traffic-distribution problem.

## B03 — Load Balancer
- Act: SOLUTION
- Source: Manim
- Visual: A load balancer sits between incoming users/requests and the backend server pool.
- Purpose: Introduce the load balancer and its position in the architecture.

## B04 — Round Robin
- Act: ROUTING
- Source: Manim
- Visual: Requests are distributed sequentially across available servers.
- Purpose: Explain round-robin load balancing.

## B05 — Least Connections
- Act: ROUTING
- Source: Manim
- Visual: Server connection loads are compared and traffic is directed toward the less-busy server.
- Purpose: Explain least-connections routing.

## B06 — Health Checks
- Act: RESILIENCE
- Source: Manim
- Visual: Backend servers are health-checked, with one server marked unavailable.
- Purpose: Show how a load balancer detects an unhealthy backend.

## B07 — Route Around Failure
- Act: RESILIENCE
- Source: Manim
- Visual: Traffic bypasses the failed server and continues toward healthy servers.
- Purpose: Demonstrate failure handling and continued availability.

## B08 — Scalable, Resilient Service
- Act: OUTRO / CONCLUSION
- Source: Manim
- Visual: Load balancer and server pool presented as one scalable, resilient service.
- Purpose: Reinforce the overall load-balancing mental model.

## B09 — Humanitarians AI Outro
- Act: OUTRO
- Source: Remotion
- Pattern: ClaudeTitleOutro
- Visual: Branded Humanitarians AI closing card.
- Title: How Load Balancers Handle Millions of Requests
- Handle: @HumanitariansAI
- Purpose: Branded closing and call to follow Humanitarians AI.

## Delivery
- Primary aspect ratio: 16:9
- Resolution: 3840x2160
- Frame rate: 24 fps
- Narration voice: am_onyx
- Creator: Akshay Chavan
- Channel: @HumanitariansAI
