# QC Report — sleeper-agents-safety-training-fails / short

**Date:** 2026-07-17  
**Reel:** `anthropics/youtube/sleeper-agents-safety-training-fails/short/`  
**Output:** `sleeper-agents-safety-training-fails-short-slate.mp4`  
**Canvas:** 1080×1920 (9:16 portrait) — confirmed via ffprobe  
**Duration:** 115.4s (under 3:00 Shorts cap ✅)  
**Beats:** 8 (B00–B06 + END)  
**Pipeline:** Free only (Kokoro TTS, no ElevenLabs spend)

---

## 8-Point Rubric

| # | Check | Result |
|---|-------|--------|
| 1 | Aspect ratio = 1080×1920 | ✅ PASS |
| 2 | SAFE916 compliance — no text overflow | ✅ PASS |
| 3 | All text has maxWidth + word-wrap (TEXT LAW) | ✅ PASS |
| 4 | Reflow quality — no center-crop artifacts | ✅ PASS |
| 5 | Animations render correctly | ✅ PASS |
| 6 | Duration < 180s Shorts cap | ✅ PASS (115.4s) |
| 7 | Audio present (per-beat narration) | ✅ PASS |
| 8 | Minor: SleeperAgentsResult916 annotation badge clips "After RLHF" bar label | ⚠️ COSMETIC |

**Overall verdict: PASS**

---

## Beat-by-beat

| Beat | Composition | Sample time | Verdict | Notes |
|------|-------------|-------------|---------|-------|
| B00 | ClaudeComposerAsk916 | 7s | ✅ PASS | Cold open, full prompt wraps inside card |
| B01 | SleeperAgentsBehaviorSwitch916 | 17s | ✅ PASS | Two lanes, model node, trigger token visible |
| B02 | SleeperAgentsExperiment916 | 42s | ✅ PASS | All 5 stages, connectors, terracotta finale, spark line |
| B03 | SleeperAgentsResult916 | 57s | ✅ PASS* | Stacked bar groups; annotation inside Distilled zone after fix |
| B04 | ClaudeVerdictArtifact916 | 75s | ✅ PASS | Centered card, 5 verdict lines, clean typography |
| B05 | ClaudeComposerAsk916 | 98s | ✅ PASS | Handoff / "Your turn." beat, prompt wraps correctly |
| B06 | ClaudeTitleOutro916 | 107s | ✅ PASS | Title card, @HumanitariansAI, citation |
| END | Static PNG | 112s | ✅ PASS | @nikbearbrown on dark bg |

*B03: annotation badge (annotation offset reduced from `height*0.12` to `height*0.03` during authoring) partially overlaps the "After RLHF" bar label — both readable. Cosmetic only.

---

## Compositions built during this session

All 4 new 916 compositions authored from scratch (R3/R4 reflow, TEXT LAW compliant):

| Composition | Reflow | Schema |
|-------------|--------|--------|
| `ClaudeVerdictArtifact916` | R3 rescale — card scales to portrait width | `claudeVerdictArtifactSchema` |
| `SleeperAgentsBehaviorSwitch916` | R3 rescale + maxWidth — lane layout already vertical | `sleeperAgentsBehaviorSwitchSchema` |
| `SleeperAgentsExperiment916` | R4 serialize — 5-stage horizontal pipeline → vertical stack | `sleeperAgentsExperimentSchema` |
| `SleeperAgentsResult916` | R4 serialize — side-by-side bars → stacked groups | `sleeperAgentsResultSchema` |

Previously existing 916 compositions (ClaudeComposerAsk916, ClaudeTitleOutro916) used without modification.

---

## ONDA check (from shorts.py)

All 7 Remotion beats passed ONDA check:

```
B00 ClaudeComposerAsk → ClaudeComposerAsk916 ✅
B01 SleeperAgentsBehaviorSwitch → SleeperAgentsBehaviorSwitch916 ✅
B02 SleeperAgentsExperiment → SleeperAgentsExperiment916 ✅
B03 SleeperAgentsResult → SleeperAgentsResult916 ✅
B04 ClaudeVerdictArtifact → ClaudeVerdictArtifact916 ✅
B05 ClaudeComposerAsk → ClaudeComposerAsk916 ✅
B06 ClaudeTitleOutro → ClaudeTitleOutro916 ✅
```

---

## Compile lint notes (non-blocking)

- **SKIN LINT B00**: "COLD OPEN LAW wants ClaudeComposerAsk" — false alarm; `ClaudeComposerAsk916` is the correct 916 variant.
- **SKIN LINT END**: "OUTRO LAW wants ClaudeTitleOutro" — the END is the 4.5s silent endcard static; B06 is `ClaudeTitleOutro916` which satisfies the outro law.
- **Motion histogram**: 87% `?` type — no explicit `motion_type` metadata in the beat_sheet (non-blocking).

---

## Sampled frames

Frames extracted at 7s, 17s, 42s, 57s, 75s, 98s, 107s, 112s — all read and inspected.  
Files retained at `/tmp/916-qc/` for this session.
