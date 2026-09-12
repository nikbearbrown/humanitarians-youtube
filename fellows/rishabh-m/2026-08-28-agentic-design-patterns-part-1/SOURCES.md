# SOURCES — agentic-design-patterns-part-1

## Primary source

**`agentic-patterns-part1.md`** — "Master Class Part 1: Foundations of Agentic
AI & The First 6 Design Patterns (An Interview Perspective)".
Local path: `Agentic Design Video/agentic-patterns-part1.md`.
Written by **Rishabh Madani** as his own synthesis of the upstream material
below. Read in full 2026-08-28. Part 2 exists in the same folder and is **out of
scope for this reel** at the author's instruction.

The notes carry bracketed reference markers (`[1]`, `[3, 6]`, …) pointing to a
bibliography not reproduced in the file — they index the upstream sources below.
They could not be resolved individually, so no claim in this reel rests on a
marker alone: every on-screen claim traces to prose stated directly in the notes.
See FACTCHECK.md.

## Upstream sources (must be credited on publication)

The notes are a derived synthesis, not original research. Confirmed by the
author 2026-08-28:

1. **Book — *Agentic Design Patterns: A Hands-On Guide to Building Intelligent
   Systems*, by Antonio Gulli.** The primary conceptual source, confirmed by the
   author 2026-08-28. The pattern names, the grouping, and the ~20-pattern scope
   all originate here. **This is the credit that must appear on publication.**
2. **Assorted YouTube explainers**, consulted while learning the concepts.
   Not individually identifiable and **deliberately not cited** — see below.

### Why the videos are not cited

The author watched several videos per concept as background understanding and
does not recall which. That is the correct reason *not* to list them: no claim,
figure, number, or phrasing in this reel traces to any specific video. Every
verifiable claim traces to the notes, and through them to Gulli's book
(FACTCHECK.md maps all 16). Citing unidentifiable sources would be decoration —
it implies a specificity that does not exist. We cite what can be verified.

### What this reel takes, and what it does not

- **Taken:** the pattern *names* and their canonical structures (chaining,
  routing, parallelization, reflection, tool use, planning). These are named
  architectural patterns in common industry use — the vocabulary, not
  expression.
- **Independently written:** all narration. Rewritten in the HAI Plain register
  per DOUBLE-CHECK LAW, fact-checked against the notes, and de-sensationalized
  (the source's "single-prompt engineering is officially over" was reframed as a
  conditional, and B10 argues the opposite case, which the notes never do).
- **Independently drawn:** all six diagrams are native Remotion renders built
  from the ASCII topologies in the notes. No figure was captured, traced, or
  lifted from the book or the videos (REBUILD LAW). The topologies themselves
  are generic engineering shapes — a fan-out, a critic loop — not distinctive
  expression.
- **Ours, not the source's:** the "three change what runs / three change how it
  thinks" grouping (B02) and the "one ticket, four patterns" worked example
  (B09), which composes the notes' own customer-support and SQL-tool examples.

## Credit line — RESOLVED 2026-08-28

> Concepts from *Agentic Design Patterns: A Hands-On Guide to Building
> Intelligent Systems* by Antonio Gulli.

Carried in both required places:

- **On screen** — the outro card's `credit` line (B13).
- **In the description** — `description.txt`, first line under the fold.

**Use this exact wording on Parts 2 and 3** so the series credits identically.
Retrofitting a changed credit across three published reels is the avoidable
mistake here.

No open attribution items remain.

## Rebuilt figures (REBUILD LAW)

The source renders all six pattern diagrams as ASCII art. None were captured or
screenshotted; all six were rebuilt as native animated Remotion graphics via the
`AgenticPatternDiagram` component. Topologies preserved exactly as drawn:

| Source diagram | Beat | Topology preserved |
|---|---|---|
| Prompt Chaining | B03 | input → subtask → validate → subtask → output |
| Routing | B04 | request → router → 3 specialists |
| Parallelization | B05 | task → split → 3 workers → merge → summary |
| Reflection | B06 | generator → output → critic, with feedback loop back |
| Tool Use | B07 | request → discover → permission → execute → parse |
| Planning | B08 | goal → milestones + constraints → execute → success |

B09's "one ticket, four patterns" is **our composition**, not a source diagram —
it assembles the source's own customer-support and SQL-tool examples into a
single worked example. Flagged as an editorial construction.

## Components authored for this reel

Both were GATE L punts — the library search found no reusable equivalent, so
they were built rather than slated, and are now in the index for future reels.

- **`AgenticPatternDiagram`** (`runtime/remotion/src/scenes/`) — parameterized
  node/edge flow diagram. Existing candidates (`HaiBrutalistE01Pipeline`,
  `CwcFanOutFlow`, `CodingAgentsFig1Loop`) are each hard-wired to one reel's
  content, so none could be reused.
- **`HaiTitleOutro`** — `@HumanitariansAI` title-restate outro. Built because
  `ClaudeTitleOutro` hardcodes `@NikBearBrown` with no prop or override
  (OUTRO-LOCK.md), leaving the HAI channel with no compliant outro card.

## Voice and house rules

- Voice: Kokoro `af_sarah`, chosen by the author. Free, local, no key.
- Greeting `Talofa` — deterministic pick from the HOUSE-RULES.local.md lexicon:
  `sum(ord(c) for c in slug) % len(GREETINGS)` = 2914 % 48 = index 34.
- 1.0s inter-beat hold applied via `pad_beats.local.py` (HOUSE-RULES RULE 2).

## Attribution note

Resolved — see "Credit line" above. An earlier draft of this file flagged the
source as unattributed; the author confirmed Antonio Gulli's *Agentic Design
Patterns* as the upstream source, and the credit now appears on the outro card
and in `description.txt`. No open attribution items.
