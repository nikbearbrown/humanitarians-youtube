# FACTCHECK — How Caching Makes Applications Faster

## Core claims

### B00 — Repeated data requests
Applications often request the same or frequently reused data multiple times. Repeatedly retrieving that data from a database can add latency and backend work.

Status: PASS

### B01 — Database load
As request volume increases, repeated database queries can increase database workload and may contribute to application latency.

Status: PASS

### B02 — Caching
A cache stores frequently or recently accessed data closer to the application so that some requests can avoid retrieving the same data from the original data source.

Status: PASS

### B03 — Cache miss
A cache miss occurs when requested data is not available in the cache. The application may then retrieve the data from the underlying data source, such as a database.

Status: PASS

### B04 — Storing the result
After retrieving data from the underlying source, applications commonly store a copy in the cache so later requests can potentially reuse it.

Status: PASS

### B05 — Cache hit
A cache hit occurs when requested data is available in the cache. In this case, the application can use the cached value without performing the corresponding database lookup.

Status: PASS

### B06 — TTL
A time to live (TTL) can define how long a cached entry remains valid. Expiration helps prevent cached information from remaining indefinitely.

Status: PASS

### B07 — Performance benefit
Serving suitable requests from a cache can reduce database workload and improve response latency.

Status: PASS

## Scope notes

The video explains the basic cache-aside/request-flow concept at an introductory system-design level.

It intentionally does not cover cache invalidation strategies, eviction algorithms, distributed-cache consistency, write-through/write-back caching, cache stampedes, replication, or specific products such as Redis.

## Overall fact-check status

PASS
