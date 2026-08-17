# Topic Explainer: How Facial Recognition Actually Works (And When It Shouldn't)

**Fellow:** Sai Pranavi Jeedigunta
**Date:** August 3, 2026
**Format:** `ai-explainer` (3-minute cap), first-person narration
**Source status:** Topic explainer, not a report of the fellow's own engineering work (contrast with the `2026-07-26-recovering-the-silently-dropped-filings/` weekly report in the sibling folder). The one factual claim with real stakes — the NIST demographic-effects finding — is verified directly against the primary source (NISTIR 8280) before narration was locked; see `FACTCHECK.md`.

This ~2-minute AI-generated video asks: **is facial recognition good or bad?** — and answers that the question itself is the wrong frame. It walks through how the technology actually works (a similarity score, not a yes/no match), states its legitimate uses and its real harms with equal directness, cites NIST's own demographic-bias data including a named industry dissent, and closes on a proportional-scrutiny thesis rather than a policy verdict.

## What this covers (and what it deliberately avoids)

Covered: the detection → embedding → comparison → score pipeline; accessibility, device-unlock, missing-persons, and medical-diagnosis use cases; mass-surveillance, unconsented-tracking, and non-resettable-biometric harms; NIST's own bias findings (NISTIR 8280), including that the gap narrows sharply for the best-performing algorithms and that an industry-aligned source disputes the framing.

Deliberately avoided: naming any specific vendor or product, asserting a ban/regulate/expand policy position, or presenting the bias finding as one-sided in either direction — both "the gap is real" and "the gap narrows for top algorithms" are stated in the same beat.

## Production state

- Plan: **approved**
- Fact-check gate: **resolved** — verified against NISTIR 8280 directly before narration was drafted (not corrected after the fact)
- Narration approval: **approved**
- Voice: **Bella (`af_bella`)**, kept consistent with this fellow's prior report
- Audio lock: pending
- Previz: pending
- Publishing: **not authorized**

## Useful project files

- `beat_sheet.json` — narrative and visual plan
- `scenes.py` — Manim source for all 8 beats
- `BUILD-PROMPT.md` — the reproducible context/prompt this video was built from
- `BUILD-LOG.md` — dated build decisions and gate history
- `FACTCHECK.md` — claim-level evidence and corrections
- `SOURCES.md` — the NIST report, exact numbers, and the industry-dissent citation
- `PEDAGOGY.md` — Gate P sign-off (act structure + evidence discipline)
