# FRICTIONAL — Lost in the Middle

*Draft written from the build session. Edit into your own voice before relying
on it; the facts are accurate, the framing is a starting point.*

---

## 2026-10-02 — the run where almost nothing broke

**What I tried and expected.** Third week. By now the pattern was set: pick a
concrete mechanical topic, source it properly, build whatever scene component
is missing, check the runtime before rendering. I expected the usual round of
render failures.

**What actually happened.** Nineteen beats, one transient failure that
succeeded on retry, zero content defects, no re-renders. The new scene
component — a U-shaped position curve — rendered correctly first time. Compare
the first week, where the same video needed six separate re-renders to chase a
crash, a layout overflow and a visual artefact.

That is the accumulated fixes paying off rather than anything I did better this
week. Worth noting because it is easy to mistake a smooth run for skill.

**The topic.** Where a fact sits inside a long context changes how reliably it
gets used, and the middle is the weakest position. The finding is published
and peer-reviewed (Liu et al., TACL 2024), so the reel quotes it verbatim —
including the clause that makes it land: "even for explicitly long-context
models." Without that, a viewer assumes a bigger window solves it.

**What I cut.** Every per-model accuracy number in the paper. They are specific
to the models and context lengths tested in 2023–24, and quoting them as
current would misrepresent them. The curve drawn on screen carries a caption
saying the *shape* is the published finding and the values are an illustration.

I also avoided the common paraphrase that models "ignore" the middle. The paper
says performance degrades. Those are different claims and only one of them is
supported.

**Where it resisted.** One beat failed to render while two beats using the same
component succeeded, then worked on retry — almost certainly a browser process
dying under memory pressure at raised concurrency. Not a bug, but worth knowing
the pipeline can fail transiently. It failed loudly, which is the good kind.

**What Claude contributed, and what I accepted.** Claude proposed the topic
after noticing I had twice chosen tangible over sophisticated, and weighted the
list that way — this was recommended and I took it. It sourced the paper, built
the curve component, and flagged that its own earlier time estimate had been
wrong (it predicted ~17 minutes for the previous week's render and it took 59,
because these components are heavier per frame than the ones it benchmarked on).
I accepted the corrected estimate over the optimistic one.

**What is understood now.** The pipeline is in a state where the interesting
work is the content again, not the tooling. That took three weeks and nineteen
recorded fixes.

**Still open.** The reel's four pieces of advice — put key material at the ends,
cut padding, repeat the question, move the passage before blaming the model —
follow from the finding but are not themselves measured. They are labelled as
engineering advice in the factcheck rather than presented as results.
