# Week 8: Stateless Authentication (JWT)

**Series:** STEM AI Explainer
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A graphic shows a central server buckling under the weight of thousands of active user sessions.
**ON SCREEN:** `THE STATEFUL BOTTLENECK`
**VO:**
Hi, I am Onkar Bhujbal, and this video is about why modern microservices do not remember who you are. Traditionally, when you logged into a website, the server kept a persistent record of your session in its memory. But in an era of distributed AI agents and microservices scaling to millions of requests, remembering every single active user creates a massive, expensive bottleneck. 

### SCENE 2 — THE JWT SOLUTION
**VISUAL** — Two mono-text boxes snap in.
`01 SESSION IDS (STATEFUL)` 
`02 JSON WEB TOKENS (STATELESS)`
**VO:**
The solution is stateless authentication, most commonly implemented using JSON Web Tokens, or JWTs. Instead of the server storing a record of your login, the server cryptographically signs a digital passport and hands it directly to you. It says, "I verify this user is an admin, and this passport expires in thirty minutes."

### SCENE 3 — DECODING THE TOKEN
**VISUAL** — A long, scrambled JWT string splits into three distinct colored sections: Header, Payload, and Signature. 
**VO:**
A JWT consists of three parts. The Header defines the algorithm. The Payload contains the claims—like your username and role. And the Signature is the cryptographic lock. Because the token is signed with a secret key that only the server knows, the server doesn't need to look up your session in a database. It just checks the math. If the math verifies, you are allowed in.

### SCENE 4 — MICROSERVICE SYNERGY
**VISUAL** — An AI Agent sends a JWT to three different microservices simultaneously. They all grant access instantly without talking to a central database.
**VO:**
This fundamentally changes system architecture. You can have fifty different microservices running on fifty different servers, and as long as they all share the same secret key, they can instantly verify an AI agent's JWT without ever communicating with a central database. It is infinitely scalable.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Shift to stateless architecture.`
**VO:**
Stop overloading your databases with session checks. Use JSON Web Tokens to cryptographically distribute trust across your architecture.
Liam, for Onkar Bhujbal and Humanitarians AI.