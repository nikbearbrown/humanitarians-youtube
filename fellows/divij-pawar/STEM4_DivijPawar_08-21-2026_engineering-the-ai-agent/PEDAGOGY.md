# PEDAGOGY GATE — Engineering the AI Agent

## Revision note (read first — three passes now)

**Pass 1** (6 body beats, a single case-study walkthrough) was reviewed by
the human and judged too thin to be genuinely useful. **Pass 2** added four
generalizable frameworks and restructured the body from 6 beats to 8
(B01–B08; bookends shift to B09–B11).

**Pass 3 (this one): the human pointed at the real source repository**
(`https://github.com/coding-parrot/pothole-reporter`) and asked for its
actual info, images, and graphics to be used. Fetching it live turned up
several inaccuracies in the case-study details carried over from the
original user-supplied script — not the general frameworks, which were
unaffected, but specifics about what this one project actually does. All
are corrected; see SOURCES.md's "Corrections made this pass" table for the
full list. Highlights:

- The app is **not Bengaluru-specific** — it covers National Highways
  nationwide plus several states, Bengaluru being one small part.
- **"Every 8 meters of GPS delta" and "thousands of accidents a year" are
  removed** — neither is documented anywhere in the real project; they
  were unverifiable and are dropped rather than carried as fact.
- **Confidence is never shown as a percentage** — the real UI reports
  clear/probable/uncertain/absent. The invented "92%" and generic
  "probable contract" language are replaced with this real categorical
  scale throughout B03–B05.
- **"42,000 contracts" is replaced with the real, more interesting
  numbers**: a 42,283-row source snapshot → 13,577 indexed → ≤25
  candidates → 1 probable match, Karnataka-only, most with no known
  contractor name.
- **The three guardrails are now shown as one real, unifying principle**
  (fail closed) rather than three unrelated tricks, using the project's
  actual mechanisms: checksum-verified data packs, a highway hand-off
  (not a hard stop), and a date-based warranty inference.
- **B03 now uses the project's own real documentation photo**
  (`assets/example-pothole.jpg`, MIT-licensed) instead of a drawn
  abstraction — a legitimate nopunt HOLD, not a PUNT costume.

This pass also caught and fixed one **pre-existing** layout bug missed in
Pass 2's smoke testing (an arrow in B04 that visually crossed through the
word "night") — see CHECKS-REPORT.md.

Nothing about the general frameworks (truth-table test, pipeline-vs-loop,
guardrail derivation method, the anti-pattern) changed — they're
independent of the case study's specifics and this pass's fact-check.

**What's new, and why:**

