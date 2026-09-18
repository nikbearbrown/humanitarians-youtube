# SOURCES — claude-rag-chunking

*"Where You Cut The Page." · RAG Foundations, Chapter 4 — Chunking Documents*
*DOUBLE-CHECK LAW record: what the source says, what the reel says, and every
correction applied in between.*

---

## Primary source

| Field | Value |
|---|---|
| Book | *RAG Foundations* — Vedanshu Daxesh Patel |
| Repo | `D:\ai1-cli-main` (the book's canonical repo — `metadata.yaml`) |
| Chapter | `chapters/04-chunking-documents.md` |
| Fact-check record | `chapters/04-chunking-documents.md.verified.json` |
| Verified | `true` — phase `fact_checked`, GATE 4, **0 discrepancies** |
| Verified by | Vedanshu Daxesh Patel, 2026-08-13 |

The chapter is a fact-checked artifact, so the verification burden here is not
re-deriving its claims but **not exceeding them** — the chapter is deliberately
careful about what is and is not settled, and the reel has to preserve that
care rather than flatten it into confident narration.

## Figures

| Source figure | Treatment |
|---|---|
| `images/chunking-documents-fig-01.png` / `.svg` — "Three chunking strategies compared" / "The same page, cut three ways" | **Rebuilt natively** as B05 (`ChunkThreeStrips`). Never embedded. REBUILD LAW. |

Rebuild notes, per REBUILD LAW's honesty clause:

- The source figure is **schematic** — its "text" is grey rules, not real
  prose, and it asserts no character counts. The rebuild is schematic in
  exactly the same way, so nothing quantitative was introduced that the source
  did not have.
- **Retint logged:** the source marks the severing cut in crimson (`#C8102E`-
  class). The rebuild uses Claude terracotta `#D97757`, because this is a
  FIDELITY-palette brand and terracotta is its one accent. The accent still
  lands on the same element — the cut that severs the sentence — so the
  figure's argument is unchanged.
- Captioned on screen, once, small: *"Redrawn (simplified) from the chapter's
  own Fig. 01 — retinted to the Claude palette; the severing cut is the one
  accent."*
- The source's three panel titles and three notes are carried **verbatim**:
  "Fixed character count" / "severs a sentence mid-word", "Paragraph & heading
  breaks" / "boundaries sit at real breaks", "Meaning-shift detection" /
  "boundary where meaning shifts".

No other image from the book is used. There are **zero pantry stills** in this
reel — see "VOX LAW" below.

## Sources the chapter itself cites, and how the reel uses them

| # | Source | Used in | How |
|---|---|---|---|
| 1 | Pinecone, *Chunking Strategies for LLM Applications* — https://www.pinecone.io/learn/chunking-strategies/ | B03 caption, B04 "common default" panel | Cited as **practitioner guidance**, for the SHAPE of the size tradeoff and for the modest-overlap default. No specific size or percentage is reproduced. |
| 2 | LangChain, `RecursiveCharacterTextSplitter` — https://docs.langchain.com/oss/python/integrations/splitters | B06 caption + narration | Named as **one illustrative example of the pattern**, with the chapter's own disclaimer carried over verbatim in substance: the category, not an endorsement of one library. |
| 3 | Zhong, Liu, Cui, Zhang & Qin, *Mix-of-Granularity* (COLING 2025) — arXiv 2406.00456 | B02 (background) | Supports "chunk granularity measurably affects downstream answer quality". Not named on screen — the reel makes the qualitative claim only. |
| 4 | Kreileder, Reisinger & Fischer, *Evaluating Chunking Strategies for RAG on Academic Texts* — arXiv 2607.01852 | B02 (background) | Part of the granularity-effect evidence the chapter surveys. Not named on screen. |
| 5 | Taiwo & Yusoff, *Evaluating Chunking Strategies for RAG in Oil and Gas Enterprise Documents* (CCSEIT 2026) — arXiv 2603.24556 | B02 (background) | Same. Establishes the effect is not confined to one domain. Not named on screen. |
| 6 | Bennani & Moslonka (2026), *A Systematic Analysis of Chunking Strategies for Reliable Question Answering* — arXiv 2601.14123 | **B04, named on screen** | The controlled study that found, in its tested setup, no measurable benefit from overlap and increased indexing cost. Cited under the figure. |

## Corrections and editorial decisions applied

Logged per DOUBLE-CHECK LAW — the register's value IS the rewrite.

1. **No chunk size is ever stated.** The chapter offers no specific token or
   character count and explicitly warns that any numbers from practitioner
   guidance are "illustrative of the shape of the tradeoff, not a universally
   correct setting." B03 therefore draws the axis with **the middle
   deliberately unmarked**, and its on-screen note says so in words. A
   recommended number would have been the single easiest thing to invent here
   and the source refuses to supply one.

2. **No overlap percentage is stated.** Same reasoning. B04 says "a small
   fraction of the chunk length" — the chapter's own hedge — rather than a
   figure.

3. **The overlap question is left unresolved, on purpose.** The chapter is
   explicit that "some overlap is good practice" is *not* settled the way the
   size tradeoff is. The reel could easily have flattened this into "use
   overlap, it helps." Instead B04 gives the practitioner default and the 2026
   study **equal panels, equal weight, and no winner marked**, neither panel
   takes the accent, and the narration says "hold this one loosely" aloud. The
   verdict artifact repeats the word "Unsettled." This is the reel's
   falsifiability beat.

4. **The 2026 study's finding is kept scoped.** The chapter says the study found
   no benefit *"in its tested setup."* The reel does not upgrade this into "overlap
   doesn't work." On screen it reads "no measurable benefit to answer quality;
   only increased indexing cost", attributed to that study by name — a finding,
   not a law.

5. **Named tools stay examples, not endorsements.** The chapter has a standing
   paragraph on this ("Named tools here (Pinecone, LangChain) are used as
   illustrative examples of the category of chunking approach, not as an
   endorsement of one product over any other"). B06's narration carries it in
   the register rather than reciting it: *"The pattern is the point, not the
   library."*

6. **The B02 match meter carries no number.** It fills part-way and stops, with
   the label "approximate match". The chapter claims a direction — a whole-
   document vector "can only match that single all-purpose vector
   approximately", and embedding more topics "dilut[es] the signal" — but no
   score. Putting a percentage on that bar would have been inventing a figure.

7. **Nothing version-dated was introduced.** No model names, no library
   versions, no counts that drift. The reel should not age.

8. **The worked example is the chapter's own**, not a substitute: the 40-page
   benefits manual, the question "How many vacation days do I get in my second
   year?", and all three outcomes (whole document / fixed count / paragraph and
   heading boundaries) are the chapter's §"Worked example: one manual, chunked
   three ways", compressed into the narration budget.

9. **The bridge is the chapter's own.** BVDT's closing line points at Chapter 5
   ("how do you search that many chunks fast?") because the chapter's own
   Bridge section does.

## VOX LAW — why this reel has zero stills

VOX LAW (parent `explainer` chassis): *a still is EVIDENCE, never texture*, and
*"a film whose evidence is text, code, or data should have ZERO vox beats, and
that is a correct outcome — not a gap, not a skipped pantry."*

Chapter 4's evidence is entirely text and diagrams: there is no photograph, no
archival record, and no physical artifact that any argument in it turns on. A
stock image of a document or a filing cabinet would fail the law's one
question — it could be swapped for any other image of the same subject without
changing what the beat proves. So every body beat is a native animated
illustration instead, and the reel ships with an empty pantry by design.

The book's own `pantry/` directory was checked: it holds research notes and
source markdown, not images. `images/` holds the chapter figures, of which
Fig. 01 is the only one for this chapter — and that one is rebuilt, not
embedded, per REBUILD LAW.

## Components

New this reel (GATE L: six searches, six genuine misses, **built rather than
slated** — which is the doctrine's prescribed resolution of a punt):

| Composition | Beat | 9:16 twin |
|---|---|---|
| `ChunkWholeDocVector` | B02 | `ChunkWholeDocVector916` |
| `ChunkSizeTradeoff` | B03 | `ChunkSizeTradeoff916` |
| `ChunkOverlapGuard` | B04 | `ChunkOverlapGuard916` |
| `ChunkThreeStrips` | B05 | `ChunkThreeStrips916` |
| `ChunkSeparatorLadder` | B06 | `ChunkSeparatorLadder916` |
| `ChunkThreeWays` | B08 | `ChunkThreeWays916` |

Plus `ChunkChrome.tsx` — a layout primitive, not a registered composition.
All six render inside Chapter 3's existing `EmbedChrome` `FigureFrame`, so the
two chapters cut together as one series.

**Note on the miss ledger.** `scene_search.py` only appends to
`TEMPLATE-MISSES.md` when invoked with `--reel <path>`, which these searches
were not, and no such file exists at the toolkit root. Nothing is outstanding
either way: a punt is discharged by *building* the component, and all six were
built, registered at both aspects, and added to `scenes.json` via
`./art scene-index` — which is the index anyone actually searches. Verified
renderable afterwards with `./art scenes --check` on each.

Reused unmodified (props only): `ClaudeComposerAsk` (B00, BHTF),
`BrutalistHesitantWriter` (B01), `ProblemPredictCard` (B07),
`ClaudeVerdictArtifact` (BVDT), `TitleOutroChannel` (BOUT).

## Determinism

Every beat is a pure function of its frame. The one component with a seeded
performance, `BrutalistHesitantWriter`, has its seed pinned in the beat sheet
(`claude-rag-chunking-b01`) — same seed, identical typing performance, forever.
No `Math.random` at render.

## Voice

Kokoro `am_onyx`, local, free. **$0.00 spent.** No paid API was called at any
point in this build.
