# Week 8: API Security & JWT Authentication

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A terminal window shows an anonymous script rapidly pinging the `/verify` endpoint. A red `401 UNAUTHORIZED` shield slams down, blocking the requests.
**VO:**
Hi, I am Onkar Bhujbal. Our Provenance Gatekeeper can now intercept AI hallucinations and automatically run regression tests in a CI/CD pipeline. But up until now, the API was completely open. Anyone with the URL could bombard our endpoint, poison our logs, and exhaust our vector database. This week, we are locking down the perimeter with OAuth2 and JSON Web Tokens.

### SCENE 2 — THE BCRYPT PIVOT
**VISUAL** — Code block showing `passlib` importing `bcrypt`. The screen glitches with a red error: `ValueError: password cannot be longer than 72 bytes`.
**VO:**
Security implementations rarely go smoothly. We initially tried to use the standard Python `passlib` library to hash our passwords, but immediately hit a wall. Because we are running a modern Python 3.13 environment, `passlib` triggered a fatal 72-byte truncation bug. To fix it, we ripped out the deprecated library entirely and wrote a custom, lightweight wrapper using raw `bcrypt`.

### SCENE 3 — THE TOKEN EXCHANGE
**VISUAL** — An animated flow diagram. A user sends a username and hashed password to `/token`. The server replies with a glowing cryptographic string (JWT). 
**VO:**
With the hashing fixed, we secured the `/verify` route. Now, when a system tries to access the Gatekeeper, it must first hit the token endpoint with valid credentials. If they match, the server generates a time-limited JSON Web Token—a cryptographic passport that grants temporary access to the microservice.

### SCENE 4 — ADVERSARIAL AUTHENTICATION
**VISUAL** — Dual terminal setup. Left terminal: FastAPI server running. Right terminal: `stress_test.py` executing. The first request fails with `401`. The script authenticates, gets the token, and the rest of the payloads process successfully.
**VO:**
To prove the architecture works, we updated our automated stress test. If it tries to fire adversarial payloads blindly, the server immediately drops the connection. The test script must now actively negotiate a Bearer token before it is permitted to execute its normalization checks. The gate is officially closed.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Implement stateless authentication.`
**VO:**
Never leave a microservice exposed, even internally. Implement stateless authentication so your infrastructure protects itself by default.
Liam, for Onkar Bhujbal and Humanitarians AI.