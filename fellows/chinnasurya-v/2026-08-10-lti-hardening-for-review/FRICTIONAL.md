# Frictional log — LTI hardening for the security review

Dated entries, appended as the work happened. Earlier entries are never rewritten.

## 2026-08-05 — auditing my own code against the spec

What I expected: a short pass to confirm the integration matched LTI 1.3 before
review. What happened: the role check was the first thing I read and the first
thing that was wrong. It tested whether an accepted role word appeared anywhere in
the role string. IMS role URNs carry their meaning in the final segment, so a
string ending in something else can still contain an accepted word earlier on. I
had written that check myself and read past it for weeks.

What I did: rewrote it to split on `[/#:]`, take the last segment, and compare that
against an allow list. Then wrote the privilege-escalation inputs first and made
them fail before I made them pass.

## 2026-08-07 — encryption, and what it does not protect

What I expected: enabling encryption at rest on the database would be enough to
answer the review question about stored credentials. What resisted: it is not the
same threat. Storage encryption protects the disk. It does not protect a secret
from a query the database is required to answer, which is the case that matters
when a service role is compromised.

What I did: AES-256-GCM in the application above the database's own layer, with the
format versioned as `v1:` from the start so a future rotation does not have to
guess what it is reading.

Claude's contribution: drafted the envelope helper. I changed the format to carry
the version prefix and rejected its first test set, which only covered the happy
path. The tampered-tag and truncated-IV cases are mine.

## 2026-08-12 — the endpoint I deleted instead of fixing

A legacy launch endpoint decoded the `id_token` and used its claims without
verifying the signature. The instinct was to add verification. I checked callers
first and found none, so I deleted it. A second launch path that nothing uses is a
second path to keep correct forever.

## 2026-08-14 — what is still open

- The dormant self-register generator still composes all four gradebook and roster
  scopes in its payload, even though the scopes were removed from the live
  registration. It is behind a flag and unreachable, which is why it survived this
  pass, but a flag is not a guarantee.
- Row level security is verified on the dev database only. The production database
  is not mine to touch until the developer key is issued.
