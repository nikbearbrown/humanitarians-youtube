# BUILD-PROMPT — The Tier That Grades the Papers

Paste into Claude Code from `books/` (typically `claude --dangerously-skip-permissions`):

```
Build the hai ai-explainer reel "The Tier That Grades the Papers" from scratch.

Ground truth, read first:
1. brutalist/youtube/kk_brutalist/beat_sheet.hai.json — the master; narration approved (GATE P, see NARRATION-GATE-P.md).
2. brutalist/youtube/kk_brutalist/PEDAGOGY.md + FACTCHECK.md — the gates and the sourced verdicts.
3. brutalist/skills/make/ai-explainer/SKILL.md + brutalist/skills/make/hai/SKILL.md — the laws, incl. ILLUSTRATE LAW and the humanitarians palette spec.
4. The example this mirrors: brutalist/examples/ai-explainer/claude-debunked/ — beat_sheet.json + remotion-src/Wheel.tsx for the exact grade/startAt/focus prop contract TierPyramid.tsx should copy.

Steps:
1. Build brutalist/runtime/remotion/src/scenes/TierPyramidBeat.tsx — a Remotion component with props { sparkLine, pyramid: { grade: bool, startAt: number, focus?: "methods"|"studies"|"diagnosis"|"fix" } }. Renders a 3-tier pyramid/ladder (Tier 1 top, empty — no study reaches it; Tier 2 middle, holds Dong et al. + Huang et al. near the boundary; Tier 3 base, most of the field) in the humanitarians palette (cream #F3EBDD ground, ink #2F2A26, teal #1F4E5F confirmed/validated, crimson #E4572E red-flag/unresolved, slate #29335C structure, gold #F3A712 highlight-only). grade:false = empty scale, no studies plotted. grade:true + focus="methods" highlights the SVM/RF vs. CNN/transformer comparison off to the side of the pyramid; focus="studies" plots Dong et al. and Huang et al. into their tiers with labels; focus="diagnosis" and focus="fix" can dim the pyramid and foreground a small paper-icon element representing the draft being checked (do not overload the pyramid itself with Kumar's story — keep the two visually distinct per PEDAGOGY.md's scoping note). Same grade/startAt/focus contract as Wheel.tsx — copy its animation timing logic, not its visual content.
2. Audio: python3 runtime/scripts/generate_audio_kokoro.py youtube/kk_brutalist/ --sheet beat_sheet.hai.json — voice am_onyx (already generated, ground-truth durations locked in the beat sheet — this step is a no-op unless audio needs regenerating). GATE P already passed (see NARRATION-GATE-P.md VERDICT: PASS) — confirm before any spend regardless.
3. Render: ./art run youtube/kk_brutalist — the fast draft compile, for eyeballing pacing and the new TierPyramidBeat component before committing to a full master.
4. Once the draft looks right: ./art final youtube/kk_brutalist — the clean 4K master (GATE T). If this blocks on a missing or failing TYPECHECK.md, STOP and report back rather than working around it — do not fabricate a passing TYPECHECK.md to force the gate.
5. Do NOT run ./art post or anything in RENDER-4K-AND-UPLOAD.md Part 2/3 — this video is not going through the shared YouTube publishing pipeline. The output stays local in the reel folder for human review, per house law (never publish).
6. QC: ffprobe on the 4K master; stills of B00 (result lines), B01 assemble, B02 methods-focus, B03 studies-focus, B04 predict, B05 diagnosis-focus, B06 fix-focus, verdict page, handoff, outro. Run the full VISUAL QC LAW frame-level pass (CLAUDE-CODE-VISUAL-QC-CHECK.md) — note the FILL-THE-CANVAS legibility check matters more at 4K, not less.
7. Report and STOP. Never publish.
```
