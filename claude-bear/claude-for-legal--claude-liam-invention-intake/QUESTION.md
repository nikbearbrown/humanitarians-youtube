# QUESTION.md

**Question:** Can Claude tell me if my invention is patentable?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of Anthropic's
`invention-intake` skill for IP-legal work).

**Name usable:** N/A.

**Source-skill finding — DIFFERENT from the family's usual source-gap (logged plainly):**
the source sheet (`anthropics/claude-for-legal/youtube/claude-liam-invention-intake/beat_sheet.json`)
is fully "built" (7 beats, all VIDEO/filled, dated 2026-07-25) and its narration carries
the same unfilled template placeholders (`>`) the family's other redos hit: `"The skill
is invention-intake. >."`, `"Claude's job: >."`, `SkillTeardownMechanism.body` left as
`">"`, a bare `">"` inside `ClaudeVerdictArtifact.artifactLines`, `"I want to >."`. Its
`source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ip-legal/skills/invention-intake/SKILL.md`
— that exact path does not exist on this machine, BUT the real file exists at the
parallel path `/Users/nik/Documents/Cowork/anthropics/claude-for-legal/ip-legal/skills/invention-intake/SKILL.md`
(22,732 bytes — matches the source sheet's own already-filled `"size": "22k"` in its
`SkillTeardownAnatomy` props, confirming it's the same file). Unlike the `clearance`,
`ai-inventory`, `ai-tool-handoff` siblings, this build used the REAL SKILL.md rather
than reconstructing generically.

**Real facts pulled from the source SKILL.md (all verified against that file):**
- It is "a first-pass screen by a non-specialist, not a patentability opinion." It
  never concludes an invention is patentable — only that it passes the initial screen
  and warrants a prior-art search and registered-practitioner review, needs more
  information, or hits a disqualifier.
- It runs six screens, each producing ✓ / 🟡 / 🔴: novelty signals, obviousness flags,
  § 101 subject-matter eligibility, public disclosure / bar dates, detectability
  (patent vs. trade secret), and strategic value against the firm's filing strategy.
- The bottom line is always one of three words: **PURSUE** (schedule a prior-art
  search and attorney review), **INVESTIGATE** (needs a specific open item resolved),
  or **DECLINE** (a concrete, stated reason — never "not patentable").
- Hard guardrail, stated explicitly in the file: "Never say patentable." A prior-art
  search is a separate step this skill does not perform.
- Worked example in the file's own `## Examples` section: "a new cache-eviction
  algorithm that uses a learned model rather than LRU; conceived Q1 this year, not yet
  disclosed, engineering prototype in internal staging" — reused as this build's
  handoff-prompt anchor (BHTF).

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/claude-for-legal/youtube/claude-liam-invention-intake/beat_sheet.json`
(7-beat Teardown skill-teardown, register "Teardown"). Shape and beat count are locked
from that source; this build re-registers the narration to Plain, replaces the cold
open with BrutalistHesitantWriter, reskins the close to Humanitarians AI, and — because
the real source SKILL.md was actually found — fills every fact-shaped beat with the
skill's own stated behavior instead of a generic reconstruction.
