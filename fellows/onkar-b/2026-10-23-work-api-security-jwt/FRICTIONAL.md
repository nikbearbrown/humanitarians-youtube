# Frictional log — API Security & JWT

## 2026-10-23 — the project update, in two aspect ratios

**What I was working on.** Implementing OAuth2 JWT authentication for the FastAPI Gatekeeper.

**What I tried, and what I expected.** 
- I followed standard FastAPI security documentation, installing `passlib[bcrypt]` and `python-jose`, and configured the stress test to hit the endpoint. I expected a clean 401 rejection followed by a successful auth flow.

**Where it resisted, and what I did next.** 
- Two massive roadblocks. First, the FastAPI server crashed on startup with a `ValueError: password cannot be longer than 72 bytes`. This is a known, unpatched bug in `passlib` when running on modern Python 3.13 environments combined with the latest `bcrypt` binaries. I had to rip `passlib` out completely and write raw `bcrypt` wrapper functions in `auth.py`.
- Second, when I ran the stress test, I got a fatal `ConnectionRefusedError: [WinError 10061]`. I had forgotten that a test script cannot hit a local API if the local API isn't actually running. I solved this by utilizing a dual-terminal workflow: spinning up `uvicorn` in Terminal 1, and executing `stress_test.py` in Terminal 2.

**What Claude contributed, and what I did with it.** 
- Mine: The initial FastAPI OAuth2 scheme and the logic for the stress test payloads.
- Claude's: Diagnosing the exact cause of the `passlib` 72-byte truncation bug, providing the raw `bcrypt` replacement code to bypass the C++ compiler issues, and identifying the `WinError 10061` missing-server problem.

**What I understand now, and what I still do not.**
- Understood: Python's security ecosystem has fragile dependencies. If a wrapper library (`passlib`) is abandoned, you must bypass it and use the cryptographic primitives directly (`bcrypt`).