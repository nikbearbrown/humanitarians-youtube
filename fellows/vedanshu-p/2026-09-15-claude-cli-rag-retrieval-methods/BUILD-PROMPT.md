# BUILD-PROMPT — Watch The Right Answer Get Outvoted.

Paste-ready Claude Code prompt that rebuilds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root —
the reel lives in the book, not the toolkit (CLAUDE.md rule 3).

```
Reel: D:\ai1-cli-main\youtube\2026-09-08-claude-cli-rag-retrieval-methods

0. Windows note — set UTF-8 for EVERY python step below:
   export PYTHONUTF8=1
   Without it, build_scene_index.py fails reading Root.tsx and compile.py's
   status-line arrow crashes a cp1252 console. Environmental, not a reel defect.

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.

2. THE DEMO IS REAL — re-run it if the code changed:
   cd <REEL>/code
   python encoder.py                        # validate the embeddings FIRST
   python bm25_search.py   > ../_run-bm25.txt
   python hybrid_search.py > ../_run-hybrid.txt

   encoder.py must print roughly:
     identical   1.000
     paraphrase  0.555
     unrelated   0.100
   If those collapse toward each other, the BERT forward pass is broken and
   every dense number downstream is meaningless — stop and fix that first.

   Requirements: numpy + tokenizers, and the all-MiniLM-L6-v2 snapshot in the
   local HuggingFace cache. NOT sentence-transformers or transformers — they
   are absent here, which is why encoder.py parses safetensors by hand and runs
   the 6 layers itself. No network access is used.

3. Audio (only if narration changed — it is the master clock):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   Add --only <BEAT_ID> for a single beat. NEVER hand-edit actual_duration_s.

3b. *** IF AUDIO CHANGED ON B01, B07 OR B08, RE-SYNC `beatSeconds` ***
   Those three beats pass their measured duration to their component, which
   stages every reveal as a fraction of it. remotion_scenes.py renders each
   composition at its REGISTERED length (900f/30s) then truncates with
   `ffmpeg -t`, so keying to durationInFrames would push late reveals past the
   cut, where they are silently lost.

     python - <<'PY'
     import json
     p = r'<REEL>\beat_sheet.json'
     d = json.load(open(p, encoding='utf-8'))
     for b in d['beats']:
         rem = b['shot']['remotion']
         if rem['pattern'] in {'RetrievalTwoQueries','RetrievalMatrix','RrfMargin'}:
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
   the first render of a batch (this reel: B00, Chrome connect timeout at 25s;
   the Ch.5 short: B00, createSilentAudio). Both succeeded on a plain retry.

   Bespoke components (in runtime/remotion/src/scenes/, registered in Root.tsx
   at BOTH 16:9 and 916):
     RetrievalTwoQueries (B01) · RetrievalMatrix (B07) · RrfMargin (B08)
   All three sit on EmbedChrome's FigureFrame and ChunkChrome's useBeatClock.
   Do not fork that chrome.

   Reused unmodified: ClaudeComposerAsk (B00/B02/B05/B10), ClaudeCodeBeat
   (B03/B06), CliRunOutput (B04), RagExecutiveSummary (B09),
   TitleOutroChannel (B11).

   B11 must stay TitleOutroChannel. Do NOT swap to ClaudeTitleOutro: it is
   locked to claude-liam-* slugs (OUTRO-LOCK.md §Scope), hardcodes
   @NikBearBrown, and never renders a subline — silently dropping the signature.

   After ANY new component: ./art scene-index

5. Assemble at 4K:
   python runtime/scripts/compile.py <REEL> --height 2160
   Explicit --height 2160 — compile.py's bare default is NOT 4K.

6. Visual QC — MANDATORY. ffprobe is a FILE check, never QC:
   ffmpeg -i <REEL>/claude-cli-rag-retrieval-methods.mp4 -vf fps=2 \
          <REEL>/_qc/frames/%05d.png
   Read the PNGs, audit the 9-point rubric. Watch especially:
     B03 — the regex must render literally as r"[a-z0-9][a-z0-9\-]*"
           (JSON escaping makes this easy to break silently)
     B04 — transcript column alignment and the 6-line fit
     B07 — the derived "both" column must agree with its own row
     B08 — both reciprocal sums legible; the margin line present
   Log defects in _qc/REPORT.md. Fix ROOT CAUSES in component source, re-render.

7. Confirm resolution:
   ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
     -of csv=p=0 <REEL>/claude-cli-rag-retrieval-methods.mp4  → 3840,2160

8. Never publish.
```

## What's already done (as of this build)

- `code/` — four real scripts, executed; transcripts in `_run-bm25.txt` and
  `_run-hybrid.txt`; encoder validated.
- `beat_sheet.json` — 12 beats on the full CLI spine, one revision cycle, audio
  generated (Kokoro `am_onyx`, $0.00).
- `PEDAGOGY.md` (VERDICT: PASS) / `SOURCES.md` / `CHECKS-REPORT.md` /
  `_qc/REPORT.md`.
- Three new components registered at both aspects, typechecked, indexed.
- Master: **3840×2160, 228.0s, 12/12 filled, zero slates.** QC: zero BLOCKER,
  zero MAJOR, no component fixes required.

## If re-running after a content edit

- **Changing the code or the corpus changes the finding.** This reel's whole
  point is that the measured result was NOT the expected one (hybrid lost the
  paraphrase by 0.00025; dense did not fail the exact-code query). If you edit
  `corpus.py` or either retriever, re-run step 2 and **re-read the result before
  touching narration** — B07's matrix, B08's arithmetic and B09's caveats all
  describe a specific outcome. Do not leave narration describing a run that no
  longer happens.
- **Do not tune the corpus to restore the tidy story.** Adding code-shaped
  decoys until dense stumbles would be engineering the data to fit a claim.
  SOURCES.md §Corrections records that this was considered and rejected.
- **4K is a hard requirement** per the original build request: step 5 must pass
  `--height 2160` and step 7 must confirm `3840,2160`.

## Deriving the 9:16 Short

All three new components register `916` twins and re-band rather than crop.
Per cli-explainer's REVISION LAW the 9:16 cut ships a SINGLE cycle — so drop the
revision (B05–B08) and rewrite B09, which currently describes results the short
would not show:

```
python runtime/scripts/shorts.py <REEL> --drop B05 B06 B07 B08 --keep B10 \
       --handle "@VedanshuDaxeshPatel" \
       --next "Full video: the hybrid, and how it lost."
python runtime/scripts/compile.py <REEL>/short --height 3840
```

Three Windows notes if you do: pre-copy `mp3/beat-*.mp3` into `short/mp3/`
(`shorts.py` symlinks them and that needs privileges Windows withholds —
`OSError 1314`); regenerate the endcard at 2160×3840 with a font from
`runtime/fonts/` (its `find_serif()` probes only macOS/Linux paths and silently
falls back to an ~11px bitmap); and hand-write the rewritten outro narration,
because the auto-rewrite builds its topic list by truncating dropped beats'
`narration_text` and produces unusable output.
