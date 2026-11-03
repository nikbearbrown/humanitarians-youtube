# SOURCES — `ai-data-engineering-etl`

## Origin

Original explainer. There is **no single source document** — the topic was
specified by the reel's own narrator (Mohammed Hussain): *"how AI can be helpful in
data engineering tasks, like sending data from one pipeline to another; how ETL
will be simplified."*

Because there is no source to rewrite, the DOUBLE-CHECK LAW applies in its
stricter form: the reel may only assert what is checkable from the systems it
names. See `FACTCHECK.md` for the claim-by-claim ledger.

## What the technical claims rest on

| Claim | Rests on |
|---|---|
| `float8` → `numeric(12,2)` rounds | IEEE-754 binary64 cannot represent most decimal fractions exactly; conversion to a fixed-scale decimal must round. Property of the standard, not of any vendor. |
| `text` → `timestamptz` needs an explicit parse | A text column has no format guarantee; a typed target requires interpretation. Property of typed SQL/warehouse targets generally. |
| `NULL` → `NOT NULL` rejects the row | SQL constraint semantics. |
| Row-count reconciliation ≠ value correctness | Cardinality and value fidelity are independent properties; a count test cannot observe a value transformation. |

None of these depend on a product, a version, or a benchmark, so none of them will
date the video.

## Generated assets and determinism

Every visual in this reel is a native Remotion render. No stock images, no
screenshots, no lifted figures — REBUILD LAW satisfied by construction.

| Composition | New? | Determinism |
|---|---|---|
| `EtlGlueTax` / `…916` | new for this reel | pure function of `useP()`; no `Math.random()`, no timers |
| `EtlStages` / `…916` | new for this reel | same |
| `EtlSchemaMapping` / `…916` | new for this reel | same |
| `EtlWhereAiHelps` / `…916` | new for this reel | same |
| `EtlSilentFailure` / `…916` | new for this reel | same |
| `ClaudeComposerAsk` / `…916` | existing toolkit scene | frame-keyed typing, deterministic |
| `ClaudeCodeBeat` / `…916` | existing toolkit scene | deterministic |
| `ClaudeVerdictArtifact` / `…916` | existing toolkit scene | deterministic |
| `ClaudeTitleOutro` / `…916` | existing toolkit scene | deterministic |

There are no seeds to log — nothing in this reel is stochastic. Same commit →
identical frames, in both aspect ratios.

## Voice

Kokoro-82M (`kokoro-onnx`, Apache-2.0), voice `am_onyx` ("Onyx"), running locally
from `runtime/models/kokoro/`. No API, no key, no cost.

## Attribution / persona

The narrator speaks as himself. No channel identity is claimed: the
`@NikBearBrown` chip, the HAI chip, and the IN-FOR-BEAR sign-off are all dropped —
`folderLabel` and the outro handle read "Mohammed Hussain". This matches the prior
`onprem-rag-chatbot` and `mycroft-credit-rating` builds in this book.
