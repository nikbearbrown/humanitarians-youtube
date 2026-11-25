# BUILD-LOG — Embedding Model Staleness: The Index That Quietly Split in Two

## 2026-11-19 — Research and verification demo

**Gate P:** Beat sheet approved 2026-11-19. **FACTCHECK:** resolved same day — the mechanism
(embedding-model geometry incompatibility, generically stated), the worked example (an invented,
illustrative corpus-split scenario), and the falsifiability case (the identical scenario with a
full re-embed instead) all confirmed fully qualitative where generic, with the ONE quantified claim
backed by a real, reproducible local demo. Confirmed distinct from nine prior videos in this
series, with particular care taken distinguishing from the earlier general embeddings video and
the context-window-limits video.

**mycroft source read (read-only reference, confirmed, nothing modified):** read
`/Users/pranavijs/mycroft/scripts/mycroft-main/Core_Components/Regulatory_QA/backend/app/rag.py`,
`app/config.py`, and `app/routers/chat.py` directly before building anything. Confirmed:
`HuggingFaceEmbeddings(model_name=settings.embedding_model)` with `settings.embedding_model`
defaulting to `"all-MiniLM-L6-v2"` (`config.py` line 18); `build_vectorstore()` calls
`Chroma.from_documents(..., persist_directory=None)` (lines 173-178); `routers/chat.py`'s `POST
/api/chat` handler calls `rag.build_vectorstore(feeds)` inline on every request (lines 30-31,
before `rag.query(...)`). This confirms the honest side-note: mycroft rebuilds its vector store
fresh on every single chat request, sidestepping the embedding-staleness bug class by construction
— at the real cost of re-embedding the full feed set every time. No bug exists there for this
failure mode; none is claimed.

**Real, reproducible local demo (`verification/`):** installed `sentence-transformers`,
`scikit-learn` (pulled in `torch`/`transformers`); hit and fixed a real `401`/`RepositoryNotFoundError`
from an expired cached HF token triggering an incidental network call even for already-cached
models — fixed with `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`. Used two real, different, published
sentence-transformer checkpoints already locally cached: `sentence-transformers/all-MiniLM-L6-v2`
(Model A, matching mycroft's own default) and `sentence-transformers/multi-qa-MiniLM-L6-cos-v1`
(Model B, a genuinely different checkpoint, same architecture family/dimensionality, different
training objective). Loaded via plain `transformers` `AutoTokenizer`/`AutoModel` with mean-pooling
and L2-normalization coded by hand (not the `sentence-transformers` wrapper), so the pooling math is
auditable in the script itself.

Real results from one run (`verification/demo_output.txt`): Part 1 — mean cross-model cosine
similarity of the IDENTICAL sentence embedded by both models: 0.7416 (range 0.6832-0.7801), far
from the ~1.0 a shared geometry would produce. Part 2 — aggregate same-model vs. cross-model
similarity distributions (same-model mean ~0.04-0.05 vs. cross-model mean ~0.10, cross-model std
0.225, much noisier). Part 3 — on a 10-sentence, 10-topic corpus, a partially-migrated index
measurably degraded a stale document's similarity score in every tested query, though top-1 ranking
happened to survive on this particular wide-topic-margin corpus (reported honestly, including the
non-flip). Part 4 — on a closer, more confusable real document pair found via a short, documented
search over several candidate pairs/phrasings, the identical mechanism produced a genuine top-1
RANK INVERSION: correct document wins 0.6090 vs. 0.5859 when both are embedded by the current
model; loses 0.5109 vs. 0.5859 (unchanged) once it alone is stuck in the old model's stale space.

## 2026-11-19 — Landscape build

**Audio:** Kokoro `af_bella`, all 9 spoken beats generated via `generate_audio_kokoro.py --only
B01...B09` in one background pass (ran longer than the foreground timeout; polled via `ps`/directory
listing, not re-run). B00 a real silent mp3 (`ffmpeg anullsrc`, requested 4.1s, measured via
`ffprobe` at 4.128s). `generate_audio_kokoro.py` again defaulted B00's `actual_duration_s` to its
`estimated_duration_s` fallback (4.0) despite skipping B00 as silence — this time caught immediately
via a raw `grep -c '"actual_duration_s"'` count (exactly 10, one per beat) before hand-editing, and
the hand-edit replaced the existing key in place (re-`Read` first) rather than inserting a
duplicate — avoiding the exact duplicate-JSON-key bug a sibling reel's build documented. Measured
durations: B00=4.128 B01=17.78 B02=24.67 B03=29.23 B04=32.47 B05=23.11 B06=32.02 B07=24.22 B08=13.1
B09=1.51 — total 202.238s.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper for every on-screen string,
`PALETTE`/`fit()`/`panel()`/`box_around()`/`stat_row()`/`metric_panel()` helpers copied verbatim
from the CWL reel. B03 shows all 3 tests (Check the Checkpoint / Audit the Whole Index / Watch for
Silence) fully, before any example. B04/B05 share the exact same corpus size (1,000 documents) and
the exact same switch event, isolating the one variable the rubric's test #2 names — whether a
full re-embed happened before serving. B06 quotes `rag.py`/`config.py` verbatim, double-checked
against the live source before finalizing.

### Real findings during this build

1. **A real GATE A static-distinctness failure on B06, not a false positive:** `B06_MycroftRealWorldNote`
   failed "shapes never change — 1 distinct shape-state across 13 frames" because its only non-text
   shape was one panel created once and never joined by another. Fixed by adding a real top rule
   and real `box_around()` highlight boxes around each quoted code line as revealed — confirmed via
   a scoped re-check before re-running the full pipeline.
2. **A real GATE B layout failure, a self-caused bug found on the first full re-run:** B06's closing
   line and its `bottom_rule` were both set to the SAME `to_edge(DOWN, buff=0.5)`, landing the
   closing text partly outside the safe area (overlapping the rule's own safe placement). Fixed by
   giving the text `buff=0.68` (matching B04/B05's established text-above-rule convention) and the
   rule `buff=0.5`. Re-ran: GATE A/B clean on the remaining pending beats (B06-B09).
3. **Review-slate GATE V matched the documented burn-in false-positive pattern exactly:** 20
   BLOCKER / 0 MAJOR for this 10-beat reel (2 per beat), not trusted at face value.
4. **The TRUE final landscape candidate passed GATE V clean on the first attempt — 0 BLOCKER, 0
   MAJOR:** built via `compile.py --out deliverables/landscape --height 2160` directly (true 4K, no
   `--review`). Wrote a `.verified.json` with `"status": "ready"`. Independently re-ran
   `final_frame_check.py --lenient` directly against the written candidate: **0 BLOCKER, 0 MAJOR.**
5. **A real visual defect caught only by extracting and looking at real frames, not by any
   automated gate:** B06's small file-label captions ("rag.py"/"config.py") were rendered in
   `PALETTE["slate"]` on an ink background — a combination this file's own `PALETTE` dict comment
   already documents as broken contrast, but too small a region for GATE V's whole-panel contrast
   sampling to trip on. Fixed by switching to `PALETTE["sage"]`, the house-documented safe
   substitute. Re-rendered only `B06_MycroftRealWorldNote` directly via `manim` (bypassing
   `run.sh`/`./art run` entirely to avoid the documented shared-`clips/`-cache-reverts-to-preview-
   resolution side effect), confirmed clean via a scoped layout-audit re-check, then rebuilt the
   final master directly via `compile.py` again. Re-verified: still 0 BLOCKER/0 MAJOR, 202.5s.

**Landscape final:** `deliverables/landscape/EmbeddingModelStaleness_SaiPranaviJ.mp4` — 3840x2160,
24fps, h264/aac, **202.5s** (ffprobe). GATE V on the true clean master (`final_frame_check.py
--lenient`, run directly against the deliverable, not a `-slate.mp4` review cut): **0 BLOCKER, 0
MAJOR.**

## 2026-11-19 — Vertical build

Scaffolded via `./art vertical <reel> --no-endcard --handle "@HumanitariansAI"` (both flags
explicit). Confirmed it copies the parent's 10 mp3s and beat-sheet metadata into `vertical/`
(`aspect_ratio: "9:16"`) and correctly refuses to auto-generate a portrait Manim layout for any
GENERATED beat. `vertical/scenes.py` was hand-authored ahead of rendering, with every beat's timing
hand-matched to `../scenes.py` beat-for-beat. Confirmed the `config.frame_width` portrait patch
(toolkit bug #7) is actually present and active in the written file, not just documented in a
comment, by direct grep/read before relying on it.

### Real findings during the vertical build

1. **A real GATE A false positive on B04, matching the documented stub-vs-real-Manim-portrait
   divergence class exactly:** flagged "1 explicit coord(s) outside the frame" for a `move_to` call
   that does not exist anywhere in the file (confirmed by direct grep — every `move_to()` call takes
   `.get_center()` or `ORIGIN`). Independently verified via the real pixel-true
   `manim_layout_audit.py --portrait`, run against a scratch copy of the file for ALL 10 beats: B04
   came back CLEAN.
2. **A real GATE B warning on B06, found and fixed before any full render:** "label on a curve/line"
   near a quoted code row. A rendered frame appeared to show an overlap, but a static debug scene
   built from the identical positioning code (no animation) showed zero overlap, proving the
   apparent defect was a mid-transition extraction artifact, not a layout bug. The REAL root cause,
   found via a small Python coordinate probe: `code_rows`' inter-row `buff=0.18` left only ~0.02
   units of clearance against each row's `box_around()` `buff=0.16` highlight box — not comparable
   to the landscape file's comfortable 0.25-unit clearance (`buff=0.35` vs. `buff=0.1`). Fixed by
   widening the inter-row buff to 0.4. Re-verified via the real portrait auditor against all 10
   beats again: all 10 CLEAN, 0 errors, 0 warnings — confirmed BEFORE rendering, not after.
3. **A real GATE V underfill/edge-bleed cycle on the first true vertical candidate, not a burn-in
   false positive:** `compile.py --out deliverables/vertical --height 3840` REFUSED with 2 BLOCKER
   (B08 `edge-bleed`, both samples) + 4 MAJOR (B02 48% fill, B09 47% fill, both min 55%). Fixed
   B08 by capping its frame width (`min(content.width + 0.8, 3.7)`) to stay inside the portrait
   safe full-width; fixed B02/B09 with genuine added content mass (larger real text, wider real
   rules, more real spacing between real elements — never a padding rectangle). The B08 fix
   round-tripped once: capping the width dropped its own fill to 53% (just under the floor),
   recovered with more real content mass within the now-capped width. Verified each fix via the
   tool's own `--frames-dir` direct-PNG test mode against scratch-rendered frames before touching
   the full pipeline again.
4. **A real cross-aspect duration mismatch, caught by explicitly checking the hard constraint
   (not just two independent green GATE V results):** the second true vertical candidate passed
   GATE V clean but measured 202.458s vs. landscape's 202.500s via `ffprobe` — a 1-frame (4860 vs.
   4859 frames) real mismatch. Root-caused to B06: its vertical `scenes.py` used `self.wait(1.3)`
   twice where the design intent (and the landscape file) used `self.wait(1.7)` — a real 0.8s
   authoring drift, silently absorbed by `compile.py`'s own silent-retime-within-±5% step rather
   than erroring. Fixed by restoring `1.7` in both places; confirmed the raw clip now matches
   landscape's exactly (32.041667s).
5. **A real empty-Text bounding-box bug, found only by printing raw coordinates, not by eye or by
   any gate:** while re-rendering B06 for the duration fix, a frame showed two highlight boxes
   visibly overlapping. Root cause: continuation code lines were built via
   `code_row("", "settings.embedding_model", ...)` — an empty-string `Text("")` label. Manim's
   `Text("")` has no points, so it's never repositioned by `arrange()`, yet `VGroup.height`/
   `get_top()`/`get_bottom()` still fold its origin-anchored bounding box into the group's extent,
   silently inflating `box_around()`'s computed box height. Fixed by rewriting the statement
   builder to take one real label plus a list of real code lines, with no empty-string `Text()`
   created anywhere. Re-verified via the real portrait auditor (0 errors/0 warnings) and a fresh
   extracted frame (three cleanly separated boxes) before re-slotting.
6. **The TRUE vertical candidate passed GATE V clean on the final re-run — 0 BLOCKER, 0 MAJOR,**
   with duration now frame-exact against the landscape master (4860 frames each via
   `ffprobe -count_frames`, not just matching rounded seconds). Real frames extracted and
   personally inspected at B02, B04, B06 (repeatedly, across the bug-fix cycle), B07, B08, B09 —
   all clean, properly filled, no overlap, mechanism legible in both B04 (SPLIT GEOMETRY —
   SILENTLY) and B05 (FULLY RE-EMBEDDED — NOTHING TO MIX), and B06's verbatim code quotes read
   correctly and legibly against the real `rag.py`/`config.py` source.

**Vertical final:** `deliverables/vertical/EmbeddingModelStaleness_SaiPranaviJ.mp4` — 2160x3840,
24fps, h264/aac, **202.5s** (4860 frames via `ffprobe -count_frames`) — frame-exact match with the
landscape master, not just matching rounded seconds. GATE V on the true clean master
(`final_frame_check.py --lenient`, run directly against the deliverable): **0 BLOCKER, 0 MAJOR.**

**Deliverables confirmed (both masters, both GATE V clean, both ffprobe-verified, frame-exact
duration parity):**
- `deliverables/landscape/EmbeddingModelStaleness_SaiPranaviJ.mp4` — 3840x2160, 24fps, h264/aac,
  202.5s (4860 frames). GATE V: 0 BLOCKER, 0 MAJOR.
- `deliverables/vertical/EmbeddingModelStaleness_SaiPranaviJ.mp4` — 2160x3840, 24fps, h264/aac,
  202.5s (4860 frames). GATE V: 0 BLOCKER, 0 MAJOR.

Both masters' durations match exactly (202.5s each, 4860 frames each, confirmed via `ffprobe`).

Publishing not authorized. Nothing inside `brutalist/` was modified. Nothing inside `mycroft` was
modified (read-only reference).
