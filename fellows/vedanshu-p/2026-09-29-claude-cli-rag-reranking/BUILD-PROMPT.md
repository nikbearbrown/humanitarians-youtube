# BUILD-PROMPT — Reorder Is Not Retrieve.

Paste-ready Claude Code prompt that rebuilds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root —
the reel lives in the book, not the toolkit (CLAUDE.md rule 3).

```
Reel: D:\ai1-cli-main\youtube\2026-09-29-claude-cli-rag-reranking

0. Windows note — set UTF-8 for EVERY python step below:
   export PYTHONUTF8=1
   And run `./art scene-index`, NOT build_scene_index.py directly — the script
   resolves Root.tsx relative to CWD and fails from the toolkit root.

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.
   CHECKS-REPORT.md must show 0 PUNT-flagged before any render (PROOF GATE).

2. THE DEMO IS REAL — re-run it if the code changed:
   cd <REEL>/code
   python encoder.py  > ../_run-encoder.txt     # validate embeddings FIRST
   python rerank.py   > ../_run-rerank.txt
   python rewrite.py  > ../_run-rewrite.txt

   encoder.py must print roughly:
     identical   1.000
     paraphrase  0.555
     unrelated   0.100
   If those collapse toward each other the numpy BERT forward pass is broken and
   every rank downstream is meaningless — fix that before anything else.

   rerank.py must print `max elementwise difference: 0.00e+00`. That is the
   structural proof the whole reel rests on: a bi-encoder's document vector
   cannot depend on the query. A non-zero value means `encode` is leaking batch
   state and B01/B03's claim is false.

   Requirements: numpy + tokenizers, and the all-MiniLM-L6-v2 snapshot in the
   local HuggingFace cache. NOT sentence-transformers or transformers — absent
   here, which is why encoder.py parses safetensors by hand. No network access.

   *** TIMINGS VARY BETWEEN RUNS. *** The on-screen figures (2448 ms, 86 ms per
   pair, 23.8 hours) come from the captured transcripts. If you re-run, either
   keep the shipped numbers or update B04's props to the new ones — do not let
   narration and screen disagree.

3. Audio (only if narration changed — it is the master clock):
   python runtime/scripts/generate_audio_kokoro.py <REEL>

3b. *** RE-SYNC `beatSeconds` AFTER ANY AUDIO CHANGE ***
   B04, B05 and B08 stage every reveal as a fraction of their measured duration.
   remotion_scenes.py renders at the REGISTERED length (900f/30s) then truncates
   with `ffmpeg -t`, so keying to durationInFrames loses late reveals silently.

     python - <<'PY'
     import json
     p = r'<REEL>\beat_sheet.json'
     NEW = {'TwoStageCascade','ShortlistReorder','RetrievalMatrix'}
     d = json.load(open(p, encoding='utf-8'))
     for b in d['beats']:
         rem = b['shot']['remotion']
         if rem['pattern'] in NEW:
             rem['props']['beatSeconds'] = b['actual_duration_s']
     json.dump(d, open(p,'w',encoding='utf-8'), indent=1, ensure_ascii=False)
     PY

   Do this while NO render is running — remotion_scenes.py rewrites the sheet on
   completion and will clobber a mid-flight edit. Read it back afterwards.

4. Visuals:
   python runtime/scripts/remotion_scenes.py <REEL>
   --force to re-render after a component edit; --only <BEAT_ID> for one.
   *** --only takes ONE id. `--only B03 B04` is an argparse error — loop. ***

   Bespoke components (runtime/remotion/src/scenes/, registered at BOTH aspects):
     TwoStageCascade   (B04) — corpus block, shortlist, measured cost per stage
     ShortlistReorder  (B05) — two ranked columns + crossing connectors
   Reused after inspection: RetrievalMatrix (B08), from the Ch. 6 reel.
   All three sit on EmbedChrome's FigureFrame and ChunkChrome's useBeatClock.
   After ANY new component: ./art scene-index

   B11 must stay TitleOutroChannel. Do NOT swap to ClaudeTitleOutro: it is
   locked to claude-liam-* slugs (OUTRO-LOCK.md §Scope), hardcodes
   @NikBearBrown, and renders no subline — silently dropping the signature.

5. Assemble at 4K:
   python runtime/scripts/compile.py <REEL> --height 2160
   Explicit --height 2160 — compile.py's bare default is NOT 4K.

6. Visual QC — MANDATORY. ffprobe is a FILE check, never QC:
   ffmpeg -i <REEL>/claude-cli-rag-reranking.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read the PNGs, audit the 9-point rubric. Watch especially:
     B03, B07 — code beats: ~18 lines fit. B03 previously clipped mid-proof
     B04 — no arrow may point off-panel; stage 2 annotates the shortlist
     B08 — COUNT THE ROWS. Six are expected (see the trap below)
     B05 — the connectors must visibly cross, and the absent answer must land
   Log defects in _qc/REPORT.md. Fix ROOT CAUSES in scene source, re-render.

7. Confirm resolution:
   ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
     -of csv=p=0 <REEL>/claude-cli-rag-reranking.mp4   → 3840,2160

8. Never publish.
```

## The trap this build hit — a reuse that passed props and failed capacity

`RetrievalMatrix` was a legitimate GATE L hit: its contract (rows × columns of
HIT/MISS cells, one accent, a derived all-hits column) matched this beat exactly,
and opening the file confirmed it. It still broke, because it carried an
**implicit capacity assumption** that a props inspection cannot reveal:

