# ENCRYPTED TWICE
### Why a stored credential gets a second layer the database does not provide

Single-topic explainer. Source: `medhavi-hub/lib/lti-crypto.ts`,
`tests/lti-crypto.test.ts`, `lib/lti-v1-oauth.ts`, and
`medhavy-lti-security-review.md`.

---

## ART DIRECTION

**Script-native brutalism.** Same system as the rest of the series.

| Role | Value |
|---|---|
| ground | `#0A0A0A` |
| paper | `#F2F0EB` |
| signal | `#E8452C` |
| mute | `#6B6B6B` |

Four colours. Never a fifth.

**Layout** — single column, stacked. Every beat must read at 16:9 and at 9:16
without a second layout.

**Hard rules**

- Hard cuts only. `border-radius: 0`.
- No screenshots, no logos, no photography.
- **No key material, no real ciphertext, no hostname.** The format string is the
  shape only.
- Field names appear in mono, spelled as the code spells them.

---

## SCENES

### B00 — INTRO · title card

> Hi, I am Surya, and this video is about why a secret sitting in our database
> gets encrypted a second time, by us, after the database has already encrypted
> it.

**Shot** — TITLE. "ENCRYPTED TWICE" flush left; signal rule above; mono subtitle
`CREDENTIALS AT REST`.

---

### B01 — WHAT IS ACTUALLY STORED

> The hub holds credentials for every platform it trusts. A signing key for the
> tool, and for older platforms a shared secret. They sit in a column, in
> Postgres, like any other value.

**Shot** — One bordered row, full width: `lti_platform_registrations` in mono,
and beneath it two mute field names: `rsa_private_key` · `shared_secret`.

---

### B02 — THE DATABASE ALREADY ENCRYPTS

> And the database does encrypt its storage. Supabase applies AES-256 at the
> storage layer. So the honest question is why bother doing it again.

**Shot** — A full-width block in mute: `STORAGE LAYER - AES-256`. Beneath, in
signal, the question: `SO WHY AGAIN?`

---

### B03 — WHAT STORAGE ENCRYPTION PROTECTS

> Because storage encryption answers exactly one threat. Somebody walks off with
> the disk. It does not help if a query runs. Anything that can read the table
> reads the value in clear, because decryption already happened underneath it.

**Shot** — Two rows, stacked, appearing 4 frames apart. First in mute:
`STOLEN DISK - PROTECTED`. Second, filled signal: `A QUERY THAT RUNS - NOT
PROTECTED`.

---

### B04 — THE SECOND LAYER

> So the value is encrypted before it is ever written, with a key the database
> does not hold. AES-256-GCM, in the application. What lands in the column is
> four fields joined by colons: a version marker, the initialisation vector, the
> authentication tag, and the ciphertext.

**Shot** — One mono line, full width, the four parts separated:
`v1 : iv : tag : ciphertext`. Each part labelled beneath in mute as it appears,
3 frames apart: `VERSION` · `INITIALISATION VECTOR` · `AUTH TAG` ·
`THE SECRET ITSELF`.

---

### B05 — WHY GCM AND NOT PLAIN ENCRYPTION

> GCM is the part worth naming. It does not only hide the value, it signs it. If
> one byte of that ciphertext is altered, decryption does not return wrong data.
> It fails. That difference matters: a credential you cannot trust is more
> dangerous than one you cannot read.

**Shot** — Two outcomes stacked. In mute: `ENCRYPTION ALONE - TAMPERED DATA
DECRYPTS TO GARBAGE`. In signal, filled: `AUTHENTICATED - TAMPERED DATA DOES NOT
DECRYPT AT ALL`.

---

### B06 — THE MIGRATION PROBLEM

> There was already data in that column when this shipped. So the decrypt path
> checks the format first. A value starting with the version marker is decrypted.
> Anything else is passed through unchanged, as a value written before the
> encryption existed. That is a deliberate transitional allowance, and it is the
> thing to remove once every row has been rewritten.

**Shot** — A two-branch decision, drawn as two full-width rows under a single
mono condition `isEncrypted(value)`: `YES - DECRYPT` in signal, `NO - PASS
THROUGH AS LEGACY PLAINTEXT` in mute. Caption beneath, in signal: `TRANSITIONAL -
REMOVE WHEN THE LAST ROW IS REWRITTEN`.

---

### B07 — OUTRO

> One layer for the disk, one layer for everything above it, and a key held
> outside the database for the second one. The second layer is not distrust of
> the database. It is the recognition that the database cannot defend a secret
> from a query it is required to answer.

**Shot** — Two full-width rows: `STORAGE LAYER - THE DISK` in mute, and
`APPLICATION LAYER - EVERYTHING ABOVE IT` in signal. Hard cut to the title
restated.

---

## APPENDIX — CLAIMS AND SOURCES

| # | Beat | Claim | Source |
|---|---|---|---|
| 1 | B01 | The hub stores a signing key and, for LTI 1.1 platforms, a shared secret | `02_lti_multi_tenant_schema.sql` `rsa_private_key`; `03_lti_v1_credentials.sql` `shared_secret` |
| 2 | B02 | Supabase applies AES-256 at the storage layer | Supabase platform documentation, cited in `medhavy-lti-security-review.md` and not independently verified by us |
| 3 | B03 | Storage-layer encryption does not protect a value from a query that runs | Property of at-rest encryption, stated as mechanism |
| 4 | B04 | Stored credential values carry an application-layer AES-256-GCM layer | `lib/lti-crypto.ts` — `encryptSecret` / `decryptSecret` |
| 5 | B04 | The stored format is `v1:<iv>:<tag>:<ciphertext>` | `lib/lti-crypto.ts`; asserted in `tests/lti-crypto.test.ts` |
| 6 | B05 | GCM is authenticated, so tampered ciphertext fails to decrypt rather than returning wrong data | Property of AES-GCM; asserted in `tests/lti-crypto.test.ts` |
| 7 | B06 | Values not carrying the version marker are passed through as legacy plaintext | `lib/lti-crypto.ts` `isEncrypted` guard on the decrypt path |
| 8 | B06 | The key is an environment variable, not held in the database | `LTI_ENCRYPTION_KEY`, read from the server environment |

**Row 2 is the one claim in this reel we did not measure.** Supabase's
storage-layer encryption is the vendor's statement, repeated in our security
document and labelled there as a vendor claim. Everything else traces to our own
code or its tests.

**Invented values: none.** No key material, no real ciphertext and no IV appears.
The format line is the shape only.
