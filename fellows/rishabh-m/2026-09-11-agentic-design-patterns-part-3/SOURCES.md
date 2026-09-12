# SOURCES — agentic-design-patterns-part-3

## Primary source

**`agentic-patterns-part3.md`** — "Master Class Part 3: Advanced Optimization,
Safety, and the Interview Blueprint (Patterns 14-20)".
Local path: `Agentic Design Video/agentic-patterns-part3.md`.
Written by **Rishabh Madani** as his own synthesis of the upstream book below.
Read in full 2026-09-11.

## Upstream source (credited on publication)

**Book — *Agentic Design Patterns: A Hands-On Guide to Building Intelligent
Systems*, by Antonio Gulli.** The primary conceptual source: the pattern names,
their numbering (14–20 of 20), and the five-step interview blueprint that closes
the series all originate there.

Assorted YouTube explainers were consulted while learning the material. They are
not individually identifiable and are **deliberately not cited** — no claim,
figure or phrasing traces to any specific video. Same policy as Parts 1 and 2.

### Credit line — identical across all three parts

> Concepts from *Agentic Design Patterns: A Hands-On Guide to Building
> Intelligent Systems* by Antonio Gulli.

On screen in the outro card (B14) and in `description.txt`. Matches Parts 1 and
2 exactly, as planned from Part 1 — the series credits identically.

## Rebuilt figures (REBUILD LAW)

The source draws all seven patterns as ASCII art. None were captured; all were
rebuilt as native Remotion renders via `AgenticPatternDiagram`, topologies
preserved as drawn:

| Source diagram | Beat | Topology |
|---|---|---|
| Inter-Agent Communication | B03 | three topologies: boss-worker / peer-to-peer / bulletin board |
| Resource-Aware Optimization | B04 | task → classifier → cheap / standard / reasoning |
| Tree of Thoughts | B05 | root → three scored branches, two pruned → answer |
| Evaluation & Monitoring | B06 | system → pre-deploy / in-flight / production |
| Guardrails & Safety | B07 | input → PII redaction → injection check → model → output moderation |
| Prioritization | B08 | task list → score → rank queue → execute top |
| Exploration & Discovery | B09 | goal → map → cluster → investigate → report |

**B10 renders the source's own Conclusion checklist** as a five-step chain —
scope the goal, define workers, name trade-offs, safety and recovery, state
machine. The five steps and their order are the source's; the rendering is ours.

**Ours, not the source's:** the thesis that all seven patterns *subtract*
capability on purpose (see FACTCHECK), and B11's "when not to", which the source
does not argue.

## Components

**No new components were authored.** GATE L searched for tree-search, guardrail
and cost-tiering scenes; the candidates (`CwcDecompositionTree`,
`SleeperAgentsBehaviorSwitch`, `CwcModelCostComparison`) are each hard-wired to
another reel's content and expose only a `sparkLine` prop. All seven topologies
*and* the blueprint chain are carried by `AgenticPatternDiagram`, built for
Part 1 — the third reel running on it without modification.

Reused: `ClaudeComposerAsk` (B00, B13) · `BrutalistHesitantWriter` (B01) ·
`ClaudeVerdictArtifact` (B12) · `AgenticPatternDiagram` (B02–B11) ·
`HaiTitleOutro` (B14).

## Voice and house rules

- Voice: Kokoro `af_sarah`, matching Parts 1 and 2.
- Greeting **Ahoy** — deterministic pick from the HOUSE-RULES lexicon
  (`sum(ord(c)) % 48` = index 36). Talofa · Bula · Ahoy across the series; no
  repeat, as intended.
- 1.0s inter-beat hold via `pad_beats.local.py` (HOUSE-RULES RULE 2).
