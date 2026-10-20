# PLAN — banking-domain-interview-end-to-end-v2 (whole-book trailer, cli-explainer)

**Status: APPROVED 2026-09-08.** Voice locked: `af_bella` (Bella).

**OPEN FLAG FOR PM — 9:16 length.** Earlier PM guidance wanted the 9:16
full-length (matching the 16:9), not a shortened cut. This plan's 9:16
derivation (`./art shorts`) drops the revision cycle to fit the 180s Shorts
cap per `cli-explainer/SKILL.md`'s own REVISION LAW carve-out — so the 9:16
master will run shorter than the 16:9 master. The PM's latest feedback (4K
bitrate, frame-fill, branding) didn't revisit the length point either way.
Proceeding on the user's instruction, but this is unresolved — **check with
PM whether a shortened 9:16 is acceptable, or whether it needs to be
full-length after all** (which would mean abandoning `./art shorts` for a
hand-built full portrait reflow of all 12 beats instead, i.e. this toolkit's
version of what v1 did in the other checkout).

## What this replaces

There is an existing v1 whole-book trailer at
`brutalist-art/reels/banking-domain-interview-end-to-end/` — a *different*, paid
toolkit checkout (not this one), built as a 7-beat Manim-only title-card montage
(no CLI/composer beats at all). Its masters, measured just now:

| file | resolution | video bitrate |
|---|---|---|
| `banking-domain-interview-end-to-end-cut.mp4` (16:9) | 3840×2160 | 330 kbps |
| `bankinginterviewendtoend_supriya_vertical.mp4` (9:16) | 2160×3840 | **139.5 kbps** |

Both numbers are low for 4K, but the 9:16 one is the PM complaint: at 2160×3840,
139 kbps means the frame is mostly flat/empty — CRF-based encoding (which this
toolkit uses) spends bits on content, so a near-empty frame compresses to
almost nothing. That matches PM issue #2 (text filling only ~15–20% of frame
height) — **issues #1 and #2 are the same root cause**: fix the fill, the
bitrate rises on its own. No bitrate floor needs to be hacked in.

v1's branding: spoken "Hi, I am Supriya…" in narration, but no visible on-screen
handle. PM issue #3 wants a visible on-screen handle reading "Supriya" — direct,
not the "in for Supriya" framing `banking-domain-sql-running-total-bug` used
(that phrasing fits an anonymous-narrator compliance workaround; it's not what's
being asked for here).

**v2 is a genre change, not a patch**: rebuilt from scratch in *this* toolkit
(`brutalist.art`), as a proper `cli-explainer` build reel (composer → code →
moving output, at least one revision cycle), same shape as
`projects/banking-data-analyst-interview-prep/banking-domain-sql-running-total-bug/`.

## Source

