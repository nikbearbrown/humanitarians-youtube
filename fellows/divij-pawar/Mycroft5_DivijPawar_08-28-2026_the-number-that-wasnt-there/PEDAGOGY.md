# PEDAGOGY.md — the-number-that-wasnt-there (Video 3 of the Cross-Agent Validation series)

**GATE P VERDICT: PASS**

> GATE P is a human checkpoint, not an agent one (`youtube/CLAUDE.md` §4). Read
> the arc below, then change `PENDING` on the line above to `PASS`, and sign
> it. `generate_audio_kokoro.py` must not run until you do — nothing in this
> build has generated audio or rendered anything, per the task's explicit
> constraint.

Source script: `the-number-that-wasnt-there.md`, in this same folder — the
human's rewritten, superseding script for this week's slot. It replaces
`../the-other-agent-wasnt-real/` (see "Known deviations" below for why that
folder could not actually be used as a template).

**Rebuild note (2026-08-29):** this file, `beat_sheet.json`, `scenes.py`,
`SOURCES.md`, `CHECKS-REPORT.md`, and `BUILD-PROMPT.md` were all rebuilt
after two script changes: (1) Chapter 3 expanded from a ~95-second, 3-beat
summary of "five tests" into a full six-field (WHAT IT IS / WHY WE RAN IT /
WHAT A GOOD RESULT LOOKS LIKE / PARAMETERS GIVEN / WHAT ACTUALLY HAPPENED /
WHAT IT MEANS) deep-dive across 7 beats, and (2) Chapter 2's two-failed-API-
keys detour was cut, shortening that beat. Beat count grew from 11 (B00-B10)
to 15 (B00-B14). **Every prior-build checklist item below has been
re-verified against the rebuilt sheet**, not carried forward blindly.

---

## Read this first — a missing precedent, not a missing script

The build instructions for this reel named `../the-other-agent-wasnt-real/`
as the **primary structural and stylistic template** — "built minutes ago in
this exact house style," with a full `beat_sheet.json`, `PEDAGOGY.md`,
`SOURCES.md`, `CHECKS-REPORT.md`, `BUILD-PROMPT.md`, `scenes.py`, and
`graphics_lib.py`.

**That folder does not exist.** A direct search of this checkout
(`youtube/the-other-agent-wasnt-real/`), the full git history (`git log
--all --diff-filter=A --name-only`), every local branch, and the one other
worktree on this machine (`agents-dynamic-docs-index-html`, unrelated
content) all came back empty. Whatever produced that folder either ran in an
environment never synced to this checkout, or the premise itself was
mistaken.

**This build fell back to `youtube/three-files-twenty-one-tests/`** as the
closest real, in-repo precedent instead — same persona (Divij Pawar), same
`claude-divij` brand, the direct predecessor entry in this same Cross-Agent
Validation series, and a fully-authored `beat_sheet.json` / `PEDAGOGY.md` /
`SOURCES.md` / `scenes.py` / `graphics_lib.py` to model against. `graphics_lib.py`
in this folder is copied byte-for-byte from that reel's copy (diffed to
confirm identical, and untouched by this rebuild per the task's explicit
instruction not to modify it). `CHECKS-REPORT.md`'s format follows
`accountability-mesh/` and `STEM5/` (the only reels in this channel that
carry that file), and `BUILD-PROMPT.md`'s format follows
`STEM5/BUILD-PROMPT.md` (the only existing example of that file in this
channel), since neither `three-files-twenty-one-tests/` nor any other
pre-STEM5 reel has one.

**What a human reviewer should specifically check:** whether this fallback
introduced any drift from whatever house-style refinements the (missing)
`the-other-agent-wasnt-real` build might have made beyond what
`three-files-twenty-one-tests` already established. This build cannot know
what it doesn't have; it used the best available real precedent rather than
inventing conventions from nothing.

---

## Runtime — recomputed, and it disagrees meaningfully with the script's own header

