# Frictional Log — How Coding Agents Navigate Code

> Append dated entries as you go; never rewrite an earlier one.

## 2026-10-15 — Build a 60-second explainer on how coding agents navigate a codebase, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I expected an agent to read the whole codebase and then write a fix. I wanted the steps on screen to be real tool calls and real test output, so the loop was replayed on a small toy repo.

- **Where it resisted, and what I did next:**
  My first draft ran about 73 seconds, and I trimmed it three times. Beat 2's correction didn't fire at first because the component only swaps single words, so I had it rewritten word by word. Several cards collided with the spark line in both formats, and I had them moved.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes and the replay script, checked the claims against Anthropic's docs, and fixed the layout issues. I accepted keeping "largely on its own" rather than "on its own", and the note that the edit style shown is Claude Code's.

- **What I understand now, and what I still do not:**
  I understand that agents work by searching and testing in a loop rather than reading everything. I haven't measured how a real agent behaves on a large repo.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
