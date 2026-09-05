# Week 6 video — narration script

**Target:** 3:00 · 441 spoken words
2:56 at 150 words per minute, 3:09 at 140. The script calls for four deliberate pauses, which is
what carries it to a genuine three minutes. Taking the cut in the Notes brings it to ~2:40.

Same pacing as the earlier weeks: steady, unhurried, let the numbers land. Spoken forms are
written out below where they differ from what is on screen. Five figures accompany this script;
the folder README maps each one to its beat.

---

### 0:00 — Opening · on camera

> Hi I'm Om Mali. This video is about the human review queue I built this week — the part of
> the pipeline that knows when to stop and ask a person.
>
> The project turns SEC filings into share prices for private companies like OpenAI, Anthropic
> and SpaceX. The hard part was never the arithmetic. It is working out which company a filing
> is actually talking about, when the same company shows up under dozens of different
> spellings.

*Shot: straight to camera. Keep it moving; the numbers start in twenty seconds.*

---

### 0:25 — What stopped, and what did not · cut to `w6-funnel.png`

> Five thousand eight hundred and six holdings. The matcher resolved four and a half thousand
> of them on its own — seventy-eight percent — off a registered identifier or a name it already
> knew.
>
> On the rest, it refused to guess. Those stopped and waited for me. Nothing was dropped for
> being difficult.

*Shot: hold on the stacked bar. The red segment is the whole point of the week.*

---

### 0:55 — Eight questions, not forty-two · cut to `w6-collapse.png`

> Now look at what stopped. Forty-two cards — but only eight actual questions.
>
> X.AI alone arrives under twenty-four different spellings. X dot A-I Holdings Corp. x dot A-I,
> Inc. Twenty-two more.
>
> Asking twenty-four times whether X.AI belongs in the dataset would be absurd. So the answer
> is recorded against the company, not the spelling. One answer clears all twenty-four — and
> spelling number twenty-five never asks anyone.

*Shot: let the repeated spellings scroll, then land on the bracket.*

---

### 1:30 — Where a paused question lives · cut to `w6-durability.png`

> The other half of this is durability. When the graph stops, it writes its entire state into
> Postgres. The process can exit.
>
> I tested that by pausing in one process and answering in a completely separate one.
>
> Then I got a second test I did not ask for. The database server crashed. When it came back,
> all forty-two questions were still sitting there, exactly as they were.

*Shot: on the fork, then the Postgres box. Pause before "the database server crashed."*

---

### 2:00 — What it caught · cut to `w6-split.png`

> And here is what that bought.
>
> Three price steps looked identical — a price falling by exactly ten. Only one was real.
>
> Perplexity's share count went from six thousand and eighty-one to sixty thousand eight
> hundred and ten, while the dollar value stayed the same to the cent. That is a ten-for-one
> stock split, and it would have entered my price history as a ninety percent crash.
>
> SpaceX's ten-times step is not a split at all. The same fund reports common stock at
> eighty-one dollars and preferred at eight hundred and ten on the same day. And Anthropic's
> jump is an ordinary funding round.
>
> Same shape, three different causes. A detector that treated them alike would be wrong two
> times out of three.

*Shot: three rows, one at a time. Slow down on "to the cent."*

---

### 2:40 — Close · cut to `w6-final.png`, then camera

> Seven commands later, every one of the five thousand eight hundred and six holdings has a
> decision. Each one records who made it and why.
>
> And each one is now a test — so a future change to the matcher cannot quietly overturn a
> judgment I already made.
>
> Next week: turning all of this into an actual price panel.

*Shot: end card.*

---

## Notes

**If you run long,** cut the second paragraph of the opening. The project gets re-explained
every week and this one has plenty to say without it. That buys about twenty seconds.

**Say the Perplexity numbers slowly** — "six thousand and eighty-one to sixty thousand eight
hundred and ten." The whole distinction between a split and a crash lives in the fact that the
dollar value did not move, so the share count has to be heard clearly for the point to land.

**The strongest beat is the crash.** Not the percentages. "The server crashed and the queue
came back whole" is a durability claim that a viewer can feel, and it happened by accident
rather than by test design, which is worth saying out loud.

**Say "X dot A-I", not "ex ay eye".** And say "ten-for-one split", not "ten to one".

**Do not say the matcher is now finished.** Seventy-eight percent is what it resolves unaided;
the other twenty-two percent needed a person, and that is the design working, not a shortfall.

**Do not imply the AI decided anything.** It routed, grouped and presented. Every one of the
forty-five recorded decisions carries a human name and a written reason, and the code rejects a
decision that carries neither. That distinction is the whole argument of the project.

**If anyone asks about the eight questions:** three were suspected splits, three were companies
not yet admitted to the published universe, one was a low-confidence name match, and one was a
company that turned out not to belong at all — 28 holdings of a similarly-named business,
planted as a deliberate canary two months ago. The queue found it without being told to.
