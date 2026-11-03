# PEDAGOGY.md — zero-for-sixteen (Video 4 of the Cross-Agent Validation series)

**GATE P VERDICT: PASS**
Divij Pawar 

> GATE P is a human checkpoint, not an agent one (`fellows/divij-pawar/CLAUDE.md`
> §4). Read the arc below, resolve the open checklist items at the end, then
> change `PENDING` on the line above to `PASS`, and sign it.
> `generate_audio_kokoro.py` must not run until you do — nothing in this build
> has generated audio or rendered anything.

Source script: `zero-for-sixteen.md`, in this same folder, copied verbatim
from `D:\Code\mycroft\verification-layer\divij\video-script-mycroft-6-zero-for-sixteen.md`.
This is the fourth video in the Cross-Agent Validation weekly-update
sub-series, continuing directly from `the-number-that-wasnt-there/`
(Mycroft5) — that reel's own honest ledger ended on "does the flag reliably
mean these two agents disagree? Not yet." This reel's cold open answers that
question with a measured result: zero of thirty-one stored runs.

---

## Beat breakdown — 16 beats (B00–B15), not the house default of 10

The script's own PRODUCTION NOTES section names exactly 12 figures with
timestamps. This build used that table as the authoritative content map,
plus two structural facts about the script itself:

1. **Chapter 1** (recap) carries no commissioned figure at all — the script
   explicitly says "Reuse the two-column agent diagram from the prior video.
   Fast cuts, no new build," which is followed literally in B01: a
   simplified recap panel, not an elaborate new diagram.
2. **Chapter 7** (the honest ledger) is the one section the script itself
   splits into two separate VISUAL directions — "List one, building line by
   line" and "List two, in warning color, held on screen. Do not clear it."
   — which map naturally to two beats (B12, B13) rather than one overloaded
   beat, especially since the combined word count for that chapter (300
   words) is roughly triple this reel's median beat length.

Per the house convention confirmed against the-number-that-wasnt-there
(Mycroft5): the cold open and TITLE CARD fold into B00's Remotion bookend
rather than getting a custom Manim scene, and dense factual callouts
(end-card stats) belong in the second-to-last beat (B14 here), never the
truly final Remotion outro (B15), which stays a clean title restate.

| Beat | Role | Figure(s) |
|---|---|---|
| B00 | Cold open + title (Remotion) | fig.1 `sixteen-zero` deferred to B14; f4a4c782 record deferred to B10 |
| B01 | Ch.1 recap | none commissioned — reused diagram per script's own instruction |
| B02 | Ch.2 | fig.2 `ledger-table` |
| B03 | Ch.3a | fig.3 `one-fetch-not-two` |
| B04 | Ch.3b | fig.4 `provenance-rows` |
| B05 | Ch.4a | fig.5 `snapshot-diff` |
| B06 | Ch.4b | fig.6 `dedup-collapse` |
| B07 | Ch.4c | fig.7 `layering-violations` |
| B08 | Ch.5a | fig.8 `corpus-buckets` |
| B09 | Ch.5b | fig.9 `disjoint-vocabularies` |
| B10 | Ch.6a | fig.10 `two-fixes-one-record` (+ f4a4c782 payoff) |
| B11 | Ch.6b | fig.11 `regex-truncation` + stale-ledger footnote |
| B12 | Ch.7a — "true now" | none commissioned — script's own "list one" direction |
| B13 | Ch.7b — "still not true" | fig.12 `uncommitted` + script's own "list two" direction |
| B14 | Close | fig.1 payoff (`sixteen-zero` reprise) + END CARD |
| B15 | Outro (Remotion) | — |

This matches the reel's actual content mass (`fellows/divij-pawar/CLAUDE.md`
§4's "one idea per beat" rule prioritized over hitting a fixed count), the
same reasoning the-number-that-wasnt-there used for its own 15-beat
deviation from the 10-beat default.

---

## Runtime — recomputed, then cut (2026-09-08, same day)

**Original state.** The source script's own header claims **~1,200 words of
VO at ~150 wpm for an 8:00 target**. Counting the actual VO text
word-for-word directly from the script file (1,918 words) and this build's
first-pass `narration_text` (1,939 words) both landed far above that
estimate: **12:55 (775s) projected, a +61% overrun** — larger than the
prior reel's own +17% overrun. That first-pass table is preserved in git
history / the original authoring pass; it is not reproduced here since the
sheet has since changed.

