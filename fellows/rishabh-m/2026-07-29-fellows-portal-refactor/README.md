# Fellows Portal, Refactored.

**Fellow:** Rishabh Madani \
**Project:** Humanitarians AI Fellows Portal — role tiering refactor \
**Date:** 2026-08-07

## Subject

A build reel on taking the Fellows Portal from a single shared admin password to a
proper three-role system — fellow, admin, super-admin — without introducing a roles
table.

The video covers the three gaps in the pre-refactor app (one shared
`ADMIN_PASSWORD` with no per-user identity, a fellow dashboard file grown past 400
lines, and free-text project matching where a typo silently files an orphaned
report), the two-boolean schema change that fixes the first, one unified session
model replacing the separate admin-password system, and nav-level gating so a plain
admin sees Fellows and Reports while a super-admin sees everything.

The closing beat is the transferable one: audit your own app's admin checks and ask
whether they read a real per-user flag or a shared secret.

## How the Video Is Structured

Sixteen beats alternating between the ask, the code, and the running result.

Each change follows the same three-step shape — a prompt to Claude, the diff it
produced, then a screen recording of that change working in the live app. The
schema beat pairs the `ALTER TABLE` with the before/after of `admin-auth.ts`; the
matching beat pairs the free-text field with the `<Select>` that replaced it; the
gating beat pairs the `NAV_ITEMS` filter with the two dashboards it produces.

The four OUTPUT beats are real screen recordings against the live dev app using
existing dummy accounts, not mockups — the fellow profile, the reporting form, and
both tiers of the admin dashboard.

## How the Video Was Built

Built with the Brutalist workflow: a `beat_sheet.json` driving narration and timing,
Kokoro narration in the Pragmatist register (`af_bella`), and Remotion scenes for
the twelve non-capture beats.

Narration is generated and measured first, so audio duration is the master clock and
every visual beat is cut to fit it rather than the other way around. The Remotion
scenes are reel-local patterns — `ClaudeComposerAsk` for the prompt beats,
`ClaudeCodeBeat` for the diffs, `ClaudeVerdictArtifact` for the summary card, and
`FellowsPortalLayerStack` for the two illustrated layer-stack beats.

## The 9:16 Short

A 1:05 Shorts cut is derived from this reel, in `short/`. It is a derivative cut,
not a re-edit: beats were dropped, never re-written, and every kept beat reuses this
reel's narration. Only the outro is new, pointing the viewer back to the long.

It keeps the hero cycle — intro, the ask, the schema change — and drops the rest.
All four beats are re-rendered natively in portrait rather than centre-cropped, so
no code is chopped mid-line.

One deliberate departure, recorded in `short/PEDAGOGY.md`: the Short has **no OUTPUT
beat**. The only candidates were the four 1280x720 screen recordings, and a 9:16
centre-cut of those is a 404x720 slice upscaled 2.7x with the dashboard layout
chopped mid-component. The result is deferred to the long instead.

## Files

- `README.md` — this file
- `beat_sheet.json` — narration, timing, and scene instructions (16 beats)
- `PEDAGOGY.md` — teaching-quality gate, signed before audio was generated
- `SOURCES.md` — source log, including the two corrections below
- `STATUS.md` — per-beat fill state
- `ToDo.md` — outstanding human slots (none)
- `scenes.py`, `todo.json` — build support
- `short/` — the 9:16 Shorts cut: its own `beat_sheet.json` (5 beats) and
  `PEDAGOGY.md` gate

## Notes

- **Two corrections logged in `SOURCES.md`.** The pre-refactor app was not "just a
  login page" — fellow auth, the profile dashboard, and report submission already
  existed, built 2026-04-04 by a different author with Claude Opus. What was missing
  was role tiering: a single shared `ADMIN_PASSWORD` rather than per-user flags. And
  "report upload" was corrected to "report submission" — reports are markdown text
  entered in a form, not file uploads.
- **Scope.** This demonstrates role tiering for a small, known set of roles. The
  two-boolean approach is deliberate and has a stated limit, called out in the video:
  ship booleans for two tiers, reach for a roles table before you have five.
- **Production caveat.** The four screen-capture beats were recorded at 1280x720, so
  they are upscaled in the 4K master and read softer than the twelve natively-4K
  beats.
