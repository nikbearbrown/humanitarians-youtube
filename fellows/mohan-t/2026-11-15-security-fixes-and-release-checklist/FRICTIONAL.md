# FRICTIONAL — Timesheet Redesign – Week 3: Security Fixes and the Release Checklist

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned — appended as the work goes, never rewritten.
What an entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-11-18 — Retrospective entry

> **Written 2026-11-18, after the work.** Reconstructed from my weekly notes, the project code and GitHub
> history, and this folder's fact-check — then drafted with Claude from that record. **Sections marked
> `[NOT RECORDED]` are gaps only I can fill.**

**Where it resisted, and what I did next.**

- The second review (17 Nov) found two security issues: an admin could bypass the self-change rule by spelling their ID differently (fixed; 8 spellings tested), and an email change followed by a reset could take over an account (now owner-only for PMs and admins, confirmed for others).
- Also fixed: unsaved edits silently lost on leaving, and a reset limit that was per-server.
- 84/84 and 25/25 pass. PR #16 is not merged and nothing new is live; staging needs Professor Nik's setup.

**What Claude contributed — accepted, changed, rejected.**

- Claude Code helped write the code for this work under my direction; I reviewed and tested the
  changes. `[NOT RECORDED]` — which suggestions I accepted, changed or rejected.
- Claude built this video from my notes using the brutalist.art toolkit and fact-checked each on-screen
  claim against the code and GitHub. I chose the voice, the length and the 1080 format, and kept the
  Your Turn beat after first asking to drop it.

**Understand now / still don't.**

- `[NOT RECORDED]`