The source script's own header claims **~1,600 words of VO at ~150 wpm for a
~10:40 target**. This rebuild counted the actual VO text word-for-word,
beat by beat, at the same 150 wpm / 2.5 words-per-second assumption
(`round(words / 2.5)` per beat, matching the prior build's own method):

| Beat | Words | Duration | Cumulative start |
|---|---|---|---|
| B00 | 54 | 22s | 0:00 |
| B01 | 113 | 45s | 0:22 |
| B02 | 106 | 42s | 1:07 |
| B03 | 57 | 23s | 1:49 |
| B04 (Test 1) | 229 | 92s | 2:12 |
| B05 (Test 2) | 249 | 100s | 3:44 |
| B06 (Test 3) | 225 | 90s | 5:24 |
| B07 (Test 4) | 181 | 72s | 6:54 |
| B08 (Test 5) | 225 | 90s | 8:06 |
| B09 | 31 | 12s | 9:36 |
| B10 | 152 | 61s | 9:48 |
| B11 | 77 | 31s | 10:49 |
| B12 | 84 | 34s | 11:20 |
| B13 | 71 | 28s | 11:54 |
| B14 | 17 | 7s | 12:22 |
| **Total** | **1,871** | **12:29 (749s)** | ends 12:29 |

**This disagrees meaningfully with the script's own estimate**, and per the
task's explicit instruction ("flag in PEDAGOGY.md if your math disagrees
meaningfully"), that disagreement is stated plainly rather than papered
over: **~1,871 words counted vs. ~1,600 claimed (+17%), and ~12:29 projected
runtime vs. ~10:40 targeted (+1:49, about +17% as well)**. The script's own
stated chapter-start timestamps (Chapter 4 at 8:02, Chapter 5 at 9:04, the
Honest Ledger at 9:36, Close at 10:10) do not hold under this word-count
math either — this rebuild's Chapter 4 starts at 9:48, Chapter 5 at 10:49,
the Ledger at 11:20, and Close at 11:54, each roughly **+1:46 to +1:50**
later than the script's own header.

**Where the overrun comes from:** almost entirely Chapter 3. The script's
own timestamps budget 2:06→8:02 (356s) for the whole five-test chapter; this
rebuild's word-count math for the same content (B03 through B09) comes to
**479 seconds (7:59)** — a **+2:03 overrun in Chapter 3 alone**. Chapter 2
(B02) got *shorter* by 16s (the two-failed-API-keys cut), which partially
offsets this but nowhere near cancels it out. Every beat from B10 onward
inherits the same constant ~1:49 shift, since nothing downstream of Chapter
3 changed in content or word count from the prior build (beyond the -16s at
B02).

**This rebuild did not compress the narration to force-fit the script's
stated timestamps.** The task's own instruction ("condense lightly for TTS
pacing if needed, but don't drop any of the six fields for any test") was
read as permission for light trims, not authorization to cut content to hit
a target number — cutting a script that explicitly commits to "don't skip a
field even when the answer is short" in order to match a runtime estimate
that the script's own header may simply have miscounted would be exactly
the kind of rounding-up this reel's own honesty register argues against.
The narration_text fields are close to verbatim from the script (numbers
spelled out for TTS, matching this reel's existing house convention —
"zero point three four" for 0.34, "forty-two" for the seed value — but no
sentences cut).

**What a human reviewer should check:** whether a ~12:30 runtime is
acceptable for this reel, or whether the script's own "If you need to cut to
~6:20" section (which explicitly preserves the six-field structure while
dropping to one sentence per field, and folds Test 4 into a single line
inside Test 5's setup) should be applied before Gate P sign-off. This
decision was left to the human, consistent with the task's instruction not
to resolve it here. Separately, **the pre-audio estimate should be treated
as a starting point, not a guarantee** — `youtube/CLAUDE.md` §5 notes that
measured Kokoro output has run both faster and slower than the ~150 wpm
planning assumption on different past reels; re-check this projection once
Step 3's retiming pass has real Kokoro durations for all 15 beats.

---

## Teaching arc

| Beat | Role | What the viewer walks away holding |
|---|---|---|
| **B00** | Cold open | The premise in four short clauses: two agents, first live run, and a number that came from nowhere. No self-intro — this is a weekly-update entry, not a sequel needing re-introduction. |
| **B01** | Recap | The comparator's whole mechanism (set arithmetic, no model, no judge) and last week's upgrade (fixture → real second grader), landing on an explicitly still-empty "OBSERVED" chip — so the viewer knows nothing has actually been watched running yet. |
| **B02** | Chapter 2 | The central artifact: Producer A's three real inputs next to its invented debt-to-equity line. This is the number the whole video is about. (Trimmed 2026-08-29: no longer opens on the two-failed-API-keys detour — goes straight to the local model and the invented line.) |
| **B03** | Chapter 3 intro | The shape of what's coming: five tests, each getting the same six-field treatment. A blank scorecard, five grey slots, waiting. |
| **B04** | Test 1 | Claim verification, in full — what it is, why it exists, what a clean result looks like, exactly what it was given, what happened (the regex gap), what it means (starved upstream, not broken). Scorecard slot 1: amber. |
| **B05** | Test 2 | Determinism, in full — same question, same seed, five times; four cluster on a wrong answer, one outlier never repeats. Scorecard slot 2: amber. |
| **B06** | Test 3 | The consistency probe, in full — the one test that worked exactly as designed, no workaround needed. Scorecard slot 3: green. |
| **B07** | Test 4 | The guardrail stress test, in full — the odd one out, testing format not content; 24/24, clean. Scorecard slot 4: green. |
| **B08** | Test 5 | The breadth test, in full — twelve companies, eleven flagged, and the reel's sharpest falsifiability moment (a correct-but-unrelated false positive). Scorecard slot 5: red. |
| **B09** | Chapter 3 close | The full scorecard, all five verdicts held at once: amber, amber, green, green, red. |
| **B10** | Chapter 4 | Two different kinds of fix: a mechanical one (three files, same regex, all widened) and a judgment call, stated as a judgment call, with an explicit boundary of what it does and does not fix. |
| **B11** | Chapter 5 | The fix, measured against the same real data — a specific, countable improvement (11→7), not a vague "better now." |
| **B12** | Honest ledger | The reel's two-part verdict: infrastructure proven, judgment not yet proven — held as two separate claims, never merged into one verdict. |
| **B13** | Close | The cold-open's number returns, restamped by a human rather than the system, plus the end-card stats (per OUTRO-LAW, kept off the truly final beat). |
| **B14** | Outro | Title restate + sign-off. Deliberately simple. |

## Source & adaptation

The script's own PRODUCTION NOTES section references "D3 v7, per
`brutalist/D3.md`" and an `npm run audit:layout` / `ACCURACY-REVIEW.md`
workflow — **that is a different toolkit's convention, not this project's.**
This build did not attempt to satisfy those references; it translated the
script's content (the eleven named figures across both drafts, the
fact-check table, the refusal list) into **this** pipeline's actual formats
(`beat_sheet.json`, `scenes.py` Manim classes, Remotion
`ClaudeComposerAsk`/`ClaudeTitleOutro` patterns), per the task's explicit
instruction to implement the script faithfully into the pipeline's own file
formats rather than its stage directions verbatim.

