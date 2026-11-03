# BUILD-PROMPT — madison-archetype-progress-week2

The single paste-ready prompt that builds this reel end to end. Never publishes.

---

Build the reel at `examples/madison-archetype-progress-week2/` end to end.

Read `skills/make/ai-explainer/SKILL.md` first, then this reel's `beat_sheet.json`,
`CHECKS-REPORT.md`, `FACTCHECK.md` and `SOURCES.md`.

Register is **Plain** (`runtime/prose/plain/PROSE.md`) — explain and stop, never
judge the design. Channel is `@HumanitariansAI`, kicker `Irreducibly Human`,
persona **Prashanth**. IN-FOR-BEAR LAW is not armed.

**This is a design-stage update. Honesty is the hard constraint:** nothing is built,
so no beat may show detector output. B06 is a labelled design target with `0.0`
placeholder scores, B07 is labelled illustrative, B10 states "nothing built / no
sample data / no results". Do not soften those. Keep collaborator and tool names
**generic** — no personal names, no internal tool names.

**REUSE ONLY — do not build new components.**

Then:

1. **Gate check** — `./art doctor`.
2. **Audio** — `python3 runtime/scripts/generate_audio_kokoro.py examples/madison-archetype-progress-week2`.
3. **Wire durations** — copy each measured `actual_duration_s` into
   `shot.remotion.props.durationInSeconds` on **every** beat.
4. **Render + compile** (compile WITHOUT `--review`, per the build request):
   ```bash
   ART_NO_DRAWTEXT=1 PYTHONUTF8=1 ART_SCALE=1 \
     python3 runtime/scripts/remotion_scenes.py examples/madison-archetype-progress-week2
   ART_NO_DRAWTEXT=1 PYTHONUTF8=1 \
     python3 runtime/scripts/compile.py examples/madison-archetype-progress-week2 --height 1080
   ```
   No `--review` means the **master path**: `final_frame_check.py` runs as a hard
   gate and the output lands in `<toolkit>/renders/`, not beside the reel. If the
   gate refuses, report the refusal and its flagged frames — do not silently switch
   to the review path.
5. **Verify by LOOKING** (CLAUDE.md rule 4) — sample frames and Read the PNGs:
   - B01's **final** frame shows the whole corrected sentence.
   - B00 / B05 / BHTF composer chips read `@HumanitariansAI`.
   - BVDT shows four numbered lines, no orphan number.
   - B06 and B07 carry their "not produced" / "illustrative" labels.
6. **Report** — beat count, measured durations, total runtime, QC verdict.

**Stop at the cut.** Do not publish.
