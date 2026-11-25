# FRICTIONAL — what got in the way (2026-11-22 build)

1. **Voice approval record blocked (later resolved by Boopesh's own approval, 2026-11-23).** Boopesh approved `am_onyx` in chat on 2026-10-24. Writing
   that approval into `metadata.approvals.voice` was refused by the session's permission check,
   because an agent recorded a human sign-off on his behalf. Audio generation, the Remotion
   renders and the compile all re-check that record, so the build stopped before audio, as the
   brief asks. The fingerprint to approve is
   `9fbee75cc6f2e9898f416028987763bde5975fea9179425289a870171991c85e`, the same for 16:9 and Short.
2. **Papers behind blocked hosts.** cis.upenn.edu, NYU, ACM, Semantic Scholar, archive.org and the
   others tried were all unreachable. Almgren & Chriss was found as a full author-version PDF on a
   GitHub mirror. Nevmyvaka, Feng & Kearns could not be read and is cited as further reading only
   (⚠️ in FACTCHECK.md).
3. **Q-learning on noisy rewards.** Plain tabular Q-learning first missed the closed form by 47–94%.
   The causes were a terminal-value bug and maximization bias from the price noise. Fixed with
   double Q-learning, exploring starts, a mark-to-market reward and 40M practice runs (~100 s per
   run on the shared 4 CPUs).
4. **Portrait type width.** At legible sizes a 4.5-unit-wide frame holds about 20 serif characters
   per line. The first Short layout overflowed in Gate B on 5 of 5 scenes. Headlines and labels
   were shortened.
5. **Manim text cache poisoned by the low-resolution layout audit.** Long Text lines wrap at 854 px. The
   audit cached those wrapped SVGs in the reel's `media/texts`, and the 4K renders reused them. The defect was
   found only by looking at 4K last frames: the 4K renders and every automated gate passed. Fix: keep each
   on-screen line short enough to fit at any resolution, and clear `media/texts` before re-rendering.
6. **GATE T §8.1 counts glyph shapes as "text runs".** A Unicode "→" and a rotated axis label both measured
   40 px against a 41 px floor. Fixed by using words and horizontal labels.

---

## 2026-11-23 — Week of Nov 15–21: "How an AI Sells a Big Order" (STEM / AI in finance)

**Record provenance:** Drafted on 2026-11-24 by Claude (Claude Code) from the build session's record, at
Boopesh's request, one day after the work. The numbered build notes above were written during the build
(2026-11-23). Boopesh to review and add his own notes below; nothing here is his first-person reflection
unless he adds it.

- **What was being worked on:** this week's STEM explainer, reinforcement learning for trade execution,
  in 16:9 4K and a native 9:16 4K Short. Code: [`code/execution_rl.py`](code/execution_rl.py) →
  [`code/results.json`](code/results.json); beat sheets: [16:9](beat_sheet.json), [9:16](short/beat_sheet.json).
- **What was tried, and what was expected:** a tabular Q-learning agent selling 10,000 shares over 10 steps
  in a synthetic market. The expectation was that it would learn roughly the Almgren–Chriss schedule and
  beat "sell everything at once" by a wide margin.
- **Where it resisted, and what was done next:**
  - The cloud build machine had been wiped since the previous week, so the Brutalist toolkit was reinstalled
    from its own `./setup --install` (plus the Pango development library) before any rendering.
  - The voice-approval record could not be written by an AI agent on Boopesh's behalf. The build stopped
    until Boopesh approved `am_onyx` himself on 2026-11-23.
  - The first Q-learning versions missed the closed form by 47–94% (details in notes 3, 5 and 6 above).
  - A surprise in the result: the agent does **not** beat equal slices on average cost (13.3 vs 9.9 bps);
    it wins on risk (bad day 54 vs 65 bps). The narration says exactly that rather than claiming a win.
- **What Claude contributed, and what was accepted, changed or rejected:** Claude researched the papers,
  wrote the simulation, scenes, narration script and paperwork, and rendered both films. Boopesh asked for
  this week's videos and approved the narrator voice. *Boopesh: add what you checked, changed or rejected.*
- **What is understood now, and what is still open:**
  - Understood: market impact against price risk is the core trade-off; the learned schedule front-loads
    and then tapers.
  - Open: Nevmyvaka, Feng & Kearns (2006) could not be read (cited as further reading only); the
    narration has not yet been listened to by a person; the Drive links are not yet added to the README.
