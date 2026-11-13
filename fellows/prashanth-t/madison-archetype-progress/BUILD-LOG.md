# BUILD-LOG — madison-archetype-progress

Deviations and findings that need an explicit author justification rather than a
silent pass, per the PROOF GATE and VISUAL QC LAW.

## 1. B01 typing overran its beat — found by frame inspection, fixed

The first compile passed every gate the same way the previous reel did, but
sampling B01's final frame showed it read:

    I'm scoping a brand-archetype analyzer.
    It reads your real evidence
    and ends in dec|

The `quiz` → `analyzer` correction fired correctly (the single-token lesson from
`llm-function-calling` held), but the sentence was **cut off mid-word**, so the
mandatory executive summary never completed.

Cause: `BrutalistHesitantWriter` paces its performance in absolute milliseconds
(`charMs`), not as a fraction of the composition, so it cannot be re-timed by
`durationInSeconds` — it simply truncates. At `charMs: 34` with the trigger
pause, two newline pauses and three punctuation pauses, the performance ran past
the 10.47s audio window.

Fixed by tuning the performance to fit: `charMs: 22`, `hesitateWithin: 0`,
`hesitateBetween: 4`. Verified by re-sampling the final frame — the whole
corrected sentence is now on screen and holds before the cut.

**Lesson for the next reel:** for this component, always sample the final frame.
A gate-clean build does not prove the typing finished.

## 2. Outro is `FnCallTitleOutro`, not `ClaudeTitleOutro` — deliberate

SKIN LINT warns: *"BOUT: palette=claude but the outro is 'FnCallTitleOutro' —
OUTRO LAW wants ClaudeTitleOutro."*

Justified, same as the previous reel. `ClaudeTitleOutro` hardcodes
`@NikBearBrown` and always renders a mascot; `OUTRO-LOCK.md` scopes that card to
claude-liam / @NikBearBrown reels and states other channels *"have their OWN
outros and NEVER get this card, handle, or mascot."* This is an
`@HumanitariansAI` reel. `FnCallTitleOutro` keeps what OUTRO LAW requires — exact
title restate, poster serif, terracotta terminal period, handle beneath, no
subline, slug-seeded polarity — and drops only what the lock reserves. The lint
checks the component name, not the channel scope.

## 3. Motion histogram is 100% Remotion — accepted

Warning: *"'remotion' carries 14/14 beats (100%) — over the ~40% pantry cap."*

Accepted. The cap guards against a single-language slideshow; the mix it assumes
needs Manim fragments or sourced media. This is a planning-stage project update
with no equations and no footage to source. Every beat carries a distinct visual
scheme (composer, hesitant writer, chip grid, layer stack, predict card, source
flow, code block, binary branch, verdict artifact, title card) and **no two
adjacent beats share one**, so the monotony the cap exists to prevent does not
occur. Adding Manim to satisfy a ratio would be padding.

## 4. Final QC state — BLOCKER 0, MAJOR 9, all `underfill`

| Frame | Fill | Assessment |
|---|---|---|
| B01_50 / B01_85 | 9% / 31% | Three-line centred serif at 92px. Cannot reach 55% without redesigning the component. |
| B02_50 | 50% | **Transient** — sampled mid-stagger; all twelve chips are present by 85% (absent from the report at that sample). |
| B03_50 | 30% | **Transient** — cards still stacking. Clean by 85%. |
| B04_50 | 53% | Two points under; `PredictCard` exposes no size prop. |
| B09_50 | 38% | **Transient** — scope ladder still stacking. Clean by 85%. |
| B10_50 | 23% | **Transient** — status chips still landing. Clean by 85%. |
| BVDT_50 / BVDT_85 | 51% | `ClaudeVerdictArtifact` geometry. Four points under. |

**Five of the nine are transient mid-stagger samples** (B02, B03, B09, B10 and
partly B01): GATE V samples at 50% of each beat, when by design not every element
has landed. Their `_85` frames are absent from the report, which is the evidence
that the animations now complete — the duration fix from the previous reel is
doing its job. Front-loading those reveals to clear the metric would fight the
signalling principle (reveals land ON the spoken word).

The remaining four (B01 ×2, B04, BVDT ×2) are **shared-component geometry**.
Raising their fill means changing layouts used by other reels, which was out of
scope for a reuse-only build.

No BLOCKER at any point. `./art run` exits 2 because MAJOR is treated as
blocking; `ART_STRICT=0` downgrades it.

## 5. Reuse-only constraint held

No new components were built. Nothing was added to `Root.tsx`, no `scene-index`
rebuild was needed, and `TEMPLATE-MISSES.md` gained no entries. Every scene was
confirmed RENDERABLE before authoring.

This reel is also the first to benefit from the `calculateMetadata` duration fix
made during `llm-function-calling`: the shared compositions re-time to their
beats, so a 14–18s beat no longer shows only half of a 30s animation.
`ClaudeCodeBeat` (B08) is the intentional exception — at 300f/10s it completes
inside its beat and freeze-holds.

## 6. Layout constraint resolved before rendering

B02 shows all twelve archetypes. `cols=4` would put the grid at 1338px on a
1280px stage (`x0=-29`, off-canvas — an edge-bleed BLOCKER). `cols=3` fits (4
rows ending at y=678, inside the 684 limit) but row four collides with the
caption slot (~598). Resolved as `cols=3` with no caption, clarifier moved to the
spark line. B10's five chips keep their caption — two rows, no collision.

## 7. Environment

`ART_NO_DRAWTEXT=1 PYTHONUTF8=1 ART_SCALE=1`. The first two work around unfixed
Windows bugs (ffmpeg filtergraph font path; cp1252 stdout). `ART_SCALE=1` is the
pacing-cut setting — **text is not supersampled in this cut**; drop it for a
master.
