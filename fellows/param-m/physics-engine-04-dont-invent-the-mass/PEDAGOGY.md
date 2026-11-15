# PEDAGOGY.md — GATE P — dont-invent-the-mass

**Status: SIGNED.**
Claude did not sign it. No audio is generated until it is signed (toolkit rule 3).

## Learning outcome

After watching, a viewer with no physics or coding background can:

1. **State** what parse may do (read quantities, name the unknowns) and may not do
   (solve, rearrange, pick a value).
2. **Name** its rules: engine vocabulary, SI units, no constants, letters stay letters.
3. **Explain** why a reading mistake is the one error later checks can't catch — and
   recognize an invented number in any AI's answer.

Measurable: given an AI solution, the viewer checks its knowns against the problem
text before checking the arithmetic.

## Audience

Students and general viewers. Defined on first use: *parse / reading comprehension*
(B01), *vocabulary / canonical name* (B02), *SI units*, *constant* (B03),
*benchmark* (B04), *symbolic answer* (B05), *parse error* (B06).

## Teaching arc (PROOF GATE checklist)

| Requirement | Where | Status |
|---|---|---|
| Framework before examples | B01: one job, then the rules | ✓ |
| Worked example | B04–B05: "mass m" → invented 1.0 → kept as a letter → a = g(m2 − m1)/(m1 + m2) | ✓ |
| Falsifiability | B06: parse quality not yet measured against a real model; this step can vary | ✓ |
| Scaffolded viewer task | B08: list knowns with source phrases, keep letters, solve nothing yet | ✓ |
| Four bookends | B00 ask · B00B promise · B08 handoff · B09 outro | ✓ |
| No source, no verdict | Every figure ledgered in SOURCES.md | ✓ |
| Expiry handled | B06 frames the gap as "not proven yet", as of commit 2dc4aa4 | ✓ |

## Known weakness

B02's unit examples are prompt instructions, not measured parser behaviour; the video
presents them as rules the parser is given, not as an accuracy claim.

VERDICT: PASS — standing approval by Param Madan in chat for the series, 2026-10-30
