# SHOTLIST — llm-function-calling

Typed work order. 14 beats, 201.0s measured (Kokoro `am_onyx`; audio is the clock).

**All 14 slots are FILLED by deterministic Remotion scenes. There are no open
slots, no pantry requests, and no human-supplied media.** Nothing in this reel
is a slate awaiting media, so `PROMPTS.md` carries no open-slot prompts.

| # | Beat | Dur | Lane | Scene | Type | Status |
|---|---|---|---|---|---|---|
| 1 | B00 | 16.00s | remotion | `ClaudeComposerAsk` | UI — cold open, ask lands answered | FILLED |
| 2 | B01 | 10.05s | remotion | `BrutalistHesitantWriter` | UI — BLUF, written + corrected | FILLED |
| 3 | B02 | 15.04s | remotion | `FnCallPredictCard` | illustration — predict/commit | FILLED |
| 4 | B03 | 14.34s | remotion | `ClaudeScienceChipGrid` | illustration — 5 chips | FILLED |
| 5 | B04 | 15.45s | remotion | `FnCallLoop` | illustration — framework figure | FILLED |
| 6 | B05 | 18.24s | remotion | `ClaudeScienceSourceFlow` | illustration — defs into context | FILLED |
| 7 | B06 | 5.03s | remotion | `ClaudeComposerAsk` | UI — ask micro-beat (ASK→RESULT) | FILLED |
| 8 | B07 | 17.34s | remotion | `FnCallLoop` | illustration — worked example | FILLED |
| 9 | B08 | 15.45s | remotion | `ClaudeCodeBeat` | code — the message list | FILLED |
| 10 | B08B | 16.32s | remotion | `ClaudeScienceLayerStack` | illustration — rounds stacking | FILLED |
| 11 | B09 | 16.90s | remotion | `BinaryBranch` | pattern — two failure directions | FILLED |
| 12 | BVDT | 16.62s | remotion | `ClaudeVerdictArtifact` | UI — verdict artifact page | FILLED |
| 13 | BHTF | 21.29s | remotion | `ClaudeComposerAsk` | UI — handoff + rubric | FILLED |
| 14 | BOUT | 2.94s | remotion | `FnCallTitleOutro` | UI — title restate | FILLED |

## Components built for this reel

Three GATE L misses, built rather than slated. Reasoning in
`runtime/remotion/src/FnCalling.tsx`; registered in `Root.tsx` and confirmed
RENDERABLE via `./art scenes --check`.

| Component | Canvas | Why it was not in the library |
|---|---|---|
| `FnCallLoop` | 1280×720 | No component expresses a four-stage round trip with a return leg; `SourceFlow` is one-directional |
| `FnCallPredictCard` | 1280×720 | `PredictCard` existed only as the `Illu-PredictCard` Studio preview with baked props |
| `FnCallTitleOutro` | 1920×1080 | `ClaudeTitleOutro` hardcodes `@NikBearBrown` + mascot, both locked to that channel |

## Components reused unchanged

`ClaudeComposerAsk` ×3 · `BrutalistHesitantWriter` · `ClaudeScienceChipGrid` ·
`ClaudeScienceSourceFlow` · `ClaudeScienceLayerStack` · `ClaudeCodeBeat` ·
`BinaryBranch` · `ClaudeVerdictArtifact`

## Accent audit — one terracotta moment per beat

| Beat | The single accent |
|---|---|
| B00 | send button arming |
| B01 | the phrase marked for deletion (component contract) |
| B02 | the commit line |
| B03 | none highlighted — the point is that none is available; caption carries the turn |
| B04 | the dashed return leg |
| B05 | `get_weather` checking off as the match |
| B06 | send button arming |
| B07 | stage 2 (`active: 1`) — the request, the beat's claim |
| B08 | spark line |
| B08B | round 3 card (`accent: true`) |
| B09 | the resolver card |
| BVDT | the artifact heading |
| BHTF | send button arming |
| BOUT | the terminal period |

## Render notes

- Remotion beats render at `--scale=2` and conform to the 1920×1080 reel canvas.
  The 1280×720 illustration stages scale uniformly, so composition and type
  proportions are preserved.
- No captions (`metadata.captions: false`), per the build request.
- Review cut only. `./art final` is not run; nothing is published.
