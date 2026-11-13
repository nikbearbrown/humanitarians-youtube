# FRICTIONAL — You're Only Seeing Half the Curve

*Draft written from the build session. Edit into your own voice before relying
on it; the facts are accurate, the framing is a starting point.*

---

## 2026-10-09 — the week the evidence had to be rebuilt three times

**What I tried and expected.** I picked double descent out of four candidates
because it is the rare result that is both genuinely strange and fully
reproducible on a laptop — no API, no dataset download, no GPU. The pitch was
simple: the bias-variance U-curve that every course draws is the left half of a
longer curve, and past the peak the test error comes back down *below* the
classical best. I expected to write the script, run it once, and start
authoring.

**Where it resisted.** The first experiment produced a spectacular spike at the
interpolation threshold and no second descent worth the name — the right-hand
side drifted back up toward the null model. Worse, the "best classical model" it
reported was the two-parameter one, which was not learning anything at all; the
comparison was meaningless. The second attempt fixed the left half (a genuine U
with a real minimum) and still lost the right half, because the target function
only used the first forty features and every feature past that was noise the
min-norm solution had to absorb.

Only the third construction — sweeping feature bandwidth and label noise
together — produced the textbook shape, and I only trusted it after running it
across twelve seeds. The headline claim survived in all twelve, median 52%
better than the classical optimum, worst seed still 18% better.

**What I accepted, and what I rejected.** I had the option, twice, of writing
narration around what the first two runs showed and describing it in language
vague enough to be defensible. I rejected that. On a video arguing that a
familiar curve is incomplete, shipping an incomplete curve of my own would have
been the same error one level up. `FACTCHECK.md` records all three attempts
rather than presenting the third as if it were the first.

**The thing I would have gotten wrong without reading the source.** The skill
doctrine says that when the misconception in the opening beat lives in a phrase,
put the whole phrase in `triggerWords` — and gives a worked example. The
component it configures matches triggers against single whitespace-delimited
tokens, so a phrase trigger silently never fires and the beat renders with no
correction at all. Nothing errors. No gate catches it. I found it only because I
opened the component instead of trusting `./art scenes --check`, which does not
list those two props at all. Logged as A11, with the contradiction raised in
`open-issues.md` rather than quietly worked around.

**Evidence.** `double_descent_evidence.py` ships in this folder. Pure numpy,
fixed seeds, a few seconds to run. The documentary support is Belkin et al.'s
PNAS paper, quoted verbatim — and the reason that paper rather than a more
recent one is that its experiments use random Fourier features, the same model
family as the script. The reel reproduces the paper's own setup rather than
reaching for an analogy.

**What is understood now.** The expensive discipline is not fact-checking the
narration, it is *running the experiment before the narration exists*. Both
times my evidence contradicted my pitch, the contradiction arrived while the
cost of changing course was a rewritten script — not a re-render, and not a
correction after publishing.

**Still open.** Everything here is a linear model with random features. The
mechanism is general and Nakkiran et al. show the shape in deep networks, but
the threshold there sits at *effective* model complexity, not a parameter count
you can read off an architecture. The reel deliberately quantifies nothing about
deep networks for that reason, and that restraint is the part most likely to be
questioned by someone who has seen the deep-learning plots. It is defensible:
our numbers describe our experiment.
