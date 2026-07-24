# BUILD-PROMPT — Claude, By the Numbers (`claude-liam-data`)

Paste this into Claude Code from your `books/` root (where `brutalist-art/` lives).
Typically under `claude --dangerously-skip-permissions` — the pipeline is git-tracked,
regenerable, and GATE P still requires your signature before any audio spend.

---

```
Build the deep-explainer reel at books/anthropics/books/claude-cowork-plugins/youtube/claude-liam-data/.

The plan is authored: read beat_sheet.json, PLAN.md, SOURCES.md, and the book-level
FACTCHECK.md (books/anthropics/books/claude-cowork-plugins/FACTCHECK.md). Then:

1. SCHEMA RECONCILE. Load runtime/schema/beat_sheet.schema.json and conform this
   beat_sheet.json to it exactly — field names, scene keys, shot/vox_run/handoff
   shape. This sheet was authored to the deep-explainer doctrine but may use loose
   field names; fix them to the schema without changing content, lanes, narration,
   or the act order. Keep the spine: ClaudeComposerAsk cold open (ask answered,
   greeting "Olá, Kore", Kore signs in) → body → ClaudeVerdictArtifact (0.5s lead) →
   ClaudeComposerAsk "Your turn." (Kore signs off "Kore, in for Humanitarians AI.") → ClaudeTitleOutro.

2. LANE-MIX LINT. Run the beat-mix histogram. Expect VOX 6 (20.7%), MANIM 8 (27.6%),
   REMOTION 9 (31.0%), CARD 6 (20.7%) over 29 body beats — all in band. Confirm the
   longest same-lane run is 2 (B04–B05, B08–B09 REMOTION; B15–B16 the VOX run) and
   that vox_run R1 (B15→B16) does not cross an act boundary.

3. GATE P. Present the full narration (B00 → O01) on an animated slate for my
   sign-off. Do NOT generate audio until I approve. Channel is claude-liam:
   Kokoro af_kore, free. No ElevenLabs.

4. AUDIO LOCK. python3 runtime/scripts/generate_audio.py <reel> (Kokoro/af_kore).
   Per-beat mp3 durations become the clock; align writes the word clock. Captions
   via the faster-whisper pipeline. Reveals in Manim/vox beats land ON the spoken word.

5. SHOPPING LIST (Gate D2, AFTER audio lock). For every VOX beat (B03, B11, B15, B16,
   B20, B23), first run python3 runtime/scripts/pantry_search.py on its pantry_note
   terms against svg/svg/images/. Copy real matches into pantry/ pre-checked; write
   SHOPPING.md from the LOCKED durations for the rest. All six are Tier 1 illustrative
   (no rights escalation, no real people). B15+B16 are one vox run — source them as a
   matched pair (same operator, same room; B16 pulls wider to include the calendar) and
   honor the handoff camera/object coords. B23 is drawon — plate is blank; the terracotta
   ring is added at previz.

6. GATE D1 PREVIZ. ./brutalist-art/art run <reel> — full compile, slates in the
   vox slots, Manim/Remotion rendered for real, --review burn-in. This is a previz,
   not a cut. I review pacing and source the stills.

7. PANTRY FILL → REVIEW CUT. After I drop stills into pantry/, re-run (only changed
   slots recompile). Set shot.focus per still; verify vox_run R1 continuity across B15→B16.

8. VISUAL QC LAW. Frame-level QC pass (CLAUDE-CODE-VISUAL-QC-CHECK.md): sample ≥2fps
   + 15/50/85% of each beat, actually read the PNGs, audit the 9-point rubric, fix
   root causes in scene source, re-render until zero BLOCKER/MAJOR. Log _qc/REPORT.md.

9. ./brutalist-art/art final <reel>. Master stays in the folder. DO NOT PUBLISH —
   going public is a manual Studio flip.

Manim scenes referenced (build from animated_graphics.py, white canvas, ink + one
terracotta #D97757): loop_export_stare_close, nlq_question_to_sentence,
clean_messy_to_tidy, compare_quarter_over_quarter, accumulate_monthly_reviews,
threshold_concentration_risk, verify_before_rely, accumulate_four_habits.
Remotion: SourceFlow (B04, B09), ChipGrid (B08), PredictCard (B21), code-block
(Onda — B05, B14, B18), plus illustration scenes (finances-folder-untouched B01,
column-becomes-chart B12). Retint deck patterns to the claude stage (cream #F2F0E9,
ink #3D3929, accent #D97757) and log the retint. Onda code-blocks render the ACTUAL
plain-language queries from the sheet — a data chapter's interaction surface is the query.

DATABLE STRIP — hard: never name a database vendor (no Postgres/BigQuery/Snowflake),
never name a payment/analytics tool as a beat's subject, never put a plugin count,
price, or platform list on screen. Percentages (60%/40%) appear ONLY as the framed
illustrative example answers already written into B07 and B19 — never as world-facts.

Honor every parent law: COLD OPEN, ILLUSTRATE, SHOW-DON'T-TELL, SPARK-LINE, ASK→RESULT,
REBUILD, DOUBLE-CHECK, FILL-THE-CANVAS, LOGO, HANDOFF (prompt read + discussed), OUTRO,
VISUAL QC, IN-FOR-BEAR, GATE P.
```

---

## Notes for the builder
- **Render happens on your toolkit machine**, not in the authoring sandbox — this
  folder is the complete authoring package (`beat_sheet.json` + plan + sources + this
  prompt); the `art`/Remotion/Manim/Kokoro runtime consumes it. Nothing here renders in
  place; the toolkit machine is where audio, Manim, Remotion, and the `art` conform run.
- Whole-batch build: see `youtube/BUILD-ALL.md` at the project root to render all
  chapter reels in order with one paste.
