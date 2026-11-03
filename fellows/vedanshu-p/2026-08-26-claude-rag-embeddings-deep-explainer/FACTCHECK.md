# FACTCHECK — The Geometry Of Meaning.

| # | Claim (beat) | Source | Verdict |
|---|---|---|---|
| 1 | Word2vec trains a neural network over a corpus of 1.6 billion words, learning a vector of a few hundred continuous numbers per word such that words used in similar contexts get similar vectors — nobody hand-assigns the numbers (B02–B05) | Mikolov, Chen, Corrado & Dean, 2013 (arXiv:1301.3781) | ✅ — verified; the 1.6B-word figure and "learned, not assigned" framing are the paper's own |
| 2 | king − man + woman lands close to the vector for queen — a famous illustration that *directions* between vectors can encode relationships (B07, B08) | Mikolov, Yih & Zweig, 2013, NAACL-HLT (aclanthology.org/N13-1090) | ✅ — verified as the paper's own illustrative result |
| 3 | Later replication work found this specific result depends on excluding the query word from the nearest-vector search — without that step, the closest vector to "king − man + woman" is often just "king" again (B09, B10) | chapters/03-representing-text-embeddings.md, "Text, turned into a vector" section (the chapter's own stated caveat) | ✅ — the chapter itself states this as the reason to hold the example "loosely"; no specific replication paper is named by the chapter, so B09/B10 assert only the qualitative finding, no invented statistics |
| 4 | Word2vec operates at the word level, not the passage level; BERT learns deep, contextual representations, but its raw output compares whole sentences poorly; Sentence-BERT restructures BERT so a passage becomes one directly-comparable vector (B11–B13) | Devlin, Chang, Lee & Toutanova, 2019, NAACL-HLT (arXiv:1810.04805); Reimers & Gurevych, 2019, EMNLP-IJCNLP (arXiv:1908.10084) | ✅ — both real, checkable papers; the word-vs-passage distinction and the "poor when used directly" framing are the chapter's own, matching Reimers & Gurevych's stated motivation |
| 5 | Sentence-BERT cuts the time to find the most similar pair among 10,000 sentences from roughly 65 hours with raw BERT to about 5 seconds, at comparable accuracy (B14) | Reimers & Gurevych, 2019 (same paper) | ✅ — verified as the paper's own reported figure; no other number invented on screen |
| 6 | Cosine similarity — the cosine of the angle between two vectors — predates embeddings; it is the standard closeness measure from the classical vector space model of information retrieval (B17–B20) | Manning, Raghavan & Schütze, 2008, *Introduction to Information Retrieval*, Ch. 6 (nlp.stanford.edu/IR-book/) | ✅ — verified; the "older than embeddings" framing and the vector-space-model attribution are the chapter's own, sourced to this textbook |
| 7 | If an embedding model is trained well, close vectors correspond to similar meaning and far vectors to different meaning, regardless of literal word overlap; sentence embedding models are specifically trained and evaluated on placing paraphrases close without being fooled by shared-word-but-different-meaning pairs (B21) | chapters/03-representing-text-embeddings.md, "'Closeness' as a proxy for meaning" section; Reimers & Gurevych, 2019 | ✅ — the chapter's own premise statement, directly attributed |
| 8 | Worked example: "How much vacation do I get?" / "What's the PTO policy?" share almost no words but mean the same thing, and should land close in embedding space; "How do I request time off?" / "How do I request a new laptop?" share the literal phrase "how do I request" but mean different things, and should land meaningfully farther apart (B22–B26) | chapters/03-representing-text-embeddings.md, "Worked example: two phrasings, one meaning — and a false match" section, Fig. 02 | ✅ — rebuilt natively (REBUILD LAW), not screenshotted. The chapter explicitly states this qualitatively — "reason about this qualitatively... since no embedding model was actually run to produce a precise score for this example." B24/B26's narration and Manim captions match that qualitative framing exactly; **no cosine number is invented anywhere in this reel** |
| 9 | Embeddings operate on whatever piece of text is handed to them — a sentence, a paragraph, or an entire manual — and what counts as one chunk affects how useful the resulting comparison is; that question belongs to Chapter 4, not this chapter (B28–B30, BVDT) | chapters/03-representing-text-embeddings.md, "Bridge" section | ✅ — B30 names the open question without depicting or asserting how Chapter 4 resolves it (NO-SOURCE-NO-VERDICT) |

## Datable-claim check

No model version number, parameter count beyond what the cited papers
themselves report (1.6B words, "a few hundred" dimensions, 65 hours/5
seconds, 10,000 sentences), or "as of [date]" claim appears anywhere in this
reel beyond the sourced figures above. BERT and Sentence-BERT are referred to
by name and citation year only, not by any framing that would date the
episode against future model releases.

## Real-person / real-object check

No real, named person, product, organization, or specific real object
appears anywhere in this reel's narration, on-screen text, or planned VOX
stills. All seven VOX beats depict generic, invented documentary scenes (a
library, an open book, a research desk, an old card-catalog wall/drawer, an
office with two desks, a stack of paper) — see `SOURCES.md` for the full
list. All are Tier 1 under Gate D2; none require a rights escalation.

## Numbers-on-screen audit

Every number that appears in a beat's `graphic.production_viz` or Remotion
`props` was checked against the claim it illustrates:
- B04: no numbers on screen — a qualitative 2D cluster rebuild of Fig. 01,
  captioned as a teaching simplification.
- B08/B09: no numbers — illustrative vector geometry only.
- B14 (`EmbedSpeedLeap` reuse): "~65 hours" / "~5 seconds" / "10,000
  sentences" — all three are the paper's own reported figures, already
  verified for the sibling ai-explainer reel's `SOURCES.md`.
- B19: "cos θ ≈ [value]" is a live-animated formula display, not a claim
  about any specific pair of real texts.
- B21, B24, B25, B26: explicitly qualitative — "similar meaning" / "different
  meaning" / "same region" / "different regions," never a computed score.

**GATE F: ✅ CLOSED.** All 9 rows verified against their cited sources or the
chapter's own text; no fabricated-but-fluent claims found; the one place a
prior sibling reel in this book might have been tempted to invent a cosine
number (the worked example) stays strictly qualitative here too, matching
the chapter's own explicit caveat.
