# BUILD-PROMPT — Watch A Bug Name Its Own Stage.

Paste-ready Claude Code prompt that rebuilds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root —
the reel lives in the book, not the toolkit (CLAUDE.md rule 3).

```
Reel: D:\ai1-cli-main\youtube\2026-09-22-claude-cli-rag-pipeline

0. Windows note — set UTF-8 for EVERY python step below:
   export PYTHONUTF8=1
   Without it, build_scene_index.py fails reading Root.tsx and compile.py's
   status-line arrow crashes a cp1252 console. Environmental, not a reel defect.

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.

2. THE DEMO IS REAL — re-run it if the code changed:
   cd <REEL>/code
   python encoder.py                    # validate the embeddings FIRST
   python pipeline.py  > ../_run-pipeline.txt
   python diagnose.py  > ../_run-diagnose.txt

   encoder.py must print roughly:
     identical   1.000
     paraphrase  0.555
     unrelated   0.100
   If those collapse toward each other the BERT forward pass is broken and every
   retrieval result downstream is meaningless — fix that before anything else.

   diagnose.py must end with `all three distinguishable: YES`. **If it prints NO,
   the reel's central claim no longer holds and B07's narration is wrong.** Do
   not re-render until you have either restored the distinct signatures or
   rewritten B07 and B09 to report the new result honestly.

   Requirements: numpy + tokenizers, and the all-MiniLM-L6-v2 snapshot in the
   local HuggingFace cache. NOT sentence-transformers or transformers — absent
   here, which is why encoder.py parses safetensors by hand. No network access.

3. Audio (only if narration changed — it is the master clock):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   Add --only <BEAT_ID> for a single beat. NEVER hand-edit actual_duration_s.

3b. *** IF AUDIO CHANGED ON B04 OR B07, RE-SYNC `beatSeconds` ***
   Those two beats pass their measured duration to their component, which stages
   every reveal as a fraction of it. remotion_scenes.py renders each composition
   at its REGISTERED length (900f/30s) then truncates with `ffmpeg -t`, so keying
   to durationInFrames would push late reveals past the cut, where they are
   silently lost.

     python - <<'PY'
     import json
     p = r'<REEL>\beat_sheet.json'
     d = json.load(open(p, encoding='utf-8'))
     for b in d['beats']:
         rem = b['shot']['remotion']
         if rem['pattern'] in {'PipelineTrace', 'FaultSignatureTable'}:
             rem['props']['beatSeconds'] = b['actual_duration_s']
     json.dump(d, open(p,'w',encoding='utf-8'), indent=1, ensure_ascii=False)
     PY

   Do this while NO render is running — remotion_scenes.py rewrites the beat
   sheet when it finishes and will clobber a mid-flight edit. Read the file back
   afterwards to confirm the value stuck.

4. Visuals:
   python runtime/scripts/remotion_scenes.py <REEL>
   Add --force to re-render after a component edit; --only <BEAT_ID> for one.

   *** IF EXACTLY ONE BEAT FAILS — ESPECIALLY THE FIRST — RETRY IT BEFORE
   DEBUGGING. *** Remotion's browser/audio startup intermittently times out on
   the first render of a batch (seen twice in this series: a Chrome connect
   timeout and a createSilentAudio failure). Both succeeded on a plain retry.

   Bespoke components (in runtime/remotion/src/scenes/, registered in Root.tsx
   at BOTH 16:9 and 916):
     PipelineTrace       (B04) — five stage boxes + handoffs + answer strip
     FaultSignatureTable (B07) — fault rows against signal columns + verdict
   Both sit on EmbedChrome's FigureFrame and ChunkChrome's useBeatClock.
   Do not fork that chrome.

   Reused unmodified: ClaudeComposerAsk (B00/B02/B05/B10), ClaudeCodeBeat
   (B03/B06), CliRunOutput (B08), RagExecutiveSummary (B01/B09),
   TitleOutroChannel (B11).

   B11 must stay TitleOutroChannel. Do NOT swap to ClaudeTitleOutro: it is
   locked to claude-liam-* slugs (OUTRO-LOCK.md §Scope), hardcodes
   @NikBearBrown, and never renders a subline — silently dropping the signature.

   After ANY new component: ./art scene-index

5. Assemble at 4K:
   python runtime/scripts/compile.py <REEL> --height 2160
   Explicit --height 2160 — compile.py's bare default is NOT 4K.

6. Visual QC — MANDATORY. ffprobe is a FILE check, never QC:
   ffmpeg -i <REEL>/claude-cli-rag-pipeline.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read the PNGs, audit the 9-point rubric. Watch especially:
     B04 — five boxes plus four handoff labels is the tightest horizontal
           layout in this series; check the flow labels don't collide with the
           boxes and that nothing crosses SAFE
     B07 — four columns must stay aligned across all four rows, or the
           signature comparison the beat exists for stops being scannable
     B03, B06 — code beats: check the longest line doesn't overflow
     B08 — transcript: the wrapped sick-leave line must stay readable
   Log defects in _qc/REPORT.md. Fix ROOT CAUSES in component source, re-render.

7. Confirm resolution:
   ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
     -of csv=p=0 <REEL>/claude-cli-rag-pipeline.mp4   → 3840,2160

8. Never publish.
```

