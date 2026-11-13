# Frictional log — Stateless Authentication

## 2026-10-23 — the project update, in two aspect ratios

**What I was working on.** A STEM explainer detailing the mechanics and benefits of JSON Web Tokens for microservices.

**What I tried, and what I expected.** 
- I initially tried to explain the exact cryptographic hashing math behind the JWT signature (HMAC SHA256) to make it highly technical.

**Where it resisted, and what I did next.** 
- Explaining the math bogged down the script and made it impossible to hit the 2:45 runtime target. It also distracted from the actual architectural benefit, which is *scalability*.
- I pivoted to a "digital passport" analogy. Instead of explaining how the cryptography works, I focused on what the cryptography *enables*: allowing multiple independent servers to verify a user without talking to a centralized database.

**What Claude contributed, and what I did with it.** 
- Mine: The focus on the Header, Payload, and Signature breakdown.
- Claude's: The emphasis on "The Stateful Bottleneck" in Scene 1. Framing the problem around central server memory exhaustion made the JWT solution feel much more urgent and logical.

**What I understand now, and what I still do not.**
- Understood: When explaining backend architecture, visualizing the data flow (the token moving between distributed services) is vastly more effective than explaining the underlying math algorithms.