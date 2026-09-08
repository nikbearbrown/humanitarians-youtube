# CHECKS-REPORT.md — the-number-that-wasnt-there

Written before the first slate compile, per PROOF GATE (ai-explainer
SKILL.md). This reel is **15 beats (B00-B14)**, not the ai-explainer default
of 10, and not this reel's own prior 11 — see "Beat-count deviation" below.

**Rebuild note (2026-08-29):** re-authored after the script expanded Chapter
3 into a full six-field deep-dive on all five tests (was a 3-beat/~95s
summary, now a 7-beat/~7:59 arc) and after Chapter 2's two-failed-API-keys
detour was cut. All findings below reflect the rebuilt sheet.

## Per-beat classification (SHOW / HOLD / PUNT — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_FixtureToRealGrader (Manim) | Names a comparison (fixture crossed out, real grader in) — nopunt "two things compared" row |
| B02 | SHOW | B02_InputVsInvented (Manim) | Names a worked example (Producer A's real inputs vs. its invented line) — the reel's central artifact |
| B03 | SHOW | B03_ScorecardIntro (Manim) | Names the chapter's own structure (five tests, six fields each) with a real, will-fill-in scorecard, not narrated past |
| B04 | SHOW | B04_Test1ClaimVerification (Manim) | Full six-field test card + the regex gap actually rendered, with "0.34" failing to match on screen |
| B05 | SHOW | B05_Test2Determinism (Manim) | Full six-field test card + five response bubbles, four clustering, one drifting away |
| B06 | SHOW | B06_Test3ConsistencyProbe (Manim) | Full six-field test card + a two-run divergence visual, the flag firing on screen |
| B07 | SHOW | B07_Test4GuardrailStress (Manim) | Full six-field test card + a real 24/24 structural readout |
| B08 | SHOW | B08_Test5Breadth (Manim) | Full six-field test card + twelve ticker tiles and a close-up on the one false-positive — the reel's sharpest falsifiability moment |
| B09 | SHOW | B09_ScorecardComplete (Manim) | Full scorecard, all five verdicts colored and labeled |
| B10 | SHOW | B10_ThreeFilesSynced (Manim) | Names a real fix (three files, one regex) and a real, incomplete decision (the flag rule) |
| B11 | SHOW | B11_ElevenToSeven (Manim) | Names a measured result (11→7) with a real before/after |
| B12 | SHOW | B12_TwoChipsHonestLedger (Manim) | The reel's designated falsifiability/honest-limits beat |
| B13 | SHOW | B13_CaughtByAHuman (Manim) | Callback + end-card stats; second-to-last per OUTRO-LAW |
| B14 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate, kept deliberately simple |

**15 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph or a stock stand-in. Every claim in
this script is a real mechanism, a real measured result, or a real worked
example from this project's own code and (per SOURCES.md) partially
verified against this checkout directly — all animatable diagrams, not
costumes.

**Punt costumes explicitly avoided:** no generic "AI brain" icon, no stock
handshake/checkmark photo standing in for "the system caught it," no
gen-AI clip for the debt-to-equity moment. The regex gap (B04), the
determinism cluster (B05), the divergence-flag visual (B06), and the
three-files sync (B10) are all built as real diagrams that enact the
sentence rather than illustrate it after the fact.

## Beat-count deviation (15, not 10, not the prior 11)

`agents.md`'s Quick Start default is a fixed 10-beat B00-B09 structure. This
reel's prior build authored 11 (B00-B10); this rebuild authors 15 (B00-B14)
because:

- **Chapter 3 of the rewritten script (2:06 onward) now gives each of the
  five tests a full, independent six-field treatment** (WHAT IT IS / WHY WE
  RAN IT / WHAT A GOOD RESULT LOOKS LIKE / PARAMETERS GIVEN / WHAT ACTUALLY
  HAPPENED / WHAT IT MEANS), spoken and shown as its own card, rather than
  the prior draft's ~95-second summary across three combined beats. The
  script's own PRODUCTION NOTES table lists `test-scorecard` as persistent
  through the whole chapter and `test-card-template` as reused ×5 — one
  instance per test — which forces a dedicated opening beat (blank
  scorecard), five dedicated test beats, and a dedicated closing beat
  (full scorecard) rather than compressing three or five tests into one or
  two beats. Split across B03 (intro) / B04-B08 (one per test) / B09
  (closer) — 7 beats total for what was previously 3 (B03-B05 in the prior
  build).
- **Chapter 2 (B02) got shorter, not longer** — the human cut the
  two-failed-API-keys detour from the script, so this beat's word count
  dropped from 144 to 106 words and its duration from 58s to 42s. This
  partially offsets the Chapter 3 expansion but does not come close to
  canceling it out (Chapter 3 alone grew by roughly 384s / 6:24).
- **Honest ledger (B12) and Close (B13) are kept as two separate Manim
  beats** rather than merged into one, unchanged reasoning from the prior
  build: the script gives them separate chapter framing and separate
  figures, and splitting them keeps B13 — not B12 — as the single
  "second-to-last, factual" beat the OUTRO-LAW lesson calls for, with B14
  staying a clean restate.

This matches the reel's actual content mass rather than forcing a fixed
count — `youtube/CLAUDE.md` §4's "one idea per beat" rule was prioritized
over matching any fixed beat count exactly, the same reasoning the STEM5
reel (`how-do-you-know-it-worked`, 13 beats) used for its own deviation.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01's recap states the whole comparator's
  mechanism (set arithmetic, no model, no judge) before any live-run content
  begins, so the viewer has the shape of the system before watching it
  produce a wrong answer. B03 adds a second, narrower framework moment: the
  six-field shape every one of the five tests will follow, stated once
  before any test's specifics arrive.
- [x] **WORKED EXAMPLE** — one continuous thread: Producer A's invented
  debt-to-equity line is introduced in B02, then walked through in full
  across B04 (why claim verification missed it), B05 (why determinism still
  caught the pattern of confident wrongness), B06 (why the consistency
  probe caught it cleanly), and reprised in B13 (the human catching it,
  restamped). The same fabricated number is used across five beats now, not
  four — a longer, more thorough single thread, not four disconnected
  illustrations.
- [x] **FALSIFIABILITY / edge-case beat** — B08's disjoint-concept
  counterexample (both agents correct, citing different concepts, still
  flagged) is a dedicated stress-test of the comparator's own logic, now
  given a full, uncrowded beat of its own (previously combined with the
  guardrail test in one beat). B10's explicit "does not fix" chip and B12's
  "NOT YET PROVEN" JUDGMENT half-fill are a second and third falsifiability
  moment — this script is unusually dense with them, which is a feature of
  its honesty register, not padding.
- [x] **SCAFFOLDED viewer task** — **none present, deliberately.** This is a
  weekly work-recap video, not a tutorial; the source script contains no
  "your turn" prompt, task, or rubric anywhere in its VO or production
  notes, and none was invented for this build. See "Known deviations" in
  PEDAGOGY.md.
- [x] **Bookends** — B00 (cold open), B14 (title-restate outro). This reel
  has no dedicated verdict-card or handoff bookend (no `ClaudeVerdictArtifact`,
  no "your turn" `ClaudeComposerAsk`) — the honest-ledger content that would
  normally live on a verdict card is instead a full Manim beat (B12),
  because it needs the two-chip visual metaphor, not a four-line text card.
- [x] **No source, no verdict** — every claim-bearing beat carries its own
  on-screen artifact: the crossed-fixture/real-grader panel (B01), the
  input-vs-invented split (B02), the blank scorecard naming the six fields
  (B03), each test's own six-field card plus its specific visual (B04-B08),
  the completed scorecard (B09), the three synced files plus the named
  incomplete rule (B10), the 11→7 bar (B11), the two honest-ledger chips
  (B12), and the reprised thought_log quote plus end-card stats (B13).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
SCAFFOLDED TASK — N/A, weekly-update format | BOOKENDS ✓ (2, not 4 — see
above) | NO-SOURCE-NO-VERDICT ✓**

**This is a meaningfully stronger falsifiability/worked-example showing than
the prior 11-beat build.** The prior build summarized five tests in three
beats, ~95 seconds total, with each test getting one or two sentences.
Every test now gets an explicit WHAT/WHY/GOOD-RESULT/GIVEN/HAPPENED/MEANS
treatment, spoken and shown — meaning the viewer sees not just "what
happened" per test but "what would a clean pass have looked like, and what
was actually fed in" before "what actually happened" lands, which is a much
stronger falsifiability structure than a bare "here's the result" recap.
This directly serves PROOF's "a reusable rubric a viewer could apply to a
new case" criterion (§7 of `youtube/CLAUDE.md`) — a viewer watching this
chapter now has an explicit template (six fields, five worked instances) they
could apply to evaluate any other test result, not just this project's.

## Risk flagged: five near-identical test-card beats over ~10:40+ runtime

**This is the one new risk this rebuild introduces, and it should be read
honestly rather than talked past.** B04 through B08 are five consecutive
beats that each open the same way (scorecard state, six-field card reveal,
one bespoke visual, scorecard slot resolves) for roughly 72-100 seconds
each — nearly 8 minutes of screen time following one template five times in
a row. Two mitigations are already built into `scenes.py`:

- **Each test's specific visual is genuinely different** — a regex pattern
  with a literal gap (B04), five clustering response bubbles (B05), a
  two-run divergence flag (B06), a plain numeric readout (B07), and a
  twelve-tile grid with a push-in close-up (B08) — not five copies of the
  same widget with different labels.
- **Each test's scorecard-slot verdict color is different and escalates in
  stakes** — amber, amber, green, green, red — so the running total (the
  persistent scorecard redrawn each beat) gives the viewer a visible reason
  to keep watching across the five ("which color does this one land on")
  that a flat five-in-a-row recap would not.

**But this is not a complete answer**, and it is flagged for the human,
not resolved here: five ~75-100 second beats sharing one card layout is a
real repetition-fatigue risk regardless of the visual variety underneath it,
especially given the six-field card itself (label + value rows, same
position, same font sizes) looks close to identical from beat to beat. See
PEDAGOGY.md's own flag on this for the specific question a human should
answer before signing GATE P: whether the color/visual variation is enough,
or whether the five card scenes need more structural differentiation (e.g.
varying which side of the frame the card sits on, varying the card's reveal
animation, or trimming card dwell time on the shorter/simpler tests like B07)
than what's currently authored.

## Slate rules audit (Step 4b)

`runtime/qc/sheet_check.py --strict` was run against this rebuilt reel's
`beat_sheet.json` (read-only) and reports **clean — 15 beats, no findings**.
No hard or soft findings at any point in this rebuild (unlike the prior
11-beat build, which needed one soft fix to B00's `runningText`; B00 is
unchanged in this rebuild, so that fix carries forward).

| Beat | Field | Length | Limit | OK? |
|---|---|---|---|---|
| B00 | `topic` | 20 chars ("CROSS-AGENT VALIDATION") | 125 hard | yes |
| B00 | `greeting` | "Hola, Divij" | 55 hard | yes |
| B00 | `command` | single line, well under 100 chars | wraps, not hard | yes |
| B14 | `title` | "The Number That Wasn't There" (28 chars) | wraps, not hard; ≤48 recommended for clean 2-line | yes |
| B14 | `handle` | "@DivijPawar" | ~100 hard (16:9) | yes |
| B14 | `subline` | "Proved the plumbing. Not yet the judgment." (43 chars) | ≤60 recommended | yes |

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact in `shot.manim.scene_class` or
`shot.remotion.pattern`; every Manim scene holds negative space (title/
scorecard row at top, card + visual centered, caption near the bottom) and
never drops an un-highlighted element below GHOST opacity. B08's twelve-tile
grid and its two-column close-up each hold their full state on screen before
the next transition; B12's two chips hold side by side for the full
comparison, matching the "side-by-side at the moment of comparison, held ≥2
seconds" production gate in `youtube/CLAUDE.md` §7. **Not yet verified by
actual rendered pixels** — B04-B09 are new scenes with denser layouts (a
six-row card plus a bespoke visual, sharing one frame) than any prior beat
in this reel; the mandatory §6 visual QC pass, after the first real render,
should look specifically at whether the six-field card and its adjacent
visual collide or crowd each other at 4K, since this was authored without a
render to check against.

## PPT test

No beat is a headline read over a static paragraph. B01's fixture is
visibly struck through and replaced, not narrated past. B04's regex
literally has a gap and the number literally fails to match it, on screen.
B05's five bubbles physically cluster and one physically drifts away. B06's
two runs visibly diverge and a flag physically fires between them. B07's
24/24 readout is a real count, not a claim. B08's twelve tiles physically
flip and the camera physically pushes into the one worth a second look.
B10's three files widen in the same motion at the same instant. B11's bar
physically drops from 11 to 7 while four tiles flip. B12's JUDGMENT chip
fills to exactly half, not a full or empty state, enacting "not yet proven"
rather than asserting it.

## Status

Beat sheet, `graphics_lib.py` (unchanged, copied byte-identical from
`three-files-twenty-one-tests/graphics_lib.py` in the prior build, not
touched in this rebuild per the task's explicit instruction), and `scenes.py`
are authored and internally consistent — verified by direct diff: every
`shot.manim.scene_class` in `beat_sheet.json` has exactly one matching
`class` in `scenes.py`, no extras, no gaps (`B01_FixtureToRealGrader`
through `B13_CaughtByAHuman`). `scenes.py` parses cleanly under `ast.parse`.
This pass closes the PROOF GATE for authoring.

**No audio has been generated. No Manim or Remotion render has been run.**
This build stops here, before GATE P, per the task's explicit constraint.
See `PEDAGOGY.md` for the sign-off checklist (including the runtime and
five-test-repetition flags) and `BUILD-PROMPT.md` for the commands to run
once a human flips the verdict to PASS.
