# SOURCES.md — does-it-remember-or-just-pretend

Primary source: `07_does_it_remember_or_just_pretend.md` (the authored
script with inline `[VISUAL: …]` stage directions, narration lightly
revised — see "Corrections applied to narration" below) and
`07_narration_tts_ready.txt` (the condensed narration actually spoken,
split by beat). Both live in this folder.

## Scope (per established series convention)

Like `why-agents-fail` (STEM2) and `when-two-agents-disagree` (STEM6),
this is a **general conceptual explainer**, not a first-person account of
this project's own implementation. STEM-series videos don't need to match
the real product code (which now lives at `D:\Code\mycroft\verification-
layer`, not `accountability_layer` — see the channel's own prior
correction on this point). Every claim below is checked against standard
retrieval-augmented / long-term-memory system design, not against a
specific file or line reference.

## Corrections applied to narration

Per the house style note (first raised on STEM6's script, now a standing
convention for scripts drafted through this pipeline): the source script
repeated a "that's not X, it's Y" contrastive construction several times.
Three instances were lightly rewritten for natural spoken cadence — no
factual or structural content changed:

| # | Location | What changed |
|---|---|---|
| 1 | B01 (context window) | "That's not memory in any real sense. It's more like short-term working memory" → "Really, this is short-term working memory at best" |
| 2 | B01 (persistent memory) | "it's not the model recalling anything. It's a retrieval system quietly re-inserting…" → "the model isn't recalling anything. A retrieval system is quietly re-inserting…" |
| 3 | Closing line | "isn't more capable. It's just further away from anyone noticing…" → "is not more capable — it's just further from anyone noticing…" |

## Factual claims (DOUBLE-CHECK LAW)

| Beat | Claim | Verdict | Basis |
|------|-------|---------|-------|
| B01 | The context window is temporary working attention scoped to one conversation, and does not persist to a future session unless separately saved | ✓ | Standard, accurate description of how transformer-based chat models handle conversation state |
| B01 | Persistent memory is externally stored information, retrieved and re-inserted into a future prompt — not the model "recalling" anything internally | ✓ | Correct and precise; this is the standard architecture for retrieval-augmented memory (a separate store + a retrieval step feeding text back into context), not a claim about the model's internal weights changing |
| B02 | The dominant retrieval approach uses vector embeddings and nearest-neighbor similarity search | ✓ | Standard, widely-documented architecture (embedding models + vector databases) for both RAG and agent memory systems generally |
| B02 | Similarity of meaning is not the same property as truth, current relevance, or original correctness | ✓ | Correct and is the episode's central, load-bearing claim — follows directly from what a similarity metric is actually computing (semantic distance, not a truth value) |
| B02 | Vector retrieval has no built-in expiration, confidence, or provenance tracking | ✓ | Accurate as a description of the base mechanism (nearest-neighbor search over embeddings) — those three properties are not intrinsic to similarity search and must be added by a system built on top of it |
| B03 | The vegetarian/stale-preference scenario | ⚠ **illustrative** | A constructed, common-sense example, not a logged incident — declared here per DOUBLE-CHECK LAW, consistent with STEM2/STEM6's own precedent for constructed worked examples |
| B03 | Persistent memory has no built-in clock; decay/expiration must be actively designed, not assumed | ✓ | Correct — a raw vector store has no time-based decay unless a system explicitly adds one (e.g. a TTL, a recency weight, or a re-verification step) |
| B04 | False information saved to memory can resurface and be trusted in unrelated future sessions | ✓ | Follows directly from B02's mechanism: if a false statement is embedded and stored, it is retrievable by the same similarity process as any true one, with no mechanism distinguishing them |
| B05 | The multi-agent shared-contamination blind spot (from `when-two-agents-disagree`, STEM6) and stale/poisoned memory share the same structural shape — both are invisible to a detector that only fires on contradiction | ✓ | Direct logical parallel, not a new claim: STEM6 established that arbitration-by-disagreement cannot catch two agents agreeing on a shared bad source; the same reasoning applies here to one agent agreeing with its own past poisoned memory, since nothing contradicts it |
| B06 | Provenance, decay, and contradiction-handling are the three design responses that address the failure modes described | ✓ | Direct synthesis of B03/B04/B05's already-verified claims — provenance addresses "where did this come from," decay addresses staleness, contradiction-checking addresses new-vs-stored conflicts |
| B09 | The next problem concerns whether a system can be graded at all | ✓ | Matches this channel's own next-scripted reel, `youtube/STEM8/08_grading_the_machine.md` ("Grading the Machine"), confirming the tease is a real, already-scripted follow-up |

## Anti-staleness check (DOUBLE-CHECK LAW)

No model name, vendor, version number, or benchmark score appears in the
narration. Every mechanism described (context windows, vector similarity
retrieval, decay, provenance, contradiction-checking) is a general
architectural pattern, not tied to a specific product generation, so the
reel should not date.

## Simplifications (declared)

- **The vegetarian/stale-preference example (B03) and the poisoned-memory
  scenario (B04) are both illustrative**, not logged incidents from any
  real system.
- **"Vectors" and "similarity search" are described at the conceptual
  level** (semantic distance, nearest neighbors), not tied to a specific
  embedding model, distance metric, or vector database implementation.
- **The three design responses (B06) are presented as necessary, not as
  a complete or sufficient solution** — B05's blind-spot argument already
  establishes that none of the three (nor any of them together) closes
  the specific gap of an input that never contradicts itself.

## Content carried and cut

| Source | Status | Note |
|---|---|---|
| Title card (filing cabinet drawer, "it remembers you like aisle seats") | Not built as a literal beat | Carried thematically into B00's composer framing and the outro's callback; B00 is locked to `ClaudeComposerAsk` per COLD OPEN LAW |
| "Two Completely Different Things Called Memory" section | Carried | Becomes B01, doubling as the episode's framework/BLUF beat |
| "How Retrieval Actually Works" section | Carried | B02 |
| "The Two Failure Modes" section | Carried, split | B03 (stale) + B04 (poisoned) — each failure mode gets its own diagram rather than sharing one crowded hold |
| "Where You've Actually Seen This Before" section | Carried | B05, the falsifiability/connection beat |
| "What Responsible Memory Design Actually Requires" section | Carried | B06, the framework beat — three items map directly onto three rules |
| "The Actual Question" closing section | Carried, folded | Its core claim ("it retrieves; whether that deserves to be called memory depends on tracking") is folded into B07's verdict rather than given its own beat, since B06 already carries the load-bearing argument |
| Closing aphorism ("further away from anyone noticing…") | Carried, restructured | Rephrased per the narration-style correction above; the sentiment is preserved |
| Key Takeaways (6 bullets) | Carried, condensed to 3 | Compressed into the three-rule framework in B06/B07; takeaway 5 (the shared blind spot) is B05's entire dedicated beat rather than a fourth recap line |

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) is the planned narration engine. No
ElevenLabs, no FLUX, no paid services. No publishing — the master stays in
this folder. **Audio has not yet been generated as of this writing — see
PEDAGOGY.md, GATE P is PENDING.**
