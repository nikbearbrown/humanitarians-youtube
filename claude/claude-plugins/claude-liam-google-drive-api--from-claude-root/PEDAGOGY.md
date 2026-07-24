# PEDAGOGY — claude-liam-google-drive-api

## Skill reviewed
`anthropics/claude-tag-plugins/google-drive/skills/google-drive-api/SKILL.md`

## What learners will be able to do
- State the two base hosts (metadata vs upload) and know which to use for which operation
- Explain the everything-is-a-file model: folders are files with mimeType=folder, hierarchy via parents[]
- Understand why Workspace files (Docs/Sheets/Slides) cannot use ?alt=media — must use export instead
- Use drive_search.sh and drive_read.sh with correct flags, including pagination via nextPageToken
- Identify the shared drive 404 trap (missing supportsAllDrives=true)

## What makes this teachable
The four "know up front" items at the top of the skill are the right entry point — each maps to a distinct 403/404 failure mode. The bundled scripts abstract the hardest parts (q-expression building, pagination following, mime branching) so the learner can focus on understanding the model rather than curl syntax. The everything-is-a-file abstraction is genuinely elegant and worth calling out.

## Gaps the teardown surfaces
- fields= omits nextPageToken by default — documented in Pagination section but separated from the operation recipes; easy to miss
- gdrive() helper alias is session-only, defined once in a code block — not a persistent script
- Export size limit (exportSizeLimitExceeded, 10 MB) is named as an error but has no fallback recipe in SKILL.md; deferred to references/api.md
- multipart upload content-type discrepancy (multipart/related vs multipart/form-data) documented with a caveat but no resolution recipe
- pageSize cap of 100 silently clamps larger values — no warning at the point of use

## VERDICT: PASS

The four-point upfront model (two hosts, everything-is-a-file, fields=, shared drive) is correctly ordered by failure frequency. Bundled scripts with exhaustive flag docs are the right abstraction. The nextPageToken default-omission trap is the key teachable gap — easy to miss in a separate Pagination section.
