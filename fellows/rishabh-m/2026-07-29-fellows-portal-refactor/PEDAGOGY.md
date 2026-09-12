# PEDAGOGY — Fellows Portal, Refactored. (claude-hai cli-explainer)
# Auditor: Claude Sonnet 5 | 2026-07-29
# GATE P — this is a QUALITY gate, not a cost gate (Kokoro audio is free).
# Human sign-off required below before generate_audio_kokoro.py runs.

## What this reel is
A real build reel about `humanitarians_html`'s Fellows Portal: taking a
single-tier system (one shared `ADMIN_PASSWORD`, one growing dashboard file,
free-text project matching) to a three-role system (fellow / admin /
super-admin) via a two-boolean schema change, one unified session model, and
nav-level tier gating. Built from 10 real commits by the requester
(2026-05-28 to 2026-06-09) — commit list and diffs verified in SOURCES.md.

## Spine check (cli-explainer required spine)
- B00 INTRO — cold open, `ClaudeComposerAsk`, ask shown answered ✓
- B01 PROBLEM — stakes stated before any prompt (shared password, no tiers,
  monolithic file, typo-prone matching) ✓
- Cycle 1 (B02–B04): ASK → CODE → OUTPUT — schema + auth unification
- Cycle 2 (B05–B07): ASK → CODE → OUTPUT — sidebar split + dropdown fix
- Cycle 3 (B08–B11): CHANGE → CODE → OUTPUT×2 — nav-tier gating, shown as
  admin view (B10) vs super-admin view (B11) on the same component
- **THE REVISION LAW**: satisfied twice over (cycles 2 and 3 both revise
  cycle 1's artifact further) — exceeds the ≥1 minimum ✓
- B12 SUMMARY · B13 NEXT STEPS (HANDOFF) · B14 OUTRO (title restate) ✓

## THE ACTUAL-CODE LAW
B03, B06, B09 all quote real committed diffs, trimmed to the lines that
teach — no pseudocode:
- B03 → `dc81ddd` (schema), `a879e56` (auth unification)
- B06 → `30b5fe6` (dropdown replacing free-text match)
- B09 → `0e8dc55` (`DashboardNav` tier filter)
Each ASK plausibly generates the CODE shown, and each CODE plausibly produces
the OUTPUT shown. **SCORE: PASS**

## SHOW-DON'T-TELL / real capture (not a mockup)
B04, B07, B10, B11 are REAL Playwright screen recordings against the live
dev app, driven by the requester's own existing dummy accounts (fellow,
admin, super-admin) — not Remotion recreations, not stills. B10 vs B11 is
the same component (`DashboardNav`) rendered for two real accounts with
different `is_admin`/`is_super_admin` values — the tier difference is
genuinely demonstrated, not asserted. **Disclosure**: capturing B07 submits
one clearly-labeled test report ("TEST CAPTURE — automated screen
recording, ignore.") into the dev/test database via the fellow1 account —
flagged here per the requester's own confirmation that this DB is a
dev/test branch, not production.

## DOUBLE-CHECK LAW — corrections applied (full detail: SOURCES.md)
| Claim as first told | Verified reality | Fix applied |
|---|---|---|
| "Before this, the portal was just a login page" | Fellow auth, profile dashboard, and report submission already existed (built 2026-04-04, different author + Claude Opus, commits `c656c4c`/`0266add`) | Narration (B01) states what worked before and names the actual gap: no role tiering, one shared password |
| "A report upload folder was created for fellows" | Reports are markdown text submitted via a form — no file upload | Narration uses "report submission," never "upload" |
| Search scoped to `app/fellows` + `app/portal` only | Missed `app/admin/dashboard/`, `lib/admin-auth.ts`, `lib/fellow-auth.ts` — where the real tier/auth work lives | Broadened to all `RishabhHM` commits since 2026-05-25 repo-wide before drafting the spine |

## Pragmatist register check (required when-NOT-to diagnostic)
B12 SUMMARY states the method (two booleans for two tiers) AND the boundary
condition where it fails (past 3–4 tiers, a real roles table beats a boolean
explosion) — the hai channel's mandatory "when NOT to" is present, not
skipped. **SCORE: PASS**

## HANDOFF LAW
B13's prompt is read aloud in full and discussed ("run it against whatever
you're calling 'admin' in your own app today...") before the pause — not
typed-only. Prompt extends the episode's lesson into the viewer's own
codebase, not a bland "learn more." **SCORE: PASS**

## Brand/channel check
`claude-hai` channel: Kokoro `af_bella`, Pragmatist register, `@HumanitariansAI`
footer chip, greeting `"Hi, HAI"` (HAI's shortest-forms word budget — one
word only) ✓. Visual skin stays the shared `claude` fidelity palette per
house law (persona changes voice/register/handle, never the palette) ✓.

## Estimated runtime
241s (~4:01) across 15 beats — an output of the script, not a target.

---

**VERDICT: PASS** (PASS / needs changes — human signs before
`generate_audio_kokoro.py` runs)

## Addendum (post-signature, same day)
B00 narration extended per requester's ask: opens with a spoken sign-on
("Hi! This is RM, for Humanitarians AI.") before the original line, kept
compliant with **COLD OPEN LAW** by folding it into B00's existing narration
rather than adding a pre-roll card — the composer UI is still frame one.
"commits" → "features" in the same beat (audience-appropriate wording).
`estimated_duration_s` bumped 12→17; total 241s→246s. Cosmetic/audience-fit
change, not a factual or structural one — does not require re-running the
full rubric above. No re-signature needed; proceeding to audio generation.
