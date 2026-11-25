# Frictional log — Redis Caching Layer

## 2026-11-13 — the project update, in two aspect ratios

**What I was working on.** Adding a Redis caching layer to the FastAPI Gatekeeper to optimize vector search latency.

**What I tried, and what I expected.** 
- I spun up Redis in `docker-compose.yml` and wired it into `main.py`. I tried to save the Python dictionary directly to the cache using `redis_client.set(cache_key, evaluation)`.

**Where it resisted, and what I did next.** 
- **The Serialization Error:** Redis crashed because it only stores strings (or bytes), not raw Python dictionaries. I had to import the `json` module and explicitly serialize the payload using `json.dumps(evaluation)` before setting it, and `json.loads(cached_result)` upon retrieval.
- **The Stale Data Problem:** I initially forgot to add a Time-To-Live (TTL). The cache would hold evaluated claims forever, meaning if the underlying ChromaDB ledger was updated, the API would still serve the old cached truth. I swapped `redis_client.set()` to `redis_client.setex(cache_key, 3600, ...)` to force the cache to expire every hour.

**What Claude contributed, and what I did with it.** 
- Mine: The core architectural concept of placing Redis in front of ChromaDB.
- Claude's: Identifying the TTL requirement (`setex`) to prevent stale ledger data and providing the JSON serialization syntax.

**What I understand now, and what I still do not.**
- Understood: Caching is easy to build but hard to manage. You must explicitly serialize your data structures for memory storage, and you must always have an expiration strategy (TTL) to prevent data drift.