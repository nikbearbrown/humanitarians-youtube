# SOURCES — agentic-design-patterns-part-2

## Primary source

**`agentic-patterns-part2.md`** — "Master Class Part 2: Orchestration, Memory,
and Fail-Safes (Patterns 7-13)".
Local path: `Agentic Design Video/agentic-patterns-part2.md`.
Written by **Rishabh Madani** as his own synthesis of the upstream book below.
Read in full 2026-09-04.

## Upstream source (credited on publication)

**Book — *Agentic Design Patterns: A Hands-On Guide to Building Intelligent
Systems*, by Antonio Gulli.** The primary conceptual source: the pattern names,
their numbering (7–13 of 20), and the orchestration/memory/fail-safe grouping
all originate there.

The author also watched assorted YouTube explainers while learning the material.
They are not individually identifiable and are **deliberately not cited** — no
claim, figure or phrasing in this reel traces to any specific video, so listing
them would imply a precision that does not exist. Same policy as Part 1.

### Credit line — identical to Part 1, by design

> Concepts from *Agentic Design Patterns: A Hands-On Guide to Building
> Intelligent Systems* by Antonio Gulli.

On screen in the outro card (B14) and in `description.txt`. **Part 3 must use
this exact wording.**

## Rebuilt figures (REBUILD LAW)

The source draws all seven patterns as ASCII art. None were captured; all were
rebuilt as native Remotion renders via `AgenticPatternDiagram`, topologies
preserved as drawn:

| Source diagram | Beat | Topology |
|---|---|---|
| Multi-Agent Collaboration | B03 | manager → 3 specialists → shared store |
| Memory Management | B04 | incoming → short-term / episodic / long-term |
| Learning and Adaptation | B05 | action → capture → denoise → update |
| Goal Setting and Monitoring | B06 | goal → KPIs → monitor → drift → re-plan |
| Exception Handling | B07 | error → temporary / permanent / critical |
| Human-in-the-Loop | B08 | agent → confidence → pause/review → resume |
| RAG | B09 | query → search → rerank → ground → answer |

**Ours, not the source's:** the reel's thesis ("state is the hard part" — see
FACTCHECK for why it is defensible), B10's four-pattern worked conversation, and
B11's "when not to", which the source does not argue.

## Components

**No new components were authored.** GATE L searched for memory-tier, RAG and
human-in-the-loop scenes; the candidates (`CwcMemoryTimeline`,
`CwcMemoryRetrieval`, `CodingAgentsFig1Loop`) are each hard-wired to another
reel's content and expose only a `sparkLine` prop, so none could carry this
material. All seven topologies are handled by `AgenticPatternDiagram`, built for
Part 1 — the intended payoff of making it parameterized rather than bespoke.

Reused: `ClaudeComposerAsk` (B00, B13) · `BrutalistHesitantWriter` (B01) ·
`ClaudeVerdictArtifact` (B12) · `AgenticPatternDiagram` (B02–B11) ·
`HaiTitleOutro` (B14).

## Voice and house rules

- Voice: Kokoro `af_sarah`, matching Part 1.
- Greeting **Bula** — deterministic pick from the HOUSE-RULES lexicon
  (`sum(ord(c)) % 48` = index 35). Part 1 drew Talofa; the rotation is working.
- 1.0s inter-beat hold via `pad_beats.local.py` (HOUSE-RULES RULE 2).
