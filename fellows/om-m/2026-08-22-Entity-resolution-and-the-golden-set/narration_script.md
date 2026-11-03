# Week 4 video — narration script

**Target:** 2:00 · 271 spoken words
1:48 at 150 words per minute, 1:56 at 140 — the script calls for three deliberate pauses, which
is what brings it to a genuine two minutes. Taking the cut in the Notes brings it to ~1:40.

Same pacing as weeks one and two — steady, unhurried, let the numbers land. Spoken forms are
written out below where they differ from what's on screen. Four figures accompany this script;
the folder README maps each one to its beat.

---

### 0:00 — Opening · on camera

> Week four of the Private AI Valuation Agent.
>
> Seven companies. A hundred and twenty-eight different names. This week I built the thing that
> decides which company a filing is actually talking about — and, more importantly, a way to
> prove whether it works.

*Shot: straight to camera. Keep it tight.*

---

### 0:18 — Why it's hard · cut to a list of spellings

> Databricks shows up under fifty-one different spellings. Anthropic under ten. And they're
> hiding inside three point two million distinct company names.
>
> So I built a ground truth set — three hundred and twenty-two of these strings, covering
> seven thousand holdings — and scored two systems against the same labels.

*Shot: a column of real Databricks spellings scrolling. The repetition is the point.*

---

### 0:42 — The result · cut to the two-row table

> Last month's simple name patterns: ninety-eight percent recall. The new matcher: a hundred
> percent.
>
> Here's one reason. Some funds write x-A-I with a dot in the middle. Some don't. That single
> dot was hiding eighty-five holdings — and the fund hiding behind it was Fidelity, the
> largest holder of that company.

*Shot: hold on the two numbers. Then just the two spellings, side by side.*

---

### 1:08 — The part I got wrong · back to camera

> Now the part I didn't expect.
>
> I'd flagged a holding called OpenAir dot com as *not* one of my companies. I wrote a
> confident reason. I approved my own judgment.
>
> Then I read the actual rows. Five holdings. BlackRock and New York Life. Priced at six
> eighty-seven point six-eight-six-nine — which is OpenAI's Series C price, to four decimal
> places.
>
> It was OpenAI the whole time. My reason had been factually wrong, and my own matcher was
> throwing those five holdings away.

*Shot: on camera for the admission. Then the price, alone on screen. Pause after "the whole
time."*

---

### 1:38 — What that changes · on camera

> So I withdrew the approval, fixed the matcher, and published the worse number next to the
> better one — because a score you measured after fixing what the test caught isn't a
> validation. It's just a score.
>
> Next week: can a language model beat this? And if it can't, I say so.

*Shot: end card.*

---

## Notes

**If you run long,** cut the Databricks-spellings sentence at 0:18. That buys about eight
seconds and the rest still stands on its own.

**Say "six eighty-seven point six-eight-six-nine," slowly.** That number is the entire
argument of the middle section — four decimal places of agreement between two supposedly
different companies. Don't rush it and don't round it.

**The strongest beat is "it was OpenAI the whole time."** Not the precision numbers. A viewer
will not remember ninety-nine point six percent; they will remember that the careful process
caught a confident mistake. Land it, then pause before the next line.

**Do not claim the matcher beat the patterns on precision.** It didn't — on the hardest cases
the old patterns were actually cleaner, because the new matcher wrongly claims a used-car
marketplace whose name happens to contain the words "open" and "A-I." The honest claim is
recall: eighty-five holdings recovered. Say that and nothing more.

**If anyone asks about the threshold:** there isn't one. The used-car company and three
genuine SpaceX investment vehicles all score identically, so no single cut-off separates them.
Four cases per run go to a human instead. That's a feature, and it's next month's work.

**Don't oversell the ground truth set.** Eight of the three hundred and twenty-two labels have
actually been reviewed by a person. The other three hundred and fourteen are the machine's
own work, and one of the eight already turned out wrong — which is the honest reason to keep
checking.
