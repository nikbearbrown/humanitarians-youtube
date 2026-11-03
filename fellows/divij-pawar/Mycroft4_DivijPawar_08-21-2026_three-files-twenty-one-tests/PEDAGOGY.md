# PEDAGOGY.md — three-files-twenty-one-tests (Video 2 of 2)

**GATE P VERDICT: PASS** — awaiting human sign-off.

> GATE P is a human checkpoint, not an agent one (CLAUDE.md rule 3). Read the arc
> below, then change `HOLD` on the line above to the word the gate looks for.
> `generate_audio_kokoro.py` refuses to run until you do.

Source script: `D:/Code/mycroft/verification-layer/divij/video-script-cross-agent-validation-20min.md`,
PART TWO (chapters 7–13 + close). Part One is a separate reel:
`../when-two-agents-disagree/`.

---

## Compression note (read this first)

The source script's PART TWO is **2,585 words of VO** (~12:05 at Kokoro's measured
214 wpm). This sheet is **902 words** (~4:12). That is a **2.9 : 1 compression**.
What was cut, and why:

| Cut from the script | Why it's safe to lose |
|---|---|
| The fixture adapter's construction-time validation (rejecting empty conclusions and XML block tags) | A good detail, but it teaches nothing the reel doesn't already teach through the halt handler. Cut cleanly rather than compressed into a clause. |
| The two split-out payload functions ("integration code that only exists in a design document…") | The *inherited properties* point in B06 is the stronger version of the same idea. |
| The tiered-disclosure / scope-mechanism detail | Survives as one chip in B06's inherited-properties row, unspoken. |
| The consistency probe's throwaway-UUID contrast (probe run not persisted vs. shared run ID) | B06 keeps the conclusion ("the comparison is the evidence") without the comparison to the probe's behaviour. |
| The temp-database test detail ("the real database was never written to") | Same theme as the mutation testing, weaker instance. Cut so the mutation table lands alone. |
| Known gaps #1 (only HaltError caught per agent) and #5 (four open security findings) as spoken items | #5 is spoken in **B04** where it justifies the no-new-route cut. #1 is genuinely dropped — see risk note below. |
| The close's fluency argument ("fluency is the first sign of trouble") | Folded into B09's outro. The line is good; there is no beat left to carry it at length. |

**The claim to check when you sign:** the honest list in B07 is now four items,
not six. **Known gap #1 — only `HaltError` is caught per agent, so any other
exception aborts the whole comparison and discards the other agent's records —
is not stated anywhere in this reel.** That is the single most defensible
omission to challenge. If you want it in, B07's `artifactLines` has room for a
fifth line, or B06's beat can absorb one sentence. My call was to cut it because
B05 already spends its most careful moment on exception handling, and adding a
"but only one exception type" caveat there undercuts that beat's point. Your
call, though — it is a real gap, and the reel's whole register is about not
hiding real gaps.

---

## Teaching arc

| Beat | Role | What the viewer walks away holding |
|---|---|---|
| **B00** | Cold open — welcome + self-intro | Who is talking, that this is part 2, and a one-clause recap of part 1. **tips.txt §2: a sequel still gets the welcome screen and a spoken self-intro.** The "last time" callback is inside this beat, never a replacement for it. |
| **B01** | Executive summary (BLUF) | The whole build in one breath: a layer that recorded everything but proved nothing, an empty slot on the architecture diagram, and the smallest honest thing that fills it. |
| **B02** | What already existed | The four components, so that B05 and B06 can say "unchanged" and mean something. Without this beat, "how little had to be written" is not a claim the viewer can evaluate. |
| **B03** | The orphan | Why this component and not another. The counters do the arguing: 21,824 bytes of spec, 16 scripts, 0 shared logic. |
| **B04** | The cuts are the design | The reasoning behind each scope cut — especially why a hand-written fixture is a discipline, not a shortcut. |
| **B05** | The code | The payoff: the whole comparison is a symmetric difference. Set arithmetic, no model. This is the beat the reel exists for. |
| **B06** | How it fits, and proving the tests can fail | Two halves: the integration inherits immutability for free, and a green test suite proves nothing until you've seen it go red. |
| **B07** | Verdict — the honest list | Four limitations, stated plainly. The verdict card is deliberately not a victory lap. |
| **B08** | Your turn — handoff | Extends the `false`-vs-`null` distinction into the viewer's own code. Prompt read aloud verbatim and discussed. |
| **B09** | Outro | Title restate + the series' closing line. |

## Comprehension anchors

