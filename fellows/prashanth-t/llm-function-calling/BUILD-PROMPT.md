# BUILD-PROMPT — llm-function-calling

The single paste-ready prompt that builds this reel end to end. Never publishes.

---

Build the reel at `examples/llm-function-calling/` end to end.

Read `skills/make/ai-explainer/SKILL.md` first, then this reel's
`beat_sheet.json`, `CHECKS-REPORT.md`, and `SOURCES.md`. Register is **Plain**
(`runtime/prose/plain/PROSE.md`), not Teardown — explain the mechanism and stop,
never judge the design. Channel is Liam on `@HumanitariansAI`; IN-FOR-BEAR LAW is
not armed, so Liam does not sign "in for Bear".

Then:

1. **Gate check** — `./art doctor`. Every required feature must read ready.
2. **Scene index** — `./art scene-index`, then confirm `FnCallLoop`,
   `FnCallPredictCard`, and `FnCallTitleOutro` all report RENDERABLE via
   `./art scenes --check <name>`.
3. **Audio** — `python3 runtime/scripts/generate_audio_kokoro.py examples/llm-function-calling`.
   Kokoro `am_onyx`, free. Audio is the clock; per-beat MP3 durations drive
   everything downstream. Verify B01's measured audio is ≥ 8s (it carries
   `lead_silence_s: 0.8` and the hesitant-writer correction must land on screen
   before the cut).
4. **Render + compile the review cut** — `./art run examples/llm-function-calling`.
   No captions (`metadata.captions: false`).
5. **Visual QC** — the frame-level pass from `CLAUDE-CODE-VISUAL-QC-CHECK.md`:
   sample at ≥2 fps plus each beat at ~15/50/85% of its span, **Read the PNGs**,
   audit the 9-point rubric, and log to `_qc/REPORT.md`. Fix root causes in scene
   source and re-render until zero BLOCKER and zero MAJOR remain. The mp4 probe
   is a file check and never counts as QC.
6. **Report** — beat count, measured durations, total runtime, QC verdict.

**Stop at the review cut.** Do not run `./art final`, do not export a master, do
not publish.

## Windows note

This machine needs two environment flags, both upstream bugs with issues drafted:

```bash
ART_NO_DRAWTEXT=1 PYTHONUTF8=1 ./art run examples/llm-function-calling
```

- `PYTHONUTF8=1` — several runtime scripts print `→`, `—`, `·` to stdout, which
  raises `UnicodeEncodeError` on a cp1252 console.
- `ART_NO_DRAWTEXT=1` — `compile.py` interpolates the font path into the ffmpeg
  filtergraph unescaped, which a Windows drive-letter path breaks. This falls back
  to PIL label overlays and costs only the burned-in review timecode.

Neither is needed on macOS or Linux.
