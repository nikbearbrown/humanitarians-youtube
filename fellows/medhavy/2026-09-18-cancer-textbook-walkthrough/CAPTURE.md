# CAPTURE.md — claude-liam-medhavy-cancer-textbook-walkthrough

## Source
- Hub repo `books/medhavi-hub` at `efcc3f5217d9c338e7e7d7a0bfb719c4b339bd44`; `build_id` = SHA-256 of `git archive HEAD` = `6a566cb528d17dbb8cee4a181f64b9f5cb101c66b3f054d040f0fa4a8ea83dff`.
- Sites: `https://hub.medhavy.com` (hub) and `https://cancer.medhavy.com` (Cancer Biology and Therapeutics; Fumadocs, per `medhavy_documentation/medhavi-cancer-textbook/ARCHITECTURE.md`).

## Tenant and privacy
- Production, **redacted-live**. Session = Bear's own admin account saved once by a human (`scripts/save_session.py`, outside the reel). The agent typed no credentials; sign-in and sign-up pages were captured signed out (`--no-session`) and untouched.
- Mask: emails → `learnerN@example.edu`, `CLS-` codes → `CLS-XXXXXX` everywhere; person-name masking only on the hub host (the book page has no user lists, and name masking there renamed the sidebar title in a first run, which was discarded). Zero raw emails/codes at every step (`capture/redaction.jsonl`).
- The book's AI panel shows a "U" avatar and clock times, no name. The hub header shows Bear's own name by design.

## Captures
- `run-signin.mp4` — signed-out, 33 s: landing, `/sign-in`, `/sign-up`.
- `run-book.mp4` — signed-in hub tab, 138.6 s (records for the whole session).
- `run-book-p2.mp4` — the textbook tab opened by the Open Textbook button (Playwright records each page separately), 124.8 s; starts 13.77 s into the session. All book beats are cut from it.
- Method `scripted-browser`: Chromium headless, 1600×900 CSS at DPR 2.4 = native 3840×2160, 30 fps transcode. Action logs `capture/run-*-actions.jsonl`; step plans `capture/plan-*.json`.
- The four tutor questions were real requests answered by the site (its own OpenAI-backed tutor); answers are the site's, unedited.

## Limits
- Student dashboard tiles (pending / approved / can request) not filmable from an admin account (`/dashboard` → `/admin`). Described from `DEVELOPER.md` §9 and said as such.
- One chapter (5.2) walked; the book has 37 chapters. Glossary hover popups and the Feedback button not exercised.
- Unauthenticated GETs to the textbook sites 307 back to the hub with a `localhost` `blocked_url` (seen 2026-09-17); through the signed-in hub button the handoff worked, so that earlier observation is about the unauthenticated path only.
