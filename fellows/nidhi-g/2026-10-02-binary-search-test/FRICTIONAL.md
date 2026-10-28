# Frictional Log — Binary Search in Three Looks (setup test)

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment)<br>
**Folder:** `2026-10-02-binary-search-test`<br>
**Week:** Week 2 (2026-09-30 – 2026-10-06)<br>
**Type:** Setup test, not a weekly video

---

## 2026-10-02 — First Brutalist install: test reel 1
*(Written late on 2026-10-24; describes work from 2026-10-02. Reconstructed from build files and my later account.)*

- **What I was working on:** My first install of Brutalist, in a folder called `gemma_brutalist`, done with Claude Code. A 3-beat "Binary Search in Three Looks" reel as an end-to-end test. Across Week 2 I made two failed setup attempts, about 7 hours each.
- **Where it resisted / what I did next:** The build failed: `build-state.json` records `"status": "failed"`, "Review pipeline failed (exit 2)". Narration audio was generated, but no animation rendered for this reel. The causes, as I understood them later: some dependencies needed an older Python than mine (Manim 0.18 requires Python < 3.13), and the build kept stopping at its gates. I spent hours patching symptoms.
- **Claude / others:** I set the goal (get Brutalist running and prove it with a small test reel) and provided the setup materials. Claude Code turned that into the beat sheet and ran the install and build. I reviewed what came back and decided how to proceed.
- **Understand now / still don't:** Now: gates are deliberate checks that stop the pipeline with exit code 2; the root cause was the Python version, not the reel.
- **Evidence:** [build-state.json](build-state.json) · [beat_sheet.json](beat_sheet.json) · explained in [Brutalist, Installed.](../2026-10-12-brutalist-installed/)
