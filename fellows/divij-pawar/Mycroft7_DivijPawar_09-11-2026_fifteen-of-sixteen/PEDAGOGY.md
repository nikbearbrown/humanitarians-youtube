# PEDAGOGY.md — fifteen-of-sixteen (Video 5 of the Cross-Agent Validation series)

**GATE P VERDICT: PASS**
Divij Pawar — 2026-09-20 (signed via direct chat instruction: "sign off GATE P
and move to rendering," not a separate item-by-item walk through the checklist
below — those items remain open for reference and can still be revisited
after rendering if any of them turn out to matter once real footage exists.)

> GATE P is a human checkpoint, not an agent one (`fellows/divij-pawar/CLAUDE.md`
> §4). Read the arc below, resolve the open checklist items at the end, then
> change `PENDING` on the line above to `PASS`, and sign it.
> `generate_audio_kokoro.py` must not run until you do — nothing in this build
> has generated audio or rendered anything.

Source script: `fifteen-of-sixteen.md`, in this same folder, copied verbatim
from the drafting location. This is the fifth video in the Cross-Agent
Validation weekly-update sub-series, continuing directly from
`zero-for-sixteen/` (Mycroft6) — this script's own header explicitly assumes
that video's recap chapter is common knowledge and does not re-teach it, and
this build's Chapter 1 (B01) follows that instruction: a fast recap, not a
full re-explanation.

---

## Beat breakdown — 18 beats (B00–B17), not the house default of 10

The script's own PRODUCTION NOTES section names exactly 16 figures with
timestamps — one more than Mycroft6's 12, reflecting genuinely denser
content (two sessions covering a diagnosis, a fix, a first-ever overlap
test, and same-day production wiring, versus one diagnostic session).
Per the house convention confirmed across both prior reels in this series:
the cold open and TITLE CARD fold into B00's Remotion bookend rather than
getting a custom Manim scene, and dense factual callouts (end-card stats)
belong in the second-to-last beat (B16 here), never the truly final
Remotion outro (B17).

| Beat | Role | Figure(s) |
|---|---|---|
| B00 | Cold open + title (Remotion) | fig.1 `sixteen-to-fifteen` deferred to B16; fig.2 `fabricated-quarter` referenced here, full treatment deferred to B08 |
| B01 | Ch.1 — the two threads left open | fig.3 `open-threads` |
| B02 | Ch.2a | fig.4 `number-tagging` |
| B03 | Ch.2b | fig.5 `three-bugs` |
| B04 | Ch.2c | fig.6 `replay-through-gate` |
| B05 | Ch.2d | fig.7 `checked-twice` |
| B06 | Ch.2e (chapter closer) | fig.8 `true-positive-preserved` |
| B07 | Ch.3a | fig.9 `shared-context-fork` |
| B08 | Ch.3b | fig.10 `zero-real-numbers` (+ fig.2 payoff) |
| B09 | Ch.3c | fig.11 `sign-and-magnitude` |
| B10 | Ch.3d (chapter closer) | fig.12 `model-scoreboard` |
| B11 | Ch.4a | fig.13 `route-rewire` |
| B12 | Ch.4b | fig.14 `regex-fix` (+ the old-gate quiet-failure finding) |
| B13 | Ch.4c | fig.15 `verification-rate-zero` |
| B14 | Ch.5a — "true now" | none commissioned — script's own "list one" direction, same convention as Mycroft6's B12 |
| B15 | Ch.5b — "still not true" | fig.16 `uncommitted-growing` + script's own "list two" direction |
| B16 | Close | fig.1 payoff (`sixteen-to-fifteen` reprise) + END CARD |
| B17 | Outro (Remotion) | — |

Chapter 2 gets the most beats (5, B02–B06) because it carries the most
figures (4) plus its own closer — the diagnosis, the tagging mechanism,
three bugs, the replay measurement, the double-check, and the tally are
each a distinct, one-idea-per-beat unit, matching the same reasoning
Mycroft6 applied to its own densest chapter.

---

## Runtime — accurate this time, no cut pass needed

Unlike Mycroft6 (whose script undercounted its own runtime by 61%), this
script's header claims **~1,343 words of VO at ~150 wpm for an 8:57
target**, and its own header explains why: it was "written first, timed
after," and the estimate was corrected twice as the draft grew (once to
match Mycroft6's density, once when the chapter 2 methodology beat was
added) — the number in the header is the actual draft's count, not a
pre-set target the draft was cut to fit.

Counting the actual VO text word-for-word directly from the script file
(`grep` on every `> **VO:**` block) returns **1,343 words — an exact
match** to the header's own claim. This build's beat-by-beat
`narration_text` (1,323 words, a handful of words removed by light TTS
punctuation-normalization, not content cuts) projects to:

