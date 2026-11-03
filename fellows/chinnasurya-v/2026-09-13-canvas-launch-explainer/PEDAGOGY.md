# GATE P — How a Canvas Launch Works

**The one idea.** In LTI 1.3 the trust does not come from the launch. It comes
from a key registration done in advance; the launch is only where that trust
gets spent.

| Beat | The viewer should be able to say afterwards |
|---|---|
| B00 | this is about what happens between the click and the tool knowing me |
| B01 | the tool is a separate app; it can't just believe the browser |
| B02 | both sides register endpoints and IDs before any launch happens |
| B03 | each side signs with a private key and publishes a public one — no shared password |
| B04 | Canvas calls login; the tool stores a random state and nonce first |
| B05 | the token comes back as a form POST, not in the URL |
| B06 | the token carries identity, role, course, content pointer and protocol fields |
| B07 | verification is signature + iss + aud + exp, with the algorithm pinned |
| B08 | state and nonce are consumed, so a launch can't be replayed |
| B09 | role is matched to an official list; access is decided server-side; no grade/roster scopes |
| B10 | register, sign, verify, spend |

**Register check.** Second person, plain English, no vendor pitch. Protocol
terms (`state`, `nonce`, JWKS, RS256) are named and then explained in the same
sentence. No term is used before it is introduced.

**Honesty check.** Every claim traces to a row in the script's appendix, sourced
to the operator's own security review, FERPA data-flow doc, or architecture
summary. One claim — that `response_mode=form_post` keeps the token out of
browser history and server logs — is the standard rationale for that parameter,
stated as mechanism, not as a measurement of this system. No production claims;
every verified figure was measured on the dev environment. No individual, no
hostname, no key material appears.

**Weakest beat.** B06. Ten claim rows is the densest frame in the reel and the
narration lists them faster than a first-time viewer can absorb. It is defensible
because the visual holds the list on screen after the narration moves on, but if
a beat is going to lose someone, it is this one.

**Gate status.** Narration is the operator's own approved text — reviewed and
signed off in conversation before this build — and Kokoro synthesis is free, so
audio was generated with `--no-gate`. This file remains unsigned by a human.

VERDICT: PENDING — human signature required
