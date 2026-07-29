# VISUAL-PLAN — Personalized, Project-Driven Reading Roadmaps

AI-explainer (`claude-hai`) reel. 1920×1080, 30fps. Audio-first: every scene is a pure function of its beat's measured MP3 clock (`useP()` → `p ∈ [0,1]`) — no CSS transitions, no timers, no `Math.random()`.

## Palette contract (two skins, one reel)

| Where | Palette | Tokens | Rationale |
|---|---|---|---|
| **UI / bookend beats** — B00 (ask), B07 (verdict), B08 (handoff), B09 (outro) | **claude** (fidelity) | `runtime/remotion/src/tokens/claude.ts` — PAGE `#FAF9F5`, INK `#3D3929`, SPARK `#D97757` | ai-explainer is a FIDELITY brand: the Claude UI beats replicate the real product. Never retint. |
| **Body illustration beats** — B01–B06 | **humanitarians** | `runtime/remotion/src/tokens/humanitarians.ts` — CREAM `#F3EBDD`, INK `#2F2A26`, TEAL `#1F4E5F` (good/kept), CRIMSON `#E4572E` (bad/caution), SLATE `#29335C` (structure), GOLD `#F3A712` (fill only), SAGE `#A8C686` (human) | ai-explainer ASK→RESULT LAW: "RESULT graphics render in the episode channel's palette … hai: the humanitarians token set." |

Accent discipline holds in BOTH skins: **one focal accent per beat** (terracotta on the claude skin; teal or crimson as the single meaning-carrying mark on the humanitarians skin). Type: EB Garamond (serif) + Montserrat (sans headers). Every beat carries the small HAI corner bug lower-right (LOGO LAW); the outro shows the mark full-size.

## ILLUSTRATE LAW compliance

The Claude UI appears **only** on B00 / B07 / B08 / B09 (cold open, verdict, handoff, outro). Every inner beat (B01–B06) ILLUSTRATES its concept on the humanitarians stage — no composer wallpaper, and no two consecutive beats share a visual scheme (fanout → strike+reorder → pipeline → graph → table → checklist).

## Reusable vs. new components

Four reusable structural components exist (`runtime/remotion/src/illustrations/structural.tsx`): `LayerStack`, `SourceFlow`, `ChipGrid`, `PredictCard` — all authored on the **claude** palette. This reel's body needs six domain-specific illustrations that either **retint** a structural component or are **net-new**. Net-new components render as **labeled slates** (`PIPELINE → fill media/Bxx.mp4`) on the first compile (fill-in-first doctrine), exactly as the algorithmic-art exemplar shipped its `AlgArt*` scenes.

| Beat | Pattern (this reel) | Base | Build note |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | ships | Required cold-open ask. Set `output[]` (RESULT lines), `modelLabel`/`effortLabel`, `folderLabel:@HumanitariansAI`. |
| B01 | `RoadmapProblemFanout` | net-new | One book duplicates identically, arrows fan to N distinct project cards. Could start from an inverted `SourceFlow` (one source → many dests) but motion differs → new component. |
| B02 | `RetrieveVsReorder` | net-new (rhetorical) | Strike `content→ordering`; a ranked list re-threads into a dependency path; one high-sim item lifts to a "held back" tray. Nearest kin: `BinaryBranch` in `deckPatterns.tsx`. Author `anim.json` entry. |
| B03 | `RoadmapPipeline` | retint of `SourceFlow`/net-new | 4 nodes L→R, each with an artifact chip; per-textbook vs per-student bracket. Model after the exemplar's `AlgArtPipeline`. |
| B04 | `DependencyGraphReview` | net-new | Node graph; solid TEAL = faculty-approved prereq edges (check badge), dashed GOLD = model-proposed (CRIMSON "under review" badge on some). |
| B05 | `WeeklyRoadmap` | net-new | Table fills row-by-row (Week · Section · Why · Lab task); once faculty-approved prerequisites exist, a required background row can pull earlier (conditional — not asserted as already active); split to two divergent project roadmaps. |
| B06 | `LimitsAndFuture` | retint of `ChipGrid` + panel | Four caution chips land, then a greyed "adaptive layer — DEFERRED" panel. |
| B07 | `ClaudeVerdictArtifact` | ships | Five verdict lines staggered on their spoken clauses. |
| B08 | `ClaudeComposerAsk` | ships | Handoff; `greeting:"Your turn."`, `runningText:"paste this into Claude…"`. |
| B09 | `ClaudeTitleOutro` | ships | Title restate + `@HumanitariansAI` + Satwik sign-off subline. |

