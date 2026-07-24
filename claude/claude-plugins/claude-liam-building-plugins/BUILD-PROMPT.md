# BUILD-PROMPT — Claude, Built (`claude-liam-building-plugins`)

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives).
Typically under `claude --dangerously-skip-permissions` — the pipeline is git-tracked,
regenerable, and GATE P still requires your signature before any audio spend.

---

```
Build the deep-explainer reel at books/anthropics/books/claude-cowork-plugins/youtube/claude-liam-building-plugins/.

The plan is authored: read beat_sheet.json, PLAN.md, SOURCES.md, and the book-level
FACTCHECK.md (books/anthropics/books/claude-cowork-plugins/FACTCHECK.md). Then:

1. SCHEMA RECONCILE. Load runtime/schema/beat_sheet.schema.json and conform this
   beat_sheet.json to it exactly — field names, scene keys, shot/vox_run/handoff
   shape. This sheet was authored to the deep-explainer doctrine but may use loose
   field names; fix them to the schema without changing content, lanes, narration,
   or the act order. Keep the spine: ClaudeComposerAsk cold open (ask answered) →
   body → ClaudeVerdictArtifact → ClaudeComposerAsk "Your turn." → ClaudeTitleOutro.

2. LANE-MIX LINT. Run the beat-mix histogram. Body = 30 beats: VOX 6 (20.0%),
   MANIM 8 (26.7%), REMOTION 10 (33.3%), CARD 6 (20.0%) — all inside target. No lane
   run exceeds 2 consecutive beats except vox run R1 (B03→B04), which is allowed.
   Confirm the histogram still holds after schema reconcile; do not rebalance.

3. GATE P. Present the full narration (B00 → O01) on an animated slate for my
   sign-off. Do NOT generate audio until I approve. Channel is claude-liam:
   Kokoro af_kore, free. No ElevenLabs. IN-FOR-BEAR LAW: B00 opens "Hej — this is
   Kore, in for Humanitarians AI." and the outro signs off "Kore, in for Humanitarians AI."

4. AUDIO LOCK. python3 runtime/scripts/generate_audio.py <reel> (Kokoro/af_kore).
   Per-beat mp3 durations become the clock; align writes the word clock. Captions
   via the faster-whisper pipeline.

5. SHOPPING LIST (Gate D2, AFTER audio lock). For every VOX beat (B03, B04, B08,
   B13, B18, B23), first run python3 runtime/scripts/pantry_search.py on its
   pantry_note terms against svg/svg/images/. Copy real matches into pantry/
   pre-checked; write SHOPPING.md from the LOCKED durations for the rest. All six
   are Tier 1 illustrative (no rights escalation, no real people, no logos). B03→B04
   are a continuity pair (vox run R1) — source them together so the room grammar
   matches.

6. GATE D1 PREVIZ. ./brutalist-art/art run <reel> — full compile, slates in the
   vox slots, Manim/Remotion rendered for real, --review burn-in. This is a previz,
   not a cut. I review pacing and source the stills.

7. PANTRY FILL → REVIEW CUT. After I drop stills into pantry/, re-run (only changed
   slots recompile). Set shot.focus per still; honor the R1 handoff (B03 camera +
   'operator' object pin B04's first frame).

8. VISUAL QC LAW. Frame-level QC pass (CLAUDE-CODE-VISUAL-QC-CHECK.md): sample >=2fps
   + 15/50/85% of each beat, actually read the PNGs, audit the 9-point rubric, fix
   root causes in scene source, re-render until zero BLOCKER/MAJOR. Log _qc/REPORT.md.

9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH —
   going public is a manual Studio flip.

Manim scenes referenced (build from animated_graphics.py, white canvas, ink + one
terracotta #D97757): transfer_head_to_package, variance_to_consistency,
subagents_fan_out, accumulate_build_steps, compress_hours_to_minutes,
replicate_clone_runs, divergence_admin_vs_judgment, accumulate_evolve_over_weeks.
Remotion: ChipGrid (B06 components, B17 signals), SourceFlow (B10 connectors,
B22 share), LayerStack (B15 assemble), code-block (Onda) for REAL structure only —
B07 folder tree, B09 slash commands — plus the three illustration scenes named in the
sheet (off-the-shelf-vs-yours, conversation-not-code, check-before-you-build). Retint
deck patterns to the claude stage (cream #F2F0E9, ink #3D3929, accent #D97757) and
log the retint.

ILLUSTRATE / prose-as-code guard: never box the conversational describe-prompt as
code — Onda code-block carries only real file/structure content (B07, B09).

Honor every parent law: COLD OPEN, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE, ASK→RESULT,
REBUILD, DOUBLE-CHECK, FILL-THE-CANVAS, LOGO, HANDOFF (prompt read + discussed), OUTRO,
VISUAL QC, IN-FOR-BEAR, GATE P. Never hardcode plugin counts, prices, platform lists,
or directory URLs.
```

---

## Notes for the builder
- **Render happens on your toolkit machine**, not in the authoring sandbox — this
  folder is the complete authoring package (`beat_sheet.json` + plan + sources + this
  prompt); the `art`/Remotion/Manim/Kokoro runtime consumes it. Nothing here renders
  in place; the toolkit machine holds `brutalist-art/`, `runtime/`, the Manim
  `animated_graphics.py`, the Remotion scenes, and the Kokoro pipeline.
- Whole-batch build: see `youtube/BUILD-ALL.md` at the project root to render all
  reels in chapter order with one paste.
