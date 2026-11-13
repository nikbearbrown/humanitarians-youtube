# SHOTLIST — madison-archetype-progress

Typed work order. 14 beats, ~191s projected (confirmed against measured Kokoro
`am_onyx` mp3s at build time; audio is the clock).

**All 14 slots are FILLED by already-registered Remotion scenes. NO new
components were built for this reel** — that was the explicit constraint. There
are no open slots, no pantry requests, and no human-supplied media, so
`PROMPTS.md` carries no open-slot prompts.

| # | Beat | Lane | Scene | Type | Reused from | Status |
|---|---|---|---|---|---|---|
| 1 | B00 | remotion | `ClaudeComposerAsk` | UI — cold open, ask lands answered | core | FILLED |
| 2 | B01 | remotion | `BrutalistHesitantWriter` | UI — BLUF, written + corrected | core | FILLED |
| 3 | B02 | remotion | `ClaudeScienceChipGrid` | illustration — 12 archetypes | shared | FILLED |
| 4 | B03 | remotion | `ClaudeScienceLayerStack` | illustration — shallow pipeline | shared | FILLED |
| 5 | B04 | remotion | `FnCallPredictCard` | illustration — predict/commit | llm-function-calling | FILLED |
| 6 | B05 | remotion | `ClaudeScienceSourceFlow` | illustration — artefacts in | shared | FILLED |
| 7 | B06 | remotion | `ClaudeComposerAsk` | UI — ask micro (ASK→RESULT) | core | FILLED |
| 8 | B07 | remotion | `BinaryBranch` | pattern — two readings, one resolver | shared | FILLED |
| 9 | B08 | remotion | `ClaudeCodeBeat` | code — planned output schema | core | FILLED |
| 10 | B09 | remotion | `ClaudeScienceLayerStack` | illustration — scope ladder | shared | FILLED |
| 11 | B10 | remotion | `ClaudeScienceChipGrid` | illustration — status board | shared | FILLED |
| 12 | BVDT | remotion | `ClaudeVerdictArtifact` | UI — verdict artifact page | core | FILLED |
| 13 | BHTF | remotion | `ClaudeComposerAsk` | UI — handoff + rubric | core | FILLED |
| 14 | BOUT | remotion | `FnCallTitleOutro` | UI — title restate, no mascot | llm-function-calling | FILLED |

## GATE L — library-first record

Every scene was confirmed RENDERABLE via `./art scenes --check` before
authoring. Zero misses, zero punts, nothing added to `TEMPLATE-MISSES.md`, and
no `./art scene-index` rebuild was needed.

This reel benefits directly from the duration fix made during
`llm-function-calling`: every shared composition here now re-times to its beat
via `calculateMetadata`, so a 14–20s beat no longer truncates a 30s animation.
`ClaudeCodeBeat` (B08) is the one exception by design — at 300f/10s it completes
inside its beat and then freeze-holds.

## Layout constraint found before rendering

B02 shows all twelve archetypes. `ChipGrid` geometry is `cw=300, gapX=46`, so:

- `cols=4` → `gridW=1338` on a 1280 stage → `x0=-29`, content off-canvas. **Edge-bleed BLOCKER. Rejected.**
- `cols=3` → `gridW=992`, `x0=144`, 4 rows ending at y=678 (inside the 684 safe
  limit) — but the caption slot sits at `bottom:92`, whose top is ~y=598 and
  collides with row four.

**Resolution:** `cols=3` with **no caption**; the clarifier moved to the spark
line (`"Twelve slots."`). B10's five-chip board keeps its caption — two rows
only, no collision.

## Accent audit — one terracotta moment per beat

| Beat | The single accent |
|---|---|
| B00 | send button arming |
| B01 | "quiz", marked for deletion (component contract) |
| B02 | chip dots turning as each lands — no competing focal element |
| B03 | none accented, deliberately: none of the three steps is the answer |
| B04 | the commit line |
| B05 | the first artefact chip checking off |
| B06 | send button arming |
| B07 | the resolver card |
| B08 | spark line |
| B09 | the Ruler layer rail (`accent: true`) |
| B10 | chip dots as they land |
| BVDT | the artifact heading |
| BHTF | send button arming |
| BOUT | the terminal period |

## Render notes

- `ART_SCALE=1` pacing cut: **text is not supersampled** — do not judge type
  quality from it and do not ship it as a master.
- `ART_NO_DRAWTEXT=1` — works around the unfixed Windows ffmpeg font-path bug;
  costs the burned-in review timecode, PIL label overlays still render.
- `PYTHONUTF8=1` — works around the cp1252 `UnicodeEncodeError` on redirected
  stdout.
- No captions (`metadata.captions: false`). Review cut only; `./art final` is
  not run and nothing is published.
