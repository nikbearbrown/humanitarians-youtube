# FACTCHECK — Claude, Signed. (Chapter 7 — Facts: Check a Claim, Record It, Sign It)

Source: `ai1-cli/chapters/07-facts-check-a-claim-record-it-sign-it.md` (read
in full), cross-checked against `ai1-cli/research/07-facts-check-a-claim-record-it-sign-it.md`
and the live `ai1-cli/facts/facts.json`.

| # | Claim | Tag | Note |
|---|---|---|---|
| 1 | *Mata v. Avianca, Inc.* (S.D.N.Y., 22-cv-1461, June 2023) — a lawyer filed a brief with six invented court cases; the judge fined him; the fake cases cited other fake cases | Cited | Chapter footnote [^avianca]; a real, widely reported case |
| 2 | `facts.json` entries carry a claim, evidence (source/URL/date/supports-refutes), a source tier (trusted/solid/low), and a `verified` flag only a human can flip | General/stable | Chapter body + research doc §A, pointing to `facts/facts_store.py` |
| 3 | New facts enter `verified: false`; verified facts are append-only; consensus is derived from evidence, never hand-set | General/stable | Chapter's "three rules," reused verbatim; matches `facts/facts_store.py`'s stated behavior (`make_fact`, `record_evidence`, `recompute_consensus`) per the research doc |
| 4 | The Rosser Reeves USP worked example (`Reality in Advertising`, Alfred A. Knopf, 1961) is a **real** entry in this repo's own `facts.json`, `verified: false` | Cited, verified directly | Confirmed by reading the live `ai1-cli/facts/facts.json` in this session — the "Rosser Reeves" canonical text is present verbatim, exactly as the chapter prints it |
| 5 | GATE 0 and GATE 1 were signed with the same human-attestation mechanism now used for facts | General/stable | Chapter's own cross-reference to its earlier phase gates |
| 6 | The chapter's own "what can go wrong" table (unsourced claim, signing without being sure, disagreeing sources, editing a verified fact) | Cited | The chapter's own table, used verbatim |

## Explicitly excluded

- No claim that this session actually ran `facts/facts.py lookup/record` or
  `scripts/verify.py sign` against the live repo — the video narrates the
  chapter's method and its own real worked example, not a fresh run
  performed this session.
- No benchmark numbers, pricing, or named-product claims beyond the book's
  own tooling (`facts.json`, `facts.py`, `verify.py`) and the one named
  legal case the chapter itself cites.
