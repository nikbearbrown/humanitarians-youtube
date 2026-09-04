# BUILD-LOG — "Claude, Ingested." (Week 1)

Session date: 2026-08-31 · Toolkit: `brutalist.art` (cli-explainer skill) ·
Cost: $0.00 · Register: Teardown, claude-liam channel.

## What was built

12-beat `cli-explainer` reel over the real Week 1 build of
`finance-event-signals` (a separate portfolio project — see
`SOURCE-brief.md`). Claude-skin bookends (`ClaudeComposerAsk`,
`ClaudeTitleOutro`); GitHub-dark skin (`GitHubCodeViewer`,
`GitHubCodeDiff`, `GitHubCallChain`) for every code/diff/pipeline beat, per
the ILLUSTRATE-LAW-equivalent rule that the UI skin only earns a beat when
the UI itself is the subject.

## Toolkit bugs found and fixed while building this reel (and the other 7 in this batch)

1. `runtime/scripts/remotion_scenes.py` called `subprocess.run(["npx", …])`
   with no resolved path/shell — on Windows `npx` is a `.cmd` shim
   `CreateProcess` can't exec directly, so every Remotion beat silently
   fell back to a slate. Fixed: route through `cmd /c` on `os.name=="nt"`.
2. `runtime/qc/final_frame_check.py`'s burn-in exclusion mask covered only
   the bottom-left beat-id strip, not the top-right global timecode
   `compile.py --review` burns in — every frame in every reel's review cut
   false-flagged `edge-bleed` (BLOCKER), 100% of the time. Fixed with a
   second exclusion region.
3. `runtime/scripts/generate_audio_kokoro.py` read `beat_sheet.json` via
   `Path.read_text()` with no `encoding="utf-8"`, defaulting to Windows
   cp1252 — every em-dash in every narration line decoded as 3 mojibake
   characters that didn't match the script's own em-dash cleanup table, so
   Kokoro's phonemizer spelled them out literally ("circumflex euros"),
   audibly, in every beat. Fixed with explicit `encoding="utf-8"` on every
   read/write in that script. User-reported; caught by ear after the first
   render, not by any gate.

Full diagnosis for all three: see the CHECKS-REPORT.md files in
`C:\Users\sachi\finance-event-signals\youtube\claude-liam-week1-ingest\`.

## Known gaps in this submission

- **9:16 cut not built.** Spec requires both 16:9 and 9:16; only 16:9
  exists for this video (and all 7 others in this batch). Deferred —
  re-render not yet scheduled.
- **PROOF-REVIEW: pending.** The required `PROOF.md` self-assessment
  document has not been supplied yet; this video has not been run through
  it.
