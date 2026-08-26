# Feedback: "Upload to GitHub. No Code." — Sanjana / @HumanitariansAI, film 1 (v3)

**Verdict:** clear-for-public. **Teaching 11/12. Production gate PASS.**

## What changed vs v2
- **Intro & outro** now reuse the exact reference-video Claude scenes (`ClaudeComposerAsk` + `ClaudeTitleOutro`, EB Garamond loaded via `fonts.tsx`) — brand-consistent with the fellow's own uploads.
- **Personal open:** the intro voices **"Hi, I'm Sanjana. This video is about…"** — a named host, per PROOF's "a face/voice earns trust" note.
- **New Step 1 — create a branch:** the branch dropdown → type name → *Create branch from 'main'*, so the "you're on your own branch" claim in later steps is now *shown*, not assumed (tightens the worked-example spine to a full 7 steps).
One line: *This film teaches non-coders the exact 7-step web flow to push a folder to GitHub — drag-and-drop and all — anchored on a reusable rule (text&<25MB→GitHub, video→Drive), stress-tested with an edge case, and closed on a copyable scaffold, now with a voiceover cut to the visuals.*

## What changed vs v1
- **Audio added** — Kokoro `af_bella` voiceover is the master clock; scenes are cut to the narration, with SFX (clacks, chimes, whooshes).
- **Restyled** to the **Claude palette** (cream + terracotta) with realistic **light-theme** GitHub/Drive/Explorer UI.
- **New content** the user requested: the **Windows/Mac folder drag-and-drop** flow (Explorer → drag whole folder → paths preserved → progress), the **Add file → Upload files** menu, **commit directly to your branch**, the **PR** flow with named reviewers, and a **gotchas** beat (25 MB / 100-file limits; Chrome/Edge vs Firefox/Safari).

## Rubric
| Criterion | This cut |
|---|---|
| Explicit framework | **2** — Golden Rule shown before any step. |
| Reusable rubric | **2** — "text & <25 MB → GitHub, video/big → Drive" applies to any new file. |
| Worked example | **2** — the full 7-step flow walked live on realistic UI, narrated. |
| Falsifiability / edge | **2** — 30 MB README edge case + the gotchas (size/browser limits). |
| Active task | **2** — copyable README scaffold + "message Sanjana with both links." |
| Friction | **1** — narration mostly tells; the viewer receives more than they decide. |

**Total: 11/12** (ship bar ≥ 8 ✓)

## Production gate
- **Legible at assertion** — PASS. Instruction bands (ink on cream, ~5% frame height) + light UI verified on encoded 4K frames.
- **Sources on screen** — PASS. Real repo path in every chrome bar; the GitHub/Drive/Explorer artifact is shown, not paraphrased.
- **Side-by-side** — PASS. Golden Rule holds GitHub vs Drive together.
- **Audio/video sync** — PASS. Timings are generated from the narration durations, so voice and visuals cannot drift.

## Remaining path to 12/12 (optional)
Friction is the last point. To lift it, add a 2-second "GitHub or Drive?" hold on a sample file before the reveal, so the viewer commits to a choice rather than receiving it.

## What works (keep)
- The **Claude cream + light-UI** treatment reads as premium and calm while staying a realistic tutorial.
- **Step 4 drag-and-drop**: the cursor dragging the `sanjana-rao` folder chip into the dashed box, then the file list with `sanjana-rao/…` paths preserved and progress bars — this is the clearest possible demo of the one thing fellows get wrong.
- Voiceover + on-screen bands doubly encode every instruction (heard *and* read).
