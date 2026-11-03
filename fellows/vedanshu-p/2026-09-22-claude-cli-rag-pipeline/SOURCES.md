# SOURCES — claude-cli-rag-pipeline

*"Watch A Bug Name Its Own Stage." · RAG Foundations, Chapter 7 — The RAG
Pipeline End to End*
*DOUBLE-CHECK LAW record.*

---

## Primary source

| Field | Value |
|---|---|
| Book | *RAG Foundations* — Vedanshu Daxesh Patel |
| Repo | `D:\ai1-cli-main` |
| Chapter | `chapters/07-rag-pipeline-end-to-end.md` |
| Fact-check record | `chapters/07-rag-pipeline-end-to-end.md.verified.json` |

## The demo is real — with one component declared as a stand-in

| File | Role | Real? |
|---|---|---|
| `code/corpus.py` | Six raw help-desk policy documents + the chapter's question | synthetic, written |
| `code/encoder.py` | `all-MiniLM-L6-v2` embeddings, numpy BERT forward pass | **real model weights** |
| `code/pipeline.py` | The five stages, traced end to end | **real** |
| `code/diagnose.py` | One fault per stage, three signals recorded | **real** |

Captured transcripts, verbatim: `_run-pipeline.txt` (feeds B04),
`_run-diagnose.txt` (feeds B07 and B08).

`encoder.py` is carried over from the Chapter 6 reel — the same hand-rolled
safetensors parser and 6-layer numpy forward pass, because `sentence-transformers`
is not installed on this machine. Its behavioural validation (identical 1.000 /
paraphrase 0.555 / unrelated 0.100) is recorded in that reel's SOURCES.md.

### The generate stage is NOT a language model — and that is deliberate

`generate()` is a **deterministic extractive reader**: it scores every sentence
in the prompt's CONTEXT block against the question's content words and returns
the best one verbatim, with the chunk id it came from. It cannot produce a
sentence that is not in the prompt.

**This is stated out loud in the reel** — in the code beat (B03's docstring says
"NOT an LLM"), and in B09's narration, which names it as the reason the
signatures came out clean.

**Why a stand-in is the right call here, not a shortcut.** Chapter 7's claim is
about *stage localisation*: that a symptom at the output traces back to exactly
one stage. A stochastic LLM actively undermines the test —

* it can answer correctly **from prior knowledge** even when retrieval failed,
  hiding a retrieval fault behind a right answer; and
* it can hallucinate even when every upstream stage worked, imitating a fault
  that is not there.

Either behaviour breaks the one-to-one mapping between fault and symptom that
the chapter is asserting. A reader that can only quote the prompt makes the
mapping measurable. It is a **control**, and the reel treats its cleanness as a
limitation to declare rather than a result to boast about.

## What was measured

**B04 — the end-to-end trace (`_run-pipeline.txt`):**

| stage | emitted | what moved |
|---|---|---|
| ingest | 13 chunks | 6 documents → paragraph chunks |
| embed | 13×384 index | chunks → vectors |
| retrieve | top-3 chunks | VA-101#0 (0.618), VA-101#1 (0.512), VA-101#2 (0.490) |
| augment | 615-char prompt | question + chunks + instruction |
| generate | 1 answer | "First-year employees accrue 12 paid vacation days." cited `VA-101#0` |

**B07/B08 — one fault at a time (`_run-diagnose.txt`):**

| stage broken | top chunk | right fact? | cited | grounded |
|---|---|---|---|---|
| none (control) | VA-101#0 | yes | VA-101#0 | yes |
| retrieve | SL-140#0 | NO | SL-140#0 | yes |
| augment | VA-101#0 | yes | none | yes |
| generate | VA-101#0 | NO | none | NO |

`all three distinguishable: YES` — printed by the script, not asserted by the
narration.

## Corrections and editorial decisions applied

