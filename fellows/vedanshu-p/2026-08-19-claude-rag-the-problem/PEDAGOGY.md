# PEDAGOGY — Confident, Frozen, Or Buried. (personal-author ai-explainer)

Concept explainer of *RAG Foundations*, Chapter 2 ("The Problem: Why LLMs
Alone Aren't Enough"). Vox-style `ai-explainer` build — NOT skill-teardown,
NOT profile, NOT audit. Personal author channel: persona and sign-off are the
book's author, Vedanshu Daxesh Patel (`@VedanshuDaxeshPatel`), voice Kokoro
`am_onyx` ("Onyx"), free. IN-FOR-BEAR LAW does not apply — this is not a
`@NikBearBrown`/Liam substitution; the narrator is named as themself in B00
and signs off as themself in BOUT. Never publishes; master stays in this reel
folder. Matches the established series template from
`youtube/2026-08-12-claude-rag-introduction/` (Chapter 1's reel).

## Act structure

- **B00 cold open** — `ClaudeComposerAsk`, RESULT lines answered (COLD OPEN
  LAW). The "which of the three is it" question, bridged from Chapter 1's own
  closing sentence ("the model never saw the document").
- **B01 executive summary (BLUF)** — one-breath statement of the whole idea
  before any specific (EXECUTIVE-SUMMARY LAW): three distinct failures, one
  shared fix — gist only, no reveals spent.
- **B02–B07 body** — six illustrated beats, ILLUSTRATE LAW: no Claude UI,
  each a bespoke or shared C3/rhetorical illustration (no two consecutive
  beats share a visual scheme):
  - B02 `ProblemHallucination` (bespoke) — intrinsic/extrinsic hallucination,
    help-desk example.
  - B03 `ProblemStaleKnowledge` (bespoke) — training-cutoff timeline.
  - B04 `ProblemContextLimits` (bespoke — not a `ScaleComparison` wrap: that
    shared pattern is a log-scale physical-unit comparator and can't express a
    qualitative, unitless ordering without inventing an axis) — the "lost in
    the middle" ordering, qualitative only, no invented numbers.
  - B05 `ProblemWorkedExample`, wraps the shared `ChipGrid` — the reveal: the
    help-desk assistant hitting all three, rebuilding the chapter's own Fig. 01.
  - B06 `ProblemBiggerWindowVerdict`, wraps the shared `LayerStack` — why a
    bigger context window fixes none of the three alone.
  - B07 `ProblemPredictCard`, wraps the shared `PredictCard` (unmodified
    pedagogy device) — commit before the bridge to "the right passages,
    chosen at question-time."
- **BVDT verdict** — `ClaudeVerdictArtifact`, four claims, each traceable to a
  cited source (NO-SOURCE-NO-VERDICT).
- **BHTF handoff** — `ClaudeComposerAsk`, greeting `Your turn.`, an interesting
  prompt that runs the three-failure lens on the viewer's own document;
  narration reads it aloud and discusses what to look for (HANDOFF LAW).
- **BOUT outro** — `ClaudeTitleOutro`, exact title restate, `@VedanshuDaxeshPatel`
  handle, `Vedanshu Daxesh Patel` byline subline (OUTRO LAW).

## Evidence discipline (DOUBLE-CHECK LAW)

| Claim | Source (chapter's citation) | Verdict |
|---|---|---|
| Hallucination = fluent, unfaithful output; splits into intrinsic (contradicts a source) / extrinsic (unverifiable) | Ji et al., 2023 (ACM Computing Surveys); Huang et al., 2023 (arxiv.org/abs/2311.05232) | Both real, checkable surveys; used for B02's split, not sensationalized |
| Grounding in retrieved documents *reduces* (not eliminates) hallucination | Shuster et al., 2021 — arxiv.org/abs/2104.07567 | Used in BVDT exactly as a reduction, never an elimination, matching the chapter's own careful framing |
| Models have a frozen knowledge cutoff; no further learning after deployment | OpenAI, 2023, GPT-4 Technical Report — arxiv.org/abs/2303.08774 | Used in B03/BVDT; no specific cutoff date stated on screen (chapter itself declines to memorize one) |
| Context windows are bounded, have grown across generations, and are never unbounded | OpenAI, 2023 (same report) | Used in B04's framing line only; no specific token count invented |
| Long-context accuracy is highest when the fact sits at the start/end, lowest when buried mid-context | Liu et al., 2024 — arxiv.org/abs/2307.03172 | Used in B04/BVDT as a qualitative ordering only; the chapter states no specific accuracy numbers, so none appear on screen |
| Fig. 01 three-panel illustration (invented / retired / buried) | chapters/02-the-problem.md, Figure 01 | Rebuilt natively as B05 `ProblemWorkedExample`; no screenshot used |
| Help-desk anecdote (all three failures on one system) | chapter's "Worked example" section | Used as B05's scenario only; no invented specifics beyond the chapter's own framing |

Nothing in the narration cites a model version number, a specific cutoff
date, or a context-length figure likely to date the video — matching the
chapter's own explicit choice not to memorize a number that "shifts from one
release to the next."

## Friction protected

- **Kept**: the "why a bigger window doesn't fix any of them" act (B06) — it
  is the chapter's own central falsifiability move (naming the obvious wrong
  fix and explaining exactly why it fails each of the three).
- **Kept**: the predict/bridge beat (B07) — the chapter's own bridge
  paragraph ("the model has to be given the right text... which means text
  has to be put into a form that can be compared") is a genuine scaffolded
  claim worth committing to before the reveal.
- **Removed for time**: the chapter's two numbered exercises (matching
  descriptions to failure names) are not reproduced as an on-screen quiz —
  the handoff prompt (BHTF) does the equivalent scaffolded task on the
  viewer's own material instead, which is the stronger version of the same
  exercise.

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01 BLUF states the three-failures frame
  before B02–B06 supply specifics)
- WORKED EXAMPLE ✓ (B05 — the same help-desk assistant hitting all three)
- FALSIFIABILITY ✓ (B06 names what does NOT fix the problem — a bigger
  window — and explains why not, per failure)
- SCAFFOLDED VIEWER TASK ✓ (BHTF handoff runs the three-failure lens on the
  viewer's own document)
- FOUR BOOKENDS ✓ (cold open, BLUF, verdict, handoff+outro)
- NO-SOURCE-NO-VERDICT ✓ (every claim in BVDT traces to a cited source above)

## VERDICT: PASS

Approved 2026-08-18 — Vedanshu Daxesh Patel reviewed `beat_sheet.json` and
this document and signed off. Proceeding to Part B (Kokoro audio → bespoke
`Problem*` Remotion components → compile at 4K → visual QC).