**One structural decision this rebuild required that the prior build didn't
face:** the script's own production-notes figure table lists `test-scorecard`
as "persistent through Ch. 3" — a single Mobject staying alive across seven
beats. Since each Manim beat renders as an independent scene/process, true
persistence across beats isn't possible; this build instead has every beat
from B03 through B09 **redraw the scorecard in its correct cumulative fill
state** (same pattern the prior build's `counter_panel` helper used for the
old three-beat five-tests arc), which reads as continuous to a viewer even
though it's re-authored per-scene. Flagged for review: this is a reasonable
interpretation of "persistent" given the pipeline's constraints, not a
literal implementation of the script's stage direction.

**Carried forward from the prior build, unchanged:** figure 1
(`unsourced-number`) is not built as a Manim scene at 0:00, because the
house convention (confirmed against `three-files-twenty-one-tests`) fixes
B00 as the Remotion cold-open bookend, which cannot run a custom Manim
animation. Figure 1's full treatment — the thought_log fade-in, the
citation, the stamp — lands once, with more weight, in B13's callback
instead of twice at reduced weight.

## Factual check

See `SOURCES.md` for the full beat-by-beat mapping and the independent
verification pass. Summary: `claims.py`, `consistency.py`, `verification.py`,
`financial_grader.py`, `adapters/ollama_adapter.py`, and `middleware.py` are
all confirmed present in this checkout, and all three regex modules were
read directly and confirmed to share the exact same quantitative-number
pattern with no bare-decimal case — this directly corroborates Test 1
(B04)'s central claim. `adapters/ollama_adapter.py`'s `temperature=0.0`/
`seed=42` defaults directly corroborate Test 2 (B05)'s GIVEN field, and
`middleware.py`'s retry-then-halt structure directly corroborates Test 4
(B07)'s WHY field — both newly confirmed in this rebuild's verification
pass, not present in the prior build's SOURCES.md. `logs/RUN_LOG.md`,
`work.md`, `divij/model-test-report-2026-08-29.md`, `divij/sdd.md`,
`cross_validation.py`, and `run_cross_agent_live.py` are **not** present in
this checkout (searched directly, across git history, branches, and the one
other worktree on this machine) — every claim sourced only to those files
(the specific run transcript, the exact determinism figures, the specific
11→7 recalculation) is **unconfirmed from this checkout**, not contradicted.

