# Report: Claude, Indexed. — Vector Databases Compared, Two Cuts

**Topic:** Vector databases compared — Pinecone, Weaviate, pgvector, Qdrant, Chroma
**Skill:** `deep-explainer` (brutalist.art toolkit)
**Location:** `humanitarians-youtube/fellows/divyank-s/2026-09-20-vector-databases/`
**Cost:** $0.00 (Kokoro TTS, local Remotion rendering, no API keys)

## 1. Deliverables

| | 16:9 master | 9:16 Short |
|---|---|---|
| **File** | `claude-liam-vector-databases-compared.mp4` | `short/claude-liam-vector-databases-compared-short.mp4` |
| **Resolution** | 3840×2160 (4K UHD) | 2160×3840 (4K UHD, vertical) |
| **Duration** | 405.08s (6:45.1) | 157.64s (2:37.6) |
| **File size** | 154.0 MB | 83.0 MB |
| **Beats** | 32 | 13 |
| **Gate** | `PEDAGOGY.md` — `VERDICT: PASS` | `short/PEDAGOGY.md` — `VERDICT: PASS` (covers the one new line, the rewritten outro) |
| **Signed** | "Liam, in for Divyank" / `@DivyankSingh` throughout | same |

Both are real, rendered, playable files. Neither is published or
authorized for publication.

## 2. The 6 required points, and where each is covered

No single source document underlies this reel — it compares five real,
actively-developed products. The 6 required points are grouped into 4 acts:

| Act | Points | Beats |
|---|---|---|
| **I — How Each One Finds Your Vector** | (1) Indexing algorithm/strategy, (2) Pre/post filtering | `A1-1`–`A1-6` |
| **II — Who Else Is In Your Index** | (3) Multitenancy, (4) Scalability | `A2-1`–`A2-6` |
| **III — What Breaks in Production** | (5) Drawbacks in production use | `A3-1`–`A3-6` |
| **IV — Pick One** | (6) Use cases | `A4-1`–`A4-6` |

On screen, specifically:

- **(1) Indexing** (`A1-2`): Pinecone's proprietary approximate index;
  Weaviate/Qdrant/Chroma on HNSW-family graphs; pgvector adding IVFFlat or
  HNSW as a Postgres index type rather than a new engine.
- **(2) Pre/post filtering** (`A1-3` the concept, `A1-4` per-database
  positioning, `A1-5` the consequence): the post-filter/pre-filter
  distinction, each database's documented filtering approach, and the
  concrete failure mode of naive post-filtering against a highly selective
  filter (zero results returned even when a match exists).
- **(3) Multitenancy** (`A2-2`, `A2-3`): Weaviate's first-class multi-tenant
  collections, Qdrant's payload-based partitioning, Pinecone's namespaces,
  pgvector's inherited Postgres RLS/schema-per-tenant patterns, and
  Chroma's comparatively thin story — plus the shared-index-vs.
  one-index-per-tenant architecture fork every one of the five forces.
- **(4) Scalability** (`A2-5`): the qualitative split between
  Pinecone/Weaviate/Qdrant's horizontal shard-and-add-nodes model and
  pgvector's mostly-vertical, single-Postgres-instance ceiling.
- **(5) Production drawbacks** (`A3-2`, `A3-3`, `A3-4`): one named tradeoff
  per database (Pinecone's lock-in, Weaviate's self-hosting labor,
  pgvector's ongoing ANN tuning, Qdrant's younger ecosystem, Chroma's
  simplicity-first design under multi-tenant strain), unified by the
  managed-vs-self-hosted fork behind most of them.
- **(6) Use cases** (`A4-2`, `A4-3`): one best-fit scenario per database,
  plus the "already on Postgres?" decision fork as the practical
  starting question.

## 3. Sourcing and fact-check method

Per `FACTCHECK.md`, every comparative claim is kept at the level of
**stable, publicly documented architecture** — index family, managed vs.
self-hostable, dedicated engine vs. Postgres extension — and explicitly
excludes version numbers, benchmark scores, latency figures, and pricing,
since none of those were sourced or verified for this build and would date
the video. Claims are tagged General/stable (architectural facts unlikely
to change) or Qualitative (comparative claims stated in kind, not degree —
"scales outward" vs. a specific number).

## 4. The archival imagery — used as metaphor, not evidence

The topic has no historical photographic referent, so all 5 real
Wikimedia Commons stills (public domain or CC-licensed) illustrate a
CONCEPT, never the databases themselves:

| Beat | Image | Stands in for |
|---|---|---|
| A1-1 | 1967 MBTA subway map | an index as a fast-navigation map |
| A2-1 | Building with many windows | multitenancy — many units, one structure |
| A2-4 | Cargo ship, Eurogate Container Terminal Hamburg | scaling capacity |
| A3-1 | Steel beams stabilizing a bridge | production tradeoffs, felt under load |
| A4-1 | Organized tool case (Moderationskoffer) | picking the right tool for the job |

## 5. Building the two aspect ratios

This build was signed for Divyank from the first draft (unlike the two
prior builds this session, which were authored for "Nik Bear Brown" and
rebranded afterward) — `@DivyankSingh` and "in for Divyank" throughout,
no retrofit needed.

Portrait coverage was again planned into the beat sheet up front: one
`BinaryBranch`/`DivergentFates` hero beat per act (`A1-5`, `A2-3`, `A2-5`,
`A3-4`, `A4-3`). As with both prior Shorts, `shorts.py`'s auto cap-check
still needed manual correction — its first proposal landed at 180.4s
(still over the 3:00 cap) while cutting 4 of the 5 pre-planned hero beats
in favor of shorter, portrait-unsupported `ChipGrid`/`FluencySegmentCard`
beats. Manually overridden (`--drop` on the 20 non-essential beats) to
keep the cold open, one VOX still per act, all 5 mechanism beats, the
handoff, and the outro — 13 beats, 167.4s, zero `ONDA CHECK` blocks. The
same recurring auto-rewritten-outro bug (raw narration fragments stitched
into a broken sentence) was hand-fixed before its audio was generated —
the third time this exact defect has appeared across three Shorts built
this session.

**A file-integrity incident during this build, resolved:** shortly after
the 16:9 master was first written to its correct location, something
outside this session silently rewrote it with a slightly shorter, invalid
duration (402.6s instead of 405.08s) while no render process was running.
The likely cause is this folder's location under `Documents`, which
commonly syncs to iCloud or a similar cloud-storage layer — a sync or
file-eviction/re-materialization cycle is the probable culprit, not a
toolkit defect. Caught during verification; a forced fresh recompile
(`--force`) reproduced the file byte-for-byte identical to the original
correct render (same size, same duration), confirming the render itself
is deterministic and the master is now stable at the correct spec.

## 6. Known limitations

- **No frame-level Visual QC** was run on either cut (`ART_QC=0`, this
  session's standing agreement).
- **`./art run`'s final (non-review) compile pass does not forward
  `--out`** — it still defaults to `brutalist.art/renders/` even when
  `--out` is passed to `./art run` itself. Calling `compile.py` directly
  with `--out` (as done for the Short and for the corrective recompile)
  works correctly; this is worth fixing in `art`/`run.sh` if this pattern
  recurs.
- **`shorts.py`'s auto-planner still has no concept of portrait-composition
  support** — the third build in a row where pre-planned hero beats needed
  a manual `--drop` override because the auto-plan optimizes on duration
  alone.
- **Neither video is published or authorized for publication.**
