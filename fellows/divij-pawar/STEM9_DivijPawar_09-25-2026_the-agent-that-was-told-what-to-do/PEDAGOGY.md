# PEDAGOGY GATE — The Agent That Was Told What To Do

## Narration Review

**Topic:** Prompt injection — why a language model has no architectural
separation between "instructions" and "content it's merely reading," a
worked example of a hidden instruction riding inside an email, why this
is a structurally different problem from the autonomy/permission
question, the three real mitigations and each one's honest limit, and
the deliberately unresolved close: this is an open problem, not a solved
one.
**Register:** Mechanism-focused thriller, quiet dread (per the source
script's own header)
**Audience:** High-school technicality, per the source script's own header
**Series:** STEM — Agents, Episode 9. This is the **fifth and, as of
this writing, final episode** of the "Accountability" mini-series
(STEM5–STEM9) — no STEM10 script exists in `youtube/` as of this writing
(confirmed by directory listing). B10 closes the series accordingly:
reflective, not a tease to a next episode.

### Source & Adaptation

Narration is condensed from `09_the_agent_that_was_told_what_to_do.md`,
split into 11 beats matching the source's 6 body sections plus bookends
— one beat per mitigation (B04/B05/B06) rather than crowding all three
into one hold, per `youtube/CLAUDE.md` §4's "one idea per beat" rule.

Before beat-sheet authoring, three instances of a repeated "isn't X. It's
Y." construction were rewritten in the source script for natural spoken
cadence — no factual or structural content changed. This is now a
standing house convention — see SOURCES.md "Corrections applied to
narration."

**What was added, because the source script has no scaffolded viewer
task and this is a series finale:**

- **B00 (cold open)** — condenses the source's opening paragraph and adds
  the required self-introduction per house convention.
- **B09 (your turn)** — a new, concrete 2-question task (would your own
  system notice a hidden instruction; does your approval screen surface
  every side-effect), built from the episode's own mitigations, since
  the source poses no runnable scaffold.
- **B10 (outro)** — reflects on the mini-series as a whole (five videos,
  five different shapes of the same underlying question) rather than
  teasing a next episode, since none is currently scripted. This departs
  from STEM5–STEM8's "bridge to next episode" outro convention
  deliberately, not by oversight — flagged below for reviewer sign-off.

Nothing from the source's substantive content was cut; the token-level
mechanism, the worked example, the autonomy distinction, all three
mitigations with their limits, and the closing "this is unsolved" stance
all survive intact.

### Teaching Arc ✓

- **B00 (Cold open):** States the scenario — an agent did exactly its job
  and still followed an unauthorized instruction
- **B01 (Framework/BLUF):** The token-level mechanism — no channel
  separation between instructions and data — stated before any example
- **B02 (Worked example):** Hidden instruction in an email, riding beside
  a legitimate approval-gated task
- **B03 (Distinction):** Why this isn't a repeat of the autonomy question
- **B04 (Mitigation 1):** Lock the core instructions, and its limit
- **B05 (Mitigation 2 / Falsifiability callback):** Cross-examination,
  and the shared-contamination hole already established in STEM6
- **B06 (Mitigation 3):** Human approval, and its real limit
- **B07 (Honesty beat):** Sitting with the unsolved state of the problem
  — deliberately not a clean framework
- **B08 (Verdict):** Condensed recap card that preserves "this is
  unsolved" rather than manufacturing false resolution
- **B09 (Your turn):** A concrete, 2-question audit task
- **B10 (Outro):** Series-reflective close, not a next-episode tease

**EXECUTIVE-SUMMARY LAW:** satisfied at B01 — the token-level mechanism
(no channel separation) is stated as the episode's organizing fact before
the worked example or any mitigation is introduced.

**FRAMEWORK-BEFORE-EXAMPLES:** B01 states the mechanism in the abstract;
B02 makes it concrete with one worked example; B03 sharpens the
distinction from a prior episode's framework; B04–B06 each test one
candidate fix against the mechanism stated in B01.

### Factual Check ✓

See SOURCES.md for the full claim table. Summary: this reel describes
**general, structural facts about LLM-based agents** (token-level
instruction/data conflation, prompt injection, mitigation limits), not
this project's own code. No model names, vendors, versions, or benchmark
figures appear anywhere.

### Register & Tone ✓

- "Mechanism-focused thriller, quiet dread" carried through: B02's hidden
  white-on-white text and B07's flickering "could this be an instruction?"
  both land the unsettling register without overstating the mechanism.
- This episode's honest ending is explicitly *not* a clean framework —
  B07/B08 preserve that rather than manufacturing false resolution, which
  is itself the register the source script calls for ("the one video...
  where the honest ending isn't a clean framework").
- Narration budget: body beats (B01–B07) run roughly 75–170 words each.

### Falsifiability ✓

This entire episode *is* the series' falsifiability beat in miniature —
unlike prior episodes where one dedicated beat stress-tests a proposed
fix, here **B04, B05, and B06 each state their own mitigation's limit in
the same beat that introduces it** (shrinks but doesn't remove; raises
cost but has a hole; only as good as what it surfaces), and B07 then
states plainly that none of the three closes the gap. No beat oversells
a fix as complete.

### Known deviations from house defaults

1. **Beat count.** 11 beats (B00–B10), one more than STEM7/STEM8's 10,
   because three mitigations each earned their own dedicated beat rather
   than being crowded into one "mitigations" hold.
2. **The outro does not bridge to a next episode.** STEM5–STEM8 all
   closed on a tease to the next scripted episode; this one closes on a
   series-reflective note instead, since STEM9 is the final currently-
   scripted episode. **Flagged for the human reviewer** — confirm this
   reflects an intentional series pause/close rather than an oversight
   (i.e. that a STEM10 isn't expected imminently).
3. **Runtime.** The source script header says "~9 minutes." Based on the
   pattern established across STEM2/STEM5/STEM6/STEM7/STEM8 (all
   estimated ~9 min, all measured shorter once real Kokoro audio was
   generated), this narration is likely to run **shorter than 9
   minutes** — the actual number is unknown until Step 2 of
   BUILD-PROMPT.md runs.

---

## VERDICT: PASS

**Prepared by:** Claude (beat-sheet authoring pass)
**Approved by:** Divij Pawar
**Date:** 09/20/2026

**What a human reviewer should check before flipping this to PASS:**

1. **The series-closing outro (B10)** — confirm this is the right call
   given no STEM10 exists yet, rather than assuming a next episode will
   follow shortly.
2. **The beat-count deviation (11, one more than STEM7/STEM8)** — confirm
   splitting the three mitigations into separate beats is worth it.
3. **The illustrative email scenario (B02)** — confirm it's acceptable as
   a declared-illustrative teaching device.
4. **The B09 scaffolded task** — confirm the 2-question audit is concrete
   enough, or needs sharpening.
5. **The runtime gap** — once Step 2 (Kokoro) runs, compare actual
   runtime to the source's "~9 min" header.

Once satisfied, replace this line with `VERDICT: PASS`, sign, and date it.
**No audio generation (Step 2 of BUILD-PROMPT.md) may run until this line
reads PASS** — this is GATE P, per `youtube/CLAUDE.md` §4 and
`brutalist.art/CLAUDE.md` rule 3.
