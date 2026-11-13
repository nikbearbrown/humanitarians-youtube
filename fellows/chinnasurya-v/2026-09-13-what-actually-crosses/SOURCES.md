# SOURCES — What Actually Crosses

## Narration provenance

All narration is the operator's own script text (`script.md`), written before the
build and reviewed line by line. Kokoro synthesised it verbatim; no sentence was
rewritten, paraphrased or generated during the build.

## On-camera claims

Enumerated in `FACTCHECK.md`, nine rows. The research for this reel was done
against the code rather than against the project's own documents, which is why
the fact-check cites source files and line numbers rather than prose:

| Source | Used for |
|---|---|
| `app/api/lti/callback/route.ts` | The launch token is the only inbound transfer |
| `lib/lti-utils.ts` | `scopes: []` and the deep-linking placement |
| `lib/lti-validation.ts` | Which message types are admitted |
| `lib/quiz/grading.ts` | Server-side grading, no client-submitted score |
| `app/api/quizzes/[id]/submit/route.ts` | The comment marking the unbuilt AGS push |
| `db-migrations/02_lti_multi_tenant_schema.sql` | Links written on arrival |
| `medhavy-lti-security-review.md` §2.1 | Scope removal as a deliberate decision |
| `medhavy-ferpa-data-flow.md` §2 | The claim list carried in the token |
| LTI 1.3 specification (IMS Global) | What NRPS and AGS are for |

## Invented values

**None.** Every parameter name and identifier on screen traces to a FACTCHECK row.
The identifier pairs shown in B03 are abstract placeholders, visibly truncated,
and are not real subject identifiers from any database.

## Deliberately excluded

No hostname, no key material, no individual named, no institution's internal
review process, and no claim about the production environment. The two code
findings in `FACTCHECK.md` are kept off camera on purpose.
