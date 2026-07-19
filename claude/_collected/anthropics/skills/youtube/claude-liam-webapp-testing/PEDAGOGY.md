# PEDAGOGY — claude-liam-webapp-testing

Skill: webapp-testing
Register: Teardown (skill-teardown modifier)
Audience: Claude / developers

## What the skill does
Playwright-based reconnaissance-and-action toolkit for testing local web applications. Two-branch decision tree: static HTML (read file, write script) vs dynamic webapp (use with_server.py helper, write Playwright separately). Core pattern: navigate → wait for networkidle → screenshot/inspect → identify selectors → act.

## Learning objective
Viewer understands: (1) the two-branch decision tree, (2) the networkidle requirement before DOM inspection, (3) how with_server.py decouples server lifecycle from automation logic, and (4) the reconnaissance-then-action pattern.

## Teardown structure
- B00: cold open — Playwright, decision tree, networkidle rule
- B01: decision tree anatomy — static HTML path + dynamic webapp path + recon loop
- B02: with_server.py patterns + Playwright best practices
- B05: gets-right / bites teardown
- BVDT: verdict
- BHTF: handoff
- BOUT: outro

## Key concepts for viewer
- Static HTML: read → selectors → file:// URL
- Dynamic webapp: with_server.py manages lifecycle; Playwright script is pure automation
- networkidle wait is mandatory before DOM inspection on dynamic apps
- Reconnaissance: screenshot first, then act

## VERDICT: PASS
No paid spend required. Free Kokoro pipeline. Skill content is teachable as a standalone unit.
