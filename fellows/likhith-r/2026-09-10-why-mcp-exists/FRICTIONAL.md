# Frictional Log — Why MCP Exists

> Append dated entries as you go; never rewrite an earlier one.

## 2026-09-10 — Build a 60-second explainer on why MCP exists, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I gave seven points I wanted covered and expected the API-versus-MCP distinction to be easy to show. I also wanted the discovery step to be real rather than a mock-up, so a toy MCP server and client were run and their actual `tools/list` output went on screen.

- **Where it resisted, and what I did next:**
  The first draft ran 72 seconds, so the narration was trimmed twice without speeding up the audio. The vertical version needed real redesigns, not just resizing: several scenes became grids or rows so the text would stay above the portrait size floor. The final type check also flagged the outro and one bar for contrast, which were fixed.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes, ran the toy server for evidence, and fixed layout problems the checks found. I accepted its corrections that MCP doesn't remove authentication and that someone still writes each server once. The checkout-versus-terminal analogy was my idea, and it stays labelled as an analogy.

- **What I understand now, and what I still do not:**
  I understand that MCP standardises the agent-facing side while the server still does the real API work underneath. I haven't tried a real vendor's MCP server yet, only the toy one used for the evidence.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
