# The Verifier Never Sees Your Thinking. — The Math-Olympiad Skill's Proof Check

Claude's math-olympiad skill checks a problem's reading before it ever
starts solving — competition problems often bury an easy reading next to
the hard one, and in past runs most errors came from solving the wrong
reading entirely. Once the intended reading is settled, eight to twelve
solvers tackle it in parallel, each iterating on its own with no
calculator and no code, reasoning only. Before any proof reaches a
verifier, everything except the finished argument is deleted — every
false start, every scratch note. Fresh verifiers then attack the bare
proof against a checklist of known mistakes, and the vote is asymmetric:
four clean checks confirm it, but just two flagged holes send it back.
Here's why the hiding matters: a verifier that reads a full page of
confident reasoning starts nodding along before it reaches the last line.
Show it only the proof instead, and it has to find the gap on its own.

**Topic:** ADVERSARIAL PROOF CHECK · CLAUDE PLUGINS
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-math-olympiad

---

## Chapters

0:00 The naive framing: "does showing the checker everything work?"
0:10 Read twice, then solve many ways
0:32 Hide the reasoning, then attack the proof
0:57 Why hiding it matters
1:17 Carry-out
1:28 Your turn
1:44 Outro

---

## YOUR TURN

Paste this into Claude: Give me a tricky proof for a claim of your
choosing, but write it in two passes. First, work out the reasoning
however you like. Then hand me only the finished proof, with none of that
reasoning attached, and check it fresh, as if you'd never seen how it was
built. Tell me if the two passes agree.

Run that today, on your own claim, not the video's example.

---

## Deliberately not claimed

No claim about how any other AI system verifies its own reasoning — the
mechanism (interpretation check first, parallel solvers with internal
refinement, the thinking trace stripped before verification, a
pattern-armed adversarial check with an asymmetric vote, calibrated
abstention) is what this particular Claude Code Skill specifies. No claim
that Claude cannot make mistakes; the video states the opposite — the
entire architecture exists because a single unchecked pass can be wrong.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