Whole book: `books/banking-data-analyst-interview-prep/book.md` (six-part
outline) plus two real worked examples pulled from actual chapters (kept
real, not invented, per the reference project's own standard):
- Ch. 8 (`08-sql-i-balances-cohorts-window-functions.md`, lines 141–197) —
  the correct running-balance CTE (shown correct here — no bug; this is a
  trailer, not the bug-teardown piece).
- Ch. 9 (`09-sql-ii-charge-off-waterfalls-vintage-curves.md`) — a charge-off
  waterfall snippet, for the revision cycle ("now make it harder").

## Output location

`brutalist.art/projects/banking-data-analyst-interview-prep/banking-domain-interview-end-to-end-v2/`
— mirrors the two sibling projects already in this folder.

## Beat arc (12 beats, same spine shape as the reference)

| Beat | Role | Renders via | Content |
|---|---|---|---|
| B00 | INTRO (cold open) | Remotion `ClaudeComposerAsk` | "Hi, I'm Supriya" + hook: banking DA interviews test bank-specific vocabulary general SQL/Python prep doesn't cover |
| B01 | PROBLEM | Manim | The gap: regulators, ratios, charge-off math — fluent in `pandas`, cold on CET1/LCR/DPD |
| B02 | MECHANISM | Manim | Book map: the six parts (Landscape → Regulation/Risk → Data Stack → Technical Prep → Behavioral/Case/Systems → Day-Of) |
| B03 | CLI (ask) | Remotion `ClaudeComposerAsk` | Ask Claude to review a real running-balance CTE (Ch. 8) |
| B04 | CODE | Remotion `ClaudeCodeBeat` | The actual correct Ch. 8 SQL, trimmed to the lines that teach |
| B05 | OUTPUT | Manim | Animated correct running-balance table |
| B06 | CLI (revision, required) | Remotion `ClaudeComposerAsk` | "Now make it harder — add the charge-off waterfall" (Ch. 9) |
| B07 | CODE (revised) | Remotion `ClaudeCodeBeat` | The actual Ch. 9 snippet |
| B08 | OUTPUT (revised) | Manim | Animated waterfall result |
| B09 | SUMMARY | Manim | What the book covers, six parts recap |
| B10 | NEXT STEPS (handoff) | Remotion `ClaudeComposerAsk` | "Your turn" — a self-check prompt the viewer can paste into Claude |
| B11 | OUTRO | Remotion `ClaudeTitleOutro` | Title restate + visible "Supriya" handle |

Target runtime ~190–200s (matches the reference's own 168s-ish scale plus a
bit more for a whole-book trailer's broader summary).

## Branding — the actual PM-driven change from the reference

- **No "in for X" framing anywhere.** B00 greeting: "Hi, I'm Supriya." Outro
  subline: "Supriya — built with Claude."
- **Visible handle on-screen**, not just spoken: `folderLabel` on every
  composer/code beat = `"Supriya"` (replacing the reference's book-title
  folder chip), and the OUTRO's `handle` = `"Supriya"` at full size (LOGO LAW's
  corner-mark slot, substituted the same way the reference substituted a plain
  text mark for the missing @handle).
- **Persona: none, channel: null** — same structural choice as the reference
  (this book isn't the claude-liam or claude-hai channel; it's the author's own).

## Voice — locked

`voice_kokoro: "af_bella"` (Bella) — same choice the reference reel made for
this book (series continuity across the two banking-domain reels). Confirmed
by user 2026-09-08.

## Resolution — 16:9 and 9:16, both genuinely 4K

- **16:9 master**: 3840×2160, same as the reference (`compile.py --height 2160`).
- **9:16 master**: built via **this toolkit's own `./art shorts` pipeline**
  (`runtime/scripts/shorts.py`), not a hand-rolled full reflow like v1 was.
  This is the toolkit-native path and it directly fixes both PM complaints:
  - `cli-explainer/SKILL.md`'s own **REVISION LAW** carve-out: the 9:16 cut
    is *allowed* — required, even — to ship a single CLI→CODE→OUTPUT cycle,
    no revision, with a rewritten outro pointing at the 16:9. At ~190–200s our
    reel is over the Shorts 180s cap, so `shorts.py`'s auto-plan will drop the
    longest unprotected beats — in practice the revision cycle (B06–B08) is
    exactly what should go, which lines up with the SKILL's own rule instead
    of fighting it.
  - Compile the derived short at **`--height 3840`**, not the `1920` shorts.py
    prints as its example next-step. `compile.py` computes width from height
    and the sheet's `aspect_ratio` (`w = height * num/den`), so `--height 3840`
    on a 9:16 sheet yields genuine **2160×3840 4K** — matching the 16:9
    master's resolution, not a downgraded HD derivative.
  - Frame-fill: `ClaudeComposerAsk` is already portrait-aware
    (`useVideoConfig` + a `portrait` branch scaling UI off `height`), and
    `ClaudeComposerAsk916` / `ClaudeTitleOutro916` are already registered in
    `Root.tsx`. **`ClaudeCodeBeat` is NOT** — its code-line font sizes are
    hardcoded pixels (13/11/22px), which would render as a tiny island on a
    3840-tall canvas — precisely the underfill bug PM is flagging, just in a
    component that hasn't been portrait-fixed yet. **New engineering needed:**
    a `ClaudeCodeBeat916.tsx` (relative font sizing off `height`, same pattern
    `ClaudeTitleOutro916`/`ClaudeVerdictArtifact916` already use) + its
    `Composition` registration in `Root.tsx`, so `shorts.py`'s ONDA CHECK can
    rewire B04/B07's beat to it. (B07 itself will likely be dropped by the
    cap-plan, but B04 stays, so this component is load-bearing either way.)
  - Manim beats kept in the short (B01, B02, B05 — B08/B09 depend on which
    the cap-plan drops) need portrait scene classes in `short/scenes.py`,
    written to the same fill-the-canvas standard as `ClaudeVerdictArtifact916`
    (font sizes as a fraction of frame height, not fixed pixels).

## Paperwork set (required — GATE F / GATE P — matches the reference exactly)

`SHOTLIST.md`, `PROMPTS.md`, `FACTCHECK.md`, `PEDAGOGY.md`, `NARRATION-SCRIPT.md`,
`RESEARCH-SUMMARY.md`, `VISUAL-PLAN.md`, `STATUS.md`, `ToDo.md` — same purpose
and gate-binding as documented in the reference project's own `PLAN.md`.

## Gates (in order)

1. **This plan** (incl. the voice choice above) — you review and confirm.
2. **Paperwork set + `beat_sheet.json`** — written together; you review
   narration and sign `PEDAGOGY.md`'s `VERDICT: PASS` yourself.
3. **`scenes.py`** (3 Manim classes, 16:9) + **`ClaudeCodeBeat916.tsx`** (new
   Remotion component + `Root.tsx` registration) — you review before anything
   renders.
4. **Render gate, 16:9**: `generate_audio_kokoro.py` (blocked until GATE P
   signed) → `run.sh` → Manim + Remotion renders → Gate B pixel audit → Gate V
   final-frame check → review cut → clean master.
5. **9:16 derivation**: `./art shorts` (cap check → auto-plan, printed for
   your review before anything recompiles) → portrait Manim scenes in
   `short/scenes.py` → `compile.py short --review --height 3840` → Gate V
   check specifically for frame-fill (the PM's #2) and a bitrate sanity check
   on the resulting master (the PM's #1) → clean 9:16 master.
