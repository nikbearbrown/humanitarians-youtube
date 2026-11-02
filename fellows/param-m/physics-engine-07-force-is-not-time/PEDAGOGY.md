# PEDAGOGY.md — GATE P — force-is-not-time

**Status: SIGNED.**
Claude did not sign it. No audio is generated until it is signed (toolkit rule 3).

## Learning outcome

After watching, a viewer with no physics or coding background can:

1. **Explain** why a number without the right unit is a wrong answer (cm vs m = ×100).
2. **Describe** the engine's two unit checks — real dimension; card agrees with the
   dictionary — and what they don't do (carry units through the algebra).
3. **Retell** the T finding (newtons vs seconds) and why an honest "we used X instead
   of Y, and here's the limit" is a strength.

Measurable: given an AI physics answer, the viewer checks its units before its number.

## Audience

Students and general viewers. Defined on first use: *unit*, *dimension* (B01–B03),
*dictionary of variables* (B01), *tension*, *period* (B04), *library* (B06).

## Teaching arc (PROOF GATE checklist)

| Requirement | Where | Status |
|---|---|---|
| Framework before examples | B01–B03: labels, two checks | ✓ |
| Worked example | B04–B05: T as newtons and seconds → flagged → glossary says "N or s" | ✓ |
| Falsifiability | B06: pint not used; units not propagated through the solve | ✓ |
| Scaffolded viewer task | B08: step-by-step unit check on any formula | ✓ |
| Four bookends | B00 ask · B00B promise · B08 handoff · B09 outro | ✓ |
| No source, no verdict | Every figure ledgered in SOURCES.md | ✓ |
| Expiry handled | B06 calls propagation "still open" as of commit 2dc4aa4 | ✓ |

## Known weakness

Overlaps video 5's brief mention of the T collision; this video owns the mechanism
that found it.

VERDICT: PASS — standing approval by Param Madan in chat for the series, 2026-10-30
