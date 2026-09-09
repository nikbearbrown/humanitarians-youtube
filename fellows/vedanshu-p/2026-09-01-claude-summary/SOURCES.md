# SOURCES — claude-rag-the-right-text

This is a **summary reel**. It makes no claim of its own: every number, figure,
and quoted output is carried across from one of the three source reels' own
beat sheets, which are the primary sources here. DOUBLE-CHECK LAW: nothing was
invented for the summary, and nothing was sharpened beyond what the sources
support.

## Source reels

| Ch. | Reel | Title |
|---|---|---|
| 1 | `youtube/2026-08-31-claude-cli-rag-introduction` | Watch Retrieval Fix A Stale Answer. |
| 2 | `youtube/2026-08-31-claude-cli-rag-the-problem` | Watch The Obvious Fix Fail. |
| 3 | `youtube/2026-09-01-claude-rag-embeddings` | Meaning, As A Number. |

## Claim → source trace

| Beat | Claim on screen | Traces to |
|---|---|---|
| B02 | ten sick days, stale for eight months; fifteen after retrieval, with the passage cited | ch. 1 beats B03/B04 (`TRAINING_SNAPSHOT`) and B06/B07 (`retrieve()`, `DOCUMENT_STORE`) |
| B03 | the scan returns the vacation paragraph because it shares "leave" and comes first | ch. 2 beats B06/B07 (`naive_scan` returns the first match; the correct parental-leave passage is never reached) |
| B04 | the four query phrasings and their close/far grouping | ch. 3 beat B09 (`EmbedRevealPairs`), coordinates copied unchanged |
| B05 | cosine similarity is the angle between two vectors | ch. 3 beat B06, citation carried verbatim |
| BVDT | the five verdict lines | one line per source claim above; chapter attributions on each |

## Third-party citations (carried through, not re-derived)

- Mikolov, Yih & Zweig (2013) — word-vector arithmetic, and the caveat that the
  result depends on excluding the query word. Carried from ch. 3 beat B03.
  *Not used in this summary* — the arithmetic beat was not summarised.
- Reimers & Gurevych (2019) — Sentence-BERT. Carried from ch. 3 beats B04/B05.
  *Not used in this summary.*
- Manning, Raghavan & Schütze (2008) — cosine similarity in classical IR.
  Used on B05, citation string carried verbatim from ch. 3 beat B06.

## Redraw notice

B04 carries "Redrawn (simplified) from chapter three's Fig. 02" on screen, per
REBUILD LAW — the figure is a native Remotion render, not a lifted image, and
the simplification (two dimensions instead of hundreds) is disclosed in the
caption exactly as the source reel disclosed it.

## Determinism

- Narration: Kokoro `am_onyx`, local, free. `$0.00`. No paid API was called.
- `BrutalistHesitantWriter` seed: `claude-rag-the-right-text-b01` — same seed
  renders an identical performance forever.
- Every other beat is a pure function of its measured audio duration.