**Cut applied.** Per explicit request, the script's own "If the runtime
needs to shrink (to ~6:00)" guidance was applied, targeting ~8:00 rather
than the more aggressive ~6:00, since those three named cuts alone were
sized against the script's own (undercounted) 8:00 header estimate, not
this build's actual ~12:55 measurement. All three named items were cut in
full:

1. **Chapter 4's duplication detail** — B06 dropped the `_latest_value`
   cross-producer-import case entirely (both narration and the second
   Manim movement), keeping only the regex-duplication case. The
   byte-identical snapshot (B05) and the deliberate layering violations
   (B07) — the two things the script says to *keep* — are untouched.
2. **The `766ms`/`812ms` timings in Chapter 3** — dropped from B03's
   narration and from its on-screen content (the `timings` VGroup was
   removed from the scene entirely). The one-fetch structural claim, the
   four-band layout, and the retry path are untouched.
3. **The third, smaller stale-ledger finding at the end of Chapter 6** —
   dropped from B11's narration and its footnote card was removed from the
   scene. Still logged in SOURCES.md as a confirmed, independently-verified
   finding — cut from the video, not from the record.

Since those three cuts alone only saved ~55 seconds (they were sized for a
~2-minute cut against an 8:00 base, not a ~13:00 one), the same "keep the
throughline, cut the illustrative detail" principle was extended
proportionally to B01, B02, B03 (beyond the named cut), B05, B07, B08, B09,
B10, and B14 — trimming connective prose, restated framing, and secondary
clauses while preserving every beat's core fact, number, and quote.
**Chapter 7 (B12, B13) and the uncommitted-state content inside it were
left completely untouched — not one word cut** — per the script's explicit
"never cut chapter 7" instruction, which this build treats as a hard floor,
not a suggestion.

**Result:**

| Beat | Words (post-cut) | Est. duration | Cumulative start |
|---|---|---|---|
| B00 | 96 | 38s | 0:00 |
| B01 | 80 | 32s | 0:38 |
| B02 | 104 | 42s | 1:10 |
| B03 | 95 | 38s | 1:52 |
| B04 | 68 | 27s | 2:30 |
| B05 | 58 | 23s | 2:57 |
| B06 | 45 | 18s | 3:20 |
| B07 | 61 | 24s | 3:38 |
| B08 | 53 | 21s | 4:02 |
| B09 | 75 | 30s | 4:23 |
| B10 | 80 | 32s | 4:53 |
| B11 | 59 | 24s | 5:25 |
| B12 | 102 | 41s (unchanged) | 5:49 |
| B13 | 198 | 79s (unchanged) | 6:30 |
| B14 | 62 | 25s | 7:49 |
| B15 | 12 | 5s | 8:14 |
| **Total** | **1,248** | **8:19 (499s)** | ends 8:19 |

**~8:19 against the requested ~8:00 — a 4% difference**, achieved without
touching the one section the script itself forbids cutting. This is now a
*closer* match to the script's own original 8:00 estimate than either this
reel's own first pass (+61%) or the prior reel's rebuild (+17%) managed,
precisely because the two beats that make up 24% of the runtime (B12+B13,
120s of 499s) were deliberately exempted from the compression the rest of
the reel absorbed.

**What a human reviewer should check:** whether the post-cut narration
still reads naturally beat-to-beat (a trim pass done for time can
occasionally leave an abrupt transition) — re-read `zero-for-sixteen.md`
against `beat_sheet.json`'s `narration_text` fields side by side; whether
B03/B06/B11's now-shorter, more asymmetric scene lengths next to B12/B13's
untouched length still read as one coherent reel rather than a visibly
front-loaded-fast, back-loaded-slow pace; and whether the three specific
cut items (timings, the second duplication case, the stale-ledger
footnote) are acceptable losses — all three are still fully recorded in
SOURCES.md even though they no longer appear in the video.

---

## Teaching arc

