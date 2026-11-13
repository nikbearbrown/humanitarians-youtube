# SHOTLIST — madison-archetype-progress-week2

Typed work order. 14 beats. Runtime confirmed against measured Kokoro `am_onyx`
mp3s at build time; audio is the clock.

**All 14 slots are FILLED by already-registered Remotion scenes. NO new components
were built.** No open slots, no pantry requests, no human-supplied media.

| # | Beat | Scene | Type | Status |
|---|---|---|---|---|
| 1 | B00 | `ClaudeComposerAsk` | UI — cold open, status stated | FILLED |
| 2 | B01 | `BrutalistHesitantWriter` | UI — BLUF, `built` → `designed` | FILLED |
| 3 | B02 | `FnCallPredictCard` | illustration — predict/commit | FILLED |
| 4 | B03 | `ClaudeScienceLayerStack` | illustration — the three design parts | FILLED |
| 5 | B04 | `ClaudeScienceSourceFlow` | illustration — inputs into the detector | FILLED |
| 6 | B05 | `ClaudeComposerAsk` | UI — ask micro (ASK→RESULT) | FILLED |
| 7 | B06 | `ClaudeCodeBeat` | code — planned scored output | FILLED |
| 8 | B07 | `BinaryBranch` | pattern — keywords vs voice | FILLED |
| 9 | B08 | `ClaudeScienceChipGrid` | illustration — the sample-data blocker | FILLED |
| 10 | B09 | `ClaudeScienceLayerStack` | illustration — the four-rung route | FILLED |
| 11 | B10 | `ClaudeScienceChipGrid` | illustration — honest status board | FILLED |
| 12 | BVDT | `ClaudeVerdictArtifact` | UI — verdict artifact page | FILLED |
| 13 | BHTF | `ClaudeComposerAsk` | UI — handoff + rubric | FILLED |
| 14 | BOUT | `FnCallTitleOutro` | UI — title restate, no mascot | FILLED |

## GATE L — library-first record

Every scene confirmed RENDERABLE **and confirmed to re-time via
`calculateMetadata`** before authoring. Zero misses, zero punts, nothing added to
`TEMPLATE-MISSES.md`, no `scene-index` rebuild needed.

## Regression guards, verified programmatically before the first render

| Prior bug | Guard | Result |
|---|---|---|
| `@NikBearBrown` in the composer chip | `folderLabel` as a **per-beat prop** on B00/B05/BHTF | 0 missing |
| Multi-word `triggerWords` never fired | B01 trigger is one token | `built`, 1 occurrence |
| Typing truncated mid-sentence | `charMs: 22` tuned to fit; final frame sampled after render | visual check |
| Animation truncated at ~50% of the beat | `durationInSeconds` on **every** beat | 0 missing |
| Orphan number on the verdict page | no empty strings in `artifactLines` | 0 empties |
| 12-chip grid colliding with its caption | B08/B10 run `cols=3` with 5 items = two rows | no collision |
| Names that should stay generic | no personal or tool names in the sheet | verified |

## Accent audit — one terracotta moment per beat

| Beat | The single accent |
|---|---|
| B00 | send button arming |
| B01 | "built", marked for deletion (component contract) |
| B02 | the commit line |
| B03 | the evaluation layer rail (`accent: true`) |
| B04 | the first source chip checking off |
| B05 | send button arming |
| B06 | spark line |
| B07 | the resolver card |
| B08 | chip dots as they land |
| B09 | the rung-one rail (`accent: true`) |
| B10 | chip dots as they land |
| BVDT | the artifact heading |
| BHTF | send button arming |
| BOUT | the terminal period |

## Render / compile

- `ART_SCALE=1` pacing cut: **text is not supersampled** — do not judge type
  quality from it and do not ship it as a master.
- `ART_NO_DRAWTEXT=1` — works around the unfixed Windows ffmpeg filtergraph
  font-path bug.
- `PYTHONUTF8=1` — works around the cp1252 `UnicodeEncodeError` on redirected stdout.
- Compiled **WITHOUT `--review`** as requested. That is the master path, so
  `final_frame_check.py` (GATE V) runs as a hard gate and the output lands in
  `<toolkit>/renders/` as `madison-archetype-progress-week2.mp4`, not beside the
  reel. If the gate refuses, the refusal and its flagged frames are reported
  rather than silently falling back to the review path.
- No captions (`metadata.captions: false`). Nothing published.