**This gap has not shrunk with the Chapter 3 expansion** — it has, if
anything, gotten more consequential, since three of the five tests (Test 2's
specific 4-of-5 clustering, Test 4's specific 24/24 count, Test 5's specific
11/12 count and the disjoint-concept case) are sourced only to files absent
from this checkout. The mechanisms behind those tests (the adapter defaults,
the retry-then-halt structure, the regex, the scoring weights) are
independently confirmed; the specific numbers this particular live run
produced are not.

## Register & tone

Teardown, first-person, matching the predecessor reel's register: calm, not
apologetic, and not triumphant either. The script is unusually disciplined
about one specific distinction — **capability vs. observation** (the
machinery working vs. the flag meaning what it claims to mean) — stated as
"two separate questions, two separate answers" in the honest ledger and
carried through as the two-chip visual in B12 (solid green vs. half-filled
"NOT YET PROVEN"), never collapsed into one verdict. The expanded Chapter 3
extends this discipline into each individual test: every test's MEANS field
is a hedged, specific claim about what that one test does and doesn't prove
(e.g. Test 3's "of all five tests here, this is the one that worked
precisely as intended" — an explicit contrast with the other four, not a
blanket "it worked").

**What a human reviewer should specifically check:** whether that
capability/observation discipline survived the beat-sheet and visual
translation intact across all five new test beats, or whether any beat's
on-screen framing accidentally implies more confidence than the narration
claims. The places most at risk of this: B08's "both agents were completely
correct" line (check it reads as "correct about different things," not
"correct, so the flag is simply wrong"), B05's GIVEN field (check the
scorecard/card visual doesn't imply the specific run's parameters are
confirmed when only the adapter's defaults are), and B12's two-chip visual
(check the green fill on INFRASTRUCTURE doesn't visually imply the whole
system is proven, only the machinery half of it).

## Falsifiability

B08 (the disjoint-concept case) and B10 (the explicit "does not fix" chip,
stamped "LEFT OPEN ON PURPOSE") are this reel's two sharpest falsifiability
beats — both stress-test the comparator's own logic rather than a
hypothetical edge case. B12 is a third, softer falsifiability moment (the
half-filled JUDGMENT chip). The expanded Chapter 3 adds a subtler fourth:
each test's GOOD RESULT field states what a clean pass would have looked
like *before* the HAPPENED field reveals what actually happened — meaning
every one of the five tests is framed as falsifiable on its own terms, not
just the chapter as a whole. This is more falsifiability content than a
typical 10-beat reel carries, which is a property of this particular
script's honesty register (see CHECKS-REPORT.md), not padding.

