# BUILD-LOG — The Silent Thief (The Uncertain Eye S1E01)

Built 2026-09-07. Channel `claude-hai` / @HumanitariansAI, Kokoro `am_onyx`, free
path throughout. No paid API was called at any point.

## Order of work

1. Read `THE_UNCERTAIN_EYE_series.md` in full, then
   `skills/make/ai-explainer/SKILL.md` in full (Rule 1), plus `nopunt/SKILL.md`,
   `brands/hai.md`, and the sibling reel `hai-only-the-uncertain-cases` as the
   nearest precedent (same project, same channel, same voice).
2. GATE L — library search before authoring any beat.
3. Authored `beat_sheet.json` (11 beats), `CHECKS-REPORT.md`, `SOURCES.md`,
   `DESIGN-CARDS.md` — all before the first render, per PROOF GATE.
4. Built four new components, registered them, regenerated the index.
5. Audio, then composition-duration sync, then scene render, compile, visual QC.

## Decisions

**Rate calibration instead of the doc's word budget.** The series doc budgets
~150 wpm. The sibling reel measured **187.4 wpm** aggregate on Kokoro `am_onyx`
(range 139-224, slowest on number-heavy beats). Scripted to the measured rate,
not the assumed one: 483 words, predicted 2:36, **measured 2:21**. Inside the
2:00-2:45 target with margin at both bounds.

**Remotion for all body beats, not Manim.** The nopunt catalog routes "moving
mechanism" to Manim. Overridden deliberately, matching the sibling reel's
decision: keeping this lane Remotion-only means no LaTeX dependency in the
glaucoma series. B03's fiber mechanism and B04's threshold both animate cleanly
as SVG under `useP()`. Logged here as required when deviating from the catalog.

**One ask-to-result pair, not one per graphic.** ASK-RESULT LAW read literally
would put a composer beat before all six illustrated beats. House practice
(sibling reel, explicitly noted in its metadata) is one representative pair per
reel. B06 to B07 is that pair, and it sits on the episode's actual pivot.

**B01 added to the author's structure.** The series doc's Episode 1 is
hook/body/your-turn/hook-out. The chassis mandates a BLUF at beat 2
(EXECUTIVE-SUMMARY LAW), so B01 is the one beat not in the source. Its
hesitant-writer correction carries the episode's real misconception
(`a looking problem` to `a pattern problem`), which B05 dismantles and B07
replaces — the correction is load-bearing, not texture.

**`SourceFlow` evaluated and rejected for B07.** Its geometry is fixed as a dark
server rack feeding an app window — wrong imagery for an eye and a measurement,
and it would break the cream fidelity stage. Purpose-built instead.

## Repo fixes made during this build

**Stale scene index (real bug, fixed).** `./art scenes --check HaiGlaucomaStakes`
reported **NOT RENDERABLE** although all eight `HaiGlaucoma*` components are
correctly registered as `<Composition>` in `Root.tsx` (line ~3652, inside
`<Folder name="HaiGlaucoma">`). The cause was `scenes.json` never being
regenerated after that reel shipped, so the components existed but were
invisible to every search. Ran `./art scene-index` (601 to 609 renderable).

This is exactly the failure Rule 8 exists to prevent, and it nearly cost this
episode a duplicate component: `HaiGlaucomaStakes` already had this episode's
80M/111M numbers as its schema defaults. B02 reuses it unchanged.

**`TEMPLATE-MISSES.md` did not exist.** `scene_search.py` only auto-logs a miss
when a search returns **zero** hits (`if not hits:`). A search that returns
candidates which are all bad fits — the common case, and the one GATE L actually
warns about ("a hit is a LEAD, not a verdict") — logs nothing. Created the ledger
and recorded this reel's four bad-fit punts by hand, under a section header that
leaves the tool's `AUTO_HEADER` free to append later.

## Components added

`runtime/remotion/src/UncertainEyeE01.tsx` — `UeNerveBundle`, `UeSilentWindow`,
`UeLooksNormal`, `UePatternProblem`. Registered under
`<Folder name="UncertainEyeE01">`. Index regenerated (609 to 613 renderable).
`npx tsc --noEmit` clean.

`UeSilentWindow` is built for season-wide reuse — the silent-window framework is
the reason tier-one screening exists, and E03/E04 refer back to this exact
picture.

## Number policy

Zero performance figures in this episode; none is needed. Verified by reading
every `narration_text` and every on-screen prop string. B07's caption states it
explicitly: "Conceptual. No performance claim is made in this episode."

## Fact-check

Five corrections applied and logged in `SOURCES.md`. One claim — "more than a
million" optic-nerve fibers — is standard anatomy but sits outside the series
doc's §A verified list; flagged to the author, who confirmed keeping it
(2026-09-07).
