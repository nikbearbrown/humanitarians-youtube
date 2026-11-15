# PEDAGOGY.md — GATE P — five-steps-one-answer

**Status: SIGNED.**
Claude did not sign it. No audio is generated until it is signed (toolkit rule 3).

## Learning outcome

After watching, a viewer with no physics or coding background can:

1. **Name** the five steps in order: parse, retrieve, plan, solve, verify.
2. **Say** what each step did to one problem (car from rest, 2.5 m/s², 12 s →
   30 m/s, 180 m), including why five of six candidate formulas were rejected.
3. **Explain** that only parse uses a language model, and that the output is a
   record of every step, not just a number.

Measurable: given any AI answer, the viewer asks what it read, which formula it
used, and how it checked.

## Audience

Students and general viewers. Defined on first use: *parse* (B02), *formula card*
(B03), *closure check* (B04), *SymPy* (B05), *verify / second path* (B06),
*solution object* (B07).

## Teaching arc (PROOF GATE checklist)

| Requirement | Where | Status |
|---|---|---|
| Framework before examples | B01: five steps, one job each | ✓ |
| Worked example | B02–B06 carry one golden-set problem (MECH-001) through every step | ✓ |
| Falsifiability | B04: what happens when no card closes — the engine stops and logs the gap | ✓ |
| Scaffolded viewer task | B08: run the same five labeled steps on your own problem | ✓ |
| Four bookends | B00 ask · B00B promise · B08 handoff · B09 outro | ✓ |
| No source, no verdict | Every figure ledgered in SOURCES.md | ✓ |
| Expiry handled | B03 says "thirty-one in this version"; the card count will grow | ✓ |

## Known weakness

The worked problem is deliberately easy, so the pipeline is visible rather than the
physics. The hard cases (ambiguous routes, symbolic answers, ± roots) are later
videos in the series.

VERDICT: PASS — standing approval by Param Madan in chat for the series, 2026-10-30