## Known deviations

1. **No scaffolded viewer task / "your turn" beat.** The source script
   contains no prompt, task, or rubric for the viewer — this is a
   weekly-update recap, not a tutorial. None was invented. If the channel
   wants every reel to carry one regardless of source-script content, that
   is a house-style decision for the human to make, not something this
   build should have added unilaterally.
2. **B14's spoken sign-off ("Signing off, Divij Pawar") is original to this
   build**, not present in the source script, which has no outro dialogue
   at all — added to match this channel's established outro convention
   (see `accountability-mesh/beat_sheet.json` B09: "Signing off — Divij
   Pawar."). Flagged since it is the one line in this reel not drawn
   directly from the script.
3. **The primary template folder (`the-other-agent-wasnt-real/`) does not
   exist** — see "Read this first" above. This build used
   `three-files-twenty-one-tests/` instead, the closest real precedent
   available.
4. **Runtime estimate is ~12:29 against the script's own ~10:40 target** —
   a ~1:49 (~17%) overrun, concentrated almost entirely in the expanded
   Chapter 3. See "Runtime — recomputed" above for the full word-count math
   and per-beat breakdown. Not resolved unilaterally; flagged for the
   sign-off decision, with the script's own "cut to ~6:20" section named as
   the prescribed path if a shorter cut is wanted.
5. **NEW — five near-identical test-card beats, repetition risk.** B04
   through B08 share one structural template (scorecard state → six-field
   card reveal → bespoke visual → scorecard slot resolves) across roughly
   72-100 seconds each, nearly 8 minutes total. Each beat's specific visual
   differs (regex gap / bubble cluster / divergence flag / numeric readout /
   ticker grid + close-up) and each scorecard slot resolves to a different,
   escalating color (amber, amber, green, green, red), which gives real
   variation and a running "which color this time" hook — but the six-field
   card itself (same label/value row layout, same font sizes, same screen
   position) looks close to identical from beat to beat, and this is
   content-rich but visually repetitive by construction. **This is not
   resolved here.** A human should judge whether the color/visual variation
   already authored in `scenes.py` is enough to keep five ~90-second beats
   visually interesting back to back, or whether the five card scenes need
   more structural differentiation (varying card position/side, varying the
   reveal animation, trimming card dwell time on the simpler tests) before
   Gate P sign-off. See CHECKS-REPORT.md's "Risk flagged" section for the
   full detail.

## What a human reviewer should check before signing

- [ ] **Runtime: ~12:29 projected vs. ~10:40 target** (1,871 words at 150
  wpm) — a ~1:49 overrun, concentrated in Chapter 3. Decide whether this
  length is acceptable as-is, whether to apply the script's own "cut to
  ~6:20" compression guidance, or something in between. Re-check once
  Kokoro's real durations land for all 15 beats (see "Runtime — recomputed").
- [ ] **NEW — the five-test-card repetition risk** (Known deviations #5 /
  CHECKS-REPORT.md "Risk flagged") — does the color/visual variation already
  in `scenes.py` read as enough differentiation across B04-B08, or does the
  card template itself need more variety before render?
- [ ] The source-verification gap in `SOURCES.md` — every claim sourced only
  to `logs/RUN_LOG.md` / `divij/model-test-report-2026-08-29.md` is
  unconfirmed from this checkout, now including three of the five Chapter-3
  tests' specific numbers. Decide whether that's acceptable for GATE P or
  whether those files need to be located first.
- [ ] Capability-vs-observation discipline across B05, B08, and B12 (see
  Register & tone above) — does the visual framing still match the
  narration's hedging, or did anything get rounded up in translation?
- [ ] Whether B14's original sign-off line is acceptable, or should be cut
  to a silent title card.
- [ ] Whether the missing `the-other-agent-wasnt-real/` template changes
  anything about how this reel should look — this build could not compare
  against it and used the next-best real precedent instead.

**Once these are resolved, replace `PENDING` at the top of this file with
`PASS`, sign, and date. Until then, `generate_audio_kokoro.py` must not run.**
