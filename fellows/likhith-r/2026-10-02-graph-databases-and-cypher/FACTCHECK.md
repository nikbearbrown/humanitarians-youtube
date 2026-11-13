# FACTCHECK — Graph Databases and Cypher

Status: claims checked by Claude Code against the primary sources in SOURCES.md. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

Sign-off: I, Likhith, reviewed the 16:9 and 9:16 review cuts and approve the claims above as spoken and shown. I'm signing off for the final master.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Some data is mostly relationships (who knows / paid whom) | PASS | framing; the table shown is the real `friendships` table from the evidence | — |
| 2 | B03 | A graph DB stores nodes (things) and edges (relationships) directly | PASS | Neo4j docs: property graph model (nodes, relationships, properties) | "as data in their own right" → on-screen "stored as data" |
| 3 | B04 | In SQL, 3 hops = 3 joins of the friendships table | PASS | evidence/graph_demo.py SQL3 (real query, abridged on screen) | "every hop adds one" (not "exponentially slower") |
| 4 | B05 | A graph follows stored edges like pointers; work tracks what you visit | PASS (simplified) | Neo4j docs: native graph storage / index-free adjacency | see SOURCES: implementation-dependent; SQL with indexes pays a lookup per hop, not a full scan |
| 5 | B06 | Cypher: parentheses = nodes, arrow = relationship; `MATCH (a:Person)-[:FRIENDS_WITH]->(b:Person) RETURN b` | PASS | Cypher manual (patterns); real Kuzu output Ben, Cai for a = Ana | — |
| 6 | B07 | `*3` = three hops; same answer as the 3-join SQL: Fay | PASS | evidence/graph_demo.out.txt (Kuzu 0.11.3 and SQLite 3.53 both return Fay) | — |
| 7 | B08 | Fraud rings, recommendations, knowledge graphs | PASS | standard documented graph use cases (Neo4j use-case pages) | panels labelled illustrative |
| 8 | B09 | "Not a default: for plain rows and totals, tables still win" | PASS | added caveat (de-sensationalising) | — |
| 9 | B00, B11 | AI-narration disclosure: "narrated by an AI voice" · "Narrated by an AI voice." | PASS | Kokoro TTS narrates; no model named per Likhith | — |
