# PEDAGOGY — The Model Never Saw The Document. (personal-author ai-explainer)

Concept explainer of *RAG Foundations*, Chapter 1 ("Introduction: What RAG Is
and Why It Exists"). Vox-style `ai-explainer` build — NOT skill-teardown,
NOT profile, NOT audit. Personal author channel: persona and sign-off are the
book's author, Vedanshu Daxesh Patel (`@VedanshuDaxeshPatel`), voice Kokoro
`am_onyx` ("Onyx"), free. IN-FOR-BEAR LAW does not apply — this is not a
`@NikBearBrown`/Liam substitution; the narrator is named as themself in B00
and signs off as themself in BOUT. Never publishes; master stays in this reel
folder.

## Act structure

- **B00 cold open** — `ClaudeComposerAsk`, RESULT lines answered (COLD OPEN
  LAW). The help-desk sick-leave scenario from the chapter's opening, used as
  the hook.
- **B01 executive summary (BLUF)** — one-breath statement of the whole idea
  before any specific (EXECUTIVE-SUMMARY LAW): search first, answer second.
- **B02–B06 body** — five illustrated beats, ILLUSTRATE LAW: no Claude UI,
  each a C3 concept illustration built on the shared `illustrations/structural.tsx`
  library (no two consecutive beats share a visual scheme):
  - B02 `SourceFlow` — the retrieve-then-generate mechanism (rebuilds Fig. 01).
  - B03 `LayerStack` — bigger model vs. fine-tuning vs. RAG (rebuilds Fig. 02,
    simplified per REBUILD LAW — captioned on screen).
  - B04 `PredictCard` (shared, unmodified) — commit before the reveal: when is
    RAG overkill?
  - B05 `ChipGrid` — the reveal: fits-in-the-prompt vs. needs-to-be-searched.
  - B06 `SourceFlow` (reused, different props) — the help-desk scenario closed
    with the fix applied; worked example.
- **BVDT verdict** — `ClaudeVerdictArtifact`, four claims, each traceable to a
  cited source (NO-SOURCE-NO-VERDICT).
- **BHTF handoff** — `ClaudeComposerAsk`, greeting `Your turn.`, an interesting
  prompt that runs RAG reasoning on the viewer's OWN stale document; narration
  reads it aloud and discusses what to look for (HANDOFF LAW).
- **BOUT outro** — `ClaudeTitleOutro`, exact title restate, `@VedanshuDaxeshPatel`
  handle, `Vedanshu Daxesh Patel` byline subline (OUTRO LAW).

## Evidence discipline (DOUBLE-CHECK LAW)

| Claim | Source (chapter's citation) | Verdict |
|---|---|---|
| RAG = non-parametric memory + retriever + generator, two-step | Lewis et al., 2020, NeurIPS — arxiv.org/abs/2005.11401 | Verbatim to the paper's own framing; not sensationalized |
| Retrieval beats fine-tuning at injecting facts, incl. long-tail | Ovadia et al., 2024 (arxiv.org/abs/2312.05934); Soudani et al., 2024 (arxiv.org/abs/2403.01432) | Both cited in B03/BVDT; no rate/number invented beyond what the chapter states |
| Pretrained LMs store some facts but incompletely/unreliably vs. an external source | Petroni et al., 2019 — arxiv.org/abs/1909.01066 | Referenced in register but not quoted verbatim on screen (no figure needs it) |
| Fig. 01 two-box retrieve→generate flow | chapters/01-introduction.md, Figure 01 | Rebuilt natively as B02 `SourceFlow`; no screenshot used |
| Fig. 02 three-column comparison | chapters/01-introduction.md, Figure 02 | Rebuilt natively as B03 `LayerStack`, captioned "Redrawn (simplified)" per REBUILD LAW — the checklist rows are compressed to one verdict phrase per column, not reproduced as an exact grid |
| Help-desk anecdote (sick-leave policy, 8 months stale) | chapter's Opening + Worked Example sections | Used as B00 hook and B06 close; no invented specifics beyond the chapter's own framing |

Nothing in the narration cites a model version number or a count likely to
date the video; the qualitative "when RAG is overkill" line follows the
chapter's own hedge (no specific document-count threshold is asserted).

## Friction protected

- **Kept**: the RAG-vs-bigger-model-vs-fine-tuning act (B03) — it's the
  chapter's central falsifiability move (what does NOT fix the problem, and
  why not) and directly supports the interview-prep framing of the book.
- **Kept**: the overkill predict/reveal (B04/B05) — the chapter explicitly
  flags this as a boundary condition worth remembering.
- **Removed for time**: full citation of Petroni et al.'s "Language Models as
  Knowledge Bases?" framing as its own beat — folded into B03's narration
  instead since it restates the same point (parametric memory is incomplete)
  the bigger-model card already makes.

## Teaching-arc checklist (nopunt whole-sheet gate)

- FRAMEWORK before examples ✓ (B01 BLUF states the retrieve→generate frame
  before B02–B06 supply specifics)
- WORKED EXAMPLE ✓ (B00 cold open + B06 close — the same help-desk scenario,
  broken and then fixed)
- FALSIFIABILITY ✓ (B03 names what does NOT fix the problem and why; B05
  names the boundary where RAG stops earning its cost)
- SCAFFOLDED VIEWER TASK ✓ (BHTF handoff runs the lesson on the viewer's own
  document)
- FOUR BOOKENDS ✓ (cold open, BLUF, verdict, handoff+outro)
- NO-SOURCE-NO-VERDICT ✓ (every claim in BVDT traces to a cited source above)

## VERDICT: PASS

Approved 2026-08-14 — human reviewed `beat_sheet.json` + this document and
signed off "approve as-is." Proceeding to Step 3 (Kokoro audio) and Step 4
(bespoke Rag* components + render).
