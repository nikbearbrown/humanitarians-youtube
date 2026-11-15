# Week 11: Scaling the Gatekeeper with Redis Caching

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A terminal shows a progress bar taking a painfully long time to process a single request. 
**VO:**
Hi, I am Onkar Bhujbal. Our Provenance Gatekeeper is secure and fully automated. But there is a glaring problem: speed. Converting text into mathematical embeddings and searching a vector database takes heavy compute power. If our AI generates the same financial claim ten times, we are calculating that math ten times from scratch. This week, we are kicking off Phase 2 of our architecture by integrating a high-speed Redis caching layer.

### SCENE 2 — THE REDIS ARCHITECTURE
**VISUAL** — An architectural diagram. The FastAPI app sits in the middle. On the right is the heavy ChromaDB icon. On the left, a lightning-fast Redis icon appears as a shield.
**VO:**
We updated our Docker Compose file to spin up an Alpine Linux Redis container. Redis is an in-memory data store, meaning it runs entirely on RAM. By positioning it between our API and our Vector Database, we can intercept repeat queries before they ever reach the heavy machine learning models.

### SCENE 3 — THE CACHE HIT
**VISUAL** — The Python code for `verify_claim`. It highlights the `redis_client.get(cache_key)` logic, then drops down to the `redis_client.setex()` logic.
**VO:**
The logic is incredibly simple. When a claim comes in, the Gatekeeper checks Redis. If the answer is there—a Cache Hit—it returns it instantly in milliseconds. If it’s not there—a Cache Miss—it falls back to ChromaDB, does the heavy lifting, and then saves the final evaluation in Redis for the next hour. 

### SCENE 4 — PERFORMANCE GAINS
**VISUAL** — Split screen comparison. Left: "Without Cache" (Response Time: ~450ms). Right: "With Redis Cache" (Response Time: ~12ms).
**VO:**
The performance gains are staggering. Our initial vector searches were taking nearly half a second to process locally. But on a cache hit, Redis serves the verified answer in under 15 milliseconds. We have effectively decoupled our read-latency from our compute overhead, allowing the Gatekeeper to handle massive enterprise scale.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Don't do the same math twice.`
**VO:**
Compute is expensive. RAM is cheap. Cache your results and save your processors for the novel problems.
Liam, for Onkar Bhujbal and Humanitarians AI.