# SOURCES — llm-function-calling

## What this reel asserts, and on what basis

This is a **mechanism explainer**, not a reading of a specific publication. Every
claim is about the shape of the tool-use / function-calling loop as it is
documented by the major model providers and as it is implemented in the message
formats they publish. The reel makes no claim about any benchmark, rate, market
figure, or model version.

Deliberately excluded, per DOUBLE-CHECK LAW's "strip anything that will date the
video": no model version numbers, no context-window sizes, no provider feature
comparisons, no claims about which models support tool use.

## The example values are constructed, and labelled as such

The Boston weather trace (`get_weather(city="Boston")` → `{ "temp_f": 41 }` →
"It's 41°F and overcast in Boston.") is a **constructed teaching example**, not a
live reading and not a figure lifted from a source.

This is honest rather than invented because it is not presented as evidence of
anything: it is a worked instance of a mechanism, and the reel says so on screen.
B07's caption reads *"example values, shown to trace the mechanism — not a live
reading."* No beat claims the temperature is current, correct, or measured.

Plain register's move 4 requires one concrete running example, planted early and
paid off late, and requires it to be specific enough to visualise — "user input"
would not do the work. A constructed-but-labelled instance satisfies that without
asserting a fact the reel cannot support.

## Structural claims and where they come from

| Claim | Basis |
|---|---|
| A language model produces text and has no clock, network, database, credentials, or ability to act on its own | Definitional — this is what a text-generation model is; it is the premise the whole tool-use design exists to work around |
| Tools are declared to the model as written descriptions (name, description, arguments) | The published tool/function definition format used across provider APIs |
| The model emits a *request* naming a tool and arguments; it does not execute | The published message schema: a tool-use block is model *output*, and execution happens in the caller |
| The tool result is appended to the conversation as a message, and the model is invoked again | The published message schema: the result is a message in the same list, which is why one question costs two model turns |
| A tool call can succeed with wrong arguments; a tool can go un-called because its description was vague | Standard, widely-documented failure modes of tool use; stated as failure directions, not as measured rates |

No number in this reel is presented as a research finding, so there is no figure
to verify against a published table.

## Corrections applied during authoring

- **No rate or reliability claim.** An earlier framing of B09 would have implied
  how *often* wrong-argument calls happen. There is no source for a rate that
  would not date immediately, so B09 states the two failure *directions* and
  their shared cause instead, with no frequency attached.
- **No design judgment.** Plain register does not judge the design. Lines that
  rated function calling as a good or bad design choice were cut; the register's
  job here is transfer of understanding.
- **One inference flag only.** Plain permits exactly one flagged inference. It is
  placed in B05, on "that matching is learned behaviour, not a lookup table" —
  the one place where the explanation moves from published format to model
  behaviour.

## Determinism / seeds

| Beat | Seed or determinism note |
|---|---|
| B01 | `seed: "llm-function-calling-b01"` — same seed, identical typing performance forever |
| BOUT | polarity seeded by slug `llm-function-calling` (`seedHash % 2`); no mascot, so no mascot seed |
| all illustration beats | pure functions of `useP()`; no `Math.random()`, no timers, no CSS transitions |

## GATE L — library-first record

Searched before authoring. Reused as-is: `ClaudeComposerAsk`,
`BrutalistHesitantWriter`, `ClaudeScienceChipGrid`, `ClaudeScienceSourceFlow`,
`ClaudeCodeBeat`, `BinaryBranch`, `ClaudeVerdictArtifact`.

Three genuine misses, built as components rather than slated (see
`runtime/remotion/src/FnCalling.tsx` header for the full reasoning):

- `FnCallLoop` — no library component expresses a four-stage round trip with a
  return leg. `SourceFlow` is one-directional; `CodingAgentsFig1Loop` and
  `HaiBrutalistE01Pipeline` are reel-local with hardcoded content.
- `FnCallPredictCard` — `PredictCard` existed but only as the `Illu-PredictCard`
  Studio preview with baked props; this is the parameterized wrapper.
- `FnCallTitleOutro` — `ClaudeTitleOutro` hardcodes `@NikBearBrown` and always
  renders a mascot, both locked by OUTRO-LOCK.md, whose scope is explicitly
  @NikBearBrown reels only.
