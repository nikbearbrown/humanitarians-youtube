# Frictional Log — Word2Vec: King − Man + Woman ≈ Queen

> Append dated entries as you go; never rewrite an earlier one.

## 2026-11-14 — Build a 60-second explainer on Word2Vec, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I gave eight points, from the analogy to the bias catch, and expected a small skip-gram to reproduce king − man + woman = queen cleanly. I wanted every number on screen to come from that run.

- **Where it resisted, and what I did next:**
  The toy didn't cooperate at first: the first corpus made king and prince identical, and the second still failed the place analogy because the place words sat outside the context window. Both versions are kept. Even the final run shows the catch the video talks about: queen only wins once the input words are excluded. The voice also needed help with "Word2Vec" and "computer programmer", and the type check read two overlapping dots on the map as text, so each dot got a thin ring.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the skip-gram and the scenes, checked the claims against Mikolov et al. 2013, Firth 1957, Bolukbasi et al. 2016 and Nissim et al. 2020, ran the corpus sweep, and fixed the audio and type-check issues. I accepted showing the toy's near-tie honestly and the note that today's models learn their own vectors.

- **What I understand now, and what I still do not:**
  I understand how predicting neighbours turns into geometry, and why the famous analogy needs the inputs excluded. I'm still curious how much of the bias comes from the text versus how the analogy is asked.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
