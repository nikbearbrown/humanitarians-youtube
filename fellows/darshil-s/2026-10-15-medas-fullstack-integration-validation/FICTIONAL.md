# Frictional Log — 2026-10-15

**Learnings:** Cross-origin resource sharing (CORS) between two independently-deployed Cloud Run services; the difference between a build-time environment variable and a runtime one, and why that matters for pointing a frontend build at the correct backend; tracing a browser-visible error back to its true root cause instead of its surface symptom.

**Implemented work:** Verified the staging frontend's build-time configuration correctly targets the staging backend, confirmed the CORS boundary between the two services is configured correctly, and ran a full regression pass across core user flows against the live staging backend.
