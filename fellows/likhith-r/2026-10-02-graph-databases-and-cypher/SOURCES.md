# SOURCES — Graph Databases and Cypher

- Neo4j, Cypher Manual — patterns, `MATCH`, variable-length relationships — https://neo4j.com/docs/cypher-manual/current/
- Neo4j, "What is a graph database?" (property graph model; native graph storage / index-free adjacency) — https://neo4j.com/docs/getting-started/graph-database/
- openCypher project (Cypher as an open query language implemented by several databases) — https://opencypher.org/
- Kuzu embedded graph database, `kuzu==0.11.3` (PyPI), run in a throwaway `uv` env; not a toolkit dependency.
Brief supplied by the requester (Likhith); the 7 points were checked against the sources above (2026-10-21).

## Executable evidence
- `evidence/graph_demo.py` → `evidence/graph_demo.out.txt`. One 7-person toy network, loaded into Kuzu (Cypher) and SQLite (people + friendships foreign-key table).
- B02 table, B04 SQL, B06 result (Ben, Cai), B07 result (Fay from both engines) are verbatim from that run.

## Corrections / de-sensationalising
- "Joins get slower as depth increases" → stated as "every hop adds a join". With indexes, SQL pays an index lookup per row per hop, not a full-table scan; the cost growth is real but we don't claim a rate.
- "Deep queries stay fast" → stated as "the work tracks what you visit". Graph traversal still grows with the neighbourhood it touches; it avoids per-hop global index lookups. "Index-free adjacency" is how native stores like Neo4j describe this; other graph engines (Kuzu included) use adjacency lists and join internally. B05 is labelled illustrative.
- `*3` is shown because both Kuzu and Neo4j accept it (exact-length 3).
- Verdict card adds the honest limit: plain rows and aggregates are still a relational job.
- No benchmarks, version-dated adoption counts or vendor rankings.
