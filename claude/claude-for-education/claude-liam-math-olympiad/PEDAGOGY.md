# PEDAGOGY — claude-liam-math-olympiad

## Skill
math-olympiad (claude-plugins-official / math-olympiad)

## Learning objective
Understand adversarial proof verification for competition math: interpretation check before solving, context isolation to remove thinking-trace bias, pattern-armed adversarial verifiers, asymmetric vote thresholds, and calibrated abstention.

## Prior knowledge assumed
Knows what competition math is; has used LLM agents; unfamiliar with adversarial verification architecture or olympiad-specific failure modes.

## Key concepts
1. Interpretation check first — 50/63 errors in prior work were wrong reading of the problem
2. Dual context isolation: strip thinking trace before verifying AND blind verifiers to each other's verdicts
3. VERBATIM solver prompt — tool restriction is enforced only by the prompt text, not the Agent tool
4. Asymmetric vote: 4 HOLDS to confirm, 2 HOLE FOUND to refute, pigeonhole early exit
5. Calibrated abstention: "no confident solution" over wrong-and-confident; deep mode before final abstain

## VERDICT: PASS

The adversarial architecture is well-specified with clear reasoning for each design choice. Main gaps: VERBATIM enforcement is fragile (prompt-only), no cost guidance for high-agent-count runs, and pattern reference files must be loaded or verifier falls back to generic checking.
