# FACTCHECK — vox-channel-reset

Source: `computational-skepticism-for-ai/chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| Session-boundary attack | Attack that succeeds by opening a new channel, resetting the agent's trust context and prior defensive safeguards | Lines 238, 252 |
| Displayed identity | The name/label visible in a chat interface — not verified against an authoritative identity source | Line 252 |
| Verified identity | Identity grounded in infrastructure that persists across sessions — e.g. cryptographic credentials | Line 252 |
| Trust context | The accumulated interaction history, suspicious-behavior flags, and prior trust judgments within a session — does not transfer across channel boundaries | Lines 238, 252 |
| Case #8 | Discord channel-boundary identity attack on agent Ash (owned by Chris): impersonator caught in public channel, succeeded in private channel | Lines 236–252 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | Attacker changes display name to owner's name; agent correctly catches user-ID mismatch; attacker opens new private channel; agent has no memory of prior flags; spoofed identity accepted | Lines 236–238 | PASS |
| B04 | Agent's suspicion lived in session context; new channel starts fresh; no mechanism to carry trust judgments across session | Lines 238, 252 | PASS |
| B05 | Agent uses displayed identity as primary authority signal; discrepancy visible in same channel, invisible across channels | Lines 236, 252 | PASS |
| B07 | User ID vs display name discrepancy caught in ch1; fresh channel with only display name — no basis to suspect | Lines 236, 238 | PASS |
| B08 | Quote verbatim | Line 252: exact | PASS |
| B09 | Fix: identity verification must persist across channel boundaries (infrastructure, not session context) | Line 252 | PASS |
| B10 | Quote verbatim | Line 252: first sentence, exact | PASS |
| B11 | Validate across channel boundaries; test the same attack in a new channel | Lines 316, 325 | PASS |

## B12 — THE EXAMPLE beat (illustrative)

| Claim | Status |
|---|---|
| Support agent handles ticket #47 — export request from display name "Sarah Chen" | illustrative — made-up instance |
| Email address in request doesn't match account on file — agent flags it | illustrative |
| Attacker submits ticket #48 — fresh session, same display name, different submission path | illustrative |
| Agent has no record of ticket #47 — export runs | illustrative |

All identifiers, ticket numbers, and scenario details in B12 are invented and illustrative. They demonstrate the channel-boundary reset mechanism (per-session context cannot carry over trust judgments) without claiming any specific system or platform.

## VERDICT: PASS
