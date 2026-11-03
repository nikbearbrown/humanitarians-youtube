# Frictional Log — RAG Pipelines, End to End

> Append dated entries as you go; never rewrite an earlier one.

## 2026-09-11 — Build a 60-second explainer on RAG pipelines, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I gave eight points, from why models don't know private files to grounded answers, and expected the five-step pipeline to map neatly onto the beats. I wanted the similarity scores to be real numbers, so they were computed by a small script rather than typed in.

- **Where it resisted, and what I did next:**
  The first draft ran about 84 seconds and had to be cut twice. Some reveals were being cut off until each scene's length was matched to its narration, and the typeset cosine formula took extra work to stay legible. The vertical version needed dedicated portrait layouts for four beats to pass the text-size floor.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes, ran the cosine script, and fixed what the checks and frame reviews found. I accepted softening "answers accurately" to "grounded, and only as good as its retrieval". I changed the greeting to "Hey, Likhith".

- **What I understand now, and what I still do not:**
  I understand that retrieval quality is the real bottleneck: if the right chunk isn't retrieved, the answer can't use it. I haven't tested this on a real document set yet; the vectors in the video are 2-D toys.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
