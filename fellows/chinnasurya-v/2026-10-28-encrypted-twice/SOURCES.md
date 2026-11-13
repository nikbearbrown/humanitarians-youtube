# SOURCES — Encrypted Twice

## Narration provenance

All narration is the operator's own script text (`script.md`), written before the
build. Kokoro synthesised it verbatim.

| Source | Used for |
|---|---|
| `lib/lti-crypto.ts` | The envelope format, the encrypt and decrypt paths, the `isEncrypted` guard |
| `tests/lti-crypto.test.ts` | The format assertion and the tamper-detection assertion |
| `db-migrations/02_…` and `03_…` | The two credential fields and where they live |
| `medhavy-lti-security-review.md` | The storage-layer claim, labelled there as a vendor statement |

## Invented values

**None.** No key, no IV, no auth tag and no ciphertext appears anywhere on
camera. `v1 : iv : tag : ciphertext` is the field layout, not a value.

## Deliberately excluded

No key material, no connection string, no hostname, no individual named, and no
claim about the production environment.