New components live in `remotion-src/` beside the beat sheet, follow the structural-family contract (props only, no motion-math forks), keep one accent, and register in the reel composition. `RetrieveVsReorder` is a rhetorical (changes-over-time) beat → gate it through `anim.json` per the animated-deck rule.

## Per-beat show design

Each beat's ordered `show` events (what the viewer WATCHES as each phrase lands) are authored in `beat_sheet.json` under `shot.show`. Design intent per beat:

- **B00 (ASK):** greeting + spark → ask types in → send arms terracotta → 3 RESULT lines stagger (ASK→RESULT at the cold open) → `@HumanitariansAI` centered bottom overlay (first beat only, per hai skill).
- **B01 (problem):** a 38-tick topic-ordered book draws → duplicates identically → arrows fan to distinct project cards → faint "unread" watermark. Enacts "same book, different projects."
- **B02 (reframe):** "a content problem" types then is **struck through**; "an ordering problem" types beneath in teal → ranked top-k list (LEFT) → a blinking unanswered "read first?" badge (the ranker can't order) → sections **re-thread** into an arrowed dependency path (RIGHT) → one high-similarity item **lifts out** to "held back" (select, don't retrieve). This is the reel's thesis beat.
- **B03 (pipeline):** four nodes draw in on "One/Two/Three/Four"; each drops its artifact chip; connector arrows draw on; a terracotta bracket marks stage 4 "per student"; artifact chips flip to an "editable" mark on "inspectable, editable file."
- **B04 (graph + faculty):** nodes appear → **solid teal** approved prereq edges with a check badge → **dashed gold** proposed edges → some keep a **crimson "under review"** badge (guardrail: NOT all approved) → irreducibly-human caption "propose = AI · approve = faculty."
- **B05 (output):** table header draws; rows fill; **once faculty-approved prerequisites are available**, a required background row can **pull earlier** (conditional — the reel does not claim prerequisites are already pulling sections forward today); frame **splits** to Project A vs Project B; shared rows neutral, unique rows distinct — divergence visible = personalization.
- **B06 (limits + future):** four caution chips land one per limit (single textbook · advisor heuristic · **rule-based/deterministic tagging → uncertain metadata to faculty review** · no outcome data); then a **greyed** "adaptive layer" panel fades up stamped "DEFERRED · not implemented" (guardrail: future, not shipped).
- **B07 (verdict):** Claude artifact page; five lines stagger on their clauses; terracotta marks "reordering, not retrieval"; last line "Learning outcomes: future work" (no over-claim).
- **B08 (handoff):** "Your turn." → the paste-ready prompt types in while the voice **summarizes and discusses** it (shortened; no longer read verbatim) → "flag every prerequisite that needs human approval" highlights terracotta (human-in-the-loop) → holds for the pause.
- **B09 (outro):** poster-serif title restate with terracotta period → `@HumanitariansAI` + full HAI mark → Satwik sign-off subline.

## Guardrails enforced in the visuals (see SOURCES.md ledger)

1. **No effect sizes on screen** — every Hattie *d* in the draft is a `[TO DO: confirm]`. No numeric d anywhere.
2. **No "all prerequisites approved"** — B04 always shows dashed **under-review** edges alongside approved ones.
3. **No "adaptive / real-time" as shipped** — B06's future panel is greyed and stamped **DEFERRED**.
4. **No learning-outcome claim** — B06 flag + B07 closing line both say outcomes are future work.
5. **No textbook title/authors on screen** — draft placeholder; refer to it generically ("38-chapter, topic-ordered").
6. **Concepts used on cards** (particle stability, surface chemistry, cellular uptake, pharmacokinetics; concepts/mechanisms/techniques) are drawn verbatim from the draft's own examples — see SOURCES.md.

## QC (VISUAL QC LAW — after each `compile.py`)

Sample ≥2 fps + each beat at ~15/50/85% → **Read the PNGs** → audit the 9-point rubric (edge bleed, title-safe 5% inset, overflow, collision, offscreen anchors, legibility, HAI bug placement, aspect, CANVAS FILL). Two-skin check: confirm B00/B07/B08/B09 read as the **claude** cream/terracotta UI and B01–B06 read as the **humanitarians** editorial set; confirm exactly one accent per beat. Log to `_qc/REPORT.md`; fix root causes in scene source; re-render until zero BLOCKER/MAJOR.
