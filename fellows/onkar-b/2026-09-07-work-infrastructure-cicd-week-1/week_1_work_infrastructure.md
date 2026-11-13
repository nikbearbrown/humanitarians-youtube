# Week 1: Infrastructure & CI/CD — Video Script

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A terminal snaps in showing a server crash.
`Error: Port 8000 already in use.`
**ON SCREEN:** `ISOLATE OR DIE`
**VO:**
I am Onkar Bhujbal, a software engineer. Building an AI validation pipeline directly on your host machine is a guarantee of failure. Dependencies clash, environments break, and deployments stall. This week, we laid the foundation for the Provenance Gatekeeper by containerizing our environment and automating our build process.

### SCENE 2 — THE FRAMEWORK
**VISUAL** — Two Brutalist text boxes snap in.
`01 DOCKER ISOLATION` 
`02 GITHUB ACTIONS`
**VO:**
Our infrastructure relies on two pillars. First, a Dockerized FastAPI backend. This ensures the Gatekeeper runs in strict, mathematical isolation, regardless of the host operating system. Second, GitHub Actions. No code enters the main repository without automatically triggering a strict deployment governance pipeline that checks our manifest and enforces structural integrity.

### SCENE 3 — WORKED EXAMPLE
**VISUAL** — Split frame.
**TOP:** A git push command executing.
**BOTTOM:** GitHub Actions console lighting up green `✓ Build Success`
**VO:**
Here is the CI/CD pipeline in action. When an engineer commits an update to the evaluation logic, they push it to the remote branch. GitHub Actions intercepts the push, instantly spins up an ephemeral Ubuntu runner, builds the Docker image from scratch, and verifies the application state. If it compiles, it passes.

### SCENE 4 — FALSIFIABILITY
**VISUAL** — A Dockerfile flashes red on screen.
**ON SCREEN:** `CONFIGURATION DRIFT`
**VO:**
Where does this architecture fail? Silent configuration drift. If your Dockerfile pulls the `latest` version of a Python package instead of a strictly pinned version, your container might build perfectly today and crash catastrophically tomorrow when the underlying library pushes a breaking change. 

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to a terminal command.
`docker run -d -p 8000:8000 gatekeeper-api`
**VO:**
Audit your infrastructure. Write a Dockerfile that spins up a basic FastAPI server, map the ports, and attempt to run it. If you can't tear down and rebuild your entire environment in under ten seconds, your pipeline is too fragile.
Liam, for Onkar Bhujbal and Humanitarians AI.