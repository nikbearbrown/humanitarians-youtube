# FRICTIONAL — Same Prompt, Different Answer

*Draft written from the build session. Edit into your own voice before relying
on it; the facts are accurate, the framing is a starting point.*

---

## 2026-10-16 — the week a source corrected the argument

**What I tried and expected.** This one looked like the easy video of the pair.
Sampling and temperature are well understood, the arithmetic is a softmax, and
the twist — that temperature 0 is not actually deterministic — is a good hook I
already believed. I expected to write it down and render it.

**Where it resisted.** The explanation I was about to give was wrong. I had it
as: *temperature 0 isn't deterministic because floating-point addition isn't
associative.* Checking sources before writing the narration turned up the
flaw — a fixed sequence of operations on the same inputs **is** deterministic.
Non-associativity is the mechanism by which a changed order produces a changed
result. It is not, by itself, a reason for the same request to behave
differently twice.

The actual cause is dynamic batching: your request lands in a differently sized
batch, the kernel splits its reductions differently, and the order changes.
SGLang's documentation states this plainly, so the beat now quotes it and the
narration spends a sentence on the distinction rather than gliding over it.

That is a better video than the one I set out to make. The wrong version would
have been persuasive, quotable, and would have taught a misconception to people
who would then repeat it.

**What I rejected.** Three figures were available and attractive, and none of
them are in the reel. A widely repeated claim that a particular model produced
80 distinct completions in 1,000 runs at temperature 0 — a single secondary
report about a system I have not run. A ~34% throughput cost for deterministic
inference — one benchmark, unreproduced. And my own measurement of how often a
tiny numerical perturbation flips the argmax, which sounded authoritative and
was entirely an artefact of a near-tie I had constructed by hand to make it
happen. That last one was mine, which makes it the one worth remembering.

**What the library gave back.** Three of four body beats came from existing
components. The one that surprised me was `DistributionShape`, built hours
earlier the same day for the model-collapse reel. Its `ghost` prop exists to
show a distribution that has *lost* something; here the identical mechanic
shows one being *reshaped* by temperature. Same visual problem, different
meaning. That is the argument for building generically rather than for the beat
in front of you.

**What is understood now.** The fact-check is not a step after the writing. On
this reel the sources changed what the video argues, not merely how confidently
it argues it — and they could only do that because nothing had been written
yet. Checking afterwards would have produced a defence of the wrong claim
rather than a correction of it.

**Still open.** The reel demonstrates that summation order changes a float
result, and cites documentation for the claim that batching changes that order
in real serving. It does not measure the latter — that would need a GPU, a
server, and a controlled batch-size experiment. Worth doing, and it would make
a stronger follow-up than restating this one.
