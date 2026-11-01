# PEDAGOGY.md — GATE P — where-it-went-wrong

**Status: SIGNED.**
Claude did not sign it. No audio is generated until it is signed (toolkit rule 3).

## Learning outcome

After watching, a viewer with no physics or coding background can:

1. **Explain** how grade mode names a mistake: the student's number is tested against
   wrong formulas built from the right one.
2. **Describe** divergence detection: the first wrong step is the only useful pointer.
3. **State** its two refusals (no unverified grading; nothing stored) and that it is
   not deployed.

Measurable: given feedback that just says "wrong", the viewer asks which step and which
mistake.

## Audience

Students, instructors and general viewers. Defined on first use: *grade mode* (B00),
*verified answer* (B01), *sign flip*, *square root of two* (B02), *sign convention* (B03),
*moment of inertia*, *downstream* (B04), *tolerance* (B05), *not assessable* (B06).

## Teaching arc (PROOF GATE checklist)

| Requirement | Where | Status |
|---|---|---|
| Framework before examples | B01–B02: diagnose; the pattern list | ✓ |
| Worked example | B03 (−1.96 sign flip) and B04 (I = 0.125 vs 0.0625) | ✓ |
| Falsifiability | B06: refuses unverified grading; nothing deployed, no student has used it | ✓ |
| Scaffolded viewer task | B08: find my first wrong step and the matching mistake | ✓ |
| Four bookends | B00 ask · B00B promise · B08 handoff · B09 outro | ✓ |
| No source, no verdict | Every figure ledgered in SOURCES.md | ✓ |
| Expiry handled | B06 "not deployed yet", as of commit 2dc4aa4 | ✓ |

## Known weakness

Video 6 introduced not_assessable; this video gives it one line and spends its time on
diagnosis.

VERDICT: PASS — standing approval by Param Madan in chat for the series, 2026-10-30
