# SOURCES — agent-memory

## What this reel is

A mechanism explainer on how memory is implemented in an AI agent. It makes no
claim about any product, benchmark, framework or result. Every structural claim
rests on the published chat-completion contract (the caller supplies the full
message list on each request) and on the ordinary shape of the
retrieve-into-context pattern.

## Structural claims and where they come from

| Claim | Basis |
|---|---|
| Each model call is stateless; the caller re-sends the whole conversation | The published request contract: `messages` is supplied in full by the caller every turn |
| The model keeps nothing between calls | Same contract — persistence is the caller's, not the model's |
| Short-term memory is the in-request conversation, and it has a finite ceiling | Follows from the contract plus the documented existence of a context limit |
| Filling the window forces something out, usually the oldest turns | Truncation / sliding-window is the ordinary handling. Narration says "usually", which is accurate rather than a hedge |
| Long-term memory is an external store, written to and searched, with results pasted into the next request | The retrieval-augmented pattern as ordinarily implemented |
| Retrieved content enters the conversation, never the model's weights | Definitional — nothing at inference time modifies weights |
| Same weights on every call, so recall differences come from the surrounding code | Follows from statelessness |

## Deliberately excluded (would date the video)

No model names or versions. **No context-window sizes in tokens** — those numbers
move constantly and would date the reel; B05 makes the point structurally instead.
No named vendor, library or framework. No retrieval-accuracy or reliability figure.

## Constructed material, labelled

The coffee order — "prefers an oat flat white" — is a **constructed teaching
example**, planted at B02 as a prediction prompt and paid off at B09. It is not
attributed to any real product or user. Plain register's move 4 requires one
concrete running example, specific enough to visualise; "user preference" would
not do that work. Nothing about it is presented as evidence.

The code in B03 and B08 is illustrative of the pattern's normal shape. It names no
library and is not copied from any source; B03 shows a `messages` list, B08 shows
`store.save` / `store.search` as stand-ins for whatever store a viewer uses.

## Corrections applied during authoring

- **No token counts.** An earlier draft of B05 named a specific context size. Cut:
  it would date immediately and the structural point ("there is a ceiling") is what
  actually teaches.
- **No design judgment.** Plain explains and stops. Lines rating statelessness or
  RAG as good or bad design were cut.
- **One inference flag only.** It sits at B07, on what counts as "relevant" — the
  genuine seam, since relevance is a scoring decision rather than ground truth.
- **"turn 60" is illustrative**, not a measured limit; recorded here so the
  simplification is on the record.

## Determinism / seeds

| Beat | Seed or determinism note |
|---|---|
| B01 | `seed: "agent-memory-b01"` — same seed, identical typing performance forever |
| BOUT | polarity seeded by slug `agent-memory` (`seedHash % 2`); no mascot, so no mascot seed |
| all illustration beats | pure functions of `useP()`; no `Math.random()`, no timers, no CSS transitions |

## Components

Reuse only — **no new components built**. Already registered and confirmed
RENDERABLE: `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `ClaudeScienceChipGrid`,
`ClaudeScienceLayerStack`, `ClaudeScienceSourceFlow`, `BinaryBranch`,
`ClaudeVerdictArtifact`, `ClaudeCodeBeat`, plus `FnCallPredictCard` and
`FnCallTitleOutro` from `llm-function-calling`.

One shared-component change was made, as instructed ("every shared composition
re-times to its beat"): `ClaudeCodeBeat` gained an optional `durationInSeconds`
plus `calculateMetadata`, defaulting to its previously-registered 300f/10s so no
existing reel renders differently. Its line stagger now spreads across the whole
beat instead of completing in the first 10s and freeze-holding.
