# PEDAGOGY.md — GATE P — who-does-the-math

**Status: SIGNED.** A human signs `VERDICT: PASS` at the bottom of this file.
Claude did not sign it. No audio is generated until it is signed
(toolkit rule 3).

## Learning outcome

After watching, a viewer with no physics or coding background can:

1. **Explain** the division of labor: the language model reads the problem,
   picks the formula and explains; a symbolic solver (SymPy, pint) does every
   calculation.
2. **Name** the three routes the engine picks *before* solving — one card fits
   (final answer), several fit (all answers returned, AI arbitrates), none fit
   (AI handles it, gap logged).
3. **Apply** three questions to any AI-produced number: who did the math, were
   units checked, would it say if it didn't know.

Measurable: given a chatbot answer to a physics question, the viewer can say
which of the three questions it fails.

## Audience

Students and general viewers. Defined on first use: *large language model*
(B01), *SymPy*, *pint* (B01), *physics problem-solving engine* vs game engine
(B02), *formula card* (B03), *route* (B04), *baseline* (B06).

## Teaching arc (PROOF GATE checklist)

| Requirement | Where | Status |
|---|---|---|
| Framework before examples | B00B states the three claims before any detail | ✓ |
| Worked example | B03–B05 follow one question through pipeline, routing, results | ✓ |
| Falsifiability | B06 lists what the team says is unproven (parse, baseline, coverage, deployment) | ✓ |
| Scaffolded viewer task | B08: paste a real problem from your own class | ✓ |
| Four bookends | B00 ask · B00B promise · B08 handoff · B09 outro | ✓ |
| No source, no verdict | Every figure ledgered in SOURCES.md against a pinned commit | ✓ |
| Expiry handled | B06 carries "as of" the pinned commit; B07 says the numbers change, the rule doesn't | ✓ |

## Known weakness

Results (16/16, ten identical runs) are the repo's own reported checks; they
were not re-executed for this video. Video 15 (golden set) is the place to show
them being run.

VERDICT: PASS — signed by Param Madan in chat, 2026-10-30