| Beat | Words | Est. duration | Cumulative start |
|---|---|---|---|
| B00 | 88 | 35s | 0:00 |
| B01 | 90 | 36s | 0:35 |
| B02 | 81 | 32s | 1:11 |
| B03 | 100 | 40s | 1:43 |
| B04 | 42 | 17s | 2:23 |
| B05 | 67 | 27s | 2:40 |
| B06 | 27 | 11s | 3:07 |
| B07 | 69 | 28s | 3:18 |
| B08 | 59 | 24s | 3:46 |
| B09 | 59 | 24s | 4:10 |
| B10 | 48 | 19s | 4:34 |
| B11 | 34 | 14s | 4:53 |
| B12 | 113 | 45s | 5:07 |
| B13 | 77 | 31s | 5:52 |
| B14 | 111 | 44s | 6:23 |
| B15 | 143 | 57s | 7:07 |
| B16 | 103 | 41s | 8:04 |
| B17 | 12 | 5s | 8:45 |
| **Total** | **1,323** | **8:50 (530s)** | ends 8:50 |

**8:50 against the script's own 8:57 target — a 1.3% difference.** No
runtime-cut pass was applied or needed. **What a human reviewer should
check:** this is only a pre-audio estimate; re-check once Kokoro's real
durations land for all 18 beats (per this series' own history, actual
Kokoro output has run both faster and slower than the 150 wpm planning
assumption on past reels — Mycroft6's came in 35% faster than estimated).

---

## Teaching arc

| Beat | Role | What the viewer walks away holding |
|---|---|---|
| **B00** | Cold open | The headline number (15 of 16, gone) immediately followed by the sharper finding the fix-verification test surfaced: a model that doesn't read its own input. |
| **B01** | Ch.1 recap | The two-way diagnosis from last video (link concepts / test overlap) and the order both were tackled in — fast, per the script's own "assume the recap is known" instruction. |
| **B02** | Ch.2a | The core mechanism: tag every number with its concept, exclude tagged numbers from comparison entirely. |
| **B03** | Ch.2b | Three real bugs caught before the measurement was trusted — each a specific, teachable failure mode, not a vague "some issues came up." |
| **B04** | Ch.2c | The measurement method itself: replaying the *same* 16 real runs, not new synthetic examples — this is the "how do we know it's real" beat the script's own production notes call out as unskippable. |
| **B05** | Ch.2d | The double-check: module-level and production-function-level, both landing on 15/16 — confirms the wiring didn't change the answer. |
| **B06** | Ch.2e | The tally, with the one survivor explicitly labeled as the thing that matters most, not a rounding error. |
| **B07** | Ch.3a | The test nothing in 31 runs had performed: identical evidence to both agents, with a role-swap control. |
| **B08** | Ch.3b | The flag fires for the first time on shared evidence — immediately followed by the "but" that it's not for the reason it was built to catch. |
| **B09** | Ch.3c | A concrete, specific failure: real income turned into a loss, wrong sign, wrong by 1000x. |
| **B10** | Ch.3d | The chapter's own verdict: the mechanism works, on a problem it wasn't built to find. |
| **B11** | Ch.4a | The same-day ship decision, stated plainly as a decision, not an inevitability. |
| **B12** | Ch.4b | Two fixes that came free from the same wiring change, each named with its own specific mechanism. |
| **B13** | Ch.4c | Claim verification's first real connection to this route, replayed against the actual historic fabrication — a real signal, explicitly not "this number is fake" but "this source doesn't back the claim." |
| **B14** | Ch.5a | Every real gain this period produced, held as a specific, checkable list. |
| **B15** | Ch.5b | "Still not true," held on screen without clearing, ending on the growing uncommitted pile. |
| **B16** | Close | The smallest true claim, restated, with the full end-card stat block. |
| **B17** | Outro | Title restate + sign-off. Deliberately simple. |

## Source & adaptation

This script is exceptionally well-sourced — every specific figure was
independently read directly from `D:\Code\mycroft\verification-layer`
during this build and confirmed exact: the 242-test count, the 15-issue
ledger with its exact status breakdown (9 open/unverified, 1 critical, 4
resolved this arc), the three `concept_linkage.py` bugs, the
`mistral-7b-context-grounding-failure` ledger entry, the `numeric.py`
comma-regex fix comment, and both 2026-09-11 `RUN_LOG.md` entries. See
SOURCES.md for the full pass.

**One register fix this build made, not a content cut:** the script's cold
open ends on two consecutive "That's not X. That's Y." sentences back to
back ("That's not a comparator bug. That's a model that doesn't do the
reading."). B00's narration merges these into one sentence ("This is a
model that doesn't do the reading, not a comparator bug") to avoid the
repeated construction reading as a stock rhetorical tic, without dropping
or softening the claim. No other narration in this build was reworded
beyond light TTS-normalization (numbers spelled out, em dashes to commas)
— the script's other uses of contrastive "not X, Y" framing (e.g. B13's
"not 'this number is fake' — but 'this source doesn't back what's
claimed'") were left exactly as written, since those are precise technical
distinctions the whole video's honesty register depends on, not a
repeated stylistic tic.

## Factual check

See SOURCES.md for the full beat-by-beat mapping. Summary: `web/self_report.py`,
`validation/concept_linkage.py`, `core/numeric.py`, `tests/test_concept_linkage.py`,
`tests/test_real_run_corpus.py`, `tests/test_compare_route.py`,
`tests/fixtures/cross_agent_real_runs_corpus.json`, `logs/RUN_LOG.md`, and
the git log/status of `D:\Code\mycroft\verification-layer` were all read
directly during this build (2026-09-20) and corroborate the script's claims
exactly. One honestly-reportable drift: `git status --short` in this
checkout currently shows **62** changed/new files, not the arithmetic the
script implies (56 from Mycroft6 + 11 this period = 67) — a drift
consistent with ongoing work between drafting and this build, not a
contradiction; see SOURCES.md for the full accounting. This build kept the
script's own "+11 more files" framing in the narration and end card, since
it describes a measurement taken for a specific period, matching the same
judgment call made for Mycroft6's own file-count drift.

## Register & tone

Periodic update, first-person, matching the series' calm,
neither-apologetic-nor-triumphant register. This script sharpens the
series' running capability-vs-observation discipline into a new
distinction: a *fix that reduces false alarms* and a *fix that catches
fabrication* are named explicitly as two different problems solved for two
different reasons, and the script's own "things this script deliberately
refuses to say" list calls out conflating them as "exactly the overclaim
this format exists to catch." B10's and B16's narration both carry this
distinction explicitly, and the beat visuals (B10's split scoreboard, B16's
two-line close) were built to keep it visually explicit too.

**What a human reviewer should specifically check:** whether B08's "4 for
4, flagged" visual reads as unambiguous vindication before the "but" lands
(the script is careful to sequence "flagged" then "not for the reason it
was built to catch" — confirm the beat's pacing doesn't let the first half
land as a standalone triumphant beat).

## Falsifiability

B08/B09 (the overlap test finds a real problem, but the wrong one) and
B12's explicit "does not fix" framing carried over from the series'
established discipline are this reel's sharpest falsifiability beats. B15's
"narrowing the gap from any disconnected number to any unlabeled one is
not closing it" is a third, more subtle one — it explicitly rejects reading
progress on one axis (false-positive rate) as progress on a different axis
(fabrication detection).

## Known deviations

1. **No scaffolded viewer task / "your turn" beat.** Same as both prior
   reels in this series — this is a weekly-update recap, not a tutorial.
2. **B17's spoken sign-off ("Signing off, Divij Pawar") is original to this
   build**, not present in the source script, matching this channel's
   established outro convention.
3. **18 beats, not the house default of 10 or the series' prior 16** — see
   "Beat breakdown" above for the exact mapping to the script's own 16
   figures.
4. **B00's cold-open rephrase** (see "Source & adaptation" above) — the
   only narration line in this build that isn't close to verbatim from the
   script.
5. **The file-count drift** (62 measured now vs. the ~67 the script's own
   arithmetic implies) — see "Factual check" above. This build kept the
   script's own "+11 more files" framing, consistent with how Mycroft6's
   own git-status drift was handled.

## What a human reviewer should check before signing

- [ ] **B00's cold-open rephrase** — confirm merging the script's two
  consecutive "That's not X. That's Y." sentences into one line preserves
  the intended emphasis and doesn't read as softened.
- [ ] **B08's sequencing** (see Register & tone above) — confirm "4 for 4,
  flagged" doesn't land as a standalone triumphant beat before the "but."
- [ ] The file-count drift (62 measured vs. ~67 implied) — confirm using
  the script's own "+11 files" framing is the right call.
- [ ] Whether B17's original sign-off line is acceptable, or should be cut
  to a silent title card.
- [ ] Runtime: re-check the ~8:50 estimate once Kokoro's real durations
  land for all 18 beats.

**Once these are resolved, replace `PENDING` at the top of this file with
`PASS`, sign, and date. Until then, `generate_audio_kokoro.py` must not
run.**
