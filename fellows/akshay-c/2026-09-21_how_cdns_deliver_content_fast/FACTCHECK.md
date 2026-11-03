# Fact Check — CDN Explainer

- A CDN distributes content delivery across edge infrastructure / points of presence.
- CDN routing does not necessarily select the geographically closest machine.
- DNS, Anycast, topology, health and network conditions may influence routing depending on provider architecture.
- A cache hit can serve a fresh cached object without fetching it from the origin.
- A cache miss may require fetching the object from the origin or another configured upstream.
- Cache-Control and CDN-specific policies can determine cacheability and freshness.
- TTL, revalidation, purge and invalidation are different mechanisms for controlling freshness.
- Static reusable assets such as images, CSS, JavaScript, fonts, downloads and video segments are common CDN workloads.
- Personalized or otherwise uncacheable responses may still require origin processing.
- A CDN reduces repeated long-distance delivery work; it does not eliminate the origin or network latency.
