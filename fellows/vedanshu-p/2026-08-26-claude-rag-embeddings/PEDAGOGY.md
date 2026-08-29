# PEDAGOGY — Meaning, As A Number. (personal-author ai-explainer)

Concept explainer of *RAG Foundations*, Chapter 3 ("Representing Text:
Embeddings and Semantic Similarity"). Vox-style `ai-explainer` build — NOT
skill-teardown, NOT profile, NOT audit. Personal author channel: persona and
sign-off are the book's author, Vedanshu Daxesh Patel (`@VedanshuDaxeshPatel`),
voice Kokoro `am_onyx` ("Onyx"), free. IN-FOR-BEAR LAW does not apply — the
narrator is named as themself in B00 and signs off as themself in BOUT.
Never publishes; master stays in this reel folder.

**Book root note.** This reel is built into `D:\ai1-cli-main\youtube\`, the
book's canonical repo (confirmed via `metadata.yaml`: title "RAG
Foundations", author "Vedanshu Daxesh Patel") — not the
`C:\Users\vedan\Downloads\ai1-cli-main` copy used for the Chapter 1–2 reels
earlier this session, per the human's explicit path this time and CLAUDE.md
rule 4 ("videos travel with their book"). Folder dated 2026-08-26 per
explicit instruction.

## Act structure

- **B00 cold open** — `ClaudeComposerAsk`, RESULT lines answered (COLD OPEN
  LAW). Bridges directly from Chapter 2's closing requirement ("the right
  text") into Chapter 3's question ("how does a computer even tell what's
  'about the same thing'?").
- **B01 executive summary (BLUF)** — reuses `ProblemExecutiveSummary`
  (built for the Chapter 2 ai-explainer reel), props-only: the whole idea
  in one breath before any specific.
- **B02–B09 body** — eight illustrated beats, ILLUSTRATE LAW: no Claude UI,
  each a bespoke C3 illustration or a shared pedagogy device (no two
  consecutive beats share a visual scheme):
  - B02 `EmbedScatterPlot` (bespoke) — word2vec, rebuilds Fig. 01.
  - B03 `EmbedVectorArithmetic` (bespoke) — king − man + woman ≈ queen,
    WITH the chapter's own replication caveat on screen, not softened.
  - B04 `EmbedWordToPassage` (bespoke) — BERT (raw) → Sentence-BERT.
  - B05 `EmbedSpeedLeap` (bespoke) — the real, cited 65-hours-to-5-seconds
    figure (the one beat in this reel with a real number on screen, since
    the chapter cites it as the paper's own reported result, not a
    qualitative-only claim).
  - B06 `EmbedCosineSimilarity` (bespoke) — angle between two vectors.
  - B07 `ProblemExecutiveSummary` (reused, second use, different props) —
    the payoff: meaning, not vocabulary.
  - B08 `ProblemPredictCard` (shared, unmodified) — commit before the
    reveal, using the chapter's own worked-example phrasing.
  - B09 `EmbedRevealPairs` (bespoke) — rebuilds Fig. 02, resolves B08.
- **BVDT verdict** — `ClaudeVerdictArtifact`, four claims, each traceable to
  a cited source (NO-SOURCE-NO-VERDICT).
- **BHTF handoff** — `ClaudeComposerAsk`, greeting `Your turn.`, a prompt
  adapted from the chapter's own Exercise 1/2, read aloud and discussed
  (HANDOFF LAW).
- **BOUT outro** — `ClaudeTitleOutro`, exact title restate,
  `@VedanshuDaxeshPatel` handle, `Vedanshu Daxesh Patel` byline subline
  (OUTRO LAW).

## Evidence discipline (DOUBLE-CHECK LAW) — see SOURCES.md for full citations

| Claim | Source | Verdict |
|---|---|---|
| Word2vec learns per-word vectors from a 1.6B-word corpus, purely from context patterns | Mikolov et al., 2013 (arXiv:1301.3781) | Verbatim to the paper's own description |
| king − man + woman ≈ queen, but depends on excluding the query word from the search | Mikolov, Yih & Zweig, 2013; later replication work | Caveat preserved on screen, not dropped — this IS the chapter's own honesty move |
| BERT raw output performs poorly for whole-sentence comparison; Sentence-BERT fixes this | Devlin et al., 2019; Reimers & Gurevych, 2019 | Verified against both papers' own framing |
| ~65 hours (raw BERT) → ~5 seconds (Sentence-BERT) for finding the most similar pair among 10,000 sentences, comparable accuracy | Reimers & Gurevych, 2019 | Real, cited number from the paper's own results — checked against the paper, not just the chapter's restatement |
| Cosine similarity predates embeddings, from the classical vector space model of IR | Manning, Raghavan & Schütze, 2008 | Verified — a standard textbook citation |
| Fig. 01 (word2vec 2D cluster) and Fig. 02 (question-pair embedding sketch) | chapters/03-representing-text-embeddings.md, Figures 01/02 | Rebuilt natively as B02/B09; no screenshot used |
| The worked example (vacation/PTO close, "how do I request" pair far) | chapter's "Worked example" section | Used as B08/B09's scenario; no invented similarity score — the chapter explicitly says none was computed |

## Friction protected

- **Kept**: the vector-arithmetic caveat (B03) in full, rather than
  simplifying "king − man + woman ≈ queen" into a clean, unqualified fact —
  the chapter itself treats this as the central example of DOUBLE-CHECK
  LAW discipline, and cutting the caveat would undo exactly what the
  chapter is modeling.
- **Kept**: the real 65-hours/5-seconds figure (B05) rather than converting
  it to a vaguer "much faster" — this is a genuinely verifiable, cited
  number from the paper, unlike Chapter 2's qualitative-only cases.
- **Removed for time**: the chapter's own Exercise 1 (three phrases,
  predict pairwise closeness) is not reproduced as a full separate
  three-way beat — B08's predict beat uses two of the three phrases from
  that exercise, and BHTF's handoff explicitly invites the viewer to bring
  their own three phrases, which is the stronger, personalized version of
  the same exercise.

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01 BLUF states the vector/closeness frame
  before B02–B06 supply mechanism, B07–B09 supply the payoff and example)
- WORKED EXAMPLE ✓ (B08/B09 — the vacation/PTO vs. request-time-off/laptop
  pairs, run through predict-then-reveal)
- FALSIFIABILITY ✓ (B03's caveat: the famous vector-arithmetic result does
  NOT reliably hold without a specific extra step — a genuine boundary
  condition, not just a "works great" claim)
- SCAFFOLDED VIEWER TASK ✓ (BHTF handoff asks the viewer to bring their own
  three phrases and check their intuition against the chapter's framework)
- FOUR BOOKENDS ✓ (cold open, BLUF, verdict, handoff+outro)
- NO-SOURCE-NO-VERDICT ✓ (every claim in BVDT traces to a cited source above)

## VERDICT: PASS

Approved 2026-08-26 — Vedanshu Daxesh Patel reviewed `beat_sheet.json` and
this document and signed off. Proceeding to Part B (Kokoro audio → render
→ compile at 4K → visual QC).
