# SOURCES — Four Documents

## Narration provenance

All narration is the operator's own approved script text (`script.md`), reviewed
before the build. Kokoro synthesised it verbatim.

## On-camera claims

16 rows in `FACTCHECK.md`, each traced to one of the four review documents:

| Document | Used for |
|---|---|
| `medhavy-lti-security-review.md` | B02 — endpoints verified, and the remediation list |
| `medhavy-ferpa-data-flow.md` | B03 — FERPA basis, fields received, retention, subprocessor count |
| `medhavy-architecture-hosting-summary.md` | B04 — request path, WAL archiving, RPO, segment counts |
| `medhavy-hecvat-lite-answers.md` | B05, B06 — section list, and the three "no" answers |

## Invented values

**None.** Every figure on screen traces to a FACTCHECK row.

## Time-sensitive

`105 segments archived, 0 failures` was true when read from the dev database.
Re-measure before reusing this reel.

## Deliberately excluded

No individual's name. No subprocessor named aloud or on screen. No hostname, no
key material, no credential. Nothing about production — every verified figure was
measured on dev.
