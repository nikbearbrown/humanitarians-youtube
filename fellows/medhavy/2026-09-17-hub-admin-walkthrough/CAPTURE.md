# CAPTURE.md — claude-liam-medhavy-hub-walkthrough

## Source
- Repo: `books/medhavi-hub` at commit `efcc3f5217d9c338e7e7d7a0bfb719c4b339bd44`
- `build_id` = SHA-256 of `git archive --format=tar HEAD` = `6a566cb528d17dbb8cee4a181f64b9f5cb101c66b3f054d040f0fa4a8ea83dff`
- Site: `https://hub.medhavy.com` (production). Next.js 16 App Router, Clerk identity, Supabase data, PostHog analytics (per `DEVELOPER.md`).

## Tenant and privacy
- **Tenant:** production, **redacted-live**. The `brutalist` walkthrough account could not sign in; the capture session is Bear's own admin account, saved once by a human via `scripts/save_session.py` to `~/.medhavy-walkthrough/` (outside the reel, mode 600). No credential was typed by the agent.
- **Redaction method:** DOM text substitution at capture time (`capture_admin.py` MASK). Every email is rewritten to `learnerN@example.edu`; every `CLS-` invite code to `CLS-XXXXXX`; the display name in the same card, and any Title-Case name inside list/row/card containers, is rewritten to `Learner N`. Role words, headings, textbook titles, URLs, counts, and the signed-in admin's own header name (`Nik Bear`) are kept. Per-step counts and a per-step count of raw emails still visible are in `capture/redaction.jsonl`; the driver discards a run if any raw email is visible at any step.
- **Known residue:** no leaks observed in run-05 frames inspected (Users, Classes, Analytics overview). Cosmetic over-masking only: a split instructor name shows two adjacent `Learner N` labels, and one assigned-textbook title that matches the person-name pattern is masked. The signed-in admin's own display name appears in the header and Settings by design.
- **Discarded:** run-01 (first attempt) leaked unmasked names because the mask installed before `document.body` existed; its files were deleted and are not evidence. A later run-01 with a working mask was superseded by run-02 (longer dwell), run-02 by run-03 (DPR 2.4 for legibility and frame fill), run-03 by run-04 (CLS- invite codes masked as CLS-XXXXXX), and run-04 by run-05 (mask narrowed to the name block beside each email plus full person names, so class titles, textbook names and date labels are no longer over-masked); all were removed.

## Capture method
- `scripted-browser`: Playwright Chromium, headless, CSS viewport 1600×900 at `deviceScaleFactor` 2.4 (physical 3840×2160, native render, not an upscale; pilot edge-variance 984 vs 1037 for a native screenshot), `recordVideo` 3840×2160, transcoded losslessly-enough (libx264 crf 14, 30 fps, no audio) to `capture/run-05.mp4`.
- Step plan: `capture/plan-run-05.json`. Action log: `capture/run-05-actions.jsonl` (`t_ms`, action, selector/text, URL after). Screenshots per tab: `capture/run-05-*.png`.
- Real clicks through the normal UI; no API calls, no cookie edits, no DB seeding. Tab switches use the accessible button name (exact, then prefix fallback because analytics tabs carry a count).
- The hub has no meaningful audio; narration is the only voice.

## Coverage limits (see coverage.json)
- Single-account admin run. Student and instructor screens are `planned`-status rows with the reason "not shown, single-account run", not faked.
- The textbook handoff (`open-textbook`) is stopped at the hub: all three registered textbook sites answered a plain GET with a 307 back to `hub.medhavy.com/dashboard?blocked_url=https://localhost:300x/` on 2026-09-17, so the protected page load could not be shown.
- Requests queue was empty at capture time; the approve/deny action is described from source (`DEVELOPER.md` §5.3, §8.3), not demonstrated.
