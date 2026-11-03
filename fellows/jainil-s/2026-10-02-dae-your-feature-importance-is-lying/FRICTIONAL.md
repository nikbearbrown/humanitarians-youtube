# FRICTIONAL — Your Feature Importance Is Lying

*Draft written from the build session. Edit into your own voice before relying
on it; the facts are accurate, the framing is a starting point.*

---

## 2026-10-02 — the reel that had to correct its own pitch

**What I tried and expected.** I asked for something crazy this week. Claude
offered double descent, grokking and model collapse — all genuinely strange,
all well-documented. I passed on those and asked it to re-explain correlated
features, which it had recommended earlier in a description so flat I had
skipped past it.

**The re-explanation is what sold it.** The first pitch said "two correlated
features split the credit between them" — technically true, completely
lifeless. The second pitch led with the consequence: permutation importance
can report near-nothing for a feature that is doing all the work, because
shuffling one copy leaves the model reading the other. That is the same topic
described honestly instead of blandly.

Worth recording: this was the second time Claude undersold a topic it had
recommended, and the second time I had to push back to get the real version.
It named the pattern itself when I pointed it out.

**Where it resisted — and this is the important part.** The sharper pitch
claimed that **both copies report ~zero importance**. I asked for the reel to
be built on that. When Claude actually ran the experiment, it was not true.

With two copies, each scored about 0.58 against a true 1.68 — reduced, not
zero — and the genuinely important feature **still ranked first**. The
dramatic claim did not survive contact with the numbers.

Rather than soften the wording into something vague enough to be defensible,
Claude ran it further and found the real threshold: with **three** copies each
scores about 0.12 while a weaker, unique feature sits at 0.27, and the ranking
genuinely inverts. That is the number the reel uses.

**What I accepted, and what I rejected.** I accepted the corrected figure over
my own pitched framing. I rejected the option of keeping the punchier claim
with a hedge attached — on a video about misleading measurements, an
overstated measurement is not a small problem. `FACTCHECK.md` records the
original claim, why it failed, and what replaced it, rather than quietly
shipping the better version.

**Evidence.** `importance_evidence.py` ships in this folder. Pure numpy, fixed
seed, no scikit-learn needed. Every number on the three bar charts comes out
of it, and anyone can rerun it. The documentary support is scikit-learn's own
warning about correlated features, quoted verbatim — the same
"the-library-indicts-itself" pattern that worked for the temporal-leakage reel.

**What is understood now.** A claim that sounds good in a pitch is a
hypothesis, not a finding. Running the experiment before writing the narration
is what caught this; if the evidence script had been written *after* the
script, the reel would have shipped the wrong number and the code proving it
wrong would have been sitting in the same folder.

**Still open.** The evidence is a linear model. The mechanism is general and
scikit-learn states it generally, but I have not tested how the thresholds
change for tree ensembles, where substitution is more complete and the effect
is probably stronger. The reel makes no tree-specific claim for that reason.
