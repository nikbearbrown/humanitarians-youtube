# Week 2: Learning the Physics Engine

**Weekly progress update (Medhavy)** · **Reporting week:** 2026-10-15 · **Fellow:** Shubham L.

## Executive Summary

Learning how the physics simulations inside Medhavy's Physics Volume 1 textbook work.

**Takeaway:** Know whether a simulation solves equations or steps time; it decides accuracy and speed.

## Evidence — Open Directly

- **Watch (16:9, 4K):** [Week2PhysicsEngine_ShubhamL.mp4](https://drive.google.com/file/d/1_QkZUy3S8BYBJnm0kacy6lD2WoN25L90/view)
- **Watch (9:16, 4K):** [Week2PhysicsEngine_ShubhamL.mp4](https://drive.google.com/file/d/1eiywwoH2HVzpyh_xzl5cKNOYbiokR0S8/view)
- [All renders on Drive](https://drive.google.com/drive/folders/1wGT_paFqo03H4KRqjkETQ5ESL5Rw_ELP)
- [Beat sheet](beat_sheet.json) (9 beats) · [vertical beat sheet](vertical/beat_sheet.json)
- [Fact check](FACTCHECK.md) · [Sources](SOURCES.md) · [Shot list](SHOTLIST.md) · [Prompts](PROMPTS.md)
- [Frictional log](FRICTIONAL.md)
- [Demo code and its real output](code/)

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

- The physics engine's source repository was not available locally; this film relies on its documentation.
- Vertical (9:16) master passes GATE V frame QC but not GATE T's portrait type-size floor.

## Rebuild

Built with [brutalist.art](https://github.com/nikbearbrown/brutalist.art) (free path: Kokoro, Remotion).
Scene components come from `runtime/remotion/src/scenes/FellowKit.tsx` (not yet merged into the toolkit).
See [BUILD-PROMPT.md](BUILD-PROMPT.md). Renders are on Drive, not in this repository.
The rendered narration says my full name; per this repository's rule the beat sheets here use "Shubham L.".
