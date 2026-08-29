# FACTCHECK.md — claude-liam-rag-deep-explainer (Gate F)

Source: `chapters/01-introduction.md` (RAG Foundations, Vedanshu Daxesh Patel).
Same underlying source/citations as the sibling reels (`claude-liam-rag-introduction`,
`claude-cli-rag-introduction`); this file re-verifies each claim in the
deeper cut's own words.

| # | Claim (beat) | Source | Verdict |
|---|---|---|---|
| 1 | A help-desk assistant answers confidently from a stale policy (B00–B06) | Chapter's "Opening" section | ✅ — scenario as stated, no invented specifics beyond it |
| 2 | Every model has a training cutoff; the policy changed after it (B05) | Chapter: "text has a cutoff... policy documents were never part of it" | ✅ — "eight months ago" is the chapter's own figure |
| 3 | RAG = pretrained LM + non-parametric memory + learned retriever (B07–B11) | Lewis et al., 2020, NeurIPS — arxiv.org/abs/2005.11401 | ✅ — near-verbatim quote in B11, cited on screen |
| 4 | Retrieve → generate is two separate, ordered jobs (B12–B16) | Chapter's "Retrieve, then generate" section; Lewis et al., 2020 | ✅ — matches the chapter's own two-step framing |
| 5 | A bigger model doesn't fix this — still parametric-only (B18) | Chapter: "'Just use a bigger model'" section | ✅ — no fabricated capability claim about any specific model |
| 6 | Fine-tuning loses to retrieval at injecting fresh/long-tail facts (B21) | Ovadia et al., 2024 (arxiv.org/abs/2312.05934); Soudani et al., 2024 (arxiv.org/abs/2403.01432) | ✅ — presented qualitatively (bar chart, no invented percentages); citation on screen |
| 7 | Retrieval keeps documents outside the model, updatable instantly, traceable (B22) | Chapter's "Retrieval" paragraph | ✅ |
| 8 | No fixed document-count threshold for when RAG is overkill (B24–B26) | Chapter: "practitioner sources disagree on exact thresholds... any number offered here would age quickly" | ✅ — narration and B26's Manim scene both stay qualitative, matching the chapter's own hedge exactly |
| 9 | Worked example: same mechanism resolves the sick-leave answer (B28–B31) | Chapter's "Worked example" section | ✅ — "15 sick days" / "10 sick days" / "updated 8 months ago" are demo numbers invented FOR THIS VIDEO's illustration (as in the sibling `cli-explainer` reel), not asserted as the book's own figures — logged in SOURCES.md |

## Datable-claim check (DOUBLE-CHECK LAW, sharpened for this genre)

No model version numbers, vendor names, or "as of [date]" claims appear
anywhere in the narration or on-screen text. "Fable 5" appears only inside
the fixed `ClaudeComposerAsk` UI chrome (brand fidelity element, not a
narration claim) — consistent with how the sibling reels handle it.

## Real-person / real-object check

None. Every VOX still is Tier 1 (generic office/library/server-room scenes,
no real named person, building, or artifact) — no rights escalation
required (see SHOPPING.md).

**GATE F: ✅ CLOSED.** All 9 rows verified against the chapter and its own
cited sources. No narration changes required.
