# FACTCHECK — dangerous-middle-activity

## Claims audit

| Claim | Beat | Verdict | Source / Note |
|---|---|---|---|
| Dangerous middle: tasks that look like pattern work but require supervisory capacity | B01 | ✓ | Chapter 09: dangerous middle documented |
| SQL NULL ordering: NULLs sort before positive values in ascending ORDER BY | B03 | ✓ | NULLS FIRST is the default in many SQL databases (PostgreSQL, SQLite) in ascending order |
| File watcher CPU flood without rate limit | B03 | ✓ | Documented system-level failure mode for inotify/FSEvents watchers |
| Research synthesis hallucination: invented consensus | B06 | ✓ | Documented LLM behavior — consensus confabulation in multi-document synthesis |
| Supervisory capacities: PF, PA, TO, IJ, EI | B02 | ✓ | Chapter 09: five supervisory capacities documented |
| Each probe is specific: a concrete input, not check the output | B04 | ✓ | Chapter 09: probe specificity requirement |

## Illustrative scenarios
- GPA sort tie-breaking: synthetic scenario, non-deterministic sort behavior is real
- SQL NULL scenario: synthetic, NULL ordering behavior is factually correct
- File watcher bulk upload: synthetic, CPU flood from unbounded watchers is real
- Research synthesis consensus: synthetic, hallucination pattern is documented
- All scenarios structured consistently with chapter 09

## Exclusions verified
- No API key discussion: PASS
- No npm install walkthrough: PASS
