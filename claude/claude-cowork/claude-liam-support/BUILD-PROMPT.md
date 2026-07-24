# BUILD-PROMPT — Claude, On Call (`claude-liam-support`)

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives).
Typically under `claude --dangerously-skip-permissions` — the pipeline is git-tracked,
regenerable, and GATE P still requires your signature before any audio spend.

---

```
Build the deep-explainer reel at books/anthropics/books/claude-cowork-plugins/youtube/claude-liam-support/.

The plan is authored: read beat_sheet.json, PLAN.md, SOURCES.md, and the book-level
FACTCHECK.md (books/anthropics/books/claude-cowork-plugins/FACTCHECK.md). Then:

1. SCHEMA RECONCILE. Load runtime/schema/beat_sheet.schema.json and conform this
   beat_sheet.json to it exactly — field names, scene keys, shot/vox_run/handoff
   shape. This sheet was authored to the deep-explainer doctrine but may use loose
   field names; fix them to the schema without changing content, lanes, narration,
   or the act order. Keep the spine: ClaudeComposerAsk cold open (ask answered) →
   body → ClaudeVerdictArtifact → ClaudeComposerAsk "Your turn." → ClaudeTitleOutro.

2. LANE-MIX LINT. Run the beat-mix histogram over the 24 body beats. Authored mix:
   VOX 5 (20.8%), MANIM 6 (25.0%), REMOTION 8 (33.3%), CARD 5 (20.8%) — all in band.
   Confirm no non-vox-run lane runs >2 consecutive; the only 2-beat repeat (B13→B14)
   is the intended vox run R1. Do not pad: this is the book's shortest chapter and
   the reel is meant to land short (~4:00).

3. GATE P. Present the full narration (B00 → O01) on an animated slate for my
   sign-off. Do NOT generate audio until I approve. Channel is claude-liam:
   Kokoro am_onyx, free. No ElevenLabs.

4. AUDIO LOCK. python3 runtime/scripts/generate_audio.py <reel> (Kokoro/am_onyx).
   Per-beat mp3 durations become the clock; align writes the word clock. Captions
   via the faster-whisper pipeline.

5. SHOPPING LIST (Gate D2, AFTER audio lock). For every VOX beat (B01, B08, B13,
   B14, B18) first run python3 runtime/scripts/pantry_search.py on its pantry_note
   terms against svg/svg/images/. Copy real matches into pantry/ pre-checked; write
   SHOPPING.md from the LOCKED durations for the rest. All five are Tier 1
   illustrative (no rights escalation, no real people). B13→B14 is vox run R1 —
   author the two stills as one continuous desk scene (declined-payment screen →
   drafted reply); honor the handoff block on B13.

6. GATE D1 PREVIZ. ./brutalist-art/art run <reel> — full compile, slates in the
   vox slots, Manim/Remotion rendered for real, --review burn-in. This is a previz,
   not a cut. I review pacing and source the stills.

7. PANTRY FILL → REVIEW CUT. After I drop stills into pantry/, re-run (only changed
   slots recompile). Set shot.focus per still; B18 gets the terracotta underline
   annotation at previz.

8. VISUAL QC LAW. Frame-level QC pass (CLAUDE-CODE-VISUAL-QC-CHECK.md): sample ≥2fps
   + 15/50/85% of each beat, actually read the PNGs, audit the 9-point rubric, fix
   root causes in scene source, re-render until zero BLOCKER/MAJOR. Log _qc/REPORT.md.

9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH —
   going public is a manual Studio flip.

Manim scenes referenced (build from animated_graphics.py, white canvas, ink + one
terracotta #D97757): transform_burden_to_process, converge_voices_to_one,
converge_draft_inputs, compress_time_triage, accumulate_faq_patterns,
loop_patterns_to_product. Remotion: ChipGrid (x2), SourceFlow, code-block (Onda),
plus the illustration scenes named in the sheet (triage-three-lanes, sentiment-flag,
connect-support-inbox, configure-tone-escalation). Retint deck patterns to the
claude stage (cream #F2F0E9, ink #3D3929, accent #D97757) and log the retint.

Honor every parent law: COLD OPEN, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE, ASK→RESULT,
REBUILD, DOUBLE-CHECK, FILL-THE-CANVAS, LOGO, HANDOFF (prompt read + discussed), OUTRO,
VISUAL QC, IN-FOR-BEAR, GATE P. Cold open opens "Jambo — this is Liam, in for Bear.";
the reel signs off "Liam, in for Bear." (tail of H01). Never hardcode plugin counts,
prices, platform lists, or named support vendors (Zendesk/Intercom/etc. stay generic).
```

---

## Notes for the builder
- **Render happens on your toolkit machine**, not in the authoring sandbox — this
  folder is the complete authoring package (`beat_sheet.json` + plan + sources + this
  prompt); the `art`/Remotion/Manim/Kokoro runtime consumes it.
- Shortest chapter in the book: the reel is meant to be short (~4:00). Duration is an
  OUTPUT — if the measured audio lands at 3:50, ship 3:50; do not add beats.
- Whole-batch build: see `youtube/BUILD-ALL.md` at the project root to render all
  reels in chapter order with one paste.
