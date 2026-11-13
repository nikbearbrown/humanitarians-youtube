# SOURCES — Ten Prefixes, Eleven Tables

## Narration provenance

All narration is the operator's own script text (`script.md`), written 13
September and unchanged since. Kokoro synthesised it verbatim; no sentence was
rewritten or generated during the build.

## On-camera claims

Eight rows in `FACTCHECK.md`, one of them carrying an explicit note that the
claim is contested by the project's own later audit.

| Source | Used for |
|---|---|
| `db-migrations/02_lti_multi_tenant_schema.sql` | Seven table definitions, their purposes and their expiry defaults |
| `db-migrations/03_lti_v1_credentials.sql` | The three LTI 1.1 tables and their RLS |
| `db-migrations/05_lti_multi_tenant_rls.sql` | The eight tables with RLS, `institutions` among them |
| `medhavy-lti-security-review.md` §2.4 | Service-role restriction, verified on the dev database |
| `medhavy-ferpa-data-flow.md` §4 | The retention figures, now carrying a note |

## Invented values

**None.** Every table name is copied from a migration file. No column contents,
no sample rows, no identifiers. The numerals in B06 are counts and the arithmetic
for them is shown in `FACTCHECK.md` row 7.

## Deliberately excluded

No hostname, no key material, no connection string, no individual named, no claim
about the production environment.
