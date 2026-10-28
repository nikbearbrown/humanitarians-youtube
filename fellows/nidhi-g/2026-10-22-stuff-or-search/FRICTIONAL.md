# Frictional Log — Stuff It or Search It?

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment)<br>
**Folder:** `2026-10-22-stuff-or-search`<br>
**Week:** Week 3 (2026-10-07 – 2026-10-13)<br>
**Type:** STEM/AI video<br>
**Late note:** Made late (built 2026-10-22)

---

## 2026-10-22 — Planning the STEM videos
*(Written late on 2026-10-24; describes work from 2026-10-22. Made late because Brutalist setup issues blocked videos in Week 3.)*

- **What I was working on:** An informational video based on my agentic-search work ([agentic-repl](https://github.com/nidhi-humanitarians/agentic-repl)).
- **Tried / expected:** Asked Claude for topic ideas from the repository, then for a ~1:30 video on why this matters (NIAH, the problems, what's needed). I asked for more angles, such as context stuffing, and settled on two videos: why RAG isn't enough, then multi-hop RAG as the solution. All 11 points had to be covered across the pair, ~2:00 each. Script approved.
- **Claude / others:** The research context and the repository came from me. Claude turned them into topic options and then a script with sources. I chose the split, the scope and the length, then reviewed and approved the script.
- **Evidence:** [SCRIPT.md](SCRIPT.md) · [FACTCHECK.md](FACTCHECK.md)

## 2026-10-22 — Build: more fix rounds than expected
*(Written late on 2026-10-24; describes work from 2026-10-22.)*

- **Tried / expected:** Expected this to build faster than the longer videos. It took longer, so I asked why.
- **Where it resisted / what I did next:** Length wasn't the cause; beats and fix rounds were (12 beats, 9 animations). Five fix rounds, each another pass through compile and gates: the browser timed out on B00 (CPU contention); B03's faint lines failed contrast; text in the accent color in B04–B06 (a house rule Claude already knew); the B04 accent bar was misread as text; portrait B01 underfilled (re-rendered, measured 58% / 79% fill). A cosmetic wrap in portrait B04 ("RULER (Hsieh et / al.)"): I said fix it, and it became two clean lines.
- **Claude / others:** Claude carried out the build and the fix rounds. It said the accent-text error was its own mistake and saved a pre-render checklist to avoid repeats. I asked for the extra B04 fix and approved the final video.
- **Understand now / still don't:** Build time depends on beat count and fix rounds, not video length. Running the gate checks before a long render saves hours.
- **Evidence:** [TYPECHECK.md](TYPECHECK.md) · [STATUS.md](STATUS.md) · [final/stuff-or-search.verified.json](final/stuff-or-search.verified.json) · [video](https://www.youtube.com/watch?v=bgagiyyImeI)
