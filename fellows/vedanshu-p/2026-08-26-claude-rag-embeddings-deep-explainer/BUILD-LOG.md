# BUILD-LOG — The Geometry Of Meaning.

## 2026-08-26 — authored (Part A)

- Human requested a `deep-explainer` build of *RAG Foundations* Chapter 3,
  voice Onyx, signed Vedanshu Daxesh Patel, 4K, matching the existing
  ai-explainer and cli-explainer sibling reels for this chapter, folder
  dated 2026-08-26.
- ADVANCED-tier gate (CLAUDE.md rule 8) surfaced; proceeding on the same
  precedent already confirmed for cli-explainer and this book's own
  Chapter 1/2 deep-explainer siblings — not a claim of being Bear.
- Plan (6 acts, 30 body beats, lane histogram) presented via plan mode and
  approved by the human before any beat was authored in full, per
  SKILL.md's own `plan → GATE: approve` workflow step.
- `beat_sheet.json` authored: 34 beats total (30 body + cold open + verdict
  + handoff + outro), lane mix CARD 3 / VOX 7 / MANIM 8 / REMOTION 12 — all
  within lint bands (vox 23.3%, manim 26.7%, remotion 40%). Two vox runs
  (R1: B02–B03, R2: B17–B18), three single vox stills (B12, B23, B29), all
  Tier 1 (generic, no rights escalation).
- `scenes.py` authored: 8 Manim scenes (`B04_VocabularyToVectors`,
  `B08_VectorArithmetic`, `B09_ExcludeTheQuery`, `B11_WordToPassage`,
  `B13_BertToSbert`, `B19_CosineGeometry`, `B21_ClosenessPremise`,
  `B26_ParaphraseVsTrap`) — test-rendered at low quality (`manim -ql`) to
  confirm all 8 run without error before authoring their beats' final
  content; no new components needed beyond the existing palette helpers.
- Zero new Remotion components needed: REMOTION beats reuse
  `ProblemExecutiveSummary` (11×, generic headline/subline/sparkLine,
  already registered from the Chapter 2 sibling), `DeepActCard` (3×, same
  sibling), and `EmbedSpeedLeap` (1×, from this chapter's own ai-explainer
  sibling's `EmbedIllu.tsx`) — all props-only reuse.
- `SOURCES.md`, `FACTCHECK.md` (GATE F: CLOSED, 9/9 rows verified),
  `PEDAGOGY.md` (VERDICT: PENDING), `CHECKS-REPORT.md` written.
- Honesty notes carried into this build: B09/B10 state only the chapter's
  own qualitative replication caveat (excluding the query word matters),
  no invented statistics; B22–B26's worked example stays strictly
  qualitative — no cosine number is put on screen anywhere, matching the
  chapter's own explicit disclaimer that no embedding model was actually
  run to produce a score for that example; B30/BVDT name the open "what
  counts as one chunk" question without depicting how Chapter 4 resolves it.

## 2026-08-26 — audio lock, Gate D2, Gate D1 previz (Part B)

- GATE P signed by Vedanshu Daxesh Patel (see PEDAGOGY.md).
- Audio generated (Kokoro `am_onyx`, free): 34/34 beats, total ≈ 7:13.
- `SHOPPING.md` written after audio lock with locked durations for all 7
  VOX beats (2 runs + 3 singles), all Tier 1.
- Gate D1 previz built by direct `manim`/`remotion_scenes.py`/`compile.py`
  invocation rather than `run.sh` — same known Windows path bug documented
  for every prior reel this session. 8 Manim scenes rendered at 3840×2160
  for real; 19 Remotion beats rendered clean on first pass; previz compiled
  with `--review --height 2160`: 3840×2160, 433.1s, 27/34 filled, 7 VOX
  beats correctly rendered as labeled slates.
- Visual QC on the previz found and fixed two BLOCKER defects at the
  source (`scenes.py`): B09's labels collided (rebuilt the layout with
  well-separated coordinates); B19 briefly showed a claim/visual mismatch
  (the "small angle" caption lingering after the angle had already
  widened) plus a vector tip nearly running off-frame (reordered the label
  swap and tightened the geometry). Both re-rendered at 4K, re-verified clean.

