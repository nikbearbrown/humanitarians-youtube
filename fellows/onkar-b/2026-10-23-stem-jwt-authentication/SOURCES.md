# SOURCES — The Stateful Bottleneck

## Primary source

| Field | Value |
|---|---|
| Title | Week 8: Stateless Authentication (JWT) |
| Series | STEM AI Explainer (built on the `claude-stem` channel) |
| Supplied | 2026-10-22 |
| Author / narrator | Onkar Bhujbal (Humanitarians AI) |

## Beat ↔ scene map

| Scene | Beats |
|---|---|
| 1 — HOOK | B00 (+ B01, the mandatory BLUF the script does not carry) |
| 2 — THE JWT SOLUTION | B02 |
| 3 — DECODING THE TOKEN | BASK (ask) → B03 |
| 4 — MICROSERVICE SYNERGY | B04 |
| *(none in script)* | **B05 — FALSIFIABILITY, added** |
| 5 — SCAFFOLDED TASK & CLOSE | B06 · BHTF · BOUT |

## Claims taken from the source, verbatim or near-verbatim

| On screen / in narration | Source |
|---|---|
| "Hi, I am Onkar Bhujbal…" | Scene 1 VO, verbatim |
| `THE STATEFUL BOTTLENECK` | Scene 1 visual |
| "the server kept a persistent record of your session in its memory" | Scene 1 VO |
| `01 SESSION IDS (STATEFUL)` · `02 JSON WEB TOKENS (STATELESS)` | Scene 2 visual |
| "cryptographically signs a digital passport and hands it directly to you" | Scene 2 VO |
| "I verify this user is an admin, and this passport expires in thirty minutes" | Scene 2 VO |
| header / payload / signature; "the Signature is the cryptographic lock" | Scene 3 VO |
| "It just checks the math." | Scene 3 VO |
| fifty services verifying without a central database | Scene 4 VO |
| `TASK: Shift to stateless architecture.` | Scene 5 visual |

## THREE DELIBERATE CHANGES

### 1. A falsifiability beat was ADDED (B05)

The script runs HOOK → SOLUTION → DECODING → SYNERGY → TASK. There is no scene where the
idea breaks. Every other reel in both series has one, and the ai-explainer teaching arc
requires it.

The honest content is **revocation**: a session can be deleted server-side and the user
is out instantly; a signed token stays valid until `exp` precisely *because* nothing
looks anything up. Steal one and it works until the clock runs out. That is the real
price of statelessness, and the reel says so.

### 2. "Share the same secret key" is corrected (B04)

The script: *"as long as they all share the same secret key, they can instantly verify."*

Sharing one HMAC secret across N services means **any one of those services can MINT
tokens for all the others** — one compromised service forges admin everywhere. The
correct multi-service pattern is asymmetric signing (RS256/ES256): the issuer holds the
private key; verifiers hold only a public key, which can check a signature and cannot
create one. The reel teaches that and explains why, and B06's code shows `PUBLIC_KEY`
with `algorithms=["RS256"]` rather than a shared secret.

### 3. "Infinitely scalable" is scoped

Removing the session lookup removes one bottleneck. It does not remove rate limits,
network, or compute. The narration says fifty services verify independently without a
central database — which is true — and does not claim infinity.

## One addition inside Scene 3

The script lists the three parts but never says the payload is **base64url-encoded, not
encrypted**. That is the most common and most consequential misreading of JWTs: anyone
holding the token can read every claim in it, which is why secrets must never be put in
a payload. B03 shows it and the narration states it.

## Illustrative

The token string in B03 is a constructed example, not a real signed token. No latency,
throughput or scale figure appears anywhere — the script reports none.

## Narrator

First person, Onkar Bhujbal. Kokoro `am_onyx` is a **synthetic read of the author's own
script**, not a voice clone. The script's sign-off still reads "Liam, …"; per the
author's standing instruction this reel signs off **"Onkar Bhujbal, for Humanitarians
AI."**

## Build mode

Built **straight to `./art final`** — no review cut. No beat chip and no timecode is ever
drawn, and GATE V runs on both aspects (the `--review` path skips the gate entirely).

## Components — zero new, one prop

| Scene | Component |
|---|---|
| 1 · 3-ask · handoff | `ClaudeComposerAsk` (+ `916`) |
| BLUF | `BrutalistHesitantWriter` (+ `916`) — fontSize 92 |
| 2 | `ThreeStageBand`, two stages |
| 3 | `GuardrailCompare` — passing stamp |
| 4 | `ThreeStageBand` with **`connectors: false`** (new prop) |
| 4b | `ThreeStageBand` in failure mode (`failIndex: 1`) |
| 5 | `ClaudeCodeBeat` · outro `HaiTitleOutro` |

The `connectors` prop exists because Scene 4's claim is that the services verify
**independently**. Drawing connectors between them would assert a pipeline — the exact
thing the beat denies. Defaulted to `true`, so every earlier reel renders unchanged.
