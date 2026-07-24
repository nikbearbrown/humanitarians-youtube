# BUILD-PROMPT — Claude, Counsel (`claude-liam-legal-finance`)

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives).
Typically under `claude --dangerously-skip-permissions` — the pipeline is git-tracked,
regenerable, and GATE P still requires your signature before any audio spend.

---

```
Build the deep-explainer reel at books/anthropics/books/claude-cowork-plugins/youtube/claude-liam-legal-finance/.

The plan is authored: read beat_sheet.json, PLAN.md, SOURCES.md, and the book-level
FACTCHECK.md (books/anthropics/books/claude-cowork-plugins/FACTCHECK.md). Then:

1. SCHEMA RECONCILE. Load runtime/schema/beat_sheet.schema.json and conform this
   beat_sheet.json to it exactly — field names, scene keys, shot/vox_run/handoff
   shape. This sheet was authored to the deep-explainer doctrine but may use loose
   field names; fix them to the schema without changing content, lanes, narration,
   or the act order. Keep the spine: ClaudeComposerAsk cold open (ask answered,
   greeting "Shalom") → 6 acts → ClaudeVerdictArtifact → ClaudeComposerAsk "Your
   turn." → ClaudeTitleOutro. This chapter is TWO separate plugins (legal, finance)
   in one episode — never merge them into a single "Legal and Finance plugin" in any
   card, label, or line. Legal owns Acts II–III, finance owns Acts IV–V.

2. LANE-MIX LINT. Run the beat-mix histogram over the 30 body beats (B00/V01/H01/O01
   exempt). Expected: VOX 7 (23.3%), MANIM 8 (26.7%), REMOTION 9 (30.0%), CARD 6
   (20.0%) — all in-band. Confirm the only consecutive-VOX pair is the authored run
   R1 (B11→B12); every other VOX beat is a hard cut.

3. GATE P. Present the full narration (B00 → O01) on an animated slate for my
   sign-off. Do NOT generate audio until I approve. Channel is claude-liam:
   Kokoro am_onyx, free. No ElevenLabs. Confirm the two hard-limit caveats land as
   their own acts — "screening tool, not a lawyer" (Act III) and "accelerator, not a
   CFO" (Act V) — and that no plugin count, price, or platform list appears anywhere.

4. AUDIO LOCK. python3 runtime/scripts/generate_audio.py <reel> (Kokoro/am_onyx).
   Per-beat mp3 durations become the clock; align writes the word clock. Captions
   via the faster-whisper pipeline.

5. SHOPPING LIST (Gate D2, AFTER audio lock). For every VOX beat (B02, B05, B11, B12,
   B14, B20, B24), first run python3 runtime/scripts/pantry_search.py on its
   pantry_note terms against svg/svg/images/. Copy real matches into pantry/
   pre-checked; write SHOPPING.md from the LOCKED durations for the rest. All seven
   are Tier 1 illustrative (no rights escalation, no real people, no logos, no real
   party names or financial figures). B05 and B20 are drawon beats — the terracotta
   highlight/ring is added at previz, the still is clean.

6. GATE D1 PREVIZ. ./brutalist-art/art run <reel> — full compile, slates in the
   vox slots, Manim/Remotion rendered for real, --review burn-in. This is a previz,
   not a cut. I review pacing and source the stills.

7. PANTRY FILL → REVIEW CUT. After I drop stills into pantry/, re-run (only changed
   slots recompile). Set shot.focus per still; preserve the R1 handoff (B11→B12) so
   the push from the flagged clause to counsel stays continuous.

8. VISUAL QC LAW. Frame-level QC pass (CLAUDE-CODE-VISUAL-QC-CHECK.md): sample >=2fps
   + 15/50/85% of each beat, actually read the PNGs, audit the 9-point rubric, fix
   root causes in scene source, re-render until zero BLOCKER/MAJOR. Log _qc/REPORT.md.

9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH —
   going public is a manual Studio flip.

Manim scenes referenced (build from animated_graphics.py, cream canvas, ink + one
terracotta #D97757): coverage_net_firstpass (filter), legal_flag_counts (state —
green/yellow/red, tallies illustrative), threshold_hours_to_minutes (threshold),
branch_routine_vs_highstakes (branch), runway_burn_depletion (depletion),
scenario_model_payback (best/likely/worst → break-even), branch_analysis_to_human
(branch), cost_rises_the_later (growth). Remotion: PredictCard, ChipGrid (x5),
code-block (Onda, B06 + B15), plus the illustration scene three-habits-triptych.
Retint deck patterns to the claude stage (cream #F2F0E9, ink #3D3929, accent
#D97757) and log the retint.

Honor every parent law: COLD OPEN, ILLUSTRATE (legal/finance concept-illustrated —
the Claude UI appears only in the two Onda code-blocks where the prompt IS the
subject), SHOW-DON'T-TELL, SPARK-LINE, ASK->RESULT, REBUILD, DOUBLE-CHECK,
FILL-THE-CANVAS, LOGO, HANDOFF (prompt read in full + discussed), OUTRO, VISUAL QC,
IN-FOR-BEAR, GATE P. Never hardcode plugin counts, prices, or platform lists; keep
the "15%" and the contractor as explicitly illustrative examples.
```

---

## Notes for the builder
- **Render happens on your toolkit machine**, not in the authoring sandbox — this
  folder is the complete authoring package (`beat_sheet.json` + plan + sources + this
  prompt); the `art`/Remotion/Manim/Kokoro runtime consumes it. Nothing here renders
  in place.
- **Two plugins, one reel.** The single most important content guardrail: legal and
  finance are separate official plugins. Keep them separate in every card and line;
  the reel's job is to show they SHARE a pattern (screen + accelerate, human keeps the
  call), not that they are one tool.
- Whole-batch build: see `youtube/BUILD-ALL.md` at the project root to render all
  reels in chapter order with one paste.
