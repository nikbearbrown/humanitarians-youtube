# FACTCHECK — solve-verify-asymmetry

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B00 | Claude's solve speed doubles roughly every 18 months | ✓ approximate | Illustrative trend; approximate per model generation cadence |
| B03 | GPA tie-breaking bug: sort by GPA descending without stable secondary key produces non-deterministic tie order | ✓ | Python sort is stable but requires complete sort key specification; the bug is in missing the tie-case test |
| B05 | Claude self-audit may miss its own bugs | ✓ | Pearce et al. 2022 "Asleep at the Keyboard" — model self-audit misses same errors |
| B06 | Solve speed grows; verify speed approximately constant | ✓ illustrative | Structural asymmetry — verify requires deliberate human judgment |

## Illustrative / Synthetic

- 8-second solve time vs. 4-minute verify time — illustrative ratio
- 30x gap label — illustrative, not empirically measured
- Year/ratio table (2023-2026) — illustrative trend

## Sources

- Pearce et al. 2022 "Asleep at the Keyboard" — GitHub Copilot security study
- Chapter 02: Division of Labor — claude-code-for-students

## Exclusions Confirmed

- No benchmark comparison across models ✓
- No formal cognitive science of System 1/System 2 ✓
