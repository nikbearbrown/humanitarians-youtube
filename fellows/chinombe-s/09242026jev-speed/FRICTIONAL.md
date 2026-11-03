# Frictional log — Explainer: Why Jev Is Fast

## 2026-09-25 — making "Why Jev Is Fast"

- **Video:** 
- **Drive:** https://drive.google.com/drive/folders/1LYJr3yRnV_77b5HQTvbN21b-z5r7EJEB?usp=sharing
- **Report:** [REPORT.md](REPORT.md)
- **Script:** `SCRIPT-jev-speed.md` in this folder



**What I was working on.** A ~4:20 explainer on why TypeSafe AI's Jev answers a
structured decision in 70–500 ms where a frontier LLM takes seconds, and what
"faster than an LLM" actually means when the two models are doing different
jobs. Twelve beats, B00–B11.

**What I tried, and what I expected.**
- I expected the interesting part to be the headline numbers — 193x faster,
  445x cheaper — and built the first outline around them.
- I expected to have to author new diagram components for the two decoding
  strategies, since I had not drawn a non-autoregressive pass before.
- I expected this to be a straightforward speed comparison.

**Where it resisted, and what I did next.**
- **It is not a speed comparison, and that took a rewrite to see.** Jev does
  structured decisions; an LLM does open-ended work. Measuring Jev's speed
  against a general model on *Jev's own task type* is a category comparison, not
  an apples-to-apples one. That became B08, and it changed what the video is
  about: the mechanism, not the scoreboard.
- **The numbers are single-vendor and I nearly presented them as findings.**
  They come from TypeSafe's own homepage, on TypeSafe's own example task, and the
  company itself says the reported gains likely represent "the high end of
  real-world results." There is no published architecture, no released weights,
  no independent technical paper. Restructured so B05 states them explicitly as
  the company's figures, and B06–B08 do nothing but examine the evidence. The
  build notes mark those three beats **do not cut for time** — at a 4:20 target
  they are the first thing that looks trimmable, and they are the load-bearing
  part.
- **One of my sources is weak and I left it visible rather than dressing it up.**
  Outside observers have guessed Jev may build on an existing open-weight model;
  that is unverified, and I said so on screen instead of implying a confirmed
  architecture. The strongest independent source, Tom's Hardware, stopped at
  "only practical use will tell" — which I quoted rather than paraphrased into
  something firmer.



**What Claude contributed, and what I accepted, changed or rejected.**
- Claude made the video
- I drafted the beat sheet
- I did the diagram props and the vendor-claim structure.
- Accepted: splitting the verdict in B09 into *mechanism* and *magnitude*. The
  mechanism  close the answer space and the autoregressive loop disappears  is
  just how non-autoregressive generation works and needs no vendor's word. The
  magnitude is entirely TypeSafe's claim. Keeping those two apart is the whole
  honesty of the video.
- Source: TypeSafe AI homepage 
- Accepted: searching the existing scene library before authoring anything.


**What I understand now, and what I still do not.**
- Understood: autoregressive decoding is sequential because each token depends on
  the last. If the set of possible answers is small and fixed in advance, there
  is nothing to decode step by step  one forward pass produces the whole typed
  answer. The speed does not come from a better model; it comes from a smaller
  question.
- Understood, and it connects straight to my own project: Mycroft's gateway
  checks answer *shape* after the model has produced it, and I have now found
  two cases where such a check failed a correct answer over formatting  a quoted
  span, a bracket glyph. A closed answer space is the claim that this class of
  bug cannot exist, because the shape is guaranteed rather than inspected. That
  is a much stronger position than validating after the fact, *if* the claim
  holds.
- Not understood: whether the magnitude survives outside the vendor's own
  example task. The mechanism predicts a large gap; nothing published predicts
  193x specifically.
- Not understood: what Jev actually is. Without weights, architecture or a paper,
  "non-autoregressive typed decoder" is a description of behaviour, not of a
  model.