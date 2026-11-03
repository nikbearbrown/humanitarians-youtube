# BUILD-PROMPT — madison-archetype-progress

The single paste-ready prompt that builds this reel end to end. Never publishes.

---

Build the reel at `examples/madison-archetype-progress/` end to end.

Read `skills/make/ai-explainer/SKILL.md` first, then this reel's
`beat_sheet.json`, `CHECKS-REPORT.md`, `FACTCHECK.md`, and `SOURCES.md`.

Register is **Plain** (`runtime/prose/plain/PROSE.md`) — explain and stop, never
judge the design. Channel is Liam on `@HumanitariansAI` with the fixed
`Irreducibly Human` kicker; IN-FOR-BEAR LAW is not armed, so Liam does not sign
"in for Bear".

**This is a planning-stage progress update. Honesty is the hard constraint:**
no beat may show tool output, because no tool exists. B07 and B08 are captioned
as illustrative/design-target respectively, and B10 states status including
"build not started" and "no results yet". Do not soften those.

**REUSE ONLY — do not build new components.** Every scene is already registered.

Then:

1. **Gate check** — `./art doctor`. Every required feature must read ready.
2. **Audio** — `python3 runtime/scripts/generate_audio_kokoro.py examples/madison-archetype-progress`.
   Kokoro `am_onyx`, free. Audio is the clock.
3. **Wire durations** — copy each beat's measured `actual_duration_s` into its
   `shot.remotion.props.durationInSeconds` so `calculateMetadata` re-times the
   animation to the beat instead of truncating it. Skip `ClaudeCodeBeat` (B08):
   at 300f/10s it completes inside its beat and freeze-holds.
   Verify B01's measured audio is ≥ 8s so the hesitant-writer correction lands
   before the cut.
4. **Render + compile the review cut** — `./art run examples/madison-archetype-progress`.
   No captions.
5. **Visual QC** — the frame-level pass from `CLAUDE-CODE-VISUAL-QC-CHECK.md`:
   sample at ≥2 fps plus each beat at ~15/50/85% of its span, **Read the PNGs**,
   audit the 9-point rubric, log to `_qc/REPORT.md`. Fix root causes in scene
   source and re-render. The mp4 probe is a file check and never counts as QC.
6. **Report** — beat count, measured durations, total runtime, QC verdict.

**Stop at the review cut.** Do not run `./art final`, do not export a master, do
not publish.

## Environment

```bash
ART_NO_DRAWTEXT=1 PYTHONUTF8=1 ART_SCALE=1 ./art run examples/madison-archetype-progress
```

- `PYTHONUTF8=1` — runtime scripts print `→`, `—`, `·`; cp1252 stdout raises
  `UnicodeEncodeError` without it.
- `ART_NO_DRAWTEXT=1` — `compile.py` interpolates the font path into the ffmpeg
  filtergraph unescaped, which a Windows drive-letter path breaks. Falls back to
  PIL label overlays; costs only the burned-in review timecode.
- `ART_SCALE=1` — fast pacing cut. **Text is not supersampled.** Drop this flag
  for a real master.

None of the three are needed on macOS or Linux except `ART_SCALE`.
