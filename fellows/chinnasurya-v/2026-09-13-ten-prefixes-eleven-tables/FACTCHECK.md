# FACTCHECK — Ten Prefixes, Eleven Tables

Every table name on screen is copied from a migration file. No column contents,
no sample rows and no identifiers appear. **Invented values: none.**

| # | Beat | Claim | Source | Status |
|---|---|---|---|---|
| 1 | B02 | `lti_platform_registrations` and `lti_deployments` hold trusted platforms and their installations | `02_lti_multi_tenant_schema.sql` lines 19, 42 | VERIFIED |
| 2 | B03 | `lti_user_links`, `lti_course_links` and `lti_resource_links` map Canvas identifiers onto the hub's | `02_lti_multi_tenant_schema.sql` lines 55, 73, 91 | VERIFIED |
| 3 | B04 | `lti_nonce_store` and `lti_launch_sessions` exist and are purged | `02_lti_multi_tenant_schema.sql` lines 111, 135 | VERIFIED |
| 4 | B04 | Nonce retention 10 minutes, launch audit 1 hour | `02_lti_multi_tenant_schema.sql` table defaults; `medhavy-ferpa-data-flow.md` §4 | **SEE NOTE** |
| 5 | B05 | `lti_v1_credentials`, `lti_v1_nonces` and `lti_v1_launches` carry LTI 1.1 | `03_lti_v1_credentials.sql` lines 3, 18, 30 | VERIFIED |
| 6 | B06 | Ten tables carry the `lti_` prefix | Count of the 7 in `02_…` plus the 3 in `03_…` | VERIFIED |
| 7 | B06 | Eleven tables have RLS enabled: the ten plus `institutions` | `05_lti_multi_tenant_rls.sql` lines 16-23 (8 tables including `institutions`) + `03_lti_v1_credentials.sql` lines 46-48 (3 tables). 8 + 3 = 11 | VERIFIED |
| 8 | B07 | RLS restricted to the backend service role, non-service roles denied reads and writes | `medhavy-lti-security-review.md` §2.4, verified against the dev database | VERIFIED |

## Note on row 4 — the retention figure is contested in the project's own records

The reel states nonce retention as 10 minutes and launch audit retention as 1
hour, which is what the schema's column defaults say and what the project's FERPA
data-flow document says. A later audit of the same codebase found that the figure
is not consistently true:

- The schema sets `expires_at` on `lti_launch_sessions` to `NOW() + interval '1 hour'`.
- The application's published privacy policy states launch audit records are kept
  for **12 months**.
- The `cleanup_lti_expired_data()` function that performs the purge is **not
  scheduled**: the `pg_cron` line that would run it is commented out in
  `02_lti_multi_tenant_schema.sql`, so in practice neither figure is enforced and
  rows accumulate.

The 10-minute nonce figure is unaffected in substance, since nonces are consumed
delete-on-read at the callback rather than waiting for the purge.

This note is recorded rather than quietly corrected because the claim is on
camera. Reconciling the retention figure to one enforced number, and correcting
the privacy policy to match, is listed in the project's research plan as work for
the next period. **If the reel is rebuilt, B04's launch-audit figure must be
re-measured first.**

## Count resolution

The ten-versus-eleven discrepancy flagged during the first reel is resolved here,
and the resolution is itself on camera: both numbers were right, counting
different things. Row 7 shows the arithmetic.
