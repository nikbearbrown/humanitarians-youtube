# Frictional Log — Monorepos vs. Polyrepos

> Append dated entries as you go; never rewrite an earlier one.

## 2026-10-17 — Build a 60-second explainer on monorepos versus polyrepos, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I expected one approach to come out clearly better. I wanted the monorepo benefits on screen to be real, so a toy monorepo was built to show an atomic commit and sparse checkout, and a small script showed build caching.

- **Where it resisted, and what I did next:**
  The first draft ran about 81 seconds and was trimmed twice. The fact-check corrected how I'd used Google as an example, since their monorepo isn't git, and softened "dependencies stay in sync automatically". Portrait titles and counters needed reworking to stop wrapping and collisions.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes and the evidence scripts, checked the claims, and fixed the layout issues. I asked for the exact opening line and the per-format greetings, and accepted the "no universal winner" verdict.

- **What I understand now, and what I still do not:**
  I understand the trade-off is independence versus coordination, and that monorepos need tooling to scale. I haven't tried a remote build cache on a real project.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
