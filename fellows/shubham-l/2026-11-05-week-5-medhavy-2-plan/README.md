# Week 5: Studying the Medhavy 2.0 Plan

**Weekly progress update (Medhavy)** · **Reporting week:** 2026-11-05 · **Fellow:** Shubham L.

## Executive Summary

Studying the Medhavy two point oh plan: what changes, in what order, and how a release gets approved.

**Takeaway:** Treat 'builds', 'approved' and 'deployed' as three separate checks.

## Evidence — Open Directly

- **Watch (16:9, 4K):** [Week5Medhavy2Plan_ShubhamL.mp4](https://drive.google.com/file/d/1YkC9u50XXRTxHclX6M_ipMzBBURD3_DJ/view)
- **Watch (9:16, 4K):** [Week5Medhavy2Plan_ShubhamL.mp4](https://drive.google.com/file/d/1eCw47aiym65friDnINmTOiHzYyHWKTyd/view)
- [All renders on Drive](https://drive.google.com/drive/folders/1wGT_paFqo03H4KRqjkETQ5ESL5Rw_ELP)
- [Beat sheet](beat_sheet.json) (9 beats) · [vertical beat sheet](vertical/beat_sheet.json)
- [Fact check](FACTCHECK.md) · [Sources](SOURCES.md) · [Shot list](SHOTLIST.md) · [Prompts](PROMPTS.md)
- [Frictional log](FRICTIONAL.md)

## Human and AI work

- **Mine:** topic and framing, review of every claim against the cited sources, final approval.
- **Claude (Claude Code):** drafted the beat sheet, narration, demo code and figure layouts.
- **Kokoro `am_onyx` (Liam):** AI narration, disclosed in the first beat.
- **Corrected during the build:**
  - Accent text darkened to pass the WCAG contrast check.
  - Type enlarged on every card to meet the 4K minimum glyph size.
  - Verdict and outro beats rebuilt as new layouts because the stock ones left the frame mostly empty.
  - Notes cut to 12 words or fewer; labels that were truncated on screen were reworded.

## Still unverified

- Vertical (9:16) master passes GATE V frame QC but not GATE T's portrait type-size floor.

## Rebuild

Built with [brutalist.art](https://github.com/nikbearbrown/brutalist.art) (free path: Kokoro, Remotion).
Scene components come from `runtime/remotion/src/scenes/FellowKit.tsx` (not yet merged into the toolkit).
See [BUILD-PROMPT.md](BUILD-PROMPT.md). Renders are on Drive, not in this repository.
The rendered narration says my full name; per this repository's rule the beat sheets here use "Shubham L.".
