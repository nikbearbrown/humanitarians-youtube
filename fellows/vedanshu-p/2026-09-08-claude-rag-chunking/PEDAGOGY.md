# PEDAGOGY — Where You Cut The Page. (personal-author ai-explainer)

Concept explainer of *RAG Foundations*, Chapter 4 ("Chunking Documents for
Retrieval"). Vox-style `ai-explainer` build — NOT skill-teardown, NOT profile,
NOT audit. Personal author channel: persona and sign-off are the book's author,
Vedanshu Daxesh Patel (`@VedanshuDaxeshPatel`), voice Kokoro `am_onyx` ("Onyx"),
free. IN-FOR-BEAR LAW does not apply — the narrator is named as themself in B00
and signs off as themself in BOUT. Never publishes; master is written to the
render target, working cut stays beside the reel.

**Book root note.** Built into `D:\ai1-cli-main\youtube\`, the book's canonical
repo, per CLAUDE.md rule 3 ("videos travel with their book"). Folder dated
**2026-08-26** per explicit instruction — independent of the chapter's own
fact-check date (2026-08-13) and of the session's calendar date.

**Direct predecessor:** `2026-09-01-claude-rag-embeddings` ("Meaning, As A
Number.", Chapter 3). This reel picks up its closing thread — embeddings let a
computer compare meaning, but over a piece of text *of what size?* — which is
the question Chapter 4 opens on.

## The ONE idea

> Chunking is a design decision, not a preprocessing step. Where you cut a
> document decides what retrieval can find.

Everything is built to land that. It is also the chapter's own closing
sentence, which is why it is the correction the hesitant writer makes in B01.

## Act structure

- **B00 cold open** — `ClaudeComposerAsk`, RESULT lines answered (COLD OPEN
  LAW). Bridges from Chapter 3's result into Chapter 4's open question: a piece
  of text of *what size*?
- **B01 executive summary (BLUF)** — `BrutalistHesitantWriter` per the current
  EXECUTIVE-SUMMARY LAW. The writer types *"Chunking is preprocessing."*, stops,
  and corrects `preprocessing` → `a design decision`.
  **The correction is the reel's actual misconception**, taken from the
  chapter's own closing contrast between "a mechanical preprocessing step" and
  "a real design decision with consequences" — not a synonym swap for texture.
  Read back with the replacement applied, the full text stands alone as the
  reel's claim: *"Chunking is a design decision. Where you cut a document
  decides what retrieval can find."*
  Audio window 11.01s (law floor: 9s), explicit `lead_silence_s: 0.8`, seed
  pinned per reel.

  *Note on the predecessor:* the Chapter 3 reel rendered B01 as the static
  `ProblemExecutiveSummary` card. That rendering rule has since been superseded
  — beat 2 is the writer, not a card — so this reel follows the current law
  rather than copying the sibling.

- **B02–B08 body** — seven illustrated beats, ILLUSTRATE LAW: no Claude UI
  anywhere in the body, no two consecutive beats sharing a visual scheme:
  - B02 `ChunkWholeDocVector` (new) — the whole-document collapse. Five topic
    bands converge into one dot; the query's match meter fills part-way and
    stops.
  - B03 `ChunkSizeTradeoff` (new) — the failure at BOTH ends of the size axis,
    with the middle deliberately unmarked.
  - B04 `ChunkOverlapGuard` (new) — **the falsifiability beat.** A fact severed
    at a seam, rescued by an overlap window; then the split verdict, both
    readings held at equal weight.
  - B05 `ChunkThreeStrips` (new) — rebuilds the chapter's own Fig. 01, the
    three strips of one page cut three ways.
  - B06 `ChunkSeparatorLadder` (new) — the prioritized separator fallback,
    lighting top-down.
  - B07 `ProblemPredictCard` (shared, unmodified) — commit before the reveal.
  - B08 `ChunkThreeWays` (new) — resolves B07 with the chapter's own worked
    example: one manual, one question, three outcomes, held side by side.
- **BVDT verdict** — `ClaudeVerdictArtifact`, five lines, each traceable
  (NO-SOURCE-NO-VERDICT), closing on the chapter's own bridge to Chapter 5.
- **BHTF handoff** — `ClaudeComposerAsk`, greeting `Your turn.`, a prompt built
  from the chapter's Exercise 1, read aloud verbatim and then discussed
  (HANDOFF LAW).
- **BOUT outro** — `TitleOutroChannel`, exact title restate,
  `@VedanshuDaxeshPatel` handle, `Vedanshu Daxesh Patel` signature subline
  (OUTRO LAW).

  **Why not `ClaudeTitleOutro`:** OUTRO-LOCK.md §Scope restricts that card to
  `claude-liam-*` slugs and states other channels "have their OWN outros and
  NEVER get this card, handle, or mascot." Its handle is now hardcoded to
  `@NikBearBrown` with no prop and it never renders a subline — so using it
  would both break the lock's scope and drop the author signature.
  `TitleOutroChannel` is the sanctioned own-channel counterpart: same
  title-restate form, handle as a prop, subline reserved for exactly this
  author credit. (The predecessor reel rendered before that lock landed, which
  is why its outro looks like this one despite naming the other component.)

## Evidence discipline (DOUBLE-CHECK LAW) — see SOURCES.md for full citations

| Claim | Source | Verdict |
|---|---|---|
| A whole document embedded as one vector averages every topic it contains, so a specific query matches only approximately | Ch. 4 §"Why whole-document embedding loses precision"; granularity studies surveyed there | Direction asserted, no score — the reel puts no number on the match meter |
| Chunk granularity measurably affects downstream answer quality, across domains | Zhong et al. (COLING 2025); Kreileder et al.; Taiwo & Yusoff (CCSEIT 2026) | Qualitative claim only; papers not named on screen |
| Too small loses context; too large loses precision | Ch. 4 §"Chunk size"; Pinecone | Both directions kept — the symmetry IS the point |
| There is no universally correct chunk size | Ch. 4, explicit | **Preserved as a refusal.** B03's axis has no recommended midpoint |
| Overlap guards a fact straddling a boundary | Ch. 4 §"Overlap between chunks" | Rationale kept |
| A 2026 controlled study found no measurable benefit from overlap, only higher indexing cost | Bennani & Moslonka (2026), arXiv 2601.14123 | **Named on screen.** Kept scoped to "its tested setup" — not upgraded into "overlap doesn't work" |
| Structure-aware splitting keeps semantically related text together | Ch. 4 §"Structure-aware chunking" | Verified |
| Tooling tries a prioritized separator list, falling back only when a chunk would be oversized | Ch. 4; LangChain `RecursiveCharacterTextSplitter` | Named as an illustrative example of the pattern, per the chapter's own disclaimer |
| Fig. 01 — the same page cut three ways | `images/chunking-documents-fig-01.svg` | Rebuilt natively as B05; no screenshot used |
| The worked example (40-page manual, second-year vacation days, three outcomes) | Ch. 4 §"Worked example" | Used as B07/B08's scenario, compressed to budget; no invented retrieval scores |

## Friction protected

- **Kept: the unsettled overlap question (B04), unresolved.** This is the
  reel's hardest editorial call and the one most worth defending. The easy cut
  is "use a small overlap, it helps" — clean, actionable, and exactly what the
  chapter refuses to say. B04 instead gives the practitioner default and the
  2026 study equal panels, denies both the accent colour, and has the narration
  say "hold this one loosely" out loud. An explainer that resolved this would
  be teaching false confidence about the very design decision it is about.
- **Kept: no numbers anywhere.** No chunk size, no overlap percentage, no
  similarity score. The chapter's position is that specific numbers are
  illustrative of a shape, not correct settings, and the fastest way to betray
  that would have been a tidy "512 tokens, 10% overlap" card. B03 marks its
  axis ends and leaves the middle blank on purpose.
- **Kept: the tools-are-examples disclaimer.** Carried in the register
  ("The pattern is the point, not the library") rather than recited.
- **Compressed for time**: the chapter's Exercise 1 asks for chunking
  strategies for two document types (a short FAQ page, a 40-page policy PDF).
  Rather than spending two body beats on hypotheticals, BHTF hands the viewer
  the stronger personalized version — bring a document *you* actually work
  with — and adds the argue-the-opposite-case move, which is what turns it from
  a quiz into a judgment exercise.
- **Dropped**: Exercise 2 (the FAQ page chunked with large arbitrary chunks).
  It makes the same point as B08's fixed-count row, and repeating it would have
  pushed the reel past its useful length without adding a distinction.

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01 BLUF states the design-decision frame;
  B02–B06 build the mechanism; the worked example does not arrive until B07/B08)
- WORKED EXAMPLE ✓ (B07/B08 — the chapter's own manual, question, and three
  outcomes, run through predict-then-reveal)
- FALSIFIABILITY ✓ (B04 — overlap's payoff is explicitly unsettled, with the
  counter-evidence named and given equal weight)
- SCAFFOLDED VIEWER TASK ✓ (BHTF — the viewer's own document, plus a forced
  counter-argument and a ranking of the two failure modes)
- FOUR BOOKENDS ✓ (cold open, BLUF, verdict, handoff + outro)
- NO-SOURCE-NO-VERDICT ✓ (every BVDT line traces to the table above)

## VERDICT: PASS

Beat sheet and this document reviewed against the chapter (fact-checked
2026-08-13, GATE 4, 0 discrepancies) before audio. Proceeding to Kokoro audio →
Remotion render → compile at 4K → frame-level visual QC.
