# Frictional Log — Multi-Hop Search: Connecting the Pieces

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment)<br>
**Folder:** `2026-10-22-multi-hop-search`<br>
**Week:** Week 4 (2026-10-14 – 2026-10-20)<br>
**Type:** STEM/AI video<br>
**Late note:** Completed late (2026-10-22)<br>
**Project repository:** [agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)

---

## 2026-10-20 — First version (files since deleted)
*(Written late on 2026-10-24; describes work from 2026-10-20, from my account.)*

- **Where it resisted / what I did next:** Parts of the video were generated, then the approach was reworked and the video recreated on 2026-10-22. The files from this pass were deleted, so no renders or logs survive.
- **Evidence:** None kept (files deleted). Recorded from my account.

## 2026-10-22 — Reworked and recreated
*(Written late on 2026-10-24; describes work from 2026-10-22.)*

- **Tried / expected:** Recreate it to cover the fixes for points 6–9, plus citations (10) and privacy (11). Edits I asked for: stress why citations matter in B07, and spell out IRCoT in full. I accepted the proposed narration trims and asked for an update at least every 15 minutes.
- **Where it resisted / what I did next:**
  - 16:9: three runs. Gate V failed (2 major issues), then gate T failed on 2 beats, then everything passed.
  - 9:16: eight runs. Text-size failures (B05 labels, the outro hyphen), two safe-area failures (B02 caption off by 0.02, B10 footer off by 0.08), and a visual review of frames at ≥405 px that found collisions every gate had passed: "Hop" sitting higher than "Multi", line numbers overlapping words, labels touching card edges, cramped wrapped text. Fixing those meant re-rendering 10 scenes.
  - Most of the extra time on the 9:16 version was fix rounds.
- **Claude / others:** As with the earlier STEM video, I gave Claude the context and source material, and it turned them into the script and both builds. I edited the script (B07 citations, IRCoT in full) before approving it, and approved the final video. Claude also listed its own mistakes and created `precheck.py` and `gateb.sh`, which run the layout and size checks before any long build (kept in `brutalist-vids/_tools`).
- **Understand now / still don't:** Passing the automated gates doesn't mean a frame looks right, so check frames by eye. Run the cheap checks before the long build.
- **Evidence:** [SCRIPT.md](SCRIPT.md) · [FACTCHECK.md](FACTCHECK.md) · [TYPECHECK.md](TYPECHECK.md) · [final/multi-hop-search.verified.json](final/multi-hop-search.verified.json) · [video](https://www.youtube.com/watch?v=rZhI6hPbIOs)