| Beat | Role | What the viewer walks away holding |
|---|---|---|
| **B00** | Cold open | The measurement in one sentence: sixteen flags, replayed, zero real conflicts — plus the sharper hook that the one real catch this tool ever made is suppressed today. |
| **B01** | Ch.1 recap | The comparator's mechanism and the prior video's own disclosed, unmeasured limitation (7/12), plus the project's own verbatim admission that the UI never called the backend at all. |
| **B02** | Ch.2 | The self-report ledger as the UI's organizing principle — live test discovery, a generated caveat, and the `null`-vs-`false` distinction that is this whole subsystem's reason for existing. |
| **B03** | Ch.3a | The falsifiability beat: a critique was checked before being designed around, and the reality (one fetch, two lenses, sequential) was *worse* than the critique stated — plus the retry path made visible for the first time. |
| **B04** | Ch.3b | The reel's central artifact: a real, reconciled number next to the one that traces to nothing — the fabrication, shown, not narrated past. |
| **B05** | Ch.4a | Architecture-with-proof: layering with zero behavior change, verified twice (suite green at every step; byte-identical route snapshot). |
| **B06** | Ch.4b | Two duplication bugs, each with a named, specific failure mode — not a generic "clean up the code" gesture. |
| **B07** | Ch.4c | The reel's clearest falsifiability demonstration: an architecture test proven able to fail, three times, on purpose. |
| **B08** | Ch.5a | The headline measurement: 31 stored runs, labeled, replayed — not a hand-derived claim anymore. |
| **B09** | Ch.5b | The actual structural finding: disjoint vocabularies by design, meaning no amount of comparator tuning can ever produce a genuine-conflict result — this reel's sharpest falsifiability beat. |
| **B10** | Ch.6a | The reel's own honest surprise: the one confirmed true positive, replayed, doesn't fire today — two individually-reasonable fixes interacting badly, found only by building the corpus. |
| **B11** | Ch.6b | A second, independently-confirmed extraction bug, plus a small self-referential finding (a stale ledger entry) noted rather than quietly fixed. |
| **B12** | Ch.7a | "True now" — every real gain this period produced, held as a specific, checkable list. |
| **B13** | Ch.7b | "Still not true," held on screen without clearing, then the single largest fact of the period: nothing is committed. |
| **B14** | Close | The smallest true claim, restated, with the full end-card stat block — the same cold-open counter, now with its full payoff context. |
| **B15** | Outro | Title restate + sign-off. Deliberately simple. |

## Source & adaptation

This script is exceptionally well-sourced compared to prior reels in this
series — see SOURCES.md for the full verification pass. Nearly every
specific figure in the script (the 31-run corpus size, the 224 test count,
the 14 ledger entries with their exact status breakdown, the f4a4c782 and
515f263a run IDs, the §3.4 quote, the earnings producer's "deliberately
disjoint" docstring, the `test_layering.py` AST check, the `c53746a` commit
hash) was independently read directly from
`D:\Code\mycroft\verification-layer` during this build and confirmed exact,
not merely plausible. This is a meaningfully stronger verification position
than the-number-that-wasnt-there had, where most of the specific run figures
were sourced only to files absent from that build's checkout.

**One adaptation this build made beyond the script's own stage directions:**
the script's Chapter 7 VISUAL directions ("List one, building line by line"
/ "List two... do not clear it") were translated into two full Manim beats
(B12/B13) rather than one combined beat with two internal movements, because
the combined word count (300 words, ~120s) would have made a single beat
nearly 50% longer than any other beat in the reel. This is the same kind of
per-beat pacing judgment the-number-that-wasnt-there's rebuild made when it
split its own five-test chapter across seven beats instead of three.

## Factual check

See SOURCES.md for the full beat-by-beat mapping. Summary: `web/self_report.py`,
`producers/earnings.py`, `tests/test_layering.py`,
`tests/fixtures/cross_agent_real_runs_corpus.json`, `logs/RUN_LOG.md`,
`divij/cross-agent-validation-status.md`, `divij/cross-agent-validation-disjoint-concepts-diagnosis.md`,
`divij/weekly-update-2026-09-04-to-2026-09-07.md`, and the git log/status of
`D:\Code\mycroft\verification-layer` were all read directly during this
build (2026-09-08) and corroborate the script's claims exactly, including
several highly specific figures (14 ledger entries with exactly 11 OPEN + 2
UNVERIFIED + 1 RESOLVED + 2 BY_DESIGN status counts; 31-entry corpus; the
`f4a4c782` and `515f263a` run IDs named in `self_report.py` itself). One
small, honestly-reportable drift: `git status --short` in this checkout
currently shows **57** changed/new files, not the script's stated 56 — a
one-file drift consistent with ongoing uncommitted work between when the
script was drafted and when this build ran, not a contradiction. See
SOURCES.md for the full accounting.

## Register & tone