## What's already done (as of this build)

- `code/` — four real scripts, executed; transcripts in `_run-pipeline.txt` and
  `_run-diagnose.txt`; encoder validated.
- `beat_sheet.json` — 12 beats on the full CLI spine, one revision cycle, audio
  generated (Kokoro `am_onyx`, $0.00).
- `PEDAGOGY.md` (VERDICT: PASS) / `SOURCES.md` / `CHECKS-REPORT.md` /
  `_qc/REPORT.md`.
- Two new components registered at both aspects, typechecked, indexed.

## If re-running after a content edit

- **The generator is not an LLM, and the reel depends on that.** If you swap in
  a real model, the clean one-to-one fault/symptom mapping will degrade — a
  model can answer correctly from prior knowledge despite a retrieval fault, or
  hallucinate despite a healthy pipeline. That is a legitimate follow-up
  experiment, but it invalidates B07's table and B09's caveat as written. Do not
  make that swap and leave the narration alone.
- **Changing the corpus changes the finding.** SL-140 and BO-001 are there so
  the broken retriever returns something plausible rather than obvious nonsense.
  Remove them and the retrieval fault stops being interesting.
- **4K is a hard requirement** per the original build request: step 5 must pass
  `--height 2160` and step 7 must confirm `3840,2160`.

## Deriving the 9:16 Short

Both new components register `916` twins and re-band rather than crop. Per
cli-explainer's REVISION LAW the 9:16 cut ships a SINGLE cycle — so drop the
revision (B05–B08) and rewrite B09, which currently reports fault results the
short would not show:

```
python runtime/scripts/shorts.py <REEL> --drop B05 B06 B07 B08 --keep B10 \
       --handle "@VedanshuDaxeshPatel" \
       --next "Full video: break one stage, name the bug."
python runtime/scripts/compile.py <REEL>/short --height 3840
```

Three Windows notes if you do: pre-copy `mp3/beat-*.mp3` into `short/mp3/`
(`shorts.py` symlinks them and that needs privileges Windows withholds —
`OSError 1314`); regenerate the endcard at 2160×3840 with a font from
`runtime/fonts/` (its `find_serif()` probes only macOS/Linux paths and silently
falls back to an ~11px bitmap); and hand-write the rewritten outro narration,
because the auto-rewrite truncates dropped beats' `narration_text` into
unusable output.

### As built (the short exists — `short/claude-cli-rag-pipeline-short.mp4`)

2160×3840, 24fps, 149.96s (2:30), 9 beats, `am_onyx`, $0.00. Full record in
`short/_qc/REPORT.md`. Four things a rebuild must repeat:

1. **Rewrite B09 — do not just re-render it.** Its parent narration reports the
   three fault signatures, which B05–B08 measure and the short cuts. Left alone
   the short asserts a result it never shows. The shipped version claims only
   the *structure*, and `sparkLine` moved from "Localise before you fix." to
   **"Name the seams first."** for the same reason. Keep the deterministic-reader
   caveat — B03 is in the cut and its docstring carries it on screen.
2. **B09's first pass ran 25.43s.** Trimmed to 17.75s by cutting the
   stage-by-stage recitation, which B04 has just drawn. Siblings: 18.41s / 18.62s.
3. **Compile clean and portrait-4K:** `compile.py <REEL>/short --height 3840`.
   Not `--review --height 1920` as `shorts.py`'s own "next steps" suggests —
   that yields a 1080-wide review cut with markers.
4. **Expect one stalled beat.** B10 hung with 31s of CPU after 3h13m. Stop the
   run, kill stale `node`/`chrome`, re-launch — it skips finished beats. Retry
   before debugging (step 4 above).
