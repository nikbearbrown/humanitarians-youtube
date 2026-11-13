# SOURCES — Three Ways To Be Wrong.

## Book source

- Book: *RAG Foundations* (author: Vedanshu Daxesh Patel)
- Chapter: `chapters/02-the-problem.md` — "Chapter 2 — The Problem: Why LLMs Alone Aren't Enough"
- Same source as the sibling ai-explainer reel (`2026-08-18-claude-rag-the-problem`) and
  cli-explainer reel (`2026-08-18-claude-cli-rag-the-problem`). This deep-explainer cut
  makes no new factual claims beyond those two — it re-presents the same five citations
  across a 6-act documentary structure instead of a single reel.

## Citations (identical to the sibling ai-explainer reel's SOURCES.md)

- Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J.,
  Madotto, A., & Fung, P. (2023). Survey of Hallucination in Natural Language
  Generation. *ACM Computing Surveys*, 55(12), Article 248.
  https://dl.acm.org/doi/10.1145/3571730 — used for the intrinsic/extrinsic split (B08).
- Huang, L., Yu, W., Ma, W., Zhong, W., Feng, Z., Wang, H., Chen, Q., Peng, W.,
  Feng, X., Qin, B., & Liu, T. (2023). A Survey on Hallucination in Large
  Language Models. https://arxiv.org/abs/2311.05232 — corroborates the same
  split, folded into B08/B09's citation lines rather than given its own act.
- Shuster, K., Poff, S., Chen, M., Kiela, D., & Weston, J. (2021). Retrieval
  Augmentation Reduces Hallucination in Conversation. *Findings of ACL: EMNLP
  2021*, pp. 3784–3803. https://arxiv.org/abs/2104.07567 — used in B10/BVDT
  exactly as a reduction, never an elimination (the B10 Manim curve flattens
  above zero — no rate number is put on screen).
- OpenAI (2023). GPT-4 Technical Report. https://arxiv.org/abs/2303.08774 —
  used in B12/B18/BVDT for the training-cutoff and context-ceiling claims. No
  specific cutoff date or token count is stated on screen anywhere in this reel.
- Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F.,
  & Liang, P. (2024). Lost in the Middle: How Language Models Use Long
  Contexts. *Transactions of the Association for Computational Linguistics*,
  12, 157–173. https://arxiv.org/abs/2307.03172 — used in B19/B20/BVDT as a
  qualitative ordering only (accuracy highest at start/end, lowest in the
  middle) — no accuracy percentages are invented for the B19 Manim scene or
  the B20 Remotion beat.

## Figures (REBUILD LAW — rebuilt natively, never screenshotted)

- `images/the-problem-fig-01.png` / `.svg` — the chapter's three-panel
  illustration. Rebuilt natively as B26 (`ProblemWorkedExample`, reused
  verbatim from the sibling ai-explainer build) as three peer chips —
  captioned "Redrawn (simplified) from the chapter's three-panel figure —
  Fig. 01." The original PNG/SVG remains reference-only; never embedded.

## VOX stills — all Tier 1 (generic/illustrative, no rights escalation)

None of the eight VOX beats depict a real, named person, object, or event —
all are generic documentary-style metaphors invented for this reel, so all
are Tier 1 per Gate D2 (`reference/shopping-list.md`): AI-generate or stock,
no rights clearance required. Full generation prompts + sourcing tiers live
in `SHOPPING.md` (written after audio lock, per Gate D2 — not yet written as
of this authoring pass). Subjects, by beat:

- **B02/B03 (run R1)** — an office desk with a chat window open, then a
  tight shot on the blinking cursor. Illustrates the chapter's own help-desk
  worked example as a establishing/close pair.
- **B06/B07 (run R2)** — a stage magician's "something from an empty hat"
  moment. A metaphor for confident invention (hallucination) — not a claim
  that models perform stage magic.
- **B11 (single)** — a dusty archive of old bound documents. A metaphor for
  frozen, untouched knowledge (stale knowledge).
- **B17 (single)** — a desk buried under one long unrolled document. A
  metaphor for "everything technically present, the right part still
  buried" (context limits / lost in the middle).
- **B21 (single)** — an oversized, empty open suitcase or moving box. A
  metaphor for "bigger container, nothing more useful inside" (why a bigger
  window doesn't fix anything).
- **B27 (single)** — a hand with a magnifying glass over a page, or pulling
  one book from a shelf. A metaphor for "deciding which one piece matters" —
  the honest bridge to Chapter 3, illustrating the QUESTION the next chapter
  answers, not its mechanism.

## Numbers NOT put on screen (honesty guard)

- No model version number, context-length figure, or knowledge-cutoff date
  is spoken or shown anywhere in this reel — matching the chapter's own
  choice to avoid claims that would date the video.
- B19 (Manim) and B20 (Remotion, reused) both show the Liu et al. ordering
  as a qualitative shape only — bright at the edges, dim in the middle — no
  invented accuracy percentages.
- B10 (Manim) shows the Shuster et al. reduction as a curve that flattens
  above zero — no invented hallucination-rate percentage.

## Bridge honesty (B27, B28, BVDT)

Chapter 2 presents no fix — it only names the three failures, argues a
bigger window doesn't solve them, and bridges to Chapter 3 ("representing
text" / comparison). B27's still and B28's Manim scene both name the
QUESTION ("something has to decide which passage matters") without
depicting or asserting HOW Chapter 3 answers it — no retrieval mechanism,
no embedding/vector-space visual, is shown here. That mechanism belongs to
the Chapter 3 video, not this one (NO-SOURCE-NO-VERDICT).
