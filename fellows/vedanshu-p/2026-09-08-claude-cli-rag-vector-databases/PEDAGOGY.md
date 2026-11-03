# PEDAGOGY — Watch Exact Search Hit A Wall. (personal-author cli-explainer)

CLI explainer of *RAG Foundations*, Chapter 5 ("Vector Databases and
Approximate Nearest-Neighbor Search"). Built with the **`cli-explainer`** skill
— the build-with-Claude loop, not the vox-style `ai-explainer` used for
Chapters 3 and 4.

**Tier note.** `cli-explainer` is ADVANCED tier ("Bear only" in CLAUDE.md's
table). It was invoked here by explicit human request. Nothing about the build
escalates tier in any other sense: it runs entirely on the free path (Kokoro
`am_onyx`, Remotion, local numpy), spends $0.00, and calls no paid API.

Personal author channel: persona and sign-off are the book's author, Vedanshu
Daxesh Patel (`@VedanshuDaxeshPatel`). IN-FOR-BEAR LAW does not apply — the
narrator is named as themself in B00 and signs off as themself in B11.
Never publishes.

**Book root.** Built into `D:\ai1-cli-main\youtube\`, per CLAUDE.md rule 3.
Folder dated **2026-09-08** per explicit instruction, independent of the
chapter's own fact-check date and of the session's calendar date.

**Siblings.** `2026-08-26-claude-cli-rag-embeddings` (Ch. 3 CLI) set the spine
this follows. The Ch. 4 `ai-explainer` (`2026-08-26-claude-rag-chunking`) is the
concept-side counterpart; this reel shares its chrome (`EmbedChrome`) and its
beat clock (`ChunkChrome`), so the series cuts together.

## The ONE idea

> Exact search is correct and doesn't scale. An index narrows the search space
> instead of scanning it — and the accuracy you give up is a setting you choose,
> measure, and can move.

## Why this chapter suits a CLI video

Chapters 3 and 4 argued about meaning and structure — ideas better carried by
illustration. Chapter 5's claim is about **cost**, and cost is measurable. A CLI
video can therefore do something an explainer cannot: rather than asserting that
brute force scales linearly and an index doesn't, it can build both, run both,
and put the measured numbers on screen. The chapter's own hedge — "the
qualitative shape of the argument is what carries the point, not any specific
timing numbers" — is satisfied by plotting comparison counts, which are
machine-independent, while still showing real milliseconds where the felt cost
is the point.

## Act structure (the mandatory CLI spine)

- **B00 INTRO** — `ClaudeComposerAsk`, ask shown answered (COLD OPEN LAW).
  Bridges Ch. 3's embeddings and Ch. 4's chunks into Ch. 5's question.
- **B01 PROBLEM** — `RagExecutiveSummary`. The stakes, stated before any prompt
  exists: exact search never misses, and that is exactly why it doesn't scale.
  Mandatory beat; no code yet.
- **B02 CLI → B03 CODE → B04 OUTPUT** — cycle 1, the naive version.
  `brute_force_search.py` is real, and B04 is its real stdout: 0.08 → 1.16 →
  10.87 ms as the collection goes 1k → 10k → 100k.
- **B05 CLI → B06 CODE → B07 OUTPUT** — the revision (THE REVISION LAW).
  The revised prompt asks for an inverted-file index **and for recall to be
  reported**, which is the beat's real teaching move: the ask itself models
  measuring what a shortcut costs. B07 rebuilds the chapter's Fig. 01 from the
  measured run.
- **B08 OUTPUT (second result, same run)** — the dial. Recall against share of
  the collection compared, four measured settings.
- **B09 SUMMARY** — the lesson, plus the honest caveat about IVF vs HNSW.
- **B10 NEXT STEPS** — `ClaudeComposerAsk`, `"Your turn."` (HANDOFF LAW).
- **B11 OUTRO** — `TitleOutroChannel`, exact title restate, signature.

## Evidence discipline (DOUBLE-CHECK LAW) — full detail in SOURCES.md

| Claim | Basis | Verdict |
|---|---|---|
| Exact search compares against every stored vector and its cost tracks collection size | Ch. 5; Malkov & Yashunin (2018) | **Measured** — B04, 10× data → ~9.4× time |
| Classical exact indexes stop helping in high dimensions | Ch. 5; Indyk & Motwani (1998) | Stated in B01's framing; not demonstrated (out of scope for one build) |
| An index makes per-query cost grow far more slowly | Ch. 5 | **Measured** — B07, 100× data → 10.5× comparisons |
| The speed/accuracy tradeoff is tunable and quantifiable | Ch. 5; ANN-Benchmarks (2018/2020) | **Measured** — B08, four settings, recall 0.33 → 0.96 |
| ANN means "estimate well enough, fast enough", not "silently return garbage" | Ch. 5 | Carried by B08 showing recall as a known number at every setting |
| HNSW is one illustrative family, not the only answer | Ch. 5, explicit | Preserved — B09 names that the demo built IVF instead |

## Friction protected

- **Kept: the method shown failing first.** B08 opens on `nprobe 1` recovering
  33% of the true neighbours before climbing to 96%. The tempting cut is to show
  only the good row. Showing the bad one is what makes the dial a dial rather
  than a sales pitch — and it is the chapter's actual position, which is that the
  error is *bounded and adjustable*, not absent.
- **Kept: the IVF-vs-HNSW mismatch, said out loud.** The reel could have quietly
  let viewers assume the code was HNSW, since the chapter walks through HNSW. It
  names the difference in B09 instead. The chapter explicitly licenses a
  different family; the viewer still gets told.
- **Kept: comparison counts as the headline metric.** Milliseconds flatter or
  punish an implementation for reasons that have nothing to do with the
  algorithm. Comparisons per query are what the chapter's cost argument is
  about, so that is what B07 plots.
- **Dropped: Figure 02.** The chapter's HNSW layer diagram is not rebuilt,
  because this reel's code builds flat cells and drawing a hierarchy beside it
  would misrepresent the demo. See SOURCES.md §2.
- **Dropped: product quantization and LSH.** Named in the chapter as other
  families; including them would have added a third cycle without changing the
  lesson.

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01 states the cost problem before any code)
- WORKED EXAMPLE ✓ (the body is an executed example, not a described one)
- FALSIFIABILITY ✓ (B08 measures the recall the index loses, at four settings)
- SCAFFOLDED VIEWER TASK ✓ (B10 — sweep the dial on your own data and find the
  query where it first breaks)
- FOUR BOOKENDS ✓ (intro, problem, summary, handoff + outro)
- NO-SOURCE-NO-VERDICT ✓ (every number traces to a captured run; every concept
  to the chapter or a source it cites)

## VERDICT: PASS

Beat sheet, code, and captured runs reviewed against the chapter before audio.
Proceeding to Kokoro audio → Remotion render → compile at 4K → frame-level
visual QC.
