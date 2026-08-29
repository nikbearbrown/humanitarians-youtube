# BUILD-LOG — Three Ways To Be Wrong.

## 2026-08-18 — authored (Part A)

- Human requested a `deep-explainer` build of *RAG Foundations* Chapter 2,
  voice Onyx, signed Vedanshu Daxesh Patel, 4K, matching the existing
  ai-explainer and cli-explainer sibling reels for this chapter.
- ADVANCED-tier gate (CLAUDE.md rule 8) surfaced; requester confirmed
  proceeding on the strength of this book's existing shipped sibling
  deep-explainer reel (`2026-08-12-claude-rag-deep-explainer`) as precedent
  — applying the same reasoning already confirmed for the cli-explainer
  build earlier in this session.
- Plan (6 acts, 28 body beats, lane histogram) presented and approved by
  the human before any beat was authored in full, per SKILL.md's own
  `plan → GATE: approve` workflow step.
- `beat_sheet.json` authored: 32 beats total, lane mix CARD 3 / VOX 8 /
  MANIM 8 / REMOTION 9 — all within lint bands. Two vox runs (R1: B02–B03,
  R2: B06–B07), four single vox stills (B11, B17, B21, B27), all Tier 1
  (generic, no rights escalation).
- `scenes.py` authored: 8 Manim scenes (`B08_HallucinationSplit`,
  `B10_ReductionNotElimination`, `B12_TrainOnceDeployStop`, `B13_NoFlag`,
  `B18_TokenCeiling`, `B19_PositionEffect`, `B22_BiggerBoxSameLoss`,
  `B28_ConvergingBridge`) — syntax-checked, not yet rendered.
- Two new Remotion components built and registered in `Root.tsx`:
  `DeepActCard` (act-opening segment card, reused ×3) and
  `ProblemThreeFailuresTeaser` (wraps the shared `ChipGrid`). Seven other
  REMOTION beats reuse patterns already registered from the sibling
  ai-explainer build — no new component needed for those.
- `SOURCES.md`, `FACTCHECK.md` (GATE F: CLOSED, 8/8 rows verified),
  `PEDAGOGY.md` (VERDICT: PENDING), `CHECKS-REPORT.md` written.
- Honesty note carried from the cli-explainer sibling: Chapter 2 presents
  no fix, so B27/B28/BVDT name the missing step (deciding which passage
  matters) and bridge to Chapter 3 WITHOUT depicting or asserting a
  retrieval mechanism.

## 2026-08-19 — audio lock, Gate D2, Gate D1 previz (Part B)

- GATE P signed by Vedanshu Daxesh Patel (see PEDAGOGY.md).
- Audio generated (Kokoro `am_onyx`, free): 32/32 beats, total ≈ 6:02.
  `align.py` wrote the word clock (32 aligned, 0 fallback).
- `SHOPPING.md` written after audio lock with locked durations for all 8
  VOX beats (2 runs + 4 singles), all Tier 1.
- Gate D1 previz built by direct `manim`/`remotion_scenes.py`/`compile.py`
  invocation rather than `run.sh` — `run.sh`'s own `HAS_MANIM` probe embeds
  the reel path into an inline `python3 -c` script assuming a POSIX
  (`/c/Users/...`) path, which native Windows Python can't open; the same
  three tools `run.sh` would have called were run directly instead, with
  the same 4K flag.
- 8 Manim scenes rendered at 3840×2160 for real; visual QC found and fixed
  two defects at the source (`scenes.py`): 3 scenes (B08, B19, B22) were
  being stretched past 3× ("extreme slow-mo") to fill their beats — fixed
  by lengthening each scene's native `wait()`; B28's three edge labels
  overlapped their connecting lines — fixed by removing an errant
  `.shift()` and widening the buffer. Both re-rendered, re-verified clean.
- 9 Remotion beats + 3 CARD beats + 4 bookends rendered via
  `remotion_scenes.py` — all clean on first pass.
- Compiled the Gate D1 previz (`compile.py --review --height 2160`):
  3840×2160, 362.4s, 24/32 filled, 8 VOX beats correctly rendered as
  labeled slates. `_qc/REPORT.md` written: 0 BLOCKER / 0 MAJOR remaining.

## 2026-08-19 — pantry fill, final master (Part B continued)

- Human asked for the 8 pantry stills to be sourced directly rather than
  waiting on a human photo shoot. No AI image-generation tool is available
  in this environment, so real, licensed stock photos were searched for
  and downloaded instead (WebSearch + WebFetch + curl), each with a
  `pantry/<BID>.source.txt` sidecar (url/license/credit/retrieved date).
- 5 of 6 initial fills were solid matches (B02/B03, B11, B17, B27). **B21
  caught on review**: the first fill ("Two Old Books in a Suitcase," Pexels
  18137003) had a legible book title as its clear focal point, contradicting
  the "empty, cavernous interior" intent and reintroducing real-world
  legible text — a genuine mismatch, not used. Swapped for Pexels 7957726
  (Eva Bronzini), a genuinely empty box shot — container type shifted from
  "suitcase" to "box" since an honestly-empty suitcase isn't a natural
  stock-photo subject.
- B06/B07 (the magician's-hat scene): two independent searches found no
  real, freely-licensed photo of "hands over an empty top hat" — every
  result was a worn hat, a hat-less card trick, or a costumed child. Left
  as slates initially, per the standing rule against forcing a mismatch.
- Human then said "take whatever is available." Found a real antique top
  hat photo (Unsplash, Fiona Feng / @moonai) — genuinely a top hat, real
  photo, correctly licensed, but without the "hands reaching in" action
  the brief asked for. Documented in SHOPPING.md as an honest
  best-available PARTIAL match (not represented as an exact one) and used;
  B07 manually cropped tighter from the same source image.
- `pantry.py` intake run twice (once after the first 6 fills + the B21
  swap, once after B06/B07); pantry.py does not itself copy `.source.txt`
  sidecars into `media/` (it only stubs a generic placeholder if one is
  missing), so the real sidecars were mirrored into `media/` by hand each
  time to overwrite pantry.py's generic "FILL-IN" stubs.
- Recompiled: `compile.py --height 2160` (no `--review`) → **32/32 filled,
  zero slates** → `claude-rag-the-problem-deep-explainer.mp4`, 3840×2160,
  362.4s. Frame-checked all 8 formerly-vox beats directly against the
  compiled output: 6 sharp with no artifacts despite `compile.py`'s
  conservative upscale warnings; B07 shows mild softness from cropping a
  2956×2116 source, judged acceptable (masked further by the vox grain
  treatment) rather than reshooting a fourth time.

## Gate status

- [x] GATE F (factcheck) — CLOSED, see FACTCHECK.md
- [x] GATE P (pedagogy sign-off) — PASS, signed by Vedanshu Daxesh Patel
- [x] Audio lock — 32/32 beats, Kokoro am_onyx, ≈6:02 total
- [x] Gate D2 (SHOPPING.md) — written after audio lock, all 8 slots filled
- [x] Gate D1 previz — built, 4K, 24/32 filled, visual QC clean (0 BLOCKER/MAJOR)
- [x] Pantry fill — 8/8 stills placed (6 strong matches, 2 best-available partial)
- [x] Final master — `claude-rag-the-problem-deep-explainer.mp4`, 3840×2160,
      362.4s, 32/32 filled, 0 BLOCKER/MAJOR
- [ ] Never publish — master stays in this reel folder (standing rule, not a TODO)
