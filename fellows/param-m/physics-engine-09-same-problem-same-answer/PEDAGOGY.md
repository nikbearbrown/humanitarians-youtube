# PEDAGOGY.md — GATE P — same-problem-same-answer

**Status: SIGNED.**
Claude did not sign it. No audio is generated until it is signed (toolkit rule 3).

## Learning outcome

After watching, a viewer with no physics or coding background can:

1. **Explain** why a symbolic solver can't disagree with itself.
2. **Name** the two places variation can enter: formula selection and model sampling.
3. **Describe** the three routes (one card / none / several) and why the count happens
   before solving — using the 30 vs 2.37 m/s case.

Measurable: given an AI answer, the viewer asks which method it chose and why.

## Audience

Students and general viewers. Defined on first use: *deterministic* (B00–B01),
*formula selection*, *sampling* (B02), *route*, *arbitrate* (B03), *reference* (B05).

## Teaching arc (PROOF GATE checklist)

| Requirement | Where | Status |
|---|---|---|
| Framework before examples | B01–B03: solver, two sources, three routes | ✓ |
| Worked example | B04: the constructed ambiguity case, both answers shown | ✓ |
| Falsifiability | B06: ten runs prove the solver only; parse can vary; the team's own hard question | ✓ |
| Scaffolded viewer task | B08: list every method before picking one | ✓ |
| Four bookends | B00 ask · B00B promise · B08 handoff · B09 outro | ✓ |
| No source, no verdict | Every figure ledgered in SOURCES.md | ✓ |
| Expiry handled | B06 names the model-sampling limit as of commit 2dc4aa4 | ✓ |

## Known weakness

Video 1 introduced the three routes; this video owns why they exist and proves the
ambiguous one with the team's constructed case.

VERDICT: PASS — standing approval by Param Madan in chat for the series, 2026-10-30
