# FACTCHECK — Encrypted Twice

**Invented values: none.** No key material, no real ciphertext and no IV appears.
The format line is the shape only.

| # | Beat | Claim | Source | Status |
|---|---|---|---|---|
| 1 | B01 | The hub stores a signing key and, for LTI 1.1 platforms, a shared secret | `02_lti_multi_tenant_schema.sql` `rsa_private_key`; `03_lti_v1_credentials.sql` `shared_secret` | VERIFIED |
| 2 | B02 | Supabase applies AES-256 at the storage layer | Supabase platform documentation, cited in `medhavy-lti-security-review.md` | **VENDOR CLAIM — not independently verified** |
| 3 | B03 | Storage-layer encryption does not protect a value from a query that runs | Property of at-rest encryption, stated as mechanism | MECHANISM |
| 4 | B04 | Stored credential values carry an application-layer AES-256-GCM layer | `lib/lti-crypto.ts` — `encryptSecret` / `decryptSecret` | VERIFIED |
| 5 | B04 | The stored format is `v1:<iv>:<tag>:<ciphertext>` | `lib/lti-crypto.ts`; asserted in `tests/lti-crypto.test.ts` | VERIFIED |
| 6 | B05 | GCM is authenticated, so tampered ciphertext fails to decrypt rather than returning wrong data | Property of AES-GCM; asserted in `tests/lti-crypto.test.ts` | VERIFIED |
| 7 | B06 | Values without the version marker are passed through as legacy plaintext | `lib/lti-crypto.ts` `isEncrypted` guard on the decrypt path | VERIFIED |
| 8 | B06 | The key is an environment variable, not held in the database | `LTI_ENCRYPTION_KEY`, read from the server environment | VERIFIED |

## Row 2 is the one claim here we did not measure

Supabase's storage-layer encryption is the vendor's own statement. It is repeated
in our security document and labelled there as a vendor claim. Everything else in
this reel traces to our own code or its tests. The reel says "Supabase applies
AES-256 at the storage layer" rather than "we verified AES-256 at rest", because
we did not.

## Row 7 is a known transitional weakness, stated on camera

The decrypt path passes through any value that does not carry the `v1:` marker,
so a row written before the encryption shipped still reads in clear. B06 names
this out loud as a transitional allowance and says it should be removed once every
row has been rewritten, rather than leaving it implied.
