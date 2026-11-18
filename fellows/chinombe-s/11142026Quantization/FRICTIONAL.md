# Frictional log — Explainer: Quantization In LLMs


## 2026-11-14 — the sixth inference-mechanics explainer

- **Video:** TO FILL
- **Drive:** (https://drive.google.com/drive/u/1/folders/10vBcZC-Pgq_oK_yeLS8QyZZNgFg6lbRK)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** Quantization — how a model's weights get stored in
fewer bits, and what that costs you. Sixth in the series after KV cache, paged
attention, prefill vs decode, speculative decoding and continuous batching.
Eleven beats, about three minutes, 16:9 with a short vertical cut.

**What I tried, and what I expected.**
- I expected this to be the easiest one in the series, because the headline is
  just arithmetic: halve the bits, halve the memory.
- I expected to quote real benchmark figures — the accuracy drop at 8-bit and
  4-bit — since those numbers are everywhere.
- I expected to reuse every component, having built the series' library over
  five previous reels.

**Where it resisted, and what I did next.**
- **The easy part was the easy part, and then the actual topic turned out to
  be outliers.** The memory arithmetic is three lines. Everything interesting
  — why GPTQ, AWQ, GGUF and QLoRA all exist — is downstream of one fact: a
  single huge weight forces the scale factor wide enough to crush every normal
  weight into a few buckets. I reorganised the script around that, so the
  arithmetic is setup and the outlier problem is the turn.
- **I could not honestly cite the numbers I wanted.** There is no source
  document behind this one, unlike the Mycroft reels where I could point at a
  paper or a run log. Quoting "4-bit costs you x% on benchmark y" would mean
  asserting a figure with nothing behind it. The script says "roughly half"
  and "roughly a quarter" instead, and names no benchmark. That is less
  impressive and it is the only version I am willing to publish.
- **A component I had listed as confirmed was not.** B03 was drafted as a bar
  chart, and on inspection `BarChart` is a differently skinned component with
  no Claude-skin equivalent and no `sparkLine` prop at all. My own notes had it
  in the working set; the notes were wrong. Rather than build a new chart for
  one beat, B03 became a `ClaudeCodeBeat` table with the same three numbers.
- **The portrait bug from Sprint 8 was waiting in another component.**
  `MedhavyConceptCard` had a fixed, unwrapped sparkLine and no `*916`
  composition — the exact defect that forced a rebuild last time. Caught it
  before building instead of after, registered `MedhavyConceptCard916`, and
  checked it on an isolated still.
- **The greeting trap.** `ClaudeComposerAsk` silently defaults its greeting to
  a placeholder from someone else's reel if you leave the field unset. Both
  composer beats now set it explicitly.
- **Production friction:** TO FILL — the beat that would not render, a take
  that did not land, anything cut for length.

**What Claude contributed, and what I accepted, changed or rejected.**
- Mine: the research and the diagrams — deciding that the outlier problem is
  the spine of the piece rather than a footnote, and what each beat has to show.
- Claude's: the beat sheet in the series' conventions, the two component fixes,
  and the build notes.
- Accepted: dropping the bar chart rather than authoring a new component for a
  single beat. The series has been built on reuse and one beat is not worth
  breaking that.
- Accepted: fixing the portrait composition before building, having learned
  what skipping that costs.
- Rejected: citing benchmark numbers I cannot source. TO FILL anything else
  you changed.

**What I understand now, and what I still do not.**
- Understood: quantization is not lossy in the way I assumed. The loss is not
  spread evenly across the weights — it concentrates wherever the scale factor
  was stretched by an outlier, which is why the mitigation is always "find the
  outliers and treat them differently" rather than "use more bits".
- Understood, and it connects to the gateway work: this is part of why a cheap
  tier can exist at all. Nine sprints measuring that the cheapest model answers
  as well as the expensive one, and this is the mechanism underneath the price
  difference — with the same shape of conclusion, that the saving is real and
  not free.
- Not understood: where the floor actually is. Everything I can say about
  sub-4-bit is qualitative, because the honest answer is "measure it on your
  own task", which is exactly what the gateway project spent nine sprints doing
  for model choice.
