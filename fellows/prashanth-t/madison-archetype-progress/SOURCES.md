# SOURCES — madison-archetype-progress

## What this reel is

A **project progress update** at the planning/scoping stage, not a mechanism
explainer and not a launch. The source is the project's own strategic plan plus
the owner's current status. Nothing here is a research finding.

## The twelve archetypes

The twelve-archetype branding framework — Hero, Sage, Ruler, Creator, Caregiver,
Everyman, Jester, Lover, Rebel/Outlaw, Magician, Innocent, Explorer — is the
standard set as given in the project's strategic plan, and is presented as the
established vocabulary it is. The reel credits Jungian archetype theory as the
origin the branding framework borrowed from, and makes no scholarly claim beyond
that attribution.

The reel renders the set as "Rebel" rather than "Rebel/Outlaw" for on-screen
legibility in a 300px chip. Both names refer to the same archetype.

## Claims about existing tools

B03's description — a short self-report brief in, one label out, a generic
paragraph after — comes from the project's own competitive assessment. It is
stated **descriptively and without naming any product**, for two reasons: Plain
register does not judge design (that is Teardown), and an unnamed generalisation
cannot be checked against a specific vendor's current behaviour, which would date
the video.

## The constructed and illustrative material

Two items could be mistaken for results. Both are captioned on screen:

1. **The $4,000 handbag (B04)** — a hypothetical posed to the viewer as a
   prediction prompt. Not attributed to any real brand.
2. **The Everyman/Ruler tension (B07)** — the example tension given in the
   strategic plan, rendered as an illustration of the *class* of finding the
   method is designed to catch. The beat's `slideMeta` reads *"illustrative
   example — not a produced result."*
3. **The output schema (B08)** — a design target. The file tab reads *"planned
   output schema — a design target, not produced"* and the code block closes with
   `// NOT OUTPUT. This is the shape I am building toward.`

## Honesty position

No capability is claimed. There is no accuracy figure, no benchmark, no user
count, no ship date, and no screenshot of a working system. B10 is a dedicated
status beat carrying two deliberately negative items — "build not started" and
"no results yet" — and BVDT's artifact page ends on "Status: scoped with the
team. Not built. No results yet." so the summary cannot be excerpted as a
capability claim.

## Corrections applied during authoring

- **No competitor named, no quality verdict.** An earlier framing of B03 rated
  existing tools as poorly built. Plain does not judge design, so it now
  describes the mechanism and stops at the mechanical consequence: the loop
  closes on the user's own input.
- **No timeline.** A ship estimate was cut. There is no basis for one at the
  scoping stage, and it would date the video immediately.
- **One inference flag only.** Plain permits exactly one. It sits at B05, on how
  much personality a brand's real artefacts actually encode — the project's
  genuine unknown, and the reason samples precede code.
- **"Rebel" not "Rebel/Outlaw" on screen** — legibility inside a chip; noted
  above so the simplification is on the record.

## Determinism / seeds

| Beat | Seed or determinism note |
|---|---|
| B01 | `seed: "madison-archetype-progress-b01"` — same seed, identical typing performance forever |
| BOUT | polarity seeded by slug `madison-archetype-progress` (`seedHash % 2`); no mascot, so no mascot seed |
| all illustration beats | pure functions of `useP()`; no `Math.random()`, no timers, no CSS transitions |

## Components

Reuse only — **no new components were built**. Every scene was already registered
and confirmed RENDERABLE: `ClaudeComposerAsk`, `BrutalistHesitantWriter`,
`ClaudeScienceChipGrid`, `ClaudeScienceLayerStack`, `ClaudeScienceSourceFlow`,
`BinaryBranch`, `ClaudeVerdictArtifact`, `ClaudeCodeBeat`, plus
`FnCallPredictCard` and `FnCallTitleOutro` from `llm-function-calling`.
