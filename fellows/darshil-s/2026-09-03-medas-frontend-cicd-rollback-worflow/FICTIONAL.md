# Frictional Log — 2026-09-03

**Learnings:** The difference between an automatic, lenient check and a manual, strict one — CI runs on every PR and can flag a failure, but on this org's Free plan it can't block the merge button, so a red X is a warning, not a gate; Rollback runs only on a deliberate `workflow_dispatch`, gated by two guards (tag-to-environment validation, then an Artifact Registry image-exists check) before it ever touches a live service.

**Implemented work:** Documented both workflows end to end — CI's checkout → Node setup → `npm ci` → lint (continue-on-error) → test (blocking) → build sequence, and Rollback's manual trigger → input validation → image verification → `gcloud run deploy` redeploy sequence — and proved CI's actual behavior with a worked example: PR #2 deliberately broke a test assertion, confirming the check failed and reported correctly while the merge button stayed clickable, exactly as designed on this plan tier.
