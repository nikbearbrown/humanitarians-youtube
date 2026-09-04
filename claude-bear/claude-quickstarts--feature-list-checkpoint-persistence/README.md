# Persisting Progress Across Context Windows.

An agent working through a long list of features fills its context window, and the
session ends. Watch it come back in a brand-new session and pick up exactly where
it stopped — not because it remembers, but because it rereads a file. Using the real
Anthropic Claude Quickstarts checkpoint pattern as the specimen: `feature_list.json`
holds one entry per feature, marked incomplete or passing; git holds a commit per
finished feature as an immutable ledger. Every new session reads the file, finds the
first incomplete entry, and starts there. A context window is a workspace, not
memory — what carries over is whatever got written down.

**Topic:** AUTONOMOUS CODING · AGENTS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-quickstarts--feature-list-checkpoint-persistence

---

## Chapters

0:00 Does Claude just remember where it left off?
0:11 The session boundary is a wipe
0:24 Two files hold the truth
0:44 The file, across the boundary
1:00 Exactly this far
1:15 Carry-out
1:26 Your turn
1:42 Outro

---

## YOUR TURN

Externalize my agent's progress to a checkpoint file plus git commits, so a
brand-new session can resume exactly where the last one stopped — then prove it
by starting a fresh session and watching it pick up correctly.

Run that today — on any multi-session agent task you already have running.

---

## Deliberately not claimed

Not a claim about how the two-hundred-item feature list gets generated, or what
counts as a passing test — the video states plainly that both are out of scope.
Not a verdict on whether this is the best possible checkpoint design — it states
the mechanism and stops.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
