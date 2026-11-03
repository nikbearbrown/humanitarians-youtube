# PEDAGOGY GATE — Grading the Machine

## Narration Review

**Topic:** Why the two obvious ways to score an AI system's confidence —
self-reporting and a second AI judge — are both structurally broken, why
a computed score built from fixed, observable penalties actually holds
up, why a low score must never be suppressed, and the honest limit that
the computed score's own constants are still uncalibrated.
**Register:** Energetic, myth-busting teardown (per the source script's
own header)
**Audience:** High-school technicality, per the source script's own header
**Series:** STEM — Agents, Episode 8. B09 closes by teasing the next
problem (an agent instructed by content it's merely reading), already
scripted as `youtube/STEM9/09_the_agent_that_was_told_what_to_do.md`.

### Source & Adaptation

Narration is condensed from `08_grading_the_machine.md`, split into 10
beats matching the source's 6 body sections plus bookends. Two instances
of a repeated contrastive construction were rewritten in the source
script for natural spoken cadence, per the now-standing house convention
(first applied to STEM6 at explicit request, applied proactively since)
— see SOURCES.md "Corrections applied to narration."

**What was added, because the source script has no scaffolded viewer
task:**

- **B00 (cold open)** — condenses the source's opening two paragraphs and
  adds the required self-introduction per house convention.
- **B08 (your turn)** — a new, concrete 3-step task (identify which of
  the three scoring categories your own system falls into, then sketch a
  computed alternative), built from the episode's own framework, since
  the source poses no runnable scaffold.
- **B09 (outro)** — bridges to STEM9 rather than ending on the source's
  own closing aphorism, matching the house convention of closing on a
  tease to the next scripted episode.

Nothing from the source's substantive content was cut; both bad ideas,
the computed-scoring mechanism, the suppression argument, and the
calibration caveat all survive intact.

### Teaching Arc ✓

- **B00 (Cold open):** Poses the question — who grades the grader?
- **B01 (Bad idea 1):** Self-reported confidence, and why it's the same
  mechanism grading itself
- **B02 (Bad idea 2):** LLM-as-a-judge, and the category error it commits
- **B03 (Framework/mechanism):** Computed scoring — the approach that
  actually holds up
- **B04 (Design rule):** Never suppress a low score
- **B05 (Falsifiability):** The honest caveat — uncalibrated constants
- **B06 (The framework):** Three-way comparison, transferable rubric
- **B07 (Verdict):** Condensed recap card
- **B08 (Your turn):** A concrete, ordered 3-step audit task
- **B09 (Outro):** Title restate, handle, bridge to STEM9

**EXECUTIVE-SUMMARY LAW:** satisfied at B00 — the whole episode's
question (who grades the grader, and can they be trusted) is posed
before either bad idea is examined.

**FRAMEWORK-BEFORE-EXAMPLES:** B01/B02 each demonstrate a failure mode
before B03 introduces the mechanism that avoids both; B06 collapses all
three into one transferable comparison a viewer can apply to any scoring
system, not just this one.

### Factual Check ✓

See SOURCES.md for the full claim table. Summary: this reel describes
**general practice** around AI confidence/evaluation design (self-report,
LLM-as-judge, computed scoring), not this project's own code. No model
names, vendors, versions, or benchmark figures appear anywhere. One claim
("serious systems walked away from this approach") is kept general
rather than attributed to a specific unverified project.

### Register & Tone ✓

- "Energetic, myth-busting teardown" carried through: each bad idea gets
  a real diagram and a named failure (not just narrated dismissal) before
  the actual mechanism is introduced.
- B05 refuses the easy ending — it explicitly stress-tests the episode's
  own proposed fix (computed scoring) rather than presenting it as a
  clean solution.
- Narration budget: body beats (B01–B06) run roughly 95–170 words each,
  consistent with the sibling series' established body-beat length.

### Falsifiability ✓

**B05** is the dedicated stress-test beat, and it stress-tests the
episode's *own* proposed mechanism: computed scoring is inspectable, but
its specific penalty constants are still first-principles guesses, not
yet checked against real outcomes. This is why B06's framework says
"computed — inspectable, and still being calibrated" rather than
presenting computed scoring as a finished, trustworthy answer.

### Known deviations from house defaults

1. **Beat count.** 10 beats (B00–B09), matching STEM7's count but arrived
   at independently from this script's own 6 body sections.
2. **Runtime.** The source script header says "~9 minutes." Based on the
   pattern established across STEM2/STEM5/STEM6/STEM7 (all estimated
   ~9 min, all measured shorter once real Kokoro audio was generated),
   this narration is likely to run **shorter than 9 minutes** — the
   actual number is unknown until Step 2 of BUILD-PROMPT.md runs.
3. **B02 and B03 are longer body beats** (est. 56s and 54s), matching the
   established pattern for beats carrying multi-part content.

---

## VERDICT: PASS

**Prepared by:** Claude (beat-sheet authoring pass)
**Approved by:** Divij Pawar
**Date:** 09/20/2026

**What a human reviewer should check before flipping this to PASS:**

1. **The generalized "serious systems" claim in B02** — confirm it's
   acceptable kept general (no specific project named) rather than cut
   or replaced with a real citation.
2. **The illustrative ledger example** (base 1.0, -0.1 penalties) —
   confirm it's acceptable as a declared-illustrative teaching device.
3. **The B08 scaffolded task** — confirm the 3-step audit is concrete
   enough, or needs sharpening.
4. **The runtime gap** — once Step 2 (Kokoro) runs, compare actual
   runtime to the source's "~9 min" header.

Once satisfied, replace this line with `VERDICT: PASS`, sign, and date it.
**No audio generation (Step 2 of BUILD-PROMPT.md) may run until this line
reads PASS** — this is GATE P, per `youtube/CLAUDE.md` §4 and
`brutalist.art/CLAUDE.md` rule 3.
