# FRICTIONAL — The Tails Go First

*Draft written from the build session. Edit into your own voice before relying
on it; the facts are accurate, the framing is a starting point.*

---

## 2026-10-16 — the week the simulation disagreed twice

**What I tried and expected.** Model collapse is a famous result with a Nature
paper behind it, so I assumed the experiment would be the easy part and the
writing would be the work. I expected to build a recursive training loop, watch
the tails vanish, and start authoring.

**Where it resisted, the first time.** My first loop did the exact opposite of
collapse. Using a Silverman-rule bandwidth for the kernel density model, the
kernel width scales with the current spread — so every generation *added*
variance instead of losing it. Standard deviation ran 1.6 to 1563 across 120
generations, and the rare subpopulation's share climbed toward 50%. A clean,
confident, completely wrong result. The idea was fine; my model was wrong.

**Where it resisted, the second time.** With a fixed bandwidth the drift
behaved, but my *measurement* was broken. I was counting samples beyond x = 3
as "the rare subpopulation", and ordinary bulk outliers wander across that line
— so the subpopulation appeared to come back from extinction in 30 of 41 runs.
That is structurally impossible: nothing in the loop can reinvent a region. The
number was telling me my metric was wrong, not that the world was strange.
Replaced it with a lineage label carried through resampling. Recoveries went to
zero, as they must.

**What I accepted, and what I rejected.** Twice I had a plausible-looking
result I could have written narration around. The first would have claimed
something false. The second would have claimed something impossible. In both
cases the cost of noticing was a rewritten script, because nothing had been
rendered yet and no words had been written.

**Two fabrications I caught in my own work.** Writing the beat sheet, I filled
the on-screen decline curve with hand-made interpolation between the measured
points — and misaligned it with the generations it claimed to plot. Separately,
the function that exported the "after" density curve generated a *fresh* sample
instead of running the loop and measuring it. Both would have put invented
figures on screen in a video about measurement. Both are now computed by the
script, which prints the exact arrays the beat sheet uses.

**What the library gave back.** This was the first reel where GATE L carried
more than it demanded. `StageRail`, built last week for a completely different
subject — the YouTube publish pipeline — rendered "Real data → Gen 1 → Gen 2 →
Gen n" without modification, because it takes its stages as data. `PositionCurve`,
built a fortnight ago for long-context position bias, plotted a share decaying
to zero. Only one component had to be built. The discipline of making
components generic has started paying rent.

**What is understood now.** Running the experiment first is not about
efficiency, it is about which mistakes are cheap. Every error in this build was
caught while it still cost a rewrite. The two that reached the beat sheet — the
invented curve and the fabricated density — were caught by the habit of asking
"where did this number come from?" of my own output, not by any gate.

**Still open.** The loop isolates statistical error from finite sampling. The
paper names two further mechanisms — expressivity and approximation error —
which are real and which this script does not demonstrate. A follow-up could
show a model that *cannot represent* the rare mode at all, which collapses for
a different reason and probably faster.
