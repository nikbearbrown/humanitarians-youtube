# Frictional log — Explainer: PagedAttention

## 2026-09-07 — script written, video published

- **Video:** [Paged Attention Explained: How OS Paging Fixes GPU Memory Waste in LLMs](https://www.youtube.com/watch?v=0rRC3kx5Jd8)
- **Drive:** https://drive.google.com/drive/folders/1CY_suzRRK4f05C5OeNKXm-5Bw6Ynhv1H?usp=sharing
- **Report:** [REPORT.md](REPORT.md)
- **Paired sprint:** [Sprint 3 — task policy, router, frozen test set](../09102026paged-attention/)


**What I was working on.** A STEM deep-dive on PagedAttention: the idea of
applying operating-system paging to the KV cache. Instead of reserving one
contiguous slab per sequence, memory is split into fixed-size blocks, a block
table maps logical blocks to physical ones, and candidates generated from the
same prompt share blocks copy-on-write. Twelve beats, ~4:00, single 16:9 cut,
persona Simba, voice Kokoro `af_bella`.

**What I tried, and what I expected.**
- This one exists because the [KV Cache explainer](../09032026how-kv-cache-works/)
  named PagedAttention as a mitigation and never explained it. I expected to be
  able to pick it up where that script left off.
- I expected to be able to use real figures here, unlike the KV Cache script.

**Where it resisted, and what I did next.**
- **Every number in this one is sourced, and that was the point.** 60–80% memory
  wasted under naive allocation, under 4% waste and 2–4x throughput under
  PagedAttention, a 16-token default block size  all cited in the script's own
  Sources section to Kwon et al., *"Efficient Memory Management for Large
  Language Model Serving with PagedAttention"*, SOSP 2023. The KV Cache script
  stayed qualitative because nothing was measured; this one can be specific
  because someone else measured it and published it. The difference between those
  two positions is the whole of what "provenance" means.
- **Two beats had no component to build on.** B04 and B06 are marked NEW 
  no existing scene covers those diagram shapes, and GATE L and the component
  authoring were explicitly deferred to build time rather than pretended done.
- **No sprint result backs this topic.** It is general LLM-serving mechanics, not
  a Mycroft finding, and the script says so plainly instead of manufacturing a
  connection to that week's engineering work, which was the task policy, the
  router and the frozen fixture set.
- **The build itself is unrecorded.** The video is published and verified, so it
  was made  but whether GATE L was run, whether the two NEW components were
  authored or worked around, and what went wrong on the way are not in any record
  I hold.

**What Claude contributed, and what I did with it.**
- Mine: the research  reading the SOSP paper and working out which of its ideas
  a four-minute explainer can carry  and the diagrams, including the two shapes
  no existing component covered.
- Claude's: the beat sheet in the pipeline's conventions, and the production run
  that produced the published video.
- Not recorded: what happened during that production run, or what either of us
  changed along the way.

**What I understand now, and what I still do not.**
- Understood: the waste under naive allocation is not fragmentation in the
  classic sense  it is reservation. A contiguous slab sized for the longest
  possible output sits mostly empty for most requests, which is why fixed-size
  blocks recover so much.
- Understood: copy-on-write sharing across candidates from one prompt is the same
  trick operating systems use on `fork`, and it is why parallel sampling gets
  cheap rather than linearly more expensive.
- Understood, and it bears on my own project: the strong tier in the gateway is
  capped at 1000 output tokens per minute, and that cap exists because of exactly
  these memory economics. Serving limits are a consequence of allocation
  strategy, not an arbitrary policy.
- Not resolved: how the two NEW beats were eventually drawn, and whether GATE L
  was run before authoring them.
