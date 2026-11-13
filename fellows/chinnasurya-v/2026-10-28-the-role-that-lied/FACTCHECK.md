# FACTCHECK — The Role That Lied

Every claim and the source it came from. **Invented values: none.** The strings
shown in B03 and B06 are copied from the test file.

| # | Beat | Claim | Source | Status |
|---|---|---|---|---|
| 1 | B01 | The launch token carries a `roles` claim, as a list of URN identifiers | LTI 1.3 specification (IMS Global); `lib/lti-auth-bridge.ts` reads `roles` from the validated claims | VERIFIED |
| 2 | B03 | A substring check matches strings whose final segment is not an accepted role | `tests/lti-roles.test.ts` — the three strings shown are literal test inputs asserted to return `student` | VERIFIED |
| 3 | B04 | The role identifier is the final segment after `/`, `#` or `:` | LTI 1.3 role vocabulary; `parseLTIRole` splits on `[/#:]` and takes the last element | VERIFIED |
| 4 | B05 | The fix splits, takes the last segment, lowercases and looks up an allow-list set | `lib/lti-v1-oauth.ts` `INSTRUCTOR_ROLES`; `lib/lti-auth-bridge.ts` `ADMIN_ROLES` and `INSTRUCTOR_ROLES` | VERIFIED |
| 5 | B05 | Unrecognised roles resolve to student | `parseLTIRole` returns `"student"` as its default | VERIFIED |
| 6 | B06 | The escalation strings are committed as test cases | `tests/lti-roles.test.ts`, the "fails closed on substring-escalation attempts" block | VERIFIED |

## Threat model, stated precisely

The `roles` claim arrives inside a platform-signed token, so **this is not a reel
about forging a token.** Signature verification covers that and is the subject of
a separate reel. What this change fixes is **misreading legitimate platform
input**: role vocabularies are extensible, platforms can define custom and
sub-roles, and a substring test cannot distinguish an accepted identifier from a
longer string that merely contains it.

The reel does not claim an exploit was observed in production. It claims the check
was asking the wrong question, which is what the test file records.

## Why this is safe to publish

The change shipped in
[`1fd8443`](https://github.com/Medhavy/medhavi-hub/commit/1fd8443) and its tests in
[`55e47ad`](https://github.com/Medhavy/medhavi-hub/commit/55e47ad). Nothing on
camera describes a live unfixed weakness. Two defects found during a later
re-audit are deliberately kept off camera and recorded in the project's research
plan instead, following the same practice as the earlier reels in this series.
