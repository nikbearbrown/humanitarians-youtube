# Frictional Log — Spec-Driven Development

> Append dated entries as you go; never rewrite an earlier one.

## 2026-09-26 — Building a 60-second explainer on spec-driven development, in 16:9 and 9:16

*Written 2026-09-28, after the build; drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I gave seven points I wanted covered, from the vibe-coding hook to the "maintainable at scale" close, with the same 12-beat, one-voice, both-formats setup as the Jev video. I expected this one to go faster, since the pipeline and some scenes from the Jev build could be reused. I also assumed an argument-style topic wouldn't need much sourcing.

- **Where it resisted, and what I did next:**
  The fact-check gate still needed a source for every claim, so the video follows GitHub's own Spec Kit post. The portrait version again had layout problems: two-line titles overlapping content, a chart line poking past the margin, and one overlap that the automatic check missed and was only caught by looking at the frame. Each was fixed and re-checked before the final compile.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet from my points, found and checked the GitHub source, wrote the seven scenes, and fixed the layout issues. I accepted using one login-feature example throughout, so the four advantages connect. I kept the closing chart only as a labelled "qualitative sketch, not data", because I don't have numbers showing spec-driven projects break less.

- **What I understand now, and what I still do not:**
  I understand why treating the spec, not the chat history, as the source of truth makes AI-written code easier to review and hand over. I also learned the visual check is necessary but not enough; someone still has to look at the frames. I don't have evidence yet that this approach reduces breakage in practice, and the AI-voice intro and clean finals are still open.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [sources](SOURCES.md)

## 2026-09-28 — Turning the review cuts into final masters

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I signed off the fact-check and asked for clean final masters in both formats. I expected `./art final` to be a quick re-export of the review cuts I had already checked.

- **Where it resisted, and what I did next:**
  The final is blocked until the type-lock check passes, and it didn't: terracotta text on cream failed the contrast rule, and some small words fell under the size floor, especially in portrait. The fixes were a darker terracotta for text and a few fills, rewording a couple of lines, and bigger sans-serif body text in the vertical cut.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code traced each failure to the exact element, made the fixes, re-rendered, and re-ran the checks until all four cuts passed. I also had it put the AI-narration disclosure on screen, since the fellows guide asks for it. I accepted the slightly darker accent color as the cost of readable text.

- **What I understand now, and what I still do not:**
  Portrait 4K has a much stricter text-size rule than landscape, so I'll design vertical layouts with bigger text from the start. I still need YouTube's 4K processing check and a decision on the "Hi, I am Likhith" line in an AI voice.
