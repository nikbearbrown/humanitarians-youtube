# PEDAGOGY — Watch The Right Answer Get Outvoted. (personal-author cli-explainer)

CLI explainer of *RAG Foundations*, Chapter 6 ("Retrieval Methods: Sparse,
Dense, and Hybrid"). Built with the **`cli-explainer`** skill — the
build-with-Claude loop.

**Tier note.** `cli-explainer` is ADVANCED tier ("Bear only" in CLAUDE.md).
Invoked here by explicit human request. It escalates nothing: the whole build
runs on the free path (Kokoro `am_onyx`, Remotion, local numpy, a
already-cached model checkpoint), spends **$0.00**, calls no paid API and makes
no network request.

Personal author channel: persona and sign-off are the book's author, Vedanshu
Daxesh Patel (`@VedanshuDaxeshPatel`). IN-FOR-BEAR LAW does not apply — the
narrator is named as themself in B00 and signs off as themself in B11.
Never publishes.

**Book root.** Built into `D:\ai1-cli-main\youtube\` per CLAUDE.md rule 3.
Folder dated **2026-09-08** per explicit instruction — the same date as the
Chapter 5 CLI reel, which is fine; the slugs differ.

**Siblings.** Follows the spine set by `2026-08-26-claude-cli-rag-embeddings`
(Ch. 3 CLI) and `2026-09-08-claude-cli-rag-vector-databases` (Ch. 5 CLI), and
shares chrome (`EmbedChrome`) and beat clock (`ChunkChrome`) with the Ch. 4
`ai-explainer`, so Chapters 3–6 cut together as one series.

## The ONE idea

> Sparse and dense retrieval fail on different queries, so combining them
> usually helps — but fusion counts ranks rather than reasoning, so a
> confidently wrong retriever can still outvote a correct one.

## Why this chapter suits a CLI video

Chapter 6's central claims are all *testable in one sitting*: that sparse wins
an exact-code query, that it loses a paraphrase, and that combining the two
signals "usually helps and rarely hurts". A CLI video can build all three
retrievers, run the chapter's own two queries through them, and put the measured
outcome on screen — turning a set of assertions into a result the viewer watches
arrive.

It also happens to be a chapter that **refuses to over-claim**, and that made it
the right chapter to build honestly: when the run disagreed with the expected
story, the chapter's own hedging was already there to land on.

## Act structure (the mandatory CLI spine)

- **B00 INTRO** — `ClaudeComposerAsk`, ask shown answered (COLD OPEN LAW).
- **B01 PROBLEM** — `RetrievalTwoQueries`. Two employees, one policy, opposite
  questions. Mandatory beat; no code yet. Rebuilds the chapter's worked-example
  premise as the reel's spine.
- **B02 CLI → B03 CODE → B04 OUTPUT** — cycle 1, sparse only. Real BM25,
  real stdout: HIT on the code, MISS on the paraphrase.
- **B05 CLI → B06 CODE → B07 OUTPUT** — the revision (THE REVISION LAW). The
  revised prompt asks for dense retrieval *and* for all three methods to be
  reported, which is what makes the surprise visible.
- **B08 OUTPUT (second result, same run)** — the fusion arithmetic on the query
  fusion lost.
- **B09 SUMMARY** — the lesson, plus the two things this run does NOT prove.
- **B10 NEXT STEPS** — `ClaudeComposerAsk`, `"Your turn."` (HANDOFF LAW).
- **B11 OUTRO** — `TitleOutroChannel`, exact title restate, signature.

## The finding, and how the reel handles it

The expected shape was: sparse wins query 1, dense wins query 2, hybrid wins
both. **Two of those three turned out wrong**, and the reel is built around the
measurement rather than the expectation.

| | expected | measured |
|---|---|---|
| sparse on exact code | HIT | HIT ✓ |
| sparse on paraphrase | MISS | MISS ✓ |
| dense on exact code | **MISS** (entity-centric weakness) | **HIT** (0.600) |
| dense on paraphrase | HIT | HIT ✓ |
| hybrid on both | **HIT** | **MISS on the paraphrase** |

**Why hybrid lost.** On the paraphrase, CE-118 was sparse's confident #1 and
dense's #2 → 1/61 + 1/62 = 0.03252. The gold TR-114 was dense's #1 but sparse's
#3 → 1/63 + 1/61 = 0.03227. The wrong passage takes the fusion by 0.00025. RRF
has no mechanism for noticing that one of its input lists is confidently wrong.

**Why dense didn't fail the code query.** Twelve passages is nowhere near enough
to reproduce the entity-centric weakness, which is documented over large
collections with rare entities. B09 states that limit out loud rather than
letting the viewer assume the chapter was wrong.

## Evidence discipline (DOUBLE-CHECK LAW) — full detail in SOURCES.md

| Claim | Basis | Verdict |
|---|---|---|
| Rare terms should outweigh common ones (IDF) | Spärck Jones (1972) | Implemented in `idf()`; shown in B03 |
| BM25 adds length normalisation and TF saturation over TF-IDF | Robertson & Zaragoza (2009) | Implemented and named on screen |
| Sparse loses paraphrases (the vocabulary gap) | Karpukhin et al. (2020) | **Measured** — B04, gold drops to rank 3 |
| Dense can lose exact codes / rare entities | Sciavolino et al. (2021) | **Not reproduced at this scale** — stated as a limit, not hidden |
| RRF = Σ 1/(k + rank), no weight tuning, k=60 | Cormack et al. (2009) | Implemented exactly; arithmetic shown in B08 |
| Hybrid improves "in general", with exceptions | Kamalloo et al. (2023/2024); Mandikal & Mooney (2024) | **Independently reproduced** — this run is one of the exceptions |

## Friction protected

- **Kept: the result that broke the story.** The easiest version of this reel
  ends with hybrid winning both queries and a tidy "combine your signals"
  lesson. The measured run says otherwise, and the reel leads with that. This is
  the single most important editorial decision in the build.
- **Kept: the failure the demo could NOT reproduce.** Not claiming dense failed
  the code query costs the reel a neat symmetry, but claiming it would have been
  fabrication. B09 names the scale limit instead.
- **Kept: the corpus as first designed.** It would have been easy to add more
  code-shaped decoys until dense stumbled. That is engineering the data to fit
  a claim, and it was not done.
- **Kept: one loss is not a verdict.** The reel does not swing to "hybrid is
  bad". It says fusion counts rather than reasons — which is exactly what the
  arithmetic shows.
- **Dropped: DPR's 9–19 point margin.** The chapter quotes it but explicitly
  warns against generalising it, since it was measured on paraphrase-style
  questions. Putting it beside a 12-passage run would invite that error.
- **Dropped: Fig. 01** (sparse vs dense vector shapes). No beat's claim rests on
  vector geometry; see SOURCES.md.

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B00/B01 establish the two kinds of match first)
- WORKED EXAMPLE ✓ (the chapter's own, executed rather than described)
- FALSIFIABILITY ✓ (B07/B08 — the method shown failing, with the arithmetic)
- SCAFFOLDED VIEWER TASK ✓ (B10 — find where YOUR hybrid is worse than its best
  single retriever, and show the rank arithmetic)
- FOUR BOOKENDS ✓ (intro, problem, summary, handoff + outro)
- NO-SOURCE-NO-VERDICT ✓ (every number is captured stdout; every concept cited)

## VERDICT: PASS

Beat sheet, code, encoder validation and captured runs reviewed against the
chapter before audio. Proceeding to Kokoro audio → Remotion render → compile at
4K → frame-level visual QC.
