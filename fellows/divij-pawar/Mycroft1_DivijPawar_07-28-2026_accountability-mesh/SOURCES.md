# SOURCES.md — accountability-mesh (Expanded)

All claims trace to `accountability_layer/context/video_script.md`, the project's
own narrated design script, which is grounded in the project's ADR log, source files
(`schemas.py`, `directive.py`, `parser.py`, `middleware.py`, `verification.py`,
`consistency.py`, `web/db.py`), and design documents. This is a first-person
project account.

## Factual claims (DOUBLE-CHECK LAW)

| Beat | Claim | Source (video_script.md) |
|------|-------|---------------------------|
| B00 | Thesis: an unauditable conclusion is a system failure, no matter how accurate | §0, Cold open |
| B00 | AI systems can hallucinate reasons for wrong answers | §1, "world-class rationalizers" paragraph |
| B02 | Four sub-agents (financials, patents, earnings, competition) converge on a grade | §1, The problem |
| B02 | A hallucinated number from one agent can launder into an official investment grade | §1, same section |
| B02 | LLMs will invent a confident, coherent explanation for a wrong answer they already made | §1, same section |
| B03 | An LLM judge shares the same blind spot as the agent — it evaluates plausibility | §2, "LLM-as-a-judge" |
| B03 | Gradient inversion works in principle but forces abandoning frontier models | §2, "white-box gradient inversion" |
| B04 | ReasoningObject: frozen dataclass with confidence, citation, exact source line, citations | §3, Mechanism one |
| B04 | Checkpointing: database triggers enforce append-only at DB level, not application code | §3, Mechanism two |
| B04 | Adversarial Arbitration: divergent agents debate; unresolved disagreement ships as output | §3, Mechanism three |
| B05 | ADR-11: polite directive failed on live Gemini (model wrote preamble) | §4, "Making it real" |
| B05 | Fix was mechanical constraint: first character = bracket, no preamble | §4, same section |
| B05 | Validation loop: failure logs → retry → halt on second failure | §4, same section |
| B06 | ADR-06: structure enforced, truth not; fabricated log passes all checks | §5, "The honest limit" |
| B07 | Ground-truth checking: compare AI claims to SEC filings | §6, "Claim verification against ground truth" |
| B07 | Reproducibility checking: run twice, flag numbers appearing in only one run | §6, "Consistency probing" |
| B07 | Structural enforcement is real and tested; proving reasoning is real is open | §7, "What's next" summary |

## Simplifications and content coverage (per DOUBLE-CHECK LAW)

- **The LangSmith rejected-approach point is dropped from B03** (creator's
  editorial call — kept the reel to two rejected approaches instead of three).
  The source script's LangSmith point (deletable traces ≠ an audit trail)
  remains true and remains in `video_script.md` §2; it's simply not carried
  into this video's B03 beat.
- **Full mechanisms explained (B04):** All three mechanisms are defined in detail,
  not just named. Each mechanism's purpose and enforcement method is stated.
- **The ADR-11 worked example (B05):** The concrete failure-and-fix story is carried
  fully, showing the shift from "polite" to "mechanical" constraints.
- **Ground-truth and reproducibility checks (B07):** Included in the verdict beat
  to show the full accountability toolkit, not just structural enforcement.
- **Inversion Audit Engine (source §6, second half):** Cut from the video.
  Genuinely unresolved research frontier; belongs in a follow-up, not this reel.
- **LangFuse observability layer (source §7):** Cut from the video.
  Additive layer that doesn't serve the single thesis; separate piece material.
- **Honest limit (ADR-06, B06):** Preserved and expanded. This is the reel's
  intellectual center per the source script's own recording notes.

## Scene/beat map

| Beat | Scene / pattern | Notes |
|------|------------------|-------|
| B00 | ClaudeComposerAsk (Remotion) | Cold open — thesis + problem + solution |
| B01 | B01_TheMesh (Manim) | BLUF — agent → gate → investor, three properties light up |
| B02 | B02_NakedConclusion (Manim) | Four agents, one hallucinated input, funnel, no proof |
| B03 | B03_RejectedApproaches (Manim) | Three-row comparison table |
| B04 | B04_ThreeMechanisms (Manim) | Three lit nodes with definitions |
| B05 | B05_ValidationLoop (Manim) | Attempt 1 (fail) → Attempt 2 (succeed) → Halt branch |
| B06 | B06_TheHonestLimit (Manim) | Fabricated log passes checks, strikethrough "TRUE" |
| B07 | ClaudeVerdictArtifact (Remotion) | Verdict — four recap lines (structural, ground truth, reproducibility, limit) |
| B08 | ClaudeComposerAsk (Remotion) | Your Turn — prompt + 3-item rubric, read aloud |
| B09 | ClaudeTitleOutro (Remotion) | Title restate + @DivijPawar |

## Coverage from original script

| Original section | In video | Notes |
|---|---|---|
| §0 Cold open (thesis) | B00 | Full |
| §1 Problem (four agents, hallucinated conclusion, LLM rationalization) | B02 | Expanded, explained |
| §2 Rejected approaches (LLM judge, gradient inversion) | B03 | LangSmith point cut (editorial); other two full, with reasons |
| §3 Mechanisms (ReasoningObject, checkpointing, Arbitration) | B04 | Detailed definitions |
| §4 ADR-11 directive failure | B05 | Full worked example |
| §5 ADR-06 honest limit | B06 | Full, held on screen |
| §6 first half (consistency probing, EDGAR verification) | B07 verdict | Mentioned as "reproducibility" and "ground truth" |
| §6 second half (Inversion Audit Engine) | — | Cut (unresolved research) |
| §7 LangFuse observability | — | Cut (separate layer, separate reel) |

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) for all narration. No ElevenLabs, no FLUX, no
paid services. No publishing — master stays in the reel folder.
