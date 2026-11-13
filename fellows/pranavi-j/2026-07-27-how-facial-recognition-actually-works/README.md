# Topic Explainer: How Facial Recognition Actually Works (And When It Shouldn't)

**Fellow:** Sai Pranavi J.
**Date:** August 3, 2026 (rebuilt August 25-26, 2026 — 4K + 2 new opening beats, program feedback)
**Format:** `ai-explainer` (3-minute cap), first-person narration
**Source status:** Topic explainer, not a report of the fellow's own engineering work (contrast with the `2026-07-26-recovering-the-silently-dropped-filings/` weekly report in the sibling folder). The one factual claim with real stakes — the NIST demographic-effects finding — is verified directly against the primary source (NISTIR 8280) before narration was locked; see `FACTCHECK.md`.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=14Vb3jj-31gty6uv8i9gfYcqJBGwD2l8V)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=12lwyok1GkrM35EHB3AD0UbqU5r5xyJT0)

This ~3-minute AI-generated video asks: **is facial recognition good or bad?** — and answers that the question itself is the wrong frame. It opens with a title card and a personal on-screen introduction from the fellow, then walks through how the technology actually works (a similarity score, not a yes/no match), states its legitimate uses and its real harms with equal directness, cites NIST's own demographic-bias data including a named industry dissent, and closes on a proportional-scrutiny thesis rather than a policy verdict.

## What this covers (and what it deliberately avoids)

Covered: the detection → embedding → comparison → score pipeline; accessibility, device-unlock, missing-persons, and medical-diagnosis use cases; mass-surveillance, unconsented-tracking, and non-resettable-biometric harms; NIST's own bias findings (NISTIR 8280), including that the gap narrows sharply for the best-performing algorithms and that an industry-aligned source disputes the framing.

Deliberately avoided: naming any specific vendor or product, asserting a ban/regulate/expand policy position, or presenting the bias finding as one-sided in either direction — both "the gap is real" and "the gap narrows for top algorithms" are stated in the same beat.

## Production state

- Plan: **approved** (re-approved 2026-08-25 for the 4K rebuild + 2 new opening beats)
- Fact-check gate: **resolved** — verified against NISTIR 8280 directly before narration was drafted (not corrected after the fact); unchanged by the rebuild (no new factual claims introduced)
- Narration approval: **approved** — B01's exec-summary line approved 2026-08-25 (exact text supplied by program feedback); B00 is silent by design
- Voice: **Bella (`af_bella`)**, kept consistent with this fellow's prior report
- Resolution: **3840x2160 (4K)**, 24fps
- Audio lock: **locked** — 12/12 beats (2 new + 10 re-verified unchanged)
- Previz: **done** — 12/12 beats real MANIM media, 0 slates
- QC: GATE A/W/B clean; GATE V (against the true clean master, not the watermarked review cut) 0 BLOCKER / 12 MAJOR, all reviewed by eye and judged cosmetic — see `BUILD-LOG.md` and `SELF-ASSESSMENT.md`
- Duration: **185.17s**
- Publishing: **not authorized** (unchanged — separate human fellowship sign-off; this rebuild does not push or upload)
- Code repository: paperwork/code (no media) pushed to `github.com/nikbearbrown/humanitarians-youtube`, branch `sai-pranavi-j-facial-recognition-4k-rebuild` (commit `4a2a8c2`) — no PR opened yet

## 9:16 Short (`short/`)

A derivative Shorts cut built via the toolkit's `shorts.py` workflow (see
`BUILD-LOG.md`'s 2026-08-28 entry for full detail):

- **Master**: `short/2026-07-27-how-facial-recognition-actually-works-short.mp4`
  — **1080x1920, 24fps, 169.98s**, 12/12 slots real media (11 Manim beats +
  1 silent branded endcard), 0 slates.
- **Dropped**: **B09** (WORKED-EXAMPLE, the retail loss-prevention case
  applying the 3-question lens). The parent is 185.3s, ~5.3s over the 180s
  Shorts cap. The auto-plan's first choice was to drop **B07** (EVIDENCE,
  the NIST FRVT finding) since it's the single longest beat — but that beat
  is the script's only cited primary-source evidence, so it was protected
  with `--keep B07` and the planner found B09 instead. The framework (B03)
  and CTA (B10) both still carry the underlying "ask three questions"
  pedagogy without B09's worked example.
- **Outro rewritten**: B11's narration now explains what was cut and points
  viewers to the full 16:9 long (auto-rewritten by `shorts.py`, the only
  beat whose audio was regenerated for this cut — 11.95s, up from 4.92s).
- **Portrait redesign**: `short/scenes.py` is a from-scratch portrait
  authoring pass, not a crop. Four beats were structurally restacked for
  portrait's vertical reading direction — B02 (context chips: row→column),
  B04 (the detect→embed→compare→score pipeline: horizontal row→vertical
  column, arrows now point down), B07 (NIST evidence: two side-by-side
  vertical bars→two horizontal bars stacked, magnitude read as fill
  length), B08 (fluency-trap split panel: side-by-side→stacked top/bottom).
  The rest were re-indented/narrowed from the parent's 16:9 layout.
- **QC**: GATE A/W/B clean; GATE V against the TRUE clean master (not the
  watermarked `-slate.mp4`, which produces the same false-positive
  edge-bleed BLOCKERs documented elsewhere in this project) — 0 BLOCKER,
  8 MAJOR remaining, all reviewed against real extracted frames: 6 are the
  same whole-frame low-contrast heuristic false positive already
  documented for the parent (direct WCAG: ink-on-cream 11.99:1), and 2 are
  underfill on the toolkit-generated silent endcard (`shorts.py`'s own
  `endcard_png()`, outside this task's scope). One real defect was found
  and fixed in this pass: B03's thesis text animation straddled its GATE V
  50% sample point, producing garbled glyphs — fixed the same way as the
  parent's B04 fix (`Write()` → `FadeIn()`).
- Publishing: **not authorized** (same as the parent).

## Useful project files

- `beat_sheet.json` — narrative and visual plan (12 beats: B00 silent title card, B01 spoken exec-summary, B02-B11 the original 10 beats renumbered)
- `scenes.py` — Manim source for all 12 beats
- `BUILD-PROMPT.md` — the reproducible context/prompt this video was built from
- `BUILD-LOG.md` — dated build decisions and gate history, including the 2026-08-25/26 4K rebuild
- `FACTCHECK.md` — claim-level evidence and corrections
- `SOURCES.md` — the NIST report, exact numbers, and the industry-dissent citation
- `PEDAGOGY.md` — Gate P sign-off (act structure + evidence discipline)
- `SELF-ASSESSMENT.md` — this rebuild's honest score against PROOF.md's teaching rubric + production gate
- `SHOTLIST.md` / `PROMPTS.md` — updated per-beat work order for all 12 beats
