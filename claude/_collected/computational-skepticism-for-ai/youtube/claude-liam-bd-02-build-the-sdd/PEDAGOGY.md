# PEDAGOGY — claude-liam-bd-02-build-the-sdd

## Act structure
8 beats (~348s). Process tutorial (E2/4). Cold open (B00) states the governing principle for the whole SDD: don't clean up the flags. B01 covers /v1 (problem summary distinguishing this system from comparables, collision-tested principles in /v2), and introduces the personal paragraph requirement with its scope boundary (Gru does not write it). B02 covers /v3 and /v4 with a concrete vs. vague contrast at both levels. B03 covers /s1 and names the two traps: scope creep and cosmetic cleanup. B04 unpacks the personal paragraph specifically: what it answers, when to write it, and what "I got lucky" looks like as a valid response. BVDT delivers the full gate sequence as a checklist. BHTF reads the full prompt aloud including the load-bearing "do not write it for me" instruction. BOUT closes.

## Cold open law
Opens on the single governing rule: the SDD's value is in the unresolved flags it shows, not its polish. The tension is stated immediately — "a polished SDD with no flags is a document that was easy to write" — and the lesson is complete in four sentences.

## Gap formula
Gap: students have passed /v0 but have no framework for running the five remaining gates at the required level of specificity, and will default to vague formulations that look like output but fail the testability criterion. Bridge: concrete-vs-vague contrast at /v3 (flow steps) and /v4 (need statements), plus explicit naming of the two traps at /s1. Close: a complete SDD submitted with unedited Gru output and a personally authored paragraph.

## Utility lint
Every gate has a specific failure mode named. /v1: fails if it doesn't distinguish from comparables. /v2: fails without a collision test. /v3: fails if any step says "system processes." /v4: fails if the need can't be run as a test. /s1: fails if any component has no mapped Need. Two traps named by consequence, not by caution.

## Vocabulary / register
"SDD" (Software Design Document) defined on first use in B00. "Collision test" defined in B01 with a passing example (the full principle sentence that names the sacrifice). "Scope creep" named in B03 with the exact Gru trigger (component with no Need). Register: Pragmatist throughout — imperative second person, no hedging, no encouragement filler.

## Honesty
The claim that a cosmetic cleanup "is a coverup" is accurate and direct — it names what the behavior actually is. The "I got lucky" framing for /v1 passing without pushback is honest: it acknowledges the possibility and makes it acceptable to say so. The concrete flow-step example (policy-check module, rule set v3.2, UNKNOWN_VENDOR) is specific enough to be an actual test case, which is the standard it's illustrating.

## Length law
8 beats (~348s, ~5:48). 8-beat structure warranted: E2 covers five gates (vs. E1's one), has a distinct personal-artifact requirement, and needs a beat (B04) to scope the paragraph carefully so students don't ask Gru to write it. No beat is padded. B03 and B04 are the shortest body beats; they carry discrete, bounded concepts.

## Narration spot-check
B00 correctly echoes the "don't clean it up" frame that drives the BHTF instruction. B01 personal paragraph requirement scoped correctly (after /v1, before /v2). B02 concrete flow example uses a real-sounding system name and specific artifact (violation record with field name, rule ID, rejection reason). BHTF reads the full prompt verbatim including the "do not write it for me" clause and explains why it's load-bearing. BOUT title matches metadata title exactly.

## Visual law
All Remotion. B00 and BHTF use ClaudeComposerAsk. B01–B04 use ClaudeWindow artifact view, ≤6 lines each. BVDT uses ClaudeVerdictArtifact with 5 lines. BOUT uses ClaudeTitleOutro. sparkLine on each ClaudeWindow beat ≤4 words + short phrase (compliant).

VERDICT: PASS
