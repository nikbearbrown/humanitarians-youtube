# FRICTIONAL — Both Sides Passed

*Draft written from the build session. Edit into your own voice before relying
on it; the facts are accurate, the framing is a starting point.*

---

## 2026-10-23 — the check that caught nothing because my data was too tidy

*Built 2026-10-23; held and delivered in the week ending 2026-10-30. The session date above is when the work happened and is not rewritten.*

**What I tried and expected.** The argument was clear before I started: checks
that live inside a stage cannot see a disagreement *between* stages. I wanted
three numbers — what in-stage validation catches, what a boundary contract
catches, and what a boundary contract plus a distribution profile catches — so
the claim would be a measurement rather than an assertion.

**Where it resisted.** The third number refused to be different from the
second. I built seven defects, and the one the plain boundary contract was
supposed to miss — a 5.5-hour timezone shift — was also missed by the shape
check that existed to catch it. Two of my three levels were identical, which
would have killed the beat.

The easy exit was to drop the shape level and ship a two-level story: 1 out of
7 versus 6 out of 7, still a strong result.

**What was actually wrong.** The generator, not the claim. My synthetic events
had timestamps spread *uniformly* across the day. Shifting a uniform
distribution round a 24-hour clock gives you back the same uniform
distribution, so there was no shape to move. The check was correct; the world
I had built for it was unrealistically flat. Real payment events have a daily
rhythm — quiet overnight, busy in the afternoon — so I gave the generator one.
The timezone shift then moved the hour-of-day distribution by a total variation
distance of 0.42, and the shape check caught it. 7 of 7.

Worth being precise about what happened, because the two are easy to confuse:
I did not tune the simulation until the result appeared. I made the simulation
*less unrealistic* in a respect that I could justify independently of the
outcome — real transaction data is diurnal, and that is not in dispute. The
earlier version was a bug. It is written up in `FACTCHECK.md` so a reader can
disagree with that judgement if they want to.

**What the library gave back.** Zero new components, same as the other reel
this week. `StageRail` came from the 2026-10-09 weekly report, `CardSet` from
2026-10-16, `FormACard` and `ClaudeBarChart` from elsewhere. Four beats, four
hits, nothing built.

**What I caught looking at frames.** The Short refused GATE V twice over, and
both failures turned out to be one bug wearing two hats. B02 (`StageRail916`,
three stages) filled 51% of the frame; B03 (`ClaudeBarChart916`, three bars)
filled 29%. Both components sized their rows and cards to a *fixed* height, so
the fewer items you gave them the more of a 3840px-tall frame they left empty.
Four stages and seven bars had filled the frame fine in previous weeks, which
is exactly why it had never shown up. Both now scale with the item count, and
four stages land on approximately the old value so no shipped reel changed.

The useful lesson is that it was tempting to read these as two separate
underfilled beats and nudge a `plotScale` on each. That would have left the
library broken for every future chart with a small number of items.

**What this reel found in the library.** Building B03 I went looking for a bar
chart and found `BarChart` — which imports `../tokens/vox`, where the page is
flat white and the "good" colour is plain ink. Every Claude reel that had used
it since 2026-09-18 rendered with no terracotta and no cream, and passed every
gate while doing it, because nothing in the pipeline checks which palette a
component imports. Three published reels, five beats. `ClaudeBarChart` was
built as the replacement, GATE L now carries a palette check, and the gotcha is
logged as A15.

**What is understood now.** Two different bugs this week came from the same
blind spot: the gates check whether a thing rendered, not whether it rendered
*right*. A fixed row height passes. A vox palette passes. Both exit 0. The
palette check added to GATE L closes one of those; the other was closed by
reading frames, which no amount of tooling has yet replaced.

**Still open.** Seven defects is a chosen set, not a sample. A stronger version
of this reel would take a real incident log from a real pipeline and ask what
fraction of it a batch contract would have caught — a much harder claim to
make honestly, and a much better one.
