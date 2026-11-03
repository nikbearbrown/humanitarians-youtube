# SOURCES.md — claude-liam-medhavy-hub-walkthrough

All claims trace to one of these; see `FACTCHECK.md` for the per-beat map.

## Primary
- **medhavi-hub repository**, commit `efcc3f5217d9c338e7e7d7a0bfb719c4b339bd44` (2026-09-17)
  - `README.md` — features, architecture diagram, data ownership, naming note (Medhavy vs Medhavi)
  - `DEVELOPER.md` — §3 roles and admin lock, §4 access tokens, §5 core domain logic and access oracle, §8 API reference, §9 frontend map, §10 concept-map lifecycle, §11 analytics (PostHog + first-party), §16 known issues
  - `docs/concept-map-editor.md`, `docs/creating-a-new-textbook.md`
  - `Feature-Testing-Manual/Admin-Features-Testing.md`, `Student-Features-Testing.md`
- **Live site** `https://hub.medhavy.com` admin, captured 2026-09-17 (`capture/run-05.mp4`, `capture/run-05-actions.jsonl`), signed in as Bear's own admin account; names, emails and invite codes masked in the page before recording (`CAPTURE.md`).
- **Textbook-site reachability probe** 2026-09-17: `curl -I` on electron-microscopy / quantumv1 / physics `.medhavy.com` → HTTP 307 to `hub.medhavy.com/dashboard?blocked_url=https://localhost:300x/` (basis for the Verdict's open defect).

## Toolkit
- `brutalist.art/skills/make/medhavy-walkthrough/` (capture driver, mask, evidence check, media prep, SRT/description builder)
- `brutalist.art/skills/make/riff/SKILL.md`, `ai-explainer`, `OUTRO-LOCK.md`

## Not used
No stock footage, no generated imagery, no paid models, no third-party recordings.
