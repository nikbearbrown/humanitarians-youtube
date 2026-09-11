# Week 7 video — narration script

**Target:** 3:00 · 458 spoken words
3:03 at 150 words per minute, 3:16 at 140. The script calls for four deliberate pauses, which is
what carries it to a genuine three minutes. Taking the cut in the Notes brings it to ~2:45.

Same pacing as the earlier weeks: steady, unhurried, let the numbers land. Spoken forms are
written out below where they differ from what is on screen. Five figures accompany this script;
the folder README maps each one to its beat.

---

### 0:00 — Opening · on camera

> Hi I'm Om Mali. This video is about the price panel — turning SEC filings into an actual
> per-share price history for private AI companies, and catching the one thing that would have
> silently ruined it.

*Shot: straight to camera. Short — the numbers start in fifteen seconds.*

---

### 0:20 — The panel · cut to `w7-panel.png`

> The arithmetic is one line. Value divided by share count. Do it once per security, per fund,
> per quarter, and you get five thousand four hundred and seventy-nine marks.
>
> What actually took the week was making every filed row account for itself. Five thousand eight
> hundred and six holdings go in. Twenty-eight were rejected last month. Seventy-two sit on
> filings a later amendment replaced. The remaining five thousand seven hundred and six
> aggregate into marks.
>
> It reconciles exactly. Nothing gets dropped for being awkward.

*Shot: hold on the bar, then the reconciliation legend.*

---

### 0:55 — The window that missed its own test · cut to `w7-tolerance.png`

> Then the split detector, which is the part that matters. A stock split makes a price look like
> a crash.
>
> Perplexity went from six hundred and ninety-five dollars a share to fifty-eight. That is not a
> ninety-two percent collapse. It is a split.
>
> My detector used a window of plus or minus nought point nought two around a whole number.
> Perplexity's ratio is eleven point nine three. That window misses it by a factor of three — and it had looked correct only because the other Perplexity step landed on exactly
> ten.
>
> So the rule is now a relative one percent window. Both the detector and last month's review
> queue import the same one.

*Shot: the number line. Pause on the gap between the grey box and the red line.*

---

### 1:35 — Catching it is not deciding it · cut to `w7-evidence.png`

> But catching a step is not deciding what it is. Three looked like splits, and the ratio
> cannot tell you which.
>
> The share count can.
>
> Perplexity's went from nineteen thousand shares to a hundred and ninety-three thousand while
> the dollar value did not move by a cent. That is a split.
>
> Anthropic held the same eighty-nine thousand shares in all thirteen quarters. Only the value
> moved — and the step reverses the next quarter, which a split never does. SpaceX the same:
> share count constant, value exactly doubled.
>
> Splits move the share count. Repricings move the value. A person made all three calls, with
> the reason written down.

*Shot: one row at a time. Slow down on "did not move by a cent."*

---

### 2:20 — Ratio is not factor · cut to `w7-factor.png`

> One of those is subtler than it looks. That eleven point nine three is not a split factor. It
> is a ten-for-one split and a sixteen percent markdown that landed in the same quarter.
>
> Divide by eleven point nine three and you erase a real price move. Divide by ten and it
> survives.
>
> So the panel records what a person decided to divide by, separate from what the machine
> measured.

*Shot: the three boxes, then the two outcomes.*

---

### 2:45 — Close · cut to `w7-checks.png`, then camera

> The plan listed seven checks for this panel. Six pass. The seventh needs filings the SEC has
> not published, and it says so rather than quietly passing.
>
> One of those checks expected four managers to agree on Anthropic's price. Ten do.
>
> Next week: how often these marks actually move.

*Shot: end card.*

---

## Notes

**If you run long,** cut the last paragraph of the panel beat at 0:20 — "It reconciles exactly"
onwards. The reconciliation is the least visual claim in the script. That buys about fifteen
seconds.

**Say the share counts slowly** at 1:35. "Nineteen thousand to a hundred and ninety-three
thousand, while the dollar value did not move by a cent" is the whole argument of the week, and
it only works if a listener hears both halves.

**The strongest beat is "catching it is not deciding it."** Not the panel size. The detector
found three identical-looking steps and could not tell them apart; a person reading share counts
could. That division of labour is what the project is actually about.

**Say "ten-for-one", not "ten to one".** And "nought point nought two", not "point oh two".

**Do not say the detector was broken.** It worked and it was too narrow — it caught the step that
landed on exactly ten and missed the one at 11.93. "Too narrow to catch its own test case" is
the accurate phrasing and it is on the figure.

**Do not claim the splits are adjusted.** They are detected, quarantined and decided. Applying
the factor is next month's work, and the Perplexity marks are still blocked from every change
series until it happens.

**If anyone asks what a "mark" is:** one fund's recorded price for one security at one quarter
end. Not a valuation of the company — this project publishes what funds wrote down, and nothing
more.
