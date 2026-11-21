# Frictional Log — How Ribosomes Read mRNA (setup test)

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment)<br>
**Folder:** `2026-10-02-claude-liam-ribosomes-read-mrna`<br>
**Week:** Week 2 (2026-09-30 – 2026-10-06)<br>
**Type:** Setup test, not a weekly video

---

## 2026-10-02 — First Brutalist install: test reel 2
*(Written late on 2026-10-24; describes work from 2026-10-02. Reconstructed from build files and my later account.)*

- **What I was working on:** A fuller second test: a 12-beat biology explainer, 60-second brief, Kokoro `am_onyx` voice, review cut only.
- **Where it resisted / what I did next:**
  - First audio pass ran 74.7 s against a 60 s brief; narration tightened and regenerated at `--speed 1.1` → 65.7 s (BUILD-LOG).
  - Gates A and W passed on all 7 scenes and Manim beats B02–B08 rendered, but the build still failed: "Review pipeline failed (exit 2)".
  - Across Week 2, two failed setup attempts took about 7 hours each.
  - I later deleted the old install and started over from a fresh copy. See [Brutalist, Installed.](../2026-10-12-brutalist-installed/FRICTIONAL.md).
- **Claude / others:** I supplied the topic and the test brief. Claude Code drafted the beat sheet and scenes and ran the build, working around one checker limitation (it can't see `.animate` moves, so FadeIn/FadeOut instead). I reviewed the results.
- **Understand now / still don't:** Now: duration is an output, not a target. Getting partway through (audio and some renders) doesn't mean the install works. I'm still understanding the concept of gate checks.
- **Evidence:** [build-state.json](build-state.json) · [BUILD-LOG.md](BUILD-LOG.md) · [BUILD-PROMPT.md](BUILD-PROMPT.md) · [CHECKS-REPORT.md](CHECKS-REPORT.md)