| Beat | Anchor | Phrase | Why it lands |
|---|---|---|---|
| B01 | Image | "perfect record, unknown truth" | The whole problem in three words |
| B02 | Consequence | "a failed attempt is evidence too" | Reframes an error path as a feature |
| B02 | Concrete | `RAISE(ABORT)` on any update | Not "append-only by convention" — the database refuses |
| B03 | Counters | 21,824 / 16 / 0 | The last number is the punchline; hold it alone |
| B04 | Reversal | "that sounds like cheating. It isn't." | Names the viewer's objection before they raise it |
| B04 | Logic | Two hypotheses you can't separate | Makes the fixture *necessary*, not convenient |
| B05 | Payoff | "no model, no judge — set arithmetic" | The reveal the whole reel builds to |
| B05 | Elegance | "silence about a figure is a disagreement about that figure" | One line, two cases, no special case |
| B06 | Discipline | "I broke it on purpose" | Turns 129/129 from a boast into a question |
| B06 | Distinction | `false` vs `null` | The sharpest idea in the reel; gets the last beat of B06 |
| B09 | Closer | "the judgment stays with the human" | Answers Video 1's outro subline |

## Register and tone

Teardown, first-person build log. Calm, not triumphant — the reel's subject is a
component that deliberately does very little, and the narration has to sound like
someone who thinks that was the right call rather than someone apologising for it.
Two holds:

- **B07 is not a disclaimer beat.** Read it at the same pace and confidence as
  B05. "Producer B is still a fixture" is a design fact, not a confession.
- **No beat claims the system works.** It claims a component now runs, and that
  a comparison is recorded. Those are the true, smaller claims.

## Series continuity

- B00 opens on the welcome screen with a full self-intro, then recaps Video 1 in
  one clause. **This is the specific bug that hit the last reel** (tips.txt §2) —
  do not let the recap eat the cold open.
- B00's recap restates Video 1's B06 conclusion (surface, don't resolve), which is
  the premise B04's third cut depends on.
- B05's `information asymmetry, encoded in a function signature` is a direct
  callback to Video 1's B04 trap one. It only lands if Video 1 exists — that's
  fine, it's a bonus for series viewers, not load-bearing here.
- B09's subline answers Video 1's B09 subline. Design the two outro cards as a pair.

## Scene placeholder check

| Beat | Class / pattern | Status |
|---|---|---|
| B00 | `ClaudeComposerAsk` (Remotion) | props authored, within slate limits |
| B01 | `B01_PerfectRecordUnknownTruth` | needs writing |
| B02 | `B02_WhatAlreadyExisted` | needs writing |
| B03 | `B03_TheOrphan` | needs writing |
| B04 | `B04_CutsAreTheDesign` | needs writing |
| B05 | `B05_SymmetricDifference` | needs writing — the visual spine, budget the most time here |
| B06 | `B06_RunIdAndMutation` | needs writing — two halves, hard cut between them |
| B07 | `ClaudeVerdictArtifact` (Remotion) | props authored, within slate limits |
| B08 | `ClaudeComposerAsk` (Remotion) | props authored, within slate limits |
| B09 | `ClaudeTitleOutro` (Remotion) | props authored, within slate limits |

`runtime/qc/sheet_check.py` reports clean — 10 beats, no findings.

## Known risks to watch at render time

Per `tips.txt`, in order of how likely they are to bite this specific sheet:

1. **B06 is 40s — the longest beat across both reels**, and it carries two
   distinct movements. Its Manim scene must reach 40s natively or `compile.py`
   will slow-motion it (tips.txt §8). If it can't be made to breathe, the split
   point is clean: integration in B06, mutation testing lifted into B07's
   narration with the artifact card unchanged.
2. **`ReasoningObject` must never go through an uppercase chip helper.** It
   smashes to `REASONINGOBJECT` with no visible word break — the exact defect
   called out in tips.txt §9. Write it as "Reasoning Object" or keep mixed case.
3. **B04's checklist is twelve rows** (5 in scope, 7 deferred). At the 24px floor
   that stack will run past y = −3.6. Compress row spacing and render-check the
   *last* row before committing to a 4K render (tips.txt §7).
4. **B04 needs tick marks.** Use `checked()` from `graphics_lib.py` — never put
   ✓ or ✕ inside a font-forced `Text()` (tips.txt §4).
5. **B03's three mechanism nodes with chips underneath** are the same collision
   class that broke the last reel: wrap "Dynamic Task Allocation" and "Pattern
   Recognition" to two lines (tips.txt §6).
6. **B02, B05, B06 all show real source text.** PT Mono only, real file contents
   only — never prose restyled as code.

## Audio gate sign-off

Narration is final and grammar-checked. All spoken figures are written as words
("twenty-one thousand, eight hundred and twenty-four bytes") so Kokoro reads
them correctly; the digit forms live in the `show` events and Remotion props only.

Ready for `am_onyx` generation across all 10 beats **once a human flips the
verdict line at the top of this file to PASS** — and once the known-gap-#1
question above is decided either way.
