# PEDAGOGY — banking-sql-running-total-bug

**Prepared by:** Claude (agent) · **Date:** 2026-08-10
**Skill:** `cli-explainer` (`skills/make/cli-explainer/SKILL.md`)

This is **GATE P** — the quality gate `generate_audio_kokoro.py` checks before a single second of
narration is generated. Per P1 (AI+1 doctrine, this repo's own constitution and this toolkit's
house law), **an agent never signs its own gate.** Everything below is my checklist against the
skill's required elements; the `VERDICT` line stays `PENDING` until you sign it.

## Required-elements checklist

1. **Required 12-beat spine present** (INTRO → PROBLEM → MECHANISM → CLI→CODE→OUTPUT →
   CLI→CODE→OUTPUT → SUMMARY → NEXT STEPS → OUTRO), matching the structural reference's own beat
   count and role sequence exactly.
   **CHECK: satisfied** — see `beat_sheet.json`, 12 beats B00–B11, roles verified against
   `SKILL.md`'s required-spine table.
2. **THE REVISION LAW** — at least one CLI → CODE → better OUTPUT cycle.
   **CHECK: satisfied** — B06 (CLI/CHANGE) → B07 (CODE, fixed) → B08 (OUTPUT, corrected) is the
   required revision; B03→B04→B05 is the first (buggy) cycle.
3. **THE ACTUAL-CODE LAW** — CODE beats show real, runnable SQL, trimmed to teaching lines, never
   pseudocode.
   **CHECK: satisfied** — B04 and B07 show the actual `running` CTE from Chapter 8 (buggy and
   fixed versions respectively), trimmed with `-- unchanged` comments for the other 2 CTEs, not
   rewritten or simplified beyond removing repeated boilerplate.
4. **Output beats are never a still — always motion** (Manim/Remotion/d3/screen-capture).
   **CHECK: satisfied** — B01, B02, B05, B08, B09 are Manim; all other beats are Remotion
   `ClaudeComposerAsk`/`ClaudeCodeBeat`/`ClaudeTitleOutro`. No PNG-still fallback anywhere in
   `beat_sheet.json`.
5. **NO FABRICATION** — every claim traces to the book/fact-check, illustrative data honestly
   labeled.
   **CHECK: satisfied** — see `FACTCHECK.md`'s claim-by-claim trace (7 claims, all CONFIRMED) and
   its "what is new here" section (the one addition — sample account `ACCT-50231` — is disclosed,
   not presented as real). One caught-and-fixed issue: an earlier draft of B00's narration said
   "wrong for half your customers," an invented statistic with no source; corrected to "wrong for
   any account with a past," which matches the book's actual claim (any account with pre-2026
   history) with no invented fraction.
6. **HANDOFF LAW** — the NEXT STEPS beat's suggested prompt is read aloud and discussed, not just
   shown.
   **CHECK: satisfied** — B10's narration reads the prompt's intent ("check my own running-balance
   CTE... move it downstream... check it against an account with history older than your reporting
   window") rather than only displaying it on screen.
7. **Compliance/persona requirement** — "in for Supriya," no default persona name, no channel
   branding.
   **CHECK: satisfied** — B00 and B11 narration use "in for Supriya" only; `metadata.persona` is
   `"none"`; no `@handle` anywhere, `channel_title` is the book's own title text instead.
8. **No paid services.**
   **CHECK: satisfied** — Kokoro (local), Manim (local), Remotion (local Node render). See
   `FACTCHECK.md`'s "No paid services" section.

## Outstanding for the human reviewer

- [x] Read all 12 narration blocks in `NARRATION-SCRIPT.md` and confirm the Teardown voice reads
      right to you (spare, no padding, no forbidden phrases).
- [x] Confirm the illustrative sample data (`ACCT-50231`, the four transactions, the
      buggy/corrected balances) in `VISUAL-PLAN.md` is clearly enough labeled as illustrative once
      it's on screen.
- [x] Confirm the persona/branding choices (no name, `claude` skin, Kokoro `af_heart`, plain
      `channel_title` mark) still read as sufficient compliance attribution to you.
- [x] Confirm the 4K (3840×2160) render target is acceptable given the longer render time it
      implies, or tell me to drop to 1080p instead.

## VERDICT: PASS

Signed: Supriya Kushwaha (human, author)
Date: 2026-08-10
Evidence: Reviewed PLAN.md, beat_sheet.json, FACTCHECK.md, NARRATION-SCRIPT.md, VISUAL-PLAN.md,
and this checklist in-session; approved narration, illustrative sample data, persona/branding
choices, and the 4K render target as-is. Verdict communicated directly to the agent in-session;
transcribed here per that instruction.