Periodic update, first-person, matching the predecessor reel's calm,
neither-apologetic-nor-triumphant register. This script is unusually
disciplined about **capability vs. observation** — same as the prior reel —
but sharpens it into a single number: not "the flag is imperfect," but "zero
genuine conflicts out of every run it has ever produced." B09's "you cannot
detect disagreement between two witnesses asked different questions" is the
reel's clearest statement of *why*, not just *that*. B13's warning-color list
held uncleared through the uncommitted-state reveal is a deliberate
register choice (per the script's own stage direction) — the two facts are
presented as one continuous admission, not two separate concerns.

**What a human reviewer should specifically check:** whether B10's
suppression-timeline visual reads as "a specific, diagnosed interaction
between two named fixes" (what the script claims) rather than "a bug that
makes the tool look bad" (an overclaim in the other direction, the same
class of error the script's own "things this script deliberately refuses to
say" list warns against for "zero for sixteen means the tool doesn't work").

## Falsifiability

B09 (disjoint vocabularies — the structural reason no tuning fixes the flag)
and B07 (three deliberately-broken layering tests, each producing a named
failure) are this reel's two sharpest falsifiability beats — both stress
real mechanisms rather than hypothetical edge cases. B10 (the suppressed
true positive) is a third, subtler one: it falsifies the previous reel's own
implicit assumption that a shipped fix is a settled fix. B03's "checked the
critique and it was worse than stated" is a fourth falsifiability moment
applied to the *process* of building the UI, not just the system under test.

## Known deviations

1. **No scaffolded viewer task / "your turn" beat.** The source script
   contains no prompt, task, or rubric for the viewer — this is a
   weekly-update recap, not a tutorial. None was invented.
2. **B15's spoken sign-off ("Signing off, Divij Pawar") is original to this
   build**, not present in the source script, matching this channel's
   established outro convention (see `the-number-that-wasnt-there/beat_sheet.json`
   B14 and `accountability-mesh/beat_sheet.json` B09).
3. **Runtime was cut from ~12:55 to ~8:19** using the script's own "cut to
   ~6:00" guidance (applied toward ~8:00 rather than ~6:00, since the
   original 12:55 was measured against the script's own undercounted 8:00
   header, not against a 6:00 one). All three named cut items were applied
   in full (B06's `_latest_value` case, B03's timing readout, B11's
   stale-ledger footnote), plus proportional trims elsewhere. **Chapter 7
   (B12, B13) was not touched at all.** See "Runtime — recomputed, then
   cut" above for the full before/after table and per-beat reasoning.
4. **16 beats, not this series' prior 15 or the house default of 10** — see
   "Beat breakdown" above for the exact mapping to the script's own 12
   figures plus its two split chapters.
5. **B01 (Chapter 1 recap) deliberately under-builds relative to every other
   beat in this reel** — a simplified two-column panel rather than a
   polished new diagram, per the script's own explicit "no new build"
   instruction. Flagged so a reviewer doesn't mistake this for an
   oversight: every other beat in the reel gets a bespoke diagram: B01 does
   not, on purpose.
6. **The one-file git-status drift** (57 now vs. 56 in the script) — see
   "Factual check" above. This build kept the script's own number (56) in
   the narration and end-card text, since it is describing a measurement
   taken at drafting time for a specific period, not a live counter: this
   is a documented, explained drift, not a silent inconsistency.

## What a human reviewer should check before signing

- [ ] **Runtime: ~8:19 projected vs. ~8:00 requested** (1,248 words at 150
  wpm, post-cut) — confirm this is an acceptable landing point, and that
  the three specific cut items (B03's timings, B06's `_latest_value` case,
  B11's stale-ledger footnote) are acceptable losses; all three remain
  fully recorded in SOURCES.md even though cut from the video. Re-check
  once Kokoro's real durations land for all 16 beats — the ~150 wpm
  assumption has run both faster and slower than measured on past reels.
- [ ] **B12/B13's split of Chapter 7 into two beats** — confirm this reads
  as one continuous "honest ledger" movement rather than two disconnected
  beats, especially since B13 is instructed to hold B12's energy without a
  hard reset (per the script's "do not clear it" direction, applied within
  B13's own held list, not literally spanning both beats' independent
  Manim renders).
- [ ] **B10's suppression framing** (see Register & tone above) — confirm
  the visual doesn't read as "the tool is broken" when the narration's own
  claim is narrower: two individually-defensible fixes interacting badly on
  one specific historical case.
- [ ] The one-file git-status drift (56 scripted vs. 57 measured at build
  time) — confirm using the script's own number is the right call, or
  whether it should be updated to the freshly-measured count instead.
- [ ] Whether B15's original sign-off line is acceptable, or should be cut
  to a silent title card.
- [ ] B01's deliberately simplified treatment (Known deviations #5) — confirm
  this reads as a considered pacing choice, not an unfinished beat, once
  seen next to B02 onward's fuller diagrams.

**Once these are resolved, replace `PENDING` at the top of this file with
`PASS`, sign, and date. Until then, `generate_audio_kokoro.py` must not run.**
