# Frictional Log — Myelin: Teaching Agents Habits

**Fellow:** Nidhi Grover<br>
**Project:** Iacon Autonomics (RL Environment)<br>
**Folder:** `2026-10-24-myelin-habits`<br>
**Week:** Week 5 (2026-10-21 – 2026-10-27)<br>
**Type:** Progress video<br>
**Project repository:** [myelin](https://github.com/nidhi-humanitarians/myelin)

---

## 2026-10-24 — Plan and script
*(Written on 2026-10-25; describes work from 2026-10-24.)*

- **What I was working on:** The Week 5 progress video, on the initial plan for Myelin.
- **Tried / expected:** Asked Claude to explore the myelin repository and follow the same process as the earlier videos: plan, script for my approval, then build.
- **Where it resisted / what I did next:**
  - Checking the docs against the raw trace files turned up errors: the episode the docs cite for "six booking lookups" made 3, not 6 (the six-lookup pattern is common across other runs of the same task); the Sonnet retail counts are 920 episodes / 7,086 calls, not 460 / 3,410; and the speed and cost figures in the docs (e.g. 15,000×, 60–80% savings) have no support in the traces. The video uses only re-counted call counts and presents Myelin as an initial plan, with savings as targets.
  - Script edits I made: define "semantic cache" on screen; add the habit compiler and the dashboard as the planned deliverables; make it more generic and say explicitly that this is an initial plan. The draft ran ~2:25 and was trimmed.
- **Claude / others:** I provided the repository and the context. Claude turned them into a plan and a script and re-counted the figures from the raw traces. I edited and approved the script and approved the final video.
- **Evidence:** [SCRIPT.md](SCRIPT.md) · [FACTCHECK.md](FACTCHECK.md) · [design specification](https://github.com/nidhi-humanitarians/myelin/blob/main/docs/DESIGN_SPECIFICATION.md)

## 2026-10-24 → 10-25 — Build
*(Written on 2026-10-25; describes work from 2026-10-24 to 2026-10-25.)*

- **Where it resisted / what I did next:** 16:9: text-size and contrast check (gate T) passed; master finished, 2:10 long. 9:16: gate T passed on its first run because the pre-render checks were run first; master finished; the final frame check sampled 24 frames with no problems.
- **Claude / others:** Claude ran the build; I approved the final video.
- **Understand now / still don't:** Running the cheap checks before the long render removed the fix rounds that slowed the earlier videos.
- **Evidence:** [TYPECHECK.md](TYPECHECK.md) · [vertical/TYPECHECK.md](vertical/TYPECHECK.md) · [final/myelin-habits.verified.json](final/myelin-habits.verified.json) · [vertical/final/myelin-habits-vertical.verified.json](vertical/final/myelin-habits-vertical.verified.json)

## 2026-10-25 — Correcting the Myelin docs
*(Written on 2026-10-25.)*

- **What I did next:** Had the errors found during the fact-check corrected in the myelin docs: `insights/EMPIRICAL_FINDINGS.md` now has the correct Sonnet retail counts and exact turn counts, and case study A cites a run that actually shows six lookups (task 2, trial 2, record 102); `docs/DESIGN_SPECIFICATION.md` was corrected to match.
- **Claude / others:** I asked for the docs to be corrected rather than only noted; Claude made the edits.
