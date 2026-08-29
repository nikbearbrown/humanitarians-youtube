# BUILD-LOG — claude-liam-rag-deep-explainer

## 2026-08-16 — authored + built

- HUMAN NOTE (logged first): requester asked for a `deep-explainer` build of
  the same chapter as the sibling `ai-explainer`/`cli-explainer` reels
  (`chapters/01-introduction.md`), same voice and signature
  (Kokoro `am_onyx` / `@VedanshuDaxeshPatel`). `deep-explainer` is ADVANCED
  (Bear-only) per this toolkit's CLAUDE.md rule 8 — surfaced once already
  this session for `cli-explainer`; proceeding on the same standing basis
  (the requester's direct, explicit instruction) rather than re-litigating
  the same tier boundary a third time in one session.
- Plan: 34 beats — B00 cold open + 31 body beats across six acts + closing
  block (BVDT verdict / BHTF your-turn / BOUT title outro). Lane mix (body):
  vox 7 (22.6%) · manim 8 (25.8%) · remotion 13 (41.9%) · card 3 (9.7%).
  Vox share centered in the 20–25% target band.
- Vox runs: R1 = B02→B03 (help-desk establishing → chat-screen push), R2 =
  B19→B20 (server-room establishing → clock/queue push), R3 = B28→B29 (the
  SAME help-desk scene as R1, resolved/calm → the corrected answer push).
  Handoffs authored at plan time in `beat_sheet.json`.
- No pantry_search.py / local stock library (`svg/svg/`) exists in this
  toolkit checkout — Tier 0 (free local search) is genuinely unavailable
  here, unlike the reference example this build followed
  (`examples/deep-explainer/claude-liam-fluency-trap`). All 7 VOX slots are
  logged straight to SHOPPING.md as Tier 1 (generic/illustrative — no real
  referent anywhere in this chapter's content, so no rights escalation).
- Reused components (no new motion math, per the starter-template
  contract): `RagExecutiveSummary` ×6 (B04, B06, B07, B12, B18, B23),
  `RagRetrieveGenerate` ×2 (B13, B30), `RagThreeFixes` ×1 (B22),
  `RagPredictCard` ×1 (B24), `RagFitsInPrompt` ×1 (B25), `FluencySegmentCard`
  ×3 (B01, B17, B27, borrowed from the fluency-trap reel's already-shipped,
  already-registered component — a generic Roman-numeral act card, not
  reel-specific content). One genuinely new component:
  `DeepQuoteCard` (B11, B16) — a verbatim-quote beat, built with FRAME-based
  spring timing specifically to avoid the duration-registration bug class
  found while building the sibling reels (see Root.tsx comment above the
  Rag* registrations).
- 8 new Manim scenes authored in `scenes.py`: B05_TrainingCutoff,
  B08_FrozenWeights, B10_LiveStore, B14_RetrieverSearch,
  B15_GeneratorCondition, B21_RetrievalVsFinetune, B26_Threshold,
  B31_SameMechanism. No invented numbers on screen; B21 carries its citation
  on screen alongside qualitative-only bars.
- FACTCHECK.md: 9 rows, all closed against the chapter + its own cited
  sources. No narration changes required.

## Gate status

- [x] GATE F — FACTCHECK.md, 9/9 rows verified, closed.
- [x] GATE P — PEDAGOGY.md signed PASS (personal-author standing
      authorization, free Kokoro pipeline only, consistent with the sibling
      reels this session).
- [x] Audio lock — 35 Kokoro mp3s, 6:11 total; `actual_duration_s` per beat
      is ground truth.
- [x] Gate D2 SHOPPING.md — written from locked windows, 7 slots, all Tier 1.
- [x] Gate D1 previz — PASS 1 COMPLETE (this session).
- [ ] Pantry fill / review cut / final — pending; this build ships as an
      honest Gate-D1 previz with 7 VOX slates, by design.

## Pass 1 build — 2026-08-16

**`run.sh` could not run end-to-end on this Windows/Git-Bash environment.**
Its inline `python3 -c "...open('$REEL_DIR/...')..."` calls choke on
MSYS-translated `/c/...` paths (native Windows Python can't resolve them) —
confirmed via direct reproduction, not assumed. Same class of friction as
the `compile.py` cp1252 crash hit earlier this session. Worked around by
running each stage manually, the same approach that worked for the sibling
reels:

1. **Manim (8 scenes, `-qh` 1920×1080):** B05_TrainingCutoff,
   B08_FrozenWeights, B10_LiveStore, B14_RetrieverSearch,
   B15_GeneratorCondition, B21_RetrievalVsFinetune, B26_Threshold,
   B31_SameMechanism — all rendered successfully, copied to `manim/<BID>.mp4`.
2. **Remotion (19 beats):** `remotion_scenes.py` — 18/19 succeeded first
   pass; BHTF hit a transient `createSilentAudio` file-handle error on
   retry, succeeded clean on a second attempt (`--only BHTF --force`).
3. **Compile (`--review --height 1080`):** 28/35 filled (7 VOX beats slate,
   by design). Flagged B31 as "extreme slow-mo" (3.2x stretch, native
   Manim clip only 3.8s vs. a 12.2s beat) — fixed by extending the scene's
   own hold/transition timing (added underline reveal + longer waits) to
   ~13s native, eliminating the stretch (now a clean 0.4s head/tail trim).
4. **Visual QC (743 frames @ 2fps + per-lane spot checks):** found and
   fixed one MINOR margin issue (B21's citation line at `buff=0.5`, tighter
   than this reel's other stamps — widened to `0.8`, re-rendered,
   re-verified). Zero BLOCKER/MAJOR. Full report: `_qc/REPORT.md`.

**Slots: 28/35 filled** — MANIM: B05 B08 B10 B14 B15 B21 B26 B31 · VIDEO:
B00 B01 B04 B06 B07 B11 B12 B13 B16 B17 B18 B22 B23 B24 B25 B27 B30 BVDT
BHTF BOUT · SLATE (pantry): B02 B03 B09 B19 B20 B28 B29.

**Review cut:** `claude-liam-rag-deep-explainer-slate.mp4` (371.4s, 6:11).

## Gate D1 previz — CLOSED (Pass 1 complete)

**STOP — pantry fill is next.** Drop the 7 files named in `SHOPPING.md` into
`pantry/`, then re-render/recompile. When all 35 filled: clean master.
