# Week 5 video — narration script

**Target:** 2:00 · 306 spoken words
2:02 at 150 words per minute, 2:11 at 140. The script calls for three deliberate pauses, so read
straight through it runs ~2:10 — **take the cut in the Notes to land on two minutes flat.**

Same pacing as weeks one, two and four — steady, unhurried, let the numbers land. Spoken forms
are written out below where they differ from what's on screen. This week is a negative result,
so the tone matters more than usual: report it, don't apologise for it.

---

### 0:00 — Opening · on camera

> Week five of the Private AI Valuation Agent.
>
> This week I tried to replace my rule-based matcher with an AI model. It lost. And measuring
> that properly is the whole week.

*Shot: straight to camera. Say "it lost" flatly. No hedge, no smile.*

---

### 0:14 — The test · cut to the setup card

> An eight-billion-parameter model, running locally on my own machine. I gave it exactly what
> the rules get — the name on the filing, the security title, the fund that filed it, and the
> list of candidate companies. Nothing more.
>
> Same three hundred and twenty-two test cases I built last month. Three hundred and twenty-two
> calls. Zero failures.

*Shot: the four inputs listed one at a time. The point is that both systems see the same
evidence — if the model got extra, the comparison would be meaningless.*

---

### 0:42 — The result · cut to the two-row table

> The rules: ninety-nine point six percent precision. The model: ninety-four point five.
>
> Five points sounds survivable. In actual holdings, it turns one wrong record into a hundred
> and ninety-six.

*Shot: hold on the two numbers, then the one-to-one-ninety-six. Pause before the second line.*

---

### 1:00 — How it fails · cut to the three examples

> And it fails the same way every time. It promotes resemblances.
>
> It saw a company called Hyperscale Data, and called it Scale AI — because, it said, Hyperscale
> is Scale AI's parent company. That is not true. It invented a corporate fact.
>
> It saw a loan to a company called Scaled Agile. Also Scale AI.
>
> And it saw this — an internal Fidelity security code — and called it x-A-I, on three matching
> characters.

*Shot: one example per beat. Let the Fidelity code sit on screen alone; it's the one that shows
there was never anything there to find.*

---

### 1:32 — The part that changes next week · back to camera

> Here's what actually matters. The model reported full confidence on three hundred and fifteen
> of its three hundred and twenty-two answers — including twelve of the fifteen it got wrong.
>
> So next week's review queue can't be sorted by how sure the model is. That was the plan.

*Shot: on camera. This is the finding a viewer should carry away.*

---

### 1:52 — The thing I turned off · on camera

> One thing did work. Every mistake was the model *adding* a company. The one time it helped, it
> took one away. So a model allowed only to veto scores perfectly — on four rows. Four.
>
> I built it, measured it, and left it switched off.

*Shot: hold "four" on screen, alone, for a beat.*

---

### 2:08 — Next week

> The plan committed in advance to what happens if there's no lift: keep the rules, and say so.
> So I'm saying so. Next week: the human review queue.

*Shot: end card.*

---

## Notes

**If you run long,** cut the Scaled Agile example at 1:00. Two failures make the point as well as
three, and that buys about twelve seconds.

**Do not apologise for the result.** The plan wrote the rule for this outcome before the model
was ever run — that pre-commitment is the reason the finding is worth anything. A negative result
you decided how to handle in advance is evidence; one you rationalise afterwards is not.

**The strongest beat is the confidence number.** Not the precision gap. "It was completely sure,
and it was wrong" is the sentence a viewer remembers, and it's also the one that constrains the
next month of work.

**Say "x-A-I," not "x-dot-A-I."** And say "internal security code," not "ticker" — it isn't one.

**Don't say the model is useless.** It isn't; it's mis-scoped. It's a decent sceptic and a poor
proposer, which is exactly what the veto result shows. That distinction is the honest version.

**If anyone asks why not a bigger model:** none was tried. The claim is that an eight-billion
model failed at this, not that AI can't do it. A larger one might clear the bar — that's an open
question, and it should be described as one.

**Don't quote the flattering number.** On the subset of hardest cases, every model policy scores
a perfect hundred percent — because that subset excludes the rows where nothing should match, and
those are the only rows the model damages. Quoting it would be true and misleading at once.
