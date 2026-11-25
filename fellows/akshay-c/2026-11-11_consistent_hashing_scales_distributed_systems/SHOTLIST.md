# SHOTLIST - How Consistent Hashing Scales Distributed Systems

| Beat | Act | Visual Subject | Motion Type | Primary Source |
|---|---|---|---|---|
| B00 | PROBLEM | Naive modulo hashing: Changing server count N remaps all keys and crashes backend | annotate | manim |
| B01 | HASH_RING | Consistent hash ring: 360-degree circular keyspace mapping servers around perimeter | annotate | manim |
| B02 | KEY_ROUTING | Clockwise routing: Hashing keys to ring position and assigning to nearest clockwise node | annotate | manim |
| B03 | NODE_ADDITION | Minimal movement: Inserting Server D only reclaims K/N keys without disturbing other nodes | annotate | manim |
| B04 | NODE_REMOVAL | Graceful failover: Server B crashes; its keys spill clockwise to Server C seamlessly | annotate | manim |
| B05 | HOTSPOTS | Hotspot imbalance: Sparse nodes create non-uniform arcs and severe load concentration | annotate | manim |
| B06 | VIRTUAL_NODES | Balanced distribution: Multiple virtual tokens per physical node balance traffic evenly | annotate | manim |
| B07 | PAYOFF | Production architecture: Four pillars of consistent hashing horizontal scalability | hold | manim |
| B08 | OUTRO | Branded Humanitarians AI closing title card | hold | remotion |