## 2026-08-26 — pantry fill, final master (Part B continued)

- Pantry images sourced directly (no AI image generator available in this
  environment) via a background research agent: real, licensed stock
  photos (WebSearch/WebFetch), each with a `pantry/<BID>.source.txt`
  sidecar (url/license/credit/retrieved date). All 7 slots filled: B02/B03
  (library run), B12 (research desk), B17/B18 (card-catalog run), B23
  (two-desk office), B29 (paper stack).
- **Two real legibility defects caught on visual QC of the compiled
  master, not just at sourcing time**: B03's original photo showed
  genuinely readable full sentences from a real, unidentified book
  (page numbers visible) — more legible than the "text as abstract
  texture" brief intended. B12's original photo legibly branded a real
  open-source charting library ("Morris Charts") plus a branded pen
  ("spoko") — a specific real product, which the Tier-1 brief for this
  beat explicitly disallows. Both were re-sourced by a second agent pass
  with explicit instructions to zoom into any text-bearing region before
  accepting — B03 became a page-edge/fanned-pages close-up with no
  legible words anywhere; B12 became a different desk prop from the same
  photographer's series showing only generic placeholder chart labels
  ("Our company," "Receipts/Sales/Orders"). Sidecars document the
  substitution reasoning.
- `pantry.py` intake run three times (initial 7-fill, then again after
  each Manim-cache cleanup accidentally wiped the reel's `media/` folder —
  see note below — then again after the B03/B12 replacement); `pantry.py`
  does not itself copy `.source.txt` sidecars into `media/` (it only stubs
  a generic placeholder if one is missing), so the real sidecars were
  mirrored into `media/` by hand each time.
- **Self-caught process bug, disclosed rather than silently worked around**:
  Manim's own render cache directory is also named `media/`, and it lives
  at the same reel-root level as the toolkit's own `media/` folder (where
  `remotion_scenes.py` and `pantry.py` write their real output). Running
  `rm -rf media` to clean up Manim's cache after a render — done twice
  during this build — twice deleted the toolkit's already-rendered
  Remotion clips and, the second time, the already-intaken pantry stills
  too. Both times this was caught immediately by the next compile's
  "nothing rendered" warnings/refused-slate-count rather than silently
  shipping a broken master; recovered by re-running `remotion_scenes.py`
  and `pantry.py` intake. Lesson for future reels in this book: never
  `rm -rf media` at the reel root — target Manim's own subpaths
  (`media/videos`, `media/images`, `media/texts`) or move the rendered
  clips out *before* deleting anything.
- Recompiled: `compile.py --height 2160` (no `--review`) → **34/34 filled,
  zero slates** → `claude-rag-embeddings-deep-explainer.mp4`, 3840×2160,
  433.1s. Frame-checked the two replacement stills directly against the
  compiled output at full resolution — both clean, no legible text/branding.
  B17/B18 (portrait-oriented sources) triggered `compile.py`'s conservative
  width-based upscale warning; visually confirmed sharp with no artifacts,
  accepted (same disposition as this book's Chapter 1 sibling reel).

## Gate status

- [x] GATE F (factcheck) — CLOSED, see FACTCHECK.md
- [x] GATE P (pedagogy sign-off) — PASS, signed by Vedanshu Daxesh Patel
- [x] Audio lock — 34/34 beats, Kokoro am_onyx, ≈7:13 total
- [x] Gate D2 (SHOPPING.md) — written after audio lock, all 7 slots filled
- [x] Gate D1 previz — built, 4K, 27/34 filled, 2 BLOCKERs found and fixed
- [x] Pantry fill — 7/7 stills placed (5 clean on first pass, 2 replaced
      after visual QC caught legibility defects)
- [x] Final master — `claude-rag-embeddings-deep-explainer.mp4`, 3840×2160,
      433.1s, 34/34 filled, 0 BLOCKER/MAJOR
- [ ] Never publish — master stays in this reel folder (standing rule, not a TODO)
