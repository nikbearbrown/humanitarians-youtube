# Friction Log: Week 1 (Phase 1)

**Project:** Mycroft — ECIS + Decision Scorecard


**Week:** June 29 – July 4, 2026

---

## 1. Focus of the week

- Proposal and system architecture for ECIS + Decision Scorecard.
- Dev environment setup and dependency installation.
- Codebase reading and architectural reformulation.
- Seam schema design and ingest scaffold.
- Data-source research for earnings call transcripts.
- Reformulation diagram (Claude artifact).
- Two Substack articles, both published:
  - "When the Earnings Call Ends"
  - "Your Data Has Two States"

## 2. What was tried, and what was expected

- **Architecture.** Proposal model: ECIS + Scorecard as a standalone system connecting to Mycroft externally, with Mycroft treated as a signal-emitting engine.
- **Trust loop.** Assumption: a trust/validation loop would need to be built from scratch.
- **Data.** Assumption: SEC EDGAR as a primary source of earnings call transcripts.
- **Stack.** Expectation: the proposed stack (Pydantic, sentence-transformers, ChromaDB) would install and run locally.
- **Pace.** Expectation: implementation code would start early in the week.

## 3. Points of resistance, and next steps taken

### Framing mismatch (load-bearing)
- **Repo reading:** read in its prescribed order, `_MANIFEST.md` → `SNICKERDOODLE.md` → `DOMAIN.md`. Tracing `package.json` showed two layers: Node for conformance/build, Python for recipes.
- **Finding:** Mycroft is not an external engine. It is a book of finance recipes governed by Snickerdoodle. Each recipe moves through a lifecycle: DRAFT → SPECIFIED → RUNNABLE-SAMPLE → RUNNABLE-LIVE → VERIFIED.
- **Consequence:** ECIS + Scorecard belong inside Mycroft as recipes, reusing the existing governance trust loop.
- **Next step:** build redirected before any code was written against the wrong model. Seam schema built to the corrected model.

### Urge to code first
- Time deliberately spent on gates, lifecycle, and provenance rules before implementing.
- Slower, but code written without them would not have passed conformance.

### Environment friction
- Part of the intended stack did not install cleanly.
- Offline stand-ins used instead:
  - a stdlib validator in place of Pydantic
  - a hashing-based embedder in place of sentence-transformers
- Prompted early design for graceful degradation when the full stack isn't present.

### Data sourcing
- SEC EDGAR provides 8-K earnings press releases, not call transcripts.
- Sourcing plan redirected toward a speaker-segmented transcript API. Not yet selected.

## 4. AI and other contributions: accepted, changed, rejected

### Gru (SDD session)
- Used to understand how the architecture fits together.
- Produced the SDD documenting the seam schema and ingest scaffold design.

### Claude
- Built the reformulation diagram: an interactive React component with a before/after toggle and a hoverable seam element.
- Insight came from the codebase reading; Claude handled the build.

## 5. Understood now, and still unresolved

### Understood
- **Where the project lives:** as recipes inside Mycroft's governance, not as a separate system.
- **The seam schema** is the contract that makes ECIS output the Scorecard's input.
- **Raw vs. verified:** data has exactly two states with one gate between them. The architecture enforces point-in-time integrity rather than leaving it to developer discipline.

### Unresolved
- Which transcript API to use. Decision needed early in Week 2.
- How messy real transcripts are: encoding issues, inconsistent speaker segmentation, and edge cases the stand-ins could not surface.
- What "guidance raised / lowered / maintained" actually means. This is a human decision, and extraction depends on it.
- Whether N≈50 is enough to resolve the question. The success criteria already allow an "inconclusive" verdict.
- Onboarding questions OQ-3 through OQ-7 still open.
