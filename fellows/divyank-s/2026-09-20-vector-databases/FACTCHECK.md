# FACTCHECK.md — Claude, Indexed.

## Method note (read first)

No single source document — this reel compares five real, actively-developed
products (Pinecone, Weaviate, pgvector, Qdrant, Chroma). Per the
DOUBLE-CHECK LAW, every claim is kept at the level of **stable, publicly
documented architecture** — never a specific version number, benchmark
score, latency figure, or pricing claim, since any of those would date the
video or require a live source check this build doesn't have. Claims are
tagged:

- **(General/stable)** — architectural facts unlikely to change: what
  indexing family a product uses, whether it's managed or self-hostable,
  whether it's a dedicated engine or a Postgres extension. These are
  foundational design choices, not implementation details that shift
  release to release.
- **(Qualitative, not quantitative)** — comparative claims stated in kind,
  not degree (e.g. "scales outward" vs. "scales mostly vertically") —
  deliberately avoiding "X times faster" or specific numbers that would
  require a benchmark this build didn't run.

## Claim-by-claim

| Beat | Claim | Category | Note |
|---|---|---|---|
| A1-2 | Pinecone: proprietary approximate index. Weaviate/Qdrant/Chroma: HNSW-family graph index. pgvector: IVFFlat or HNSW as a Postgres index type | General/stable | Widely documented in each product's own architecture docs; the algorithm family (not a specific implementation detail) is the stable claim |
| A1-3/A1-4 | Pre-filter (restrict candidates during/before the search) vs. post-filter (search then discard); Qdrant, Weaviate, Pinecone documented as integrating filtering into the index; pgvector's filtering runs through the Postgres query planner; Chroma's filtering is comparatively simple | General/stable | The pre/post-filter distinction is a well-known ANN systems concept, not specific to any one vendor; each vendor's general filtering *approach* (integrated vs. planner-based vs. simple) is publicly documented positioning, not a specific number |
| A1-5 | A highly selective filter can return zero results under naive post-filtering (top-k search, then discard) | General/stable | A well-known, logically-necessary consequence of the post-filter pattern (if k candidates are drawn before filtering and none pass, the result set is empty) — not vendor-specific, a property of the pattern itself |
| A2-2 | Weaviate multi-tenant collections; Qdrant payload-based tenant partitioning; Pinecone namespaces; pgvector via Postgres RLS/schema-per-tenant; Chroma's multitenancy support is comparatively thin | General/stable | Each product's own documented multitenancy feature/pattern; "comparatively thin" is a qualitative positioning claim, not a specific missing-feature claim |
| A2-5 | Pinecone/Weaviate/Qdrant scale by sharding/adding nodes; pgvector scales primarily the way a single Postgres instance scales (vertical + read replicas) | Qualitative, not quantitative | Directional/architectural claim (horizontal vs. vertical scaling model) — no specific ceiling number or benchmark claimed |
| A3-2/A3-3 | Pinecone: no self-hosting option, usage-based cost; Weaviate: self-hosting requires real operational work; pgvector: ANN tuning is ongoing manual work; Qdrant: younger/smaller ecosystem than longer-established alternatives; Chroma: designed for simplicity, strained by large multi-tenant scale | Qualitative, not quantitative | Positioning/tradeoff claims, phrased as directional statements, not measured facts (no specific age, community-size, or cost number stated) |
| A3-4 | Managed removes ops burden but adds vendor lock-in; self-hosted removes lock-in but keeps the ops burden | General/stable | A general, well-known tradeoff in all managed-vs-self-hosted software, not a claim specific to any one product |
| A4-2/A4-3 | Use-case framing per product (RAG at scale / hybrid search / already-on-Postgres / filter-heavy search / prototyping) | Qualitative | Framed as the reel's own synthesis/recommendation, not a claim any vendor makes about itself |

## What was deliberately left out

- No specific version numbers (e.g., which pgvector release added HNSW) —
  these change and would date the video.
- No benchmark numbers, QPS figures, or latency/cost comparisons — none
  were run or sourced for this build.
- No claim about any product's roadmap or unreleased features.

## Corrections applied

None — first draft, no prior version to correct against.