1. **The chapter's predicted retrieval set did not occur, and the reel says what
   did.** Chapter 7 illustrates retrieval returning the vacation chunk "along
   with a few other plausibly related chunks, perhaps one about sick leave and
   one about a general benefits overview". The actual run returned all three
   chunks from VA-101 itself, because paragraphs of one policy sit close
   together in embedding space. B04's narration reports that rather than the
   chapter's illustration. The chapter says "perhaps", so this is not a
   contradiction — but it is a difference, and the measured result wins.

2. **The five-stage breakdown is framed as the book's own device, not as
   research.** The chapter is explicit that no single source defines RAG with
   exactly these five names, and that it is "this book's teaching device for
   organizing and diagnosing the pipeline". B04's citation line says so; the
   reel never attributes the five names to Lewis et al.

3. **The generator's limitation is a summary beat, not a footnote.** B09 spends
   roughly a third of its narration on it. The alternative — letting a clean
   four-row table imply the result generalises to a real LLM — would have been
   the most misleading thing this reel could do.

4. **No accuracy or benchmark number is claimed.** The reel reports one
   question, four runs. It does not extrapolate to a hit rate.

5. **The corpus is synthetic and stacked in both directions.** SL-140 and BO-001
   exist specifically so the broken retriever returns something *plausible*;
   BO-001 mentions vacation without giving a first-year number. Without those
   distractors the retrieval fault would have returned obvious nonsense and
   proved nothing.

6. **Nothing version-dated introduced** — no model version claims beyond the
   specific checkpoint used, no drifting counts.

## Sources the chapter cites, and how the reel uses them

| # | Source | Used in | How |
|---|---|---|---|
| 1 | Lewis et al. (2020) — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* | B07 citation | Cited for the retriever + generator architecture the pipeline framing rests on. NOT cited as the origin of the five stage names |
| 2 | Gao et al. (2023/2024) — *RAG for LLMs: A Survey* | background | The three-part retrieval/generation/augmentation framing the chapter contrasts its own five-way split against. Not named on screen |

## Figures

| Source figure | Treatment |
|---|---|
| `images/rag-pipeline-end-to-end-fig-01` — five labelled boxes with annotations of what moves between them | **Rebuilt natively** as B04 (`PipelineTrace`), with the boxes carrying measured artifacts (13 chunks, 13×384 index, 615-char prompt) instead of illustrative labels. REBUILD LAW |

Chapter 7 has only the one figure. No source image is embedded anywhere.

## Components

New this reel (GATE L: four searches, both genuine misses):

| Composition | Beat | 9:16 twin |
|---|---|---|
| `PipelineTrace` | B04 | `PipelineTrace916` |
| `FaultSignatureTable` | B07 | `FaultSignatureTable916` |

Closest lead: `HaiBrutalistE01Pipeline` (score 9.0) — a seven-stage pipeline
rail. **Rejected on inspection:** its `STAGES` array is a module constant
hardcoded to that reel's own stage names, and it exposes only `sparkLine`. A hit
is a lead, not a verdict; opening the file settled it.

Both new components sit on the existing `EmbedChrome` `FigureFrame` and reuse
`ChunkChrome`'s `useBeatClock`, so Chapters 3–7 share one chrome and one clock.

Reused unmodified (props only): `ClaudeComposerAsk` (B00, B02, B05, B10),
`ClaudeCodeBeat` (B03, B06), `CliRunOutput` (B08),
`RagExecutiveSummary` (B01, B09), `TitleOutroChannel` (B11).

`TitleOutroChannel`, not `ClaudeTitleOutro`: OUTRO-LOCK.md §Scope restricts the
locked card to `claude-liam-*` slugs; it hardcodes `@NikBearBrown` and never
renders a subline, which would drop the author signature.

## Determinism

Ingest, augment and generate are deterministic by construction. The embeddings
are a fixed pretrained checkpoint with no sampling. Re-running either script
reproduces every number in this reel exactly. Every Remotion beat is a pure
function of its frame; no `Math.random` at render.

## Voice

Kokoro `am_onyx`, local, free. **$0.00 spent.** No paid API, no network call.
