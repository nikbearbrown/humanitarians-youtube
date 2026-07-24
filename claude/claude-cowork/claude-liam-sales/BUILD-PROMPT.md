# BUILD-PROMPT — Claude, Closing (`claude-liam-sales`)

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives).
Typically under `claude --dangerously-skip-permissions` — the pipeline is git-tracked,
regenerable, and GATE P still requires your signature before any audio spend.

---

```
Build the deep-explainer reel at books/anthropics/books/claude-cowork-plugins/youtube/claude-liam-sales/.

The plan is authored: read beat_sheet.json, PLAN.md, SOURCES.md, and the book-level
FACTCHECK.md (books/anthropics/books/claude-cowork-plugins/FACTCHECK.md). Then:

1. SCHEMA RECONCILE. Load runtime/schema/beat_sheet.schema.json and conform this
   beat_sheet.json to it exactly — field names, scene keys, shot/vox_run/handoff
   shape. This sheet was authored to the deep-explainer doctrine but may use loose
   field names; fix them to the schema without changing content, lanes, narration,
   or the act order. Keep the spine: ClaudeComposerAsk cold open (ask answered) →
   body → ClaudeVerdictArtifact → ClaudeComposerAsk "Your turn." → ClaudeTitleOutro.

2. LANE-MIX LINT. Run the beat-mix histogram over body beats only (bookends exempt).
   Expect VOX 6/30 = 20%, MANIM 8/30 = 27%, REMOTION 9/30 = 30%, CARD 7/30 = 23% —
   all inside target. Confirm no run of >2 same-lane beats except vox run R1
   (B12→B13). If the lint disagrees, fix the plan, not the label.

3. GATE P. Present the full narration (B00 → O01) on an animated slate for my
   sign-off. Do NOT generate audio until I approve. Channel is claude-liam:
   Kokoro af_kore, free. No ElevenLabs.

4. AUDIO LOCK. python3 runtime/scripts/generate_audio.py <reel> (Kokoro/af_kore).
   Per-beat mp3 durations become the clock; align writes the word clock. Captions
   via the faster-whisper pipeline.

5. SHOPPING LIST (Gate D2, AFTER audio lock). For every VOX beat (B03, B12, B13,
   B18, B22, B24), first run python3 runtime/scripts/pantry_search.py on its
   pantry_note terms against svg/svg/images/. Copy real matches into pantry/
   pre-checked; write SHOPPING.md from the LOCKED durations for the rest. All six
   are Tier 1 illustrative (no rights escalation, no real people). B12→B13 is vox
   run R1 — the two stills must share room/duotone grammar; honor the handoff
   block on B12.

6. GATE D1 PREVIZ. ./brutalist-art/art run <reel> — full compile, slates in the
   vox slots, Manim/Remotion rendered for real, --review burn-in. This is a previz,
   not a cut. I review pacing and source the stills.

7. PANTRY FILL → REVIEW CUT. After I drop stills into pantry/, re-run (only changed
   slots recompile). Set shot.focus per still; B18 gets the terracotta drawon ring.

8. VISUAL QC LAW. Frame-level QC pass (CLAUDE-CODE-VISUAL-QC-CHECK.md): sample ≥2fps
   + 15/50/85% of each beat, actually read the PNGs, audit the 9-point rubric, fix
   root causes in scene source, re-render until zero BLOCKER/MAJOR. Log _qc/REPORT.md.

9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH —
   going public is a manual Studio flip.

Manim scenes referenced (build from animated_graphics.py, white canvas, ink + one
terracotta #D97757): range_solo_to_org, accumulate_prep_sheet, scatter_to_pipeline,
assemble_briefing, threshold_three_days_to_five_minutes, sort_pipeline_review,
threshold_stock_vs_configured, accumulate_wins. Remotion: ChipGrid, PredictCard,
SourceFlow, code-block (Onda), ClaudeVerdictArtifact, plus the illustration scenes
named in the sheet (notes-to-message, cold-outreach-personal). Retint deck patterns
to the claude stage (cream #F2F0E9, ink #3D3929, accent #D97757) and log the retint.

Honor every parent law: COLD OPEN, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE, ASK→RESULT,
REBUILD, DOUBLE-CHECK, FILL-THE-CANVAS, LOGO, HANDOFF (prompt read + discussed), OUTRO,
VISUAL QC, IN-FOR-BEAR, GATE P. Never hardcode plugin counts, prices, or platform lists;
Salesforce/HubSpot appear only as fleeting examples, never a beat's subject.
```

---

## Notes for the builder
- **Render happens on your toolkit machine**, not in the authoring sandbox — this
  folder is the complete authoring package (`beat_sheet.json` + plan + sources + this
  prompt); the `art`/Remotion/Manim/Kokoro runtime consumes it. Nothing here compiles
  in place; the machine with `brutalist-art/` and `runtime/` does the compile.
- Whole-batch build: see `youtube/BUILD-ALL.md` at the project root to render all 14
  reels in chapter order with one paste.
