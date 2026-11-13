# BUILD-PROMPT — agent-memory

The single paste-ready prompt that builds this reel end to end. Never publishes.

---

Build the reel at `examples/agent-memory/` end to end.

Read `skills/make/ai-explainer/SKILL.md` first, then this reel's
`beat_sheet.json`, `CHECKS-REPORT.md`, `FACTCHECK.md` and `SOURCES.md`.

Register is **Plain** (`runtime/prose/plain/PROSE.md`) — explain and stop, never
judge the design. Channel is `@HumanitariansAI` with the fixed `Irreducibly Human`
kicker and the persona **Prashanth** (not Liam); IN-FOR-BEAR LAW is not armed.

**REUSE ONLY — do not build new components.** Every scene is already registered.

Then:

1. **Gate check** — `./art doctor`. Every required feature must read ready.
2. **Audio** — `python3 runtime/scripts/generate_audio_kokoro.py examples/agent-memory`.
   Kokoro `am_onyx`, free. Audio is the clock.
3. **Wire durations** — copy each beat's measured `actual_duration_s` into its
   `shot.remotion.props.durationInSeconds` so `calculateMetadata` re-times each
   animation to its beat instead of truncating. **Every** beat, including the two
   `ClaudeCodeBeat` beats.
4. **Render + compile**:
   ```bash
   ART_NO_DRAWTEXT=1 PYTHONUTF8=1 ART_SCALE=1 \
     python3 runtime/scripts/remotion_scenes.py examples/agent-memory
   ART_NO_DRAWTEXT=1 PYTHONUTF8=1 \
     python3 runtime/scripts/compile.py examples/agent-memory --review --height 1080
   ```
   `metadata.review_labels: false` suppresses the footer. **Do not drop
   `--review`**: that takes the master path, where `final_frame_check.py` runs as a
   hard gate, exits 2 on the underfill MAJORs these shared components always
   produce, and writes no file.
5. **Verify by LOOKING** (CLAUDE.md rule 4) — sample frames and Read the PNGs.
   Four things a gate cannot catch:
   - B01's **final** frame shows the whole corrected sentence, not a truncated one.
   - B00 / B06 / BHTF composer chips read `@HumanitariansAI`.
   - BVDT shows four numbered lines with no orphan number.
   - No beat-marker footer anywhere.
6. **Report** — beat count, measured durations, total runtime, QC verdict.

**Stop at the review cut.** Do not run `./art final`, do not export a master, do
not publish.
