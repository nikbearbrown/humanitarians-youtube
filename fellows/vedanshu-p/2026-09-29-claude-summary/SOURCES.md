# SOURCES — claude-rag-every-fix-has-a-ceiling

*"Every Fix Has A Ceiling." · RAG Foundations, Chapters 7–9 — the summary*
*DOUBLE-CHECK LAW record.*

---

## What this reel is

A summary of three videos. It makes **no new measurements**. Every figure in the
body is the source reel's own component, passed that reel's own measured data
verbatim, with the video it came from named in the citation line.

| Source reel | Title | Chapter | Recapped as |
|---|---|---|---|
| `2026-09-22-claude-cli-rag-pipeline` | "Watch A Bug Name Its Own Stage." | 7 | B02 — `FaultSignatureTable` |
| `2026-09-22-claude-rag-prompt-construction` | "Labels Are Not Decoration." | 8 | B03 — `GroundingDrift` |
| `2026-09-29-claude-cli-rag-reranking` | "Reorder Is Not Retrieve." | 9 | B04 — `ShortlistReorder` |

Book: *RAG Foundations* — Vedanshu Daxesh Patel, `D:\ai1-cli-main`.
Folder dated **2026-09-29** per explicit instruction.

## The ONE idea

> Each of these three techniques does exactly what it promises and then stops.
> The pipeline names which stage broke; it does not repair it. Prompt assembly
> improves the odds; it does not compel the model. A re-ranker orders what it
> was handed; it cannot retrieve. None of them makes an answer true — they make
> being wrong traceable.

## Data provenance — every number traces to a sibling reel

**B02, from Chapter 7's `_run-diagnose.txt`:**

| stage broken | top chunk | right fact? | cited | grounded |
|---|---|---|---|---|
| none (healthy) | VA-101#0 | yes | VA-101#0 | yes |
| retrieve | SL-140#0 | NO | SL-140#0 | yes |
| augment | VA-101#0 | yes | none | yes |
| generate | VA-101#0 | NO | none | NO |

**B03, from Chapter 8's worked example** — the two-sentence answer, the first
traceable to `resignation-policy.pdf` and the second to nothing.

**B04, from Chapter 9's `_run-rerank.txt`:** the five-candidate shortlist for
"When am I allowed to change my health plan?", its re-ranked order, and the
totals — 0 promoted, 0 demoted across six questions, with `OE-300` absent from
the shortlist entirely.

Only four prop fields differ from the sources: `sparkLine` (reframed to carry
the ceiling), `verdict` and `caption` (reframed as a recap), and `citation`
(which now names the video the figure came from). **No measured value was
changed.** If a number here disagrees with the video it came from, this reel is
wrong.

## B05 — the one beat that is not a recap, and why it exists

Two of the three reels ran a **declared stand-in** at the centre of their demo:

* **Chapter 7** — `generate()` is a deterministic extractive reader, not a
  language model. It cannot produce a sentence absent from the prompt. That is
  what made the four-row fault table come out as cleanly as it did.
* **Chapter 9** — stage 2 is late interaction (MaxSim), not the cross-encoder
  the chapter is about. No cross-encoder checkpoint existed on this machine,
  `transformers` was absent, and there was no network.

Both reels declared this on screen. **A summary is precisely where such a
declaration gets dropped**, because the recap wants the clean result and not the
caveat attached to it. So B05 is built to carry the caveat forward: one tier for
what was genuinely measured, one for what stood in, with visibly unequal
evidence bars and a terracotta verdict saying both videos said so out loud.

Dropping that beat would have made this the most misleading reel in the series
rather than the most careful one.

## Corrections and editorial decisions applied

1. **No figure was re-styled to look more conclusive.** `ShortlistReorder`
   still reports a null (0 promoted, 0 demoted). `GroundingDrift` still keeps
   both sentences equally confident. The recap inherits each source's honesty
   rather than tidying it.
2. **The chapter citations stay with their chapters.** Lewis et al. (2020),
   Anthropic's prompting docs, Gao et al. (2023/2024) and the rest are cited on
   the beats that carry their claims, exactly as in the source reels. No
   citation was promoted to a broader claim than it supports.
3. **Nogueira & Cho's 27% is still absent.** It did not appear in the Chapter 9
   reel and it does not appear here — this series never ran a cross-encoder.
4. **The title is about limits, not a criticism.** B02–B04 each show the
   technique working before naming where it stops.
5. **No accuracy or benchmark number is claimed** for any technique.
6. **Nothing version-dated.**

## Components — zero new, by design

| Beat | Component | Origin | Modified? |
|---|---|---|---|
| B00, BHTF | `ClaudeComposerAsk` | house | props only |
| B01 | `BrutalistHesitantWriter` | house | props only |
| B02 | `FaultSignatureTable` | Ch. 7 reel | props only |
| B03 | `GroundingDrift` | Ch. 8 reel | props only |
| B04 | `ShortlistReorder` | Ch. 9 reel | props only |
| B05 | `EvidenceTiers` | Ch. 8 reel | props only — new content, existing component |
| BVDT | `ClaudeVerdictArtifact` | house | props only |
| BOUT | `TitleOutroChannel` | house | props only |

GATE L was satisfied without a single search, because the summary's whole
design is to replay components the viewer has already seen. Building anything
new here would have been the wrong instinct: a new figure in a recap is a new
claim.

`TitleOutroChannel`, not `ClaudeTitleOutro`: OUTRO-LOCK.md §Scope restricts the
locked card to `claude-liam-*` slugs; it hardcodes `@NikBearBrown` and renders
no subline, which would drop the author signature.

**B01 uses a SINGLE-TOKEN trigger** (`correct` → `easier to diagnose`).
`BrutalistHesitantWriter` matches whitespace-delimited tokens, so a multi-word
trigger fails silently and leaves the misconception on screen — the Chapter 8
build hit exactly that and it is recorded in that reel's `_qc/REPORT.md`.

## VOX LAW — zero pantry stills, and that is the correct number

No photographic stills, and none were fetched. VOX LAW holds that a still is
evidence, never texture. This reel's evidence is three previously-measured
figures and one honesty table — there is no beat whose evidence is an image, so
a pantry still could only be decoration. No image file enters the render.

## Determinism

Every beat is a pure function of its frame; no `Math.random` at render.
`BrutalistHesitantWriter` is seeded
(`claude-rag-every-fix-has-a-ceiling-b01`), so the typing performance is
identical on every render. The recapped data is static, so this reel has no
run-to-run variance at all — unlike the Chapter 9 source, whose timings shift a
few percent between runs.

## Voice

Kokoro `am_onyx`, local, free. **$0.00 spent.** No paid API, no network call.
