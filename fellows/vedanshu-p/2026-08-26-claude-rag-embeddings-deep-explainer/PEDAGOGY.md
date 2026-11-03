# PEDAGOGY — The Geometry Of Meaning. (deep-explainer, personal author channel)

`deep-explainer` build (per `skills/make/deep-explainer/SKILL.md`) of *RAG
Foundations*, Chapter 3 ("Representing Text: Embeddings and Semantic
Similarity") — the 6-act documentary treatment of the same source as the
sibling ai-explainer (`2026-08-26-claude-rag-embeddings`) and cli-explainer
(`2026-08-26-claude-cli-rag-embeddings`) reels. Personal author channel:
Kokoro `am_onyx` ("Onyx"), signed `@VedanshuDaxeshPatel` throughout.
IN-FOR-BEAR LAW does not apply.

**Tier note.** `deep-explainer` is listed ADVANCED (Bear-only) in this
toolkit's root `CLAUDE.md`, rule 8 — same tier as `cli-explainer`. Built on
the requester's direct, explicit instruction, applying the same
precedent-based reasoning already surfaced and confirmed earlier in this
session: this book already has two shipped sibling deep-explainer reels
(`2026-08-12-claude-rag-deep-explainer`, Chapter 1; and
`2026-08-19-claude-rag-the-problem-deep-explainer`, Chapter 2).

## Act structure (the plan, approved via plan mode before authoring)

Six acts, 30 body beats + 4 bookends (B00 cold open, BVDT verdict, BHTF your
turn, BOUT outro) = 34 beats total:

- **I — From Words To Numbers** (B01–B05): a computer needs a vector, not
  words; word2vec learns one from an enormous corpus, purely from context —
  no dimension is hand-assigned.
- **II — The Trick That Almost Works** (B06–B10): king − man + woman ≈
  queen — and the honest replication caveat (exclude the query word, or
  the nearest vector is just "king" again). The episode's falsifiability
  beat.
- **III — From Words To Whole Passages** (B11–B15): word2vec is word-level,
  not what RAG embeds; BERT's raw output compares sentences poorly;
  Sentence-BERT fixes it, with the real 65-hours-to-5-seconds figure.
- **IV — Closeness As Meaning, An Old Idea** (B16–B21): cosine similarity's
  actual geometry, and its pedigree — a classical-IR tool, decades older
  than embeddings, now applied to a much richer vector.
- **V — The Worked Example: Same Words, Different Meaning** (B22–B26): the
  chapter's central payoff — a paraphrase pair (few shared words) should
  land close; a shared-phrase trap pair (same opening words, different
  topic) should land far apart. Stated qualitatively, exactly as the
  chapter itself insists.
- **VI — Meaning Over Vocabulary** (B27–B30): the payoff stated plainly —
  retrieval needs proximity, not matching words — and an honest bridge to
  Chapter 4's "what is a chunk" question, named but not resolved here.

Lane mix (body, 30 beats): CARD 3 (10.0%) · VOX 7 (23.3%, two 2-beat runs +
three singles) · MANIM 8 (26.7%) · REMOTION 12 (40.0%, 11 of which reuse
`ProblemExecutiveSummary`, 1 reuses `EmbedSpeedLeap` — both already
registered from sibling builds) — all within the doctrine's lint bands
(vox 15–30%, manim 25–40%, remotion 30–45%; see SKILL.md THE BEAT-MIX
CONTRACT).

## Continuity (the vox-run contract)

Two runs, both length 2 (well under the max of 3), neither crossing an act
boundary: **R1** (B02 opener with `handoff`, B03 closer) in Act I —
library shelves to an open book's printed text. **R2** (B17 opener with
`handoff`, B18 closer) in Act IV — a card-catalog wall to one open drawer.
The three other VOX beats (B12, B23, B29) are single stills, not runs —
legal per SKILL.md (kenburns singles, not repeated holds).

## Evidence discipline (DOUBLE-CHECK LAW) — see FACTCHECK.md for the full table

All nine factual rows trace to the same five citations used in the sibling
ai-explainer reel, or to the chapter's own text. The one place this genre's
extra runtime creates real risk — inventing a precise number for the
worked example just because there's more screen time to fill — is
explicitly avoided: B22–B26 and BVDT state the paraphrase/trap comparison
qualitatively only, matching the chapter's own caveat that no embedding
model was actually run to produce a score for that example. B09/B10's
replication caveat likewise states only the qualitative finding (excluding
the query word matters), no invented statistics.

## Friction protected

- **Kept**: both vox runs (R1, R2) — the establishing/close pairing earns
  its two beats each: R1 grounds "a vocabulary learned from ordinary text"
  in something visible; R2 grounds "an idea older than embeddings" in a
  real documentary object (the card catalog).
- **Kept**: the honest, unresolved bridge at B30/BVDT — Chapter 3 opens a
  question (what counts as one chunk) it does not answer, and manufacturing
  an answer here would be a NO-SOURCE-NO-VERDICT violation.
- **Kept**: B26 as a fresh Manim scene rather than reusing the ai-explainer
  sibling's `EmbedRevealPairs` Remotion component for the same Fig. 02
  rebuild — the geometric callback to B19's cosine-angle treatment adds
  real pedagogical value (grounding "close/far" in actual coordinates) that
  a second Remotion pass wouldn't add on its own.
- **Removed for scope**: a seventh act walking through the chapter's own
  two exercises verbatim — BHTF's handoff already runs an equivalent
  scaffolded reasoning task on the viewer's own material, restated in this
  reel's own words rather than lifted from the chapter, which is the
  stronger version of the same exercise.

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01 states "text must become a learned
  vector" before any mechanism or example)
- WORKED EXAMPLE ✓ (B22–B26 — the paraphrase pair vs. the shared-phrase
  trap pair, the chapter's own central worked example)
- FALSIFIABILITY ✓ (B09/B10 — vector arithmetic's own honest failure mode
  when the query word isn't excluded)
- SCAFFOLDED VIEWER TASK ✓ (BHTF hands the viewer the same close-vs-far
  reasoning task, restated for a topic of their own choosing)
- FOUR BOOKENDS ✓ (cold open, verdict, handoff, title-restate outro)
- NO-SOURCE-NO-VERDICT ✓ (every claim in BVDT traces to FACTCHECK.md; B30
  names the open "what is a chunk" question without asserting an answer)

## VERDICT: PASS

Approved 2026-08-26 — Vedanshu Daxesh Patel reviewed `beat_sheet.json`,
`scenes.py`, and this document and signed off. Proceeding to Part B: audio
(Kokoro) → align (word clock) → `SHOPPING.md` (Gate D2, after audio lock)
→ Gate D1 previz → visual QC on every rendered (non-slate) beat. The seven
VOX beats stay labeled slates until real stills land in `pantry/` — that is
Gate D1's correct, honest first deliverable, not a shortfall.
