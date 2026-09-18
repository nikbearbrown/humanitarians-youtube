# BUILD-PROMPT — Watch Exact Search Hit A Wall.

Paste-ready Claude Code prompt that rebuilds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root —
the reel lives in the book, not the toolkit (CLAUDE.md rule 3).

```
Reel: D:\ai1-cli-main\youtube\2026-09-08-claude-cli-rag-vector-databases

0. Windows note — set UTF-8 for EVERY python step below:
   export PYTHONUTF8=1
   Without it, build_scene_index.py fails reading Root.tsx and compile.py's
   status-line arrow crashes a cp1252 console. Environmental, not a reel defect.

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.

2. THE DEMO IS REAL — re-run it if the code changed:
   cd <REEL>/code
   python brute_force_search.py > ../_run-brute.txt
   python ann_search.py        > ../_run-ann.txt

   Every number in B04, B07 and B08 is this stdout. If you edit anything in
   code/, you MUST re-run and re-copy the numbers into the beat sheet — a
   CODE beat that no longer produces its OUTPUT beat is an ACTUAL-CODE LAW
   violation, and it is invisible in the render.

   Requires numpy only (scipy unused; sklearn/matplotlib are broken against
   numpy 2.x on this machine and are not needed). Seed is fixed in corpus.py,
   so comparison counts and recall reproduce exactly. Wall-clock ms will differ
   per machine — that is expected, and is why B07 plots COMPARISONS, not ms.

3. Audio (only if narration changed — it is the master clock):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   Add --only <BEAT_ID> for a single beat. NEVER hand-edit actual_duration_s.

3b. *** IF AUDIO CHANGED ON B07 OR B08, RE-SYNC `beatSeconds` ***
   Those two beats pass their measured duration to their component, which
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
         if rem['pattern'] in {'AnnScalingChart', 'AnnRecallDial'}:
             rem['props']['beatSeconds'] = b['actual_duration_s']
     json.dump(d, open(p,'w',encoding='utf-8'), indent=1, ensure_ascii=False)
     PY

   Do this while NO render is running: remotion_scenes.py rewrites the beat
   sheet when it finishes and will clobber a mid-flight edit. Read the file
   back afterwards to confirm the value stuck.

4. Visuals — render every beat carrying shot.remotion.pattern:
   python runtime/scripts/remotion_scenes.py <REEL>
   Add --force to re-render after a component edit; --only <BEAT_ID> for one.

   Bespoke components for this reel (in runtime/remotion/src/scenes/,
   registered in Root.tsx at BOTH 16:9 and 916):
     AnnScalingChart  (B07)   — two series over collection size
     AnnRecallDial    (B08)   — recall vs share of collection compared
   Both sit on EmbedChrome's FigureFrame and use ChunkChrome's useBeatClock
   (both built for the Ch. 3/Ch. 4 reels). Do not fork that chrome.

   Reused unmodified: ClaudeComposerAsk (B00/B02/B05/B10), RagExecutiveSummary
   (B01/B09), ClaudeCodeBeat (B03/B06), CliRunOutput (B04),
   TitleOutroChannel (B11).

   B11 must stay TitleOutroChannel. Do NOT swap to ClaudeTitleOutro: it is
   locked to claude-liam-* slugs (OUTRO-LOCK.md §Scope), hardcodes
   @NikBearBrown, and never renders a subline — which silently drops the
   author signature.

   After ANY new component: ./art scene-index

5. Assemble at 4K:
   python runtime/scripts/compile.py <REEL> --height 2160
   Explicit --height 2160 — compile.py's bare default is NOT 4K.

6. Visual QC — MANDATORY. An ffprobe duration check is a FILE check, never QC:
   ffmpeg -i <REEL>/claude-cli-rag-vector-databases.mp4 -vf fps=2 \
          <REEL>/_qc/frames/%05d.png
   Read the PNGs, audit the 9-point rubric. Watch especially:
     B03, B06 — code beats: the longest line must not overflow; check the
                legibility floor holds at 4K
     B04      — transcript: column alignment survives, verdict line visible
     B07      — both series drawn, end labels not colliding with the frame edge
     B08      — all four points labelled, labels not overlapping the curve
   Log defects and fixes in _qc/REPORT.md. Fix ROOT CAUSES in component source
   and re-render (--force) until zero BLOCKER and zero MAJOR.

7. Confirm resolution:
   ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
     -of csv=p=0 <REEL>/claude-cli-rag-vector-databases.mp4   → must read 3840,2160

8. Never publish.
```

## What's already done (as of this build)

- `code/` — three real scripts, executed; transcripts in `_run-brute.txt` and
  `_run-ann.txt`.
- `beat_sheet.json` — 12 beats on the full mandatory CLI spine, one revision
  cycle, audio generated (Kokoro `am_onyx`, $0.00).
- `PEDAGOGY.md` (VERDICT: PASS) / `SOURCES.md` / `CHECKS-REPORT.md` /
  `_qc/REPORT.md`.
- Two new components registered at both aspects, typechecked, indexed.

## If re-running after a content edit

- **Changing the code means changing the numbers.** Re-run step 2, copy the new
  stdout into B04's `lines`, B07's `series.values` and B08's `points`, then
  re-render those beats. The reel's honesty rests on those three staying in
  sync with `code/`.
- **4K is a hard requirement** per the original build request: step 5 must pass
  `--height 2160` and step 7 must confirm `3840,2160`.
- Do not add a chunk of HNSW imagery to this reel. The code builds an
  inverted-file index; the chapter's Fig. 02 shows a graph hierarchy. Mixing
  them implies the demo does something it does not — see SOURCES.md §2.

## Deriving the 9:16 Short

Both new components register `916` twins and re-band rather than crop:

```
python runtime/scripts/shorts.py <REEL> --handle "@VedanshuDaxeshPatel" \
       --next "Full video: the index, and what it costs."
python runtime/scripts/compile.py <REEL>/short --height 3840
```

Two Windows notes if you do: `shorts.py` symlinks the parent mp3s into
`short/mp3/` and that needs privileges Windows does not grant by default
(`OSError 1314`) — pre-copy them instead; and its endcard helper falls back to
an ~11px bitmap font because `find_serif()` probes only macOS/Linux paths, so
regenerate the endcard with a bundled font from `runtime/fonts/`.
