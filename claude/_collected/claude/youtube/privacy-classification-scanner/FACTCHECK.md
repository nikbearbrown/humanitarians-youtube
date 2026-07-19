# FACTCHECK — privacy-classification-scanner

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | Scanner finds patient identifiers in files you forgot to redact | Illustrative | Chapter 08: privacy scenario — files with PII patterns in working folders | None needed |
| B01 | 'I can access this file' and 'I should give Claude access to this file' are different questions | ✓ | Chapter 08: near-verbatim framing of the privacy access distinction | — |
| B02 | Six-tier sensitivity taxonomy: Public, Internal, Confidential, Personal, Regulated, Credentials | ✓ | Chapter 08: sensitivity taxonomy described | — |
| B03 | Classification is filename-only — tool never reads file contents for Personal/Regulated | ✓ | cli-ideas.md candidate 07: "verify the tool does not read file contents for Personal/Regulated classification (filename + extension only for privacy)" | — |
| B03 | Tax records → Regulated, client contracts → Confidential, API keys → Credentials | ✓ | cli-ideas.md candidate 07: pattern examples verbatim | — |
| B07 | Scanner makes access vs appropriate access gap visible before the session begins | ✓ | Chapter 08: scanning before session as the practice move | — |

## Terms Table
| Term | Debut beat | Prior beat |
|---|---|---|
| sensitivity taxonomy | B02 | B01 established the access distinction |
| Cowork-ready | B05 | B02 showed the taxonomy |

## Exclusion Confirmation
- NO content-level PII scanning (filename only): PASS
- NO GDPR compliance workflows: PASS
- NO enterprise DLP integration: PASS

## Illustrative Examples
- B04: fifteen-file test directory — ILLUSTRATIVE with dummy filenames
