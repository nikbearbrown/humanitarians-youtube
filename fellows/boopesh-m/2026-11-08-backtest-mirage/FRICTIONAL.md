# FRICTIONAL — The Backtest Mirage

_Drafted by Claude (Claude Code) from the build session; Boopesh to read, correct and add his own entries._

## 2026-11-08
- **Tried:** read the anchor paper (Bailey, Borwein, López de Prado & Zhu, Notices of the AMS, 2014) from ams.org,
  the author copy on carmamaths.org, WMU ScholarWorks, CORE and phys.org. **Found:** every host blocked from the
  build container (proxy 403 / host not allowed). **Did:** took title, authors, venue, DOI and the paper's main
  claims from search-result summaries only, marked all of it ⚠️ in FACTCHECK.md, used no quotation from the paper,
  and recomputed the "45 tries → Sharpe ≈ 1 with 5 years of data" figure myself (independent-trials theory 0.99;
  my rule search 0.91).
- **Resisted (honesty about the result):** the 10,000-rule winner's out-of-sample line does not crash straight
  down: it rises for about a year, then falls, ending at −12 % for the two years. The first script said "turns
  down"; changed to "stalls, then slips" after looking at the chart.
- **Resisted:** a single out-of-sample Sharpe is noisy (±0.7 for two years), so one world can't prove "≈ 0". Added
  200 fresh noise worlds; the 10,000-rule winners average −0.02 ± 0.05 out of sample. One of the other N values
  (N = 100) averages +0.14, 2.7 standard errors above zero — reported in FACTCHECK.md as chance (the true value is
  0 by construction), and the film says "about zero".
- **Resisted:** within one world the rules' in-sample and out-of-sample Sharpe ratios correlate a little (+0.12),
  because all rules trade the same noise path; averaged over 200 worlds it is +0.03. Not shown on screen; logged.
- **Resisted:** the hesitant writer's first correction ("is the luckiest of 10,000 tries") stopped at "10." — the
  comma in "10,000" cut the replacement short. Caught by looking at the last frame; replaced with "is just the
  luckiest try" and re-rendered.
- **Resisted:** first layouts had small text with collapsed spaces ("randomnoise"), a y-axis title colliding with
  tick labels (B40), bar labels crossing ghost outlines (B50), the paper card touching the title (B60) and the
  winner label running into a bar (B70); fixed by looking at preview frames.
- **AI contribution:** Claude wrote the experiment, script, sheets and scenes. Kokoro `am_onyx` speaks the narration.
- **Still open:** read the paper itself when ams.org is reachable and confirm the 45-trials wording; pronunciation of
  "Borwein" (set to BOR-wine) and "Zhu" (set to "joo") needs a human listen.

---

## 2026-11-24 — Submission note for the week of Nov 1–7 (written later than the week it describes)

**Record provenance:** added on 2026-11-24 by Claude (Claude Code) at Boopesh's request, when this folder was
first committed. The entries above were drafted during the build, in the week of the work.

- **Why this commit is late:** the films and this source were delivered in the week of Nov 1–7. They could not
  be committed then: Boopesh's fork of the repository failed, and push access only arrived on 2026-11-24.
  This folder is restored unchanged from the source archive delivered that week.
- **Who did what:** Boopesh gave the prompts and instructions for the week (the topic direction, and
  the voice approval on 2026-10-24) and reviewed the delivered videos and code. Claude did the research,
  code, scenes, narration script and rendering.
- **Still open:** the Drive link for each film goes in this folder's README; Boopesh to add any notes of
  his own on what he checked, changed or rejected.
