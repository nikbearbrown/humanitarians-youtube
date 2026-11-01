# PEDAGOGY.md — GATE P — the-engine-that-says-no

**Status: SIGNED.**
Claude did not sign it. No audio is generated until it is signed (toolkit rule 3).

## Learning outcome

After watching, a viewer with no physics or coding background can:

1. **Explain** a closure check: with what's given, can the equations pin down every
   unknown — asked before solving.
2. **Name** the three ways a plan fails (missing knowns, solver error, no definite
   answer) and what happens next (marked unverified, logged as a gap).
3. **Judge** "zero wrong" correctly — it measures honesty, not coverage — and
   recognize when declining is itself a bug.

Measurable: shown an AI answer, the viewer asks whether the tool could have declined.

## Audience

Students and general viewers. Defined on first use: *closure* (B01), *known*,
*solver error* (B02), *damped oscillator*, *coverage gap* (B03), *benchmark*,
*derivation* (B04), *symbolic* (B05), *not assessable* (B06).

## Teaching arc (PROOF GATE checklist)

| Requirement | Where | Status |
|---|---|---|
| Framework before examples | B01: closure, then the three failure modes | ✓ |
| Worked example | B03: the damped oscillator → unverified → coverage queue | ✓ |
| Falsifiability | B04–B05: "zero wrong" mostly measures honesty; declining hid real capability | ✓ |
| Scaffolded viewer task | B08: run a closure check before solving | ✓ |
| Four bookends | B00 ask · B00B promise · B08 handoff · B09 outro | ✓ |
| No source, no verdict | Every figure ledgered in SOURCES.md | ✓ |
| Expiry handled | B04 frames the 60-problem result as a measurement of a thin library, at 2dc4aa4 | ✓ |

## Known weakness

Overlaps video 3's plan step by design; this video goes past the single happy path
into failures, the benchmark run, and grading.

VERDICT: PASS — standing approval by Param Madan in chat for the series, 2026-10-30
