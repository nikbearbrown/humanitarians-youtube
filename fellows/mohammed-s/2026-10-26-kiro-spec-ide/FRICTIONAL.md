# FRICTIONAL — Kiro, Plan Before Code.

- **Folder:** `2026-10-26-kiro-spec-ide` · reporting week **2026-10-26 → 2026-11-01**
- **Dates inside this folder's artifacts:** brief, fact-check and build 2026-11-03 · masters
  promoted and approved 2026-11-04 UTC (2026-11-03 evening, US Eastern)
  (after the reporting week — see the README evidence index)
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-10-26 · written later, on 2026-11-03

> Reconstructed from the files in this folder on the day the reel was built.
> Drafted with Claude Code from those files.

**1. Date and what I was working on**
- A 3:04 explainer on Kiro, Amazon's spec-driven AI IDE built on VS Code: how planning before
  code changes security, and whether it suits a first-time developer.

**2. What I tried, and what I expected**
- Built from my own brief, with every claim checked by live web search on 2026-11-03.
- Library-first: reused `MuseChatVsAgent`, `MuseSteps`, `CortexWhereItBites` and the house
  composer and verdict scenes; five new dual-aspect components (`KiroSpecFiles`, `KiroHooks`,
  `KiroAdvisory`, `KiroSteering`, `KiroAutonomy`).

**3. Where it resisted, and what I did next**
- **My brief had a wrong fact.** It said autonomy "ranges from supervised to autopilot"; Kiro
  documents exactly two modes, Supervised and Autopilot. Narration and B08 now show two.
- Security claims were made precise rather than general: the two 2026 flaws are named by
  CVE ID (CVE-2026-4295, fixed in 0.8.0; CVE-2026-10591, fixed in 0.11), and the Checkmarx
  integration by product name.
- Pricing kept to "free tier; paid from $20/month" — credit allowances change too often.
- Preview stills showed type too small in the spec, hooks, steering and autonomy scenes;
  enlarged before rendering. The 9:16 title was kept short from the start, learning from
  the Muse reel's right-edge clip.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude built the scenes and ran the web fact-check and frame QC.
- Both masters passed the full final path: **GATE V 0 BLOCKER / 0 MAJOR** in both aspects.
- I watched and approved both masters on 2026-11-03; the approval is recorded in each beat
  sheet with the master's sha256.

**5. What I understand now, and what I still do not**
- Understood: a spec (requirements → design → tasks) gives a first-time developer a place
  to catch security edge cases before any code exists; hooks can run scans on every save.
- Open: the B03 password-reset spec is an illustration, not a real project; the CVE and
  pricing facts will date.

**Evidence in this folder**
- [`QC-STATUS.md` — GATE V 0/0, human approval](QC-STATUS.md) · [`build-state.json` — promoted master](build-state.json)
- [`FACTCHECK.md` — nine claims, one corrected](FACTCHECK.md) · [`SOURCES.md`](SOURCES.md) · [`CHECKS-REPORT.md`](CHECKS-REPORT.md) · [`PROMPTS.md`](PROMPTS.md)
- Masters: [16:9](https://drive.google.com/file/d/1XBUPVLg_xhwwyR3bB8Ao_JWWsx9BxZBB/view) · [9:16](https://drive.google.com/file/d/194FlBQBpHT_R9mZcn3SIQlmAoXQzKGmb/view)
