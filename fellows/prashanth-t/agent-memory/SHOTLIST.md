# SHOTLIST — agent-memory

Typed work order. 14 beats. Runtime confirmed against measured Kokoro `am_onyx`
mp3s at build time; audio is the clock.

**All 14 slots are FILLED by already-registered Remotion scenes. NO new components
were built** — that was the explicit constraint. No open slots, no pantry requests,
no human-supplied media, so `PROMPTS.md` carries no open-slot prompts.

| # | Beat | Scene | Type | Origin | Status |
|---|---|---|---|---|---|
| 1 | B00 | `ClaudeComposerAsk` | UI — cold open, ask answered honestly | core | FILLED |
| 2 | B01 | `BrutalistHesitantWriter` | UI — BLUF, written + corrected | core | FILLED |
| 3 | B02 | `FnCallPredictCard` | illustration — predict/commit | llm-function-calling | FILLED |
| 4 | B03 | `ClaudeCodeBeat` | code — the re-sent transcript | core | FILLED |
| 5 | B04 | `ClaudeScienceLayerStack` | illustration — the three tiers | shared | FILLED |
| 6 | B05 | `ClaudeScienceChipGrid` | illustration — the window fills | shared | FILLED |
| 7 | B06 | `ClaudeComposerAsk` | UI — ask micro (ASK→RESULT) | core | FILLED |
| 8 | B07 | `ClaudeScienceSourceFlow` | illustration — retrieve into context | shared | FILLED |
| 9 | B08 | `ClaudeCodeBeat` | code — save + retrieve | core | FILLED |
| 10 | B09 | `BinaryBranch` | pattern — store vs no store | shared | FILLED |
| 11 | B10 | `ClaudeScienceChipGrid` | illustration — both failure directions | shared | FILLED |
| 12 | BVDT | `ClaudeVerdictArtifact` | UI — verdict artifact page | core | FILLED |
| 13 | BHTF | `ClaudeComposerAsk` | UI — handoff + rubric | core | FILLED |
| 14 | BOUT | `FnCallTitleOutro` | UI — title restate, no mascot | llm-function-calling | FILLED |

## GATE L — library-first record

Every scene confirmed RENDERABLE via `./art scenes --check` before authoring. Zero
misses, zero punts, nothing added to `TEMPLATE-MISSES.md`, no `./art scene-index`
rebuild needed.

## Every regression from the previous two reels, guarded

Checked programmatically before the first render:

| Prior bug | Guard here |
|---|---|
| Composer chip showed `@NikBearBrown` | `folderLabel: "@HumanitariansAI"` is a **per-beat prop** on B00, B06 and BHTF. Verified: 0 ComposerAsk beats missing it. `metadata.folderLabel` alone is not read by the component |
| Multi-word `triggerWords` silently never fired | B01's trigger is a **single token** (`remembers`), occurring exactly once in the text. Replacement is a phrase, which is allowed |
| Hesitant-writer typing truncated mid-sentence | `charMs: 22`, `mistakeRate: 0`, `hesitateBetween: 4` — tuned to fit the beat. Its final frame is sampled after render, because a gate-clean build does not prove the typing finished |
| Animations truncated at ~50% of the beat | **Every** beat carries `durationInSeconds`. Verified: 0 beats missing it. `ClaudeCodeBeat` got `calculateMetadata` for this reel (default stays 10s, so other reels are unaffected) |
| Orphan "4." on the verdict page | BVDT `artifactLines` contain no empty strings. Verified: 0 empties |
| Review footer / timecode burned in | `metadata.review_labels: false` |

## Layout note

B05 and B10 both run `ChipGrid` at `cols=3` with 5–6 items — two rows, so the
caption slot does not collide (the 12-chip four-row collision found on
madison-archetype-progress does not apply here).

## Accent audit — one terracotta moment per beat

| Beat | The single accent |
|---|---|
| B00 | send button arming |
| B01 | "remembers", marked for deletion (component contract) |
| B02 | the commit line |
| B03 | spark line |
| B04 | the long-term tier rail (`accent: true`) |
| B05 | chip dots as they land |
| B06 | send button arming |
| B07 | the retrieved coffee-order chip checking off |
| B08 | spark line |
| B09 | the resolver card |
| B10 | chip dots as they land |
| BVDT | the artifact heading |
| BHTF | send button arming |
| BOUT | the terminal period |

## Render / compile

- `ART_SCALE=1` pacing cut: **text is not supersampled** — do not judge type
  quality from it, and do not ship it as a master.
- `ART_NO_DRAWTEXT=1` — works around the unfixed Windows ffmpeg filtergraph
  font-path bug; costs the burned-in review timecode, PIL overlays still render.
- `PYTHONUTF8=1` — works around the cp1252 `UnicodeEncodeError` on redirected stdout.
- Compiled **with `--review` plus `review_labels: false`**, which yields a
  footer-free cut that actually writes. Compiling *without* `--review` takes the
  master path, where `final_frame_check.py` exits 2 on the underfill MAJORs these
  shared components always produce and writes no file at all.
- No captions (`metadata.captions: false`). Nothing published.