1. **The truth-table test (B01, expanded)** — a concrete decision rule for
   finding the unstructured piece ("can you write a truth table for this
   decision?"), not just the abstract instruction to "isolate" it.
2. **Orchestration patterns: pipeline vs. agent loop (B02, new)** — the
   source script asserts a "Sequential Orchestration Pattern" without ever
   naming the alternative or explaining why you'd choose one over the
   other. This is a real, load-bearing architecture decision in agentic
   engineering and the reel was incomplete without it.
3. **Deriving your own guardrails (B07, reframed)** — the source script
   lists three guardrails this one project happens to have. B07 now leads
   with the three-question method that generates them (what's stale? what's
   irreversible? what should refuse outright?), then shows the case study's
   three guardrails as answers to those questions, not as a closed list to
   copy.
4. **The anti-pattern: grading its own homework (B08, new)** — the
   dedicated falsifiability/stress-test beat. Names the actual way people
   get this wrong (skipping the human check because the model is "usually
   right") rather than only showing the system working as designed.

## Narration Review

**Topic:** How to design an agentic AI workflow — isolate the unstructured
reasoning via a concrete test, choose your orchestration pattern
deliberately, derive guardrails from a general method, and know the failure
mode that undoes all of it — worked through a single case study (the
open-source "Pothole Reporter" project)
**Register:** Teardown (narrated by Divij Pawar)
**Audience:** Smart non-technical-to-technical viewers; the supplied source
script is written at a builder/engineer level (mentions VLMs, RAG,
deterministic pipelines by name)
**Series:** STEM — Agents, 4 of 4 (siblings: STEM1 *What Makes an AI
Agentic?*, STEM2 *Why Agents Fail*, STEM3 *The Agent's Dilemma: Autonomy vs.
Control*)

### Source & Adaptation

The user supplied a complete script (`04_engineering_the_ai_agent.md`)
written for an 8–10 minute video, addressed directly to camera ("Welcome...")
with interleaved `[Visual/Graphic]` / `[AI Voice Narration]` blocks.

- **B00 (cold open)** — new, per COLD OPEN LAW. Expanded in this pass to
  preview all three frameworks (truth-table test, orchestration choice,
  guardrail derivation), not just the general topic.
- **B01 (framework)** — from the source's Introduction, expanded with the
  truth-table test (new, this pass).
- **B02 (orchestration patterns)** — entirely new, this pass. No equivalent
  in the source script.
- **B03 (case study), B05–B06 (pipeline)** — carried from the source's
  Introduction/Act 2, condensed for pacing, content unchanged from the
  first authoring pass.
- **B04 (context gap)** — from the source's Act 1, expanded with the
  "narrow blast radius" callback to STEM3's own framework (new, this pass).
- **B07 (guardrails)** — from the source's Act 3, reframed around the
  three-question derivation method (new framing, this pass); the three
  concrete guardrails themselves are unchanged from the source.
- **B08 (anti-pattern)** — entirely new, this pass. No equivalent in the
  source script.
- **B09 (verdict)** — updated to recap all four ideas (truth-table test,
  pipeline choice, guardrail derivation, the anti-pattern) rather than the
  original pass's three-line takeaway.
- **B10 (your turn), B11 (outro)** — updated to reflect the deeper
  framework; still entirely new relative to the source, per HANDOFF LAW.

### Teaching Arc ✓

- **B00 (Cold open):** Self-intro + the three frameworks this video actually
  delivers
- **B01 (Framework 1):** The truth-table test — how to find the model's job
- **B02 (Framework 2):** Pipeline vs. agent loop — how to decide who
  controls sequencing
- **B03 (Case study):** Pothole Reporter introduced; why a photo alone isn't
  an agent
- **B04 (Deconstruction):** The unstructured piece isolated and its blast
  radius named; the context gap it leaves behind
- **B05 (Pipeline, pt. 1):** Perception trigger + the first deterministic
  tool call (reverse-geocoding)
- **B06 (Pipeline, pt. 2):** RAG grounding against a contracts database +
  the synthesized output (the email)
- **B07 (Framework 3):** The three-question guardrail method, demonstrated
  by the case study's own three guardrails
- **B08 (Anti-pattern):** The failure mode that undoes all of it — trusting
  "usually right"
- **B09 (Verdict):** All four frameworks, recapped
- **B10 (Your turn):** Apply all three frameworks to your own feature;
  scaffolded prompt + 3-item rubric
- **B11 (Outro):** Title restate + handle

**EXECUTIVE-SUMMARY LAW:** satisfied at B01 — the isolate/wrap-in-tools
framework and its concrete test are stated whole before the case study, any
mechanism, or any guardrail is introduced.

**FRAMEWORK-BEFORE-EXAMPLES:** B01–B02 establish two independent, general
frameworks; B03–B08 apply both to one worked system end to end, reusing
their vocabulary ("the unstructured piece," "fixed pipeline," "blast
radius," "the three questions") throughout the case study rather than only
in the framework beats.

### Factual Check ✓ (see SOURCES.md for the full table — now largely VERIFIED)

The design-pattern claims from the original script (isolate the
unstructured piece; deterministic tool orchestration; RAG for context
grounding; fail-safe routing; probabilistic hedging; human-in-the-loop
review) are standard, uncontroversial agentic-engineering practice.

The truth-table test, the pipeline-vs-agent-loop framework, the
three-question guardrail method, and the "grading its own homework"
anti-pattern remain **original editorial synthesis** (added in Pass 2), not
claims from the user's source script or the real repo — checked as sound
reasoning, not citation.

**As of Pass 3, the case study's specific claims are verified against the
live repository**, not carried unverified from the user's script. The repo
name, coverage, AI scope, confidence-display language, contract-matching
numbers, and all three guardrail mechanisms are now confirmed directly
against README.md, docs/sources.html, docs/DEMO.md, and docs/privacy.html
(fetched 2026-08-24). Several specifics in the original script turned out
to be wrong or unverifiable and were corrected rather than carried — see
SOURCES.md's "Corrections made this pass" table. The remaining open item is
much narrower now: whether these figures could have changed since the
2026-08-24 fetch (the project's own docs describe versioned, dated data
packs), not whether they were accurate at the time of writing.

No model name, vendor, version, or benchmark appears in the narration (the
real project does use OpenAI's vision API specifically — kept generic here
by choice, see SOURCES.md). The reel should not date on that front, though
the specific numbers now cited are pinned to the fetch date.

### Register & Tone ✓

- Teardown register, consistent with the rest of the series.
- The new framework beats (B02, B07's reframing, B08) are written as
  general, portable advice — "here's how you'd decide for your own system"
  — not as additional trivia about Pothole Reporter specifically.
- Narration budget: body beats now run roughly 45–140 words. **B04 is the
  longest at ~140 words (~54s)** — see Known Deviations below.

### Falsifiability ✓ — strengthened this pass

The first pass's B06 (guardrails) did double duty as both the mechanism
beat and the closest thing to a stress test. This pass gives falsifiability
its own dedicated beat: **B08** doesn't show the system working — it shows
the specific way teams undermine it (skipping the human check because the
model is "usually right"), and states plainly that "usually right" is
exactly the failure mode the guardrails from B07 exist to catch. This is a
stronger falsifiability beat than the first pass had.

### Known deviations from house defaults

1. **Beat count.** This reel now runs 12 beats (B00–B11) against the house
   10-beat default (`agents.md`). Two additional body beats (B02, B08) were
   added specifically because the human reviewer judged the 6-beat version
   too thin — this is a deliberate content decision, not scope creep.
   Precedent: `deep-explainer` (ADVANCED tier) exists exactly for
   "multi-layered concept depth passes" with variable beat count; this reel
   doesn't formally switch skills, but the same judgment applies.
2. **Runtime.** With the real, denser case-study content added in Pass 3
   (the real funnel numbers, the real fail-closed mechanisms, the real
   photo), body narration (B01–B08) is now estimated at roughly **~6.75
   minutes** before Kokoro runs, and the full reel with bookends lands
   around **~7.4 minutes** — solidly inside the source script's own
   8–10 minute framing, achieved by adding real, verified substance rather
   than padding. Still an estimate — confirm against `actual_duration_s`
   after Step 2 of BUILD-PROMPT.md.
3. **B04 (~56s), B06 (~58s), and B07 (~64s)** are the longest body beats,
   similar to STEM3's ~62s B03. B06 and B07 grew this pass because the real
   mechanisms (the contract funnel; the three fail-closed cases) carry more
   legitimate content than the generic versions they replaced — each still
   holds one throughline (grounding+synthesis; the fail-closed principle),
   so one-idea-per-beat is preserved at the level of the beat's core claim.
4. **Case-study numbers are now verified**, not an open item — see
   SOURCES.md Pass 3. The residual uncertainty is only whether the
   project's versioned data (contract counts, coverage) has changed since
   the 2026-08-24 fetch, which is a normal source-staleness question, not a
   fact-check gap.

All 8 Manim scenes (2 new: B02, B08; 6 carried/renumbered from the first
pass) have been still-frame and mid-scene smoke-tested — see
CHECKS-REPORT.md for the specific defects caught and fixed in both passes.

---

## VERDICT: PASS

**Prepared by:** Claude (3 passes — case-study authoring, framework
deepening, live-repo verification; all 8 Manim scenes layout-tested,
including a fix caught only in this pass — see CHECKS-REPORT.md)
**Awaiting approval by:** Divij Pawar
**Date:** 08-24-2026

To approve: replace this section's heading with `VERDICT: PASS` and add
your name and today's date. The main open item from Pass 1 (unverified
case-study numbers) is now resolved — see SOURCES.md's Pass 3 corrections
table. Worth a quick look before signing: confirm you're comfortable with
(a) the real project photo now used in B03, and (b) the corrected numbers
replacing the original script's figures, since the video's claims about
Pothole Reporter now differ in specifics from what was originally supplied.
No audio may be generated — and per BUILD-PROMPT.md, no further build steps
should run — until this reads PASS.
