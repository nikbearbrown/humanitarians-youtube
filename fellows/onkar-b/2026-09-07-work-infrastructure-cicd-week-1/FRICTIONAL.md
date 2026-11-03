# Frictional log — Infrastructure & CI/CD

## 2026-09-07 — the project update, in two aspect ratios

**What I was working on.** A project update explainer on Dockerizing the FastAPI backend and setting up GitHub Actions, cut at both 16:9 and 9:16, opening on the verbatim line *"Hi, I am Onkar Bhujbal, and this video is about..."*

**What I tried, and what I expected.**
- I built the Docker image using `ubuntu:latest` and expected it to deploy flawlessly via GitHub Actions.
- I assumed the local environment would mirror the CI/CD pipeline exactly.

**Where it resisted, and what I did next.**
- Silent configuration drift caused local builds to pass but GitHub Actions to fail during the manifest checks. 
- Fixed this by strictly pinning dependency versions in the `requirements.txt` and locking the base image version rather than using `latest`.

**What Claude contributed, and what I did with it.**
- Mine: The Dockerfile setup, GitHub Actions YAML, and API routing.
- Claude's: Writing the beat sheet formulation and identifying the `metadata.aspect` compiler bug in the 9:16 framing.

**What I understand now, and what I still do not.**
- Understood: If you cannot tear down and rebuild your entire environment in under ten seconds, your pipeline is too fragile.
- Not resolved: Publishing to YouTube is deferred pending setup of the separate `brutalist.yt` credentials.