```tsx
const rowAt = [prog(0.24, 0.09), prog(0.44, 0.09), prog(0.64, 0.09)];
const on = rowAt[ri] ?? 0;     // row 4+ -> opacity 0, forever
```

Three hardcoded reveal timings, one per row, for the three-row reel it was built
for. Chapter 9 passes six. Rows 4–6 rendered at opacity 0 — invisible but still
occupying full height, which also pushed the table up over the headline. One
root cause, two symptoms, and the visible one (overflow) was not the real one.

Both fixes are scoped so Chapter 6 renders unchanged: the reveal step is
preserved exactly at ≤3 rows, and the natural `rowH` became a ceiling rather
than a fixed value.

**Rule for the next reuse: check capacity as well as props.** Ask how many rows,
columns or items the component was built for, not just what shape its props are.

## What's already done (as of this build)

- `code/` — four real scripts, executed; transcripts in `_run-encoder.txt`,
  `_run-rerank.txt`, `_run-rewrite.txt`.
- `beat_sheet.json` — 12 beats on the full CLI spine, one revision cycle, audio
  generated (Kokoro `am_onyx`, $0.00), `beatSeconds` synced.
- `PEDAGOGY.md` (VERDICT: PASS) / `SOURCES.md` / `CHECKS-REPORT.md`
  (12 SHOW / 0 HOLD / 0 PUNT) / `_qc/REPORT.md`.
- Two new components registered at both aspects; `RetrievalMatrix` generalised.
- Master: 3840×2160, 24fps, 197.18s (3:17), 11.4 MB.

## If re-running after a content edit

- **Do not swap the stand-in in silently.** Stage 2 is late interaction
  (MaxSim), NOT the cross-encoder Chapter 9 describes — no such checkpoint is
  available on this machine. If you ever do run a real cross-encoder, the
  measured null in B05 may well change, and B04's caption, B09's narration and
  the whole SOURCES.md declaration must change with it.
- **Do not present Nogueira & Cho's 27% as this reel's number.** It is their
  measurement of a BERT cross-encoder on MS MARCO. It is deliberately absent
  from every frame.
- **The rewrites are hand-written and must stay declared as such.** HyDE and
  Rewrite-Retrieve-Read both need an LLM this machine does not have.
- **Changing the corpus changes the finding.** The eight confusable neighbours
  (HC-500, EL-120, QL-330, WS-260, PR-180, CB-140, DP-390, ST-210) exist so the
  first pass has somewhere to go wrong. Remove them and OE-300 stops falling out
  of the shortlist, which is the observation the whole second cycle rests on.
- **Do not "fix" the null result.** Re-ranking moving nothing IS the finding.
- **4K is a hard requirement**: step 5 passes `--height 2160`, step 7 confirms.

## Deriving the 9:16 Short

Both new components register `916` twins and re-band rather than crop. Per
cli-explainer's REVISION LAW the 9:16 cut ships a SINGLE cycle — so drop the
revision (B06–B08) and rewrite B09, which currently reports the comparison
between both cycles:

```
python runtime/scripts/shorts.py <REEL> --drop B06 B07 B08 --keep B10 \
       --handle "@VedanshuDaxeshPatel" \
       --next "Full video: the fix a re-ranker cannot make."
python runtime/scripts/compile.py <REEL>/short --height 3840
```

**If you drop B06–B08, rewrite B09.** Its subline says "on this corpus only the
second one mattered" and names the hand-written rewrites — both refer to the
rewriting cycle the short would have cut. A short that keeps that line asserts a
comparison it never showed.

Four Windows notes: pre-copy `mp3/beat-*.mp3` into `short/mp3/` (`shorts.py`
symlinks them, needing privileges Windows withholds — `OSError 1314`);
regenerate the endcard at 2160×3840 with a font from `runtime/fonts/` (its
`find_serif()` probes only macOS/Linux paths and falls back to an ~11px bitmap);
hand-write the rewritten outro narration; and check B05's portrait twin, since
two ranked columns plus connectors is the tightest horizontal layout here.

### As built (the short exists — `short/claude-cli-rag-reranking-short.mp4`)

2160×3840, 24fps, 160.24s (2:40), 10 beats, `am_onyx`, $0.00. Full record in
`short/_qc/REPORT.md`. Four things a rebuild must repeat:

1. **Rewrite B09 — the warning above fired exactly as written.** Its headline
   was "Two refinements, one stage, not interchangeable" and its subline
   compared the two cycles and named hand-written rewrites. All of that refers
   to B06–B08. The shipped version is "Stage one sets the ceiling." and claims
   only what the short shows. **Keep the cross-encoder stand-in caveat** (B04
   still shows the cascade); **drop the hand-written-rewrites caveat** (the
   rewrites no longer appear).
2. **Hand-write the outro.** The auto-rewrite produced the documented garbage
   ("also covers reorder is not retrieve., The change is almost nothing…").
3. **B04 portrait needs its own budget, and took three passes.** Landscape puts
   stage 1 in a horizontal gutter costing no height; portrait stacks and must
   pay for it. Solve the bar pitch across `corpusRows + shortlistRows` when the
   blocks stack — sizing each block independently crushes the bars to 2px. Then
   the stage strips still overran their slots and the opaque Panel below painted
   over stage 1's `index built once: 2448 ms`, so portrait drops the strip's
   explanatory `note` line and shrinks the arrow and gaps.
4. **Compile clean and portrait-4K:** `compile.py <REEL>/short --height 3840`.
   Not `--review --height 1920` as `shorts.py`'s own "next steps" suggests.
