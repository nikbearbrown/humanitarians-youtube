# BUILD-PROMPT — Claude, In Concert (`claude-liam-combining-plugins`)

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives).
Typically under `claude --dangerously-skip-permissions` — the pipeline is git-tracked,
regenerable, and GATE P still requires your signature before any audio spend.

---

```
Build the deep-explainer reel at books/anthropics/books/claude-cowork-plugins/youtube/claude-liam-combining-plugins/.

The plan is authored: read beat_sheet.json, PLAN.md, SOURCES.md, and the book-level
FACTCHECK.md (books/anthropics/books/claude-cowork-plugins/FACTCHECK.md). Then:

1. SCHEMA RECONCILE. Load runtime/schema/beat_sheet.schema.json and conform this
   beat_sheet.json to it exactly — field names, scene keys, shot/vox_run/handoff
   shape. This sheet was authored to the deep-explainer doctrine but may use loose
   field names; fix them to the schema without changing content, lanes, narration,
   or the act order. Keep the spine: ClaudeComposerAsk cold open (ask answered) →
   6 acts → ClaudeVerdictArtifact → ClaudeComposerAsk "Your turn." → ClaudeTitleOutro.

2. LANE-MIX LINT. Run the beat-mix histogram. Authored mix over 32 body beats:
   VOX 7 (21.9%), MANIM 8 (25.0%), REMOTION 10 (31.2%), CARD 7 (21.9%) — all inside
   the deep-explainer bands. No lane runs >2 consecutive except vox_run R1 (B10→B11).
   If the lint disagrees, fix the plan, not the label.

3. GATE P. Present the full narration (B00 → O01) on an animated slate for my
   sign-off. Do NOT generate audio until I approve. Channel is claude-liam:
   Kokoro af_kore, free. No ElevenLabs.

4. AUDIO LOCK. python3 runtime/scripts/generate_audio.py <reel> (Kokoro/af_kore).
   Per-beat mp3 durations become the clock; align writes the word clock. Captions
   via the faster-whisper pipeline.

5. SHOPPING LIST (Gate D2, AFTER audio lock). For every VOX beat (B04, B08, B10,
   B11, B16, B21, B25), first run python3 runtime/scripts/pantry_search.py on its
   pantry_note terms against svg/svg/images/. Copy real matches into pantry/
   pre-checked; write SHOPPING.md from the LOCKED durations for the rest. All seven
   are Tier 1 illustrative (no rights escalation, no real people). B10→B11 is the
   vox_run — source the two stills as one continuous room (doorway → table) so the
   handoff camera move reads.

6. GATE D1 PREVIZ. ./brutalist-art/art run <reel> — full compile, slates in the
   vox slots, Manim/Remotion rendered for real, --review burn-in. This is a previz,
   not a cut. I review pacing and source the stills.

7. PANTRY FILL → REVIEW CUT. After I drop stills into pantry/, re-run (only changed
   slots recompile). Set shot.focus per still; the B25 terracotta bridging arc is
   the drawon annotation, added at previz.

8. VISUAL QC LAW. Frame-level QC pass (CLAUDE-CODE-VISUAL-QC-CHECK.md): sample ≥2fps
   + 15/50/85% of each beat, actually read the PNGs, audit the 9-point rubric, fix
   root causes in scene source, re-render until zero BLOCKER/MAJOR. Log _qc/REPORT.md.

9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH —
   going public is a manual Studio flip.

Manim scenes referenced (build from animated_graphics.py, white canvas, ink + one
terracotta #D97757): branch_route_request, accumulate_both_contribute,
accumulate_research_into_marketing, branch_signals_to_brief, branch_tickets_to_specs,
accumulate_loop_closes, accumulate_merge_brief, accumulate_workflow_to_plugin — all
branch/accumulate patterns, which is the visual grammar of a plugin hand-off.
Remotion: LayerStack, SourceFlow, ChipGrid (the plugins-working-together patterns),
plus the illustration scenes named in the sheet (grounded-vs-generic, two-halves,
informed-vs-instinct, blind-spots) and ClaudeVerdictArtifact / ClaudeComposerAsk /
ClaudeTitleOutro bookends. Retint deck patterns to the claude stage (cream #F2F0E9,
ink #3D3929, accent #D97757) and log the retint.

Honor every parent law: COLD OPEN, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE, ASK→RESULT,
REBUILD, DOUBLE-CHECK, FILL-THE-CANVAS, LOGO, HANDOFF (prompt read + discussed), OUTRO,
VISUAL QC, IN-FOR-BEAR, GATE P. Never hardcode plugin counts, prices, or platform lists;
keep "How a T works" corrected to the STACK framing.
```

---

## Notes for the builder
- **Render happens on your toolkit machine**, not in the authoring sandbox — this
  folder is the complete authoring package (`beat_sheet.json` + plan + sources + this
  prompt); the `art`/Remotion/Manim/Kokoro runtime consumes it. Nothing here is
  rendered; the machine downstream turns these artifacts into `[slug].mp4` +
  `[slug]-slate.mp4`.
- **The hand-off is the whole subject** — every Manim beat is a branch (ask routes to
  the right domain; signals fan into a brief) or an accumulate (two domains merge into
  one answer/brief/calendar). Keep that reading; don't swap them for generic charts.
- **Whole-batch build**: see `youtube/BUILD-ALL.md` at the project root to render all
  reels in chapter order with one paste.
