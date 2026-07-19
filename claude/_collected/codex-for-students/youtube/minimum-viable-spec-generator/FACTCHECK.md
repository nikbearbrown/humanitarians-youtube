# FACTCHECK — minimum-viable-spec-generator

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00 | Every vague user need is an unconstrained degree of freedom — Codex fills them with its defaults | ✓ | Ch08: "Every vague user need is an unconstrained degree of freedom. Codex fills unconstrained degrees of freedom with its defaults." Verbatim. | — |
| B01 | Five-section MVS: Problem, Architecture, User flows, User needs, Out of scope | ✓ | Ch08: The five sections are named. Verbatim. | — |
| B01 | 'Responsive' is not a user need; 'loads in under 2 seconds on a 5MB input file on throttled 3G' is | ✓ | Ch08: "Responsive is not a user need. Loads in under 2 seconds on a 5MB input file on a throttled 3G connection is." Verbatim. | — |
| B04 | 2 user needs flagged and rewritten: 'fast' → 2-second threshold; 'easy to read' → 120% zoom test | Illustrative | Synthetic example illustrating the validation step from Ch08. Threshold values consistent with Ch08's examples. | Marked synthetic. |
| B04 | Interrogation added delta-versus-last-build view not in original description | Illustrative | Synthetic example illustrating the interrogation's value from Ch08. | Marked synthetic. |
| B06 | Without interrogation, delta view absent; it represented 30% of eventual build scope | Illustrative | Synthetic calculation illustrating the interrogation's contribution. | Marked synthetic. |
| B07 | Interrogation targets: returning vs first-time users, failure states, outputs not named | ✓ | Ch08: "The Ask Mode questions target the aspects most likely to be unconsidered: returning users vs. first-time, failure states, outputs you didn't think to name." Verbatim. | — |

## Illustrative Scenarios
- B04: User needs rewriting examples (fast/easy-to-read) — SYNTHETIC. Threshold values drawn from Ch08's examples.
- B04/B06: Delta-versus-last-build view discovered via interrogation — SYNTHETIC. Illustrates the mechanism from Ch08.
- All code outputs are synthetic demonstrations.
