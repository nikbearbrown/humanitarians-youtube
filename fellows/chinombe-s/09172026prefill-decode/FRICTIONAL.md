# Frictional log — Explainer: Prefill vs Decode


## 2026-09-14 — topic and components exist, script and build not recorded

- **Video:** https://www.youtube.com/watch?v=G-BSNylji68&t=4s
- **Drive:** https://drive.google.com/drive/folders/1dNRtEobtVoOo96AsAAauUyMaR99WWjsT?usp=sharing
- **Report:** [REPORT.md](REPORT.md)
- **Paired sprint:** [Sprint 4 — retry system and first full run](../09172026mycroft-retry/)



**What I was working on.** A STEM explainer on the two phases of LLM inference:
**prefill**, where the entire prompt is processed in one parallel forward pass,
and **decode**, where output tokens are produced one at a time, each conditioned
on the last. Reel slug `hai-prefill-decode`.

**What I tried, and what I expected.**
- I expected the explanation to be mostly about speed, and for the diagrams to
  be the straightforward part  two phases, two pictures.
- I expected the topic to sit alongside the KV cache explainer as background
  rather than connect to that week's project work.

**Where it resisted, and what I did next.**
- **The two phases needed two genuinely different diagram shapes, and neither
  existed.** A sequential loop  last token plus cache in, one pass, next token
  out, repeat  is nothing like a single pass producing many outputs at once.
  Two components were authored for this reel: `AutoregressiveLoop` for the decode
  side and `ParallelPass` for prefill.
  
- **`ParallelPass` turned out to generalise further than intended.** It was drawn
  for prefill specifically, but the shape it encodes  one forward pass, several
  outputs at once  describes any non-autoregressive generation. The Jev
  explainer reuses it for a completely different model's output strategy. That
  is a good outcome and also a small risk: a viewer who learns the component here
  may read "prefill" into it there.
- **The topic turned out to be that week's project blocker, which I did not
  anticipate.** Sprint 4's strong tier failed every call because the configured
  budget of 1024 tokens exceeded the account's cap of **1000 output tokens per
  minute**  a decode-side limit, and the exact thing this explainer describes.
  Caps are written against output tokens because decode is the sequential,
  memory-bound phase; prefill is not billed or limited the same way for the same
  reason.


**What Claude contributed, and what I did with it.**
- Mine: the research and the diagrams  working out the two shapes and what each
  phase had to show.
- Claude's: the beat sheet in the pipeline's conventions, and whatever production
  followed, of which nothing survives in my records.
- Reusable outcome: the two components authored here were later picked up
  unchanged by a different explainer, which is the first time anything in this
  series has been reused rather than rebuilt.

**What I understand now, and what I still do not.**
- Understood: prefill is parallel because every prompt token is already known, so
  the whole sequence goes through in one pass. Decode cannot be, because token
  *n+1* does not exist until token *n* has been chosen. That asymmetry, not model
  size, is why generation is the slow half.
- Understood: it explains the pricing asymmetry this whole project routes around
   output tokens cost several times what input tokens cost  and why the router
  budgets **output** tokens per tier while measuring input in characters.
- Understood: it also explains why Sprint 2's observed cost ratios (1.4x and
  19–26x) diverged so far from the rate card's 2x and 10x. Cost follows how much
  a model decides to say, and saying is decoding.
- Not resolved: whether a script was ever written for this topic, and whether any
  part of the reel was rendered. If a script or a render turns up, this entry
  gets an appended update rather than an edit.
- Not resolved: the exact date inside the 14–18 Sep window.